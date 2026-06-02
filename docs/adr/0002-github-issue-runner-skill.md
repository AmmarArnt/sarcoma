# ADR-0002: GitHub issue-runner skill (sequential, one-issue-per-run)

- **Status:** Accepted
- **Date:** 2026-06-02
- **Origin:** conversation (user request) — implements the workflow reserved in `CLAUDE.md §8`
- **Deciders:** Ammar Arnautović (maintainer), Claude Code session

## Context

`CLAUDE.md §8` reserved a slot for a dedicated **GitHub-issues skill**: the Issues tab is the
collaboration surface, and the intended workflow is *retrieve issue → apply labels → have Claude Code
respond*, where some responses require team/sub-agent research. Until now that workflow was ad-hoc —
issue #8 was processed by hand (label `Running` → research in a worktree → PR → reply → label
`Responded`). Repeating that manually is error-prone: it is easy to skip the follow-up comment thread,
pollute the working tree, clobber a baseline artifact, or leave an issue stuck mid-flight.

## Decision

Add `.claude/skills/github-issue-runner` — a **manually-invoked** skill that processes **exactly one**
issue per invocation and stops, so the maintainer drains the queue in sequence under their control.
Per run it:

1. Ensures lowercase workflow labels `running` / `responded` exist (idempotent).
2. Selects the single **oldest open** issue labeled neither `running` nor `responded`
   (case-insensitive selection, so legacy capitalized labels and already-done issues are excluded);
   reads the issue **and all comments**.
3. Labels it `running` (the queue lock).
4. Gauges the work via `CLAUDE.md §0/§2` (reuse existing artifacts first; spawn an existing team when
   warranted; a brand-new team requires user consent), and does the analysis/research/simulation under
   the `sarcoma-contract` rules.
5. Does all file work in an **isolated worktree off latest `main`** (`issue-<N>-<slug>`).
6. Runs the **ADR check** (`CLAUDE.md §10`) and writes an ADR if the outcome is framework-level.
7. Opens a PR with the artifacts, **assigned to the maintainer**, never auto-merged.
8. Posts a findings comment on the issue, then relabels `running` → `responded`.

On failure after claiming, it releases the `running` label and comments, so issues are never stranded.

Conventions locked in by this decision:
- **Lowercase** `running` / `responded` are canonical (yellow `#fbca04` / green `#0e8a16`).
- **One issue per invocation**, oldest-first, sequential by design.
- **Worktree isolation** and **new-artifact-not-clobber** are mandatory, inheriting `CLAUDE.md §0/§4/§9`.

## Consequences

- **CLAUDE.md §8 updated** from "a dedicated skill is in progress" to "the `github-issue-runner` skill
  owns this; invoke it manually," cross-referencing this ADR.
- `.claude/skills/README.md` gains a row for the skill.
- Future sessions should defer issue handling to this skill rather than improvising, keeping label
  hygiene, citation verification, and worktree isolation consistent.
- **Trade-offs / what it does NOT do:** it is not scheduled/automated (manual invocation only, matching
  `CLAUDE.md §8`); it processes one issue at a time (no batch); it will not spawn a brand-new
  supplementary team without user sign-off (it falls back to a directly-grounded answer and flags the
  proposed deeper run); it does not merge PRs.

## Alternatives considered

- **Batch all open issues in one run.** Rejected: parallel worktrees/PRs are hard to review, and the
  user explicitly wanted sequential, user-paced processing.
- **No worktree (work on the invoking branch).** Rejected: violates the "don't pollute a good state"
  convention (`CLAUDE.md §9`) and risks mixing unrelated issue work.
- **Reuse the capitalized `Running`/`Responded` labels from the #8 run.** Rejected: the maintainer
  asked for lowercase canonical labels; the skill selects case-insensitively so legacy labels still
  exclude correctly during the transition.
- **A `scripts/` Python CLI instead of a skill.** Rejected: the work is model-driven (judging effort,
  researching, writing prose under the contract), which is a skill's job, not a deterministic script's.
