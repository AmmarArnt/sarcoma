---
name: github-issue-runner
description: Manually-invoked workflow that processes exactly ONE GitHub issue end-to-end for the CIC-rearranged sarcoma repo. Picks up the oldest issue labeled `needs attention` (an author follow-up on something Claude already answered), or — if none — the oldest open issue not labeled `running`, `responded`, or `needs attention`. Labels it `running`, does the analysis/research/simulation the issue (and its full thread) asks for (reusing existing artifacts and the sarcoma-* skills, spawning a team only when warranted), opens a PR with the artifacts assigned to the maintainer, posts the findings as an issue comment, then relabels the issue `responded`. Runs one issue per invocation and stops, so the user can drive the queue in sequence. All file work happens in an isolated git worktree off the latest `main`. Invoke when the user asks to "process / pick up / work the next GitHub issue."
---

# GitHub Issue Runner

Process **one** issue, top to bottom, then **stop**. The user re-invokes this skill for the next issue,
so the queue is drained in sequence under their control. This is the dedicated GitHub-issues workflow
referenced in `CLAUDE.md §8`; see `docs/adr/0002-github-issue-runner-skill.md` for the rationale and
`docs/adr/0010-nightly-needs-attention-requeue.md` for the `needs attention` follow-up state.

> A nightly GitHub Action (`.github/workflows/issue-needs-attention.yml`) scans `responded` issues for
> new non-bot comments (typically the original author replying) and swaps `responded` ->
> `needs attention`. This skill's Phase 1 treats `needs attention` issues as the **highest-priority**
> pool — someone is waiting on a reply to something already answered.

> **Non-negotiable:** every artifact you produce obeys the golden rules in `CLAUDE.md §1` and the
> `sarcoma-contract` skill — no fabricated citations, evidence tier on every claim, mechanism before
> recommendation, a "what I could not establish" section, SOC-interaction flags, the atypical-case flag,
> and "not medical advice." This skill governs *workflow*; the contract governs *content*. Load
> `sarcoma-contract` before producing any research output.

---

## Phase 0 — Preflight

1. Confirm you are in the repo and `gh` is authenticated:
   ```bash
   gh auth status >/dev/null && gh repo view --json nameWithOwner --jq .nameWithOwner
   ```
2. Capture the maintainer (PR assignee) — the authenticated user / repo owner:
   ```bash
   gh api user --jq .login
   ```
3. Ensure the three **lowercase** workflow labels exist (idempotent — ignore "already exists"):
   ```bash
   gh label create running         --color fbca04 --description "Claude Code is actively working this issue" 2>/dev/null || true
   gh label create responded       --color 0e8a16 --description "Claude Code has acted and responded"        2>/dev/null || true
   gh label create "needs attention" --color d93f0b --description "Author replied after Claude responded - re-process this issue" 2>/dev/null || true
   ```
   The canonical labels are lowercase `running` / `responded` / `needs attention`. If legacy
   capitalized variants (`Running` / `Responded`) exist from earlier runs, treat them as equivalent for
   *selection* (Phase 1 excludes both cases) but only ever *apply* the lowercase ones.

---

## Phase 1 — Select exactly one issue (needs-attention first, then oldest unclaimed)

Two pools, checked **in order**. Stop at the first non-empty pool.

**Pool A — follow-ups (`needs attention`), oldest first.** These are issues Claude already
`responded` to, where the nightly requeue action (`docs/adr/0010`) detected a newer non-bot comment —
most likely the original author replying to the answer:

```bash
gh issue list --state open --label "needs attention" --limit 200 --json number,title,createdAt --jq '
  sort_by(.createdAt) | .[0] // empty'
```

