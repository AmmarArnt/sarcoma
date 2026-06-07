# Sim 7 — Tumorigenesis "Build Recipe" Transformation Model — RESULTS

**One-line:** Encoded the published CIC-DUX4 transformation mechanism as a Boolean "steps to
reproduce" model and enumerated it exhaustively; the model says a fully transformed CIC-DUX4
sarcoma cell requires **five non-substitutable build steps** (permissive progenitor + fusion +
MCL1/BCL2 apoptosis-buffer + telomere immortalization + p300/super-enhancer amplification) plus
**one substitutable senescence-bypass step** (CDKN2A loss *or* TP53 loss), and that **the order
matters** — installing the apoptosis buffer before the driver is the only way to avoid the DUX4
death gate.

**Confidence: this is a Mechanistic/Theoretical structuring model, not data.** Its value is making
the build logic explicit and falsifiable, and exposing where the construction relies on steps no
current attack vector targets. Every wiring rule is annotated with its source in
`transformation_model.py`. Not medical advice.

## What was run
A literature-parameterized Boolean model (engine class = sims 03–05; no data download — see
`MANIFEST.md` for the egress constraint that blocked DepMap/cBioPortal here). Seven switchable build
inputs → derived biological states → outcome. Exhaustive enumeration of all 2⁷ = 128 input
combinations; minimal-sufficient-set analysis; per-node necessity; and a full application-order
(trajectory) sweep of the smallest minimal recipe. Deterministic, no randomness.

The seven inputs and the mechanism each encodes (sources: the four team specialist briefs in
`simulation-output/tumorigenesis-reverse-engineering/` + docs/02–03):
`progenitor` (permissive cell-of-origin/open chromatin), `fusion` (CIC-DUX4 logic inversion at ETS
loci), `apop_buffer` (MCL1/BCL2 buffering of the DUX4 death program), `CDKN2A_loss` and `TP53_loss`
(senescence/p53 brakes), `immortalize` (TERT/ALT), `amplify` (p300→H3K27ac super-enhancer of the
ETS output, BRD4-read).

## Finding 1 — Most genotypes fail; transformation is a narrow target
Of 128 input combinations: **3 reach full transformation, 16 end in death, 109 are abortive/partial**
(senescence, mortal proliferation, or transient/unstable hyperplasia). "Install the fusion" on its
own never transforms and frequently kills — consistent with the experimental reality that the fusion
is a necessary-but-insufficient driver whose own DUX4 program is pro-apoptotic
(`transformation_states.csv`).

## Finding 2 — Five necessary nodes; only the senescence-bypass *gene* is substitutable
Two minimal sufficient recipes, both size 6 (`minimal_sets.csv`):
| # | Minimal recipe |
|---|---|
| A (empirical route) | progenitor + fusion + **MCL1/BCL2 buffer** + **CDKN2A loss** + immortalize + p300/SE amplify |
| B (alternative)     | progenitor + fusion + **MCL1/BCL2 buffer** + **TP53 loss** + immortalize + p300/SE amplify |

**Necessary in EVERY sufficient set** (`node_necessity.csv`): `progenitor`, `fusion`, `apop_buffer`
(MCL1/BCL2), `immortalize`, `amplify`. The senescence brake must be lifted, but the *gene* is
substitutable (CDKN2A **or** TP53). Recipe A is the empirically observed route: TP53 point mutation
is rare in CIC-DUX4 (Specht 2016, PMID 27664537), whereas CDKN2A/2B 9p21 loss removes both the
p16→Rb and p14ARF→p53 arms at once.

**The load-bearing emergent result:** because the DUX4 death program is largely *p53-independent* and
buffered by **MCL1** (verified dependency in CIC::DUX4 tumoroids, *Nat Commun* 2025 — PMID 40841513
[driver brief] / PMID 40841360 [cooperating brief]; **the two briefs cite adjacent PMIDs for what
appears to be the same finding — VERIFY the exact accession before external use**), losing p53 does
*not* substitute for the apoptosis buffer. `apop_buffer` is therefore a **non-substitutable** build
node — the single node that, flipped *off* in an existing tumor, turns the driver's own program
lethal. That is the model's strongest reverse-engineering payoff.

