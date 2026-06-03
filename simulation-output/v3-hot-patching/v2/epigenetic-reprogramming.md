# V3 Epigenetic Therapy Specialist Output (v2)

**Summary:** Covers clinical HDACi, EZH2/EED inhibitors, DNMTi, and BETi interventions targeting epigenetic reprogramming in CIC-rearranged sarcoma; dietary epigenetic modulators assessed with explicit concentration mismatch caveat. Excludes surgical, radiation, and direct cytotoxic approaches. TAZEMETOSTAT WITHDRAWN 2026-03-09 — EZH2i mechanism rerouted to valemetostat and MAK683.

**Confidence:** Medium — Epigenetic mechanisms are well-characterised in related fusion sarcomas; direct CIC-DUX4 data sparse; all EZH2i rationale extrapolates from SMARCB1-null and BAF-disrupted sarcomas.

**Not medical advice. For oncologist discussion only.**

---

## MHC-I UPREGULATION CANDIDATES
### (Mandatory Top Section — V3→V4 Bridge)

See v3-summary-v2.md MHC-I section for complete table. Summary for this specialist:

- **Valemetostat (dual EZH1/2i):** Primary EZH2-pathway bridge. H3K27me3 reduction at APM loci. Clinical-Trial. F3. FUSION-AGNOSTIC.
- **MAK683 (EED allosteric inhibitor):** Alternative PRC2 inhibitor via EED binding. Clinical-Trial. F3. FUSION-AGNOSTIC.
- **Entinostat (class I HDACi):** HDAC1/2/3 inhibition → NLRC5 upregulation → APM de-repression. Clinical-Trial. F3. FUSION-AGNOSTIC.
- **Vorinostat (pan-HDACi):** Broader HDACi; approved CTCL/MM; toxicity concern with ifosfamide. Established (CTCL/MM) / Clinical-Trial (sarcoma). F2/F3. FUSION-AGNOSTIC.
- **Azacitidine / Decitabine (DNMTi):** ERV demethylation → cGAS-STING → type I IFN → MHC-I. Established (MDS/AML) / Clinical-Trial (solid tumors). F2/F3. FUSION-AGNOSTIC.
- **~~Tazemetostat~~:** WITHDRAWN 2026-03-09. DO NOT CITE AS ACCESSIBLE. Mechanism valid; agent unavailable.

---

## CLINICAL EPIGENETIC AGENTS

### EZH2/PRC2 Inhibitors

**Valemetostat (DS-3201b)** — Tier: Clinical-Trial — Confidence: Moderate — Feasibility: F3
- Mechanism: Allosteric inhibition of both EZH1 and EZH2 → prevents H3K27 trimethylation. Dual inhibition is significant: EZH2-only inhibitors (like tazemetostat) can trigger compensatory EZH1 upregulation in some tumors; valemetostat blocks both paralogs simultaneously. H3K27me3 reduction → de-represses CDKN2A, CDKN1A, tumor suppressor, and APM gene loci.
- Evidence in CIC-DUX4: None direct. Extrapolated from: (1) SMARCB1-deficient sarcoma PRC2 dependency (epithelioid sarcoma Phase I data); (2) CDKN2A co-deletion in CIC-rearranged sarcoma (suggestive of H3K27me3-mediated silencing); (3) general ETS-driven fusion sarcoma epigenetic amplification logic.
- Regulatory status (verified 2026-06-03): PMDA-approved Japan for relapsed/refractory adult T-cell leukaemia/lymphoma. No FDA or EMA marketing authorisation for any solid tumor indication. In Phase I/II trials for solid tumors including SMARCB1-deficient sarcomas (NCT07303387, jRCT2031190268).
- SOC interaction: Valemetostat CYP3A4 interaction status: [VERIFY at prescribing information / DrugBank before concurrent use with vincristine/ifosfamide]. Myelosuppression additive risk: flag for sequential scheduling post-ifosfamide.
- Atypical-case tag: FUSION-AGNOSTIC

