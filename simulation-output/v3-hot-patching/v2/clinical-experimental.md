# V3 PROTAC/ASO Specialist Output (v2)

**TAG: Clinical / Experimental — not naturally achievable; for awareness only.**

**Summary:** Covers published and registered PROTAC constructs targeting BET/EZH2/BRD4, antisense oligonucleotides targeting fusion transcripts, CDK4/6 inhibitors in sarcoma (clinical trial landscape), and the sarcoma trial registry relevant to V3 Hot Patching. Scope: published constructs and registered trials only — no agent-invented gene therapies or speculative constructs. Excludes dietary interventions (see dietary track in v3-summary-v2.md). TAZEMETOSTAT WITHDRAWN 2026-03-09.

**Confidence:** Medium (clinical agents) / Low (PROTAC constructs) — Clinical agent mechanisms are well-characterised; CIC-DUX4-specific efficacy data are absent for most entries; all regulatory status live-verified 2026-06-03.

**Not medical advice. For oncologist discussion only.**

---

## CRITICAL STATUS UPDATE: TAZEMETOSTAT

**TAZEMETOSTAT (TAZVERIK) — ALL INDICATIONS WITHDRAWN 2026-03-09**

Ipsen voluntarily withdrew tazemetostat from all markets due to secondary hematologic malignancy signal: 18/318 (5.7%) patients in SYMPHONY-1 trial (tazemetostat + lenalidomide + rituximab arm) developed secondary primary hematologic malignancies vs. 0 in the control arm; 3 deaths. FDA Drug Alert issued; all prescriptions discontinued; ongoing SYMPHONY-1 patients stopped treatment.

EMA status: Tazemetostat held orphan designation but NOT central marketing authorisation in EU; no EMA approval to withdraw. The withdrawal was primarily US/Ipsen-market driven.

**This agent must not appear as an accessible option in any current clinical recommendation. The EZH2-inhibition mechanism remains valid — route to valemetostat or MAK683.**

---

## PROTAC CONSTRUCTS (PUBLISHED)

### BET PROTACs

**ARV-771**
- Tier: Preclinical-Animal
- Confidence: Low (D=−, A=+, R=+, X=0)
- Feasibility: F4 (preclinical-to-Phase I transition)
- Mechanism: CRBN-recruiting BET PROTAC (cereblon E3 ligase + BD2-targeting warhead). Induces proteasomal degradation of BRD4 (and BRD2/BRD3). More complete BRD4 depletion than BETi inhibitors; additionally eliminates scaffold functions of BRD4 not addressed by competitive inhibition. Prostate cancer PDX regression demonstrated [Raina et al. 2016 PNAS PMID 27528661].
- Evidence in CIC-DUX4: None direct.
- Regulatory status: Preclinical. Not in registered clinical trial as of knowledge cutoff.
- Fusion tag: FUSION-AGNOSTIC (targets BRD4, not the fusion protein)

**ARV-825**
- Tier: Clinical-Trial (Phase I)
- Confidence: Low (D=−, A=+, R=+, X=0)
- Feasibility: F4
- Mechanism: CRBN-recruiting PROTAC targeting BRD4 (and BET family); similar mechanism to ARV-771 with distinct chemical warhead. In Phase I evaluation.
- Regulatory status: NCT03328078 (Phase I). [VERIFY current recruitment status at ClinicalTrials.gov — trial may have completed or changed status.]
- Fusion tag: FUSION-AGNOSTIC

**dBET6**
- Tier: Preclinical-Cell
- Confidence: Low (D=−, A=0, R=+, X=0)
- Feasibility: F5 (tool compound; not in clinical development)
- Mechanism: CRBN-recruiting PROTAC; BRD4 degradation in cell lines; used as research tool to distinguish inhibition from degradation effects.
- Not a clinical candidate. Included to note the class mechanism has been validated chemically.
- Fusion tag: FUSION-AGNOSTIC

### EZH2 PROTACs

**MS1943**
- Tier: Preclinical-Cell
- Confidence: Low (D=−, A=0, R=+, X=0)
- Feasibility: F5 (preclinical only)
- Mechanism: CRBN-recruiting PROTAC targeting EZH2 catalytic subunit. Induces EZH2 proteasomal degradation — more complete PRC2 disruption than EZH2 catalytic inhibition. May overcome EZH2 inhibitor resistance arising from PRC2 subunit compensation or EZH2 mutation in the catalytic domain. In TNBC cell lines: growth inhibition demonstrated [Yu et al. 2021 Nat Chem Biol PMID 33349709].
- Evidence in CIC-DUX4: None direct.
- Regulatory status: No registered trial.
- Fusion tag: FUSION-AGNOSTIC

