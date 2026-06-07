# ADR-0008: Driver-uncertainty (latent-variable) decision-model sim type for fusion-unconfirmed cases

- **Status:** Accepted
- **Date:** 2026-06-07
- **Origin:** Maintainer question — "the patient in protocol v1/v2 is fusion-unconfirmed; is it possible to
  create a sim for that given there's another unknown variable?"
- **Deciders:** Maintainer + Claude Code session

## Context
The simulated patient is in the ~5% subgroup that is clinically/histologically CIC-rearranged sarcoma but
has **no confirmed fusion** (golden rule #9). Every prior sim treated the driver as known (fusion = TRUE,
DUX4 transactivation domain present). The maintainer asked whether a sim can be built when the **driver
itself is an unknown variable**. It can — the principled handling of a latent variable is not to guess it
but to marginalize over it and quantify the value of resolving it. This also stress-tests the tumorigenesis
build recipe (ADR-0007): some of its conclusions (notably the MCL1/DUX4-fragility forward hypothesis) are
contingent on the driver actually carrying the DUX4 transactivation domain.

## Decision
Add a **driver-uncertainty decision-model sim type** (`sims/08-driver-uncertainty/`) and a grounding brief
(`simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`):
1. Represent the driver as a latent variable D over five hypotheses (D1 cryptic CIC-DUX4, D2 rare non-DUX4
   partner, D3 non-fusion CIC LOF, D4 phenocopy/misclassified, D5 orphan), each with literature-anchored
   attribute probabilities (DUX4-TAD present? CIC methylation class? fusion junction findable?).
2. **Marginalize** every catalog intervention over a literature-anchored prior p(D) → a robustness ranking
   (driver-agnostic vs driver-contingent).
3. Compute **expected value of sample information (EVSI)** for three resolving tests (DUX4 IHC, methylation
   array, long-read WGS+RNA-seq) — what it is worth to resolve the unknown — reusing the VoI methodology of
   ADR-0001 (Sim 6).
4. **Sweep the prior** (the unknown-about-the-unknown) so conclusions are reported as robust-to-prior.

## Consequences
- **CLAUDE.md updated:** §0 reuse list + §2 effort-gauge row (fusion-unconfirmed / "unknown driver" /
  "what should we test first / value of resolving the driver" questions route here, reuse-first);
  `sims/00-INDEX.md` gains Sim 8.
- **Reusable findings (reuse, don't re-derive):** for the fusion-unconfirmed patient, the throttle/
  cell-cycle/immune vectors (BETi, CDK4/6i, immune/NK, EZH2→MHC-I, p300i) are robust to the driver;
  **the DUX4/MCL1 "re-arm the death program" hypothesis is driver-contingent and should be held until the
  driver is resolved**; **resolving the driver is the highest-value action** (long-read WGS+RNA-seq > DUX4
  IHC > methylation array), reproducing protocol-v1's V3-FH3 from an independent decision-analytic argument.
- **Methodological note:** EVSI (not entropy alone) is used because information has value only when it can
  flip a decision; entropy reduction is reported alongside as a descriptive companion.
- **What it explicitly does NOT do:** it is not a diagnosis, not a treatment recommendation, and not a
  fifth vector. Utilities/penalties are transparent mechanistic judgments, not elicited from a clinician;
  priors carry `[VERIFY]`/`[estimate]` components (hence the mandatory sweep). If the patient's real prior
  testing (DUX4 IHC / methylation / long-read) is known, the prior must be conditioned on it.

## Alternatives considered
- **Pick a single most-likely driver and run Sim 7 on it:** rejected — throws away the uncertainty that is
  the whole point of the question and would over-commit to contingent therapies.
- **Pure entropy/VoI without a decision model:** rejected — for a linear objective, expected information is
  zero; a decision (pursue/regret) is required to make information valuable. EVSI is the correct tool.
- **A new standalone team:** rejected — one grounding brief + a sim reusing ADR-0001/ADR-0007 machinery is
  sufficient; the spawned specialist hit a session limit and the brief was authored in-thread per CLAUDE.md §3.
