# In-Silico Simulations — Index

Three computational simulations of the CIC-DUX4 forward hypotheses, run on **real public data**
(no wet lab), each with a reproducible Python script, a data MANIFEST (source URLs + sha256 +
access date), and **OpenMed NER grounding** of named entities. No fabrication: every number traces
to executed code on downloaded data or a live API; where data was unavailable it is reported as such.

Run from the repo root with the project venv: `.venv/bin/python`
(Raw downloads are cached under each sim's `data/` and are gitignored; scripts re-download on demand.)

| # | Simulation | Real input | Engine | Headline result |
|---|---|---|---|---|
| 1 | Signature reversal | GEO **GSE60740** (IB120 CIC-DUX4 on/off) | L1000CDS2 API | Top reversers = **IGF1R→PI3K/AKT/mTOR, CDK4/6, MEK** |
| 2 | Dependency mining | **DepMap 24Q4** CRISPR (Ewing proxy, n=27) | Chronos gene-effect | **EZH2 not a dependency**; CDK4 selective; IGF1R enriched; WEE1 pan-essential |
| 3 | Network dynamics | docs/02 + cited biology | Boolean + ODE | Only **WEE1 + ifosfamide** robustly collapses viability |
| 4 | Immune-state / selective clearance | Sim-1 immune-gene data + cited biology | Boolean (nectins + immune markers) | **DNA-damage-free clearance reachable**; minimal route **CDK4/6i + αTIGIT** (NK/senescence); "strangle only" ≠ cleared. See `04-immune-state-model/STATES.md` |
| 5 | Whole-body system-state + sequencing | Sim-4 model + cited biology | Boolean + delays (5 compartments, temporal) | **Order matters: NK-first** clears fastest; checkpoint-first never; **host state must be repaired** (IL-15) in unfit-NK hosts. Reveals the "MHC-I restoration gap." |
| 6 | Biomarker value-of-information | Sim-4 model (context params as biomarkers) | Boolean decision-sensitivity | **Nectin CD155/CD112 is the highest-VoI missing biomarker** (not MHC-I — NK fallback covers antigen loss); HLA-E + NK-fitness select the route; PD-L1 baseline is low-VoI (adaptive). Answers issue #7; three-tier missing-data taxonomy. |
| 7 | Tumorigenesis "build recipe" (FORWARD/inverse) | docs/02–03 + team specialist briefs | Boolean transformation model | **Transformation = AND of 6 steps, 5 non-substitutable** (progenitor + fusion + MCL1/BCL2 buffer + immortalization + p300/super-enhancer; senescence bypass CDKN2A *or* TP53 = the only substitutable one); **order matters** (buffer the DUX4 death program before the driver); 4 build steps have **no current attack vector** → forward-hypothesis frontier. Reverse-engineers the construction (ADR-0007). |
| 8 | Driver-uncertain ("fusion-unconfirmed" patient) | driver-uncertainty brief (lit-anchored priors) | Bayesian latent-variable + EVSI + prior sweep | Driver is a latent variable D1–D5; **throttle/cell-cycle/immune vectors are robust regardless of driver** (BETi top-robust in 96.6% of priors); **the DUX4/MCL1 "re-arm" hypothesis is driver-contingent and should NOT be pursued until the driver is resolved**; **resolving the driver is the highest-value action** (long-read WGS+RNA-seq > DUX4 IHC > methylation array; long-read top-VoI in 100% of priors). Handles "another unknown variable" by marginalizing + valuing information (ADR-0008). |
| 9 | Condensate / LLPS of the DUX4 transactivation module (FORWARD Track B) | UniProt Q9UBX2/Q01844/P35637/Q96RK0 (CRC64-verified fetch; FT-verified domain boundaries) | localcider Das-Pappu/Uversky + metapredict disorder + **PLAAC** prion-HMM/PAPA | **EXECUTED 2026-06-25** (network-permissive). **Informative partial-negative:** the DUX4 C-term is a disordered (metapredict 0.65) **acidic activation domain**, **NOT** a FET-type prion-like LCD — **PLAAC PRDscore 0** vs EWSR1 77.6 / FUS 113.7; it clusters with the folded CIC HMG-box control. → **FET homotypic self-assembly does NOT transfer.** Refines **FH-9.1**: if CIC-DUX4 forms a condensate it is **heterotypic** (acidic AD → p300/CBP coactivator hub), not prion-like; falsifier = p300/CBPi (A-485/inobrodib) dissolution test. Fusion-agnostic (covers the ~5%). FuzDrop/PScore/catGRANULE not obtained (servers down/interactive — not fabricated). No DUX4/CIC-DUX4 LLPS study exists (2026-06 sweep). |

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
- **Sim 9 condensate/LLPS — DONE (2026-06-25):** executed with localcider + metapredict + PLAAC; the only remaining gap is the **heterotypic-aware web servers** (FuzDrop interactive-only; PScore + catGRANULE 2.0 servers were unreachable) — retry when up to directly test the refined *heterotypic* FH-9.1.
- **Mine GSE248040** (2024 CIC-DUX4 ChIP-seq) and the **Nat Commun 2025 patient-derived tumoroid drug-screen/CRISPR** data — real CIC-DUX4 dependency resources that can replace the Ewing proxy (see `simulation-output/evidence-refresh-2026-06.md` §F).

All results are research-simulation hypotheses, not medical advice.
