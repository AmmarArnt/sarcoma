# ADR-0003: Translational feasibility layer (clinical-trial & regulatory awareness)

- **Status:** Accepted
- **Date:** 2026-06-02
- **Origin:** Issue #9 (@Cerimagic, *"Translational Feasibility Layer: Clinical Trial and Regulatory
  Awareness"*) → PR (this branch)
- **Deciders:** Ammar Arnautovic, with Claude Code

## Context

Issue #9 raised a translational-medicine point: the framework reasons well about biological
plausibility and evidence strength, but did not explicitly capture **real-world accessibility and
development maturity** — so two biologically equivalent hypotheses were indistinguishable even when one
sits in an actively recruiting Phase 3 trial, one is preclinical, one's drug was discontinued, one is
under regulatory hold, and one is approved elsewhere and repurposable. The contributor asked for a layer
covering development stage, regulatory status, trial availability, geographic accessibility, repurposing
potential, and major translational barriers — explicitly to **distinguish biological plausibility from
practical feasibility, not to exclude early-stage ideas**.

This is a **third axis**, orthogonal to the two the framework already had (or is adding): the 7-tier
evidence vocabulary (`sarcoma-contract`) and the in-flight confidence rubric
(`docs/08-evidence-confidence-scoring.md`, PR #16 / issue #8). Notably, the issue-#8 rubric's
"Achievability" sub-axis is a *pharmacokinetic in-vivo concentration* question, which is **not** the
same as clinical-development/regulatory access — the two had to be delineated to avoid collision.

The feasibility axis is also the one that **moves without any new biology**. This run demonstrated it:
verification surfaced that **tazemetostat — the catalog's named central V3→V4 bridge agent — was
voluntarily withdrawn from all US indications by Ipsen on 2026-03-09** (SYMPHONY-1 secondary-malignancy
signal; commercial withdrawal, not an FDA revocation; never EMA-approved). The mechanism is unchanged;
the access path closed. The framework had no place to record that.

## Decision

Add a **standing translational-feasibility layer** — a supplementary analytical layer, **not** a new
attack vector (the four vectors remain fixed, golden rule #8). One artifact:

**`simulation-output/translational-feasibility-layer.md`** — defines a five-band **Feasibility Band**
scheme (F1 Accessible-now / F2 Accessible-via-trial / F3 In-development-no-route / F4
Discontinued-withdrawn-on-hold / F5 Concept-only), collapsing the issue's development-stage +
regulatory-status + trial-availability dimensions into one jurisdiction- and date-stamped band, with
geography / repurposing / barriers as explicit columns. Bands are reported as **bands, not
false-precision numbers** (same rationale as PR #16 §3). The layer is **applied to every
Clinical/Experimental entry in `protocol-v1.md`**, with each regulatory/trial fact **verified against a
live source this run** (the trial-forensics run had web access denied; this one did not).

Key composition rules:
- **Three orthogonal axes**: evidence tier (what kind), confidence (believe it works in vivo — PR #16),
  feasibility (could a patient access it — this layer). They must not be averaged into one score.
- **Two-lane rule preserved**: feasibility annotates display prominence in the *confirmatory* lane; it
  **never prunes the Forward-Hypotheses lane** (golden rule #5). Low feasibility ≠ drop the idea.
- **Jurisdiction + date stamping**: FDA ≠ EMA ≠ PMDA; every band is "as of June 2026" and perishable.

Headline applied results: **tazemetostat moved F1→F4 (US) with no biological change**; the BET-inhibitor
class has contracted to essentially one surviving clinical asset (ZEN-3694) so the catalog's "strongest
mechanistic entry point" is among its weakest *access* stories; the highest-feasibility clinical entries
(CDK4/6i, DNMTi, checkpoint antibodies, N-803/Anktiva) are F1 but modest/unproven in CIC-DUX4; the most
trial-mature platform (V940/intismeran autogene neoantigen vaccine) is F2/indication-distant. A
constructive substitution is recorded — re-anchor the EZH2 *mechanism* on the *class* (valemetostat
trials) rather than the withdrawn molecule.

## Consequences

- **CLAUDE.md updated:** §0 reuse-inventory now lists `translational-feasibility-layer.md`; §2
  effort-table gains a row routing "is it accessible / approved / in a trial / discontinued / how soon
  could a patient reach it" questions to this layer (reuse-and-extend, re-verify before external use).
- **`protocol-v1.md` is annotated, not rewritten** — the catalog's evidence tiers (axis 1) are
  unchanged; the feasibility layer is an additive overlay. The tazemetostat finding is significant
  enough that a future `protocol-v2` should carry the feasibility band beside Top-Level Finding #2; left
  to maintainer sign-off rather than clobbering the baseline.
- **Companion to PR #16 / issue #8:** this layer references `docs/08-evidence-confidence-scoring.md` as
  the in-flight confidence axis and explicitly delineates feasibility from #8's "Achievability"
  sub-axis. The two PRs are independent; whichever merges second should keep the cross-references intact.
- **Perishability is a new obligation:** feasibility bands go stale. Forward Hypothesis 3 in the layer
  proposes a lightweight periodic "regulatory-watch" re-check of the ≤5 most-cited clinical agents; not
  wired as automation (defer to the maintainer), but recorded as the maintenance pattern.
- **Trade-offs / what it does NOT do:** it ranks *access, not benefit* (F1 ≠ works, F5 ≠ worthless); it
  is not a recommendation to enroll/obtain/avoid anything; it is US-centric unless noted and
  date-stamped; `[VERIFY]` items (entinostat outcome, vorinostat EU specifics, regorafenib cohort
  recruitment) are flagged, not asserted. The atypical fusion-unconfirmed flag is unchanged (F5
  junction-specific rows remain POSSIBLY INAPPLICABLE).
- **Grounding:** entities in the layer are drugs/diseases already grounded for `protocol-v1.md` via
  `scripts/openmed_ner.py`; no new un-grounded entities were introduced (valemetostat, N-803,
  ZEN-3694 are drug-class terms; regorafenib previously grounded).

## Alternatives considered

- **A single composite "actionability score" fusing plausibility × feasibility.** Rejected: the issue's
  whole point is to *distinguish* the two; fusing them re-creates the exact confusion (a high-feasibility
  grocery-store compound would outrank a high-plausibility F5 concept). Kept as separate orthogonal axes.
- **Numeric 0–100 feasibility score.** Rejected for the same over-precision reason as PR #16 §3 — bands
  are auditable and honest; a magic number is neither, and regulatory status is categorical anyway.
- **Rewrite `protocol-v1.md` in place with the new findings (esp. tazemetostat).** Rejected by the
  preserve-the-baseline rule (CLAUDE.md §0) — additive overlay + a note that v2 should fold it in.
- **New attack vector.** Rejected by the fixed-four-vectors constraint; this is a supplementary
  analytical layer, the same call as ADR-0001.
