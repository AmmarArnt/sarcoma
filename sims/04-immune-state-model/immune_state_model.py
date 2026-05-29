#!/usr/bin/env python3
"""Immune-clearance + cell-state Boolean model of CIC-DUX4 sarcoma.

Goal (per user directive): move beyond cytotoxic destruction. Model selective IMMUNE
clearance and the STRANGLER path (stop dividing -> senescence/differentiation -> let the
immune 'garbage collector' remove the cell), with NECTINS and immune markers as explicit
parameters. Identify the target STATE of two 'microservices':
  A) the sarcoma cell   B) the immune system.

Baseline cell-state is anchored to the REAL CIC-DUX4 on/off data (GSE60740, Sim 1):
  fusion ON => NLRC5 low, MHC-I/B2M/TAP low, PD-L1 low, HLA-E low, CD112(nectin) up.

Qualitative hypothesis generator, NOT a quantitative predictor. Every edge cites a real
mechanism (see SOURCES); modeling assumptions are labelled. No fabrication.

SOURCES (verified):
  - CDK4/6i -> antigen presentation up + Treg down (Goel, Nature 2017, PMID 28813415).
  - Senescent cells cleared by NK via NKG2D ligands MICA/ULBP2 (Aging 2016, PMID 26878797);
    HLA-E is the NK/CD8 escape brake (Nat Commun 2019, s41467-019-10335-5).
  - NLRC5 = master MHC-I transactivator/CITA; immune-evasion target (PNAS 2016, PMID 27162338).
  - Nectin CD155/CD112 engage activating DNAM-1(CD226) and inhibitory TIGIT/CD96 (axis biology).
"""
from __future__ import annotations
import itertools, json, os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- parameters describing the host/tumor context (the 'environment') ----
DEFAULT_PARAMS = dict(
    Fusion=1,          # CIC-DUX4 driver present
    B2M_intact=1,      # 0 = genetic B2M/antigen-presentation loss (MHC-I cannot display)
    Treg_high=1,       # immunosuppressive TME baseline
    TIGIT_high=1,      # exhaustion/checkpoint context; nectin ligands engage TIGIT
    DNAM1L=1,          # CD155/CD112 nectin (DNAM-1 activating ligand) present (data: CD112 up)
    HLA_E=0,           # NK/CD8 inhibitory ligand; LOW per CIC-DUX4 data (favorable)
    Teff_present=1,    # tumor-reactive T cells available IF antigen is presented
    NKeff_present=1,   # NK cells available at baseline
)
# Non-cytotoxic interventions (the focus). DNAdamage included ONLY for comparison.
NONCYTO = ["EpiPrime", "CDK46i", "Diff", "BETi", "aPD1", "aTIGIT", "NKarm"]
ALL_DRUGS = NONCYTO + ["DNAdamage"]

READOUTS = ["Prolif", "MHCI", "NKG2D_L", "DNAM_active", "Tcell_kill", "NK_kill",
            "ImmuneKill", "Senescent", "Cleared", "TargetState"]


def evaluate(params, drugs):
    """Single-pass evaluation (network is feed-forward with shallow loops; resolve by ordered eval)."""
    g = dict(params)
    D = {k: (k in drugs) for k in ALL_DRUGS}

    # --- cell-intrinsic oncogenic loop / strangler axis ---
    BRD4   = not D["BETi"]
    ETV    = bool(g["Fusion"])
    SE     = ETV and BRD4
    Drive  = SE
    p21    = D["Diff"]                                   # differentiation induces CDKI
    CDK46  = Drive and not p21 and not D["CDK46i"]
    RBact  = not CDK46
    E2F    = not RBact
    Prolif = E2F and Drive and not D["Diff"]             # differentiation forces cycle exit
    Senescent = D["CDK46i"] and not Prolif               # CDK4/6i-induced durable arrest -> senescence

    # --- innate stress / interferon context ---
    STING = D["DNAdamage"] or Senescent                  # cGAS from micronuclei/senescence
    IFN   = D["CDK46i"] or STING or D["DNAdamage"]       # CDK4/6i -> ERV dsRNA -> IFN (Goel); + STING
    NKG2D_L = Senescent                                  # senescence surveillance ligands (MICA/ULBP2)

    # --- antigen-presentation / visibility module ---
    NLRC5 = D["EpiPrime"] or IFN                         # baseline (none) = 0 = suppressed (matches data)
    MHCI  = NLRC5 and bool(g["B2M_intact"])
    PDL1  = IFN                                          # adaptive (IFN-driven); baseline low (matches data)

    # --- nectin / DNAM-1 - TIGIT axis (the immune tuning knob) ---
    TIGIT_brake = bool(g["TIGIT_high"]) and not D["aTIGIT"] and bool(g["DNAM1L"])
    DNAM_active = bool(g["DNAM1L"]) and not TIGIT_brake

    # --- brakes ---
    PD1_brake   = PDL1 and not D["aPD1"]
    Treg_active = bool(g["Treg_high"]) and not D["CDK46i"]   # CDK4/6i suppresses Treg (Goel)
    HLA_E_brake = bool(g["HLA_E"])

    # --- effectors (immune microservice) ---
    NKeff = bool(g["NKeff_present"]) or D["NKarm"]
    Tcell_kill = (MHCI and bool(g["Teff_present"]) and DNAM_active
                  and not PD1_brake and not Treg_active)
    NK_kill = (NKeff and DNAM_active and (not MHCI or NKG2D_L)
               and not HLA_E_brake and not Treg_active)

    ImmuneKill = Tcell_kill or NK_kill
    Cleared = ImmuneKill                                 # selective clearance by immune GC
    TargetState = Cleared and not Prolif                 # stopped dividing AND being removed

    return dict(Prolif=Prolif, MHCI=MHCI, NKG2D_L=NKG2D_L, DNAM_active=DNAM_active,
                Tcell_kill=Tcell_kill, NK_kill=NK_kill, ImmuneKill=ImmuneKill,
                Senescent=Senescent, Cleared=Cleared, TargetState=TargetState)


