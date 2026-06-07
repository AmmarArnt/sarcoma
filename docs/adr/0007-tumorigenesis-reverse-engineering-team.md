# ADR-0007: Tumorigenesis / Cell-of-Origin Reverse-Engineering team + transformation-trajectory sim type

- **Status:** Accepted
- **Date:** 2026-06-07
- **Origin:** Maintainer request ("take a step back: how and why does the cell get into this state —
  what would you do to a stem cell to produce a sarcoma cell, so we can reverse-engineer it")
- **Deciders:** Maintainer + Claude Code session

## Context
The framework had four FIXED attack vectors (V1–V4) and all supplementary work to date (mRNA, host-biology,
VoI, feasibility, V4 expansion) was about *attacking or contextualizing an existing tumor*. None of the
existing teams or artifacts answered the **inverse / forward** question: by what sequence of steps does a
normal mesenchymal stem/progenitor cell *become* a CIC-DUX4 sarcoma cell? V2 (Compiler-Protection) touches
only the narrow translocation-genesis slice (reducing new-translocation rate), not the full transformation
trajectory (cell of origin, driver tolerance, cooperating lesions, epigenetic permissiveness,
immortalization). The maintainer's thesis: a construction recipe, read backwards, is a map of intervention
points and exposes gaps the four vectors don't cover.

## Decision
1. **New supplementary team:** "Tumorigenesis / Cell-of-Origin Reverse-Engineering Team" — a lead
   (reconciler) + four specialist sub-agents, each owning one build layer:
   - Cell-of-Origin (the permissive substrate / developmental window),
   - Driver-Engineering (installing the fusion + the DUX4 apoptosis "fragility window"),
   - Cooperating-Lesions (CDKN2A/TP53 senescence bypass, MCL1 apoptosis buffer, telomere immortalization,
     MYC accelerant),
   - Epigenetic-Permissiveness (open/bivalent chromatin, p300/CBP super-enhancer writing, lock-in).
   It is a **supplementary team, NOT a fifth vector** (golden rule #8 preserved). Its output is a
   reverse-engineering map back onto V1–V4 plus forward hypotheses for the build steps no vector covers.
   Outputs: `simulation-output/tumorigenesis-reverse-engineering/` (lead `tumorigenesis-build-recipe.md`
   + four specialist briefs).
2. **New in-silico sim *type*:** a **Boolean transformation-trajectory model** (`sims/07-tumorigenesis-
   trajectory/`) — literature-parameterized (engine class = sims 03–05), enumerating minimal sufficient
   transformation sets, per-node necessity, and application-order (death-gate) constraints, plus a
   build-step→attack-vector reverse map. This is the forward (construction) counterpart to the existing
   attack-oriented sims.

## Consequences
- **CLAUDE.md updated:** §0 reuse list gains the two new artifacts; the §2 effort-gauge table gains a row
  routing tumorigenesis / cell-of-origin / "how does the cell get into this state" / "reverse-engineer the
  construction" questions to this layer (reuse-first); §3 team table gains the new team row.
- **Key reusable findings (reuse, don't re-derive):** the build recipe is a logical AND of 6 steps,
  5 non-substitutable; the **MCL1/BCL2 apoptosis buffer is a necessary, non-substitutable node** (the DUX4
  death program is p53-independent) → top forward hypothesis "re-arm the fragility"; senescence bypass is
  the one substitutable step (CDKN2A loss empirically, TP53 rare); p300/CBP is the reversible CIC-DUX4-
  specific amplification writer (V3→V4 MHC-I bridge); telomere-maintenance mechanism in CIC-DUX4 is the
  biggest open gap.
- **Honest limits recorded:** logic model ≠ transformation data; no real co-occurrence pull was possible
  (DepMap/cBioPortal egress-blocked this session); OpenMed NER grounding could not run (HuggingFace
  blocked) — `entities.txt` emitted and `grounding.tsv` records the block; several frequencies are
  `[VERIFY]`; the MCL1 paper PMID differs between two briefs (40841513 vs 40841360 — reconcile before use).
- **What it explicitly does NOT do:** it is not a protocol, not medical advice, and does not add a fifth
  vector. Prophylactic "harden the at-risk progenitor" steps are flagged concept-only (not treatments).
- **Forward work when egress allows:** re-pull real CDKN2A/TP53/TERT alteration frequencies from DepMap
  24Q4 / cBioPortal to put data behind the cooperating-lesion nodes; run OpenMed NER grounding.

## Alternatives considered
- **Fold it into V2 (Compiler-Protection):** rejected — V2 is narrowly translocation-genesis/prophylaxis;
  the full transformation trajectory (substrate, driver tolerance, cooperating lesions, epigenetics,
  immortalization) is much broader and would overload V2's contract.
- **A direct single-pass analysis (no team):** offered to the maintainer; they chose the full
  multi-specialist team + sim for multi-angle coverage.
- **Make it a fifth vector:** rejected — violates golden rule #8; it is a reverse-engineering lens that
  maps back onto the existing four, not a new attack surface.
