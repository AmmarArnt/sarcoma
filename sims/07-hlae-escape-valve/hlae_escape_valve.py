#!/usr/bin/env python3
"""Sim 07 — HLA-E / NKG2A escape valve of epigenetic MHC-I restoration (V4 Forward Hypothesis 3).

EXTENDS sims/04-immune-state-model/immune_state_model.py. Sim 04 treats HLA-E as a STATIC
favorable parameter (HLA_E=0), so it structurally cannot represent FH-3:

    "EZH2i/HDACi restore *classical* MHC-I but may CO-INDUCE HLA-E, re-suppressing both the NK
     arm relied on earlier AND the new CD8 arm (via CD94/NKG2A) — so pair MHC-I restoration with
     anti-NKG2A (monalizumab), not anti-PD-1 alone."   (protocol-v2.md FH-3; v4-summary-v2.md)

This sim makes HLA-E a DYNAMIC node coupled to MHC-I restoration, adds an anti-NKG2A drug, and
applies the HLA-E/NKG2A brake to BOTH the NK and the CD8 effector arms. It then asks three
falsifiable questions:
  Q1 (parity)        : with coupling OFF and no anti-NKG2A, does it reproduce Sim 04 exactly?
  Q2 (escape valve)  : with coupling ON, do EpiPrime->MHC-I->T-cell routes self-block, and is
                       anti-NKG2A required to recover clearance? (=> is monalizumab load-bearing?)
  Q3 (sequencing)    : under coupling, does NK-FIRST (act while HLA-E still low) beat
                       MHC-I-restoration-first (which raises its own brake)? (links Sim 05)

MECHANISTIC BASIS FOR THE NEW COUPLING EDGE (real biology; tiered honestly):
  - HLA-E surface expression REQUIRES VL9 leader peptides derived from classical HLA-A/-B/-C/-G
    signal sequences; VL9 stabilizes HLA-E at the plasma membrane. Restoring classical MHC-I
    therefore SUPPLIES HLA-E's stabilizing ligand. [Established — general immunology]
      Braud et al., Nature 1998 (HLA-E binds CD94/NKG2A), https://www.nature.com/articles/35869
      VL9 leader-peptide dependence reviewed: PMC10690437; NKG2A:HLA-E review PMC11254306.
  - IFN-gamma transcriptionally upregulates HLA-E (a documented NK-resistance route, e.g. HLA-E/
    NKG2A resistance to BCG in NMIBC). [Clinical-correlative] PMC11398371.
  - anti-NKG2A (monalizumab-class) disrupts the NKG2A:HLA-E inhibitory interaction. [Clinical-Trial]
      review PMC11254306.
  - THE SPECIFIC CLAIM "EZH2i co-induces HLA-E in CIC-DUX4" is NOT established. It is INFERRED
    (Mechanistic / Theoretical) from (a) HLA-E's dependence on classical-MHC-I leader peptides and
    (b) IFN-inducibility of HLA-E. Tagged as a hypothesis edge, exactly as FH-3 states
    ("HLA-E response to epigenetic therapy uncharacterized in this disease").

Qualitative Boolean hypothesis generator, NOT a quantitative predictor. No fabrication: every
edge cites a real mechanism; the one inferred edge is labelled. Baseline CIC-DUX4 cell-state is
inherited unchanged from Sim 04 (anchored to GSE60740 / Sim 01: fusion ON => MHC-I/B2M/NLRC5 low,
HLA-E low, CD112/nectin up).
"""
from __future__ import annotations
import itertools, json, os, importlib.util
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
SIM04 = os.path.normpath(os.path.join(HERE, "..", "04-immune-state-model", "immune_state_model.py"))

# ---------- load Sim 04 as the baseline reference (for the parity check) ----------
def _load_sim04():
    spec = importlib.util.spec_from_file_location("sim04_immune", SIM04)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# ---------- parameters: Sim 04's context + the FH-3 coupling toggle ----------
DEFAULT_PARAMS = dict(
    Fusion=1,          # CIC-DUX4 driver present
    B2M_intact=1,      # 0 = genetic B2M loss (no surface MHC-I AND no surface HLA-E)
    Treg_high=1,       # immunosuppressive TME baseline
    TIGIT_high=1,      # nectin ligands engage TIGIT brake
    DNAM1L=1,          # CD155/CD112 nectin present (data: CD112 up)
    HLA_E=0,           # BASELINE HLA-E low per CIC-DUX4 data (Sim 04)
    Teff_present=1,
    NKeff_present=1,
    HLAE_coupling=1,   # *** FH-3 hypothesis edge: MHC-I restoration / IFN co-induces HLA-E ***
)

