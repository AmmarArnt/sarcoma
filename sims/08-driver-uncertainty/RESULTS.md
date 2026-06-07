# Sim 8 — Driver-Uncertain (Fusion-Unconfirmed) Robustness + Value-of-Information — RESULTS

**One-line:** For a patient who is *histologically* CIC-rearranged sarcoma but *fusion-unconfirmed*, the
true driver is a latent variable; marginalizing the catalog over a literature-anchored prior shows the
**throttle/cell-cycle/immune vectors are robust regardless of the driver**, the **DUX4/MCL1 "re-arm the
death program" hypothesis is genuinely contingent** (it should NOT be pursued for this patient until the
driver is resolved), and **resolving the driver is the single highest-value action** — long-read WGS+RNA-seq
> DUX4 IHC > methylation array by expected value of information.

**Confidence:** this is a Bayesian DECISION model (Mechanistic/Theoretical), not data and not a diagnosis.
Its job is to be honest about an unknown: report what's robust to it and what it's worth to resolve it.
Parameters trace to `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`.

## How the unknown variable is handled
The driver D ∈ {D1 cryptic CIC-DUX4, D2 rare non-DUX4 partner, D3 non-fusion CIC loss-of-function,
D4 phenocopy/misclassified (BCOR/Ewing), D5 orphan}. Literature-anchored prior (swept widely):
`p(D) = [0.45, 0.12, 0.10, 0.20, 0.13]`, prior entropy **2.07 bits**. Every intervention is scored by its
**expected on-target probability marginalized over D** (robustness), and every test by **EVSI** — the
expected gain in decision value, which is nonzero exactly when a test flips which interventions are worth
committing to. (Method reuses Sim 6 / ADR-0001; engine is the forward Sim 7 re-expressed for uncertainty.)

## Finding 1 — What is robust to the unknown driver (commit now)
Expected on-target probability, marginalized over the driver (`robustness_ranking.csv`):
| Intervention | E[on-target] | robust / contingent |
|---|---|---|
| BRD4 / BETi | **0.81** | robust |
| CDK4 / CCND1 (CDK4/6i) | **0.78** | robust |
| immune / NK / checkpoint | 0.70 | robust |
| EZH2i → MHC-I priming | 0.65 | robust |
| p300/CBP inhibition | 0.64 | robust |
| junction-specific ASO / vaccine | 0.51 | **contingent** |
| MCL1i / re-arm DUX4 death program | **0.39** | **contingent** |

The five throttle/cell-cycle/epigenetic/immune vectors are on-target across all driver hypotheses — they
are the safe bets for this patient *now*, exactly matching protocol-v1's "BRD4/super-enhancer addiction is
the most robust target for a fusion-unconfirmed case."

## Finding 2 — The PR's flagship hypothesis is demoted for THIS patient
The decision model pursues the five robust vectors without any test, **but does NOT pursue MCL1i / "re-arm
the DUX4 death program."** Reason: that vulnerability exists only if the driver carries a DUX4
transactivation domain (essentially D1), so its marginal on-target probability is 0.39 and its high regret
(committing a therapy line that cannot work) makes its expected value negative under the prior. **The build
recipe's top forward hypothesis is therefore driver-contingent, not a given here** — a non-obvious, honest
correction that only falls out of modeling the unknown explicitly.

## Finding 3 — Resolving the driver is the highest-value action (and which test)
Expected value of sample information (`test_value_of_information.csv`):
| Test | EVSI | entropy reduction |
|---|---|---|
| **long-read WGS + RNA-seq** | **+1.86** | 1.02 bits |
| DUX4 IHC | +1.68 | 0.79 bits |
| DNA-methylation array | +1.05 | 0.51 bits |

- **Long-read WGS+RNA-seq** is highest — it resolves cryptic CIC-DUX4 junctions and rare partners that
  FISH/short-read miss (the DUX4 D4Z4-repeat problem), unlocking junction-specific therapy *and* implying
  the DUX4 domain. This reproduces protocol-v1's V3-FH3 ("highest immediate clinical leverage") from an
  independent decision-analytic argument.
- **DUX4 IHC** is a close, *cheap* second: a positive result specifically unlocks the MCL1/DUX4-fragility
  line (`test_unlock_map.csv`: each of DUX4+, CIC-class, junction_DUX4 flips MCL1 into the pursue-set).
- **Methylation array** guards against the ~20% misclassification risk (D4) by confirming CIC class.

## Finding 4 — Conclusions are robust to the prior (sweep, 5000 samples)
Sampling the prior across the literature ranges (`prior_sweep.csv`):
- **BRD4/BETi is the top-robustness intervention in 96.6%** of prior samples (CDK4/6i the rest).
- **Long-read WGS+RNA-seq is the highest-VoI test in 100%** of prior samples.
- **MCL1/DUX4-fragility is pursued without a test in only 26%** of samples — i.e. across almost all
  plausible priors it stays contingent on resolving the driver. The demotion is not an artifact of one
  prior.

## Limitations (honest)
- Decision model, **not** a diagnosis or treatment recommendation; values/penalties are transparent
  mechanistic judgments (stated in `driver_uncertainty_model.py`), not utilities elicited from anyone.
- Priors are literature-anchored estimates with several `[VERIFY]`/`[estimate]` components (esp. D3/D5
  frequencies and the rare-partner enrichment within the fusion-negative subset) — hence the mandatory
  prior sweep. Real co-occurrence/false-negative pulls were not done here (egress-blocked; same as Sim 7).
- Assumes the generic fusion-unconfirmed state. **If this patient already had DUX4 IHC / methylation /
  long-read done, condition the prior on those results** (the model supports that — edit `PRIOR_DEFAULT`).
- OpenMed NER grounding not executed (HuggingFace blocked); `entities.txt` emitted, `grounding.tsv` records it.

## Reproduce
```
.venv/bin/python sims/08-driver-uncertainty/driver_uncertainty_model.py
```
Deterministic (seed 20260607). Outputs: `robustness_ranking.csv`, `test_value_of_information.csv`,
`test_unlock_map.csv`, `prior_sweep.csv`, `drivers.csv`, `entities.txt`.
