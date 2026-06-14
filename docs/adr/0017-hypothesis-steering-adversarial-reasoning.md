# ADR-0017: Hypothesis-steering & adversarial-reasoning protocol (the reasoning-process layer)

- **Status:** Accepted
- **Date:** 2026-06-14
- **Origin:** issue #32 ("Human-Guided Hypothesis Steering and Clinical Reasoning Loops") / PR
- **Deciders:** maintainer (via the github-issue-runner workflow)

## Context

Issue #32 asked whether the framework should explicitly support **human-guided hypothesis steering** and
**clinical-reasoning loops** — clinician-in-the-loop steering, adversarial hypothesis testing, diagnostic
debiasing workflows, structured challenge-response cycles, and dynamic expansion/contraction of the search
space — and whether human-guided steering improves hypothesis quality over purely autonomous exploration.

Unlike issues #7–#11/#31, this is **not** a biological analytical layer (it adds no new mechanisms,
biomarkers, or catalog section). It is a question about the framework's **reasoning process**. The framework
already embodied most of the requested mechanisms *implicitly* — the multi-agent expand/contract wave
architecture, golden rule #5 (the two-lane forward rule), the orchestrator's RESOLVE-CONFLICTS step, the
`sarcoma-pre-output-check` self-audit, the driver-uncertainty alternative-hypothesis model (ADR-0008), and
the GitHub-issue workflow itself as the human steering channel (ADR-0002). What was missing was a **single,
named, standing protocol** and, specifically, a **standing red-team / self-challenge step** at the agent
level (the existing self-audit checks citation/evidence hygiene, not *reasoning* bias).

## Decision

Adopt a **process layer** (not a fifth vector, not a biological analytical layer) documented in
`docs/11-hypothesis-steering-and-adversarial-reasoning.md`:

1. **Map** the issue's five proposed mechanisms onto the framework's existing (implicit) machinery, so the
   project does not re-invent what it has and the real gaps are visible.
2. **Name the project-specific biases** (anchoring on the four fixed vectors, confirmation bias toward
   "promising" compounds, premature closure on the headline catalog, base-rate/rarity blindness,
   availability bias, and the LLM-specific **sycophancy** to a steer) and pair each with its counter-measure
   (existing or added). Bias taxonomy grounded in Croskerry (PMID 23882089/23996094).
3. **Define a small protocol:** (step 1) name the leading hypothesis + its load-bearing assumption; (step 2)
   a one-pass **red-team self-challenge** — disconfirmation / alternative / flip-test / steer-audit, the
   machine analogue of Chain-of-Verification (arXiv:2309.11495); (step 3) structured challenge-response on
   high-leverage hypotheses, generalizing the ADR-0008 latent-variable pattern; (step 4) dynamic
   **expansion/contraction** triggers, with the guardrail that contraction prunes the confirmatory lane only
   and **never the Forward-Hypotheses lane** (golden rule #5).
4. **Name the clinician-in-the-loop channels** that already exist: the GitHub issue thread (async, ADR-0002)
   and `AskUserQuestion` (in-session) — with the rule that a steer **reframes** the search but does not
   supply an evidence tier (the sycophancy guard).

## Consequences

- **New artifact:** `docs/11-hypothesis-steering-and-adversarial-reasoning.md` (Tier 3 methodology doc;
  evidence tier `Mechanistic` for the framework claims, supporting human-factors citations `Established` in
  their own domain, transferred at reduced confidence per docs/10).
- **CLAUDE.md updated:** §0 reuse list and §2 routing table gain a row directing reasoning-process /
  steering / debiasing / red-team / "actively disprove" / search-space questions to this doc; §7 repository
  map gains the docs/11 row; golden rule #5 cross-references the red-team protocol.
- **Agent wiring (see PR / Phase-5-step-6 decision):** the standing **red-team self-challenge** is added as
  a Part-D step in `sarcoma-pre-output-check`, and the orchestrator's RESOLVE-CONFLICTS step references it.
  This is what makes the protocol *behavioral* rather than only documented — without it, a fresh run would
  reason exactly as before (the ADR-0016 failure mode).
- **Not a new axis, layer, or vector.** It does not feed a catalog section, does not change any biological
  finding, and does not outrank real-data evidence. It changes *how* outputs are produced, not *what* is in
  them.
- **Explicitly does NOT:** prove (in-repo) that steered/red-teamed runs produce better CIC-DUX4 hypotheses —
  that claim is `Mechanistic`, transferred from the clinical/LLM literature; a controlled comparison is
  named as forward work (the "red-team delta" forward hypothesis). It does not add bureaucracy beyond a
  one-pass self-challenge + triggered deeper passes; not medical advice.

## Alternatives considered

- **Do nothing — the capability is already implicit.** Rejected: the issue correctly identifies that
  "implicit and uneven" means it is not reliably applied; a fresh run would not red-team itself. Naming it
  and wiring the one standing step is the minimal fix.
- **Build a heavyweight clinician-in-the-loop UI / interactive steering mode.** Rejected: out of scope for a
  research-simulation repo; the GitHub-issue workflow + `AskUserQuestion` already are the steering interface.
  This ADR documents and sharpens them rather than replacing them.
- **Make it a biological analytical layer in `simulation-output/` with catalog wiring (ADR-0016 style).**
  Rejected: it contributes no mechanisms or biomarkers and would not belong in a `protocol-vN.md` section.
  It is a methodology doc (`docs/`, alongside docs/08 and docs/10) and wires into the *process* skills
  (pre-output-check, orchestrator-intake), not the catalog schema.
- **Add a fifth "adversarial" vector.** Rejected outright: violates golden rule #8 (vectors are fixed);
  adversarial reasoning is cross-cutting over all four, not a target class.
