# V3 Hot Patching — PROTAC / ASO (Clinical/Experimental) Specialist

**Tag: Clinical / Experimental — not naturally achievable; for awareness only.**

**One-line summary:** This output covers (1) the published landscape of antisense
oligonucleotides (ASOs) and PROTACs/molecular-glue degraders relevant to fusion-oncoprotein
sarcomas, screened specifically for any CIC-DUX4-targeted construct (none found — stated
explicitly below); and (2) the current clinical-trial status of EZH2 inhibitors (tazemetostat,
valemetostat), BET inhibitors (OTX015/birabresib, BMS-986158, AZD5153, ZEN-3694), and CDK4/6
inhibitors (palbociclib, ribociclib, abemaciclib) in sarcoma, with live-verified regulatory
status as of 2026-06-14. **Deliberately excluded:** dietary/naturally-achievable epigenetic
modulators (covered by the Epigenetic and Differentiation Therapy specialists), CRISPR
excision approaches (Theoretical, covered in the V3 vector-context table), and any
speculative gene-therapy construct not in the published literature or a registered trial.

**Confidence: medium** — the clinical-trial landscape (BETi, CDK4/6i, EZH2i) is well-documented
and was live-verified this session; the absence of a CIC-DUX4-specific ASO/PROTAC is a negative
finding from targeted searches (absence-of-evidence, not proof-of-absence) but is consistent
with this being an ultra-rare fusion with no dedicated drug-discovery program.

---

## 1. Antisense Oligonucleotides (ASOs) Targeting CIC-DUX4

**No published CIC-DUX4-specific ASO exists.** Targeted literature searches for
"CIC-DUX4 antisense oligonucleotide," "CIC-DUX4 ASO fusion junction," and related terms
returned no construct, preclinical paper, or registered trial describing an ASO directed at
the CIC::DUX4 fusion transcript or its junction sequence.

**What does exist (general ASO technology, not CIC-DUX4-specific):**

| Entry | Mechanism | Status | Tier | Evidence in CIC-DUX4 specifically? |
|---|---|---|---|---|
| ASO platform technology (general) | Synthetic oligonucleotides hybridize to a target pre-mRNA/mRNA, recruiting RNase H1 (degradation) or sterically blocking splicing/translation. Sequence-specific — requires a known, stable target sequence. | Established for other indications: nusinersen (Spinraza, SMA — FDA 2016/EMA 2017), eteplirsen and successors (DMD exon-skipping, FDA-approved under accelerated pathway), milasen (N-of-1 custom ASO, *NEJM* 2019, PMID 31597037) | Established (other diseases) | None direct |
| Fusion-junction ASO concept (general, not CIC-DUX4) | A junction-spanning ASO could in principle target the unique CIC-DUX4 fusion mRNA sequence (the breakpoint creates a novel sequence absent from either wild-type transcript), sparing normal CIC and DUX4. This is the same logic used for fusion-junction-targeted approaches proposed for EWSR1-FLI1 (Ewing sarcoma) in the academic literature. | No clinical-stage fusion-junction ASO exists for *any* sarcoma fusion to our knowledge from this search; EWSR1-FLI1 siRNA/ASO knockdown is preclinical-cell/animal only | Theoretical (for CIC-DUX4) / Preclinical (for EWSR1-FLI1 analogues) `[no direct citation for a CIC-DUX4 construct; mechanism inferred from general fusion-junction ASO logic and the milasen N-of-1 precedent]` | None direct |

