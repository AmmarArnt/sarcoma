# Sim 6 — Biomarker Value-of-Information (VoI) — RESULTS

**One-line:** Treats the *context parameters* of the validated Sim-4 immune-clearance model as
**biomarkers** and measures how much each currently-unknown marker, if measured, would change the
model's recommended selective-clearance regimen — producing a **ranked list of which missing
biomarkers are worth obtaining** and a three-tier missing-data taxonomy. Directly answers GitHub
issue #7.

**Confidence: low-medium (qualitative).** This is a *decision-sensitivity* analysis layered on a
qualitative Boolean model. It ranks **what to measure**, not what the measurement will be. It adds
**no new biology** — it reuses Sim 4's edges (each cites a real paper) and Sim 1's real-data baseline
(GSE60740). Not medical advice; not a treatment plan.

---

## Method

We import `evaluate`, `DEFAULT_PARAMS`, `NONCYTO` from `../04-immune-state-model/immune_state_model.py`
**unchanged**. Sim 4's host/tumor context parameters are exactly the immune biomarkers issue #7 asks
about, and for **this** fusion-unconfirmed, heavily-pretreated case **none of them were measured** —
the catalog assumed values. We therefore treat all seven as *unknown* and ask, per biomarker:

- **OAT (one-at-a-time)** — at the catalog's assumed baseline, does *learning* this biomarker flip the
  recommended minimal regimen and/or the clearance **route** (T-cell / NK / unreachable)?
- **Decision-flip frequency (total-effect)** — over all 2⁶ = 64 joint settings of the other six
  unknowns, the fraction of backgrounds in which flipping this biomarker changes the recommended
  minimal-regimen set. A Boolean decision-sensitivity index: high ⇒ the recommendation is fragile to
  this marker *regardless of what else we don't know*.

"Recommended minimal regimen" = smallest set of non-cytotoxic interventions reaching
`TargetState = (Cleared AND not Prolif)` in the Sim-4 model.

Biomarker → model parameter map (all 7 unmeasured for this case):

| Biomarker (clinical assay) | Model param | Informs |
|---|---|---|
| MHC-I / B2M / TAP1 antigen-presentation integrity | `B2M_intact` | V3→V4 T-cell |
| CD8+ tumor-infiltrating lymphocytes | `Teff_present` | V4 T-cell |
| Treg / immunosuppressive TME burden (FoxP3) | `Treg_high` | V4 T-cell + NK |
| TIGIT / exhaustion-axis expression | `TIGIT_high` | V4 nectin/TIGIT gate |
| Nectin CD155 / CD112 (DNAM-1 ligand) | `DNAM1L` | V4 nectin/TIGIT gate |
| HLA-E (NK/CD8 inhibitory ligand) | `HLA_E` | V4 NK |
| NK-cell functional reserve | `NKeff_present` | V4 NK |

---

## Key results

Case baseline (catalog assumed context): recommended minimal regimen **`CDK4/6i + αTIGIT` via the NK
route** — reproduces Sim 4 exactly.

**VoI ranking (total-effect, fraction of backgrounds where learning the marker changes the rec):**

| Rank | Biomarker | decision-flip | route-flip | reachability-flip | Informs |
|---|---|---|---|---|---|
| 1 | **Nectin CD155/CD112 (`DNAM1L`)** | **0.625** | 0.625 | **0.625** | V4 nectin/TIGIT gate |
| 2 | **HLA-E (`HLA_E`)** | **0.500** | 0.453 | 0.375 | V4 NK |
| 3 | Treg burden (`Treg_high`) | 0.312 | 0.016 | 0.0 | V4 T-cell + NK |
| 3 | TIGIT (`TIGIT_high`) | 0.312 | 0.016 | 0.0 | V4 nectin/TIGIT gate |
| 5 | NK reserve (`NKeff_present`) | 0.250 | 0.047 | 0.0 | V4 NK |
| 6 | MHC-I / B2M (`B2M_intact`) | 0.188 | 0.172 | 0.125 | V3→V4 T-cell |
| 6 | CD8+ TIL (`Teff_present`) | 0.188 | 0.172 | 0.125 | V4 T-cell |

**One-at-a-time at the case baseline — does learning it change the recommendation?**

| Biomarker | Result | Interpretation |
|---|---|---|
| Nectin CD155/CD112 | **FLIPS → UNREACHABLE** | If the nectin/DNAM-1 ligand is absent, the non-cytotoxic route fails entirely — the single most decision-changing measurement |
| HLA-E | **FLIPS NK → T-cell** | HLA-E⁺ closes the NK route and forces the T-cell (MHC-I-priming) route |
| NK reserve | **FLIPS NK → T-cell** | Unfit NK (likely post-WLI/chemo) forces the T-cell route or host repair (IL-15) |
| Treg / TIGIT | FLIPS regimen composition | Changes *which* agents are needed, not the route |
| MHC-I / B2M | no change at baseline | NK fallback covers antigen loss → lower marginal value *here* |
| CD8+ TIL | no change at baseline | NK route is robust to T-cell-arm inputs at this baseline |

