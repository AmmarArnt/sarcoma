# ADR-0006: V4 conceptual expansion — danger-signaling / ICD / Nectin-axis + the inflammation-state lens

- **Status:** Accepted
- **Date:** 2026-06-03
- **Origin:** Issue #11 (@Cerimagic, *"Immune Watchdog Expansion: Immunogenic Signaling, NK Surveillance, and Danger Recognition"*) + its two follow-up comments → PR
- **Deciders:** Ammar Arnautovic, with Claude Code

## Context

V4 (Immune Watchdog) was built around four sub-agent angles — checkpoint/T-cell, NK, microbiome-immune,
neoantigen-vaccine — and its existing output (`v4-summary.md` + four sub-agent files) covers MHC-I
restoration, NK missing-self, checkpoint blockade, and personalized vaccines well. Issue #11 asked
whether the *conceptual space* of V4 should be broadened to innate **danger recognition** — DAMPs,
immunogenic cell death (ICD), HSP70/HSP90 chaperone-signals, HMGB1/calreticulin, stress-induced immune
visibility — and the **Nectin / TIGIT / NK-surveillance axis** (explicitly naming NTX1088). It also made
a sharper methodological point: the framework should **not treat "reducing inflammation" as equivalent
to "improving anti-tumor immunity,"** and should distinguish **tumor-promoting inflammation**,
**anti-tumor immune activation**, and **treatment-related inflammatory toxicity** as separate states.

The existing files touched fragments of this (ICD/HMGB1/STING in the radiation context in
`tcell-surveillance.md`; DNAM-1 ligands PVR/Nectin-2 as *activating* in `nk-cell-activation.md`) but
**did not develop the inhibitory Nectin axis, ICD as a chemotherapy-driven adjuvant strategy, HSP/DAMP
biology, NK exhaustion/HLA-E, or any inflammation-state disambiguation**, and named no standing place
for them in the framework.

## Decision

Treat this as an **incremental expansion of V4's conceptual scope — explicitly NOT a fifth vector**
(golden rule §8; same resolution as ADR-0001/ADR-0005). Two concrete additions:

1. **One new artifact:** `simulation-output/v4-immune-watchdog/immune-watchdog-expansion.md`. It (a)
   answers issue #11's four questions directly; (b) catalogs the danger-signal/ICD module (calreticulin,
   doxorubicin-as-ICD-inducer, HMGB1/TLR4, ATP/P2RX7/NLRP3, HSP70/90, cGAS-STING), the Nectin-axis
   module (DNAM-1 / TIGIT / CD96 / PVRIG, the **failed** anti-TIGIT phase-3 programs, and NTX1088
   anti-PVR), and the NK exhaustion / NKG2D-ligand-shedding / NKG2A-HLA-E module — each with mechanism,
   evidence tier, and the confidence + feasibility axes; and (c) carries three CIC-DUX4-specific Forward
   Hypotheses.

2. **A standing analytical lens — "inflammation-state disambiguation":** every V4 (and host-biology /
   anti-inflammatory) output should, where it touches inflammation, distinguish the three states above,
   because an intervention helpful for one can be neutral or harmful for another. This is **qualitative
   discipline, reusing the existing three scoring axes** (ADR-0004) for weighting — **no new score** is
   introduced.

Evidence integration follows the **two-lane rule**: these mechanisms enter the confirmatory lane only
where real clinical evidence exists (almost all of it *outside* sarcoma → confidence/transfer axis
down-weighted; the anti-TIGIT phase-3 *failures* are recorded as a cautionary floor, not pruned), while
CIC-DUX4-specific application stays in the Forward-Hypotheses lane.

## Consequences

- **CLAUDE.md updated:** §0 reuse-inventory now lists `immune-watchdog-expansion.md`; §2 effort-table
  gains a row routing immune-visibility / danger-signaling / ICD / DAMP / Nectin-TIGIT / NK-surveillance /
  "distinguish inflammation states" questions to this artifact (reuse-and-extend, not re-derive).
- **`docs/adr/README.md`** index gains this row.
- **No existing analytical output was rewritten.** The expansion *points to and extends* the four V4
  sub-agent files; `v4-summary.md` and `protocol-v1.md` are unchanged. A future `protocol-v2` could fold
  the modules in as V4 annotations.
- **One perishable-status correction is recorded (not a biology change):** `v4-summary.md` names
  tazemetostat as the "cleanest V3→V4 MHC-I bridge"; tazemetostat was **withdrawn from all markets
  2026-03-09** (Ipsen, secondary malignancies). The EZH2i *mechanism* stands; the *agent* is no longer
  accessible and any MHC-I-priming hypothesis must reroute (valemetostat / HDACi). This reinforces the
  contract's "regulatory status is perishable — verify live" rule (ADR-0004).
- **Atypical-case note is *relieved*:** every mechanism added is fusion-agnostic, so the expansion applies
  unchanged to the ~5% fusion-unconfirmed subgroup.
- **Guardrails preserved/strengthened:** the inflammation-state lens makes the existing antioxidant/
  anti-inflammatory hazards (V2 ATBC/CARET/SELECT/NAC; ADR-0005 "direction not assumed beneficial")
  mechanistically explicit — a blanket "lower inflammation" can move tumor-promoting *and* anti-tumor
  states the wrong way at once. The one SOC-adjacent claim (doxorubicin = ICD inducer) is flagged
  mechanistic/theoretical and explicitly *not* a dosing or steroid/antioxidant instruction.
- **Trade-offs / what this does NOT do:** it does not claim any of these mechanisms changes CIC-sarcoma
  outcomes (none is CIC-DUX4-validated); it adds no vector and no sub-agent; it does not resurrect
  anti-TIGIT monoblockade. Several mechanistic anchors (HSP70 DAMP, CD96/PVRIG, NKG2A/HLA-E, the Galon
  and Hanahan–Weinberg references) are cited by concept with the PMID deliberately left unasserted /
  `[VERIFY]` rather than fabricated.

## Alternatives considered

- **A fifth attack vector ("V5 Innate / Danger").** Rejected — fixed-four-vectors constraint (golden rule
  §8); danger-signaling and the Nectin axis are *part of immune visibility/clearance*, i.e. squarely
  inside V4, not a parallel attack.
- **A new supplementary research team (spawn v4-lead + 4 specialists fresh).** Considered per CLAUDE.md
  §2/§3 and is the textbook fit, but the question was a conceptual-broadening + bounded-citation-
  verification task answerable by **reusing** the existing V4 artifacts and live-verifying a small anchor
  set; a full wave re-run was not warranted on cost-discipline grounds (CLAUDE.md §0) and the practical
  background-dispatch caveat (§3). A deeper team run (e.g. a dedicated NK / ICD-scheduling deep-dive)
  remains available if the maintainer wants it — flagged in the PR.
- **A new inflammation/danger scoring scheme.** Rejected — ADR-0004's three axes already weight this; the
  inflammation-state lens is qualitative discipline, not a fourth score.
- **Folding the content into `v4-summary.md` directly.** Rejected — golden rule (CLAUDE.md §0 / Phase 5):
  write a new artifact, preserve the baseline run.
