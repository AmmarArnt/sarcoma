#!/usr/bin/env python3
"""Boolean model of the CIC-DUX4 oncogenic loop + intervention scan with SENSITIVITY ANALYSIS.

Qualitative hypothesis generator, NOT a quantitative predictor. Every edge traces to
docs/02-cic-sarcoma-knowledge.md / docs/05-attack-vectors.md or a cited mechanism;
edges that are modeling assumptions are labelled ASSUMPTION below and in RESULTS.md.

Two assumptions are toggled to test robustness of conclusions:
  - FB  : BRD4-independent escape (BRD4 reaccumulation / kinase rewiring) — documented BETi resistance.
  - CCNE: cyclin E / CDK2 bypass of CDK4/6 — documented CDK4/6i resistance.
A conclusion is ROBUST if it holds across all four on/off combinations of these assumptions.

Readouts: Proliferation; Viability = Prolif AND not (Damage AND WEE1-checkpoint-lost).
"""
from __future__ import annotations
import itertools, json, os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ON = {"BRD4", "WEE1"}
INPUTS = {"IGF1R_in", "Fusion", "Damage"}
DRUG_CLAMP = {
    "BETi":   {"BRD4": 0}, "CDK46i": {"CDK4": 0}, "WEE1i": {"WEE1": 0},
    "MEKi":   {"MEK": 0},  "IGF1Ri": {"IGF1R_in": 0},
}


def build_wiring(fb: bool, ccne: bool):
    drive = "SE or FB" if fb else "SE"
    rb = "not (CDK4 or CDK2)" if ccne else "not CDK4"
    return {
        "RAS":  "IGF1R_in",
        "MEK":  "RAS",
        "ERK":  "MEK and not DUSP",
        "DUSP": "ERK",
        "CIC":  "not ERK",
        "ETV":  "Fusion or (not CIC)",
        "SE":   "ETV and BRD4",
        "FB":   "ETV and (not BRD4)",          # ASSUMPTION (only used if fb)
        "D":    drive,
        "CCND": "D",
        "CDK4": "CCND",
        "CCNE": "E2F or D",                      # ASSUMPTION arm (only used if ccne)
        "CDK2": "CCNE",
        "RB":   rb,
        "E2F":  "not RB",
        "Prolif": "E2F and D",
        "Viab": "Prolif and not (Damage and not WEE1)",
    }


def step(s, wiring, clamp):
    n = dict(s)
    for node, rule in wiring.items():
        n[node] = bool(eval(rule, {}, s))
    for node in DEFAULT_ON:
        n[node] = s.get(node, True)
    for node in INPUTS:
        n[node] = s.get(node, False)
    for node, val in clamp.items():
        n[node] = bool(val)
    return n


def attractor(wiring, inputs, clamp, max_steps=80):
    nodes = list(wiring) + sorted(DEFAULT_ON) + sorted(INPUTS)
    s = {k: False for k in nodes}
    for k in DEFAULT_ON: s[k] = True
    for k, v in {**inputs, **clamp}.items(): s[k] = bool(v)
    hist = []
    for _ in range(max_steps):
        key = tuple(sorted(s.items()))
        if key in hist:
            return hist[hist.index(key):]
        hist.append(key)
        s = step(s, wiring, clamp)
    return hist[-1:]


def readout(cycle, node):
    return sum(dict(st)[node] for st in cycle) / len(cycle)


def run(wiring, inputs, drugs):
    clamp = {}
    for d in drugs:
        clamp.update(DRUG_CLAMP[d])
    cyc = attractor(wiring, inputs, clamp)
    return readout(cyc, "Prolif"), readout(cyc, "Viab")


