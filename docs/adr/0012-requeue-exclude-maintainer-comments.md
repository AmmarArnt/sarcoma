# ADR-0012: Requeue heuristic excludes the maintainer/responder's own comments

- **Status:** Accepted
- **Date:** 2026-06-13
- **Origin:** maintainer report (issue #11 false-positive requeue) / PR (fix-requeue-maintainer-exclusion)
- **Deciders:** maintainer (AmmarArnt), Claude Code
- **Refines:** [ADR-0010](0010-nightly-needs-attention-requeue.md)

## Context

[ADR-0010](0010-nightly-needs-attention-requeue.md) introduced the nightly
`issue-needs-attention.yml` Action: for each open issue labeled `responded`, it compares the timestamp
of the most recent **non-bot** comment against the time the `responded` label was applied, and swaps
`responded` → `needs attention` when a comment is newer (the intended signal: "the original author
replied after Claude answered, so re-queue it").

The "non-bot" filter excluded only `github-actions[bot]`. But **the github-issue-runner skill posts its
findings reply — and the maintainer posts any manual follow-up — as the authenticated maintainer
account** (the repo owner, `AmmarArnt`), **not** as the bot. So a maintainer comment posted *after* the
`responded` label was indistinguishable from an author reply.

This produced a **false positive on issue #11**: its newest comment was a maintainer cross-issue
follow-up ("following up across all five issues you opened #7–#11", 2026-06-03 17:20 UTC), posted after
the `responded` label (12:06 UTC). The first run of the Action (manually dispatched 2026-06-13) requeued
#11 even though no third party had replied. (#7/#9/#10 were *correct* requeues — genuine author
follow-ups from @Cerimagic on 2026-06-12.)

## Decision

The "newer comment" test now excludes **both** `github-actions[bot]` **and the repo owner**
(`${{ github.repository_owner }}`, exported as `$OWNER`). The trigger is redefined from *"a newer
non-bot comment"* to *"a newer comment from someone other than the responder"* — i.e. a genuine
third-party/author reply.

Concretely, in `.github/workflows/issue-needs-attention.yml` the `last_comment_at` selector became:

```jq
[.[][] | select(.user.login != "github-actions[bot]" and .user.login != $owner) | .created_at]
| sort | last // empty
```

with `OWNER: ${{ github.repository_owner }}` in the job env. Header/inline comments and the step name
were updated to document the rationale.

Validated against live issues before merge: the fixed logic flags only #9 and #10 (real @Cerimagic
follow-ups) and correctly leaves #7, #8, and #11 as `responded`.

## Consequences

- Eliminates the maintainer-self-comment false positive. The skill's own Phase-7 findings reply (posted
  as the maintainer just before the `responded` label) also can no longer trip the next night's run.
- **CLAUDE.md §8** updated to state that the Action excludes the maintainer's own comments, not just the
  bot's.
- ADR-0010 stays the baseline; this ADR refines its heuristic (no behavioral change to *what the Action
  does* — only to *when it fires*). The workflow still ONLY relabels; it never comments or opens PRs.
- **Assumption / limitation:** the responder is assumed to be the **repo owner**. If responses are ever
  posted by a different maintainer/collaborator account, that login must be added to the exclusion (noted
  inline in the workflow). A genuine reply from any *other* account (including a different collaborator)
  still correctly triggers `needs attention`.

## Alternatives considered

- **Compare the newest comment's author to the actor who applied the `responded` label.** More general
  (handles multiple maintainers) but more complex and brittle — label-event actor history is noisier than
  a single owner check, and the legacy `Responded`→`responded` rename already complicates that history.
  Rejected for now in favour of the simpler owner exclusion.
- **Exclude any `*[bot]` login generically.** Orthogonal — does not address the real cause (the responder
  is a human/maintainer account, not a bot). Not adopted.
- **Have the skill post findings as a bot account.** Larger change to the skill's auth model; the owner
  exclusion is a smaller, self-contained fix.
