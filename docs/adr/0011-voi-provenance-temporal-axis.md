# ADR-0011: VoI acquisition-provenance & temporal-state axes (Tier-B refinement)

- **Status:** Accepted
- **Date:** 2026-06-13
- **Origin:** issue #7 follow-up comment (@Cerimagic, 2026-06-12) / PR (issue-7-voi-provenance)
- **Deciders:** maintainer (AmmarArnt), Claude Code

## Context

[ADR-0001](0001-missing-data-taxonomy-and-voi-layer.md) introduced the missing-data taxonomy
(A — Known / B — Missing-but-obtainable, ranked by value-of-information / C — Missing, low-impact) and
the Sim-6 VoI ranking. A follow-up on issue #7 pointed out that **Tier B is not homogeneous**: a missing
biomarker's practical value depends not only on *which* marker it is, but on **where the answer comes
from** (archived FFPE vs a fresh relapse biopsy vs liquid biopsy) and **which disease timepoint it
characterizes** (baseline at diagnosis vs current at relapse vs the *change* between them). For this
case in particular, several of the highest-value questions — diagnosis confirmation, clonal evolution of
the relapse, and immune-marker drift under treatment — are *temporal* questions whose answers live in
different tissue sources at very different cost and risk.

The original layer conflated "information value" with "acquisition burden" and treated each marker as
single-state, which understates the role of immune editing and overstates what an archived block alone
can answer.

## Decision

Adopt two further classification axes **inside Tier B** of the missing-data taxonomy, recorded in a new
analytical layer `simulation-output/biomarker-voi-provenance-extension.md`:

- **Axis P — acquisition provenance:** `P1` archived/historical (FFPE, slides, prior extracts) ·
  `P2` fresh current-timepoint biopsy · `P3` liquid biopsy (ctDNA/CTC), each with its verified assay
  ceiling and cost/risk profile.
- **Axis T — temporal state:** `T0` baseline (diagnostic-era) · `T1` current (relapse-era) ·
  `TΔ` change-under-treatment (requires **paired** P1+P2 with comparable assays).

Standing rule: when surfacing a high-VoI unknown, record the **cheapest source that can answer it** and
the **timepoint the decision actually needs**; realizable VoI is bounded by recoverability from an
accessible source. No numeric "realizable-VoI" model was fabricated — the layer is a qualitative
refinement, with a quantitative provenance-conditioned Sim-6 extension flagged as future work.

## Consequences

- **CLAUDE.md updated:** §0 reuse list and §2 routing row for VoI / "what should we measure / what's
  unknown" questions now point at the provenance extension alongside the Sim-6 layer.
- **`findings-ranking.md`** gains a row for the provenance/temporal refinement (methodology finding,
  scored as such — not promoted above real-data findings).
- The parent layer (`biomarker-voi-stratification.md`) gets an additive cross-link; it is **not**
  rewritten (ADR-0001 stays the baseline).
- New obligation: future "what to measure" answers should name source + timepoint, not just the marker.
- **Does NOT** change any biology, any Sim-6 VoI number, the four fixed vectors, or the
  fusion-unconfirmed (atypical-case) handling. It is not a recommendation to obtain any test and not a
  diagnosis.

## Alternatives considered

- **Extend Sim 6 with a computed realizable-VoI model.** Rejected for now: the recoverability/feasibility
  multipliers would be assumptions, not real data, violating the sims' real-data-only convention. Left as
  explicit future work.
- **Fold provenance into the translational-feasibility layer (ADR-0003).** Rejected: that layer scores
  *drug/intervention* access, whereas this concerns *diagnostic information* acquisition — a distinct
  question that belongs with the VoI/missing-data taxonomy.
- **Just answer in the issue thread without an artifact.** Rejected: the follow-up proposes a reusable
  standing distinction, which is exactly what ADR-0001's layer is for; capturing it as a layer + ADR
  keeps the framework's history honest.
