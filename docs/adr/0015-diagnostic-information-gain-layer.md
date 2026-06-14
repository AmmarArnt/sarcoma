# ADR-0015: Diagnostic strategy & expected-information-gain layer (test-level VoI, "what to learn next")

- **Status:** Accepted
- **Date:** 2026-06-14
- **Origin:** issue #31 ("Diagnostic Strategy Optimization and Information Gain Analysis") / PR
- **Deciders:** maintainer (via the github-issue-runner workflow)

## Context

The framework could rank *therapeutic* hypotheses but had no standing way to evaluate *diagnostic* ones —
which test most reduces uncertainty, which missing biomarker most changes treatment selection, which
investigations are **low-yield**, and how the diagnostic pathway should adapt under **budget / time /
tissue** constraints. Issue #31 asked the framework to also ask *"what should we **learn** next?"* and to
estimate the **expected information gain** of candidate diagnostic actions (molecular profiling, fusion
analysis, immune profiling, circulating biomarkers, imaging, histopathological reassessment, liquid biopsy).

Most of the machinery already existed but at the **variable** granularity: Sim 6 / ADR-0001 ranks unknown
*variables* by decision-flip VoI; ADR-0011 adds acquisition provenance / cost / timepoint; Sim 8 / ADR-0008
computes **EVSI** for the *driver-resolving tests*. None of these aggregated to the **diagnostic-action
(test) level** — where one test resolves a *bundle* of variables, consumes a shared resource (tissue), and
whose value depends on **what earlier tests already resolved**. Nor did any model **sequencing** under
constraint, or address **imaging**.

## Decision

Adopt a **Diagnostic Strategy & Expected-Information-Gain layer** as a standing analytical layer:
`simulation-output/diagnostic-information-gain-layer.md`. It **composes** the existing artifacts (it does
not re-derive or replace them):

- **Unit of decision = the diagnostic action (test)**, characterized by (1) the **variable bundle** it
  resolves, (2) a **two-currency value profile** — driver-resolution **EVSI** (Sim 8) and immune-route
  **decision-flip VoI** (Sim 6), kept *separate* (different sub-decisions, no fabricated blend), (3)
  **acquisition burden** (provenance P1/P2/P3 + cost/risk/tissue, ADR-0011), and (4) **timepoint**
  (T0/T1/TΔ, ADR-0011).
- **Non-additivity rule:** decision-flip VoIs are not bits and are not summed across a panel; rank by
  *dominant* leverage ÷ burden, not by an arithmetic total.
- **Sequencing rule (the genuinely new piece):** a greedy **realizable-VoI-per-unit-burden** loop —
  archived (P1) bundle first, the one expensive fresh (P2) action only for the residual delta, liquid (P3)
  as downstream monitoring, imaging on its own staging cadence — **re-ranked after every result** because
  tissue is consumed and results gate downstream value.
- **Action-level low-yield register** (the Tier-C analogue) and an **honest imaging gap**: imaging's value
  is real but sits on a *staging* axis the catalog doesn't yet model quantitatively — named, not fabricated.

A quantitative test-level simulation (proposed **Sim 9**: tissue-budget-constrained greedy EVSI-per-burden)
is flagged as **forward work, not executed**, because the action→variable map and per-test burden weights
would be assumptions and the sims obey a real-data-only rule.

## Consequences

- **New artifact:** `simulation-output/diagnostic-information-gain-layer.md` (Tier 2 analytical layer,
  evidence tier `Theoretical / Mechanistic`, confidence medium — does not outrank any real-data finding).
- **CLAUDE.md updated:** §0 reuse list gains the layer; §2 routing table gains a row directing
  diagnostic-strategy / "what test next" / information-gain / low-yield / tissue-budget-sequencing questions
  to this layer (reuse, don't re-derive).
- **Findings register:** a row added to `simulation-output/findings-ranking.md` (group B, strategic/
  diagnostic), per ADR-0009.
- **Not a new axis or a fifth vector.** It is a *composition* of the existing VoI (ADR-0001), provenance
  (ADR-0011), feasibility (ADR-0003), and driver-EVSI (ADR-0008) work at a coarser (action) granularity.
- **Explicitly does NOT:** invent a single blended EIG score across the two value currencies; quantify
  imaging information value; fabricate per-test costs or a new numeric model; or recommend any test. It
  documents diagnostic decision structure for future contributors. Perishable feasibility/assay facts carry
  `[VERIFY]` / `[re-verify]`; not medical advice.

## Alternatives considered

- **Run Sim 9 now (a quantitative test-level VoI sim).** Rejected for this issue: the action→variable
  resolution map and burden weights are assumptions, violating the real-data-only sim rule; deferred to
  forward work so the heuristic ships honestly rather than with fabricated magnitudes.
- **Fold the answer into the existing VoI doc.** Rejected: the new content (action-level bundling +
  constraint-aware *sequencing* + imaging gap) is a distinct decision question ("what to learn next" vs
  "which variable matters") and warrants its own discoverable layer + routing row, matching how #7/#9/#10/#11
  each produced a standing layer.
- **Add a single composite EIG metric.** Rejected: it would require non-data weighting across two distinct
  sub-decisions; the profile + qualitative ordering is the honest representation.