---

## The three findings that matter (and one that is counter-intuitive)

1. **Nectin (CD155/CD112) is the highest-VoI missing biomarker — not MHC-I.** In the model the
   DNAM-1 activating signal gates **both** the T-cell and the NK kill rules, so losing the nectin
   ligand makes selective clearance *unreachable* by any non-cytotoxic combination, while there is no
   fallback. This is the model-internal consequence of Sim 4's "nectin/TIGIT is the load-bearing gate"
   finding, now quantified as a *measurement priority*.

2. **MHC-I / B2M ranks lower than the issue's intuition would suggest — because of the NK fallback.**
   The issue lists MHC-I expression status first. In this model B2M loss does *not* stall the program:
   it reroutes T-cell→NK (Sim 4's "antigen-loss fallback"). MHC-I status is still worth knowing (it
   decides V3-priming-then-T-cell vs NK-first), but its *marginal decision value is smaller* than the
   nectin and HLA-E axes. This is exactly the kind of "which unknown most changes prioritization"
   nuance the issue asked the framework to make explicit.

3. **HLA-E and NK reserve are the route-selectors.** Both flip the program between the NK route and
   the T-cell route. Together with nectin they make the **NK arm's three decision variables
   (nectin, HLA-E, NK fitness)** collectively the dominant uncertainty for this case — consistent with
   the catalog's NK-first hypothesis and Sim 5's "host state must be repaired (IL-15) in unfit-NK
   hosts."

4. **PD-L1 baseline expression is a Tier-C (low-VoI) marker *in this model*** — not because it is
   unimportant biologically, but because the model encodes PD-L1 as **IFN-induced / adaptive**
   (`PDL1 = IFN`), so a static baseline PD-L1 IHC does not enter the decision until priming begins.
   This is a concrete, defensible example of the issue's "missing data that would likely have little
   impact on current decision-making" category — and a caveat: the *low* rank is a property of the
   model's adaptive-PD-L1 assumption, which should be stated, not hidden.

---

## What this does NOT establish / limitations

- **It ranks what to measure, not the measurement.** A high VoI means "learning this would often change
  the plan," not "this marker is abnormal in this patient."
- **Inherits every Sim-4 limitation:** qualitative Boolean logic, transferred mechanism edges
  (CDK4/6i-immunity from breast; senescence-NK from fibroblast; TIGIT/nectin general — none
  CIC-DUX4-validated), single-cell-line baseline (GSE60740).
- **VoI magnitudes are model-relative**, driven by the Boolean kill-rule structure (DNAM_active is a
  shared AND-gate → nectin dominates). Different rule encodings would shift magnitudes; the *ordering*
  (NK-axis markers > T-cell-axis markers, given the antigen-loss fallback) is the robust takeaway.
- **`Fusion` is held fixed (out of scope).** Junction confirmation governs a *separate* decision
  (junction-specific ASO / vaccine / CAR-T), not this immune-clearance model. The atypical
  fusion-unconfirmed flag is unchanged by this analysis.
- **Equal-weight background prior.** The total-effect metric weights all 64 backgrounds equally; it is
  a sensitivity index, not a posterior-weighted expected-value-of-information.

## Grounding (OpenMed NER)

The OpenMed NER backend (mlx + HuggingFace models) was **not installable in this ephemeral container**
(no project venv, `openmed` absent) — reported honestly rather than fabricated. Sim 6 introduces **no
new biomedical entities**: its `entities.txt` is a subset of Sim 4's already-grounded entity set
(`../04-immune-state-model/grounding.tsv`), where B2M, TAP1, HLA-A/E, NLRC5, CD274/PD-L1, PVR, CD155,
NECTIN2, CD112, TIGIT, CD226, DNAM-1, MICA, ULBP2, CDK4/6, natural-killer cell and regulatory-T-cell
were all NER-recognized. Two entities here are *not* in the Sim-4 file and remain ungrounded pending a
working NER backend: **FOXP3** and **CD8-positive T cell**.

## Reproduce

```bash
python3 sims/06-biomarker-value-of-information/run_voi.py   # needs pandas (Sim 4 import); no network
```

Outputs: `voi_ranking.csv`, `oat_detail.csv`, `voi_summary.json`, `entities.txt`.
All results are research-simulation hypotheses, not medical advice.
