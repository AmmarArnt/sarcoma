# V4 Neoantigen Vaccine Specialist — Neoantigen and CAR-T Clinical Track Report

**TAG: Clinical / Experimental — not naturally achievable; for awareness only.**

**Summary:** Reviews personalized neoantigen vaccine platforms (BNT122/mRNA-4157/NEO-PV-01), CAR-T for solid tumours, and whether any pipeline specifically targets CIC-DUX4; applies the mandatory fusion-unconfirmed flag (this patient is in the ~5% atypical subgroup with no confirmed junction sequence); incorporates the mRNA team's anti-PEG antibody finding as a PK stratification flag for any future LNP-mRNA therapeutic.

**Confidence: medium-low** — Personalized neoantigen vaccine platforms are clinically validated in melanoma and are entering trials in other solid tumour types; transfer to CIC-rearranged sarcoma is mechanistically plausible but faces the specific challenge that (a) CIC-rearranged sarcoma is typically low-TMB, and (b) the single most immunogenic neoantigen (the fusion junction) is unavailable in this fusion-unconfirmed patient. CAR-T in solid tumours remains unresolved.

---

## MANDATORY FUSION-UNCONFIRMED FLAG (MOST IMPORTANT SECTION FOR THIS PATIENT)

**This patient is in the ~5% fusion-UNCONFIRMED subgroup of CIC-rearranged sarcoma. No CIC-DUX4, CIC-NUTM1, CIC-FOXO4, or other CIC-fusion junction sequence has been confirmed on genomic sequencing.**

Consequences for this report:

1. **A CIC-DUX4-junction-specific neoantigen vaccine is NOT APPLICABLE to this patient** without confirmatory junction identification. All entries in the "CIC-DUX4 junction-specific" category below are labeled POSSIBLY INAPPLICABLE.

2. **Personalized neoantigen approaches based on whole-exome/transcriptome analysis of tumour tissue (non-junction somatic neoantigens) may still be conceivable** if viable tumour material is available from the January 2025 resection specimen or from the current oligometastatic relapse lung lesion. This approach would target somatic SNV/indel-derived neoantigens, not CIC-DUX4 junction peptides. Evidence tier: **Clinical-Trial** (mRNA-4157 platform validated in melanoma NCT03897881; transfer to CIC-rearranged sarcoma requires dedicated effort).

3. **The mRNA team's anti-PEG antibody flag applies:** This patient has received standard BNT162b2 vaccination. A subset of BNT162b2 recipients develop anti-PEG IgG/IgM. If a future LNP-mRNA neoantigen vaccine is considered, pre-treatment anti-PEG titer measurement is a recommended PK stratification step (see mRNA team summary, Section 5a; Kozma et al., NPJ Vaccines 2022, PMID 35853896 — verify).

4. **V3 Forward Hypothesis 3 is directly relevant:** Long-read WGS + RNA-seq splice junction re-analysis of archived tumour material could potentially identify the cryptic driver event and convert this patient from fusion-unconfirmed to fusion-confirmed, opening junction-specific approaches.

---

## PERSONALIZED NEOANTIGEN VACCINE PLATFORMS

### mRNA-4157 (V940) + Pembrolizumab — Moderna/Merck

- **Platform:** Individualized mRNA vaccine encoding up to 34 tumour-specific neoantigens; delivered via LNP; patient-specific sequence determined by WES + RNA-seq + bioinformatic HLA-binding prediction.
- **Lead trial:** KEYNOTE-942 (NCT03897881) — randomised phase 2b; mRNA-4157 + pembrolizumab vs. pembrolizumab alone after resection of high-risk melanoma. Positive readout: mRNA-4157 + pembrolizumab significantly reduced recurrence vs. pembrolizumab alone (Weber et al., Lancet 2024 — verify PMID).
- **Status:** Phase 3 (KEYNOTE-1010) now enrolling in melanoma. Phase 2 trials expanding to other solid tumours.
- **CIC-rearranged sarcoma specifically:** No published trial, no reported case. CIC-rearranged sarcoma is not an enrolled cohort in any mRNA-4157 trial as of knowledge cutoff.
- **Evidence tier: Clinical-Trial** for melanoma; **Theoretical** for CIC-rearranged sarcoma.
- **Applicability to this patient:** Conceivable if viable tumour tissue is available (surgery Jan 2025 specimen or current lung biopsy) and if WES/RNA-seq identifies sufficient high-quality neoantigens. The junction peptide would only be one neoantigen (and is unavailable without junction confirmation); other somatic neoantigens from tumour mutational landscape could serve.
- **Anti-PEG flag:** LNP formulation same class as BNT162b2 PEG-LNP. Pre-treatment anti-PEG titer measurement recommended before dosing.
- **Fusion tag: FUSION-AGNOSTIC** for the non-junction personalised approach; **FUSION-CONFIRMED ONLY** for any junction-specific component.