# Two candidates added vs Sim 04's pool:
#   aNKG2A  = monalizumab-class anti-NKG2A (blocks the HLA-E/NKG2A brake; the FH-3 fix).
#   Tdeplete= Treg-depletion lever INDEPENDENT of CDK4/6i (metronomic low-dose cyclophosphamide;
#             anti-CTLA-4 intratumoral Treg depletion). Sim 04 hard-wired Treg relief to CDK4/6i,
#             but CDK4/6i also drives IFN -> HLA-E under coupling, so without an IFN-free Treg lever
#             a "stay-HLA-E-low" NK-first route cannot be represented at all. [grounded: Ghiringhelli
#             metronomic-CTX Treg depletion; anti-CTLA-4 Treg depletion]
NONCYTO = ["EpiPrime", "CDK46i", "Diff", "BETi", "aPD1", "aTIGIT", "NKarm", "aNKG2A", "Tdeplete"]
ALL_DRUGS = NONCYTO + ["DNAdamage"]

READOUTS = ["Prolif", "MHCI", "HLA_E_surface", "NKG2A_brake", "NKG2D_L", "DNAM_active",
            "Tcell_kill", "NK_kill", "ImmuneKill", "Senescent", "Cleared", "TargetState"]


def evaluate(params, drugs):
    """Extended single-pass evaluation. Identical to Sim 04 EXCEPT for the HLA-E coupling block
    and the HLA-E/NKG2A brake now applied to BOTH effector arms."""
    g = dict(params)
    D = {k: (k in drugs) for k in ALL_DRUGS}

    # --- cell-intrinsic oncogenic loop / strangler axis (UNCHANGED from Sim 04) ---
    BRD4   = not D["BETi"]
    ETV    = bool(g["Fusion"])
    SE     = ETV and BRD4
    Drive  = SE
    p21    = D["Diff"]
    CDK46  = Drive and not p21 and not D["CDK46i"]
    RBact  = not CDK46
    E2F    = not RBact
    Prolif = E2F and Drive and not D["Diff"]
    Senescent = D["CDK46i"] and not Prolif

    # --- innate stress / interferon context (UNCHANGED) ---
    STING = D["DNAdamage"] or Senescent
    IFN   = D["CDK46i"] or STING or D["DNAdamage"]
    NKG2D_L = Senescent

    # --- antigen-presentation / visibility (UNCHANGED) ---
    NLRC5 = D["EpiPrime"] or IFN
    MHCI  = NLRC5 and bool(g["B2M_intact"])
    PDL1  = IFN

    # === NEW (FH-3): HLA-E as a DYNAMIC node ============================================
    # HLA-E reaches the surface only as an MHC-I molecule (needs B2M) AND needs a VL9 leader
    # peptide that comes from classical HLA-A/B/C  -> restoring classical MHC-I supplies it;
    # IFN additionally transcribes HLA-E. Under the coupling hypothesis, the very act of
    # restoring classical MHC-I (or driving IFN) raises HLA-E.
    coupling = bool(g["HLAE_coupling"])
    HLA_E_surface = (
        bool(g["HLA_E"])                                   # any constitutive HLA-E
        or (coupling and bool(g["B2M_intact"]) and (MHCI or IFN))
    )
    # anti-NKG2A (monalizumab) blocks the receptor side of the brake regardless of HLA-E level.
    NKG2A_brake = HLA_E_surface and not D["aNKG2A"]
    # ===================================================================================

    # --- nectin / DNAM-1 - TIGIT axis (UNCHANGED) ---
    TIGIT_brake = bool(g["TIGIT_high"]) and not D["aTIGIT"] and bool(g["DNAM1L"])
    DNAM_active = bool(g["DNAM1L"]) and not TIGIT_brake

    # --- other brakes. CHANGE vs Sim 04: Treg relief now also via an IFN-free depletion lever ---
    PD1_brake   = PDL1 and not D["aPD1"]
    Treg_active = bool(g["Treg_high"]) and not D["CDK46i"] and not D["Tdeplete"]

    # --- effectors. CHANGE vs Sim 04: NKG2A_brake now gates BOTH NK and CD8 (NKG2A is on both) ---
    NKeff = bool(g["NKeff_present"]) or D["NKarm"]
    Tcell_kill = (MHCI and bool(g["Teff_present"]) and DNAM_active
                  and not PD1_brake and not Treg_active
                  and not NKG2A_brake)                      # <-- NEW brake on CD8 arm
    NK_kill = (NKeff and DNAM_active and (not MHCI or NKG2D_L)
               and not NKG2A_brake and not Treg_active)     # was 'HLA_E' static; now dynamic

    ImmuneKill = Tcell_kill or NK_kill
    Cleared = ImmuneKill
    TargetState = Cleared and not Prolif

    return dict(Prolif=Prolif, MHCI=MHCI, HLA_E_surface=HLA_E_surface, NKG2A_brake=NKG2A_brake,
                NKG2D_L=NKG2D_L, DNAM_active=DNAM_active, Tcell_kill=Tcell_kill, NK_kill=NK_kill,
                ImmuneKill=ImmuneKill, Senescent=Senescent, Cleared=Cleared, TargetState=TargetState)