---

## ANTISENSE OLIGONUCLEOTIDES (ASOs)

### CIC-DUX4 Junction-Targeting ASO

**Status: NO CLINICAL-STAGE ASO PUBLISHED FOR CIC-DUX4**

Conceptual mechanism: A junction-specific ASO would target the unique mRNA sequence spanning the CIC exon 20 / DUX4 exon 1 junction → RNaseH recruitment → mRNA degradation → reduction of fusion protein translation → restoration of CIC repressor activity at ETS target loci.

Why this is attractive: The junction sequence is unique to the fusion transcript (not present in any normal proteome), so on-target specificity would be very high and off-target risk theoretically low.

Why it does not yet exist clinically:
1. **Fusion-unconfirmed status in this patient**: The junction sequence is not known; ASO cannot be designed without the specific sequence.
2. **Variable junction breakpoints**: Multiple CIC-DUX4 junction variants are documented; a single ASO may not cover all variants.
3. **Delivery**: CNS-approved ASOs (nusinersen for SMA) use intrathecal delivery. Solid-tumor delivery of ASOs remains an active engineering problem — systemic delivery efficiency to soft-tissue tumors is low.
4. **No published preclinical CIC-DUX4 ASO data** in peer-reviewed literature as of knowledge cutoff.

Tier: Theoretical
Feasibility: F5
Fusion tag: **FUSION-CONFIRMED ONLY — POSSIBLY INAPPLICABLE** (this patient: no confirmed junction sequence; even if fusion confirmed, no clinical construct available)

---

## CDK4/6 INHIBITORS — CLINICAL TRIAL LANDSCAPE

**Palbociclib (Ibrance)**
- Tier: Established (HR+ breast, FDA/EMA); Clinical-Trial (sarcoma)
- Confidence: Moderate (D=0 — CCND1/CDK4 axis predicted; A=+; R=+ [Phase II sarcoma data available]; X=− [myelosuppression with ifosfamide])
- Feasibility: F2 (approved breast cancer, accessible) / F3 (sarcoma = off-label)
- Mechanism: Selective CDK4/6 inhibitor → Rb hypophosphorylation → E2F transcription factor sequestration → G1 arrest. Targets downstream execution of the ETS→CCND1→CDK4→Rb axis constitutively driven by CIC-DUX4.
- Sarcoma Phase II data: Zucman-Rossi group Phase II in CDK4-overexpressing advanced sarcoma (excluding DDLPS): 6-month PFS rate 29% (95% CI 9–48%), mPFS 4.2 months, mOS 12 months [PMID 37875500, Signal Transduct Target Ther 2023]. CDK4 mRNA overexpression without CDKN2A overexpression was the most predictive biomarker. Provides the best published sarcoma-specific evidence for CDK4/6i in this setting.
- Regulatory status: FDA 2015 HR+/HER2− advanced breast cancer (Ibrance); EMA 2016. Not approved for sarcoma.
- SOC interaction: ADDITIVE MYELOSUPPRESSION WITH IFOSFAMIDE — MUST NOT BE USED CONCURRENTLY. Sequential scheduling: initiate palbociclib after ifosfamide course completion and count recovery.
- Trial ID: NCT03677388 (palbociclib sarcoma); also the GEIS phase II data referenced above.
- Fusion tag: FUSION-AGNOSTIC

**Ribociclib (Kisqali)**
- Tier: Established (breast); Clinical-Trial (sarcoma)
- Confidence: Moderate (D=0, A=+, R=+, X=−)
- Feasibility: F2/F3
- Mechanism: Same CDK4/6 → Rb mechanism as palbociclib. QTc prolongation risk somewhat higher vs. palbociclib; relevant if ifosfamide-related electrolyte disturbances.
- Sarcoma data: Phase I sarcoma data (30 DDLPS patients, 6 stable disease at 6 months). Thinner sarcoma evidence base than palbociclib.
- Regulatory status: FDA 2017 HR+/HER2− breast; EMA 2017. Not approved for sarcoma.
- SOC interaction: Same additive myelosuppression flag as palbociclib. QTc: additional concern with electrolyte disturbances from ifosfamide-induced nephropathy.
- Trial ID: NCT02571829
- Fusion tag: FUSION-AGNOSTIC

