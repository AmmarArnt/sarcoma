# ADR-0023: Agent model refresh, run-scoped outputs, and portable grounding

- **Status:** Accepted
- **Date:** 2026-11-11
- **Origin:** Maintainer request — "revise the instructions, agent and sub-agent setup and models … they
  are probably outdated … also, hugging face stopped working for the grounding step."
- **Relates to:** ADR-0016 (layer intake), ADR-0020 (`[VERIFY]` gate), ADR-0021/0022 (Era B), ADR-0009.

## Context

1. **Agents predated Era B.** No agent file told agents to read `CASE-BASELINE.md`. Several carried
   Era-A facts: tazemetostat described as approved (its US indications were withdrawn 2026-03-09), EZH2i as
   the MHC-I bridge (`protocol-v4.md` moved it to p300/CBP), the catalog written to `protocol-v1.md`, and
   the chemo-response, modality and oncolytic-virus layers (ADR-0018/0019/0021) missing from the leads'
   and the orchestrator's intake.
2. **Model assignments were sized for an older generation.** Leads and specialists were set to "Sonnet-tier",
   and several files carried compensations aimed at "smaller models" ("do not over-stuff context", "the
   most likely failures from a Sonnet-tier model"). Current models follow instructions more literally, so
   step-by-step choreography and defensive wording now constrain more than they help.
3. **The run gates could not tell a fresh run from an old one.** `dispatch.py gate` / `ready` checked
   unversioned filenames (`v1-summary.md` …) that already exist from the Era-A run, so a fresh cycle would
   pass the gates immediately against stale files, and leads were told to write to those same files,
   overwriting the baseline in breach of CLAUDE.md §0. The v2/v3 runs had avoided this only through
   hand-written instructions (`-v2` / `-v3` suffixes).
4. **Grounding broke outside the original laptop.** `scripts/openmed_ner.py` (a) located `.venv` only
   relative to its own checkout, so it failed with `No module named 'openmed'` in every git worktree (which
   the issue runner and `sim-*` branches use); (b) hard-coded the Apple MLX backend, so it could not run on
   Linux cloud sessions; and (c) in network-restricted sessions huggingface.co returned HTTP 403 with no
   cached weights (recorded in `sims/10-chemoresponse-cellstate/grounding.tsv`, 2026-08-02).

## Decision

- **Models (agent frontmatter `model` + `effort`):** orchestrator → **Fable**, effort high; V1–V4 leads →
  **Opus**, effort high; mRNA lead → **Sonnet**; literature specialists → **Sonnet** (leads pass
  `model: sonnet` when spawning); Metastatic-Disease Specialist → **Opus**. Reasoning: the orchestrator runs
  once per cycle and carries the highest-judgment synthesis; leads do evidence reconciliation where a
  fabricated or mis-tiered citation does the most damage; specialists do scoped, tool-heavy literature
  search.
- **Agent prompts rewritten** to state goal, case context and the reasons behind constraints, with
  `CASE-BASELINE.md` as required first reading for every lead and every spawned specialist. The fixed
  contracts (gates, schemas, skills, NER teams, output paths, track separation, fusion tagging) are
  unchanged. "Sonnet-tier / smaller model" wording was removed from `docs/06`, `sarcoma-contract`,
  `sarcoma-pre-output-check` and `sarcoma-orchestrator-intake`.
- **Run-scoped outputs.** Run N writes `<vector-dir>/<lead>-summary-vN.md`, specialist files under
  `<vector-dir>/vN/`, `metastatic-disease-considerations-vN.md`, and `protocol-vN.md`. `dispatch.py` derives
  N (next protocol version; `SARCOMA_RUN` / `--run` overrides), gates on run-scoped files, and refuses to
  let the orchestrator overwrite an existing `protocol-vN.md`.
- **Portable, offline-first grounding.** `openmed_ner.py` finds the venv via `SARCOMA_VENV`, the checkout,
  or the main worktree; auto-selects MLX or PyTorch; sets `HF_HUB_OFFLINE=1` when every needed model is
  cached; and, when weights are missing and the Hub is unreachable, exits with code 3 and a diagnostic.
  The agent then records grounding as `NOT RUN`, never invented. New `--check` and `--prefetch` modes;
  `dispatch.py check` reports grounding availability as a warning, not a blocker.
- **CLAUDE.md tightened** (≈500 → ≈290 lines): the §0 reuse list and the §2 routing table described each
  layer twice and are merged into one table; stale items were fixed (sims list, pinned commit-trailer
  model, `protocol-v1` paths). Section numbering is preserved so existing `CLAUDE.md §N` references hold.

## Consequences

- The next full cycle is run v5 and cannot overwrite v1–v4 outputs.
- Cost per full cycle rises at the orchestrator (Fable) and leads (Opus), and falls nowhere. To trade cost
  back, edit `model:` in `.claude/agents/orchestrator.md` (fable → opus) first. Evidence discipline does not
  depend on the model choice: the gates, `[VERIFY]` rule and pre-output check are model-independent.
- Network-restricted cloud sessions still cannot download weights. The fix is environmental (allow
  `huggingface.co`, `*.hf.co`, `cas-bridge.xethub.hf.co`, or copy a warmed cache); the script now says so
  instead of failing obscurely.
- Era-A ADRs are not edited (append-only).

## Alternatives considered

- **Opus orchestrator.** Cheaper per token than Fable (Opus 5.5 is $4/$20 per MTok; Fable 5.2, released
  2026-11-09, is reported at ~$8/$40 — verify current pricing before relying on it) and viable. Fable was chosen because the
  orchestrator runs once per cycle and its synthesis is the deliverable. Reversible in one line.
- **Sonnet leads (status quo).** Cheaper, but leads reconcile conflicting evidence tiers and citations, which
  is exactly where this project's documented failures (fabricated citations, the WEE1 retraction) arose.
- **Vendoring NER weights into the repo or a GitHub release.** That would bypass the Hub block, but adds
  ~2.5 GB of third-party weights to a public project; rejected in favour of an allowlist / cache copy.