**MAK683** — Tier: Clinical-Trial — Confidence: Moderate — Feasibility: F3
- Mechanism: Binds EED aromatic cage → prevents EED from reading and propagating the H3K27me3 mark → allosteric PRC2 complex inhibition. Binding site is distinct from the EZH2 catalytic domain: MAK683 retains activity in tumors with EZH2 gain-of-function mutations (which reduce EZH2i binding) and potentially in EZH2i-resistant tumors. H3K27me3 reduction confirmed pharmacodynamically in tumor biopsies and PBMCs from Phase I patients.
- Evidence in CIC-DUX4: None direct. Phase I/II (NCT02900651) enrolled patients with advanced malignancies including epithelioid sarcoma; clinical activity in ES (related SMARCB1-null sarcoma) confirmed. Publication: PMID 39793445 (Eur J Cancer, 2025 — first-in-human dose-escalation results).
- Regulatory status: Not approved. Phase I/II completed dose-escalation. No sarcoma-specific cohort; available via trial or compassionate use.
- SOC interaction: [VERIFY CYP interaction profile for MAK683 before combining with ifosfamide/vincristine].
- Atypical-case tag: FUSION-AGNOSTIC

### HDAC Inhibitors

**Entinostat** — Tier: Clinical-Trial — Confidence: Moderate — Feasibility: F3
- Mechanism: Selective class I HDAC inhibitor (HDAC1, HDAC2, HDAC3). Inhibition → histone H3 lysine 9 and H4 lysine 12 hyperacetylation at target gene promoters → de-represses NLRC5 (master transactivator of MHC-I pathway: activates HLA-A, HLA-B, HLA-C, TAP1, TAP2, B2M) → antigen presentation machinery restoration. Also de-represses CDKN1A/p21 and CDKN1B/p27 → partial G1 arrest in tumor cells.
- Evidence in CIC-DUX4: None direct. Ewing sarcoma entinostat data: Sankar et al. 2014 PMID 24531741 (EZH2i+HDACi in Ewing). Rhabdomyosarcoma entinostat in vitro: PMC11327338. Pediatric solid tumor Phase I (ADVL1513): PMC9176707.
- Regulatory status: Not approved for sarcoma. In clinical trials: NCT02890069 (entinostat + pembrolizumab, sarcoma-relevant); NCT03250273 (entinostat + nivolumab, cholangiocarcinoma/pancreatic, completed). FDA approval: entinostat has received FDA Breakthrough Therapy Designation for breast cancer in combination; not approved as of knowledge cutoff. [VERIFY current FDA status].
- SOC interaction: Entinostat class I HDACi — generally better tolerated than pan-HDACi; lower cardiotoxicity. No documented direct CYP3A4 major inhibition at clinical doses. Myelosuppression additive: use post-ifosfamide, not concurrent.
- Atypical-case tag: FUSION-AGNOSTIC

**Vorinostat (SAHA)** — Tier: Established (CTCL FDA/EMA); Clinical-Trial (sarcoma) — Confidence: Moderate (X=− for ifosfamide context) — Feasibility: F2/F3
- Mechanism: Pan-HDAC inhibitor (HDAC1/2/3/6/8). Histone hyperacetylation + α-tubulin hyperacetylation (HDAC6) → broad de-repression including APM genes, heat-shock chaperone upregulation. MHC-I upregulation documented in multiple tumor types. Broader class increases toxicity (GI, hematologic, fatigue) vs. class I-selective entinostat.
- Evidence in CIC-DUX4: None direct.
- Regulatory status: FDA 2006 (Zolinza, CTCL); EMA (Zolinza, CTCL). Not approved for sarcoma by either authority. Available as approved drug; off-label sarcoma use requires clinical trial or compassionate framework.
- SOC interaction: Higher hematologic toxicity than entinostat — concurrent use with high-dose ifosfamide not advisable. Sequence after ifosfamide course completion.
- Atypical-case tag: FUSION-AGNOSTIC