def scan(params, pool):
    rows = []
    for r in range(0, len(pool) + 1):
        for combo in itertools.combinations(pool, r):
            out = evaluate(params, set(combo))
            rows.append({"intervention": "+".join(combo) or "none", "n": r, **{k: int(v) for k, v in out.items()}})
    return pd.DataFrame(rows)


def minimal_hits(df):
    hits = df[df["TargetState"] == 1].copy()
    if hits.empty:
        return hits
    minc = hits["n"].min()
    return hits[hits["n"] == minc].sort_values("intervention")


def main():
    base = DEFAULT_PARAMS
    print("=== BASELINE (fusion ON, no intervention) = disease state ===")
    b = evaluate(base, set())
    print("   " + "  ".join(f"{k}={int(v)}" for k, v in b.items()))

    print("\n=== Scan: NON-CYTOTOXIC interventions only, B2M intact ===")
    df = scan(base, NONCYTO)
    df.to_csv(os.path.join(HERE, "scan_b2m_intact.csv"), index=False)
    mh = minimal_hits(df)
    print(f"   combos reaching TargetState (Cleared & not Prolif): {int((df.TargetState==1).sum())} of {len(df)}")
    print(f"   MINIMAL non-cytotoxic combos:")
    for _, r in mh.iterrows():
        route = "T-cell" if r["Tcell_kill"] else ("NK" if r["NK_kill"] else "?")
        print(f"     [{r['n']}] {r['intervention']:<28} via {route}  (MHCI={r['MHCI']} NKG2D_L={r['NKG2D_L']} DNAM={r['DNAM_active']})")

    # Contrast 1: cytostatic-only (strangle, no immune release) -> stops dividing but NOT cleared?
    print("\n=== Contrast: 'strangle only' (stop dividing, no immune brake release) ===")
    for combo in [("CDK46i",), ("Diff",), ("BETi",), ("CDK46i", "Diff"), ("CDK46i", "BETi", "Diff")]:
        o = evaluate(base, set(combo))
        print(f"   {'+'.join(combo):<22} Prolif={o['Prolif']} Cleared={o['Cleared']}  -> "
              + ("strangled but NOT collected" if (o['Prolif']==0 and o['Cleared']==0) else
                 ("CLEARED" if o['Cleared'] else "still dividing")))

    # Contrast 2: immune-only (release brakes / arm, but no visibility or strangle)
    print("\n=== Contrast: 'immune only' (brakes off / NK armed, no visibility or arrest) ===")
    for combo in [("aPD1", "aTIGIT"), ("aPD1", "aTIGIT", "NKarm")]:
        o = evaluate(base, set(combo))
        print(f"   {'+'.join(combo):<22} MHCI={o['MHCI']} Cleared={o['Cleared']}  -> "
              + ("CLEARED" if o['Cleared'] else "GC active but nothing to grab / braked"))

    # DNA-damage-free check
    free = df[(df.TargetState == 1)]
    print(f"\n=== DNA-damage-free clearance achievable? {'YES' if not free.empty else 'NO'} "
          f"({len(free)} non-cytotoxic combos reach the target state) ===")

    # B2M-loss scenario: T-cell route dead -> only NK route
    print("\n=== Scenario: B2M LOST (antigen-presentation genetically off) ===")
    p2 = dict(base); p2["B2M_intact"] = 0
    df2 = scan(p2, NONCYTO)
    df2.to_csv(os.path.join(HERE, "scan_b2m_lost.csv"), index=False)
    mh2 = minimal_hits(df2)
    print(f"   minimal combos that still clear (NK route only):")
    for _, r in mh2.iterrows():
        route = "T-cell" if r["Tcell_kill"] else ("NK" if r["NK_kill"] else "?")
        print(f"     [{r['n']}] {r['intervention']:<28} via {route}")
    tcell_any = int((df2.Tcell_kill == 1).sum())
    print(f"   T-cell-route clears under B2M loss: {tcell_any} (expected 0)")

    # entities for grounding
    ents = ["CIC-DUX4","NLRC5","HLA-A","B2M","TAP1","CD274","PD-L1","PVR","CD155","NECTIN2",
            "CD112","TIGIT","CD226","DNAM-1","MICA","ULBP2","HLA-E","CDK4","CDK6","RB1","E2F",
            "CDKN1A","BRD4","ETV4","WEE1","interferon","natural killer cell","regulatory T cell","senescence"]
    with open(os.path.join(HERE, "entities.txt"), "w") as fh:
        fh.write(". ".join(ents) + ".\n")
    with open(os.path.join(HERE, "minimal_combos.json"), "w") as fh:
        json.dump({"b2m_intact": mh["intervention"].tolist(),
                   "b2m_lost": mh2["intervention"].tolist()}, fh, indent=2)
    print("\n[done] wrote scan_b2m_intact.csv, scan_b2m_lost.csv, minimal_combos.json, entities.txt")


if __name__ == "__main__":
    main()
