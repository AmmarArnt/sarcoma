# Manifest — Sim 7, Tumorigenesis "Build Recipe" Transformation Model

**Type:** literature-parameterized Boolean logic model (same engine class as sims 03–05).
**No external data download.** This sim does not ingest a dataset; it encodes published
*mechanism* as Boolean wiring and enumerates the consequences exhaustively. Every wiring
rule is annotated in `transformation_model.py` with the doc/specialist source it encodes.

## Why no download here
The execution environment's egress policy is allow-listed. Verified during this run
(access date 2026-06-07):
- reachable: pypi.org (200), raw.githubusercontent.com (200)
- **blocked (HTTP 403):** figshare/ndownloader (DepMap host), depmap.org, cbioportal.org API,
  eutils.ncbi.nlm.nih.gov, huggingface.co

Consequences:
- A DepMap/cBioPortal **co-occurrence** pull (which would have put real CDKN2A/TP53/TERT
  alteration frequencies behind the "minimal cooperating genotype" node) **could not be run
  here.** Those frequencies are instead carried from the cited literature in the specialist
  briefs (`simulation-output/tumorigenesis-reverse-engineering/cooperating-lesions-specialist.md`)
  and should be re-pulled from DepMap 24Q4 / cBioPortal when egress allows. Forward step.
- **OpenMed NER grounding could not be executed** (HuggingFace blocked). `entities.txt` is
  emitted for grounding when models are reachable; the named entities here
  (CIC-DUX4, CIC, DUX4, ETV4/5, CDKN2A, TP53, TERT, BRD4, CDK4, RB1) are all standard terms
  already grounded GENE/PROTEIN/Cancer in prior sims (see sims 02–04 `grounding.tsv`).

## Parameter provenance (mechanism → wiring)
| Wiring rule | Source |
|---|---|
| permissive progenitor chromatin is the precondition for productive fusion binding | docs/03 "Cell of Origin Problem"; cell-of-origin-specialist (Yoshimoto, Cancer Res 2017, DOI 10.1158/0008-5472.CAN-16-3351) |
| DUX4 transactivation domain is pro-death in somatic cells → needs apoptosis buffering | docs/02 "DUX4 component"; driver-engineering-specialist (FSHD death program) |
| TP53 loss blocks BOTH apoptosis and senescence (double-duty) | cooperating-lesions-specialist |
| CDKN2A loss relieves the senescence brake (frequent CIC-DUX4 co-event) | docs/02; cooperating-lesions-specialist |
| super-enhancer/BRD4 amplification makes ETS output dominant (CIC-DUX4 = transfer from Ewing) | docs/02 "Epigenetic Amplification"; epigenetic-permissiveness-specialist |
| replicative immortality (TERT/ALT) required for a stable tumor cell | hallmark; cooperating-lesions-specialist |

## Reproduce
```
.venv/bin/python sims/07-tumorigenesis-trajectory/transformation_model.py
```
Deterministic; no randomness, no network. Outputs:
`transformation_states.csv`, `minimal_sets.csv`, `node_necessity.csv`,
`trajectory_orderings.csv`, `reverse_engineering_map.csv`, `entities.txt`.

## Honest scope
This is a **hypothesis-structuring** model (Mechanistic/Theoretical tier). It shows what the
*encoded mechanism implies* — it is **not** evidence that any specific genotype transforms a
human cell, and **not** medical advice. The model's value is forcing the build logic to be
explicit (what is necessary, what is substitutable, whether order matters) and exposing the
reverse-engineering gaps. Garbage-in/garbage-out applies: the conclusions are only as good as
the cited wiring, which is stated rule-by-rule so it can be challenged.
