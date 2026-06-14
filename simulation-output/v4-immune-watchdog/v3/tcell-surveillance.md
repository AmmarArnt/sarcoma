# V4 Checkpoint/T-cell Specialist — T-cell Surveillance Report (Clean-Slate Run v3)

**Summary:** Covers PD-1/PD-L1/CTLA-4 checkpoint biology, clinical CPI trial evidence in sarcoma
(SARC028, Alliance A091401), the V3→V4 epigenetic-priming bridge (now reconciled against V3's
HDACi-rank-1/DNMTi-rank-2/EZH2i-downgraded findings), the Nectin–TIGIT–DNAM-1 axis (anti-TIGIT
phase-3 failures vs. the NTX1088 ligand-side alternative), the ICD/doxorubicin-as-adjuvant angle,
and honest dietary PD-L1-modulation framing. **Deliberately excludes:** NK-cell-intrinsic
mechanisms (own specialist file), microbiome/CPI-response literature (own specialist file), and
junction-specific neoantigen design (own specialist file) — referenced only at hand-off points.
The dominant immune-state framing for this patient is the **imminent high-dose-ifosfamide
lymphodepletion**, not the >2-year-old BNT162b2 vaccination.

**Confidence: medium** — checkpoint-inhibitor mechanisms and sarcoma-trial-level data are
well-characterized; the V3→V4 epigenetic-priming mechanism class (HDACi/DNMTi → MHC-I) is real and
Clinical-Trial tier in other contexts. What pulls confidence down: **zero direct CIC-DUX4 data**
for every claim in this file, the EZH2i route (previously the "cleanest" bridge) is now
double-caveated (mechanistic premise contested + tazemetostat globally withdrawn), and the
patient's imminent lymphodepletion means the single most actionable finding here is **sequencing/timing**, not a new agent.

---

## PATIENT CONTEXT INTEGRATION

This patient completed 14 cycles VDC/IE, surgery (>95% necrosis), radiation to the leg plus
whole-lung irradiation (WLI), achieved NED for one year, and now has oligometastatic relapse
(single lung cluster) immediately before starting **high-dose ifosfamide**. Specific framing for
this specialist:

1. **High-dose ifosfamide is the dominant near-term immune event.** Ifosfamide is profoundly
   lymphodepleting. Any checkpoint-based strategy discussed here is necessarily a **post-treatment
   sequencing question**, not a concurrent one — there is essentially no functional T-cell
   compartment to "release the brake" on during active high-dose ifosfamide.
2. **mRNA vaccine team finding incorporated (no relevant effect):** per
   `simulation-output/mrna-vaccine-research/mrna-vaccine-summary-v2.md` §7, BNT162b2-induced
   T-cell memory has waned over 2+ years and is spike-specific; there is **no documented
   persistent effect on T-cell repertoire, PD-1/PD-L1, or the Nectin axis (TIGIT/DNAM-1/CD96/PVR/
   NKG2A/HLA-E) at this patient's current timepoint**. "No relevant effect found — here's what
   does matter instead" is the correct framing, and what matters instead is VDC/IE-induced
   lymphodepletion/reconstitution, post-WLI immune remodeling, and the imminent ifosfamide course.
3. **WLI abscopal context (carried forward):** the single relapsing lung lesion sits in a
   previously-irradiated field. Radiation-induced ICD/STING priming is real mechanistically but
   whether it persists >1 year post-WLI is unestablished (see "What I Could Not Establish").
4. **Doxorubicin-as-ICD-inducer (new in this run, from V4 expansion ADR-0006 module A2):** the
   prior VDC/IE backbone already contained an anthracycline. Doxorubicin is a documented
   immunogenic-cell-death inducer (CALR/HMGB1/ATP emission). This is a **retrospective framing
   question** — was there a residual ICD-primed state from 2024-2025 doxorubicin exposure, and
   does it interact with anything plannable now? Addressed under Forward Hypotheses.

---

## PD-1 / PD-L1 / CTLA-4 BIOLOGY

### PD-1/PD-L1 axis

- **PD-1 (PDCD1):** inhibitory receptor on activated/exhausted CD8+ T-cells. Ligand engagement
  (PD-L1/CD274 or PD-L2/PDCD1LG2) recruits SHP-2 to the PD-1 cytoplasmic ITSM/ITIM motifs,
  dephosphorylating TCR/CD28 signaling intermediates and suppressing proliferation, IFN-γ/TNF-α
  production, and cytotoxic granule release. [Mechanism: Established, general immunology; **no
  direct CIC-DUX4 data**]
- **PD-L1 (CD274):** expressed on tumor cells and tumor-infiltrating myeloid cells, inducible by
  IFN-γ via JAK1/2-STAT1-IRF1 signaling at the CD274 promoter, and constitutively elevated in some
  tumors via genomic amplification or super-enhancer activity at the locus. PD-L1 expression has
  been reported in a minority of cases in small CIC-rearranged sarcoma series, but there is no
  large systematic IHC dataset specific to CIC-DUX4. Evidence tier: **Mechanistic** (PD-L1
  induction biology) / **Preclinical-Cell-to-clinical-observational** (small-series PD-L1 reports
  in CIC-rearranged sarcoma) — `[no specific PMID verified this session for a CIC-DUX4 PD-L1 IHC
  series; treat as unestablished rather than cite a number]`.
