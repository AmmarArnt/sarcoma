# In-Silico Simulations — Index

Three computational simulations of the CIC-DUX4 forward hypotheses, run on **real public data**
(no wet lab), each with a reproducible Python script, a data MANIFEST (source URLs + sha256 +
access date), and **OpenMed NER grounding** of named entities. No fabrication: every number traces
to executed code on downloaded data or a live API; where data was unavailable it is reported as such.

Run from the project venv: `/Users/ammararnautovic/code/sarcoma/.venv/bin/python`
(Raw downloads are cached under each sim's `data/` and are gitignored; scripts re-download on demand.)

| # | Simulation | Real input | Engine | Headline result |
|---|---|---|---|---|
| 1 | Signature reversal | GEO **GSE60740** (IB120 CIC-DUX4 on/off) | L1000CDS2 API | Top reversers = **IGF1R→PI3K/AKT/mTOR, CDK4/6, MEK** |
| 2 | Dependency mining | **DepMap 24Q4** CRISPR (Ewing proxy, n=27) | Chronos gene-effect | **EZH2 not a dependency**; CDK4 selective; IGF1R enriched; WEE1 pan-essential |
| 3 | Network dynamics | docs/02 + cited biology | Boolean + ODE | Only **WEE1 + ifosfamide** robustly collapses viability |
| 4 | Immune-state / selective clearance | Sim-1 immune-gene data + cited biology | Boolean (nectins + immune markers) | **DNA-damage-free clearance reachable**; minimal route **CDK4/6i + αTIGIT** (NK/senescence); "strangle only" ≠ cleared. See `04-immune-state-model/STATES.md` |
| 5 | Whole-body system-state + sequencing | Sim-4 model + cited biology | Boolean + delays (5 compartments, temporal) | **Order matters: NK-first** clears fastest; checkpoint-first never; **host state must be repaired** (IL-15) in unfit-NK hosts. Reveals the "MHC-I restoration gap." |

## Convergence (the point of running three orthogonal methods)
| Target | Sim 1 transcriptomic | Sim 2 genetic dependency | Sim 3 dynamical | Net read |
|---|---|---|---|---|
| **WEE1 + DNA damage** | n/a (kinase) | strong essentiality | **only robust collapse** | **Strongest convergent + actionable (patient on ifosfamide)** |
| **IGF1R axis** | top reverser (2 drugs) + whole PI3K/AKT/mTOR arm | Ewing-enriched dependency | upstream-bypassed as monotherapy | Real target; biomarker-selected subset; combine, don't solo |
| **CDK4 (not CDK6)** | palbociclib reverser | most Ewing-selective | works unless cyclin-E bypass | Real; pair to prevent bypass |
| **EZH2** | absent | **not a survival dependency** | — | **Reposition tazemetostat as MHC-I priming, not cytotoxic** |
| **BRD4/BETi** | absent | universal-essential, non-selective | escapes via reaccumulation; needs combo | Narrow window; degrade + combine |

Two of these (EZH2-is-not-a-dependency; WEE1+ifosfamide) materially update the earlier catalog,
and one (DepMap *does* contain 3 CIC-DUX4 models — TE441T, NCC-CDS1-X1-C1, NCC-CDS1-X3-C1 — but with
no CRISPR screens) corrects a stated assumption.

## Forward / next runnable steps
- **PRISM drug-sensitivity** cross-check of the Sim 1 hits in the Ewing/CIC lines (DepMap repurposing).
- **Get CRISPR onto a CIC-DUX4 line** (TE441T exists in DepMap registry without a screen) — the single highest-value experiment to convert "Ewing proxy" into CIC-DUX4-direct.
- **Structure/condensate track** (AlphaFold + FuzDrop on the fusion) — designed in `../../sarcoma/simulation-output/forward-simulation/in-silico-experiments.md`, not yet executed here.

All results are research-simulation hypotheses, not medical advice.
