# Manifest — Sim 8, Driver-Uncertainty Robustness + Value-of-Information

**Type:** Bayesian decision model (latent-variable marginalization + EVSI + prior sweep). **No external
data download.** Encodes published mechanism + literature-anchored priors as a decision model and computes
consequences. Reuses the value-of-information methodology of Sim 6 (ADR-0001) and the forward build logic
of Sim 7 (ADR-0007), applied to the ~5% fusion-unconfirmed case.

## Parameter provenance
All parameters are defined in `driver_uncertainty_model.py` and grounded in
`simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`, which in turn cites:
| Parameter | Source (verified or [VERIFY]) |
|---|---|
| CIC FISH false-negative 14–46% → high cryptic-CIC-DUX4 prior (D1) | CIC FISH interpretation-pitfalls literature; RNA-seq recovers FISH-negative CIC-DUX4 [VERIFY PMIDs] |
| CIC-DUX4 ≈95%; non-DUX4 partners (NUTM1/FOXO4/LEUTX/NUTM2A) ≈5% (D2; no DUX4 TAD) | Frontiers Cell Dev Biol 2024 review (PMC11176417); Mod Pathol 2023 "Expanding Molecular Diversity of CIC-Rearranged Sarcomas" |
| DUX4 IHC sensitive/specific for CIC::DUX4 → DUX4_IHC resolves the DUX4-TAD attribute | Macedo et al., Histopathology 2025, DOI 10.1111/his.15341 |
| Methylation reclassifies morphologic mimics (~13–20% BCOR/other) → D4 prior + methylation array power | Array-based methylation profiling (Mod Pathol 2022; PMC7084764; PMC7819999) [VERIFY split] |
| Long-read recovers cryptic junctions short-read misses → highest EVSI | protocol-v1 V3-FH3; DUX4 D4Z4 repeat mappability |

## Egress note (verified 2026-06-07)
Same allow-list as Sim 7: pypi + raw.githubusercontent reachable; figshare/DepMap/cBioPortal/NCBI/
HuggingFace return HTTP 403. Therefore no real co-occurrence/false-negative-rate pull was executed here
(numbers carried from cited literature, several `[VERIFY]`), and OpenMed NER grounding could not run
(`grounding.tsv` records the block).

## Reproduce
```
.venv/bin/python sims/08-driver-uncertainty/driver_uncertainty_model.py
```
Deterministic (numpy seed 20260607). Outputs: `robustness_ranking.csv`,
`test_value_of_information.csv`, `test_unlock_map.csv`, `prior_sweep.csv`, `drivers.csv`, `entities.txt`.

## Honest scope
A decision model, not a diagnosis. It shows what the encoded mechanism + priors imply about (a) robustness
to the unknown driver and (b) the value of resolving it. GIGO applies — parameters are stated explicitly so
they can be challenged or re-conditioned on this patient's actual prior testing.
