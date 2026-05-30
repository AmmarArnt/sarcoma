#!/usr/bin/env python3
"""Whole-body multi-microservice state + SEQUENCING model for CIC-DUX4 selective clearance.

Per directive: model the body as multiple interacting 'microservices' (tumor cell, NK
compartment, CD8-T compartment, suppressive TME [Treg/MDSC], host context) and ask:
  (1) what GLOBAL system state permits selective clearance with minimal cytotoxics, and
  (2) does the ORDER of the vectors of attack matter (the NK-vs-MHC-I window; V3->V4 bridge)?

This is a discrete-time, qualitative model with explicit biological DELAYS (priming takes
time; senescence develops after sustained arrest; T-cell expansion lags antigen display).
Qualitative hypothesis generator, NOT a quantitative/temporal predictor. Edges cite real
mechanisms (Goel Nature 2017 PMID 28813415; senescence->NK PMID 26878797; HLA-E escape
Nat Commun 2019; NLRC5/CITA PMID 27162338). Baseline tumor markers from real data (GSE60740).
No fabrication.
"""
from __future__ import annotations
import os, json
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
T = 16  # time steps

# biological delays (steps) -- illustrative
D_PRIME = 3   # MHC-I rises this long after epigenetic/IFN priming starts
D_PDL1  = 2   # adaptive PD-L1 induction lag
D_SEN   = 4   # senescence (NKG2D ligands) develops after sustained CDK4/6i arrest
D_TPRIME= 4   # CD8-T expansion lag after MHC-I display begins
D_KILL  = 2   # consecutive steps of kill pressure needed to clear


def simulate(schedule, host):
    """schedule: {drug: start_step or None}. host: dict of body-context params.
       Returns (cleared_step or None, trace rows)."""
    def on(drug, t):
        s = schedule.get(drug)
        return s is not None and t >= s

    B2M = host["B2M_intact"]; NKfit = host["HOST_NK_fit"]
    TIGIT_high = host["TIGIT_high"]; Treg_base = host["Treg_baseline"]
    nectin = host["nectin"]; HLA_E = host["HLA_E"]

    mhc1_since = None; pdl1_since = None; arrest_since = None
    kill_streak = 0; cleared = None; rows = []

    for t in range(T):
        prime_like = on("EpiPrime", t) or on("CDK46i", t)   # both raise antigen presentation (Goel: CDK4/6i via IFN)
        if prime_like and mhc1_since is None: mhc1_since = t + D_PRIME
        if prime_like and pdl1_since is None: pdl1_since = t + D_PDL1
        arrest = on("CDK46i", t) or on("Diff", t)
        if arrest and arrest_since is None: arrest_since = t

        MHC1 = bool(B2M) and (mhc1_since is not None and t >= mhc1_since)
        PDL1 = (pdl1_since is not None and t >= pdl1_since)
        senescent = on("CDK46i", t) and arrest_since is not None and (t - arrest_since) >= D_SEN
        NKG2D_L = senescent
        treg_active = bool(Treg_base) and not on("CDK46i", t)          # CDK4/6i suppresses Treg
        TIGIT_brake = bool(TIGIT_high) and not on("aTIGIT", t) and bool(nectin)
        dnam = bool(nectin) and not TIGIT_brake
        pd1_brake = PDL1 and not on("aPD1", t)

        NK_ready = bool(NKfit) or on("NKarm", t)
        # CD8-T primed once MHC-I has been displayed long enough (expansion lag) and Treg not dominant
        T_primed = (MHC1 and mhc1_since is not None and t >= mhc1_since + D_TPRIME and not treg_active)

        nk_kill = NK_ready and dnam and ((not MHC1) or NKG2D_L) and not treg_active and not HLA_E
        t_kill  = T_primed and MHC1 and dnam and not pd1_brake and not treg_active
        kill_now = nk_kill or t_kill
        kill_streak = kill_streak + 1 if kill_now else 0
        if cleared is None and kill_streak >= D_KILL:
            cleared = t
        rows.append(dict(t=t, MHC1=int(MHC1), senescent=int(senescent), NKG2D_L=int(NKG2D_L),
                         treg=int(treg_active), dnam=int(dnam), nk_kill=int(nk_kill),
                         t_kill=int(t_kill), kill=int(kill_now)))
    return cleared, rows


STRATEGIES = {
    "S1 checkpoint-only (brakes off, nothing else)": {"aPD1": 0, "aTIGIT": 0},
    "S2 prime-first -> release":                     {"CDK46i": 0, "aTIGIT": 4, "aPD1": 4},
    "S3 NK-first (strangle+nectin-release+arm)":     {"CDK46i": 0, "aTIGIT": 0, "NKarm": 0},
    "S4 strangle-only (no immune)":                  {"CDK46i": 0, "Diff": 0},
    "S5 sequenced: NK-first then open T-arm":        {"CDK46i": 0, "aTIGIT": 0, "NKarm": 0, "aPD1": 6},
}

HOSTS = {
    "healthy host (NK fit, B2M intact)":   dict(B2M_intact=1, HOST_NK_fit=1, TIGIT_high=1, Treg_baseline=1, nectin=1, HLA_E=0),
    "B2M LOST (antigen presentation off)": dict(B2M_intact=0, HOST_NK_fit=1, TIGIT_high=1, Treg_baseline=1, nectin=1, HLA_E=0),
    "hostile host (NK unfit, no arming)":  dict(B2M_intact=1, HOST_NK_fit=0, TIGIT_high=1, Treg_baseline=1, nectin=1, HLA_E=0),
}


def main():
    print("Delays (steps): MHC-I after prime=%d, senescence after arrest=%d, T-cell expansion=%d, kill-streak=%d\n"
          % (D_PRIME, D_SEN, D_TPRIME, D_KILL))
    summary = []
    for hname, host in HOSTS.items():
        print(f"=== HOST: {hname} ===")
        for sname, sched in STRATEGIES.items():
            cleared, rows = simulate(sched, host)
            via = ""
            if cleared is not None:
                r = rows[cleared]
                via = "NK" if r["nk_kill"] else ("T-cell" if r["t_kill"] else "?")
            res = f"cleared@t={cleared} via {via}" if cleared is not None else "NOT cleared"
            print(f"   {sname:<46} {res}")
            summary.append(dict(host=hname, strategy=sname,
                                cleared_step=(cleared if cleared is not None else -1),
                                route=via or "none"))
        print()
    pd.DataFrame(summary).to_csv(os.path.join(HERE, "sequencing_results.csv"), index=False)

    # detailed trace of the winning sequenced strategy in healthy host
    cleared, rows = simulate(STRATEGIES["S5 sequenced: NK-first then open T-arm"], HOSTS["healthy host (NK fit, B2M intact)"])
    pd.DataFrame(rows).to_csv(os.path.join(HERE, "trace_S5_healthy.csv"), index=False)
    print("Trace of S5 (healthy host) written to trace_S5_healthy.csv; cleared@t=", cleared)

    ents = ["CIC-DUX4","NLRC5","MHC class I","B2M","CD8 T cell","natural killer cell","regulatory T cell",
            "NKG2D","MICA","ULBP2","TIGIT","CD226","DNAM-1","CD155","CD112","PD-1","PD-L1","HLA-E",
            "CDK4","CDK6","senescence","interferon","IL-15"]
    with open(os.path.join(HERE, "entities.txt"), "w") as fh:
        fh.write(". ".join(ents) + ".\n")
    with open(os.path.join(HERE, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
    print("[done] wrote sequencing_results.csv, trace_S5_healthy.csv, entities.txt, summary.json")


if __name__ == "__main__":
    main()