### BNT122 (RO7198457) — BioNTech/Genentech

- **Platform:** Individualised mRNA neoantigen vaccine (up to 20 neoantigens); same LNP-mRNA platform.
- **Lead trial:** NCT04486378 — phase 2 in urothelial cancer + atezolizumab.
- **Status:** Phase 2. CIC-rearranged sarcoma: not an enrolled cohort.
- **Evidence tier: Clinical-Trial** for urothelial; **Theoretical** for sarcoma.
- **Anti-PEG flag:** Same as above.
- **Fusion tag: same as mRNA-4157 above.**

### NEO-PV-01 — Neon Therapeutics (acquired by BioNTech)

- **Platform:** Long peptide neoantigen vaccine + adjuvant (poly-ICLC).
- **Trial:** NCT02897765 — phase 1b in melanoma + nivolumab; published positive data (Ott et al., Nature 2017, PMID 28678078 for original neoantigen vaccine concept — this is the original Sahin/Ugur platform paper — verify trial ID for NEO-PV-01 specifically).
- **Status:** Platform incorporated into BioNTech portfolio; specific NEO-PV-01 development status requires verification.
- **Evidence tier: Clinical-Trial** for melanoma; **Theoretical** for sarcoma.
- **Fusion tag: same caveats.**

### CIC-DUX4-Specific Neoantigen Vaccine Design — Architecture and Junction Variability

If a junction sequence were confirmed in this patient, vaccine design would face the following:

- **Junction sequence variability:** CIC-DUX4 junctions are variable at the nucleotide level (different breakpoints within CIC exon ~15-20 fused to DUX4 exon 1). The exact neoantigen peptide(s) generated depend on the specific breakpoint, which differs between patients.
- **A "pan-CIC-DUX4" vaccine would require coverage of multiple junction variants** (estimated 3-8 major variants from the literature — no large published series; verify).
- **Per-patient sequencing is the appropriate design** rather than a pan-tumor universal vaccine.
- **No clinical-stage CIC-DUX4-specific neoantigen vaccine has been published or registered** as of knowledge cutoff.
- **Evidence tier: Theoretical** for CIC-DUX4-specific junction vaccine.

---

## CAR-T FOR SOLID TUMOURS

### General Status

CAR-T cell therapy has transformed haematological malignancies (CD19-targeting, BCMA-targeting, multiple FDA approvals). Solid tumour CAR-T remains unresolved due to:
1. **Tumour penetration** — T-cell trafficking to solid tumours is poor; TME is immunosuppressive.
2. **Antigen heterogeneity** — solid tumours have heterogeneous antigen expression; antigen-escape is common.
3. **Immunosuppressive TME** — TGF-β, Tregs, MDSCs neutralise CAR-T function in TME.
4. **On-target off-tumour toxicity** — shared antigens on normal tissues cause adverse effects.

Evidence tier: **Established** for haematological malignancies (FDA approvals for CD19-CAR-T: tisagenlecleucel, axicabtagene ciloleucel, lisocabtagene maraleucel; BCMA-CAR-T: idecabtagene vicleucel, ciltacabtagene autoleucel); **Clinical-Trial/Preclinical** for solid tumours.

### CIC-DUX4-Specific CAR-T

- No published CAR-T construct specifically targeting a CIC-DUX4-derived surface antigen.
- The fusion protein itself is intracellular — not a direct CAR-T target.
- Surface antigens overexpressed specifically in CIC-DUX4 vs. normal mesenchymal cells: not well-catalogued in the literature.
- **Evidence tier: Theoretical** for CIC-DUX4-specific CAR-T.
- **Fusion tag: FUSION-CONFIRMED ONLY** for any junction-peptide-derived TCR-T or neoantigen-targeted approach; **FUSION-AGNOSTIC** for any TAA-targeted CAR-T that does not require the junction.

