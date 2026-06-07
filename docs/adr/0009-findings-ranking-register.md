# ADR-0009: Findings-ranking master register (standing deliverable + maintenance rule)

- **Status:** Accepted
- **Date:** 2026-06-07
- **Origin:** Maintainer request — "score every major artifact on the three axes so I have all the findings
  ranked in one place, and add an instruction to keep it maintained."
- **Deciders:** Maintainer + Claude Code session

## Context
The repository now holds many findings spread across `protocol-v1/v2.md`, eight sims, several
cross-cutting layers, the forward-simulation briefs, and the tumorigenesis team. There was **no single
place** to compare them, and "which finding is most promising?" could only be answered by reading
everything. The framework already defines three orthogonal scoring axes (evidence tier / confidence /
feasibility) but had never rolled them up into one cross-artifact view.

## Decision
1. Add a **standing deliverable** `simulation-output/findings-ranking.md`: a master register that scores
   every notable finding on the three axes, groups them (real-data targets / strategic-decision-diagnostic
   / immune / safety-context), and carries a "top picks by criterion" summary plus an explicit
   authorship/recency bias note.
2. Add a **maintenance rule**: when a new sim, team output, or analysis produces a result worth comparing —
   or when a perishable feasibility band changes — its row is added/updated **in the same commit/PR** that
   introduces the artifact. The rule is documented in the file itself and cross-referenced in `CLAUDE.md`
   (§0 reuse list + §4 sim conventions).

## Consequences
- **CLAUDE.md updated:** §0 lists the register as a maintained artifact with the "add a row in the same
  change" instruction; §4 (sim conventions) repeats the trigger so it fires whenever a sim is added.
- **New obligation:** future sessions that add a sim/result must update the register (lightweight: one row,
  three axes, source link, one-line caveat). Mirrors the existing convention that each sim writes
  `RESULTS.md` + updates `sims/00-INDEX.md`.
- **Guardrails baked in:** the register's rule forbids promoting a logic/decision-model finding above a
  real-data finding on evidence strength, keeps the bias note honest, and requires `[re-verify]` tagging of
  perishable regulatory/trial status (golden rule #1). It is a navigation aid, **not** a validated
  instrument and **not** medical advice.
- **What it does NOT do:** it does not change any finding's content, re-rank the catalog's clinical tracks,
  or add a vector/team.

## Alternatives considered
- **Leave rankings implicit in `protocol-v1.md` + `sims/00-INDEX.md`:** rejected — neither spans *all*
  artifacts on *all three* axes, and the question "which is most promising across everything?" had no home.
- **A scored spreadsheet / numeric composite:** rejected — false precision; the axes are deliberately
  ordinal and a single composite would hide the criterion-dependence (the "top picks by criterion" table
  captures that honestly instead).
