# V4 Checkpoint/T-cell Specialist — T-cell Surveillance Report

**Summary:** Maps PD-1/PD-L1/CTLA-4 checkpoint biology, clinical CPI trial evidence in sarcoma, epigenetic priming combinations, and dietary modulation of the PD-L1 axis in the context of CIC-rearranged sarcoma; covers the V3→V4 bridge (MHC-I restoration as prerequisite for T-cell killing) and applies the case-specific flags (fusion-unconfirmed subgroup, post-whole-lung irradiation, imminent high-dose ifosfamide, abscopal context).

**Confidence: medium** — Checkpoint inhibitor mechanisms and sarcoma trial data are well-characterised at the class level; evidence specific to CIC-rearranged sarcoma is absent (disease too rare for dedicated CPI trials); extrapolation from UPS/DDLPS sarcoma CPI data is mechanistically plausible but not validated. Dietary modulation of PD-L1 in patients is essentially unestablished.

---

## PATIENT CONTEXT INTEGRATION

This patient has completed 14 cycles VDC/IE, surgery (>95% necrosis), radiation to leg and whole-lung irradiation (WLI), achieved NED, and now presents with oligometastatic relapse (one lung lesion) prior to high-dose ifosfamide. Specific flags for this specialist:

1. **WLI abscopal context:** WLI can prime pulmonary immune microenvironment via radiation-induced immunogenic cell death (ICD), HMGB1/DAMP release, STING pathway activation, and MHC-I upregulation on surviving cells. The patient's one relapsing lung lesion is in the context of previously irradiated lung parenchyma, which may have altered the local T-cell and macrophage milieu. This is potentially relevant for checkpoint therapy sequencing.

2. **Post-ifosfamide immune reconstitution window:** High-dose ifosfamide produces profound lymphodepletion. The post-ifosfamide reconstitution window (weeks 4-12 post-completion) has been explored in other hematological and solid tumour contexts as a period of lymphocyte proliferation and enhanced responsiveness to immunotherapy (analogous to post-lymphodepletion CAR-T windows). No published data specific to CIC-rearranged sarcoma or high-dose ifosfamide + checkpoint inhibitor sequencing exist; this is a Forward Hypothesis entry.

3. **mRNA team findings incorporated:** BNT162b2 does not produce persistent checkpoint pathway (PD-1/PD-L1) alteration at this timepoint (>2 years post-vaccination). No adjustment to V4 checkpoint logic required from vaccine history.

---

## PD-1 / PD-L1 / CTLA-4 BIOLOGY

### PD-1/PD-L1 Axis

- **PD-1 (PDCD1):** Inhibitory receptor expressed on activated and exhausted CD8+ T-cells. Ligand binding (PD-L1/CD274 or PD-L2/PDCD1LG2) delivers an inhibitory signal suppressing T-cell proliferation, cytokine production (IFN-γ, TNF-α), and cytotoxic killing. [Mechanism: Established from multiple solid tumour reviews; no direct CIC-DUX4 data]
- **PD-L1 (CD274):** Expressed on tumour cells and tumour-infiltrating myeloid cells in response to IFN-γ (JAK-STAT pathway), EGF signalling, and BRD4-driven super-enhancer activity at the CD274 locus. CIC-DUX4 tumours: PD-L1 expression reported in some CIC-rearranged sarcoma series (Italiano et al. 2018 Cancer — verify PubMed; majority of series report PD-L1 expression in a minority of cases). Evidence tier: Clinical observational (small case series; no direct PD-L1 IHC dataset specific to CIC-DUX4 with large n).
- **CTLA-4 (CD152):** Expressed on activated T-cells and Tregs. Competes with CD28 for B7 ligands on APCs, delivering net inhibitory signal to T-cell priming. Anti-CTLA-4 (ipilimumab) is FDA-approved for melanoma, RCC, NSCLC, and others; not approved for sarcoma. Mechanistic rationale in sarcoma: Treg depletion in TME + enhanced T-cell priming.

### Key Evasion Mechanism Relevant to CIC-DUX4

CIC-DUX4 tumours evade T-cell killing via two parallel mechanisms:
1. **MHC-I downregulation** (via PRC2/H3K27me3 silencing of HLA, TAP1, TAP2, B2M, NLRC5) — documented mechanism; whether quantitatively confirmed in CIC-DUX4-specific tissue is unestablished (see V3 summary).
2. **PD-L1 upregulation** — BRD4 super-enhancer at CD274 locus drives PD-L1 expression; IFN-γ from infiltrating lymphocytes amplifies this signal adaptively.