- **CTLA-4 (CD152):** expressed on activated T-cells and constitutively on Tregs; competes with
  CD28 for B7-1/B7-2 (CD80/CD86) on antigen-presenting cells, raising the threshold for T-cell
  priming. Anti-CTLA-4 (ipilimumab) is FDA-approved for melanoma, RCC, NSCLC, hepatocellular
  carcinoma, and (in combination with nivolumab) several other indications — **not approved as
  monotherapy for sarcoma**. Mechanistic rationale in sarcoma is Treg depletion in the TME plus
  broadened T-cell priming, tested in combination (see Alliance A091401 below). [Established
  mechanism / Established approval in other cancers / Clinical-Trial in sarcoma combination]

### Key evasion mechanism relevant to CIC-DUX4 — the "double shield"

CIC-DUX4 tumors are hypothesized to evade T-cell killing via two compounding mechanisms, neither
of which has been directly measured in CIC-DUX4 tissue:

1. **MHC-I downregulation** — silencing of HLA-A/B/C, B2M, TAP1/TAP2, and the transcriptional
   master-regulator NLRC5, via repressive chromatin states at antigen-presentation-machinery (APM)
   loci. [Mechanistic; documented in other PRC2-dependent and chromatin-disrupted sarcomas;
   **CIC-DUX4-specific MHC-I status is unmeasured**]
2. **PD-L1 upregulation** — via the IFN-γ/JAK-STAT route above, potentially amplified by
   BRD4-driven super-enhancer activity at CD274 in CIC-DUX4's BRD4-dependent transcriptional
   program (V1/V3 framing). [Mechanistic; **CIC-DUX4-specific PD-L1 status is unmeasured**]

**If both hold**, T-cells cannot see the cell (MHC-I-low) and, if they do encounter it, the kill
signal is suppressed (PD-L1-high) — the mechanistic rationale for "restore visibility first, then
relieve the brake." This is the **V3→V4 bridge**, reconciled below against V3's updated ranking.

---

## CLINICAL CPI EVIDENCE IN SARCOMA

### SARC028 (NCT02301039) — Pembrolizumab in advanced sarcoma

- Phase 2, two-cohort (soft-tissue sarcoma n=42 / bone sarcoma n=42), single-arm, open-label.
- Soft-tissue cohort by histotype: undifferentiated pleomorphic sarcoma (UPS) and dedifferentiated
  liposarcoma (DDLPS) showed the most encouraging activity; the primary endpoint (objective
  response) was **not met overall** for either cohort.
- **CIC-rearranged sarcoma was not enrolled as a distinct cohort — too rare for a dedicated arm.
  No CIC-DUX4-specific pembrolizumab data exist.**
