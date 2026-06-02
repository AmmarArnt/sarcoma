# ADR-0001: Missing-data taxonomy + biomarker value-of-information layer

- **Status:** Accepted
- **Date:** 2026-06-02
- **Origin:** Issue #7 (@Cerimagic, *"High-impact missing biomarkers and future stratification
  opportunities"*) → PR #15
- **Deciders:** Ammar Arnautovic, with Claude Code

## Context

Issue #7 raised a translational-immunology point: the framework worked well with *available* data, but
did not explicitly distinguish between (a) currently-available patient data, (b) missing-but-obtainable
data, and (c) missing data that would have little impact on decisions. The contributor asked whether the
framework could **rank unknown biomarkers by how much they would change vector prioritization** if they
became available (e.g. MHC-I status, NK markers, PD-L1, the nectin/TIGIT axis, immune infiltration,
additional genomic/transcriptomic features).

The existing golden rule (§1.4, "say what you could not establish") captured uncertainty *qualitatively*
per output, but nothing in the framework ranked *which* unknowns matter most, or recorded low-impact
gaps with the reason they are low-impact so they stop propagating as open questions.

## Decision

Add a **standing decision-sensitivity layer**, not a new attack vector (the four vectors remain fixed —
golden rule §1.8). Two artifacts:

1. **`sims/06-biomarker-value-of-information/`** — a new *type* of in-silico experiment: it treats the
   context parameters of the already-validated Sim-4 Boolean immune-clearance model as *biomarkers* and
   measures each one's **value of information (VoI)** — the fraction of background states in which
   learning it flips the recommended selective-clearance regimen. No new biology: imports Sim 4 unchanged;
   baseline is Sim 1's GSE60740 real data.

2. **`simulation-output/biomarker-voi-stratification.md`** — the framework-layer deliverable: a standing
   **three-tier missing-data taxonomy** (Tier A Known / Tier B Missing-decision-relevant-&-obtainable,
   ranked by VoI / Tier C Missing-low-impact, recorded *with* the reason), applied to the current
   fusion-unconfirmed case.

Headline result for this case: **nectin CD155/CD112 is the highest-VoI missing biomarker (0.625), not
MHC-I (0.188)** — because the NK arm is the documented antigen-loss fallback, so MHC-I loss reroutes
rather than stalls, whereas nectin loss collapses the non-cytotoxic program with no fallback. Baseline
PD-L1 is low-VoI (modeled as IFN-induced/adaptive) — a clean Tier-C example.

## Consequences

- **CLAUDE.md updated:** §0 reuse-inventory now lists `biomarker-voi-stratification.md`; §2 effort-table
  gains a row routing "which unknowns matter / what to measure / stratify a new case" questions to the
  VoI layer (reuse-and-extend, not re-derive); §4 + §7 register Sim 6 and bump the sim range to 01–06.
- **`sims/00-INDEX.md`** registers Sim 6 in the simulation registry.
- **Future sessions** should reuse this layer for missing-data / value-of-information questions, and
  apply the three-tier taxonomy when anchoring to a new patient case, rather than re-deriving.
- **Grounding:** OpenMed NER grounding for Sim 6 was initially deferred (the PR ran in an ephemeral
  container without the venv) and later backfilled locally (team `v4-lead`); all 24 entities recognized.
- **Trade-offs / what this does NOT do:** it ranks *what to measure, not what the measurement will be*
  (high VoI ≠ "abnormal in this patient"); magnitudes are model-relative (the robust takeaway is the
  ordering logic, NK-axis > T-cell-axis given the antigen-loss fallback); it is **not** a recommendation
  to obtain any test. The model is qualitative Boolean with transferred (non-CIC-DUX4-validated) edges.
- **Bridge to #8:** the contributor's closing point — that an input's uncertainty should attenuate how
  strongly a hypothesis is propagated — is recorded here as a design principle and is the link to the
  evidence-confidence-scoring work in issue #8.

## Alternatives considered

- **Purely descriptive list of "missing data."** Rejected: the issue explicitly asked for *prioritization*,
  and the Sim-4 model already encodes most listed markers as decision variables, so a quantitative VoI
  ranking was both feasible and more useful than a flat list.
- **Bake the taxonomy into CLAUDE.md as a golden rule.** Rejected: it is an analytical capability, not a
  non-negotiable safety/citation rule; a reuse pointer (§0/§2) is the right weight.
- **New attack vector.** Rejected by the fixed-four-vectors constraint; this is a supplementary
  analytical layer.
