# Biomarker VoI — Acquisition-Provenance & Temporal-State Extension

**In response to GitHub issue #7 follow-up** (@Cerimagic, 2026-06-12) — extends the
[Biomarker Value-of-Information & Missing-Data Stratification Layer](biomarker-voi-stratification.md)
(Sim 6 / [ADR-0001](../docs/adr/0001-missing-data-taxonomy-and-voi-layer.md)) and links it to the
[driver-uncertainty decision model](tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md)
(Sim 8 / [ADR-0008](../docs/adr/0008-driver-uncertainty-decision-model.md)).

**One-line summary:** the value of a missing biomarker depends not only on *which* marker it is but on
**where the answer physically comes from** (archived tissue vs fresh biopsy vs blood) and **which
disease timepoint it speaks to** (baseline / current / change-under-treatment); this file adds those two
axes to Tier B of the missing-data taxonomy and re-maps the current case onto them. **Deliberately
excludes:** any recommendation to obtain a test, any new biology, any patient-specific prediction.

**Status:** framework-enhancement (methodology refinement of an existing layer). Research-simulation
output, **not medical advice**, **not a recommendation to obtain any specific test**, **not a
diagnosis**.

**Confidence: medium.** The provenance/temporal axes and their qualitative interaction with the Sim-6
VoI ranking are well-grounded in standard molecular-pathology constraints (verified below); the
*magnitudes* of any "realizable VoI" attenuation are illustrative, not computed — see §6.

---

## 1. The follow-up question, restated

The original layer (ADR-0001) split missing data into **A — Known**, **B — Missing but obtainable
(ranked by VoI)**, and **C — Missing, low-impact**. The follow-up observes that **Tier B is not
homogeneous**: within "missing but obtainable,"

1. some answers are recoverable from **archived material** (the diagnostic FFPE block, stored slides,
   leftover extraction material / prior molecular reports) — low marginal cost and **no new procedural
   risk**; whereas
2. others require a **fresh sample from the current disease timepoint** (a new biopsy of the relapse
   lesion) — higher cost and risk; and
3. for this case several of the highest-value questions are about **temporal evolution**, not the
   current state alone:
   - confirmation vs non-confirmation of the original CIC-rearranged diagnosis,
   - whether the relapse lesion is the **same molecular clone** or a **selected survivor subclone**,
   - whether immune markers (MHC-I/B2M, HLA-E, nectin axis, TILs) **remained stable or changed under
     treatment pressure**.

The proposal: **VoI depends not only on the biomarker but on its source and the timepoint it
characterizes.** This file adopts that as a standing refinement.

---

## 2. Two new axes inside Tier B

### Axis P — Acquisition provenance (where the answer comes from)

| Class | Source | Marginal cost / risk | Assay ceiling (what it can actually yield) | Timepoint it characterizes |
|---|---|---|---|---|
| **P1 — Archived / historical** | Diagnostic FFPE block, stored H&E/IHC slides, residual extraction material, prior molecular-test reports | **Low / none** (no new procedure) | **Good:** IHC, genome-wide DNA-methylation array, short-read targeted DNA & (DV200-permitting) RNA panels. **Poor:** long-read WGS (FFPE DNA is fragmented/low-MW), high-quality whole-transcriptome RNA-seq, any live-cell / functional assay | **Baseline (diagnostic-era)** |
| **P2 — Fresh, current timepoint** | New biopsy of the relapse lesion | **High** (procedure, sampling risk, may be infeasible by site) | **Best:** high-MW DNA → long-read WGS + RNA-seq (cryptic-junction recovery), high-quality RNA-seq, **viable cells** for flow / functional NK & TIL assays, fresh IHC | **Current (relapse-era)**; paired with P1 → **change** |
| **P3 — Liquid biopsy** | Plasma ctDNA / cfDNA, circulating tumor cells | **Lowest** (blood draw), repeatable | Fusion-**breakpoint tracking / MRD** once a junction is known; copy-number; *not* spatial architecture (no TIL pattern, no MHC-I IHC) | **Current**, serial |

### Axis T — Temporal state (which disease timepoint the answer informs)

