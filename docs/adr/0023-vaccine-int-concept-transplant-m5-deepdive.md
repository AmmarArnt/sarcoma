# ADR-0023: Vaccine / individualized-neoantigen-therapy M5 deep-dive (concept-transplant test) + Sim 11

- **Status:** Accepted
- **Date:** 2026-08-19
- **Origin:** Maintainer question — *"Is Merck's and Moderna's Intismeran drug concept applicable to sarcoma? Take the concept (high-level), not the exact drug itself, and try to simulate and find a vaccine that could work on sarcoma"*
- **Deciders:** Maintainer (AmmarArnt) + this session

## Context

The therapeutic-modality layer (ADR-0018) scored the **M5 (vaccine) cell as "Moderate — covered"**, on the
strength of the existing neoantigen-vaccine specialist output and the mRNA team. That coverage was a
*platform survey*: it recorded what intismeran autogene, autogene cevumeran and NEO-PV-01 are, what their
trial status was, and the fusion-unconfirmed caveat that makes junction-specific payloads inapplicable
here. It did **not** test whether the *concept* behind those platforms transplants into this tumour class,
and it produced no quantitative answer to "what vaccine would work instead."

The maintainer's question is explicitly a **concept-transplant** question, not a drug question — the same
shape as ADR-0019's treatment of oncolytic virotherapy (take the M4 cell, work it through the V4 biology,
score it honestly). It also arrives under **Era B** (ADR-0022): the driver is unresolved, the leading
hypothesis (D4, 0.386) is the *lowest*-TMB branch, and ADR-0021 has established that the immunological
opportunity is a **perishable post-chemo MRD window**. None of that was in scope when the M5 cell was
first surveyed.

The gap was therefore: **no artifact decomposed the INT concept into transferable vs. non-transferable
parts, and nothing in the repo quantified the antigen-supply constraint that decides the question.**

## Decision

1. **Add a new simulation type — `sims/11-vaccine-antigen-portfolio/` (Sim 11):** a Monte-Carlo
   **antigen-supply and vaccine-architecture decision model**. It marginalises antigen availability over
   the Era-B driver posterior (carried verbatim from `CASE-BASELINE.md` §3), runs a
   `TMB → clonal → expressed → HLA-binder → immunogenic` supply funnel against a **melanoma calibration
   arm** as a built-in consistency check, scores seven antigen-source classes, ranks six candidate vaccine
   architectures **against an explicit no-vaccine baseline**, computes proper EVSI (≥0 by construction)
   for five candidate tests *for the design decision only*, and closes with an ADR-0017 flip test stating
   what would have to be true for a vaccine to be load-bearing.

   Two methodological requirements are established by this sim and should carry to future ones of its
   type: **(a) a calibration arm** — a decision model that claims a therapy class fails in tumour X must
   reproduce its success in the tumour where it was validated, without being fitted to do so; and
   **(b) a null/no-intervention baseline** — an architecture bake-off without one cannot distinguish "this
   design is best" from "no design in this set beats doing the surrounding things alone." Sim 11's first
   draft lacked (b) and inverted its own conclusion once it was added.

2. **Add a standing deliverable — `simulation-output/vaccine-int-concept-transplant-layer.md`:** the M5
   deep-dive. It decomposes the concept into four pillars (P1 antigen source · P2 mRNA-LNP delivery and
   adjuvanticity · P3 polyepitope breadth · P4 MRD-window + PD-1 deployment), establishes that **only P1
   is tumour-specific and it is the one that breaks**, splits the general sarcoma answer along the
   **complex-karyotype vs. translocation-driven** axis, gives the case-level answer separately and more
   harshly, catalogues seven swappable antigen sources on the three axes, specifies the architecture the
   model endorses, and carries the counterweight (§6), three forward hypotheses with falsifiers, a
   "could not establish" section and a red-team pass.

3. **Adopt the "antigen-source inversion" as standing framework language:** *melanoma needs
   personalization because its antigens are private; translocation-driven sarcoma's best antigens are
   public, so the correct architecture is off-the-shelf.* Keep P2/P3/P4, replace P1. This is the reusable
   generalization and it applies to any future vaccine question in this repository.

**This is explicitly NOT a fifth vector and NOT a new scoring axis.** It is the M5 cell of ADR-0018
deepened through V4 (ADR-0006) and the MRD-window finding (ADR-0021), exactly parallel to ADR-0019's
treatment of M4. Modality moves the **feasibility** axis only; tier and confidence remain set by biology
and Directness (ADR-0014).

## Consequences

- **CLAUDE.md updated:** new bullet in the §0 reuse list; new routing row in §2 (vaccine / neoantigen /
  personalized-cancer-vaccine / "is drug X's concept applicable" questions); `sims/01–11` and the new
  layer added to the §7 repo map.
- **`sims/00-INDEX.md`** gains the Sim 11 row; **`simulation-output/findings-ranking.md`** gains rows in
  groups B and C per the ADR-0009 maintenance rule, placed **below** the real-data findings (Sim 11 is a
  decision model — promise ≠ proof).
- **Wiring (ADR-0016):** no new ingestion behaviour. This slots under the existing "all vector leads ←
  therapeutic-modality layer" path; the modality layer's M5 row now points here, so a fresh full cycle
  inherits it through ADR-0018. V4 additionally inherits it as an M5/antigen-supply input.
- **Forward lane only.** Literature and data egress (PubMed, ClinicalTrials.gov, DepMap, NCBI FTP,
  HuggingFace) all returned HTTP 403 on 2026-08-19, so **every citation carries `[VERIFY]`** and
  **ADR-0020's gate applies**: nothing here may enter a `protocol-vN.md` until full-text verified.
  OpenMed NER grounding could not be executed and `grounding.tsv` is **absent rather than fabricated**.
- **A named, runnable real-data upgrade is left on the table:** DepMap/GEO expression of the cancer-testis
  and lineage-antigen classes in Ewing/CIC lines, and GSE60740's antigen-presentation response to driver
  induction. Both would convert the model's weakest parameters from judgement into measurement, and both
  are blocked only by egress.
- **Honest trade-off:** the sim's headline for *this case* is a negative one — no vaccine architecture in
  the set clears the no-vaccine baseline by a meaningful margin. That is recorded rather than softened,
  and the §5 design is framed as the least-wrong construction under an explicit falsifier, not as a
  recommendation.

## Alternatives considered

- **Answer from the existing neoantigen-vaccine specialist output and stop.** Rejected: that output
  answers "what are these platforms and do they enrol CIC cohorts," which is a different question from
  "does the concept transplant." It also predates Era B, so its weighting of the fusion-contingent
  options is superseded by `CASE-BASELINE.md` §5a.
- **Spawn a fresh vaccine-design team (lead + specialists).** Rejected under CLAUDE.md §0 cost discipline
  and the session's constraints: the work is a single coherent modelling task with a well-defined output,
  and CLAUDE.md §3's practical caveat explicitly permits running it directly in the main thread. Nothing
  in the analysis needed parallel independent perspectives that the existing artifacts did not already
  supply.
- **Make "vaccines" a fifth vector.** Rejected on golden rule #8, and on the merits: Sim 11's own result
  is that the vaccine is an adjunct to V4's effector and timing findings, not an independent axis of attack.
- **Promote the layer into a `protocol-v5.md`.** Rejected: ADR-0020's `[VERIFY]` gate forbids it while
  egress is down. The layer is forward-lane until its anchors are full-text verified.