- Evidence tier: **Clinical-Trial** (Tawbi et al., *Lancet Oncology* 2017;18(11):1493-1501, **PMID
  28988646** — corrected from a prior session's citation, which had transposed a digit). Transfer
  to CIC-DUX4: mechanistically plausible (checkpoint biology is general), but the **histotypes
  that responded (UPS/DDLPS) are high-TMB, genomically complex** — the opposite of CIC-DUX4's
  genomically simple, single-driver, presumed-low-TMB profile. This is a **negative-leaning
  prior**, not a positive one, for monotherapy response.

### Alliance A091401 (NCT02500797) — Nivolumab ± ipilimumab in metastatic sarcoma

- Open-label, randomized, non-comparative, two-cohort phase 2 (n=42 per arm in the original
  report; expanded with GIST/UPS/DDLPS cohorts in a 2024 follow-up).
- Nivolumab monotherapy: 2/38 (5%) confirmed objective responses. Nivolumab + ipilimumab: 6/38
  (16%) confirmed objective responses — the combination arm met its primary endpoint and "warrants
  further study," per the authors; monotherapy alone "does not warrant further study in an
  unselected sarcoma population."
- UPS and DDLPS again carried most of the signal; **CIC-rearranged sarcoma was not analyzed as a
  separate subgroup.**
- Evidence tier: **Clinical-Trial** (D'Angelo et al., *Lancet Oncology* 2018;19(3):416-426 —
  `[PMID not independently re-verified this session; prior session's citation, "PMID 30501812 /
  NEJM 2018," is INCORRECT — the paper is in Lancet Oncology, not NEJM. Cite by journal/year/volume
  until a PMID is confirmed live.]`). 2024 expansion-cohort/correlative-analysis follow-up:
  PMID 39343511 (*J Immunother Cancer*, 2024-09-28) — verified this session via search.

### Sarcoma CPI reality check (mandatory honest flag)

Checkpoint monotherapy response rates in sarcoma are **modest overall** and concentrated in
high-TMB/complex-karyotype histotypes (UPS, DDLPS, some pleomorphic sarcomas). CIC-rearranged
sarcoma is a translocation-driven, genomically simple tumor, the class of disease that
**typically predicts poor checkpoint-monotherapy response** in pan-cancer TMB analyses. **Do not
overstate the probability of CPI monotherapy response in CIC-rearranged sarcoma** — if anything,
the existing trial evidence argues the opposite of a favorable prior, independent of the
MHC-I-visibility question.

---

## THE V3→V4 BRIDGE — RECONCILED AGAINST THIS RUN'S V3 OUTPUT

V3's `v3-summary-v3.md` MHC-I Upregulation Candidates section (read in full for this output) ranks
candidates as follows. This supersedes the prior run's framing, which led with EZH2i.

| Rank | V3 candidate | MHC-I mechanism | Tier | CIC-DUX4 direct? | Fusion-dependence |
|---|---|---|---|---|---|
| 1 | **HDAC inhibitors** (class I — vorinostat, romidepsin, panobinostat, belinostat) | H3K27ac/H4ac increase opens APM loci (TAP1/2, PSMB8/9, HLA-A/B/C, B2M); viral-mimicry/type-I-IFN/STAT1 route via ERV reactivation | Preclinical-Cell (glioma, liver, lymphoma) / Clinical-Trial (FDA-approved class, different indication — cutaneous T-cell lymphoma) | None direct | **Fusion-agnostic** |
| 2 | **DNMT inhibitors** (azacitidine, decitabine, guadecitabine) | Reverses APM/HLA/TAP promoter hypermethylation; ERV reactivation → cGAS-STING/type-I IFN → STAT1-driven APM transcription | Clinical-Trial (breast cancer; mechanism class established) | None direct | **Fusion-agnostic** |
| 3 | **EZH2 inhibitors** (tazemetostat class) — **DOWNGRADED** | PRC2/H3K27me3 removal restores APM transcription in PRC2-dependent tumors | Doubly caveated (see below) | None direct; CIC-DUX4 premise now contested | Fusion-agnostic mechanism, but access-closed |
| 4 | **BET inhibitors** (OTX015, BMS-986158, AZD5153) | Variable, context-dependent effect on interferon-stimulated genes and MHC-I/PD-L1; weakest of the four classes for MHC-I specifically | Preclinical-Cell / Clinical-Trial | None direct | Fusion-agnostic, low-confidence direction |

### What changed from the prior (v1) run, and why it matters for the T-cell/checkpoint arm

The prior run's checkpoint output anchored the entire V3→V4 bridge on **"EZH2i → MHC-I →
anti-PD-1"** (tazemetostat + pembrolizumab). That framing is **no longer the lead candidate**, for
two independently-compounding reasons (carried forward from V3, live-verified 2026-06-14):

1. **Mechanistic premise caveat:** a 2024 CIC-DUX4 chromatin-profiling study (Bakaric et al.,
   *Cancers* 2024;16(2):457, **PMC10814785**, DOI 10.3390/cancers16020457) found CIC-DUX4 functions
   as a **p300/CBP-driven transcriptional activator**, not primarily a PRC2-dependent repressor —
   undercutting the rationale for EZH2i specifically *in CIC-DUX4* (this does not undercut HDACi/
   DNMTi, whose MHC-I mechanism runs through viral-mimicry/interferon biology independent of PRC2
   status).
2. **Access caveat:** on **2026-03-09, Ipsen voluntarily withdrew tazemetostat (Tazverik) from ALL
   markets and ALL indications worldwide**, following a SYMPHONY-1 secondary-hematologic-malignancy
   signal (5.7% vs 0% MDS/AML). Tazemetostat is now an **F5/concept-only** agent. EZH2 was never
   approved by EMA. The successor valemetostat (dual EZH1/EZH2i) inherits an elevated
   index-of-suspicion for the same class effect and is not a reassurance.

**Net effect on the checkpoint arm: the mechanistically and regulatorily cleanest priming agents
for a future "epigenetic priming → checkpoint" sequence are now class-I HDACi (vorinostat,
romidepsin, panobinostat, belinostat — all FDA-approved for other indications, hence at least
F1-accessible as repurposed agents pending oncologist evaluation) and DNMTi (azacitidine,
decitabine — also FDA-approved, F1-accessible as repurposed agents), NOT tazemetostat.** This is a
**reframing of which agent anchors the bridge**, not a new claim that the bridge itself is
stronger.

### What evidence exists for "epigenetic priming THEN checkpoint inhibitor" as a combination, specifically?

This is the question this run was specifically asked to sharpen. Honest accounting:

- **HDACi + anti-PD-1, mechanism-matched precedent (closest real trial):** the PEMDAC study
  (entinostat + pembrolizumab in metastatic **uveal melanoma**, NCT02697630, Johnson et al., *Nat
  Commun* 2021, PMID 34376667) tested exactly this sequencing logic — class-I HDACi to restore
  HLA/antigen-presentation machinery and reduce myeloid-derived suppressor cells, then anti-PD-1 —
  and reported objective responses in a tumor type (uveal melanoma) that is itself
  checkpoint-monotherapy-refractory and low-TMB, similar to CIC-DUX4's expected profile. Evidence
  tier: **Clinical-Trial** (uveal melanoma, not sarcoma — **P3 rung**, solid-tumor-with-named-
  mechanism, per the Directness ladder ADR-0014). **No sarcoma-specific HDACi+CPI combination
  trial was identified this session** — `[the prior v1 session's citation "NCT02890069...sarcoma
  cohort" does NOT correspond to an HDACi+pembrolizumab sarcoma trial on live lookup; NCT02890069
  is a different study (PDR001/LCL161/everolimus/panobinostat in breast/colorectal/NSCLC). That
  prior citation is RETRACTED here as inaccurate — do not carry it forward.]`
- **DNMTi + checkpoint, mechanism-matched precedent:** azacitidine-class viral-mimicry → cGAS-
  STING → type-I IFN → MHC-I upregulation, combined with checkpoint blockade, has been explored in
  multiple solid-tumor trials on the rationale that ERV-derepression increases both antigenicity
  (new ERV-derived peptides on MHC-I) and adjuvanticity (type-I IFN). **No CIC-DUX4 or
  CIC-rearranged-sarcoma-specific DNMTi+CPI trial was identified.** Evidence tier for the
  combination rationale: **Mechanistic**, anchored to **Clinical-Trial**-tier component mechanisms
  (DNMTi → MHC-I, Rank 2 above; CPI → T-cell release, established class).
- **What the combination evidence does NOT establish:** that HDACi/DNMTi priming produces a
  *measurable MHC-I increase on the actual tumor* before the CPI is given (most combination trials
  give both agents together or near-simultaneously, not as a sequential "prime, confirm, then
  release" protocol with on-treatment biopsy confirmation of MHC-I change). The "prime THEN
  release" framing as a deliberately **sequenced, biomarker-gated** strategy — rather than a fixed
  co-administration schedule — is itself closer to **Theoretical/Forward-Hypothesis** territory
  than an established combination-trial design. See Forward Hypothesis 2.

**Bottom line for this patient, right now:** even with the reframed HDACi/DNMTi-anchored bridge,
**the immediate clinical reality is that high-dose ifosfamide is about to profoundly lymphodeplete
this patient** — any epigenetic-priming-then-checkpoint sequence is a **post-ifosfamide-recovery**
question, not a concurrent one, and the dominant near-term consideration is *when*, not *which
agent*.

---

## THE NECTIN–TIGIT–DNAM-1 AXIS AND T-CELL EXHAUSTION (from V4 expansion, ADR-0006)

Reconciled from `simulation-output/v4-immune-watchdog/immune-watchdog-expansion.md` (module B),
applied to the T-cell/checkpoint framing:

- **DNAM-1 (CD226)** is an activating receptor on CD8 T-cells (and NK cells) that binds tumor
  PVR/CD155 and Nectin-2/CD112 to deliver a co-stimulatory signal. **TIGIT** binds the same
  ligands (PVR/CD155) with **higher affinity than DNAM-1**, out-competing the activating receptor
  and delivering an inhibitory ITIM signal — TIGIT is enriched on exhausted tumor-infiltrating
  lymphocytes. [Mechanistic, general immuno-oncology; **CIC-DUX4 PVR/Nectin-2/TIGIT/DNAM-1
  expression is entirely unmeasured**]
- **Cautionary precedent — anti-TIGIT receptor blockade has FAILED at phase 3.** Tiragolumab
  (anti-TIGIT) + atezolizumab did not improve overall survival in PD-L1-high NSCLC (SKYSCRAPER-01,
  final analysis 2024-11-26) and failed in extensive-stage SCLC (SKYSCRAPER-02, 2022). Evidence
  tier: **Clinical-Trial (negative)**. **This is directly relevant to any checkpoint-stacking
  enthusiasm for this patient** — single-node receptor-level blockade of one inhibitory axis,
  even when the target biology is sound at the mechanism level, has **not** translated to clinical
  benefit in the most advanced program tested. The lesson for a CIC-DUX4 checkpoint strategy:
  **be skeptical of "just add another checkpoint inhibitor" framing** — PD-1/TIGIT/CTLA-4
  redundancy (CD96 and PVRIG/CD112R provide further backup inhibitory receptors on the same axis,
  per V4 expansion module B3) means single-node blockade may be systematically insufficient.
- **NTX1088 (anti-PVR/CD155) — ligand-side alternative, live-verified this session
  (2026-06-14):** NTX1088 is a first-in-class monoclonal antibody against **PVR/CD155** —
  removing the shared ligand for TIGIT, CD96, *and* PVRIG in one step, while simultaneously
  **restoring surface DNAM-1** on T and NK cells (a dual de-repression + co-stimulation
  mechanism, mechanistically distinct from the failed receptor-level TIGIT blockade). Phase 1
  (NCT05378425, monotherapy and + pembrolizumab, advanced solid tumors) is confirmed
  **RECRUITING** as of November 2024, with **April 2026 preliminary clinical data reporting
  restoration of DNAM1 (CD226) expression and function on peripheral T and NK cells across
  multiple dose levels** — described in conference materials as "the first-ever clinical
  restoration of DNAM1." Evidence tier: **Clinical-Trial (Phase 1, early; mechanism-of-action
  signal reported, efficacy not yet reported)**. Not sarcoma-specific. Feasibility band: **F3**
  (Phase 1, recruiting, multi-site including academic centers — not accessible outside a trial).
  **`[VERIFY before relying on this — status is perishable; re-check ClinicalTrials.gov and
  conference-abstract follow-up before any external use]`**
- **T-cell-specific implication:** because TIGIT is expressed on exhausted **CD8 T-cells** (not
  just NK cells), the NTX1088/PVR-axis rationale is **not purely an NK-cell consideration** — it
  is directly relevant to this T-cell/checkpoint file. If this patient's tumor expresses
  PVR/CD155 (unmeasured), a ligand-side PVR blockade could in principle de-repress *both* the NK
  arm (NK specialist's primary framing) *and* the exhausted-CD8 arm simultaneously — a
  potential single-agent route to two V4 sub-mechanisms. This is **Theoretical** for CIC-DUX4
  (no expression data) but mechanistically coherent and **cross-flagged to the NK specialist** so
  the two files do not duplicate the PVR-axis framing independently.

---

## ICD / DANGER-SIGNALING AND THE T-CELL ARM (from V4 expansion module A, applied here)

The V4 expansion (module A2, ADR-0006) establishes that **doxorubicin — already part of this
patient's 2024-2025 VDC/IE regimen — is a documented immunogenic-cell-death (ICD) inducer**
(Casares et al., *J Exp Med* 2005, PMID 16365148; Obeid et al., *Nat Med* 2007, PMID 17187072):
anthracycline-induced cell death exposes calreticulin (CALR) on the dying-cell surface ("eat-me"
signal to dendritic cells via CD91), releases HMGB1 (TLR4-mediated cross-presentation licensing),
and releases ATP (P2RX7/NLRP3-inflammasome-mediated DC/T-cell adjuvant signal).

**For the T-cell/checkpoint arm specifically, this raises one question: did the 2024-2025
doxorubicin exposure generate any tumor-antigen-specific T-cell priming that could be "captured"
by a later checkpoint-relief step?** This is **entirely speculative for this patient** — ICD
competence (whether CIC-DUX4 cells actually undergo CALR exposure/HMGB1 release under
anthracycline, as opposed to non-immunogenic apoptosis) is **unmeasured** in this disease, and
even if ICD occurred in 2024-2025, any primed T-cell clones would have been subject to the
subsequent WLI, the one-year NED period, and now face the imminent ifosfamide-induced
lymphodepletion — a long and lossy chain. This is recorded as Forward Hypothesis 2, not a
recommendation.

---

## INFLAMMATION-STATE LENS APPLIED TO THE T-CELL/CHECKPOINT FRAMING

Per the V4 expansion's standing analytical discipline (ADR-0006), three states must be kept
distinct when reading this patient's immune/inflammatory markers in the context of any future
checkpoint strategy:

| State | What it would look like here | Checkpoint-relevant implication |
|---|---|---|
| **(1) Tumor-promoting inflammation** | Chronic ↑CRP/NLR/IL-6 from tumor-associated macrophage/MDSC activity in the residual lung lesion | Would argue **against** delay — a smoldering pro-tumor inflammatory state is not "good inflammation" to wait out |
| **(2) Anti-tumor immune activation** | ↑IFN-γ, CXCL9/10/11, CD8/NK infiltration in the post-WLI lung field — the state any epigenetic-priming-then-checkpoint strategy is *trying to amplify* | This is the target state; **broad anti-inflammatories/antioxidants in this window would be counterproductive** if such a state exists (none recommended in this file) |
| **(3) Treatment-related inflammatory toxicity** | Ifosfamide-related cystitis/encephalopathy-adjacent inflammatory signals, or future irAEs if a CPI is ever given | Must be managed for safety but **must not be misread as state (2)** on a CRP/NLR panel |

This patient's current dominant state is almost certainly **(3)-adjacent treatment effects from
the imminent ifosfamide course**, superimposed on a one-year-post-NED baseline of unknown
state-(1)/(2) balance. **No marker-based claim about this patient's current inflammatory state is
made here** — this is a framework for interpretation, not a result.

---

## DIETARY TRACK — PD-L1 MODULATION (HONEST ASSESSMENT, NOT PADDED)

This specialist is not proposing dietary/supplement interventions. The following is included only
because the schema requires an honest accounting of the (very thin) dietary PD-L1 literature.

| Compound | Claimed mechanism | Evidence tier | Critical caveat |
|---|---|---|---|
| Curcumin | NF-κB inhibition → reduced PD-L1 transcription, reported at 10-30 µM in cell lines | Preclinical-Cell | Dietary/supplement plasma concentrations are typically ~100-fold below the active range cited. **No patient-level PD-L1 modulation data exist for any tumor type.** If a curcumin supplement were under consideration for any reason, the chemo-interaction skill would need to be invoked (CYP3A4/P-gp interactions with ifosfamide/vincristine/etoposide are documented at supplement doses — this is a flag for the oncologist, not a recommendation made here). |
| Sulforaphane (broccoli/broccoli sprouts) | Nrf2-mediated effects on PD-L1; weak class-I HDAC inhibition in cell lines | Preclinical-Cell | Mechanistically the *same class* of action as the HDACi bridge above, but **at concentrations 10-10,000-fold below cell-line-active levels** (per V3's reconciled assessment). Juicing (vs. chopping/chewing) further destroys the myrosinase-activation step needed to liberate active sulforaphane. **No PD-L1 measurement after dietary sulforaphane exposure exists in any human tumor.** |
| EGCG | DNMT inhibition → possible PD-L1 promoter demethylation | Mechanistic | Same concentration-mismatch problem; dietary plasma EGCG is far below DNMT-inhibitory concentrations used in cell-line studies. |

**Overall assessment, unchanged from the prior run and reinforced by V3's reconciled dietary-tier
findings: no dietary compound has demonstrated clinically meaningful PD-L1 modulation in any
patient cohort at culinary intake. The class-level mechanism (HDACi/DNMTi-like action) is real but
the dietary-achievable exposure gap (10-10,000×) is the same gap V3 documented for the clinical
HDACi/DNMTi bridge itself — diet is not a substitute for the clinical-track agents.**

---

## CHEMO-INTERACTION NOTE

No dietary/supplement candidate with a concrete mechanism is being proposed in this output, so the
full `sarcoma-chemo-interactions` screen is not triggered here. The one standing flag: **if any
future clinical-track agent discussed above (HDACi, DNMTi, NTX1088, checkpoint inhibitors) is
considered, it would need to be sequenced around the imminent high-dose-ifosfamide course** —
ifosfamide's lymphodepleting effect would blunt any immune-priming or checkpoint-release strategy
given concurrently, independent of any drug-drug pharmacokinetic interaction. This is a
**sequencing/timing** consideration, not a CYP/P-gp/ROS interaction, and is the basis for Forward
Hypothesis 1.

---

## FORWARD HYPOTHESES

**[Forward Hypothesis 1] Post-ifosfamide lymphocyte-reconstitution window as the earliest
plausible entry point for an HDACi/DNMTi-anchored "epigenetic priming → checkpoint" sequence —
re-anchored to the reframed bridge agents.**

*Hypothesis:* High-dose ifosfamide produces profound lymphodepletion; the reconstitution window
(roughly weeks 4-12 post-completion in analogous lymphodepleting-chemotherapy contexts) is a
period of homeostatic T-cell proliferation with elevated IL-7/IL-15 signaling. If a class-I HDACi
(vorinostat/romidepsin/panobinostat/belinostat — all FDA-approved, repurposable, F1-accessible
pending oncologist evaluation) or a DNMTi (azacitidine/decitabine, also FDA-approved/F1) were
introduced during or just before this reconstitution window to upregulate tumor MHC-I, followed by
anti-PD-1 (pembrolizumab/nivolumab) as the reconstituting T-cell compartment expands, the
*timing* — not a novel agent — could be the lever that makes an otherwise-modest CPI prior (per
SARC028/Alliance A091401's low-TMB-unfavorable signal) more favorable for this specific patient.

*Mechanistic basis:* IL-7/IL-15-driven homeostatic proliferation of reconstituting T-cells +
HDACi/DNMTi-driven MHC-I/APM re-expression (V3 rank 1-2, viral-mimicry/type-I-IFN route) + anti-PD-1
release of the (newly visible) tumor-T-cell interaction.

*Test:* A window-of-opportunity phase 1b design: post-high-dose-ifosfamide, Day 28-35, a short
course of a class-I HDACi (with on-treatment biopsy or circulating-tumor-DNA/RNA readout for
MHC-I/APM transcript change — TAP1/2, HLA-A/B/C, B2M — confirming the priming step actually
occurred *before* proceeding) → anti-PD-1. Primary endpoints: MHC-I/APM induction (biomarker
gate), T-cell reconstitution kinetics (flow cytometry, TCR-repertoire diversity), tumor response
at 12 weeks.

*Why not yet tested:* the HDACi/DNMTi-anchored version of this sequencing hypothesis is new to
this run (the prior run's version was anchored to the now-withdrawn tazemetostat); ifosfamide as a
deliberate lymphodepleting platform for subsequent epigenetic-priming-plus-CPI has not been
formally tested in sarcoma. **Falsifier:** if on-treatment biopsy/ctDNA shows no MHC-I/APM
induction after the HDACi/DNMTi step, the priming half of the sequence has failed and proceeding to
anti-PD-1 would not be expected to differ from CPI-monotherapy's already-modest prior — the trial
should not proceed to the CPI arm without the biomarker gate.

**[Forward Hypothesis 2] Retrospective ICD-priming "residue" from 2024-2025 doxorubicin exposure —
testable via archived-tissue/blood, not a prospective intervention.**

*Hypothesis:* If CIC-DUX4 cells underwent CALR-exposing, HMGB1/ATP-releasing immunogenic death
under the 2024-2025 doxorubicin-containing VDC/IE regimen (V4 expansion module A2), some
tumor-antigen-specific T-cell clones may have been primed at that time. Given the subsequent WLI,
one-year NED interval, and now-imminent ifosfamide-induced lymphodepletion, **most or all of this
priming is likely lost** — but if archived peripheral-blood samples from the 2024-2025 treatment
period exist (P1/P2 provenance, ADR-0011), a retrospective TCR-repertoire analysis comparing
pre-doxorubicin vs. post-doxorubicin/post-surgery blood could establish *whether ICD-mediated
priming occurred at all* in this patient — independent of whether anything is plannable from it
now. A positive finding (clonal expansion of tumor-reactive T-cell clones temporally associated
with the doxorubicin-containing cycles) would be the first patient-level evidence that CIC-DUX4
cells are ICD-competent under anthracycline — a finding with implications far beyond this patient
(it would support designing *future* ICD-potentiation strategies around the anthracycline pulse,
as in V4 expansion's own Forward Hypothesis 2).

*Mechanistic basis:* CALR/HMGB1/ATP-driven DC cross-priming kinetics (V4 expansion modules A1/A3/
A4); doxorubicin ICD-induction in preclinical models (PMID 16365148, PMID 17187072).

*Test:* TCR-sequencing (e.g., immunoSEQ-type assay) on archived pre-treatment and post-VDC/IE
peripheral blood samples (if banked), looking for clonal T-cell expansions that emerged during the
doxorubicin-containing cycles and whether any such clones persist (even at low frequency) into the
current relapse timepoint. **Falsifier:** no detectable clonal expansion temporally associated
with doxorubicin cycles, or no persistence of any such clones to the present — either result would
indicate this patient's CIC-DUX4 cells are not meaningfully ICD-competent under anthracycline, or
that any priming was fully lost to subsequent lymphodepleting therapy and WLI.

*Why not yet tested:* this is a **retrospective, archived-sample** question that has not, to this
catalog's knowledge, been asked for any CIC-DUX4 patient; it requires no new prospective
intervention and (per ADR-0011) may be a near-zero-additional-cost addition to existing biomarker
work if appropriate samples were banked during 2024-2025.

---

## ATYPICAL-CASE NOTES (ADR-0008, ~5% fusion-unconfirmed)

This patient is **fusion-unconfirmed** (~5% atypical subgroup).

**FUSION-AGNOSTIC (applicable to this patient regardless of driver-resolution status):**
- All checkpoint-inhibitor mechanisms (PD-1/PD-L1/CTLA-4) — target host immune-checkpoint
  machinery, not the fusion junction.
- HDACi/DNMTi-mediated MHC-I/APM restoration (V3 ranks 1-2) — acts on host chromatin/methylome and
  interferon-signaling machinery, independent of which driver (D1-D5, per ADR-0008) is present.
- The Nectin–TIGIT–DNAM-1 axis (TIGIT, DNAM-1, PVR/CD155, NTX1088) — host receptor-ligand biology,
  fusion-independent.
- The ICD/doxorubicin framing (Forward Hypothesis 2) — depends on how CIC-DUX4 (or whatever the
  actual driver is) cells die under anthracycline, not on the fusion junction sequence per se,
  though ICD competence could in principle differ by driver — this is itself unmeasured for any
  driver.
- The inflammation-state lens — a host-biology interpretive framework, fully fusion-agnostic.

**FUSION-CONFIRMED ONLY (would not apply to this patient if fusion remains unconfirmed):**
- None of the entries in *this specific file* are fusion-dependent. (Junction-specific
  neoantigen-vaccine and CAR-T approaches are addressed in `neoantigen-vaccine.md`, not here.)

**Net assessment: every mechanism discussed in this T-cell/checkpoint file remains fully
applicable to this patient's atypical, fusion-unconfirmed status** — a meaningful point of
stability in an otherwise highly uncertain picture.

---

## WHAT I COULD NOT ESTABLISH

1. **CIC-DUX4-specific MHC-I (HLA-A/B/C, B2M, TAP1/2) and PD-L1 expression status** — no large
   systematic series exists; the entire "double shield" framing (MHC-I-low + PD-L1-high) is
   **mechanistic extrapolation**, not a measured finding in this disease or this patient.
2. **CIC-DUX4 tumor mutational burden (TMB)** — without this patient's WES/TMB data, the
   "low-TMB → poor CPI-monotherapy prior" argument is itself an extrapolation from the
   translocation-driven-sarcoma class, not this tumor specifically.
3. **Whether HDACi/DNMTi actually raise MHC-I on CIC-DUX4 tumor cells specifically** — the
   mechanism class is real in glioma/liver/lymphoma/breast-cancer contexts (V3's citations); **no
   CIC-DUX4 cell line or tumor has been tested**.
4. **Whether post-ifosfamide lymphocyte reconstitution in sarcoma patients shows the same
   IL-7/IL-15-driven proliferative window documented in other lymphodepletion contexts** — no
   published sarcoma-specific data identified.
5. **PVR/CD155, Nectin-2/CD112, TIGIT, and DNAM-1 expression on CIC-DUX4 tumor cells and TILs** —
   entirely unmeasured; the NTX1088/PVR-axis T-cell rationale rests on extrapolation from other
   solid tumors.
6. **Whether any ICD priming occurred in this patient under 2024-2025 doxorubicin exposure** —
   Forward Hypothesis 2 proposes a test; no data exist either way.
7. **Whether post-WLI STING/IFN priming persists in this patient's lung at the current (>1 year
   post-WLI) timepoint** — acute radiation-ICD/STING activation is documented; persistence at this
   timepoint is unknown.
8. **An exact PMID for the Alliance A091401 2018 Lancet Oncology paper** — I corrected the prior
   session's incorrect "NEJM 2018, PMID 30501812" citation (the paper is in Lancet Oncology, not
   NEJM) but did not independently confirm a replacement PMID this session; cite by
   journal/year/volume/NCT until a PMID is live-verified.

### Red-team self-challenge (ADR-0017, one pass)

1. **Load-bearing assumption:** that HDACi/DNMTi-driven MHC-I restoration in *other* tumor types
   (glioma, liver, breast) transfers mechanistically to CIC-DUX4 — i.e., that CIC-DUX4 cells have
   the same baseline APM-locus repression that these agents relieve elsewhere.
2. **Disconfirmation search:** the strongest evidence *against* the bridge being CIC-DUX4-relevant
   at all is the same Bakaric/PMC10814785 finding that demoted EZH2i — if CIC-DUX4's dominant
   chromatin lesion is p300/CBP-driven *activation* of its own program rather than PRC2-mediated
   *repression* of APM genes, it is not guaranteed that APM loci are repressed in CIC-DUX4 in the
   first place, in which case HDACi/DNMTi might have **nothing to restore** (a ceiling effect, not
   a floor problem). I did not find a study directly addressing baseline APM-locus chromatin state
   in CIC-DUX4 — this is a genuine open gap, not just "untested," and it could undercut the
   *entire* V3→V4 bridge, not just the EZH2i leg of it.
3. **Alternative hypothesis outside V1-V4:** if CIC-DUX4's MHC-I status turns out to be
   baseline-normal (not repressed), the highest-value V4 lever might not be "restore visibility"
   at all but purely the **NK/Nectin-axis arm** (which works on MHC-I-low cells *as they currently
   are*, no priming needed) — this doesn't require a new vector, but it does mean this file's
   bridge-centric framing could be over-weighted relative to the NK specialist's file if the
   baseline-MHC-I assumption is wrong.
4. **Flip test:** if HDACi/DNMTi do *not* raise MHC-I in CIC-DUX4 (assumption wrong), Forward
   Hypothesis 1's biomarker gate (on-treatment MHC-I/APM transcript check before proceeding to
   anti-PD-1) is specifically designed to catch this — the hypothesis is structured so that a
   "no" answer stops the sequence early rather than wasting the CPI step. The hypothesis survives
   the flip test in the sense that it is **self-falsifying by design**, but the underlying
   recommendation ("HDACi/DNMTi-anchored bridge is V4's best epigenetic-priming candidate") would
   not survive — it would revert to "no good priming agent identified," strengthening the
   NK/Nectin-axis-first framing (cross-flag to NK specialist, consistent with the V4 expansion's
   existing NK-first sequencing-tension note).
5. **Steer audit:** this file's brief asked specifically to work out the rationale for "epigenetic
   priming THEN checkpoint inhibitor" sequencing — I have tried to **test** that framing (by
   searching for the actual combination-trial evidence and finding it thin/indirect, by flagging
   the unverified baseline-APM-state gap above, and by retracting a fabricated prior citation)
   rather than simply **confirming** it. The honest output is: the mechanism class is real and
   Clinical-Trial tier *in other tumors*, the sequencing logic is *coherent*, but **direct support
   for "this specific sequence in this specific disease" is Theoretical**, and the patient's
   imminent ifosfamide course makes the question moot for the next several months regardless.

---

*Grounding (OpenMed NER, `--team v4-checkpoint`):* PD-L1/CTLA-4/PDCD1/CD274/B2M/HLA-B/HLA-C/NLRC5/
DNAM-1/CD226/PVR/CD155/NKG2A/HLA-E were recognized as Anatomy-class biomedical entities; pembrolizumab,
nivolumab, ipilimumab, vorinostat, romidepsin, panobinostat, belinostat, entinostat, azacitidine,
decitabine, guadecitabine, tazemetostat, valemetostat, NTX1088, tiragolumab, TIGIT, monalizumab,
ATP, and the VDC/IE drug set were recognized as CHEM-class entities; CIC-DUX4 and sarcoma were
recognized as Disease/Cancer entities; STING was tagged DISEASE by the model (a known model
quirk — STING here refers to the cGAS-STING pathway, not a disease entity). HLA-A, PD-1, TAP1/TAP2,
HMGB1, calreticulin, cGAS, and IL-15 were not individually broken out due to multi-line input
formatting in this run but are standard, well-recognized biomedical terms. NER confirms entity
recognition only — it is not a substitute for the citation/status verification performed above.

**Research-simulation output, not medical advice.**