**Pool B — brand-new, oldest first.** Only if Pool A is empty. The single **oldest open** issue whose
labels include **none** of `running`, `responded`, `needs attention` (case-insensitive, so legacy
capitalized labels and the already-done issue #8 are excluded):

```bash
gh issue list --state open --limit 200 --json number,title,createdAt,labels --jq '
  map(select(
    ([.labels[].name | ascii_downcase]
      | any(. == "running" or . == "responded" or . == "needs attention")) | not
  )) | sort_by(.createdAt) | .[0] // empty'
```

- **If both pools are empty:** report "No unclaimed open issues — queue is clear." and **stop**. Do not
  create labels-only churn, branches, or PRs.
- **Otherwise:** note the issue number `N` and which pool it came from. Read it **completely**,
  including every comment — issue #8 carried its most important requirement in a follow-up comment, so
  never skip the thread:
  ```bash
  gh issue view N --json number,title,body,author,createdAt,labels,comments
  ```
  For a **Pool A** issue, the newest comment(s) — typically from the original author — are the new
  requirement to address; treat the original body + earlier responses as context, and the follow-up
  comment as the actual ask for this run.

---

## Phase 2 — Claim it

Apply the lock label immediately, so a second run (or a human) sees it is taken. If the issue came from
**Pool A**, also remove `needs attention` in the same edit (it's been picked up):

```bash
# Pool B (brand-new):
gh issue edit N --add-label running

# Pool A (needs attention):
gh issue edit N --remove-label "needs attention" --add-label running
```

If anything later fails before you reach Phase 7, you must **release** the lock (see "Failure handling"
at the bottom) — never leave an issue silently stuck in `running`.

---

## Phase 3 — Gauge the work (reuse first; CLAUDE.md §0 + §2)

Before producing anything, decide what the issue actually needs, using `CLAUDE.md §2`:

| The issue is… | Do this |
|---|---|
| Answerable from existing artifacts | Read & cite `simulation-output/` and `sims/`; extend incrementally. **Do not re-run the wave cycle.** |
| A simple factual / "why" question | Answer it directly and thoroughly; no spawning. |
| A framework / design / docs / coding task (like #8) | Do it directly in the worktree; produce a design doc / artifact. |
| Genuine multi-angle research that an **existing** team fits (`v1`–`v4`, `mrna-vaccine`, orchestrator) | Spawn that team per `CLAUDE.md §3`, write a **new** artifact (e.g. `protocol-v2.md`, a dated file), never clobber. |
| Research needing a **brand-new** supplementary team | This is the one case requiring consent: **pause and ask the user** (`AskUserQuestion`) before spawning — `CLAUDE.md §2/§3` require sign-off for a new team. If they decline or are unavailable, deliver the best directly-grounded analysis you can and note in the PR/response that a deeper team run is proposed and awaiting approval. Do not block the whole issue on it. |

Always prefer reuse over re-running (cost discipline). Identify which existing artifacts bear on the
issue and cite them.

---

## Phase 4 — Isolated worktree (never pollute the current tree)

Do **all** file work for this issue in a fresh worktree off the latest `main`:

```bash
git fetch origin main
SLUG=<short-kebab-summary>                       # e.g. evidence-confidence-scoring
git worktree add -b issue-N-$SLUG ../sarcoma-issue-N origin/main
```

Work inside `../sarcoma-issue-N` from here on. Branch name: `issue-<N>-<slug>`. (This mirrors the
worktree discipline in `CLAUDE.md §4/§9`.)

---

## Phase 5 — Do the work

Produce the artifacts the issue calls for, in the worktree, following the contract:

1. Load `sarcoma-contract` (rules) and any role/vector skills you need
   (`sarcoma-vector-context`, `sarcoma-output-schema`, `sarcoma-chemo-interactions`).
2. **Verify every external fact** (PMID / NCT / DOI / accession) against a live source with
   `WebSearch` / `WebFetch` before asserting it. If you cannot verify, write
   `[no direct citation; …]` or `[VERIFY]` — never invent a reference. (This is how the #8 Halassy
   citation was caught and corrected.)
3. **Write new artifacts; do not overwrite** existing outputs unless the issue explicitly asks for an
   overwrite. New analysis → a new dated/numbered file (e.g. `docs/NN-*.md`, `protocol-v2.md`,
   `sims/NN-*/`). Preserve the baseline.
4. Run `sarcoma-pre-output-check` before finalizing any research artifact.
5. **ADR check (`CLAUDE.md §10`):** if the issue's outcome is a *framework-level* decision — a new
   standing deliverable/sim type, a new team/agent, a change to the golden rules/contract/conventions,
   or a notable methodology choice — append a new ADR in `docs/adr/` (copy the template in
   `docs/adr/README.md`, next number, `Status: Accepted`, link issue #N and the PR), update the
   affected `CLAUDE.md` rule, and add a row to the ADR index. Routine answers/sims/bug-fixes do **not**
   get an ADR.

---

## Phase 6 — Open the PR (assigned to the maintainer)

From the worktree:

```bash
git add -A
git commit -m "<concise title> (issue #N)

<what + why, a few lines>

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push -u origin issue-N-$SLUG
gh pr create --base main --head issue-N-$SLUG \
  --assignee <maintainer-login> \
  --title "<title> (issue #N)" \
  --body "<What / the answers / contents / verification notes. End with the Claude Code attribution line.>"
```

- Assign the maintainer from Phase 0. (GitHub blocks requesting yourself as a *reviewer* when you are
  the PR author, so use `--assignee`, not `--reviewer`, when the author and maintainer are the same
  account.)
- **Never auto-merge.** The PR is for the maintainer's review.
- PR body should state what was produced, summarize the findings, and note any `[VERIFY]` items and
  what was deferred (e.g. an implementation deferred to sign-off, or a proposed new-team run).

---

## Phase 7 — Respond in the issue, then close out the labels

1. Post a findings comment on the issue — same standard as the #8 reply: lead with the direct answer to
   each question the issue/thread asked, link the PR, be explicit about evidence tiers and what you
   could **not** establish, and end with "*research-simulation note, not medical advice.*"
   ```bash
   gh issue comment N --body "<findings + PR link + honest limits>"
   ```
2. Flip the labels (remove the lock, mark done). Also strip `needs attention` if present (defensive —
   it should already be gone from Phase 2, but `gh issue edit --remove-label` is a no-op if the label
   isn't there, so this is safe either way) — this returns the issue to plain `responded`, which the
   nightly requeue action (`docs/adr/0010`) can flag again the next time someone replies:
   ```bash
   gh issue edit N --remove-label running --remove-label "needs attention" --add-label responded
   ```
3. Report back to the user: issue number + title, the PR URL, the artifacts created, and the worktree
   path (`../sarcoma-issue-N`). Note the worktree/branch is preserved for any PR revisions and can be
   removed with `git worktree remove ../sarcoma-issue-N` once the PR merges.

Then **stop.** One issue per invocation. The user re-runs the skill for the next.

---

## Failure handling (do not strand an issue)

If you cannot complete the work after claiming it in Phase 2:

- Post a comment on the issue explaining the blocker honestly (what you tried, what is missing).
- **Remove the `running` label** so the issue returns to the queue
  (`gh issue edit N --remove-label running`).
- **If this issue came from Pool A** (`needs attention`), restore that label so it goes back to the
  follow-up queue rather than becoming indistinguishable from a brand-new unlabeled issue:
  `gh issue edit N --add-label "needs attention"`.
- Do not apply `responded`. Do not open a half-baked PR.
- Tell the user what blocked you. If a worktree was created, leave it and report its path so work can resume.

## Guardrails recap

- One issue per run. Queue state is four lowercase labels: unlabeled (new) / `needs attention`
  (follow-up) / `running` (locked) / `responded` (done). Selection order: `needs attention`
  (oldest first), then unlabeled (oldest first) — see Phase 1.
- A nightly Action (`docs/adr/0010`, `.github/workflows/issue-needs-attention.yml`) is the only
  sanctioned scheduled automation; it only swaps `responded` -> `needs attention` on issues with a
  newer non-bot comment. It never does research, comments findings, or opens PRs.
- Reuse existing artifacts before spawning anything; new team only with user consent.
- Isolated worktree off latest `main`; never touch the tree you were invoked from.
- No fabricated citations; verify accessions; evidence tier + mechanism + "could not establish" on all research.
- New artifacts, never clobber; ADR for framework-level changes only.
- PR assigned to the maintainer, never auto-merged; findings posted to the issue; "not medical advice."