**Panobinostat** — Tier: Established (MM FDA/EMA); Clinical-Trial (sarcoma) — Confidence: Low (X=− [significant toxicity profile]) — Feasibility: F2/F3
- Mechanism: Pan-HDAC inhibitor (HDAC1/2/3/4/5/6/7/8/9/10/11). Broader than vorinostat; significant cardiac (QTc) and hematologic toxicity limits sarcoma use.
- Evidence in CIC-DUX4: None direct.
- Regulatory status: FDA 2015 (Farydak, multiple myeloma); EMA 2015 (Farydak, MM). Not approved for sarcoma.
- Note: Less preferred than entinostat for V3→V4 bridge due to toxicity profile. Included for completeness.
- Atypical-case tag: FUSION-AGNOSTIC

### DNA Methyltransferase Inhibitors

**Azacitidine / Decitabine** — Tier: Established (MDS/AML); Clinical-Trial (solid tumors) — Confidence: Moderate — Feasibility: F2 (approved, accessible) / F3 (solid tumor off-label)
- Mechanism: DNMT1 incorporation during DNA replication → DNMT1 trapping/degradation → progressive CpG demethylation over cell divisions. Two MHC-I upregulation paths: (1) Direct: CpG demethylation at methylated HLA-A/B/C and TAP1/2 gene promoters → transcription factor access restored; (2) Indirect: Endogenous retroviral element (ERV) demethylation → cytosolic dsRNA → cGAS-STING activation → IRF3 → type I IFN secretion → JAK1/TYK2 → STAT1/2 → ISG15, IRF1, HLA genes [Chiappinelli et al. 2015 Cell PMID 26317466; Roulois et al. 2015 Cell PMID 26317465]. This viral-mimicry path is distinct from EZH2i/HDACi and can act synergistically.
- Evidence in CIC-DUX4: None direct. Evidence from: melanoma (Chiappinelli 2015), colorectal cancer (Roulois 2015), AML. CpG methylation of HLA genes in sarcomas documented but CIC-DUX4-specific quantitative data not available.
- Regulatory status: Azacitidine (Vidaza): FDA 2004 MDS, EMA 2008 MDS. Decitabine (Dacogen): FDA 2006 MDS, EMA 2012 MDS. Neither approved for sarcoma. Note: oral azacitidine (Onureg/CC-486) FDA 2020 AML maintenance; EMA 2021. Cedazuridine/decitabine oral combination (E7727) in Phase I solid tumor trial (NCT03875287).
- SOC interaction: Both agents are myelosuppressive — sequential scheduling post-ifosfamide. At low decitabine doses (epigenetic dosing, not high-dose cytotoxic) the myelosuppression is manageable; still requires oncologist oversight.
- Atypical-case tag: FUSION-AGNOSTIC

### BET Bromodomain Inhibitors (epigenetic mechanism)

**OTX015 / Birabresib; BMS-986158** — Tier: Clinical-Trial — Confidence: Moderate — Feasibility: F3
- Mechanism: Competitive inhibition of BRD4 bromodomains BD1 and BD2 → displacement from acetylated H3K27 at super-enhancers → collapse of super-enhancer-driven transcription at ETS target loci (ETV4, ETV5, MYC, CCND1). Additionally: BRD4 occupancy at CD274 (PD-L1) super-enhancer displaced → PD-L1 downregulation → improved T-cell access (V3→V4 PD-L1 contribution). MHC-I upregulation by BETi is weaker than EZH2i/HDACi — the PD-L1 suppression contribution is stronger.
- Evidence in CIC-DUX4: Yoshimoto 2017 Oncotarget (CIC-DUX4 cell-line BETi sensitivity) — PMID UNVERIFIED THIS SESSION: [VERIFY at PubMed before citing as established]. BETi well-characterised in Ewing sarcoma (same super-enhancer mechanism). BMS-986158 Phase I/IIa published (PMID 36077617).
- Regulatory status: Neither approved. OTX015 and BMS-986158 in Phase I/IIa. Development status uncertain as of 2026. [VERIFY at ClinicalTrials.gov for active recruiting sarcoma cohorts].
- SOC interaction: Thrombocytopenia is primary BETi class adverse effect (43% BMS-986158 Phase I); diarrhea. Concurrent with ifosfamide: myelosuppression additive — post-ifosfamide scheduling preferred.
- Atypical-case tag: FUSION-AGNOSTIC

