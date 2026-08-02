# Sim 10 — Chemo-Response Phenotype as Evidence: Driver Re-Conditioning + DDR Cell-State Resolution — RESULTS

**One-line:** Treating this patient's **deep, twice-repeated chemotherapy response** as a likelihood-bearing
observation (not just a clinical fact) and propagating it through an explicit *driver → DDR-state → response*
model shows that **the response resolves the therapeutically decisive variable — the DNA-damage-response /
SLFN11 cell state — to ~94%, while making the driver question *harder*, not easier** (entropy over D rises).
The practical consequence: **the highest-value lever moves from "resolve the driver" to "protect the
DDR state the tumour has already demonstrated,"** and the framework's flagship contingent hypothesis
(MCL1 "re-arm") drops out of the pursue-set in **99.1%** of sampled parameterisations.

**Confidence:** Bayesian **DECISION model** (Mechanistic/Theoretical tier) — not data, not a diagnosis, not
medical advice. Extends Sim 8 (ADR-0008) at the extension point Sim 8 itself named ("condition the prior on
this patient's actual results"). Every parameter is stated in `run_chemoresponse_cellstate.py` and swept.

---

## What was observed (the input)

| | Observation | Date |
|---|---|---|
| **O1** | Excellent histologic response to first-line VDC/IE — **>95% necrosis** at resection | Jan 2025 |
| **O2** | **Complete radiographic response** of relapsed lung nodules after **4 cycles of ifosfamide** | 2026 |

Neither is a molecular test. Both are *functional assays already run on this patient's tumour*.

## Why the observation is informative (the model's load-bearing asymmetry)

The two leading driver hypotheses have **opposite, molecularly-named DDR phenotypes**:

| Hypothesis | DDR phenotype | Named mechanism | Published chemo response |
|---|---|---|---|
| Canonical **CIC::DUX4** | repair-**proficient** | **POLE upregulation** + proficient DNA repair | **~30%** of CIC patients respond well |
| **Ewing / EWSR1-FET** | repair-**limited**, sensing-competent | **EWS-FLI1 transactivates SLFN11** → irreversible replication-fork arrest | **~53%** good histologic response |

So the model does **not** map driver → response directly. It inserts the mechanism as an explicit latent layer:

```
D (driver D1..D5)  ->  S (DDR / SLFN11 state)  ->  O (observed response)
P(O|D) = Σ_S P(O|S) · P(S|D)
```
with `S_hi` = SLFN11-high / repair-limited, `S_lo` = SLFN11-low / repair-proficient.

### Consistency check (the parameters were not fitted to the outcome literature)
The per-driver response rates **fall out of** `P(S|D) × P(O1|S)` rather than being tuned to match:

| | model-implied single good-response rate | published |
|---|---|---|
| D1 canonical CIC::DUX4 | **0.260** | ~0.30 |
| D4 phenocopy / Ewing-like | **0.562** | ~0.53 |

Both land on the literature independently. That is the main reason to take the S-layer parameterisation
seriously at all — it is the only part of this model with an external check.

---

## Finding 1 — The driver most-likely hypothesis FLIPS, but the driver question gets *harder*

| Driver | prior (Sim 8) | P(O\|D) | posterior | change |
|---|---|---|---|---|
| D1 cryptic CIC::DUX4 | 0.450 | 0.089 | **0.264** | **−0.186** |
| D2 rare partner | 0.120 | 0.126 | 0.100 | −0.020 |
| D3 non-fusion CIC LOF | 0.100 | 0.144 | 0.095 | −0.005 |
| **D4 phenocopy / misclassified** | 0.200 | 0.292 | **0.386** | **+0.186** |
| D5 orphan | 0.130 | 0.182 | 0.156 | +0.026 |

- Most-likely driver **flips D1 → D4** (in **75.2%** of 20 000 swept parameterisations; D4 is top in 72.3%).
- **But entropy over D RISES: 2.065 → 2.110 bits.** The phenotype did not identify the driver — it moved
  mass off a peaked D1 into a flatter **D1-vs-D4 contest**. This is a genuine (and initially
  counter-intuitive) result and it is reported rather than smoothed over.

## Finding 2 — The phenotype *does* sharply resolve the DDR state (the headline)

| State | prior | posterior |
|---|---|---|
| **S_hi — SLFN11-high / "sensing-competent, repair-limited"** | 0.370 | **0.938** |
| S_lo — SLFN11-low / repair-proficient (the POLE-high CIC phenotype) | 0.630 | 0.062 |

Entropy over S falls **0.950 → 0.337 bits**. Sweep: median **0.936**, 90% CI **[0.830, 0.983]**, and
**P(S_hi) > 0.80 in 98.0%** of samples.

> **The asymmetry is the point.** The same observation resolves **S to ~94%** while leaving **D at a
> 39%/26% two-way split.** The chemo response is far more informative about *what the cell's DNA-damage
> response is doing* than about *which fusion it carries* — and it is the DDR state, not the fusion, that
> gates the therapeutic decisions below.

## Finding 3 — Intervention re-ranking: the biggest mover is DDR-state maintenance

Expected payoff, prior belief → posterior belief (Sim 8's seven originals keep their exact Sim 8
parameters, so any movement is attributable to the update alone):

| Intervention | P(on-target) | payoff before | payoff after | Δ |
|---|---|---|---|---|
| immune, MRD window, NK-first (V4) | 0.720 | 1.688 | **1.688** | 0.000 |
| **SLFN11 maintenance — EZH2i / class-I HDACi (V3, doubles as V4 priming)** | 0.710 | 0.455 | **1.599** | **+1.145** |
| CDK4/CCND1 (V1) | 0.773 | 1.502 | 1.478 | −0.024 |
| BRD4/BETi (V1) | 0.754 | 1.565 | 1.435 | −0.131 |
| GPX4 / ferroptosis — persister-directed | 0.550 | 1.060 | 1.060 | 0.000 |
| immune NK/checkpoint (driver-agnostic) | 0.700 | 0.960 | 0.960 | 0.000 |
| p300/CBP (V1/V3/V4) | 0.529 | 0.992 | 0.680 | −0.312 |
| EZH2i MHC-I priming (V3→V4) | 0.571 | 0.802 | 0.641 | −0.161 |
| ATR/CHK1i synthetic-lethal | 0.228 | 0.554 | **−0.162** | −0.716 |
| junction-specific ASO / vaccine | 0.327 | 0.322 | **−0.700** | −1.022 |
| **MCL1i "re-arm the DUX4 death program"** | 0.229 | −0.058 | **−0.853** | −0.796 |

- **SLFN11 maintenance is the single biggest gainer (+1.145)** and stays in the pursue-set in **100%** of
  swept samples; it beats the opposing ATR/CHK1i branch in **100%**.
- **Three items leave the pursue-set:** ATR/CHK1i (the SLFN11-*low* branch — correctly closed by S_hi),
  junction-specific ASO/vaccine, and MCL1i.
- **MCL1 "re-arm" drops out in 99.1% of samples.** Sim 8 already held it as driver-contingent; this is a
  **second, independent, phenotypic** argument for the same conclusion — a tumour that reliably dies to an
  alkylator does not have a death program that needs re-arming.
- The **driver-robust backbone is essentially unmoved** (CDK4 −0.02, BETi −0.13): as in Sim 8, the throttle/
  cell-cycle/immune vectors do not depend on this resolving.

## Finding 4 — The chemo response was a *free* SLFN11 assay (EVSI recomputed after the update)

| Test | EVSI | what it can still flip |
|---|---|---|
| long-read WGS + RNA-seq | **1.297** | MCL1i, junction ASO/vaccine |
| DUX4 IHC | 1.129 | MCL1i, junction ASO/vaccine |
| methylation array | 0.434 | MCL1i, junction ASO/vaccine |
| **SLFN11 IHC** | **0.020** | ATR/CHK1i only |
| **BH3 profiling** | **0.000** | *(nothing — confirmatory only)* |

Two honest reads:
1. **SLFN11 IHC and BH3 profiling have near-zero decision value *because the phenotype already bought that
   information*.** The clinical course functioned as the assay. (They may still be worth doing as cheap
   confirmation — EVSI values a test's power to *change a decision*, not its power to catch a modelling
   error, and the falsifiers below are exactly why one would still run SLFN11 IHC.)
2. **The remaining value of driver-resolution is now almost entirely about re-opening the two
   fusion-contingent options**, both of which currently sit at negative payoff. Driver-resolution is still
   the top-EVSI action, but its *reason* has changed: before, it protected a broad option set; now it is a
   targeted bet on rescuing MCL1/junction-specific therapy.

## Finding 5 — Falsifiers (single results that would overturn the above)

| If… | Then… |
|---|---|
| **SLFN11 IHC is negative** on relapse tissue | the S_hi inference is wrong; chemo-sensitivity runs through another route (e.g. HR/ARID1A) → SLFN11-maintenance drops out and the ATR/CHK1i branch re-opens |
| **methylation array returns CIC class** | D4 collapses; posterior returns toward D1/D3 and the CIC-directed catalog re-strengthens |
| **long-read WGS finds a canonical CIC::DUX4 junction** | D1 confirmed *despite* the phenotype → a chemo-sensitive CIC::DUX4 outlier; MCL1/junction lines re-open and the DDR read must be re-derived |
| **relapse biopsy shows a POLE-high / repair-proficient signature** | contradicts S_hi directly; the entire SLFN11-maintenance rationale fails |

## Limitations (honest)

- **Decision model, not data and not a diagnosis.** Values/penalties are transparent mechanistic
  judgements, not utilities elicited from any patient or clinician.
- **`P(S|D)` and `P(O|S)` are estimates**, not measurements — which is why every conclusion is reported with
  a 20 000-sample sweep over their stated ranges. The consistency check against the two published response
  rates is the only external validation, and it validates the *marginals*, not the internal split.
- **`O2` is a radiographic CR, not a pathologic one.** Nodule disappearance on CT after prior whole-lung
  irradiation can overstate tumour clearance, and some pulmonary nodules are non-neoplastic. If O2 is
  weaker than modelled, the S posterior softens (the sweep's lower ranges cover this: 90% CI still ≥0.83).
- **No SLFN11 data exist in CIC-DUX4 sarcoma at all.** `P(S_hi|D1)=0.20` is inferred from the POLE/
  repair-proficiency paper, not from a measured SLFN11 distribution. This is the single weakest parameter.
- **Conditional independence of O1 and O2 given S** is an assumption. Sharing a common cause (the DDR
  state) is the right structure, but residual correlation (e.g. shared micro-environment, clonal identity)
  would make the two observations partly redundant and **overstate** the S posterior.
- The observations are also **confounded with tumour burden and treatment intensity** — an oligometastatic
  relapse treated with high-dose ifosfamide is a favourable setting independent of biology. The model
  attributes all of the signal to S; some belongs to setting.
- OpenMed NER grounding not executed (HuggingFace egress blocked — see `grounding.tsv`).

## Reproduce

```
.venv/bin/python sims/10-chemoresponse-cellstate/run_chemoresponse_cellstate.py
```
Deterministic (numpy seed 20260802). Outputs: `driver_posterior.csv`, `state_posterior.csv`,
`intervention_reranking.csv`, `test_value_of_information.csv`, `sensitivity_sweep.csv`, `entities.txt`.

*Research simulation / hypothesis generation only. Not medical advice, not a diagnosis, and not a
testing or treatment recommendation.*
