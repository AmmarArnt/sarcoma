#!/usr/bin/env python3
"""DepMap CRISPR dependency mining for CIC-DUX4 candidate targets.

Real data only — DepMap 24Q4 Public (figshare DOI 10.25452/figshare.plus.27993248.v1):
  - Model.csv            (cell-line metadata)
  - CRISPRGeneEffect.csv (Chronos gene effect; more negative = stronger dependency,
                          ~ -1 = median of common-essential genes, ~0 = non-dependency)

Question: (1) Is any confirmed CIC-DUX4 line in DepMap? (2) Are the forward-simulation's
named targets (WEE1, IGF1R, BRD4, EZH2, CDK4, CDK6, ...) dependencies in the closest
available proxy — Ewing sarcoma (EWSR1-FLI1) lines? Ewing is a PROXY, not CIC-DUX4.

No fabrication: every number computed from the downloaded files.
"""
from __future__ import annotations
import os, sys, hashlib, datetime, urllib.request
import pandas as pd, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
os.makedirs(DATA, exist_ok=True)

MODEL_URL  = "https://ndownloader.figshare.com/files/51065297"   # Model.csv
EFFECT_URL = "https://ndownloader.figshare.com/files/51064667"   # CRISPRGeneEffect.csv
RELEASE = "DepMap 24Q4 Public (figshare 27993248 v1, DOI 10.25452/figshare.plus.27993248.v1)"

TARGETS = ["WEE1", "IGF1R", "BRD4", "EZH2", "CDK4", "CDK6",
           "CCND1", "CCND2", "ETV1", "ETV4", "ETV5", "MYC", "IGF1", "INSR"]
# Reference controls to anchor the Chronos scale.
CONTROLS_ESSENTIAL = ["POLR2A", "RPL3", "EEF2"]   # pan-essential -> very negative everywhere
CONTROLS_NEUTRAL   = ["OR2T4", "GFP"]              # expected ~0 / absent