**Why this matters mechanistically:** The CIC::DUX4 breakpoint creates a chimeric mRNA with a
junction sequence not present in either wild-type CIC or wild-type DUX4 transcripts. In
principle this is the cleanest possible ASO target — a sequence unique to the cancer cell.
The barrier is not biological plausibility but (a) the extreme rarity of the fusion (no
economic case for a dedicated ASO program), (b) the milasen precedent shows custom ASOs are
technically and regulatorily *possible* for an n-of-1 (PMID 31597037, Batten disease, ~$$ and
~1-year development timeline by the Yu lab at Boston Children's), and (c) **delivery to a deep
soft-tissue/lung-metastatic sarcoma is unsolved** — ASOs to date are delivered intrathecally
(CNS, e.g., nusinersen) or systemically with hepatic/renal tropism (e.g., GalNAc-conjugated
ASOs for liver targets); there is no validated delivery route for a solid extrahepatic sarcoma
mass plus lung metastases.

**Atypical-case flag (ADR-0008, ~5% fusion-unconfirmed subgroup):** Any future CIC-DUX4
junction-ASO would be **doubly contingent** for this patient: (1) it requires the fusion to be
present at all (driver hypotheses D3–D5 in the driver-uncertainty model have **zero**
applicability for a junction ASO — applicability score 0), and (2) it requires the *specific*
junction sequence to be resolved (D1/D2 score 1, but only *after* long-read WGS+RNA-seq
identifies the breakpoint). **Tag: driver-contingent — hold until the driver is resolved**
(per `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`,
applicability matrix row "junction-specific ASO / vaccine").

---

## 2. PROTACs and Molecular-Glue Degraders

### 2a. BET-protein PROTACs

| Entry | Mechanism | Status | Tier | Evidence in CIC-DUX4 specifically? |
|---|---|---|---|---|
| ARV-771 | Pan-BET (BRD2/3/4) PROTAC; VHL-recruiting; degrades BRD4 via ubiquitin-proteasome pathway | Preclinical only — published in prostate cancer (PNAS 2016, PMID 27274050) and osteosarcoma (PMC6814818, "PROTAC induced-BET protein degradation exhibits potent anti-osteosarcoma activity by triggering apoptosis"). No clinical trial registration found. | Preclinical-Cell / Preclinical-Animal (other cancers) | None direct |
| dBET6 | Pan-BET PROTAC; cereblon (CRBN)-recruiting; IC50 ~14 nM in cell-line assays | Preclinical only — tool compound widely used in academic labs; bioavailability/tissue-specificity limitations explicitly noted in the literature as barriers to clinical translation `[no direct citation for a specific clinical-translation barrier statement; mechanism inferred from general PROTAC PK literature]` | Preclinical-Cell | None direct |
| ROR1-targeting antibody-PROTAC conjugate (BRD4 degrader payload) | Antibody-drug-conjugate format delivering a BRD4-degrading PROTAC payload to ROR1-expressing solid tumors | Preclinical (PMC11729552, 2024–2025) | Preclinical-Cell/Animal | None direct — ROR1 expression in CIC-DUX4 not established in this search |

**No BET-PROTAC has reached a registered human trial** as of this search (2026-06-14). All BET
inhibitors currently in sarcoma trials (Section 3 below) are small-molecule bromodomain
*inhibitors* (occupancy-based), not degraders (PROTACs/molecular glues). This is a genuine gap
between preclinical degrader technology and clinical reality for the BET target class.

### 2b. EZH2 / PRC2 degraders

No EZH2-targeted PROTAC or molecular glue in clinical development was identified. Current
clinical EZH2-pathway agents (tazemetostat, valemetostat) are catalytic small-molecule
inhibitors of the SET-domain methyltransferase activity, not degraders of the EZH2 protein
itself.

### 2c. Degraders of fusion oncoproteins generally (not CIC-DUX4)

| Entry | Mechanism | Status | Tier | Evidence in CIC-DUX4 specifically? |
|---|---|---|---|---|
| dCBP-1 (p300/CBP degrader) | PROTAC-class degrader of p300/CBP histone acetyltransferases. CIC-DUX4 *requires* p300/CBP to acetylate H3K27 at its target loci and drive the oncogenic transcriptional program (the fusion's transactivation domain recruits p300/CBP). dCBP-1 treatment reduced CIC-DUX4 fusion-target gene expression in cell-line models. | Published preclinical-cell finding (PMC8511258, "Inactivation of the CIC-DUX4 oncogene through P300/CBP inhibition, a therapeutic approach for CIC-DUX4 sarcoma") | Preclinical-Cell | **Direct** — this is the one entry in this section with actual CIC-DUX4 cell-line data. Note: dCBP-1 does not degrade the CIC-DUX4 fusion protein itself; it degrades p300/CBP, indirectly silencing the fusion's transcriptional output. |
| Bimodal degrader-siRNA for DNAJB1::PRKACA (fibrolamellar carcinoma) | mRNA-delivered peptide degrader combined with siRNA, designed to selectively eliminate a different oncogenic fusion protein (DNAJB1-PRKACA, fibrolamellar carcinoma) while sparing native PRKACA | bioRxiv preprint, 2025-04-24 (DOI 10.1101/2025.04.24.650501) — **not peer-reviewed at time of this search** | Preclinical (unconfirmed/preprint) | None — different fusion (DNAJB1-PRKACA, not CIC-DUX4). Cited here only as evidence that **fusion-selective degrader platforms are an active area of technology development** that could in principle be retargeted to CIC-DUX4 if a tractable binding handle on the fusion were identified. |
| EWSR1::FLI1 "rewiring" with bivalent small molecules (EB-TCIP) | Chemically-induced-proximity (CIP) bivalent small molecule recruits FKBP12^F36V-tagged EWSR1::FLI1 to BCL6-bound chromatin sites, rewiring the fusion's transcriptional output toward pro-apoptotic genes — a *rewiring* rather than *degradation* strategy | Published 2025 (bioRxiv 10.1101/2025.03.14.643353; peer-reviewed in *JACS* 2025, PMC12851799, PMID 41307210) — proof-of-concept, uses an engineered FKBP12^F36V tag (not the native fusion), so not directly clinically deployable as-is | Preclinical-Cell | None — different fusion (EWSR1::FLI1, Ewing sarcoma). Cited as a **mechanistically distinct template** (proximity-induced transcriptional rewiring rather than protein degradation) that is conceptually portable to other "undruggable" transcription-factor fusions including CIC-DUX4. |

**Bottom line for Section 2:** No published CIC-DUX4-specific PROTAC exists. PROTAC/degrader
and chemically-induced-proximity technology exists and is advancing rapidly for BET proteins,
p300/CBP (with direct CIC-DUX4 cell-line data via dCBP-1), and other sarcoma fusion
oncoproteins (EWSR1::FLI1, DNAJB1::PRKACA) — but none of these platforms has been
clinically translated, and none has been specifically retargeted to CIC-DUX4.

---

## 3. Clinical Trial Landscape — EZH2i, BETi, CDK4/6i in Sarcoma

### 3a. EZH2 inhibitors

#### Tazemetostat (Tazverik) — HANDLE WITH CARE: MAJOR STATUS CHANGE 2026-03-09

**[VERIFY] Live-verified 2026-06-14 via WebSearch (OncLive, Ipsen press releases, GlobeNewswire,
CancerNetwork, Cancer Therapy Advisor, oncologynewscentral.com):**

- **FDA status: WITHDRAWN from ALL US indications, effective 2026-03-09.** On 2026-03-09, Ipsen
  announced the **voluntary worldwide withdrawal of Tazverik (tazemetostat) from all markets and
  all indications** — both relapsed/refractory follicular lymphoma (EZH2-mutant) and
  metastatic/locally-advanced epithelioid sarcoma (the 2020-01-23 accelerated approval). The
  trigger was an Independent Data Monitoring Committee finding from the Phase Ib/III
  **SYMPHONY-1** trial (tazemetostat + lenalidomide + rituximab vs. lenalidomide + rituximab in
  follicular lymphoma): **18/318 (5.7%) of tazemetostat-treated patients developed hematologic
  second primary malignancies** (predominantly MDS and AML, also B-ALL and CCUS) vs. **0
  reported in the control arm**. Ipsen is stopping treatment for all patients currently enrolled
  in SYMPHONY-1 (study remains open for long-term safety follow-up only, no new enrollment) and
  is **discontinuing all active tazemetostat clinical trials and expanded access programs**
  worldwide — this includes non-lymphoma trials (e.g., the MPNST trial, NCT04917042, discussed
  below) per the global "all trials" framing of the announcement, though the announcement's
  headline indications named are FL and epithelioid sarcoma specifically.
  Sources: Ipsen press release 2026-03-09 (ipsen.com/press-release/ipsen-voluntarily-withdraws-tazverik-tazemetostat-in-follicular-lymphoma-and-epithelioid-sarcoma-3251503), Ipsen update press release (...-3252192), OncLive, CancerNetwork, Cancer Therapy Advisor, Oncology Nurse Advisor, oncologynewscentral.com. Access date: 2026-06-14.

- **EMA status: tazemetostat was NEVER approved by the EMA.** Pre-withdrawal searches
  (everyone.org "Tazemetostat's EMA approval: What if waiting is no option?") confirm
  tazemetostat remained **unapproved in the EU** even before the March 2026 US withdrawal — it
  was available in Europe only via early-access/named-patient programs, not a centralized
  marketing authorization. Given the FDA withdrawal and the underlying safety signal (secondary
  hematologic malignancies), an EMA approval is now extremely unlikely to follow. **[VERIFY]**
  — searches did not find an EMA-specific statement dated after 2026-03-09, but given no EMA
  approval ever existed, "EMA withdrawal" is not the relevant frame; "EMA: never approved,
  and a pending application (if any) would now face the same safety data" is.

**Tier reassessment for this catalog:** Tazemetostat's tier for epithelioid sarcoma moves from
**Established** (as of the prior protocol-v1/v2 framing, FDA accelerated approval 2020-01-23)
to **historical-Established, now withdrawn** — i.e., the prior approval is a real historical
fact (the accelerated-approval mechanism and the trial data behind it, NCT02601950, remain
real), but **as of 2026-06-14 tazemetostat is not accessible to any patient through normal
prescribing channels in any major jurisdiction**, and the CIC-DUX4 extrapolation rationale
(PRC2/EZH2 dependency in BAF-disrupted fusion sarcomas) now also carries an unfavorable
risk-benefit signal (secondary hematologic malignancy) that did not previously factor into the
discussion. Feasibility band: **F5 (Concept-only / no access path)** — down from whatever band
the prior run assigned (this is a clean-slate v3 run; no prior band is being overwritten, but
the orchestrator should reconcile against `translational-feasibility-layer.md` and update it).
**Attrition reason (ADR-0013 framing): R4-regulatory / safety-driven, NOT R1-target-invalidated.**
The PRC2/EZH2-dependency mechanism in BAF-disrupted sarcomas is not biologically refuted by this
withdrawal — the drug was withdrawn for an off-target secondary-malignancy signal (genotoxicity
from broad EZH2/PRC2 inhibition in hematopoietic progenitors), not because EZH2 inhibition
failed to affect the tumor. Per ADR-0013, **R4/safety-driven closures do not carry negative
biology for the target mechanism** — but they do mean **this specific drug** is now off the
table, and **any successor EZH2/EZH1 inhibitor (e.g., valemetostat, below) inherits an
elevated index-of-suspicion for the same secondary-malignancy class effect** until shown
otherwise.

**Prior CIC-DUX4 extrapolation caveat (still applicable as historical context):**
Tazemetostat was FDA-approved 2020-01-23 for **epithelioid sarcoma** (an INI1/SMARCB1-deficient
tumor), via accelerated approval based on ORR ~15% (NCT02601950, basket study spanning
INI1-negative tumors and SS18-SSX1/2 synovial sarcoma). It was **never approved for
CIC-rearranged sarcoma** — the CIC-DUX4 rationale was always an **extrapolation** from shared
PRC2/EZH2 dependency in BAF-complex-disrupted fusion sarcomas (CIC-DUX4 chromatin profiling
shows PRC2-dependent epigenetic states; PMC10814785). With the drug now withdrawn entirely,
this extrapolation is now purely of historical/mechanistic interest unless a successor
EZH2/EZH1i with a cleaner safety profile becomes available.

#### Valemetostat (DS-3201b) — dual EZH1/EZH2 inhibitor, successor compound

| Entry | Mechanism | Status | Tier | Evidence in CIC-DUX4 specifically? |
|---|---|---|---|---|
| Valemetostat tosylate | Dual inhibitor of EZH1 and EZH2 (both PRC2 catalytic paralogs) — broader PRC2 blockade than tazemetostat (EZH2-selective) | **[VERIFY]** Active trial **NCT07303387** ("Efficacy and Safety of Valemetostat in Patients With Selected Solid Tumors") — a trial for solid tumors with alterations in SWI/SNF-complex genes (SMARCB1/A4/A2/C1/C2, ARID1A/1B, PBRM1, BAP1), 200 mg/day oral dosing, 28-day cycles, up to 2 years. Also a completed pediatric phase 1 trial (NCCH1904) in malignant solid tumors (ASCO 2025, JCO.2025.43.16_suppl.10003), and phase 1b combination trials with antibody-drug conjugates (trastuzumab deruxtecan, datopotamab deruxtecan) in solid tumors. Already FDA-approved (2022) for adult T-cell leukemia/lymphoma (a hematologic indication — separate from the solid-tumor program). Source: ClinicalTrials.gov NCT07303387, ASCO abstracts. Access date: 2026-06-14. | Clinical-Trial (solid tumors, SWI/SNF-altered) / Established (ATLL, hematologic — different indication) | None direct — but **mechanistically the most relevant successor**: CIC-DUX4 sarcomas arise in the context of BAF/SWI-SNF-complex disruption-adjacent epigenetic dependencies (PMC10814785 chromatin profiling), placing them conceptually within the population NCT07303387 targets (SWI/SNF-complex-gene-altered solid tumors), though CIC-DUX4 itself is not a SWI/SNF subunit mutation — **the analogy is PRC2-dependency, not the literal SWI/SNF-gene-alteration eligibility criterion**, so eligibility for this specific trial is uncertain without direct inquiry. |

**Important caveat on valemetostat:** Given the tazemetostat secondary-malignancy signal arose
from broad EZH2/PRC2 inhibition's effect on hematopoietic stem/progenitor cells (where PRC2
loss-of-function is a known driver of myeloid malignancy biology — PRC2 components including
EZH2 are recurrently *inactivated*, not just inhibited, in MDS/AML), and valemetostat inhibits
**both** EZH1 and EZH2 (broader PRC2 blockade than tazemetostat), **the secondary-malignancy
risk for valemetostat is plausibly equal or greater** — this has not been resolved by this
search and should be treated as an open safety question, not assumed favorable. **[VERIFY]**
— no valemetostat-specific secondary-malignancy safety signal was found in this search, but
absence of a signal in a smaller/shorter trial population does not establish absence of risk.

### 3b. BET inhibitors

| Entry | Mechanism | Status | Tier | Evidence in CIC-DUX4 specifically? |
|---|---|---|---|---|
| BMS-986158 | Selective BET (BRD2/3/4) bromodomain inhibitor — occupancy-based, not a degrader | **[VERIFY]** Phase 1/2a trial **NCT02419417** ("Study of BMS-986158 in Subjects With Select Advanced Cancers") — 83 patients dosed, monotherapy or + nivolumab, advanced solid tumors/hematologic malignancies. Results published (PMC9454848 / PMID 36077617, 2022): Schedule A (5 days on/2 days off, 0.75–4.5 mg) gave stable PK; most common AEs diarrhea (43%) and thrombocytopenia (39%); ~30% showed clinical benefit (not RECIST response — "clinical benefit" per the paper's definition). Additionally, **NCT03936465** is a phase 1 trial of BMS-986158 in pediatric/adolescent patients with relapsed/refractory solid tumors **including Ewing sarcoma** — the first pediatric BETi trial. Source: PMC9454848, ClinicalTrials.gov. Access date: 2026-06-14. | Clinical-Trial (solid tumors, incl. pediatric sarcoma cohort) | None direct — Ewing sarcoma (a different fusion-driven round-cell sarcoma with BRD4 super-enhancer dependency) is in NCT03936465; CIC-DUX4 not specifically named |
| AZD5153 | Bivalent BRD4 inhibitor (binds both bromodomains simultaneously — designed for improved potency/selectivity over monovalent BETi like OTX015) | **[VERIFY]** First-in-human Phase 1 (AACR/MCT 2023, "First-in-human Study of AZD5153...in Patients with Relapsed/Refractory Malignant Solid Tumors and Lymphoma") — 34 patients monotherapy, 15 + olaparib combination, enrolled 2017-06-30 to 2021-04-19. General advanced-solid-tumor population; no sarcoma-specific cohort identified in this search. Source: AACR Molecular Cancer Therapeutics. Access date: 2026-06-14. | Clinical-Trial (general solid tumors) | None direct |
| OTX015 / birabresib (MK-8628) | Monovalent pan-BET inhibitor (BRD2/3/4) | Phase 1 dose-finding in recurrent glioblastoma (NCT02296476) and earlier hematologic malignancy trials; **dose-limiting toxicities (notably thrombocytopenia) reported**, which motivated development of next-generation bivalent BETi like AZD5153. No active sarcoma-specific trial identified in this search. | Clinical-Trial (other cancers, largely historical/early-phase) | None direct |
| ZEN-3694 | BET inhibitor, primarily developed in combination with androgen-receptor-pathway inhibitors for prostate cancer | No sarcoma trial identified in this search. `[no direct citation for a sarcoma trial; flagged in the V3 vector-context list but not found active in sarcoma here]` | Clinical-Trial (prostate cancer) — **no sarcoma evidence found** | None direct |

**Mechanistic relevance to CIC-DUX4 (carried from preclinical literature, not this section's
trial search):** CIC-DUX4 chromatin profiling work (PMC10814785) identifies BRD4-dependent
super-enhancer programs as an "actionable therapeutic target" in CIC-rearranged sarcomas —
this is the mechanistic basis (Mechanistic tier for CIC-DUX4 specifically) for why BETi
appear in this catalog at all, even though no BETi trial enrolls CIC-DUX4 patients by molecular
selection.

### 3c. CDK4/6 inhibitors

| Entry | Mechanism | Status | Tier | Evidence in CIC-DUX4 specifically? |
|---|---|---|---|---|
| Palbociclib | Selective CDK4/6 inhibitor; blocks Rb phosphorylation, arrests cells in G1 | **Established** (FDA 2015, EMA 2016/2017 — HR+/HER2- breast cancer). In sarcoma: Phase 2 trial (GEIS group, EudraCT 2016-004039-19) in advanced sarcoma (excluding dedifferentiated liposarcoma) selected by CDK4 overexpression without CDKN2A loss — 23 enrolled/21 evaluable, 6-month PFS 29%, median PFS 4.2 months, median OS 12 months (*Nature Signal Transduction and Targeted Therapy* 2023, PMC10598203). Source: PMC10598203, JCO.2022.40.16_suppl.11511. Access date: 2026-06-14. | Established (breast cancer) / Clinical-Trial (sarcoma, biomarker-selected) | None direct — selection criterion was CDK4 overexpression / CDKN2A status, not fusion type; a CIC-DUX4 tumor with high CDK4/CCND1 expression could in principle have been eligible, but CIC-DUX4-specific enrollment/outcome data not reported |
| Abemaciclib | CDK4/6 inhibitor with additional CDK9 affinity (broader kinase profile than palbociclib/ribociclib, associated with less severe neutropenia) | **Established** (FDA 2017, EMA 2018 — HR+/HER2- breast cancer). In sarcoma: Phase 2 in dedifferentiated liposarcoma — median PFS 7 months (vs. 4 months for palbociclib in a comparable population per the same review). Source: ASCOPubs JCO Precision Oncology review (ascopubs.org/doi/full/10.1200/PO.21.00211). Access date: 2026-06-14. | Established (breast cancer) / Clinical-Trial (sarcoma, dedifferentiated liposarcoma) | None direct |
| Ribociclib | CDK4/6 inhibitor, similar selectivity profile to palbociclib | **Established** (FDA 2017, EMA 2017 — HR+/HER2- breast cancer). No sarcoma-specific trial identified in this search beyond general mention in CDK4/6i-in-sarcoma reviews. | Established (breast cancer) | None direct |

**Mechanistic relevance to CIC-DUX4:** CIC-DUX4 drives CCND1 overexpression as part of its
transcriptional program (downstream of the ETS-factor / super-enhancer activation described in
the V3 vector-context table), creating a plausible CDK4/CCND1 dependency. This is the basis for
CDK4/6i appearing in this catalog (Mechanistic tier for CIC-DUX4 specifically) — but, as with
BETi, **no CDK4/6i trial enrolls or reports CIC-DUX4 patients by molecular subtype**.

---

## 4. Driver-Robustness Summary (per ADR-0008 applicability matrix)

Per `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`,
this patient is in the fusion-**unconfirmed** subgroup (no confirming CIC fusion found on
genomic sequencing). The applicability matrix scores each intervention class across the five
driver hypotheses (D1 cryptic CIC-DUX4 … D5 orphan/no driver):

| Intervention class (this output) | D1 | D2 | D3 | D4 | D5 | Tag for THIS patient |
|---|---|---|---|---|---|---|
| BETi (BRD4, Section 3b) | 1 | 1 | 1 | 0.5 | 1 | **Driver-robust** — proceeds on pathway dependency (super-enhancer/ETS program), not fusion-junction-specific. Applicable even if D3–D5. |
| CDK4/6i (Section 3c) | 1 | 1 | 1 | 1 | 1 | **Fully driver-robust** — cell-cycle execution dependency is essentially driver-agnostic. |
| EZH2i / EZH1i (tazemetostat — now withdrawn; valemetostat, Section 3a) | 1 | 1 | 0.5 | 0.5 | 0.5 | **Partially driver-robust** — PRC2/MHC-I-low epigenetic-state dependency reduces under D3–D5, but tazemetostat's withdrawal makes this moot for the moment regardless of driver status. |
| dCBP-1 / p300-CBP degraders (Section 2c) | 1 | 0.5 | 0.5 | 0.5 | 0.5 | Mechanism depends on the fusion's transactivation domain recruiting p300/CBP — **partially driver-contingent**, strongest under D1/D2 (DUX4 transactivation domain present). |
| Junction-specific ASO (Section 1) | 1 | 1 | 0 | 0 | 0 | **DRIVER-CONTINGENT — hold until the driver is resolved.** Zero applicability under D3–D5 (no fusion to target); requires *both* a confirmed fusion (D1/D2) *and* a resolved junction sequence. |
| Fusion-protein-targeted PROTAC (hypothetical, Section 2 — none published) | 1 | 1 | 0 | 0 | 0 | **DRIVER-CONTINGENT — hold until the driver is resolved.** Same logic as junction ASO: no fusion protein exists to target under D3–D5. |

**Practical implication for this patient:** the BETi and CDK4/6i clinical-trial entries
(Sections 3b, 3c) remain relevant to discuss with an oncologist **regardless of whether the
driver is ever resolved** — they target downstream pathway dependencies, not the fusion
itself. The ASO and fusion-targeted-PROTAC entries (Sections 1, 2) are **not actionable until
and unless** long-read WGS+RNA-seq (the top EVSI test per ADR-0008) resolves a CIC-DUX4 (or
CIC-family) fusion and its junction sequence. EZH2i is now off the table as a drug regardless
of driver status (tazemetostat withdrawn; valemetostat unproven in this context and carrying
an unresolved class-effect safety question).

---

## 5. Forward Hypotheses

**[Forward Hypothesis 1]** — *Repurpose the EWSR1::FLI1 "transcriptional rewiring" chemical
biology (chemically-induced-proximity / bivalent small molecules, JACS 2025 PMC12851799) as a
template for CIC-DUX4.* **Mechanistic basis:** Both EWSR1::FLI1 and CIC::DUX4 are
"undruggable" transcription-factor fusions where the oncogenic activity comes from
aberrant transcriptional output (super-enhancer hijacking / ETS-target activation for
EWSR1::FLI1; ETS-factor-target activation via the DUX4 transactivation domain for CIC::DUX4),
not from an enzymatic active site that a classical small molecule can occupy. The EB-TCIP
approach degrades/rewires the fusion's transcriptional consequences via proximity-induced
chromatin remodeling rather than requiring a binding pocket on the fusion itself. **What
would test it:** A CIC::DUX4 cell-line model (the published CIC-DUX4 cell lines used in
PMC10814785's chromatin-profiling work would be a starting point) engineered with an
analogous FKBP12^F36V tag on the endogenous or exogenous CIC-DUX4 protein, then treated with
a bivalent small molecule recruiting it to a pro-apoptotic chromatin locus (e.g., BCL6-bound
sites, as in the EWSR1::FLI1 paper) — read out fusion-target-gene suppression and apoptosis
induction by RNA-seq/flow cytometry. **Why not yet tested:** the EB-TCIP technology is itself
brand-new (2025) and was developed specifically for EWSR1::FLI1; cross-application to
CIC-DUX4 would require a new academic collaboration and is not yet a published or funded
direction to our knowledge.

**[Forward Hypothesis 2]** — *The dCBP-1 (p300/CBP degrader) finding (PMC8511258) suggests a
"co-activator addiction" vulnerability that could be combined with BETi for synthetic
lethality in CIC-DUX4.* **Mechanistic basis:** CIC-DUX4's transactivation domain requires
p300/CBP for H3K27 acetylation at target loci, and separately the resulting open chromatin at
super-enhancers recruits BRD4 (the BETi target). If p300/CBP degradation (dCBP-1) reduces
H3K27ac deposition while BETi blocks the BRD4 reader step downstream, the two might act on
sequential steps of the same pathway — combination could be synergistic (deeper pathway
shutdown) or merely additive/redundant (same net effect via different nodes); either result
would be informative. **What would test it:** Dose-matrix combination assay (dCBP-1 ×
BMS-986158 or another clinical BETi) in the same CIC-DUX4 cell-line model used in PMC8511258
and PMC10814785, reading out fusion-target gene expression (RNA-seq), H3K27ac ChIP-seq, and
a synergy metric (e.g., Bliss independence or Loewe additivity) on viability. **Why not yet
tested:** dCBP-1 is a relatively new tool compound (PMC8511258 is itself a fairly recent
single-paper finding); a systematic combination screen in CIC-DUX4 models has not been
published in this search.

---

## 6. What I Could Not Establish

- **No CIC-DUX4-specific ASO or PROTAC exists** — this is a negative finding from targeted
  searches across PubMed/PMC/bioRxiv-indexed sources via WebSearch. Absence of evidence is not
  proof of absence (an unpublished industry program could exist), but no such program surfaced.
- **Whether the tazemetostat withdrawal's "all active clinical trials" language formally
  includes NCT04917042 (the MPNST phase 2 trial) and any CIC-rearranged-sarcoma-relevant basket
  cohorts of NCT02601950** — the announcements name follicular lymphoma and epithelioid sarcoma
  specifically as the approved indications being withdrawn, and separately state "all active
  tazemetostat clinical trials and expanded access programs" are being discontinued. I could
  not find a trial-by-trial list confirming NCT04917042's specific status post-2026-03-09.
  **[VERIFY]** before relying on tazemetostat being accessible via *any* trial mechanism.
- **Valemetostat's secondary-malignancy risk profile** relative to tazemetostat — given
  valemetostat is a *broader* PRC2 inhibitor (EZH1+EZH2 vs. EZH2-only), whether it shares or
  exceeds tazemetostat's hematologic-malignancy signal is an open safety question not resolved
  by the data surfaced here.
- **NCT07303387 eligibility for a CIC-DUX4 patient** — the trial's stated eligibility (SWI/SNF
  complex gene alterations: SMARCB1/A4/A2/C1/C2, ARID1A/1B, PBRM1, BAP1) does not literally list
  CIC or DUX4. Whether CIC-DUX4's PRC2-dependent epigenetic state (PMC10814785) would make a
  case for compassionate consideration is a question for the trial's PI/sponsor, not something
  this search can resolve.
- **ZEN-3694 in sarcoma** — the V3 vector-context table lists it among BETi candidates, but no
  sarcoma trial was found; it may be included in that table on a class-effect basis rather than
  a sarcoma-specific signal. Flagging this as a possible over-inclusion in the upstream vector
  context, for the V3 lead's awareness.
- **Red-team self-challenge results** (per `sarcoma-pre-output-check` Part D):
  - *Load-bearing assumption:* "BETi and CDK4/6i are driver-robust enough to discuss regardless
    of fusion-confirmation status" — if this patient's tumor turns out to be D4 (phenocopy,
    e.g., BCOR-altered), the BETi/CDK4/6i mechanistic rationale (CIC-DUX4-specific
    super-enhancer/CCND1 program) would not directly apply, though BCOR-altered tumors have
    their *own* super-enhancer/CCND-driven biology (per the driver-uncertainty brief's note
    that "BCOR phenocopy D4 is itself super-enhancer/CCND-driven") — so the 0.5 score for D4
    in the applicability matrix (rather than 0) reflects a real but weaker mechanistic case,
    not the *same* mechanistic case.
  - *Disconfirmation:* The strongest evidence against the overall "clinical track is the
    powerful part of V3" framing (per the V3 vector-context table) is precisely the
    tazemetostat withdrawal — the single most clinically-actionable entry in this entire
    output as of the prior protocol version has just been removed from the table entirely.
    This is not a reason to soften the framing (BETi/CDK4/6i remain real clinical options) but
    it is a reason to flag that **the "clinical track" is more fragile/perishable than its
    "Established" framing in the vector-context table implies** — a second major drug in this
    same table could change status at any time, which is exactly why the contract mandates
    live verification every session.
  - *Alternative:* The EWSR1::FLI1 chemically-induced-proximity work (Forward Hypothesis 1) is
    a genuinely different mechanism class (proximity/rewiring vs. inhibition/degradation) that
    doesn't fit neatly into "ASO" or "PROTAC" — it's closer to a third category sometimes
    called "molecular tethers" or CIPs (chemically-induced proximity). I've included it under
    Section 2/Forward Hypothesis 1 rather than forcing a new section, but the V3 lead/
    orchestrator may want to track CIP/molecular-tether technology as its own watch-item across
    future runs, separate from "PROTAC."
  - *Flip test:* If the assumption that "no CIC-DUX4 ASO/PROTAC exists" is wrong (i.e., an
    unpublished program exists that simply didn't surface in search), the core conclusions of
    this output (driver-contingent tagging, the EZH2i withdrawal, the BETi/CDK4/6i trial
    landscape) are unaffected — they stand independently.
  - *Steer audit:* The prompt's framing ("if a CIC-DUX4-specific construct does not exist, say
    so plainly") was a constraint to test against, not a conclusion to confirm — the searches
    were run as genuine negative-finding searches (multiple phrasings, multiple source types)
    before concluding absence, consistent with that constraint rather than just asserting it.

---

## Bibliography / Sources (with access dates)

- Ipsen press release, "Ipsen voluntarily withdraws Tazverik® (tazemetostat) in follicular
  lymphoma and epithelioid sarcoma," 2026-03-09 (and update press release, same URL family,
  ipsen.com/press-release/...-3251503 and ...-3252192). Accessed 2026-06-14.
- OncLive, "FDA Indications for Tazemetostat in R/R Follicular Lymphoma and Epithelioid
  Sarcoma Are Voluntarily Withdrawn." Accessed 2026-06-14.
- CancerNetwork, "Tazemetostat Withdrawn From Follicular Lymphoma, Sarcoma Markets." Accessed
  2026-06-14.
- Cancer Therapy Advisor / Oncology Nurse Advisor / oncologynewscentral.com, withdrawal
  coverage, March 2026. Accessed 2026-06-14.
- everyone.org, "Tazemetostat's EMA approval: What if waiting is no option?" (pre-withdrawal
  EU access-program context). Accessed 2026-06-14.
- ClinicalTrials.gov NCT02601950 (tazemetostat soft tissue sarcoma basket study, incl.
  epithelioid sarcoma and synovial sarcoma SS18-SSX cohorts).
- ClinicalTrials.gov NCT04917042 (tazemetostat in MPNST, phase 2, University of Florida).
- ClinicalTrials.gov NCT07303387 (valemetostat in SWI/SNF-altered solid tumors).
- ASCO 2025 abstract JCO.2025.43.16_suppl.10003 (valemetostat pediatric phase 1, NCCH1904).
- ClinicalTrials.gov NCT02419417 and PMC9454848 / PMID 36077617 (BMS-986158 phase 1/2a,
  advanced solid tumors).
- ClinicalTrials.gov NCT03936465 (BMS-986158 pediatric phase 1, incl. Ewing sarcoma).
- AACR Molecular Cancer Therapeutics 2023, "First-in-human Study of AZD5153" (bivalent BRD4
  inhibitor, NCT for AZD5153 phase 1).
- ClinicalTrials.gov NCT02296476 (OTX015/birabresib/MK-8628, recurrent GBM).
- PMC10598203 / *Signal Transduction and Targeted Therapy* 2023 (palbociclib phase 2 in
  CDK4-overexpressing sarcoma, GEIS, EudraCT 2016-004039-19).
- ASCOPubs JCO Precision Oncology, "Clinical Utility of CDK4/6 Inhibitors in Sarcoma:
  Successes and Future Challenges" (PO.21.00211) — abemaciclib in dedifferentiated
  liposarcoma.
- PMC10814785, "CIC-DUX4 Chromatin Profiling Reveals New Epigenetic Dependencies and
  Actionable Therapeutic Targets in CIC-Rearranged Sarcomas" — basis for BRD4/PRC2
  mechanistic relevance claims.
- PMC8511258, "Inactivation of the CIC-DUX4 oncogene through P300/CBP inhibition, a
  therapeutic approach for CIC-DUX4 sarcoma" — dCBP-1, direct CIC-DUX4 cell-line evidence.
- bioRxiv 10.1101/2025.04.24.650501, "Specific degrader for fusion oncokinase kills tumors
  and is augmented by bimodal degrader-siRNA" (DNAJB1::PRKACA, fibrolamellar carcinoma —
  preprint, not peer-reviewed at access date).
- bioRxiv 10.1101/2025.03.14.643353 / *JACS* 2025 PMC12851799 / PMID 41307210, "Rewiring the
  Fusion Oncoprotein EWSR1::FLI1 in Ewing Sarcoma with Bivalent Small Molecules."
- PMC6814818, "PROTAC induced-BET protein degradation exhibits potent anti-osteosarcoma
  activity by triggering apoptosis" (ARV-771 in osteosarcoma, preclinical).
- PMID 27274050 (PNAS 2016), ARV-771 in prostate cancer (original PROTAC characterization).
- PMC11729552, ROR1-targeting antibody-PROTAC conjugate (BRD4 degrader payload), 2024-2025.
- PMID 31597037 (*NEJM* 2019), milasen — N-of-1 custom ASO precedent (Batten disease).
- `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`
  (ADR-0008) — driver-hypothesis space, applicability matrix, EVSI ranking.

*Research simulation / hypothesis generation only. Not medical advice. No dosing, start/stop,
or treatment recommendations are made or implied.*