| Class | Meaning | Source requirement |
|---|---|---|
| **T0 — Baseline** | The tumor's state *at diagnosis* | P1 alone (archived) |
| **T1 — Current** | The tumor's state *now* (relapse) | P2 (fresh) or, for some markers, P3 |
| **TΔ — Delta** | *Change* between diagnosis and relapse (clonal evolution, immune editing under therapy) | **Paired** P1 **and** P2 — neither alone suffices |

**The central refinement:** the three highest-value questions in the follow-up are **TΔ** questions, and
TΔ is the most demanding class because it needs *both* a baseline (usually already archived) and a fresh
current sample, **plus** assay comparability across the two (same/equivalent antibody, threshold, and
scoring — otherwise batch effects masquerade as biology).

---

## 3. Verified provenance constraints (the load-bearing facts)

- **FFPE limits long-read sequencing.** Formalin fixation crosslinks and fragments DNA, leaving
  low-molecular-weight material; long-read platforms (Oxford Nanopore, PacBio) preferentially require
  concentrated high-MW DNA typically obtainable only from **fresh-frozen** tissue. FFPE long-read is
  possible but workaround-dependent and lower-yield. **Established** (Oxford Nanopore extraction
  guidance; *NAR Cancer* 2025, FFPE nanopore methylation, PMC equivalents; CNS-tumor FFPE-nanopore
  feasibility, PMC12590785, accessed 2026-06-13). *Consequence:* the **cryptic-junction recovery** that
  Sim 8 values most (long-read WGS+RNA-seq) is the one diagnostic that genuinely benefits from **fresh**
  tissue; DUX4 IHC and methylation arrays do **not** — they run well on the **archived** block.
- **Methylation arrays and IHC are archived-friendly.** Genome-wide methylation classification and
  protein IHC are routinely performed on diagnostic FFPE; this is the basis of the Sim-8 reclassification
  logic. **Established.**
- **ctDNA fusion-breakpoint tracking is feasible in Ewing-family sarcoma** by digital-droplet PCR of the
  patient-specific junction, enabling non-invasive MRD/monitoring (*Front Pediatr* 2022, PMC9420963;
  ASCO Educational Book EDBK_280749; review PMC12936904, accessed 2026-06-13). **Clinical-Trial /
  emerging.** *Caveat:* this literature is **EWSR1-fusion-centric**; **CIC-DUX4-specific ctDNA detection
  is extrapolated, not directly demonstrated `[VERIFY]`**, and it requires a **resolved junction first**
  — so for the fusion-unconfirmed case ctDNA is a *downstream monitoring* tool, not a front-line
  resolver.

---

## 4. The current case, re-mapped onto provenance × timepoint

Reusing the Sim-6 VoI ranking (decision-flip frequency; magnitudes are model-relative — see the parent
layer). The new columns say *where* each answer lives and *which timepoint* drives the relapse-treatment
decision.

| Marker (Sim-6 rank, VoI) | Decision-relevant timepoint | Archived (P1) read? | Needs fresh (P2)? | Provenance note |
|---|---|---|---|---|
| **Nectin CD155/CD112** (1, 0.625) | **T1 current** (gates current clearance program) | Baseline IHC: yes | For current state: **yes** | Baseline read is cheap but may be stale if edited under therapy; current read is what gates the V4 decision **now** |
| **HLA-E** (2, 0.500) | **T1 current** | Baseline IHC: yes | For current state: **yes** | Same — IFN/therapy can shift HLA-E; current value dominates |
| **Treg/FoxP3, TIGIT** (3, 0.312) | T1 current (regimen composition) | Baseline IHC: yes | For current state: **yes** | TME composition is highly therapy-modifiable → TΔ-sensitive |
| **NK functional reserve** (5, 0.250) | **T1 current**, host-side | **No** (functional, not archivable) | **Fresh / blood (P2/P3)** | Cannot be recovered from archived tissue at all — live cells required; post-WLI/chemo state is the point |
| **MHC-I / B2M / TAP1** (6, 0.188) | **TΔ** (antigen-loss may be *acquired* under immune/chemo pressure) | Baseline IHC: yes | **Paired** for the editing question | The classic immune-editing target: baseline-normal ≠ currently-normal |
| **CD8+ TIL density** (6, 0.188) | T1 current / TΔ | Baseline IHC: yes | For current/change: **yes** | Spatial — IHC only (not ctDNA); benefits from paired read |

