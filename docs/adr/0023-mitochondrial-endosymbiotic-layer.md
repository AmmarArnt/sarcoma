# ADR-0023: Mitochondrial / endosymbiotic layer — the cell's bacterial legacy as alarm, commons, and reservoir

- **Status:** Accepted
- **Date:** 2026-09-17
- **Origin:** Maintainer question (2026-09-17) — proposed approaching the sarcoma "from a mitochondria
  angle," treating it as "rogue bacteria," via the endosymbiotic theory that cells/organisms are
  cooperatives of former bacteria and the tumour is the outlier "hoarding resources for itself"; asked how
  the disease could be tackled **long-term after NED**, explicitly noting that NED ≠ absence of tumour cells
  (dormant, or sub-CT-resolution).
- **Deciders:** maintainer + Claude Code session
- **Artifacts:** `simulation-output/mitochondrial-endosymbiotic-layer.md`
- **Relates to:** ADR-0021 (chemo-response / DDR cell-state layer — extends its persister-reservoir spine),
  ADR-0022 (Era B — supplies the Directness re-weighting that makes the Ewing-family metabolic evidence
  usable), ADR-0006 (V4 danger-signalling expansion — §4A is a second, endogenous danger-signal generator),
  ADR-0019 (OV M4 deep-dive — same objective, different generator), ADR-0005 (host-biology layer — nutrient
  competition/acidosis as an immunosuppressive route), ADR-0003/0013 (feasibility + attrition reasons — two
  new entries), ADR-0014 (transferability ladder), ADR-0018 (modality axis — M1/M8, one M3 corollary),
  ADR-0020 (`[VERIFY]` gate — this layer is forward-lane), ADR-0009 (findings register), ADR-0017
  (red-team self-challenge, run in §7).

## Context

The framework had **no mitochondrial or organelle-level layer.** Mitochondria appeared only as scattered
mentions (an apoptotic-priming read in ADR-0021, antioxidant/ROS discussion in V2, a GPX4/ferroptosis
persister row) and were never treated as a coherent surface. Meanwhile `CASE-BASELINE.md` §4 had already
established that the unsolved clinical problem is the **drug-tolerant persister / dormant reservoir** rather
than the chemo-sensitive bulk — i.e. exactly the compartment a post-NED question is about — and ADR-0021
left that compartment with **one** `Low`-confidence hypothesis (GPX4/ferroptosis) and a **demoted headline
BH3 target (MCL1) with no replacement.**

The maintainer's framing is also a *conceptual* proposal, not only a target request, so it needed an honest
translation rather than either uncritical adoption or dismissal. Two things had to be established:

1. Which parts of "the body is a mitochondrial cooperative and the tumour is a resource-hoarding outlier"
   are real biology (endosymbiotic ancestry; bacterial-pattern DAMPs; cancer-as-cellular-cheating; nutrient
   competition) versus which parts mis-describe the mechanism (the tumour's genome is nuclear; mitochondria
   are conscripted infrastructure, not the rogue agent).
2. What the framing *predicts therapeutically* — because the naive reading ("attack the mitochondria") has
   **two hard clinical negatives on record** in precisely this setting, and the framework's golden rule #5
   obliges asking why they failed rather than either ignoring or capitulating to them.

## Decision

