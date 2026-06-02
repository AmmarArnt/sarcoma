#!/usr/bin/env python3
"""Sim 6 — Biomarker Value-of-Information (VoI) for vector prioritization.

Answers GitHub issue #7: "Which unknown biomarkers would have the greatest potential
to alter vector prioritization if they became available?" — and gives the framework an
explicit three-tier missing-data taxonomy (available / high-value-obtainable / low-impact).

METHOD (no new biology, no fabrication):
  We reuse the ALREADY-VALIDATED, already-grounded Boolean immune-clearance model from
  Sim 4 (`../04-immune-state-model/immune_state_model.py`). Every mechanism edge in that
  model cites a real paper; baseline cell-state is anchored to real CIC-DUX4 data
  (GSE60740, Sim 1). This sim adds NO new edges — it only treats the model's host/tumor
  CONTEXT PARAMETERS as *biomarkers* and measures how much the model's recommended
  minimal selective-clearance regimen changes when each biomarker's (currently unknown)
  value is learned.

  For THIS case the immune context was never measured (fusion-UNCONFIRMED, heavily
  pre-treated tumor; no MHC-I / NK / nectin IHC on record), so every immune context
  parameter below is ASSUMED, not known. That is exactly the situation the issue raises.

  Two VoI metrics per biomarker B:
    (1) OAT (one-at-a-time) at the case baseline — does learning B flip the recommended
        minimal regimen and/or the clearance ROUTE (T-cell vs NK vs unreachable),
        holding all other parameters at the catalog's assumed baseline?
    (2) Decision-flip frequency (total-effect) — over ALL 2^(k-1) joint settings of the
        other unknown biomarkers, the fraction of backgrounds in which flipping B changes
        the recommended minimal-regimen set. This is a Boolean decision-sensitivity index:
        high => the recommendation is fragile to this biomarker regardless of the others.

  "Recommended minimal regimen set" = the set of smallest non-cytotoxic intervention
  combinations that reach TargetState (Cleared AND not Prolif) in the Sim-4 model.

OUTPUT: voi_ranking.csv, oat_detail.csv, voi_summary.json, entities.txt (+ RESULTS.md written by hand).
Qualitative hypothesis-prioritization tool, NOT a quantitative predictor. Not medical advice.
"""
from __future__ import annotations
import itertools, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SIM4 = os.path.join(HERE, "..", "04-immune-state-model")
sys.path.insert(0, SIM4)

# Reuse the validated model verbatim — do not redefine any biology here.
from immune_state_model import DEFAULT_PARAMS, NONCYTO, evaluate  # noqa: E402


# ---- Biomarkers = the model's host/tumor context parameters, with case metadata ----
# Each: param key -> (human-readable assay, vector(s) it informs, issue-example tag).
# 'Fusion' is held fixed: the driver biology is present on histology regardless of junction
# confirmation; fusion-junction status governs a SEPARATE decision (junction-specific ASO /
# vaccine / CAR-T), not this immune-clearance model. See RESULTS.md "Out of scope".
BIOMARKERS = {
    "B2M_intact":    ("MHC-I / B2M / TAP1 antigen-presentation integrity (IHC + sequencing)",
                      "V3->V4 (T-cell)", "MHC-I expression status"),
    "Teff_present":  ("CD8+ tumor-infiltrating lymphocytes present (IHC / multiplex)",
                      "V4 (T-cell)", "Tumor immune infiltration patterns"),
    "Treg_high":     ("Treg / immunosuppressive TME burden (FoxP3 IHC)",
                      "V4 (T-cell + NK)", "Tumor immune infiltration patterns"),
    "TIGIT_high":    ("TIGIT / exhaustion-axis expression in TME",
                      "V4 (nectin/TIGIT gate)", "Nectin/TIGIT axis markers"),
    "DNAM1L":        ("Nectin CD155 / CD112 (DNAM-1 ligand) tumor expression",
                      "V4 (nectin/TIGIT gate)", "Nectin/TIGIT axis markers"),
    "HLA_E":         ("HLA-E (NK/CD8 inhibitory ligand) tumor expression",
                      "V4 (NK)", "NK-cell related markers"),
    "NKeff_present": ("NK-cell functional reserve / count (post-chemo, post-WLI)",
                      "V4 (NK)", "NK-cell related markers"),
}
UNKNOWNS = list(BIOMARKERS.keys())   # all immune context unmeasured for this case


def minimal_set(params):
    """Set of smallest non-cytotoxic combos reaching TargetState. Returns (frozenset_of_combos, route, n)."""
    best_n, hits = None, []
    for r in range(0, len(NONCYTO) + 1):
        for combo in itertools.combinations(NONCYTO, r):
            o = evaluate(params, set(combo))
            if o["TargetState"]:
                if best_n is None or r < best_n:
                    best_n, hits = r, [combo]
                elif r == best_n:
                    hits.append(combo)
        if best_n is not None:
            break  # first non-empty radius is the minimal one
    combo_set = frozenset(frozenset(c) for c in hits)
    if not combo_set:
        return combo_set, "UNREACHABLE", None
    # route label from the first minimal combo (all share the same viable effector here)
    o = evaluate(params, set(next(iter(combo_set))))
    route = "T-cell" if o["Tcell_kill"] else ("NK" if o["NK_kill"] else "?")
    return combo_set, route, best_n