**Diagnosis confirmation (the fusion-unconfirmed question) — mapped to Sim 8's tests:**

| Test (Sim 8) | Resolves | Best provenance | Timepoint |
|---|---|---|---|
| **Nuclear DUX4 IHC** | DUX4-transactivation-domain question (licenses the contingent MCL1/DUX4-fragility line) | **P1 archived** — cheap, runs on the diagnostic block | T0 (a fixed diagnostic fact) |
| **DNA-methylation array** | Collapses D4 phenocopy / triages D5 | **P1 archived** | T0 |
| **Long-read WGS + RNA-seq** | Cryptic CIC-DUX4 junction & rare partners; unlocks junction-specific options | **P2 fresh preferred** (high-MW DNA) | T0 if archived block is the only tumor; ideally T1 fresh |

**Reading of the grid:** the two *cheapest, archived-compatible* tests (DUX4 IHC, methylation) carry
most of the diagnosis-resolving leverage Sim 8 identified — so a large share of that VoI is realizable
at **near-zero marginal procedural risk** *if a diagnostic block exists and is not exhausted*. Only the
**long-read junction recovery** materially benefits from a fresh sample.

---

## 5. The non-obvious refinements (why this is more than a relabel)

1. **For immune markers, the *current* read dominates the *baseline* read — even though baseline is
   cheaper.** The Sim-6 VoI treated each marker as single-state. But MHC-I/B2M, HLA-E, nectin and TILs
   are exactly the markers most subject to **immune editing under therapy** (VDC/IE + leg RT +
   whole-lung irradiation). A baseline-only archived read can therefore be *misleadingly reassuring* for
   a relapse-era decision. So provenance **re-weights** the ranking: the high-VoI immune markers want a
   **current (P2/T1)** read, not just the cheap archived one — which raises, not lowers, the case for the
   one expensive source (fresh biopsy) *if* the V4 NK-first program is on the table.

2. **NK functional reserve is unrecoverable from any archived material.** It is a live-cell / blood
   property (P2/P3 only). The original layer ranked it #5 by VoI without noting that its answer simply
   **cannot** come from the diagnostic block — a provenance fact that changes *how*, not just *whether*,
   to value it.

3. **The cheapest leverage is front-loaded in the archived block.** Diagnosis confirmation (DUX4 IHC +
   methylation) and the *baseline* immune profile (nectin/HLA-E/MHC-I/TIL IHC) are all archived-
   compatible. If the diagnostic FFPE is retrievable, a substantial fraction of the catalog's decision
   uncertainty has a **low-cost, no-new-risk** answer — and the **incremental** ask of a fresh biopsy is
   then only the *delta / current-state / long-read-junction* increment, not the whole panel.

4. **"What to measure" becomes "what to measure, from where, for which timepoint, at what marginal
   cost."** That is the actionable upgrade the follow-up asked for: it lets a future contributor
   separate *information value* from *acquisition burden*, instead of conflating them.

---

## 6. Honest limitations (what this does and does NOT claim)

- **Realizable-VoI magnitudes are illustrative, not computed.** A principled version would multiply each
  Sim-6 VoI by a recoverability/feasibility factor (`realizable-VoI ≈ modeled-VoI × P(answer recoverable
  from an accessible source)`), but those factors would be **assumptions**, not real data. Per the sims'
  real-data-only rule, **no new numeric model was fabricated**; a quantitative provenance-conditioned
  extension of Sim 6 is flagged as future work (§7), not executed here.
- **Inherits all Sim-6 / Sim-4 limitations** — qualitative Boolean kill-rule logic, transferred
  (non-CIC-DUX4-validated) mechanism edges, single-cell-line baseline (GSE60740). Provenance does not fix
  any of those.