These two mechanisms create a "double shield": T-cells cannot see the cell (MHC-I-low), and if they do encounter it, the kill signal is suppressed (PD-L1 high). This is the mechanistic basis for the V3→V4 epigenetic priming strategy.

---

## CLINICAL CPI EVIDENCE IN SARCOMA

### SARC028 (NCT02301039) — Pembrolizumab in Advanced Sarcoma

- Phase II single-arm study; 80 patients (4 cohorts: UPS, DDLPS, synovial, osteosarcoma).
- ORR: UPS 18% (4/22), DDLPS 10% (2/20), synovial 5%, osteosarcoma 5%.
- **CIC-rearranged sarcoma: not enrolled as a distinct cohort — too rare.** No CIC-DUX4-specific pembrolizumab data exist.
- Evidence tier: **Clinical-Trial** (Tawbi et al., Lancet Oncology 2017, PMID 28988796). Transfer to CIC-DUX4: mechanistically plausible, evidence indirect.

### Alliance A091401 (NCT02978625) — Nivolumab ± Ipilimumab in Sarcoma

- Randomised phase II; nivolumab alone vs nivolumab + ipilimumab.
- Combination arm showed higher ORR (16% vs 5%) and PFS benefit in specific subtypes.
- UPS benefited most; CIC-rearranged not analysed separately.
- Evidence tier: **Clinical-Trial** (D'Angelo et al., NEJM 2018, PMID 30501812).

### Sarcoma CPI Reality Check (mandatory flag)

Sarcoma checkpoint monotherapy responses are modest overall. The highest-responding subtypes are UPS, DDLPS, and pleomorphic sarcomas — histotypes with high mutational burden or complex genomics. CIC-rearranged sarcoma is a genomically simple translocation-driven tumour with typically low TMB. Low TMB predicts poor checkpoint response in most tumour types. Do not overstate the checkpoint monotherapy probability of response in CIC-rearranged sarcoma.

### Combinations with Epigenetic Priming (V3→V4 Bridge — HIGH PRIORITY)

The mechanistically strongest approach for CIC-rearranged sarcoma immunotherapy is NOT checkpoint monotherapy but rather:

**EZH2i → MHC-I restoration → anti-PD-1/PD-L1**

- EZH2i (tazemetostat) restores MHC-I expression (see V3 MHC-I section).
- Tazemetostat + pembrolizumab: NCT04196738 (KEYNOTE-B97) — verify current status; this combination is being explored in epigenetically driven tumours. Evidence tier: **Clinical-Trial**.
- HDACi (entinostat) + pembrolizumab: NCT02890069 — sarcoma cohort; entinostat restores MHC-I + de-represses immune checkpoints on tumour cells. Evidence tier: **Clinical-Trial**.
- DNMTi (azacitidine) + checkpoint: QUILT-3.032 and related studies — viral mimicry via ERV demethylation → STING → IFN → MHC-I. Evidence tier: **Clinical-Trial**.

**V3 priming is a required prerequisite for checkpoint efficacy in MHC-I-low CIC-DUX4 tumours. Checkpoint alone is unlikely to produce T-cell killing when the target is invisible.**

### Radiation-Immune Priming (Abscopal Context)

Prior WLI in this patient constitutes radiation-mediated immune priming:
- Radiation induces ICD → HMGB1, calreticulin exposure → DC activation.
- STING pathway activation via cytosolic dsDNA release from irradiated cells → type I IFN → CD8+ T-cell priming.
- The abscopal effect (regression of non-irradiated lesions after local radiation) is rare but mechanistically attributable to this immune cascade.
- The patient's single relapsing lung lesion is in a previously irradiated field; whether this represents local radioresistant clone or new seeding is uncertain. The radiation-primed immune context could be exploited by checkpoint blockade administered post-ifosfamide reconstitution.
- Evidence tier: **Mechanistic** (radiation-immune priming is established; its exploitation in this specific CIC-rearranged patient with oligometastatic lung relapse post-WLI is Forward Hypothesis territory). No sarcoma-specific abscopal + CPI data in CIC-DUX4.

---

## DIETARY TRACK
### PD-L1 Modulation via Diet (honest assessment)

| Compound | Claimed mechanism | Evidence tier | Critical caveat | Patient's regimen? |
|---|---|---|---|---|
| Curcumin | Inhibits NF-κB → reduces PD-L1 transcription at 10-30 µM in cell lines | Preclinical-Cell | Plasma concentrations from dietary turmeric are ~100-fold below active range. No patient-level PD-L1 modulation data. This is cell-line biology, not clinical effect. | Yes (curcumin + piperine supplement) |
| Sulforaphane (broccoli) | Nrf2-mediated effects on PD-L1; weak HDACi | Preclinical-Cell | Juicing inactivates myrosinase; minimal sulforaphane from broccoli juice. Dietary effect on PD-L1: not established in patients. | Yes (broccoli juice) |
| Omega-3 EPA/DHA | Reduces PD-L1 expression in some tumour cell lines via lipid raft modulation | Preclinical-Cell | Mechanistic only at dietary doses. Patient does NOT have omega-3 in regimen — note absence. | No — absent from regimen |
| EGCG | DNMT inhibition → possible PD-L1 demethylation | Mechanistic | Not in patient's regimen; dietary plasma levels subclinical for mechanism. | No |

**Overall dietary PD-L1 modulation assessment:** No dietary compound has demonstrated clinically meaningful PD-L1 downregulation in sarcoma patients or in any patient cohort at culinary intake levels. Do not treat curcumin or sulforaphane as checkpoint modulators at dietary doses. Their mechanisms are cell-line observations only.

### Patient Regimen Items — Checkpoint-Relevant Assessment

| Item | V4/checkpoint relevance | Chemo interaction (ifosfamide context) |
|---|---|---|
| Curcumin + piperine | Cell-line NF-κB/PD-L1 data; dietary dose insufficient. No clinical checkpoint effect established. | CYP3A4 inhibition at supplement doses: possible ↑ ifosfamide or concurrent drug AUC. At dietary turmeric in food: subclinical. Discuss curcumin supplements with oncologist during ifosfamide. |
| Liposomal vitamin C | No established checkpoint mechanism. Prooxidant at high IV doses; oral/liposomal form intermediate. | High-dose vitamin C: ROS-axis concern with ifosfamide. Liposomal oral form at moderate doses: risk considered lower but not zero. Discuss with oncologist. |
| Black cumin seed oil (thymoquinone) | No checkpoint mechanism established. Anti-inflammatory via NF-κB at cell-line doses only. | CYP3A4/CYP2C9 inhibitor preclinically (Ahmed et al. 2017, Saudi Pharm J); could reduce ifosfamide activation. FLAG: discuss with oncologist. |
| Vitamin D3 | NK cell function (see NK specialist); indirect T-cell priming support via VDR in dendritic cells. | No documented interaction with ifosfamide at standard supplemental dose. Hypercalcemia monitoring required. |
| Fresh juices (celery, ginger, carrot, broccoli, apple, beetroot) | Contain polyphenols at subclinical doses after juicing. No checkpoint mechanism at these intake levels. | Ginger (6-gingerol): P-gp modulation at very high doses, not juice-level. At culinary intake: low concern. Carrot/beetroot: no known CYP/P-gp interaction at juice intake. |
| Honey | No checkpoint mechanism. Trace anti-inflammatory polyphenols at culinary intake. | No known interaction with ifosfamide at culinary intake. |

---

## CHEMO INTERACTION SCREENING (ifosfamide context)

Curcumin: CYP3A4: inhibitor at supplement doses (Chen et al., Drug Metab Dispos 2007, PMID 17065205); potential ↑ ifosfamide AUC or vincristine AUC | P-gp: inhibitor (Anuchapreeda et al., Biochem Pharmacol 2002, PMID 12126956); ↑ etoposide CNS exposure | ROS-axis: Nrf2 activation at high doses may attenuate ifosfamide oxidative mechanism | Other: hepatic load at supplement doses | Sources: DrugBank DB11672, PMID 17065205, 12126956.

Black cumin seed oil (thymoquinone): CYP3A4: inhibitor (preclinical — Ahmed et al. 2017 Saudi Pharm J); CYP2C9: inhibitor (same source) | P-gp: not well-characterised | ROS-axis: Nrf2 activation theoretical | Sources: Ahmed et al. 2017, DrugBank (limited data).

Liposomal vitamin C (high-dose): ROS-axis: prooxidant at IV doses; liposomal oral intermediate risk | CYP: no major CYP interaction at dietary doses | Source: none found for specific ifosfamide interaction; general concern based on mechanism.

Omega-3 (absent from regimen): If added — anti-platelet effect (high-dose fish oil); P-gp modulation (minor) | Sources: NCCN Integrative Medicine guidelines note caution with surgery/chemo.

---

## FORWARD HYPOTHESES

**[Forward Hypothesis 1] Post-ifosfamide lymphodepletion → immune reconstitution window as optimal timing for checkpoint blockade in oligometastatic CIC-rearranged sarcoma.**

Hypothesis: High-dose ifosfamide produces profound lymphodepletion, after which the reconstituting lymphocyte compartment is transiently enriched for naive and central memory T-cells with higher proliferative potential. This reconstitution window (weeks 4-8 post-completion) may represent optimal timing for checkpoint blockade (pembrolizumab or nivolumab), analogous to the post-lymphodepletion window exploited in CAR-T therapy and post-cytoreductive chemotherapy CPI strategies. In the context of this patient's single residual lung lesion, the combination of ifosfamide-mediated cytoreduction + post-lymphodepletion CPI could produce durable control.

Mechanistic basis: Lymphodepletion eliminates peripheral Tregs and exhausted T-cells; IL-7/IL-15-driven homeostatic proliferation of reconstituting T-cells enhances de novo antigen-specific priming. In the presence of tumour-associated neoantigens (even without confirmed junction sequence, somatic neoantigens from WES may be presentable if MHC-I is restored by concurrent epigenetic priming), checkpoint blockade during reconstitution could amplify tumour-reactive T-cell expansion.

Study design: Phase Ib window-of-opportunity design: high-dose ifosfamide → Day 28-35 initiation of pembrolizumab (or nivolumab + ipilimumab) in platinum/alkylator-responsive oligometastatic sarcoma. Primary endpoint: T-cell reconstitution kinetics (flow cytometry, TCR repertoire diversity), tumour response at 12 weeks. Why not done: The sequencing hypothesis is novel; ifosfamide as a lymphodepleting platform for subsequent CPI has not been formally tested in sarcoma clinical trials.

**[Forward Hypothesis 2] Radiation-primed STING activation from prior WLI as an exploitable immune context for checkpoint + EZH2i triplet in this patient's lung relapse.**

Hypothesis: Prior WLI has established a radiation-primed pulmonary immune microenvironment (STING-active, IFN-γ-elevated, DC-matured) in this patient's lungs. The single relapsing lung lesion is in this primed context. EZH2i (tazemetostat, to restore MHC-I) + anti-PD-1 (pembrolizumab) administered after ifosfamide could exploit this pre-primed immune context — the radiation has done the innate immune priming work; EZH2i restores tumour visibility; anti-PD-1 removes the terminal brake. This triplet (radiation-primed context + epigenetic priming + checkpoint) has not been formally tested in any sarcoma subtype.

Mechanistic basis: Radiation-induced STING activation documented in lung tissue post-thoracic RT (Deng et al., Immunity 2014, PMID 25517614 — non-CIC-DUX4 context); EZH2i MHC-I mechanism from V3; anti-PD-1 mechanism above.

Study design: Retrospective analysis of prior-thoracic-RT sarcoma patients who received subsequent checkpoint therapy — does prior thoracic RT predict higher CPI response? Prospective arm: post-high-dose-ifosfamide window, patients with prior WLI, tazemetostat 800mg BID + pembrolizumab 200mg q3w. Primary endpoint: ORR at 16 weeks. Biomarker: STING pathway markers in serial circulating cell-free DNA and tumour biopsies.

---

## ATYPICAL-CASE NOTES

This patient is fusion-UNCONFIRMED (~5% subgroup).

FUSION-AGNOSTIC entries (applicable to this patient):
- All checkpoint inhibitor approaches (pembrolizumab, nivolumab, ipilimumab): target PD-1/PD-L1/CTLA-4, not the fusion protein. Apply regardless of fusion status.
- EZH2i + checkpoint combinations: target PRC2-dependent epigenetic silencing, which is fusion-agnostic.
- HDACi + checkpoint: same reasoning.
- Radiation-immune priming context: fusion-agnostic.

FUSION-CONFIRMED ONLY (not applicable to this patient):
- Junction-specific neoantigen vaccine as a neoantigen source for T-cell priming: requires confirmed junction sequence. See Neoantigen Vaccine Specialist file.

---

## WHAT I COULD NOT ESTABLISH

1. CIC-DUX4-specific PD-L1 IHC expression data in a large series. Small series suggest variable expression; no dedicated systematic study identified.

2. CIC-DUX4-specific T-cell infiltration (TIL) density and phenotype. Whether these tumours are immunologically "hot," "excluded," or "cold" is not established from published data.

3. Whether prior WLI in this patient has durably altered the pulmonary immune microenvironment at the current timepoint (>1 year post-WLI). STING activation from radiation is documented acutely; whether it persists to generate a permissive CPI context at >12 months post-WLI is unknown.

4. Whether high-dose ifosfamide as a lymphodepleting platform prior to CPI produces any immunological benefit in the sarcoma context. No published prospective data.

5. Dietary modulation of PD-L1 in any patient at culinary intake levels. No published clinical data.

6. TMB of this patient's tumour. CIC-rearranged sarcomas are typically TMB-low; without WES data on this specific tumour we cannot confirm this.