def fmt_combos(combo_set):
    if not combo_set:
        return "(none — clearance unreachable)"
    return " | ".join(sorted("+".join(sorted(c)) for c in combo_set))


def main():
    base = dict(DEFAULT_PARAMS)
    base_set, base_route, base_n = minimal_set(base)
    print("=== CASE BASELINE (catalog assumed immune context) ===")
    print(f"   assumed params: " + ", ".join(f"{k}={base[k]}" for k in UNKNOWNS))
    print(f"   recommended minimal regimen: {fmt_combos(base_set)}  via {base_route}\n")

    # ---- (1) One-at-a-time VoI at the case baseline ----
    oat_rows = []
    for b in UNKNOWNS:
        cur = base[b]
        alt = 1 - cur
        p_alt = dict(base); p_alt[b] = alt
        s_cur, r_cur, n_cur = base_set, base_route, base_n
        s_alt, r_alt, n_alt = minimal_set(p_alt)
        flips = (s_cur != s_alt)
        route_change = (r_cur != r_alt)
        oat_rows.append(dict(
            biomarker=b, assay=BIOMARKERS[b][0], vector=BIOMARKERS[b][1],
            assumed_value=cur, alt_value=alt,
            regimen_if_assumed=fmt_combos(s_cur), route_if_assumed=r_cur,
            regimen_if_alt=fmt_combos(s_alt), route_if_alt=r_alt,
            decision_flips=int(flips), route_changes=int(route_change)))

    # ---- (2) Total-effect decision-flip frequency over all backgrounds ----
    voi_rows = []
    for b in UNKNOWNS:
        others = [x for x in UNKNOWNS if x != b]
        n_back, n_flip, n_route, n_reach_only_one = 0, 0, 0, 0
        for bits in itertools.product([0, 1], repeat=len(others)):
            p = dict(base)
            for k, v in zip(others, bits):
                p[k] = v
            p0 = dict(p); p0[b] = 0
            p1 = dict(p); p1[b] = 1
            s0, r0, _ = minimal_set(p0)
            s1, r1, _ = minimal_set(p1)
            n_back += 1
            if s0 != s1:
                n_flip += 1
            if r0 != r1:
                n_route += 1
            if (not s0) != (not s1):   # learning B flips reachable<->unreachable
                n_reach_only_one += 1
        voi_rows.append(dict(
            biomarker=b, assay=BIOMARKERS[b][0], vector=BIOMARKERS[b][1],
            issue_example=BIOMARKERS[b][2],
            decision_flip_freq=round(n_flip / n_back, 3),
            route_flip_freq=round(n_route / n_back, 3),
            reachability_flip_freq=round(n_reach_only_one / n_back, 3),
            n_backgrounds=n_back))
    voi_rows.sort(key=lambda d: (-d["decision_flip_freq"], -d["reachability_flip_freq"]))

    # ---- print ranking ----
    print("=== BIOMARKER VALUE-OF-INFORMATION RANKING (total-effect across all backgrounds) ===")
    print(f"   {'biomarker':<14}{'decision':>9}{'route':>8}{'reach':>8}   vector")
    for d in voi_rows:
        print(f"   {d['biomarker']:<14}{d['decision_flip_freq']:>9}{d['route_flip_freq']:>8}"
              f"{d['reachability_flip_freq']:>8}   {d['vector']}")

    print("\n=== ONE-AT-A-TIME (at case baseline): does learning this biomarker change the rec? ===")
    for d in oat_rows:
        tag = "FLIPS" if d["decision_flips"] else "no change"
        print(f"   {d['biomarker']:<14} {tag:<10} assumed={d['assumed_value']} -> "
              f"[{d['route_if_assumed']}] vs alt={d['alt_value']} -> [{d['route_if_alt']}]")

    # ---- write artifacts ----
    import csv
    with open(os.path.join(HERE, "voi_ranking.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(voi_rows[0].keys()))
        w.writeheader(); w.writerows(voi_rows)
    with open(os.path.join(HERE, "oat_detail.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(oat_rows[0].keys()))
        w.writeheader(); w.writerows(oat_rows)
    with open(os.path.join(HERE, "voi_summary.json"), "w") as fh:
        json.dump({"case_baseline_regimen": fmt_combos(base_set),
                   "case_baseline_route": base_route,
                   "ranking": voi_rows, "oat": oat_rows}, fh, indent=2)

    ents = ["B2M","TAP1","HLA-A","HLA-E","NLRC5","CD274","PD-L1","PVR","CD155","NECTIN2",
            "CD112","TIGIT","CD226","DNAM-1","MICA","ULBP2","CDK4","CDK6","FOXP3",
            "natural killer cell","CD8-positive T cell","regulatory T cell","CIC-DUX4"]
    with open(os.path.join(HERE, "entities.txt"), "w") as fh:
        fh.write(". ".join(ents) + ".\n")
    print("\n[done] wrote voi_ranking.csv, oat_detail.csv, voi_summary.json, entities.txt")


if __name__ == "__main__":
    main()
