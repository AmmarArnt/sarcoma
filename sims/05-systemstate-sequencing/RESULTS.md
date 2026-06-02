# Sim 5 — Whole-Body Multi-Microservice State + Sequencing — RESULTS

**One-line:** Models the body as interacting "microservices" (tumor, NK, CD8-T, suppressive TME, host
context) over time and asks whether the **order** of the non-cytotoxic vectors matters. It does:
**NK-first** clears fastest by exploiting the MHC-I-low window; **checkpoint-first** never works;
**"strangle-only" never clears**; and a **hostile host state blocks clearance unless the host
compartment is repaired** (e.g., IL-15 NK arming).

**Confidence: low (qualitative, temporal).** Discrete-time Boolean-with-delays model; illustrative
delays; transferred mechanism edges. Hypothesis generator, not a quantitative/temporal predictor.
Not medical advice.

## What it models
Five compartments + host context, with biological **delays**: MHC-I rises ~3 steps after priming;
senescence (NKG2D ligands) develops ~4 steps after sustained CDK4/6i arrest; CD8-T expansion lags
antigen display by ~4 steps; clearance needs ~2 consecutive steps of kill pressure. Baseline tumor
markers from real CIC-DUX4 data (Sim 1). Code: `system_state_sequencing.py`; full grid:
`sequencing_results.csv`; example trace: `trace_S5_healthy.csv`.

## Sequencing results (step at which selective clearance is reached)
| Strategy | Healthy host | B2M lost | Hostile host (NK unfit, no arming) |
|---|---|---|---|
| S1 checkpoint-only (αPD1+αTIGIT) | **never** | never | never |
| S2 prime-first → release (CDK4/6i; αTIGIT+αPD1 @t4) | t=5 (NK) | t=5 (NK) | t=8 (**T-cell**) |
| S3 NK-first (CDK4/6i+αTIGIT+IL-15 @t0) | **t=1 (NK)** | **t=1 (NK)** | **t=1 (NK)** |
| S4 strangle-only (CDK4/6i+Diff) | **never** | never | never |
| S5 sequenced: NK-first → open T-arm (αPD1 @t6) | **t=1 (NK)** | **t=1 (NK)** | **t=1 (NK)** |

## Three lessons (the answers to "does order matter / what state must the whole body be in")
1. **Order matters — go NK-first.** NK-first (S3/S5) clears almost immediately by exploiting the
   **MHC-I-low missing-self window** that already exists (the fusion keeps MHC-I low), *before*
   priming raises MHC-I. Checkpoint-first (S1) never works — there is nothing visible and Tregs are
   active. This is the documented NK-vs-MHC-I tension, resolved by **temporal separation**.
2. **The "MHC-I restoration gap" (emergent).** In the S5 trace, at t=3 priming has raised MHC-I
   (removing the NK missing-self trigger) but senescence-ligands (t=4) and T-cell priming (later)
   haven't caught up → a one-step window where *neither* arm kills. Implication: either clear during
   the early missing-self window (NK-first) or make sure senescence/NKG2D ligands are up *before*
   MHC-I rises. A real sequencing caution, not visible in a static model.
3. **The whole body must be in the right state, not just the tumor.** In the **hostile host** (unfit
   NK compartment), NK-first only works *because it includes IL-15 NK arming* — i.e., you must repair
   the **host NK microservice**; otherwise you are forced onto the slower T-cell route (t=8), which in
   turn requires intact antigen presentation (fails if B2M is also lost). Suppressive TME (Treg) must
   be down too — supplied here by CDK4/6i (Goel 2017). Clearance is a property of the **global state**,
   not any single compartment.

## The global "body-state vector" for selective clearance (minimal cytotoxics)
Selective clearance occurs when the system reaches approximately:
- **Tumor microservice:** proliferation OFF (CDK4/6i/Diff) → arrested/senescent; visible via MHC-I↑
  (priming/IFN) **or** NKG2D-ligand↑ (senescence); HLA-E low (already true).
- **Nectin gate:** TIGIT brake released (αTIGIT) so CD155/CD112 → DNAM-1 activation dominates — the
  indispensable lever (Sim 4 + here).
- **NK microservice:** fit/armed (host fitness or IL-15) → handles the early missing-self window and
  the B2M-loss fallback.
- **T-cell microservice:** primed (needs MHC-I + time + αPD1 once adaptive PD-L1 appears) → the
  second, slower wave.
- **Suppressive TME:** Treg/MDSC down (CDK4/6i) — without this, effectors are gated off.

## Convergence / where this leaves the picture
- **CDK4/6i + αTIGIT + IL-15 (NK-first), then open the T-arm (αPD1 ± priming)** is the model's
  fastest, most host-robust, lowest-cytotoxic route — and it still works under B2M loss and unfit-NK
  hosts (via arming). This is the selective-clearance counterpart to the cytotoxic WEE1+ifosfamide route.
- Reinforces Sim 4: stopping the loop is necessary but not sufficient; the immune collector and the
  nectin gate must be engaged, in the right order.

## Caveats
Illustrative delays/topology; transferred edges (CDK4/6i-immunity = breast, Goel 2017; senescence→NK
= fibroblast/other; TIGIT/nectin = general, not CIC-DUX4-validated); single-cell-line baseline data;
"steps" are abstract, not days. The strategies are model hypotheses, not regimens; every component
(CDK4/6i, αTIGIT, IL-15, αPD1) is experimental in this disease and carries real toxicity. Clinical
sequencing decisions belong to the oncologist/molecular tumor board.

## Grounding (OpenMed NER, team `v4-lead`)
`grounding.tsv`: CD112, CD155, CD226/DNAM-1, TIGIT, NLRC5, B2M, MICA, ULBP2, NKG2D, PD-1/PD-L1, HLA-E,
IL-15, CDK4/6, plus NK cell / CD8 T cell / regulatory T cell / senescence / interferon recognized.

## Reproduce
`.venv/bin/python sims/05-systemstate-sequencing/system_state_sequencing.py`