def scan(params, pool):
    rows = []
    for r in range(0, len(pool) + 1):
        for combo in itertools.combinations(pool, r):
            out = evaluate(params, set(combo))
            rows.append({"intervention": "+".join(combo) or "none", "n": r,
                         **{k: int(v) for k, v in out.items()}})
    return pd.DataFrame(rows)


def minimal_hits(df):
    hits = df[df["TargetState"] == 1].copy()
    if hits.empty:
        return hits
    return hits[hits["n"] == hits["n"].min()].sort_values("intervention")


def main():
    base = DEFAULT_PARAMS

    # ---------------- Q1: PARITY with Sim 04 (coupling OFF, no anti-NKG2A) ----------------
    print("=== Q1  PARITY CHECK vs Sim 04 (HLAE_coupling=0, drop aNKG2A from pool) ===")
    sim04 = _load_sim04()
    p_off = dict(base); p_off["HLAE_coupling"] = 0
    pool04 = [d for d in NONCYTO if d not in ("aNKG2A", "Tdeplete")]   # match Sim 04's exact pool
    parity_ok = True
    for r in range(0, len(pool04) + 1):
        for combo in itertools.combinations(pool04, r):
            a = sim04.evaluate(sim04.DEFAULT_PARAMS, set(combo))
            b = evaluate(p_off, set(combo))
            for k in ("Prolif", "MHCI", "Tcell_kill", "NK_kill", "Cleared", "TargetState"):
                if int(a[k]) != int(b[k]):
                    parity_ok = False
                    print(f"   MISMATCH {('+'.join(combo)) or 'none'} {k}: sim04={a[k]} sim07={b[k]}")
    print(f"   parity (key readouts identical across all {2**len(pool04)} combos): "
          f"{'PASS' if parity_ok else 'FAIL'}")

    # ---------------- Q2: ESCAPE VALVE (coupling ON) ----------------
    print("\n=== Q2  HLA-E ESCAPE VALVE (HLAE_coupling=1) ===")
    df_on  = scan(base, NONCYTO)
    df_off = scan(p_off, NONCYTO)
    df_on.to_csv(os.path.join(HERE, "scan_coupling_on.csv"), index=False)
    df_off.to_csv(os.path.join(HERE, "scan_coupling_off.csv"), index=False)

    n_on  = int((df_on.TargetState == 1).sum())
    n_off = int((df_off.TargetState == 1).sum())
    print(f"   TargetState-reaching combos: coupling OFF = {n_off} / {len(df_off)} ;"
          f"  coupling ON = {n_on} / {len(df_on)}   (lost {n_off - n_on} routes to the brake)")

    hits_on = df_on[df_on.TargetState == 1]
    need_nkg2a = hits_on[hits_on.intervention.str.contains("aNKG2A")]
    free_nkg2a = hits_on[~hits_on.intervention.str.contains("aNKG2A")]
    print(f"   of the {n_on} surviving routes under coupling, {len(need_nkg2a)} contain anti-NKG2A "
          f"({100*len(need_nkg2a)/max(n_on,1):.0f}%)")
    # the anti-NKG2A-FREE survivors should be exactly the 'stay-cold' family: no MHC-I restoration,
    # no IFN inducer -> HLA-E never surfaces -> NK missing-self works without monalizumab.
    free_induce_mhci = free_nkg2a.intervention.str.contains("EpiPrime|CDK46i|DNAdamage").any()
    print(f"   anti-NKG2A-FREE survivors = {len(free_nkg2a)} ; any of them restore MHC-I / induce IFN? "
          f"{bool(free_induce_mhci)}  (expect False — these are pure 'stay-cold' NK routes)")

    def tag_of(o):
        if o["TargetState"]:
            return "TARGET-STATE (arrested + cleared)"
        if o["NKG2A_brake"]:
            return "BLOCKED by HLA-E/NKG2A (no kill)"
        if o["ImmuneKill"]:
            return "killed but still cycling (add cytostatic for TargetState)"
        return "not cleared"

    # The specific FH-3 claim: EpiPrime-driven T-cell route self-blocks; aNKG2A rescues it.
    # Treg handled by the IFN-free Tdeplete lever so HLA-E is isolated as the decisive variable.
    print("\n   --- the EpiPrime (MHC-I restoration) route, dissected (Treg handled via Tdeplete) ---")
    for combo in [("EpiPrime", "aPD1", "aTIGIT", "Tdeplete"),
                  ("EpiPrime", "aPD1", "aTIGIT", "Tdeplete", "aNKG2A"),
                  ("EpiPrime", "aPD1", "aTIGIT", "CDK46i", "aNKG2A")]:
        o = evaluate(base, set(combo))
        print(f"     {'+'.join(combo):<42} MHCI={o['MHCI']} HLA_E={o['HLA_E_surface']} "
              f"NKG2A_brake={o['NKG2A_brake']} Tkill={o['Tcell_kill']} NKkill={o['NK_kill']} "
              f"-> {tag_of(o)}")

    # ---------------- Q3: SEQUENCING — NK-first vs MHC-I-restoration-first ----------------
    print("\n=== Q3  SEQUENCING under coupling: NK-first vs restoration-first ===")
    seqs = {
        "NK-first, stay HLA-E-low (aTIGIT+NKarm+Tdeplete)": ("aTIGIT", "NKarm", "Tdeplete"),
        "NK-first + CDK4/6i (senescence, but IFN->HLA-E)": ("aTIGIT", "NKarm", "Tdeplete", "CDK46i"),
        "Restoration-first (EpiPrime, no anti-NKG2A)": ("EpiPrime", "aPD1", "aTIGIT", "Tdeplete"),
        "Restoration-first + anti-NKG2A (FH-3 fix)": ("EpiPrime", "aPD1", "aTIGIT", "Tdeplete", "aNKG2A"),
    }
    print("   (readout = does the immune effector ENGAGE? add an IFN-free cytostatic for full TargetState)")
    for label, combo in seqs.items():
        o = evaluate(base, set(combo))
        print(f"   {label:<48} HLA_E={int(o['HLA_E_surface'])} brake={int(o['NKG2A_brake'])} "
              f"ImmuneKill={int(o['ImmuneKill'])} via "
              + ("NK" if o["NK_kill"] else ("T-cell" if o["Tcell_kill"] else "none")))

    # ---------------- B2M-loss contrast: escape valve should DISAPPEAR ----------------
    print("\n=== Contrast: B2M LOST under coupling (no surface MHC-I => no VL9 => HLA-E can't surface) ===")
    p_b2m = dict(base); p_b2m["B2M_intact"] = 0
    df_b2m = scan(p_b2m, NONCYTO)
    df_b2m.to_csv(os.path.join(HERE, "scan_b2mlost_coupling_on.csv"), index=False)
    mh_b2m = minimal_hits(df_b2m)
    any_brake = int((df_b2m.NKG2A_brake == 1).sum())
    print(f"   combos with an active NKG2A brake under B2M loss: {any_brake} (expected 0 — no VL9 source)")
    print(f"   minimal clearing combos (NK missing-self route): "
          f"{mh_b2m.intervention.tolist()[:6]}")

    # ---------------- outputs for grounding / provenance ----------------
    summary = dict(
        parity_pass=bool(parity_ok),
        targetstate_coupling_off=n_off,
        targetstate_coupling_on=n_on,
        routes_lost_to_brake=n_off - n_on,
        surviving_routes_with_aNKG2A=int(len(need_nkg2a)),
        surviving_routes_total=n_on,
        b2mloss_active_brakes=any_brake,
    )
    with open(os.path.join(HERE, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)

    ents = ["CIC-DUX4", "HLA-E", "NKG2A", "KLRC1", "CD94", "KLRD1", "monalizumab", "NLRC5",
            "HLA-A", "HLA-B", "HLA-C", "B2M", "TAP1", "EZH2", "H3K27me3", "interferon gamma",
            "PD-L1", "CD274", "PVR", "CD155", "TIGIT", "CD226", "DNAM-1", "MICA", "ULBP2",
            "CDK4", "CDK6", "natural killer cell", "CD8 T cell", "senescence", "VL9 peptide"]
    with open(os.path.join(HERE, "entities.txt"), "w") as fh:
        fh.write(". ".join(ents) + ".\n")
    print("\n[done] wrote scan_coupling_on.csv, scan_coupling_off.csv, "
          "scan_b2mlost_coupling_on.csv, summary.json, entities.txt")


if __name__ == "__main__":
    main()