def dl(url, path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        print(f"  downloading {url} -> {os.path.basename(path)}")
        urllib.request.urlretrieve(url, path)
    return path


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def main():
    print("[1] Model.csv")
    mpath = dl(MODEL_URL, os.path.join(DATA, "Model.csv"))
    model = pd.read_csv(mpath)
    # Identify the metadata columns present
    cols = model.columns.tolist()
    print(f"    {model.shape[0]} models; cols incl: {[c for c in cols if 'Oncotree' in c or 'Disease' in c or 'Subtype' in c][:8]}")

    # --- CIC-DUX4 search across all string columns ---
    cic_mask = pd.Series(False, index=model.index)
    for c in model.select_dtypes(include="object").columns:
        cic_mask |= model[c].astype(str).str.contains("CIC", case=True, na=False) & \
                    model[c].astype(str).str.contains("DUX4|CIC-DUX4|CIC::DUX4", case=False, na=False)
    cic_lines = model[cic_mask]
    # Broader: any mention of DUX4
    dux4_lines = model[model.select_dtypes(include="object").apply(
        lambda col: col.astype(str).str.contains("DUX4", case=False, na=False)).any(axis=1)]

    # --- Ewing lines ---
    disease_col = "OncotreePrimaryDisease" if "OncotreePrimaryDisease" in cols else None
    code_col = "OncotreeCode" if "OncotreeCode" in cols else None
    ew = pd.Series(False, index=model.index)
    if disease_col:
        ew |= model[disease_col].astype(str).str.contains("Ewing", case=False, na=False)
    if code_col:
        ew |= model[code_col].astype(str).str.upper().eq("ES")
    ewing = model[ew]
    name_col = "CellLineName" if "CellLineName" in cols else ("StrippedCellLineName" if "StrippedCellLineName" in cols else cols[1])
    id_col = "ModelID" if "ModelID" in cols else cols[0]

    print(f"    CIC-DUX4 lines found: {len(cic_lines)}; any-DUX4 mention: {len(dux4_lines)}")
    print(f"    Ewing lines found: {len(ewing)}")
    ewing_ids = ewing[id_col].tolist()
    ewing[[id_col, name_col] + ([disease_col] if disease_col else []) + ([code_col] if code_col else [])
          ].to_csv(os.path.join(HERE, "ewing_lines.csv"), index=False)
    print("    Ewing models:", list(zip(ewing[id_col], ewing[name_col]))[:25])

    print("[2] CRISPRGeneEffect.csv (reading header, then only target columns)")
    epath = dl(EFFECT_URL, os.path.join(DATA, "CRISPRGeneEffect.csv"))
    header = pd.read_csv(epath, nrows=0)
    gene_cols = list(header.columns)
    idcol0 = gene_cols[0]
    want = TARGETS + CONTROLS_ESSENTIAL + CONTROLS_NEUTRAL
    # columns look like "WEE1 (7465)" -> match by symbol token before " ("
    colmap = {}
    for c in gene_cols[1:]:
        symbol = c.split(" (")[0]
        if symbol in want:
            colmap[symbol] = c
    found = sorted(colmap)
    missing = [g for g in want if g not in colmap]
    print(f"    matched gene columns: {found}")
    if missing:
        print(f"    not present as columns: {missing}")

    usecols = [idcol0] + [colmap[g] for g in found]
    eff = pd.read_csv(epath, usecols=usecols).rename(columns={idcol0: "ModelID"}).set_index("ModelID")
    eff.columns = [c.split(" (")[0] for c in eff.columns]
    n_lines = eff.shape[0]
    print(f"    gene-effect matrix: {n_lines} lines x {eff.shape[1]} target genes")

    ewing_present = [m for m in ewing_ids if m in eff.index]
    print(f"    Ewing lines with CRISPR data: {len(ewing_present)}")

    print("[3] dependency stats: Ewing vs pan-cancer")
    rows = []
    for g in found:
        col = eff[g]
        ewv = col.loc[ewing_present].dropna()
        rows.append({
            "gene": g,
            "ewing_mean": round(ewv.mean(), 3) if len(ewv) else np.nan,
            "ewing_median": round(ewv.median(), 3) if len(ewv) else np.nan,
            "ewing_min": round(ewv.min(), 3) if len(ewv) else np.nan,
            "ewing_n": int(ewv.notna().sum()),
            "alllines_mean": round(col.mean(), 3),
            "alllines_median": round(col.median(), 3),
            "ewing_selectivity(ewing_mean - all_mean)": round(ewv.mean() - col.mean(), 3) if len(ewv) else np.nan,
            "frac_ewing_dependent(<-0.5)": round((ewv < -0.5).mean(), 3) if len(ewv) else np.nan,
        })
    tab = pd.DataFrame(rows)
    # classify role
    def role(r):
        if r["gene"] in CONTROLS_ESSENTIAL: return "control:pan-essential"
        if r["gene"] in CONTROLS_NEUTRAL: return "control:neutral"
        return "target"
    tab["role"] = tab.apply(role, axis=1)
    tab = tab.sort_values(["role", "ewing_mean"])
    tab.to_csv(os.path.join(HERE, "dependency_table.csv"), index=False)

    print("\n=== DEPENDENCY TABLE (Chronos gene effect; <0 = dependency; <-0.5 notable; ~-1 = common-essential) ===")
    with pd.option_context("display.width", 160, "display.max_columns", 20):
        print(tab.to_string(index=False))

    # entities for grounding
    with open(os.path.join(HERE, "entities.txt"), "w") as fh:
        fh.write(". ".join(found + ["Ewing sarcoma", "CIC-DUX4 sarcoma"]) + ".\n")

    with open(os.path.join(HERE, "MANIFEST.md"), "w") as fh:
        fh.write("# Manifest — dependency mining\n\n")
        fh.write(f"Access date: {datetime.date.today().isoformat()}\n")
        fh.write(f"Release: {RELEASE}\n\n")
        fh.write(f"- Model.csv: {MODEL_URL}\n  - sha256 {sha256(mpath)} size {os.path.getsize(mpath)}\n")
        fh.write(f"- CRISPRGeneEffect.csv: {EFFECT_URL}\n  - sha256 {sha256(epath)} size {os.path.getsize(epath)}\n")
        fh.write(f"\nEwing lines with CRISPR data (n={len(ewing_present)}): {ewing_present}\n")
        fh.write(f"CIC-DUX4 lines in DepMap: {len(cic_lines)} (any DUX4 mention: {len(dux4_lines)})\n")

    print(f"\n[done] CIC-DUX4-in-DepMap = {len(cic_lines)} ; Ewing proxy lines = {len(ewing_present)}")
    print("       wrote dependency_table.csv, ewing_lines.csv, entities.txt, MANIFEST.md")


if __name__ == "__main__":
    main()