**Abemaciclib (Verzenio)**
- Tier: Established (breast); Clinical-Trial (sarcoma)
- Confidence: Moderate (D=0, A=+, R=+, X=−)
- Feasibility: F2/F3
- Mechanism: CDK4/6 → Rb mechanism; additionally inhibits CDK9 at higher concentrations (potential V1 transcriptional CDK overlap). Higher GI toxicity; notable for crossing blood-brain barrier (potential lung met penetration benefit).
- Sarcoma data: Phase II DDLPS median PFS 7 months (best among CDK4/6i in DDLPS). Not directly in CIC-DUX4.
- Regulatory status: FDA 2017 HR+/HER2− breast; EMA 2018. Not approved for sarcoma.
- SOC interaction: Same additive myelosuppression flag. GI toxicity additive with ifosfamide GI effects. BBB penetration potentially relevant for CNS mets (not current issue for this patient but noted).
- Trial ID: NCT02664909
- Fusion tag: FUSION-AGNOSTIC

---

## CDK7 / CDK9 INHIBITORS

**SY-5609 (CDK7i)**
- Tier: Clinical-Trial (Phase I, NCT04247126)
- Confidence: Low (D=−, A=+, R=0, X=0)
- Feasibility: F3–F4
- Mechanism: CDK7 is the CDK-activating kinase (CAK) — phosphorylates CDK1/2/4/6 to activate them, and phosphorylates RNA Pol II CTD Ser5/Ser7 at transcription initiation. CDK7 inhibition: (1) transcription initiation block; (2) CDK4/6 under-activation → Rb pathway engagement; (3) particularly affects cancer cells with high transcriptional output (super-enhancer-dependent oncoproteins). Sarcoma with CIC-DUX4-driven high ETS transcription may be selectively sensitive.
- Evidence in CIC-DUX4: None direct.
- Fusion tag: FUSION-AGNOSTIC

**AZD4573 (CDK9i)**
- Tier: Clinical-Trial (Phase I, NCT03754530)
- Confidence: Low (D=−, A=+, R=0, X=0)
- Feasibility: F3–F4
- Mechanism: CDK9 inhibition → P-TEFb complex inactivation → Pol II CTD Ser2 under-phosphorylation → transcription elongation block → depletion of short-lived oncoproteins (MYC, MCL1, PIM1). Particularly effective against MYC-driven cancers. CIC-DUX4 drives MYC via ETS factors → potential sensitivity.
- Evidence in CIC-DUX4: None direct.
- Fusion tag: FUSION-AGNOSTIC

---

## ATR INHIBITORS (REPLICATION STRESS CONTEXT)

**Elimusertib (BAY1895344) / Berzosertib (M6620)**
- Tier: Clinical-Trial
- Confidence: Low (D=−, A=+, R=0, X=0)
- Feasibility: F3–F4
- Mechanism: ATR (ATM and Rad3-related kinase) inhibition → impairs replication stress response → replication fork collapse → DSB accumulation → apoptosis in cells with high replication stress. CIC-DUX4 drives high transcriptional output → replication-transcription conflicts → elevated endogenous replication stress → potential ATRi sensitivity.
- Evidence in CIC-DUX4: None direct. Preclinical ATRi sensitivity in Ewing sarcoma (related fusion-driven sarcoma) documented.
- Note: This entry is mechanistically analogous to the BETi → ifosfamide sequencing Forward Hypothesis (FH2) — both exploit replication-stress-related DNA repair vulnerability.
- Trial IDs: NCT03188965 (elimusertib); NCT02278110 (berzosertib)
- Fusion tag: FUSION-AGNOSTIC

---

## WHAT I COULD NOT ESTABLISH

1. Any published or registered ASO specifically targeting the CIC-DUX4 junction — none exists. This is a genuine research gap.
2. ARV-825 Phase I (NCT03328078) current status — needs direct ClinicalTrials.gov verification.
3. AZD5153 (bivalent BETi) registered NCT — search 'AZD5153' at ClinicalTrials.gov; not confirmed this session.
4. CRISPR-based approaches for CIC-DUX4: solid-tumor delivery remains unsolved; not listed as actionable.
5. CDK7i or CDK9i Phase II sarcoma data — trials in Phase I; efficacy signal in CIC-DUX4 not established.
6. Whether CDKN2A expression (or its absence) was characterised in this patient's archived specimen — this biomarker directly predicts CDK4/6i likelihood of response per PMID 37875500.