### GPC2-Targeted Approaches (indirect relevance)

Glypican-2 (GPC2) is overexpressed in Ewing sarcoma and some Ewing-like sarcomas. GPC2-directed CAR-T and ADC approaches are under investigation. Whether CIC-rearranged sarcoma expresses GPC2 at comparable levels is not confirmed in the published literature.

- Evidence tier: **Preclinical-Cell** (Mitra et al. — verify; GPC2 CAR-T in Ewing context).
- CIC-DUX4 GPC2 expression: not confirmed. Do not assume transferability.

### TCR-T (T-Cell Receptor Engineered T-Cells)

If MHC-I restoration via EZH2i is achieved, junction peptide-specific TCR-T (not CAR-T) could theoretically target CIC-DUX4 junction-derived peptides presented by MHC-I. This approach requires:
1. Confirmed junction sequence.
2. Confirmed HLA type of the patient.
3. Identification of junction-derived peptides predicted to bind the patient's HLA.
4. TCR cloning from junction-reactive T-cells or in silico TCR design.

No published CIC-DUX4 junction-specific TCR-T construct exists. Evidence tier: **Theoretical**.

**Fusion tag: FUSION-CONFIRMED ONLY — POSSIBLY INAPPLICABLE to this patient.**

---

## mRNA TEAM FINDINGS — DIRECT RELEVANCE TO THIS FILE

From mrna-vaccine-summary.md (Section 5a, 5c, 7):

1. **Anti-PEG antibody (mandatory flag for all LNP therapeutics in this patient):** BNT162b2 vaccination induces anti-PEG IgG/IgM in a subset of recipients. If an LNP-mRNA neoantigen vaccine (mRNA-4157 or BNT122) is considered, accelerated blood clearance (ABC phenomenon) could reduce payload delivery to lymph nodes, diminishing neoantigen presentation and vaccine efficacy. Pre-treatment anti-PEG titer measurement is a recommended stratification step. This is a PK concern, not a contraindication. Evidence tier: Clinical observational (anti-PEG antibody induction) + Mechanistic (ABC phenomenon).

2. **No persistent checkpoint or immune alteration from BNT162b2 at this timepoint.** The vaccine-induced immune context does not confound neoantigen vaccine trial entry.

3. **Platform priming:** The mRNA-4157 and BNT122 platforms use the same LNP-mRNA technology as BNT162b2. No documented antigenic competition or immune tolerance to neoantigen payloads from prior COVID-19 vaccination.

---

## FORWARD HYPOTHESES

**[Forward Hypothesis 1] Neoantigen vaccine + EZH2i as a required tandem for MHC-I-low CIC-DUX4 tumours — vaccine primes T-cells, EZH2i makes tumour visible.**

