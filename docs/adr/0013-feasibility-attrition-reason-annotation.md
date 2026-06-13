# ADR-0013: Feasibility-layer attrition-reason annotation (why a program closed)

- **Status:** Accepted
- **Date:** 2026-06-13
- **Origin:** issue #9 follow-up comment (@Cerimagic, 2026-06-12) / PR (issue-9-discontinuation-reason)
- **Deciders:** maintainer (AmmarArnt), Claude Code

## Context

[ADR-0003](0003-translational-feasibility-layer.md) introduced the translational feasibility layer
(F1 Accessible-now … F5 Concept-only), which deliberately separates *access* from *evidence*. A follow-up
on issue #9 pointed out that the band alone is **lossy about causation**: two F4 (discontinued/withdrawn/
on-hold) agents can be F4 for opposite reasons — one because its **target was invalidated** (genuinely
negative biological information) and one because a **company reprioritized** (zero biological
information). A reader seeing only "F4 — discontinued" defaults to "it failed, so the idea is dead,"
which is the error to prevent — most acutely in **rare tumors**, where a **cohort-level** negative can
hide a **subgroup-level** positive. The contributor explicitly framed this as *not* a new scoring axis,
only a request to preserve enough context that withdrawal ≠ biological invalidation. The follow-up also
asked a specific question: was the regorafenib CIC-rearranged cohort (NCT02389244) deprioritized for
negative efficacy, missing results, or supersession?

## Decision

Adopt an **attrition-reason annotation** on the existing feasibility axis (no new axis), recorded in a
new analytical layer `simulation-output/feasibility-attrition-reason-extension.md`:

- **Reason taxonomy (R0–R5)** for any F3/F4 (and, for completeness, F5/R0) entry: `R0` never-developed ·
  `R1` target/biology invalidated · `R2` clinical-trial efficacy failure (population-dependent) ·
  `R3` subgroup-dilution (cohort-negative ≠ subgroup-negative) · `R4` regulatory action (distinguish
  voluntary/commercial withdrawal from FDA revocation) · `R5` commercial/portfolio deprioritization.
- **Decoding rule:** the band says whether you can *get* it; the reason code says whether the closure
  says anything about whether it *works*. **Only R1 (and a biomarker-enriched R2) carries negative
  biological information**; R3, R4-commercial, and R5 are biology-silent and the mechanism stays eligible
  for the forward-hypotheses lane.
- **Rare-tumor R3 rule:** when an asset is banded on a basket/all-comers trial, tag R3-risk and preserve
  any reported fusion/CIC subgroup signal rather than collapsing to the cohort verdict.
- Applied to the catalog's closed-access entries (tazemetostat R5+R4, BET-class R5±R2, IGF1R R2+R5/R3,
  WEE1/adavosertib R5, entinostat R2, vorinostat R4/R5, junction agents R0) — finding: **none closed
  because a CIC-DUX4-relevant mechanism was invalidated (R1).**
- **Regorafenib answer:** REGOBONE Cohort E (NCT02389244) verified `ACTIVE_NOT_RECRUITING`, primary
  completion 2024-10-25, **no results posted** (ClinicalTrials.gov, 2026-06-13) → **results-pending**, not
  negative; plus the mechanism is multikinase/anti-angiogenic, not driver-directed. The lone efficacy
  signal is the SARC024 (NCT02048371) n=1 CIC-DUX4 partial response — a worked example of the R3 caveat.

## Consequences

- **CLAUDE.md updated:** §0 reuse list (the feasibility-layer bullet now points to the attrition
  extension) and §2 routing row for "discontinued / withdrawn / on-hold — does that mean it failed
  biologically?" questions.
- **`findings-ranking.md`** gains a Section-B row for the attrition-reason annotation + the regorafenib
  resolution (methodology/trial finding, scored as such — not promoted above real-data findings).
- The parent layer (`translational-feasibility-layer.md`) gets **additive** edits only: the regorafenib
  `[VERIFY]` flag resolved to the live status, and two cross-links to the extension. ADR-0003 stays the
  baseline; the layer is not rewritten.
- New obligation: future F3/F4 entries should carry a reason code, and basket-trial closures should
  preserve subgroup signals.
- **Does NOT** add a scoring axis, change any biology, re-rank the catalog, prune the forward lane, or
  alter the fusion-unconfirmed (atypical-case) handling. Not a treatment recommendation, not a diagnosis.

## Alternatives considered

- **Add a sixth feasibility band for "discontinued-for-commercial-reasons."** Rejected: bands describe
  the access *state*; reason is orthogonal *metadata*. Folding it into the band would re-collapse the
  access/cause distinction the contributor asked to keep, and would be a de-facto new axis (which they
  declined).
- **Just answer the regorafenib question in the issue thread, no artifact.** Rejected: the follow-up
  proposes a reusable standing distinction (how to read any program closure), which belongs as a layer +
  ADR — same reasoning as ADR-0011 for the issue-#7 follow-up.
- **Fold it into the confidence axis (issue #8 / docs/08).** Rejected: confidence is about *transfer to
  CIC-DUX4 in vivo*; attrition reason is about *why the access path closed* — a feasibility-axis
  question, so it lives with ADR-0003.