## Finding 3 — Order matters: buffer the death program before installing the driver
For the smallest minimal recipe (A), **480 of 720 application orders yield a viable build; 240 abort**
— almost all by death when the fusion drives the ETS/DUX4 program in a permissive cell *before* the
MCL1/BCL2 buffer is in place (`trajectory_orderings.csv`). Breaking the viable routes down by which
step is installed first: starting with `apop_buffer` makes **all 120/120** orderings viable, whereas
starting with `fusion` or `progenitor` leaves only 60/120 each. **Interpretation:** there is a real
construction-ordering constraint — the death gate must be disarmed no later than the moment the fusion
becomes active in a permissive cell. (This is a logic-model claim about *dependency ordering*, not a
measured kinetic; tier = Mechanistic.)

## Finding 4 — Reverse-engineering map: four build steps have NO current attack vector
Mapping each build node to the vector that "undoes" it (`reverse_engineering_map.csv`):
| Build node | Undo vector | Status |
|---|---|---|
| p300/SE amplification | **V3** (p300/CBP = the writer; bonus MHC-I restoration → V3→V4) + **V1** (BETi = the reader) | well covered; CIC-DUX4-specific anchor PMID 38275898 |
| CDKN2A senescence brake | **V1/V3** (CDK4/6i substitutes for lost p16; convergent w/ Sims 1–3 CDK4) | covered |
| fusion present | **V2** (prevent translocation, prophylactic) / **V3** (ASO/PROTAC degrade) | partially covered |
| **permissive progenitor** | (V3 differentiation, after the fact) | **GAP** |
| **MCL1/BCL2 apoptosis buffer** | none | **GAP → top forward hypothesis** |
| **TP53 / p53 brake** | none (MDM2i where p53 WT) | **GAP** |
| **telomere maintenance** | none | **GAP** |
| any survivor | **V4** (immune clearance; orthogonal) | end-stage net |

Four necessary/contributing build steps (`progenitor`, `apop_buffer`, `TP53/p53`, `immortalize`) are
targeted by **no current vector** — these are the forward-hypothesis frontier (see the team's lead
brief `simulation-output/tumorigenesis-reverse-engineering/tumorigenesis-build-recipe.md`).

## Limitations (honest)
- **A logic model is only as good as its encoded wiring.** Conclusions restate cited mechanism; they
  are not independent evidence that any genotype transforms a human cell. GIGO applies — the wiring is
  stated rule-by-rule so it can be challenged.
- **No real co-occurrence frequencies** behind the cooperating-lesion nodes: the DepMap/cBioPortal
  pull was blocked by the environment's egress policy (see MANIFEST). CDKN2A/TP53/TERT frequencies are
  carried from the cited literature, where several are themselves `[VERIFY]` (no clean CIC-DUX4-specific
  CDKN2A-deletion %; telomere-maintenance mechanism genuinely unknown).
- **MYC amplification** (recurrent accelerant: 6/7, trisomy 8 5/7, IHC 10/10 — PMID 24947144) and the
  **CCNE1/WEE1 replication-stress** survival state are modeled narratively, not as separate switches,
  to avoid over-fitting the Boolean.
- **OpenMed NER grounding could not be executed** (HuggingFace blocked). `entities.txt` is emitted and
  `grounding.tsv` records the block; the named entities are standard terms already grounded in sims 02–04.
- **Atypical ~5% fusion-unconfirmed cases:** the cooperating-state logic (senescence bypass +
  immortalization + apoptosis buffer) is fusion-agnostic and still applies; fusion-specific nodes do not.

## Reproduce
```
.venv/bin/python sims/07-tumorigenesis-trajectory/transformation_model.py
```
Outputs: `transformation_states.csv`, `minimal_sets.csv`, `node_necessity.csv`,
`trajectory_orderings.csv`, `reverse_engineering_map.csv`, `entities.txt`.
