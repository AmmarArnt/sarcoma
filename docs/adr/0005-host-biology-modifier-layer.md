# ADR-0005: Host-biology treatment-response modifier layer

- **Status:** Accepted
- **Date:** 2026-06-03
- **Origin:** Issue #10 (@Cerimagic, *"Host Biology and Treatment Response Modifiers"*) → PR
- **Deciders:** Ammar Arnautovic, with Claude Code

## Context

The framework was tumour-intrinsic by construction: the four fixed attack vectors all target the cancer
cell (throttle the loop, reduce translocation risk, restore suppressor/differentiation, restore immune
clearance). Issue #10 raised the translational-medicine point that treatment response is an emergent
property of **tumour × host × therapy**, and that host-level factors — gut microbiome / SCFA, systemic
inflammation, metabolic and nutritional status, physical activity, sleep/circadian biology, autonomic
(β-adrenergic) tone, psychological stress / PNEI / placebo-nocebo, and perioperative immune conditioning
— can modulate response, tolerance, and immune competence largely *independently of the tumour's own
biology*. The contributor asked four questions: should host factors be a separate layer; do they explain
inter-patient variability; which have sufficient evidence; and how should their evidence be weighted
against tumour-targeted evidence.

The existing artifacts touched parts of this (microbiome/SCFA in `v4-immune-watchdog/microbiome-immune.md`;
anti-inflammatory work in `v2-compiler-protection/`) but nothing decided *where host biology sits in the
framework* or *how to weight it*, and several named factors (exercise, sarcopenia/metabolic reserve,
nutrition, sleep/circadian, ANS, PNEI, placebo/nocebo, perioperative conditioning) were uncatalogued.

## Decision

Add a **standing cross-cutting modifier layer**, **not a fifth attack vector** (golden rule §8 — the four
vectors remain fixed; this is the same resolution issue #7 received as the VoI layer, ADR-0001). One
artifact:

- **`simulation-output/host-biology-modifier-layer.md`** — the framework-layer deliverable. It (1) decides
  host biology is an *orthogonal conditioning layer* that modulates the **gain** on the vectors (chiefly
  V4) and on the SOC chemo backbone, rather than a parallel attack on the cell; (2) answers the
  variability question (host factors are a legitimate, partly *measurable* source of heterogeneity —
  NLR/mGPS, L3 skeletal-muscle index, albumin are routine-data Tier-A markers); (3) catalogs ten host
  factors, each with mechanism, evidence tier, transfer caveat, what it modifies, and direction; and (4)
  resolves the weighting question by **reusing the three existing scoring axes** (ADR-0004) rather than
  inventing a new score — the **confidence/transfer axis (axis 2)** is what down-weights host evidence
  (almost all of it transfers from melanoma/NSCLC or general oncology, not CIC-DUX4), while the
  **feasibility axis (axis 3)** is kept deliberately distinct so "easy to access" (exercise, sleep) is not
  mistaken for "likely to work."

Headline framing: host modifiers enter the **confirmatory lane at attenuated confidence** (catalogued as
conditioning/tolerability/immune-context modifiers, never competing with tumour-targeted hypotheses for
the top of `protocol-v1.md`), but the **two-lane rule (golden rule §5)** keeps high-feasibility/
low-confidence host ideas alive as Forward Hypotheses. Only three factors reach Clinical-grade,
sarcoma-usable evidence today (systemic inflammation, sarcopenia/body composition, nutritional status) —
and these are notable for being measurable from routine bloods + the staging CT.

## Consequences

- **CLAUDE.md updated:** §0 reuse-inventory now lists `host-biology-modifier-layer.md`; §2 effort-table
  gains a row routing host-level / lifestyle / "does host biology explain variability / tolerance / immune
  competence" questions to this layer (reuse-and-extend, not re-derive).
- **`docs/adr/README.md`** index gains this row.
- **No existing analytical output was rewritten.** The layer *reuses and points to* `microbiome-immune.md`
  and the V2 anti-inflammatory work rather than duplicating them; `protocol-v1.md` is unchanged (a future
  `protocol-v2` could fold host modifiers in as V4/SOC annotations).
- **Three host-specific guardrails are recorded** as standing cautions: direction is not assumed beneficial
  (systemic butyrate→Treg; probiotics reduced anti-PD-1 response); prognostic ≠ targetable (NLR/mGPS/SMI
  predict outcome but moving the marker may not move the outcome); and "natural ≠ safe / correct-deficiency
  ≠ supraphysiologic-boost" (ATBC/SELECT precedent), reinforcing the contract's existing hard-refusal rule.
- **SOC-interaction obligation preserved:** the one pharmacologic axis (perioperative propranolol + COX-2/
  NSAID) is flagged for ifosfamide-nephrotoxicity / perioperative screening and explicitly marked
  forward-lane / clinician-run, never self-administered.
- **Atypical-case note is *relieved*, not triggered:** every host modifier is fusion-agnostic, so the layer
  applies unchanged to the ~5% fusion-unconfirmed subgroup — one of the few layers where the atypical
  caveat is fully relieved.
- **Trade-offs / what this does NOT do:** it does not claim any host factor changes CIC-sarcoma outcomes
  (none is CIC-DUX4-validated); it does not turn prognostic markers into treatment targets; it adds no new
  vector and re-scores no existing entry. Two cited items (ACSM 2019 roundtable PMC6814265; Haldar 2020
  Cancer DOI) carry a `[VERIFY]`-the-exact-PMID flag.

## Alternatives considered

- **A fifth attack vector ("V5 Host").** Rejected by the fixed-four-vectors constraint (golden rule §8) and
  because host factors are mechanistically *orthogonal* — they condition the vectors rather than attacking
  the cell. Same reasoning as ADR-0001.
- **A new, separate host-evidence scoring scheme.** Rejected: ADR-0004 already provides three orthogonal
  axes; the confidence/transfer axis already does the host-specific down-weighting. A bespoke scheme would
  duplicate machinery and risk drift.
- **Fold host factors into V4 directly** (since most modify the immune vector). Rejected: several act on
  SOC tolerability and the surgical window, not immunity, so a cross-cutting layer that *annotates* V4 and
  SOC is the correct scope, not a V4 sub-section.
- **Spawn a new supplementary research team.** Considered per CLAUDE.md §2/§3, but the question was a
  framework-design + evidence-cataloguing task answerable by reusing existing artifacts and live-verifying
  a bounded citation set; a full team run was not warranted. A deeper team run remains available if the
  layer is later expanded (e.g. a dedicated chronotherapy or exercise-oncology deep-dive).
