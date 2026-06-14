# ADR-0019: Oncolytic-virotherapy M4 deep-dive (danger-signal generator) — deepens ADR-0018 via ADR-0006

- **Status:** Accepted
- **Date:** 2026-06-14
- **Origin:** Issue #11 follow-up comment (@Cerimagic, 2026-06-13, *"Oncolytic Viruses as Artificial Danger-Signal Generators"*) / PR
- **Deciders:** Maintainer (AmmarArnt) + issue-runner session

## Context

The therapeutic-modality layer (ADR-0018) logged the **M4 (gene/viral) cell as "Absent"** in the catalog and
named oncolytic virus as the highest-conceptual-value M4 forward item, but did not work it through. The #11
follow-up asked the framework to treat oncolytic viruses specifically as **in-situ "danger-signal generators"**
(an "artificial alarm system" converting an immunologically quiet tumour into a visible one), to score the
named platforms (T-VEC, RP1/RP2/RP3, OH2, VG161, reovirus/pelareorep, NDV, Seneca Valley Virus), and to map
**real-world translational feasibility / accessibility** (regulatory status by region, trials, companies,
compassionate-use routes, the investigator/institution ecosystem, and the Beata Halassy N-of-1 case).

This sits at the intersection of two existing layers: the **V4 danger-signal / ICD biology** (ADR-0006, which
already owns DAMPs/PAMPs/calreticulin/HMGB1/ATP/type-I-IFN) and the **M4 modality cell** (ADR-0018). It needed
deepening, not new biology and not a new axis.

## Decision

Add a standing deliverable **`simulation-output/oncolytic-virotherapy-danger-signal-layer.md`** that:
1. Adopts the contributor's **effector-strength vs. recognition/visibility** distinction as standing V4
   language, and places OV predominantly on the *recognition* axis (raising both antigenicity and adjuvanticity).
2. Scores each named OV platform honestly (tier · Directness/confidence · F-band), with the **one positive
   sarcoma signal** (T-VEC + pembrolizumab phase-2, ORR 30%, NCT03069378) and the **disconfirming nearest
   evidence** (Ewing/round-cell lines among the *least* OV-susceptible; H-1PV failed in vivo in Ewing; **no
   CIC-DUX4 OV data**) given equal prominence (golden rule §5).
3. Maps real-world accessibility (T-VEC the only US/EU-approved OV; **RP1 rejected by FDA twice, incl.
   2026-04-10**; OH2/VG161 China-centred; deep/visceral CIC-DUX4 anatomy as the dominant intralesional-access
   limiter), and answers the "nearest real-world path" question for a clinician conversation.
4. Carries forward-hypotheses with falsifiers (gating tropism screen; reovirus×MAPK), SOC-interaction flags,
   the fusion-agnostic atypical-case note, a "could not establish" section, and an ADR-0017 red-team pass.

**It is explicitly NOT a fifth vector and NOT a new scoring axis** — it is a modality-cell deepening. Modality
moves only the feasibility axis (ADR-0018); evidence tier/confidence are set by biology/Directness (ADR-0014).

## Consequences

- **CLAUDE.md updated:** new bullet in §0 reuse list; new routing row in §2; repo-map mention in §7.
- **Wiring (ADR-0016):** this slots cleanly **under the already-wired therapeutic-modality ingestion path**
  ("all vector leads ← modality layer") — no new ingestion behaviour is required; the modality layer's M4 row
  and §9 now cross-reference this deep-dive so a fresh full cycle inherits it through ADR-0018. Noted in the PR
  rather than raised as a blocking wiring question.
- **findings-ranking.md:** one row added (immune-program group) recording the honest mixed result.
- **What it does NOT do:** it asserts **no** OV efficacy in CIC-DUX4 (Directness `Low`/`None`; the nearest data
  are discouraging); it endorses neither the Halassy self-experiment nor any compassionate-use route; all
  regulatory/trial statuses are perishable and date-stamped for live re-verification (ADR-0003 / docs/09).

## Alternatives considered

- **A full v4-lead team re-run.** Rejected: the V4 immune biology already exists (ADR-0006); the task was a
  focused modality deepening + live feasibility verification, better done as one disciplined artifact than a
  4-specialist spawn (cost discipline, CLAUDE.md §0).
- **Folding it into the modality-layer file as an M4 paragraph.** Rejected: the platform/feasibility/ecosystem
  detail and forward-hypothesis set warranted its own deliverable; the modality layer now cross-references it.
- **A new "delivery/visibility" axis or fifth vector.** Rejected — violates golden rule §8 and ADR-0018's
  load-bearing rule; the effector-vs-visibility split is captured as V4 *language*, not a new score.