---

## DIETARY EPIGENETIC MODULATORS

**Critical framing:** All dietary compounds below face a severe concentration mismatch — the concentrations required for epigenetic effects in cell lines are 5–100× above achievable dietary or supplemental plasma concentrations in humans. None of these compounds should be presented as achieving clinical-grade epigenetic reprogramming. They are listed as adjunctive background with honest caveats.

| Compound | Source | Reported Mechanism | Active Concentration (cell-line) | Dietary Plasma Cmax | Mismatch Factor | Tier | Chemo Interaction |
|---|---|---|---|---|---|---|---|
| Sulforaphane | Broccoli sprouts (chop/chew) — juicing destroys myrosinase | HDAC class I inhibition; NRF2/KEAP1-Cys151 adduct at lower doses | 5–30 µM (HDACi); 1–5 µM (NRF2) | ~0.5–1 µM (dietary) | 5–60× (HDACi range); borderline for NRF2 | Preclinical-Cell | Nrf2 at supplement dose: theoretical ROS-axis concern with doxorubicin/ifosfamide. Culinary: subclinical. Supplements during ifosfamide: discuss with oncologist. |
| EGCG | Green tea, matcha (beverage) | Reported EZH2 allosteric inhibition; HDAC modulation | 10–50 µM | ≤0.3 µM | 30–150× | Preclinical-Cell | P-gp inhibition at supplement doses (>400 mg/day): vincristine exposure risk. Beverage: low risk. |
| Quercetin | Capers, raw red onions, apple skin | Very weak EZH2 modulation; primarily V1 | >>10 µM | <0.1–0.5 µM | 20–100× | Preclinical-Cell | CYP3A4 inhibition at supplement doses: vincristine concern. Dietary: low risk. |
| Butyrate | Resistant starch/inulin fermentation | HDAC inhibitor (colonic epithelium, mM range) | 1–5 mM (colonic) | <0.1 mM (peripheral) | 10–50× (peripheral tissue vs. active) | Preclinical | No documented SOC interaction at dietary levels. |
| Curcumin | Turmeric (with piperine) | BRD4-chromatin disruption | 5–20 µM | <<1 µM (even with piperine; Shoba 1998 caveat applies) | >5–20× | Preclinical-Cell | CYP3A4 (curcumin), P-gp (piperine): supplements concern with vincristine. Food-level: subclinical. |

**Summary:** No dietary compound achieves V3-relevant epigenetic reprogramming at concentrations achievable from dietary or conventional supplemental intake in tumor tissue. All dietary entries carry Confidence: Low with A-axis hard-minus.

---

## WHAT I COULD NOT ESTABLISH

1. H3K27me3 ChIP-seq data in CIC-DUX4 cell lines — no published study confirming PRC2 activity at specific loci in this histotype.
2. Valemetostat CYP3A4 interaction at clinical doses — not confirmed from available public sources.
3. BETi (specifically OTX015/BMS-986158) CIC-DUX4 cell-line sensitivity data — PMID unverified.
4. MHC-I surface expression quantification in CIC-DUX4 patient tumors with appropriate comparators.
5. Whether sulforaphane (even from properly prepared sprouts) achieves sub-µM HDAC inhibitory activity in tumor tissue.
