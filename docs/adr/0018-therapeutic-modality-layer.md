# ADR-0018: Therapeutic-modality layer (delivery-format axis, cross-cutting — not a fifth vector)

- **Status:** Accepted
- **Date:** 2026-06-14
- **Origin:** issue #33 ("Therapeutic Modality Expansion Beyond Systemic Pharmacology") + its two follow-up
  comments (drug-repurposing scan; ethnopharmacology / phytotherapy hypothesis-space) / PR
- **Deciders:** maintainer (via the github-issue-runner workflow)

## Context

Issue #33 observed that the simulation evaluates hypotheses **mostly as systemic pharmacology** — a drug or
a dietary compound entering the bloodstream — and asked whether reasonable opportunities are missed by that
framing. It named cellular therapies (TIL / CAR-T / CAR-NK / TCR), viral / oncolytic-virus therapy, vaccine
approaches, local & regional therapies (intratumoral delivery, regional perfusion, hyperthermia), physical /
energy-based interventions (hyperthermia, focused ultrasound, radiation-immune priming), and
combination-modality strategies. Two follow-up comments extended the idea to **sourcing**: a structured
**drug-repurposing** scan, and **ethnopharmacology / phytotherapy** as a searchable hypothesis space.

The diagnosis was partly correct. The framework's organizing axis is the four **vectors** (the molecular
*goal*), which say nothing about **delivery format**. In practice the catalog populated mostly two formats —
systemic small molecules and dietary compounds. Several named modalities already lived *inside* V4
(checkpoint mAbs, NK, neoantigen/mRNA vaccines, and the ICD/DAMP biology that oncolytic viruses and
hyperthermia exploit — ADR-0006) but were never made explicit. The genuine blind spots were the
**local/regional (M6)** and **physical/energy-based (M7)** formats — most notably **regional hyperthermia**,
which has a *positive phase-3 RCT in high-risk soft-tissue sarcoma* (EORTC 62961-ESHO 95; Issels et al.,
*Lancet Oncol* 2010) yet had **zero** catalog representation.

## Decision

Adopt a **cross-cutting therapeutic-modality layer** (a delivery-format axis, **not a fifth vector** —
golden rule #8) documented in `simulation-output/therapeutic-modality-layer.md`:

1. **Name a modality axis (M1–M8)** orthogonal to the four vectors: M1 systemic small-molecule, M2 systemic
   biologics/antibodies, M3 cellular (TIL/CAR-T/CAR-NK/TCR), M4 gene/viral/oncolytic, M5 vaccines, M6
   local/regional delivery, M7 physical/energy-based, M8 dietary/natural-product/host-directed. Every
   intervention is a cell in the vector × modality grid.
2. **Load-bearing rule:** modality changes the **feasibility** axis (often downward for ultra-rare-disease
   cell/viral therapy), **never** the evidence tier or the mechanism. Delivery format earns no tier credit.
3. **Coverage map** of the existing catalog against the grid, surfacing M3/M4/M6/M7 as gaps — with
   **regional hyperthermia (M7)** as the highest-value correction (real STS RCT, V2↔V4 dual mechanism).
4. **Two hypothesis-sourcing sub-scans, kept distinct from the modality axis:** (A) **drug-repurposing** —
   reuses the feasibility/attrition machinery (ADR-0003/0013, incl. "abandoned ≠ biologically invalidated")
   and applies the standard gauntlet (tier + Directness + concentration-mismatch + chemo-interaction); the
   issue's own examples (arsenic trioxide, thalidomide, colchicine, ivermectin) are scored honestly, with
   ivermectin as the concentration-mismatch cautionary case. (B) **ethnopharmacology/phytotherapy** —
   admitted as a *source of mechanisms* scored like any other (the space V1 was already partly drawn from),
   filtered chiefly by concentration-mismatch and chemo-interaction; "searchable, not privileged."
5. **Atypical-case interaction:** junction-specific TCR/CAR/vaccine modalities are **fusion-contingent**;
   hyperthermia, local control, checkpoint/NK, and host-directed modalities are **fusion-agnostic**.

## Consequences

- **New artifact:** `simulation-output/therapeutic-modality-layer.md` (Tier 2 analytical layer; evidence
  tier of the layer itself `Theoretical/Mechanistic` — it does not outrank real-data vector findings).
- **CLAUDE.md updated:** §0 reuse list gains the layer; §2 routing table gains a row directing
  modality / cellular / viral / vaccine / local-regional / hyperthermia / "beyond systemic drugs" /
  repurposing / ethnopharmacology questions here; §7 repository-map `simulation-output/` line updated.
- **Agent wiring (ADR-0016; see PR Phase-5-step-6 decision):** added as a row in the
  `sarcoma-orchestrator-intake` step-1B layer table (so a fresh full cycle ingests it and runs a
  **modality-coverage audit** of the catalog), and referenced by the V1/V3/V4 leads' Layer Intake. Without
  this wiring a fresh run would regenerate the systemic-pharmacology-biased catalog unchanged (the ADR-0016
  failure mode).
- **Not a new vector, axis-of-scoring, or biological layer.** It conditions/annotates (feasibility +
  coverage) and **never** overrides real-data vector evidence or prunes the forward lane (golden rule #5).
- **Explicitly does NOT** assert that any cellular / viral / local-regional / physical modality works in
  CIC-rearranged sarcoma — the disease is too rare for dedicated modality trials; nearly all cross-modality
  transfer is `Theoretical`/`Mechanistic` at a P2-sarcoma rung or worse (ADR-0014). It does not model
  combination-modality synergy quantitatively. Feasibility/regulatory facts are perishable. Not medical
  advice.

## Alternatives considered

- **Do nothing — modalities are implicit in the vectors.** Rejected: the issue correctly showed the catalog
  had real blind spots (M6/M7 absent despite a positive sarcoma RCT). Implicit ≠ audited.
- **Add a fifth "modality" vector.** Rejected outright — violates golden rule #8; modality is a delivery
  form factor cross-cutting all four vectors, not a target class.
- **Fold everything into V4.** Rejected: M6/M7 (local control, hyperthermia, radiation) and M8
  (host-directed) are not purely immune; hyperthermia is a V2↔V4 bridge. A standalone cross-cutting axis is
  the honest home.
- **Treat repurposing/ethnopharmacology as new modalities.** Rejected: they are *sourcing strategies* that
  feed candidates into existing modality classes (mostly M1/M2 and M8); making them modalities would
  double-count and inflate the taxonomy.
- **Build a quantitative modality/combination-synergy simulation.** Deferred to forward work — the
  per-modality and synergy parameters would be assumptions, and the sims obey a real-data-only rule.