- **Assay availability is itself uncertain.** Clinical-grade, standardized IHC for **nectin
  (CD155/CD112)** and **HLA-E** is **not** as established as MHC-I/B2M or CD8 IHC — antibody clones and
  positivity thresholds vary `[VERIFY clinical-grade availability]`. A marker being archived-compatible
  *in principle* does not guarantee a validated assay exists.
- **TΔ comparability is hard.** A baseline-vs-relapse comparison is only valid if the two timepoints are
  assayed with equivalent methods; antibody lot, platform, and scoring drift can fake a "change."
- **Not a testing recommendation, not a diagnosis.** This documents *uncertainty structure* for future
  contributors. Whether this patient's diagnostic block exists, is exhausted, or is even from the same
  lesion as the relapse is **unknown to the simulation**; any real acquisition decision belongs to the
  treating oncologist and pathologist.
- **Atypical-case flag (unchanged).** The diagnosis-confirmation row *is* the resolution of the
  fusion-unconfirmed status. Fusion-agnostic markers (immune IHC, methylation class) apply regardless;
  the junction-specific downstream (ASO/vaccine/ctDNA monitoring) remains contingent on a confirmed,
  resolved fusion.

**What I could not establish:**
- Whether the patient's archived diagnostic material exists, is sufficient, or matches the relapse site.
- CIC-DUX4-specific ctDNA performance (extrapolated from EWSR1-fusion ddPCR; `[VERIFY]`).
- Quantitative recoverability probabilities per assay (left deliberately uncomputed — §6 bullet 1).

---

## 7. Forward hypotheses (mechanistically defensible, not yet tested here)

- **[Forward Hypothesis] Therapy-induced immune editing makes the *current* immune read decision-
  dominant over the baseline read for the V4 program.** *Basis:* MHC-I/B2M downregulation and HLA-E
  upregulation are documented immune-escape responses to cytotoxic/immune pressure; this case had heavy
  chemo + whole-lung irradiation. *Test:* paired baseline(archived-FFPE)/relapse(fresh) IHC + methylation
  for MHC-I/B2M, HLA-E, nectin, CD8/FoxP3 with matched assays. *Falsifier:* markers stable across
  timepoints → the cheap archived baseline is sufficient and the fresh-biopsy increment adds little VoI.

- **[Forward Hypothesis] For this case, realizable VoI is front-loaded into archived material.** *Basis:*
  the highest-leverage diagnostic tests (DUX4 IHC, methylation) and the entire *baseline* immune panel are
  FFPE-compatible; only long-read junction recovery and live NK/TΔ questions require fresh/blood. *Test:*
  extend Sim 6 with an explicit provenance-conditioned cost/risk penalty and re-rank by VoI-per-unit-
  acquisition-burden. *Falsifier:* a fresh-only quantity (current functional NK reserve, or a selected
  relapse **subclone** with a distinct vulnerability) flips the recommended program regardless of any
  archived read — in which case fresh sampling, not the block, carries the decisive VoI.

---

## 8. Proposed standing rule (for the framework)

> **Tier B is classified on two further axes:** provenance **P1 archived / P2 fresh / P3 liquid** and
> temporal state **T0 baseline / T1 current / TΔ change**. When surfacing a high-VoI unknown, record the
> cheapest source that can answer it **and** the timepoint the decision actually needs. A TΔ question
> requires paired P1+P2 with comparable assays. Realizable VoI is bounded by recoverability from an
> accessible source — never assume a marker is "obtainable" without naming the source.

---

*Provenance:* extends `simulation-output/biomarker-voi-stratification.md` (Sim 6) and
`simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md` (Sim 8). External
facts verified live 2026-06-13 (Oxford Nanopore FFPE/long-read guidance; *NAR Cancer* 2025 + PMC12590785
FFPE-nanopore feasibility; PMC9420963 / EDBK_280749 / PMC12936904 ctDNA in Ewing-family sarcoma). No new
biology, no fabricated citations, no new numeric model.

*Decision record:* adopted via [ADR-0011](../docs/adr/0011-voi-provenance-temporal-axis.md) (issue #7
follow-up). **Evidence tier of this layer:** `Theoretical / Mechanistic` (a methodology refinement of a
decision-sensitivity analysis). Not medical advice.
