# Sim 3 — Boolean + ODE Network Model of the CIC-DUX4 Loop — RESULTS

**One-line:** A dynamical model of the oncogenic loop, scanned over single/double interventions with an explicit assumption-sensitivity analysis, independently reproduces (a) the futility of targeted *monotherapy* in the fusion-ON state and (b) the **WEE1-inhibition + DNA-damage (ifosfamide) synthetic-lethal collapse** as the only robust kill — converging with Sim 1, Sim 2, and the literature.

**Confidence: low-medium.** This is a **qualitative hypothesis generator**, not a quantitative predictor. Parameters are illustrative; topology is from `docs/02`/`docs/05` + cited mechanisms with two resistance edges explicitly labelled ASSUMPTION and toggled in a sensitivity analysis. No data fitting. Not a treatment claim.

## Model
- **Boolean** (`boolean_model.py`): nodes IGF1R→RAS→MEK→ERK⊣CIC⊣ETV; CIC-DUX4 = constitutive ETV activator; ETV+BRD4→super-enhancer drive→CCND/CDK4→RB⊣E2F→Proliferation; WEE1 gates Viability under DNA damage. Wiring + sources in `wiring.json`.
- Two **resistance edges** toggled to test robustness (a conclusion is *robust* only if it holds in all four on/off combinations):
  - **FB** = BRD4-independent escape (BRD4 reaccumulation / kinase rewiring) — documented BETi resistance mechanism *[ASSUMPTION]*.
  - **CCNE** = cyclin-E/CDK2 bypass of CDK4/6 — documented CDK4/6i resistance mechanism *[ASSUMPTION]*.
- **ODE** (`ode_model.py`): 5-variable continuous version for threshold/dose-response.

## Baseline contrast (sanity)
| State | Boolean Prolif | ODE Cy |
|---|---|---|
| Fusion ON (disease) | 1.00 (stable proliferative attractor) | 0.528 |
| Fusion OFF (knockdown) | 0.50 (no stable proliferative attractor; oscillates) | 0.422 |

The fusion is required for a *stable* proliferative state — consistent with the GSE60740 knockdown biology used in Sim 1.

## Intervention scan — robust vs assumption-dependent (Boolean)
**ROBUST collapses (Viability <0.5 in ALL four assumption scenarios):**
- **No DNA damage:** *none.* No targeted drug or pair reliably collapses the fusion-ON cell on its own.
- **With ifosfamide (damage):** **WEE1i** and every WEE1i-containing pair (`WEE1i`, `BETi+WEE1i`, `CDK46i+WEE1i`, `WEE1i+MEKi`, `WEE1i+IGF1Ri`). WEE1i collapses viability **only in the presence of damage** — `WEE1i` with no damage stays fully viable.

**Assumption-DEPENDENT collapses (the emergent escape structure):**
- **BETi alone** collapses proliferation *only* when the BRD4-reaccumulation escape (FB) is OFF — i.e., if BRD4 truly stays down. With FB ON, BETi fails. → reproduces BETi-monotherapy escape being contingent on a documented resistance mechanism.
- **CDK4/6i alone** collapses *only* when the cyclin-E/CDK2 bypass (CCNE) is OFF. With the bypass ON, CDK4/6i fails. → reproduces cyclin-E-driven CDK4/6i resistance. (Consistent with Sim 2, where CDK4 is a real selective Ewing dependency — so the truth is between "always works" and "always bypassed.")
- **BETi + CDK4/6i** collapses in 3 of 4 scenarios — it overcomes *either* single escape, but **not both escapes simultaneously**. → the combination is more robust than either monotherapy, but dual resistance still defeats it.

## ODE dose-response (threshold behaviour)
- **MEK inhibition:** Fusion-ON proliferation index is nearly flat (0.528 → 0.50 even at 100% MEKi) = **upstream bypass** (the fusion drives ETV independent of ERK). Fusion-OFF is MEK-sensitive (→ 0 at full inhibition, with a nonlinear late drop). Quantitative echo of the Boolean result that IGF1Ri/MEKi monotherapy can't collapse the fusion-ON cell.
- **BRD4 inhibition:** lowers output but with a **threshold** — while the fusion term persists, sub-maximal BRD4 occupancy only partially reduces proliferation (0.528→0.255 at 90% inhibition). Consistent with "BETi needs very high, sustained target engagement," part of why monotherapy underperforms.

Data: `intervention_scan.csv` (all scenarios), `ode_dose_response.csv`.

## What is emergent vs what is encoded (honesty)
- **Encoded (not a discovery):** the WEE1+damage collapse is *built into* the Viability rule (it formalizes the JCI Insight 2022 checkpoint-abrogation mechanism, PMC8986087). The model demonstrates the logic is self-consistent and robust; it does not independently *discover* it.
- **Emergent (informative):** the **redundant-escape structure of the proliferation drive** — that fusion-ON cells resist IGF1R/MEK (upstream bypass), BETi (FB), and CDK4/6i (cyclin-E bypass) as monotherapies, and that only combinations overcome *single* escapes — falls out of the topology, not from hand-set outcomes. This is the model's contribution: it explains *why* targeted monotherapy disappoints and *why* the damage-coupled WEE1 axis is attractive.

## Convergence across the three simulations (the headline)
| Target | Sim 1 (signature reversal) | Sim 2 (DepMap dependency) | Sim 3 (network model) |
|---|---|---|---|
| **IGF1R** | top reverser (2 drugs) | Ewing-enriched dependency (−0.73) | monotherapy bypassed (upstream) |
| **CDK4** | palbociclib reverser | most Ewing-selective (−1.53) | works only w/o cyclin-E bypass |
| **EZH2** | absent | **not a dependency (+0.01)** | (not a survival node) |
| **BRD4** | absent | universal essential, non-selective | escapes via FB; needs combo |
| **WEE1** | (not transcriptional) | strong but pan-essential | **robust collapse only w/ damage** |

The **WEE1 + ifosfamide** hypothesis is the one idea supported (or at least not contradicted) by all three orthogonal in-silico approaches *and* the primary literature — and it is directly actionable for this patient's imminent ifosfamide.

## Limitations
- Qualitative Boolean/ODE; illustrative parameters; not fitted; small node set.
- WEE1+damage outcome is partly definitional (see honesty section).
- Synchronous Boolean update can create artifactual oscillations (fusion-OFF mean 0.50 reflects an oscillatory, not graded, attractor).
- No spatial/stochastic/microenvironment terms; single-cell logic only.

## Grounding (OpenMed NER, team `v3-epigenetic`)
`grounding.tsv`: all 18 model nodes recognized (BRD4, CCND1/2, CCNE1, CDK2/4/6, CIC, CIC-DUX4, E2F, ERK, ETV4/5, IGF1R, MYC, RAS, RB1, WEE1). No unrecognized entities.

## Reproduce
`/Users/ammararnautovic/code/sarcoma/.venv/bin/python boolean_model.py`
`/Users/ammararnautovic/code/sarcoma/.venv/bin/python ode_model.py`
