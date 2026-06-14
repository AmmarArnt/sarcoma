# ADR-0010: Nightly `needs attention` requeue Action + skill follow-up handling

- **Status:** Accepted
- **Date:** 2026-06-13
- **Origin:** Maintainer request — "a GitHub Action that runs nightly, checks all issues marked
  `responded` but with a more recent response in the thread (most likely by the original author), and
  marks it `needs attention`; the issue-runner skill should also check for and action
  `needs attention` issues."
- **Deciders:** Maintainer + Claude Code session

## Context

The `github-issue-runner` skill (ADR-0002) drains the issue queue one at a time: pick the oldest
unlabeled open issue, do the work, post findings, label `responded`. Once `responded`, an issue is
considered done and the skill never revisits it. But if the original author (or anyone) posts a
follow-up comment — a clarifying question, a correction, "can you also check X" — nothing surfaces
that. The issue sits `responded` indefinitely while a live follow-up goes unanswered, and the queue
keeps moving on to newer issues instead.

`CLAUDE.md §8` previously said: *"Don't improvise issue handling in general sessions or build
scheduled automation — defer to the skill."* This ADR narrowly reverses that for one specific,
low-risk case.

## Decision

1. **New label `needs attention`** (lowercase, color `d93f0b`) — a fourth queue state alongside
   unlabeled / `running` / `responded`. Meaning: "Claude already responded, but someone replied since
   — re-process this issue." Created idempotently by both the new Action and the skill's Phase 0, so
   neither depends on a manual setup step.

2. **New nightly Action** `.github/workflows/issue-needs-attention.yml`:
   - Triggers on a nightly cron (`17 7 * * *` UTC — off the top of the hour to avoid GitHub's
     scheduler pileup at `:00`) and `workflow_dispatch` (manual testing).
   - For each open issue labeled `responded`, compares the timestamp of the most recent
     `labeled: responded` event against the timestamp of the most recent comment **not** from
     `github-actions[bot]`.
   - If the comment is newer, swaps the labels: `responded` -> `needs attention`.
   - This is a **relabel-only** action. It never comments, opens PRs, or does research — that stays
     entirely inside the manually-invoked skill.
   - Because the skill posts its findings comment *before* applying the `responded` label (Phase 7),
     the findings comment itself can never retroactively trigger this — only a comment posted
     *after* `responded` was applied does.

3. **Skill changes** (`.claude/skills/github-issue-runner/SKILL.md`):
   - **Phase 0** also creates the `needs attention` label.
   - **Phase 1** becomes a two-pool selection: Pool A = oldest open issue labeled `needs attention`
     (processed first — someone is waiting on a reply); Pool B = oldest open issue with none of
     `running` / `responded` / `needs attention` (the previous behavior, now the fallback). For a
     Pool A issue, the newest comment(s) are read as the actual ask for this run.
   - **Phase 2** (claim): a Pool A issue has `needs attention` removed and `running` added in the
     same edit.
   - **Phase 7** (close-out): the label flip now strips both `running` and `needs attention` and
     adds `responded` — returning the issue to a state the nightly Action can flag again if the
     author replies a *second* time. The cycle is repeatable indefinitely.
   - **Failure handling**: if a Pool A issue can't be completed, `needs attention` is restored (in
     addition to removing `running`) so it returns to the follow-up queue rather than becoming
     indistinguishable from a brand-new issue.

## Consequences

- **`CLAUDE.md §8` updated**: the "no scheduled automation" line is narrowed to "no *other* scheduled
  automation" — this one Action is explicitly sanctioned because it does nothing but relabel, and all
  actual issue work still funnels through the manually-invoked skill (preserving the
  user-paced/sequential guarantee from ADR-0002).
- **New obligation**: the repo now has a `.github/workflows/` directory and depends on the default
  `GITHUB_TOKEN` having `issues: write` permission (granted via the workflow's `permissions:` block —
  no new secrets needed).
- Queue state is now four-valued instead of three-valued; anyone reading issue labels should know
  `needs attention` means "was answered, but needs a fresh look," not "new."
- **What this does NOT do**: it does not change how the skill does research, what teams it spawns, the
  contract/golden rules, or PR/assignment behavior. It adds no new automation that posts content,
  comments, or opens PRs — only the existing manually-invoked skill does that.

## Alternatives considered

- **Add-only label (keep `responded` + add `needs attention`)**: rejected in favor of a clean swap —
  a single-valued state is simpler to query (`gh issue list --label "needs attention"`) and avoids the
  skill needing a "needs-attention overrides responded" special case during selection.
- **Strict oldest-first across both pools** (ignore label, just sort by `createdAt`): rejected —
  follow-ups represent someone actively waiting on a reply to something already promised; prioritizing
  them is more responsive than treating them the same as a brand-new, never-touched issue.
- **Require the follow-up comment's author to differ from the maintainer**: rejected as an extra
  signal that isn't needed — the ordering guarantee (comment posted *before* the `responded` label in
  Phase 7) already prevents the skill's own findings comment from self-triggering, so the simpler
  "any non-bot comment newer than the label" rule suffices.
- **Have the nightly Action also do the re-processing (full automation)**: rejected — out of scope and
  contrary to ADR-0002's "user-paced, sequential" design; the Action only re-queues, a human still
  decides when to re-invoke the skill.
