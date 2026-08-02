# Architecture Decision Records (ADRs)

This directory is the **framework-evolution timeline** for the CIC-rearranged sarcoma simulation. Each
ADR records one *framework-level* decision — why it was made, when, and what it changed — so the project
has an honest history instead of silently mutating. `CLAUDE.md` holds the **current** operating rules;
this log holds **why and when** they changed.

ADRs are **append-only**: once a record is `Accepted` it is not rewritten. If a later decision reverses
or revises it, write a *new* ADR with status `Supersedes ADR-NNNN` (and mark the old one
`Superseded by ADR-MMMM` in its Status line — the one permitted edit to an accepted record).

## When to write one

Write an ADR for a **framework-level** decision — see `CLAUDE.md §10`:
- a new standing deliverable or *type* of simulation/analysis (not a routine re-run);
- a new team, lead, or sub-agent;
- a change to the golden rules, the shared contract, or the conventions;
- a notable methodology choice (e.g. how grounding, ranking, or scoring is done).

Do **not** write one for routine work: answering a question, running an existing sim, fixing a script,
or amending an artifact. Those are just commits.

## How to add one

1. Copy the template below into `NNNN-short-kebab-title.md` with the next number.
2. Fill it in; set `Status: Accepted` (or `Proposed` if pending the user's OK).
3. Link the originating issue/PR.
4. Update the relevant `CLAUDE.md` current-state rule to match, and cross-reference the ADR number.
5. Add a row to the index below.

## Index

| ADR | Title | Date | Status | Origin |
|---|---|---|---|---|
| [0001](0001-missing-data-taxonomy-and-voi-layer.md) | Missing-data taxonomy + biomarker value-of-information layer | 2026-06-02 | Accepted | Issue #7 / PR #15 |
| [0002](0002-github-issue-runner-skill.md) | GitHub issue-runner skill (sequential, one-issue-per-run) | 2026-06-02 | Accepted | Maintainer request |
| [0003](0003-translational-feasibility-layer.md) | Translational feasibility layer (clinical-trial & regulatory awareness) | 2026-06-02 | Accepted | Issue #9 / PR |
| [0004](0004-scoring-axes-and-verification-sources-wiring.md) | Wire scoring axes + verification-source registry into the contract | 2026-06-03 | Accepted | Maintainer request (post #8/#9) |
| [0005](0005-host-biology-modifier-layer.md) | Host-biology treatment-response modifier layer (cross-cutting, not a 5th vector) | 2026-06-03 | Accepted | Issue #10 / PR |
| [0006](0006-immune-watchdog-danger-signaling-expansion.md) | V4 conceptual expansion: danger-signaling / ICD / Nectin-axis + inflammation-state lens | 2026-06-03 | Accepted | Issue #11 / PR |
| [0007](0007-tumorigenesis-reverse-engineering-team.md) | Tumorigenesis / Cell-of-Origin reverse-engineering team + transformation-trajectory sim type | 2026-06-07 | Accepted | Maintainer request |
| [0008](0008-driver-uncertainty-decision-model.md) | Driver-uncertainty (latent-variable) decision-model sim type for fusion-unconfirmed cases | 2026-06-07 | Accepted | Maintainer request |
| [0009](0009-findings-ranking-register.md) | Findings-ranking master register (standing deliverable + maintenance rule) | 2026-06-07 | Accepted | Maintainer request |
| [0010](0010-nightly-needs-attention-requeue.md) | Nightly `needs attention` requeue Action + skill follow-up handling | 2026-06-13 | Accepted | Maintainer request |
| [0011](0011-voi-provenance-temporal-axis.md) | VoI acquisition-provenance & temporal-state axes (Tier-B refinement) | 2026-06-13 | Accepted | Issue #7 follow-up / PR |
| [0012](0012-requeue-exclude-maintainer-comments.md) | Requeue heuristic excludes the maintainer/responder's own comments (refines ADR-0010) | 2026-06-13 | Accepted | Maintainer report (issue #11 false positive) / PR |
| [0013](0013-feasibility-attrition-reason-annotation.md) | Feasibility-layer attrition-reason annotation (R0–R5: why a program closed) — refines ADR-0003 | 2026-06-13 | Accepted | Issue #9 follow-up / PR |
| [0014](0014-evidence-transferability-hierarchy.md) | Evidence-transferability hierarchy (biological-proximity ladder P0–P4) — refines the confidence axis (ADR-0004) | 2026-06-13 | Accepted | Issue #10 follow-up / PR |
| [0015](0015-diagnostic-information-gain-layer.md) | Diagnostic strategy & expected-information-gain layer (test-level VoI, "what to learn next") | 2026-06-14 | Accepted | Issue #31 / PR |
| [0016](0016-full-cycle-ingests-analytical-layers.md) | Full-cycle re-runs ingest the standing analytical layers (orchestrator + vector leads) | 2026-06-14 | Accepted | Maintainer request / PR |
| [0017](0017-hypothesis-steering-adversarial-reasoning.md) | Hypothesis-steering & adversarial-reasoning protocol (reasoning-process layer; standing red-team self-challenge) | 2026-06-14 | Accepted | Issue #32 / PR |
| [0018](0018-therapeutic-modality-layer.md) | Therapeutic-modality layer (delivery-format axis M1–M8, cross-cutting — not a fifth vector) + repurposing & ethnopharmacology sub-scans | 2026-06-14 | Accepted | Issue #33 / PR |
| [0019](0019-oncolytic-virotherapy-m4-deepdive.md) | Oncolytic-virotherapy M4 deep-dive (danger-signal generator) — deepens ADR-0018 via ADR-0006; not a fifth vector | 2026-06-14 | Accepted | Issue #11 follow-up / PR |
| [0020](0020-live-evidence-refresh-lane.md) | Live evidence-refresh + verification lane (catalog updates between full runs; `[VERIFY]`→full-text gate; produced protocol-v4) | 2026-06-25 | Accepted | Maintainer request / issue #33 thread |
| [0021](0021-chemoresponse-cellstate-layer.md) | Treatment-response phenotype as evidence — chemo-sensitivity / DDR cell-state layer (extends ADR-0008; not a fifth vector) | 2026-08-02 | Accepted | Maintainer question (relapse ifosfamide response) |
| [0022](0022-case-baseline-refresh-era-b.md) | **Case-baseline refresh → Era B** (chemo-responsive, Ewing-like, driver-unresolved); establishes `CASE-BASELINE.md` as canonical; Directness becomes posterior-weighted | 2026-08-02 | Accepted | Maintainer instruction |

> **⬆ Era boundary.** **ADR-0001–0020 were written under the Era-A working assumption** that the case was
> canonical **CIC-DUX4** sarcoma. **ADR-0021 onward are Era B** — chemo-responsive, Ewing-like,
> driver-unresolved (`CASE-BASELINE.md`). Per the append-only rule, **no Era-A ADR is retro-edited**: each
> remains an honest record of what was decided under what was known at the time. ADR-0022 §Consequences
> records exactly which Era-A positions changed and which carry forward unchanged.

## Template

```markdown
# ADR-NNNN: <title>

- **Status:** Proposed | Accepted | Superseded by ADR-MMMM
- **Date:** YYYY-MM-DD
- **Origin:** issue #N / PR #N / conversation
- **Deciders:** <who>

## Context
What prompted the decision? What was the problem or the gap in the framework?

## Decision
What we decided to do, concretely. Name the new artifacts / rules / teams introduced.

## Consequences
What this changes — for current rules (which CLAUDE.md sections were updated), for future sessions,
and any new obligations. Include honest trade-offs and what it explicitly does NOT do.

## Alternatives considered
What else was on the table and why it was not chosen.
```