Hypothesis: A personalised neoantigen vaccine (mRNA-4157 style, targeting somatic neoantigens from the tumour's mutational landscape) cannot produce tumour killing if the tumour cells are MHC-I-low — primed T-cells cannot see their target. Concurrent or prior EZH2i (tazemetostat) to restore MHC-I expression is a mechanistically required co-intervention for neoantigen vaccine efficacy in MHC-I-low sarcoma. The optimal sequencing would be: EZH2i (2-4 weeks to upregulate MHC-I on tumour cells) → neoantigen vaccine dosing (T-cell priming against presented neoantigens) → anti-PD-1 maintenance (prevent T-cell exhaustion post-activation).

Mechanistic basis: MHC-I-low tumour cells cannot present neoantigen peptides to CD8+ T-cells even if those T-cells are primed; without MHC-I restoration, the neoantigen vaccine generates circulating effector T-cells that cannot kill the tumour. EZH2i restores HLA-A/B/C, TAP1, TAP2, B2M expression (V3 MHC-I section). The vaccine then has a functional presentation pathway.

Study design: Two-arm phase Ib: (A) mRNA-4157 + pembrolizumab (standard of field); (B) tazemetostat 800mg BID × 4 weeks → mRNA-4157 dosing week 4 + pembrolizumab maintenance. Primary endpoint: neoantigen-specific CD8+ T-cell response by pMHC-multimer staining, and tumour MHC-I expression by serial biopsy IHC. Why not done: EZH2i + neoantigen vaccine combination has not been studied in any tumour type; CIC-DUX4-specific neoantigen vaccine design is not yet at clinical stage; MHC-I restoration as prerequisite for vaccine efficacy is an under-explored design constraint.

**[Forward Hypothesis 2] Archival tumour WES/RNA-seq re-analysis to identify high-quality non-junction neoantigens for personalised vaccine design in fusion-unconfirmed CIC-rearranged sarcoma.**

Hypothesis: Even without a confirmed fusion junction, the tumour's somatic mutational landscape (SNVs, indels, copy-number-derived frameshifts) may generate sufficient high-quality neoantigens (strong MHC-binding, expressed, absent from normal proteome) to design a personalised vaccine. Archival FFPE or frozen tissue from the January 2025 resection (>95% necrotic primary, but residual viable margin may contain sufficient DNA/RNA) or a core biopsy of the current relapse lesion could provide the input material for WES + RNA-seq + HLA typing → neoantigen prediction pipeline.

Mechanistic basis: Even low-TMB tumours generate 5-20 high-quality predicted neoantigens on WES (Rizvi et al., Science 2015 for concept — not CIC-DUX4-specific). The tumour necrosis from VDC/IE means most cells in the surgical specimen are dead; the remaining viable cells are the resistant subclone — which is the most clinically relevant target. RNA-seq from viable tumour cells would identify expressed neoantigens.

Study design: Molecular tumour board referral: (1) retrieve archival FFPE from Jan 2025 resection or biopsy current relapse lesion; (2) WES (tumour + germline paired) + RNA-seq + HLA typing; (3) neoantigen prediction (MHC-I binding by netMHCpan, expression threshold >1 TPM, absence from germline proteome); (4) if ≥5 high-quality neoantigens identified, enrol in mRNA-4157 investigational access protocol or compassionate use. Why not done: Requires dedicated tumour board engagement; fusion-unconfirmed status may not have triggered neoantigen analysis in standard clinical workup; FFPE quality from highly necrotic specimen may limit WES sensitivity.

---

## ATYPICAL-CASE NOTES

**This patient is fusion-UNCONFIRMED — the most impactful atypical-case dimension for this entire specialist report.**

FUSION-CONFIRMED ONLY (POSSIBLY INAPPLICABLE to this patient):
- CIC-DUX4 junction-specific neoantigen vaccine: requires confirmed junction sequence. No confirmed junction → this approach is not currently applicable.
- CIC-DUX4 junction peptide-specific TCR-T: same — requires confirmed junction.
- Pan-CIC-DUX4 neoantigen vaccine: same — requires junction characterisation.

FUSION-AGNOSTIC (applicable to this patient):
- Personalized neoantigen vaccine from somatic WES/RNA-seq neoantigens (non-junction): applicable if viable tissue available and sufficient neoantigens identified.
- General CAR-T targeting a TAA not derived from the junction (if such a target were identified).
- The anti-PEG antibody flag applies regardless of fusion status.

---

## WHAT I COULD NOT ESTABLISH

1. Whether any clinical-stage neoantigen vaccine trial is currently enrolling sarcoma patients (beyond melanoma). Trial landscape changes rapidly; verify at ClinicalTrials.gov.

2. Quality of archival tissue from the January 2025 resection (predominantly necrotic — DNA/RNA quality from FFPE necrotic tissue is variable; WES may have insufficient tumour purity if viable cells are <20%).

3. This patient's HLA type. Required for neoantigen binding prediction and for any TCR-T approach.

4. Anti-PEG antibody titer in this patient specifically. Prevalence is estimated at 30-50% of BNT162b2 recipients (Kozma et al. 2022 — verify); titer varies. Only measurable by ELISA.

5. GPC2 expression in this patient's tumour. Not in standard clinical report; requires IHC or RNA-seq.

6. Number and quality of somatic neoantigens in this tumour. CIC-rearranged sarcomas are typically low-TMB; if <5 high-quality neoantigens are identified, personalized vaccine design may not be feasible.

7. Whether the ~5% fusion-unconfirmed group represents true fusion-negativity, assay failure, novel undiscovered fusions, or short-read sequencing limitations at DUX4 repeat arrays. This has direct implications for whether the fusion junction exists to target.