def main():
    scenarios = {
        "escape_ON (FB+CCNE)":   build_wiring(True, True),
        "FB_only":               build_wiring(True, False),
        "CCNE_only":             build_wiring(False, True),
        "escape_OFF (neither)":  build_wiring(False, False),
    }
    base = {"IGF1R_in": 1, "Fusion": 1}
    drugs = list(DRUG_CLAMP)
    combos = [()] + [(d,) for d in drugs] + list(itertools.combinations(drugs, 2))

    # baseline contrast (any scenario; use escape_ON)
    w = scenarios["escape_ON (FB+CCNE)"]
    print("=== Baseline (IGF1R on, no drug/damage), escape_ON ===")
    for lab, fus in [("Fusion ON", 1), ("Fusion OFF", 0)]:
        p, v = run(w, {"IGF1R_in": 1, "Fusion": fus, "Damage": 0}, [])
        print(f"  {lab:<12} Prolif={p:.2f} Viab={v:.2f}")

    # full scan across scenarios x damage x combos
    rows = []
    for sname, wir in scenarios.items():
        for dmg in (0, 1):
            for combo in combos:
                p, v = run(wir, {**base, "Damage": dmg}, list(combo))
                rows.append({"scenario": sname, "damage": dmg,
                             "intervention": "+".join(combo) or "none",
                             "Prolif": round(p, 2), "Viab": round(v, 2),
                             "collapses": v < 0.5})
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(HERE, "intervention_scan.csv"), index=False)

    # robustness: which interventions collapse viability across ALL scenarios?
    print("\n=== ROBUST collapses (Viab<0.5 in ALL 4 assumption-scenarios) ===")
    for dmg in (0, 1):
        sub = df[df["damage"] == dmg]
        piv = sub.groupby("intervention")["collapses"].all()
        robust = sorted(piv[piv].index)
        print(f"  Damage={dmg}: {robust if robust else '(none)'}")

    print("\n=== Assumption-DEPENDENT collapses (collapse in some but not all scenarios) ===")
    for dmg in (0, 1):
        sub = df[df["damage"] == dmg]
        g = sub.groupby("intervention")["collapses"]
        dep = sorted([i for i, s in g if s.any() and not s.all()])
        print(f"  Damage={dmg}: {dep if dep else '(none)'}")
        for i in dep:
            where = sub[(sub.intervention == i)][["scenario", "collapses"]].values.tolist()
            print(f"      {i}: " + ", ".join(f"{s.split(' ')[0]}={'Y' if c else 'n'}" for s, c in where))

    # explicit mechanistic checks
    print("\n=== Mechanistic checks (escape_ON scenario) ===")
    print(f"  BETi alone:          Prolif={run(w, {**base,'Damage':0}, ['BETi'])[0]:.2f}")
    print(f"  BETi+CDK46i:         Prolif={run(w, {**base,'Damage':0}, ['BETi','CDK46i'])[0]:.2f}")
    print(f"  WEE1i no damage:     Viab={run(w, {**base,'Damage':0}, ['WEE1i'])[1]:.2f}")
    print(f"  WEE1i + ifosfamide:  Viab={run(w, {**base,'Damage':1}, ['WEE1i'])[1]:.2f}")
    print(f"  IGF1Ri alone:        Prolif={run(w, {**base,'Damage':0}, ['IGF1Ri'])[0]:.2f}")
    print(f"  CDK46i (escape_OFF): Prolif={run(scenarios['escape_OFF (neither)'], {**base,'Damage':0}, ['CDK46i'])[0]:.2f}")

    ents = ["CIC-DUX4","IGF1R","RAS","ERK","CIC","ETV4","ETV5","BRD4","CCND1","CCND2",
            "CDK4","CDK6","CDK2","CCNE1","RB1","E2F","WEE1","MYC"]
    with open(os.path.join(HERE, "entities.txt"), "w") as fh:
        fh.write(". ".join(ents) + ".\n")
    with open(os.path.join(HERE, "wiring.json"), "w") as fh:
        json.dump({k: build_wiring(True, True)[k] for k in build_wiring(True, True)}, fh, indent=2)
    print("\n[done] wrote intervention_scan.csv, wiring.json, entities.txt")


if __name__ == "__main__":
    main()
