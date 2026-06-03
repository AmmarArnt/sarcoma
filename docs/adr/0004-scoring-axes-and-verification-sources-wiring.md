# ADR-0004: Wire the scoring axes + a standing verification-source registry into the always-loaded contract

- **Status:** Accepted
- **Date:** 2026-06-03
- **Origin:** Maintainer request, following issues #8 (confidence scoring → `docs/08`, PR #16) and #9
  (translational feasibility → `simulation-output/translational-feasibility-layer.md` + ADR-0003, PR #18),
  both now merged to `main`
- **Deciders:** Ammar Arnautovic, with Claude Code

## Context

After #8 and #9 merged, the framework had **three** evidence axes — the 7-tier vocabulary (baked into
`sarcoma-contract`), the **confidence** rubric (`docs/08`), and the **translational feasibility** layer
(`simulation-output/translational-feasibility-layer.md`) — but only the first was *reliably picked up*.
The reason is a propagation asymmetry the maintainer identified:

- **Skill content** is reliably loaded by every agent, because each agent's prompt instructs it to load
  the relevant skills (CLAUDE.md §3). That is the only reason the 7-tier vocabulary is dependable.
- **CLAUDE.md §0/§2 pointers** reach *main-thread* sessions (auto-loaded) but **not reliably sub-agents**,
  which start cold and load skills, not necessarily the full CLAUDE.md.
- **Standalone docs** (`docs/08`, the feasibility layer) are inert unless something points to them and the
  reader opens them.

So the confidence axis (PR #16 explicitly *deferred* its wiring) and the feasibility axis were
discoverable by main-thread sessions at best, and **not guaranteed for the sub-agents that produce most
research output.** Separately, issue #9 (@Cerimagic) named a set of authoritative online sources
(ClinicalTrials.gov, EU CTIS, FDA/EMA communications, regulatory approvals & safety notices, recruiting
status); these had been used once for the feasibility layer but were **not recorded as a reusable
resource** — and the tazemetostat withdrawal (2026-03-09) proved that *status is perishable* and must be
re-verified, not trusted across sessions.

## Decision

Operationalize the two newer axes and the source list **into the always-loaded skills** (the reliable
path), keeping the heavy *methods* in their docs (the rule-vs-reference split). Concretely:

1. **`sarcoma-contract` skill** — add a **"Three Scoring Axes"** section (tier / confidence / feasibility),
   explicitly delineating axis-2 "Achievability" (in-vivo PK) from axis-3 "feasibility"
   (development/regulatory access), and stating the two-lane rule (axes annotate the confirmatory lane,
   never prune the forward lane). Extend the **Citation Rules** with a **perishable-status rule**: verify
   any approval/trial/safety status live against the registries in `docs/09`, record source + access date,
   tag `[VERIFY]` if unconfirmed. Methods stay in `docs/08` and the feasibility layer (pointers, not
   copies — the skill exists to avoid duplication).

2. **`sarcoma-pre-output-check` skill** — grows from **8→9** failure modes (new #9: *stale regulatory /
   trial / feasibility status*) and **8→9** mandatory-include items (new #9: *scoring axes beyond tier,
   where they apply*). Frontmatter, headings, and counts updated.

3. **`docs/09-verification-sources.md`** (new) — a standing registry of the authoritative trial /
   regulatory / pharmacovigilance / literature sources from issue #9 (plus those used in ADR-0003), with a
   usage workflow, the FDA≠EMA≠PMDA caveat, the perishability rule, and an explicit contrast with OpenMed
   NER (entity grounding ≠ fact verification). This is the reusable resource the maintainer asked for —
   for all future analysis/sims/research, not the one feasibility run.

4. **CLAUDE.md** — golden rule #1 now names the perishable-status rule + `docs/09`; rule #2 names the
   three axes; §5 distinguishes entity grounding (OpenMed) from fact-checking (`docs/09`); §6 updates the
   `sarcoma-contract` and `sarcoma-pre-output-check` descriptions; §7 repo map adds `docs/08` and `docs/09`.

## Consequences

- **Sub-agents now inherit all three axes + the verification discipline by default**, because the mandates
  live in the two skills every agent loads — closing the propagation gap. The full methods remain
  single-sourced in their docs.
- **A new standing obligation:** any load-bearing status claim must be live-verified against `docs/09` and
  date-stamped; pre-output-check enforces it. Existing artifacts' status facts carry their access date and
  should be re-checked when old and load-bearing (the feasibility layer is explicitly perishable).
- **No existing analytical output was rewritten** — this is contract/skills/docs wiring only. `protocol-v1.md`,
  `docs/08`, and the feasibility layer are unchanged; `protocol-v2` (if ever written) can fold the axes in.
- **Trade-offs / what it does NOT do:** it does not auto-verify anything (no automation; verification is
  still a per-session action), does not re-score existing entries, and does not change the fixed four
  vectors or any tier definition. The source URLs are canonical entry points as of June 2026 and may need
  refreshing if a portal moves.

## Alternatives considered

- **A new dedicated skill for the scoring methods** (e.g. `sarcoma-scoring-axes`). Rejected for the
  *mandate*: a new skill is only as reliable as the instruction to load it, reintroducing the exact
  pickup problem; and it would duplicate `docs/08`. The lean mandate belongs in the skills agents already
  always load. (A future on-demand method skill remains possible if the docs grow unwieldy.)
- **Leave the axes as docs + CLAUDE.md pointers (status quo).** Rejected: that is precisely the gap —
  sub-agents would keep missing them.
- **Bake the full confidence rubric / feasibility table into `sarcoma-contract`.** Rejected: too long and
  too case-specific; violates the skill's anti-duplication purpose. Mandate in the skill, method in the doc.
- **Put the verification sources only in the feasibility layer.** Rejected: the maintainer asked for a
  reusable, framework-wide resource; a top-level `docs/09` referenced from the contract reaches every task,
  not just feasibility questions.