Adopt a standing cross-cutting **mitochondrial / endosymbiotic layer**. **Not a fifth vector** (golden
rule #8): it supplies mechanism to **V4**, re-weights **V1** toward a reservoir-directed rather than
bulk-directed throttle, and extends ADR-0021's persister spine. On the ADR-0018 modality axis it sits at
**M1** and **M8**, with one **M3** (cell-therapy manufacturing) corollary.

Four rules follow:

1. **Two-level translation is mandatory.** Distinguish the **endosymbiotic bargain inside a cell**
   (nucleus ↔ mitochondrion, largely intact in tumour cells) from the **multicellular social contract
   between cells** (where cancer actually defects). The tumour defects at level 2 and must *renegotiate*
   level 1 to sustain it — and that renegotiation, not the organelle itself, is what generates targets.
   Any output using this layer states which level it is talking about.
2. **The commons objection is a standing constraint, not a caveat.** Because mitochondria are shared
   cooperative infrastructure, a class-wide mitochondrial attack hits the most OXPHOS-dependent
   cooperators (neurons, heart, muscle) first. Any mitochondria-directed hypothesis must state its
   **therapeutic window** argument or be marked as lacking one. The framing predicts its own failure mode,
   and the failure is documented (IACS-010759).
3. **The alarm is preferred over the target.** Where a mitochondrial hypothesis can be posed either as
   *starving* the organelle (catalytic OXPHOS blockade) or as *making it report* (redox/structural
   perturbation → mtDNA/DAMP → cGAS-STING), prefer the latter: the immune payoff tracks it, and the
   toxicity profile is different. These are **not the same intervention** and must not be conflated.
4. **Direction must be named, with a falsifier.** Metabolic/dormancy interventions are not monotonic —
   autophagy inhibition, the intuitive dormancy-directed move, is reported to *awaken* dormant cells. A
   hypothesis in this layer that cannot name its sign **and** a falsifier is decoration.

**Two feasibility-register entries are added** under ADR-0013's attrition scheme:
- **IACS-010759** (complex-I inhibitor): **R2 on *toxicity / therapeutic index*** — mechanism-based
  neurotoxicity + lactic acidosis, no RP2D, both phase-1 trials discontinued. Explicitly **not R1**
  (target-invalidation): the biology is not refuted, the *systemic catalytic* delivery strategy is. **F4.**
- **Adjuvant metformin** (MA.32, n=3,649): **R2, biomarker-unenriched** — negative for iDFS/DRFS/OS in the
  adjuvant recurrence-prevention setting. **F1 access but with negative phase-3 adjuvant evidence**, which
  is a worse position than unproven. Primary mechanistic explanation: **concentration mismatch**
  (millimolar in vitro vs. low-micromolar achievable plasma) — golden rule #6.

## Consequences

**What changed in the framework's standing positions** (detail in the artifact §6):

- The reservoir's **GPX4/ferroptosis** row (ADR-0021) is **unified** with the OXPHOS-high/FAO persister
  phenotype as two readings of **one lipid-redox vulnerability**; FSP1 and HDACs join as co-suppressors.
  Confidence stays `Low` (P4, no sarcoma model) but the prior rises on convergence.
- The **demoted MCL1 node gains a proposed replacement**: **BCL-XL** as the BH3 dependency of the
  **quiescent, post-anthracycline/alkylator reservoir** — not MCL1, not BCL2, and not the bulk. This is the
  layer's most specified contribution, it matches this patient's actual exposure history
  (doxorubicin/cyclophosphamide/ifosfamide), it is fusion-agnostic, and the platelet-sparing PROTAC
  degrader route answers the class's known dose-limiting toxicity. Forward lane.
- **NK-first sequencing** (Sims 4+5) gains mechanistic support **and a measurable failure mode**:
  mTOR–Drp1-driven mitochondrial fragmentation in tumour-infiltrating NK cells, aggravated by the tumour's
  own lactate/acidosis, reversible in preclinical models. Adds an *ex vivo* NK-conditioning (M3) corollary.
- **A new immune-evasion axis enters the framework**: tumour→TIL **mitochondrial transfer** with
  homoplasmic replacement and T-cell senescence. It is invisible to every assay currently in the catalog
  (MHC-I, Nectins, HLA-E, NK fitness) and is detectable as tumour↔TIL **mtDNA-variant sharing** — a
  reanalysis question rather than a new assay.
- **Danger-signal generation** gains a **second, endogenous generator** (mitochondrial DAMP → cGAS-STING)
  alongside ADR-0019's oncolytic viruses: fusion-agnostic and not anatomy-limited, but with **no clinical
  agent implementing it** — so a concept alongside OV, not a better-accessed one.
- The **"SLFN11 negative" contingency** (`CASE-BASELINE.md` §8) gains a second branch: GPL-biosynthesis
  inhibition restoring DNA-damage sensitivity in SLFN11-deficient **Ewing (P1)** models.
- **Era B's Directness inversion is load-bearing here.** The layer's only **P1** item —
  **SHMT2 / mitochondrial one-carbon dependency in Ewing** — would have been discounted under Era A as
  "Ewing, not CIC." Under ADR-0022 it is the highest-Directness mitochondrial finding available. It is
  nonetheless **proliferation-directed**, i.e. aimed at the bulk, so it **does not answer the post-NED
  question**; it is recorded for its Directness, not its fit.

**Costs and risks accepted:**

- **The layer is entirely `Preclinical`/`Theoretical` and every citation is `[VERIFY]`.** Literature egress
  (PubMed, PMC, nature.com, EuropePMC, NCBI E-utilities) **and `clinicaltrials.gov`** all returned HTTP 403
  on 2026-09-17. Identifiers are as they appeared in **search results**, not records opened. Forward-lane
  only; **no promotion to any `protocol-vN.md`** until full-text-verified, and **every F-band is inherited
  or inferred, not verified**.
- **No sarcoma data exist for anything in §4.** The strongest items are cross-lineage transfers of
  *persister-state* properties (P3/P4) — defensible as state-properties, unvalidated here.
- **The load-bearing uncertainty is inherited and unresolved**: whether a persister reservoir is the right
  model at all, versus outgrowth of a pre-existing metastatic clone (this tumour was metastatic at
  diagnosis with 12 lung nodules). If the latter, §5 of the artifact — BCL-XL included — targets a
  compartment that does not exist in this patient. Named as the falsifier, not buried.
- **Part of the framing is narrative.** The red-team pass (§7) concedes that nutrient competition and
  OXPHOS-high persisters are standard tumour-metabolism findings needing no endosymbiotic story. The framing
  earns its keep in exactly two places: bacterial ancestry as the *reason* mitochondrial components are
  immunogenic, and organelle trafficking as literal parasitism. This is recorded rather than glossed.
- **No simulation was run.** Ranking here is judgment-only — unlike Sims 8/10 there is no posterior and no
  EVSI. **Sim 11 (reservoir metabolic-dependency + explicit therapeutic-window model) is proposed, not
  executed.** Entity grounding (`scripts/openmed_ner.py`) was also **not** run; the new entities are listed
  in the artifact §8.8 for grounding before any promotion (grounding was **attempted and is blocked** — `huggingface.co` unreachable, so the models cannot download).

**Guardrail:** this layer produces **no diagnosis, no testing recommendation, and no treatment or supplement
advice**. Its outputs are mechanisms, beliefs and falsifiers. It explicitly does **not** endorse metformin,
complex-I inhibitors, autophagy inhibitors, or any antioxidant/metabolic supplement — and §3 exists
specifically to document that the two most-reached-for interventions in this space have negative or
discontinued clinical data in the relevant setting.

## Alternatives considered

- **Reject the framing as a category error** (mitochondria are not the rogue agent, so there is nothing to
  do). Rejected: it is true but unhelpfully literal, and it would have discarded three real surfaces —
  including the one genuinely explanatory link (bacterial ancestry → immunogenicity) and a 2025 immune-evasion
  mechanism the framework was entirely missing.
- **Adopt it as a fifth vector ("V5 Metabolic/Endosymbiotic").** Rejected — golden rule #8. The four
  vectors are fixed, and the content distributes cleanly across V4 (alarm, immune metabolic fitness) and V1
  (reservoir-directed throttle) as a cross-cutting layer, exactly as ADR-0005/0018/0021 did.
- **Fold it into the existing host-biology layer (ADR-0005).** Rejected: host-biology is about the *host's*
  modifiers (microbiome, inflammation, nutrition, activity, sleep). §4A and §4C are **tumour-cell and
  organelle** mechanisms, not host modifiers. Only §4B genuinely overlaps, and it is cross-referenced rather
  than duplicated.
- **Fold it into ADR-0021's cell-state layer.** Rejected as scope creep: ADR-0021 owns "treatment response
  as evidence," a decision-theoretic device. This layer is a mechanism catalogue for a compartment ADR-0021
  identified. Keeping them separate preserves ADR-0021's narrow, defensible claim.
- **Run a full §3 multi-agent cycle.** Rejected per CLAUDE.md §0/§2 (cost discipline; no fitting existing
  team, and a new team requires the user's OK first). The work was done in the main thread against the
  existing artifacts, with a new artifact written rather than any baseline clobbered.
- **Write nothing until literature egress is restored.** Rejected: ADR-0020 exists precisely so that
  snippet-level biology can be captured and quarantined in the forward lane rather than lost, provided the
  gate is applied. The gate is applied.
