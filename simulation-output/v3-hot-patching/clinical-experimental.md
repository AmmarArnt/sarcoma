# V3 Sub-Agent: PROTAC/ASO Specialist (Clinical/Experimental Track)
# Clinical and Experimental Targeted Approaches in CIC-Rearranged Sarcoma

**SCOPE TAG: Clinical / Experimental — not naturally achievable; for awareness only.**
**This output covers published constructs and registered trials only. No agent-invented gene therapies are included.**

Summary: Covers the clinical and experimental landscape of ASOs, PROTACs, EZH2 inhibitors, BET inhibitors, and CDK4/6 inhibitors as registered clinical trials or published preclinical constructs relevant to CIC-rearranged sarcoma; explicitly covers the fusion-unconfirmed subgroup caveat for junction-specific approaches.

Confidence: medium — the clinical trial landscape for related epigenetic targets is well-documented; CIC-DUX4-specific PROTAC/ASO data are essentially absent from the published literature; extrapolation from related fusion sarcomas is mechanistically defensible but not experimentally confirmed in CIC-DUX4.

CRITICAL PATIENT CASE FLAG — FUSION-UNCONFIRMED SUBGROUP:
This patient belongs to the ~5% genomically-uncharacterized subgroup: no confirmed CIC-DUX4/CIC-NUTM1/CIC-FOXO4 or other junction sequence has been identified by genome sequencing. Entries below are tagged:
- FUSION-CONFIRMED ONLY: approaches that require knowledge of the specific junction sequence to design (ASOs, junction-specific PROTACs, junction-specific degraders). These are POSSIBLY INAPPLICABLE to this patient — the junction target has not been confirmed.
- FUSION-AGNOSTIC: approaches that target the epigenetic amplification machinery or cell cycle regardless of which specific fusion is present.

---

## PART 1: ANTISENSE OLIGONUCLEOTIDES (ASOs)

### CIC-DUX4 Junction-Targeting ASOs

Published status: As of knowledge cutoff (August 2025), there are NO published clinical-stage ASOs specifically targeting the CIC-DUX4 mRNA junction. The field has not yet produced a CIC-DUX4-specific ASO construct that has been validated beyond theoretical design in the published literature.

Preclinical status: The technology is established — ASOs (gapmers) targeting fusion mRNA junctions have demonstrated activity in other fusion sarcomas:
- EWSR1-FLI1 junction ASOs have been published in preclinical Ewing sarcoma models [Toub et al. 2006 Pharm Res; Maksimenko et al. 2003]. These are proof-of-concept for the approach, not evidence for CIC-DUX4.
- No peer-reviewed published ASO targeting the CIC-DUX4 junction (exon 20 of CIC fused to exon 1 of DUX4, or any of the known junction variants) was identified.

Evidence tier: Theoretical / Preclinical (for the general ASO-junction approach applied to CIC-DUX4)
Fusion-confirmed or agnostic: FUSION-CONFIRMED ONLY

Patient-specific note: Because this patient has no confirmed junction sequence, a CIC-DUX4 junction ASO cannot be designed for this patient without first establishing the junction (if any). If the tumor is in the ~5% genomically-uncharacterized subgroup and a cryptic translocation or variant fusion is later identified by deeper sequencing (long-read WGS, RNAseq splice junction analysis), an ASO approach becomes theoretically applicable.

ASO platform context (for awareness):
- Approved ASOs for other diseases use the same basic technology: nusinersen (Spinraza, IONIS/Biogen — SMN2 intron, FDA 2016 SMA), inotersen (Tegsedi — TTR, FDA 2018), casimersen (Amondys 45 — DMD exon 45 skip, FDA 2021). These demonstrate clinical feasibility for splice-junction targeting. None are for sarcoma.

### DUX4 mRNA Suppression (not junction-specific)

- Theoretical application: DUX4 mRNA is pathologically re-expressed in CIC-DUX4 sarcoma from the C-terminal transactivation domain contribution. Separately, DUX4 overexpression in FSHD (facioscapulohumeral muscular dystrophy) has motivated development of DUX4-suppressing ASOs (Draper et al., FSHD research). These target DUX4 mRNA broadly.
- Evidence tier: Theoretical (for sarcoma application); Preclinical-Cell (for FSHD-motivated DUX4 ASOs in muscle cells)
- Fusion-confirmed or agnostic: Partial — DUX4 mRNA suppression would reduce the C-terminal transactivation domain contribution but would not eliminate the CIC-driven DNA targeting component of the fusion. Unlikely to be sufficient as monotherapy.
- Patient-specific note: Given fusion-unconfirmed status, DUX4 mRNA-targeting ASOs (which target the DUX4 portion rather than the specific junction) are more theoretically applicable than junction-specific ASOs — but the clinical utility is entirely unestablished.

---

## PART 2: PROTACs (Proteolysis-Targeting Chimeras)

### General PROTAC Technology

PROTACs recruit a target protein to an E3 ubiquitin ligase (CRBN or VHL), leading to proteasomal degradation. They are distinct from inhibitors in that catalytic degradation allows sub-stoichiometric target engagement and can overcome resistance mechanisms.

### BET-Targeting PROTACs (BRD4 degraders)

**ARV-771**
- Evidence tier: Preclinical-Animal (prostate cancer, breast cancer xenograft models); Theoretical (CIC-DUX4)
- Mechanism: ARV-771 degrades BRD2/BRD3/BRD4 via CRBN-mediated proteasomal degradation. Produces more complete BRD4 depletion than BETi inhibitors (which leave the protein intact). Preclinical activity demonstrated in prostate cancer PDX models [Raina et al. 2016 PNAS PMID 27528661].
- Sarcoma-specific data: No published data in CIC-DUX4. Preclinical activity in Ewing sarcoma-related models would be the closest available evidence — not confirmed.
- Clinical status: No registered clinical trial for ARV-771 as of knowledge cutoff. Clinical candidates include ARV-825 (CRBN-based BRD4 degrader, studied in hematologic malignancies) — Phase I NCT03328078 (note: verify current status; may have been completed or superseded).
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC (BRD4 dependency does not require a specific fusion).

**dBET6**
- Evidence tier: Preclinical-Cell (multiple cell lines, including some sarcoma-adjacent)
- Highly potent BRD4 degrader; primarily a research tool. No clinical candidate status as of knowledge cutoff.
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC.

### EZH2-Targeting PROTACs

- Evidence tier: Preclinical-Cell
- Published EZH2 degraders have been reported in academic literature (e.g., MS1943 — EZH2 degrader via CRBN, Yu et al. 2021 Nat Chem Biol PMID 33349709). Activity demonstrated in TNBC cell lines.
- Sarcoma-specific data: None published for CIC-DUX4.
- Clinical status: No registered clinical trial for an EZH2 PROTAC in solid tumors as of knowledge cutoff.
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC.

### CIC-DUX4 Fusion Protein-Targeting PROTACs

- Evidence tier: Theoretical
- No published PROTAC targeting the CIC-DUX4 fusion protein has been identified. Designing a fusion protein-targeting PROTAC requires (a) knowing the junction sequence and (b) identifying a ligandable surface unique to the fusion. The intrinsically disordered DUX4 transactivation domain poses a significant drug-discovery challenge.
- Fusion-confirmed or agnostic: FUSION-CONFIRMED ONLY. Cannot be designed for this patient without confirmed junction sequence.

---

## PART 3: EZH2 INHIBITORS — CLINICAL TRIAL LANDSCAPE

### Tazemetostat (Tazverik, Epizyme/Ipsen)

- Evidence tier: Established (epithelioid sarcoma, FDA); Clinical-Trial (CIC-rearranged sarcoma extrapolation)
- FDA approval: Accelerated approval 2020-01-23 for metastatic or locally advanced epithelioid sarcoma in patients ≥16 years not eligible for complete resection. Based on EZH-202 (NCT01897571) Cohort 5: ORR 15% (CR 1.6%, PR 13.4%), median PFS 5.7 months, median OS 82.4 weeks. This is the approval indication — NOT CIC-rearranged sarcoma.
- EMA status: As of knowledge cutoff, tazemetostat's EMA marketing authorisation status for epithelioid sarcoma should be independently verified. EMA reviewed an application; the FDA accelerated approval does not automatically transfer to EMA status. Do NOT cite tazemetostat as EMA-Established without verifying the current EMA label.
- CIC-DUX4 rationale: Extrapolated from PRC2 dependency in BAF-disrupted fusion sarcomas. CIC-DUX4 co-occurs with chromatin remodeling dysregulation, but direct EZH2 dependency has not been validated in CIC-DUX4-specific published studies. State this explicitly.
- Atypical-case flag: FUSION-AGNOSTIC. Applicable to fusion-unconfirmed subgroup.
- Relevant trials (CIC-rearranged sarcoma context):
  - NCT01897571 (EZH-202) — the pivotal epithelioid sarcoma trial; also enrolled "other sarcoma" basket; check for any CIC-rearranged enrollment data
  - NCT02601950 (SYMPHONY) — tazemetostat basket, solid tumors; verify current enrollment
  - Basket trials enrolling EZH2-altered tumors may include rare sarcomas; discuss with oncologist
- Drug interaction: Tazemetostat is a CYP3A4 substrate; strong CYP3A4 inhibitors increase exposure. Ifosfamide activates via CYP3A4; concurrent tazemetostat + ifosfamide interaction requires pharmacokinetic monitoring. Consult oncologist.

### Valemetostat (DS-3201b)

- Evidence tier: Clinical-Trial
- EZH1/EZH2 dual inhibitor (distinct from tazemetostat which primarily inhibits EZH2). Dual inhibition may be important in tumors that upregulate EZH1 as a compensatory mechanism to tazemetostat.
- Primary development in T-cell lymphoma: NCT04703192. Solid tumor data limited.
- FDA/EMA: Not approved for any indication as of knowledge cutoff.
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC.

### MAK683 (EED inhibitor)

- Evidence tier: Clinical-Trial
- Targets EED, the PRC2 allosteric activator — a different mechanistic angle than EZH2 catalytic inhibition. Phase I/II in advanced malignancies NCT02900651.
- FDA/EMA: Not approved.
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC.

---

## PART 4: BET INHIBITORS — CLINICAL TRIAL LANDSCAPE

### OTX015 / Birabresib (MK-8628)

- Evidence tier: Clinical-Trial
- Phase I/II in hematologic malignancies (NCT01713582) and solid tumors. Results in hematologic disease published; solid tumor arm results more limited. Modest monotherapy activity.
- FDA/EMA: Not approved for any indication.
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC. BRD4 super-enhancer dependency is a property of the ETS amplification layer, not the specific fusion.

### BMS-986158

- Evidence tier: Clinical-Trial
- Phase I/II solid tumors including sarcoma. NCT02419417. Limited published efficacy data.
- FDA/EMA: Not approved.
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC.

### AZD5153

- Evidence tier: Clinical-Trial
- Bivalent BET inhibitor (occupies both bromodomains). Trials in solid tumors. [NCT number: I cannot confirm the exact registered trial NCT ID for AZD5153 without verified source — do not fabricate. Verify at ClinicalTrials.gov by searching "AZD5153".]
- FDA/EMA: Not approved.
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC.

### BET inhibitor + immunotherapy combinations

- Evidence tier: Clinical-Trial
- The mechanistic rationale (BETi reduces PD-L1 → augments T-cell killing) has motivated combination trials. BMS-986158 + nivolumab (NCT02419417 expansion); ZEN-3694 + enzalutamide (prostate). No CIC-DUX4-specific combination trial identified.

---

## PART 5: CDK4/6 INHIBITORS — CLINICAL TRIAL LANDSCAPE

### Palbociclib (Ibrance, Pfizer)

- Evidence tier: Established (HR+/HER2- breast cancer, FDA 2015; EMA 2016); Clinical-Trial (sarcoma)
- Mechanism: Inhibits CDK4 and CDK6 → prevents Rb phosphorylation → E2F target gene suppression → G1 arrest. In CIC-DUX4, the ETS factors constitutively activate CCND1 and CDK4 → CDK4/6 inhibition is mechanistically rational (targeting the downstream execution machinery even if the fusion remains).
- FDA approval: HR+/HER2- breast cancer (multiple lines). NOT approved for sarcoma.
- EMA approval: HR+/HER2- breast cancer. NOT approved for sarcoma.
- Sarcoma data: Well-differentiated/dedifferentiated liposarcoma (CDK4-amplified) has shown sensitivity; CDK4/6i in other sarcomas is less clear. NCT03677388 (palbociclib in sarcoma basket); NCT02441946. Response rates in CDK4-non-amplified sarcomas have been modest.
- Atypical-case flag: FUSION-AGNOSTIC. CDK4/CCND1 dependency is a downstream effect of ETS factor overactivation; applicable regardless of which upstream fusion is present.
- Patient context: Patient on high-dose ifosfamide. CDK4/6 inhibitors cause bone marrow suppression (neutropenia). Combining with ifosfamide (which also suppresses marrow) would require careful timing and dosing. This is a key safety concern for oncologist discussion.

### Ribociclib (Kisqali, Novartis)

- Evidence tier: Established (HR+/HER2- breast cancer, FDA 2017; EMA 2017); Clinical-Trial (sarcoma)
- Same mechanism as palbociclib; approved in breast cancer. Sarcoma trials: NCT02571829.
- Not approved for sarcoma. FUSION-AGNOSTIC.

### Abemaciclib (Verzenio, Eli Lilly)

- Evidence tier: Established (HR+/HER2- breast cancer, FDA 2017; EMA 2018); Clinical-Trial (sarcoma)
- Abemaciclib is somewhat more selective for CDK4 and has better CNS penetration than palbociclib. Sarcoma data: NCT02664909, NCT03310151. ORR modest in non-CDK4-amplified sarcomas.
- Not approved for sarcoma. FUSION-AGNOSTIC.

---

## PART 6: TRANSCRIPTIONAL CDK INHIBITORS

### CDK7 Inhibitors (SY-5609)

- Evidence tier: Clinical-Trial
- CDK7 activates CDK9 and drives transcription initiation. Highly transcriptionally active fusion sarcomas are theoretically vulnerable. SY-5609: NCT04247126. Published data limited as of knowledge cutoff.
- FDA/EMA: Not approved.
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC.

### CDK9 Inhibitors (Flavopiridol, AZD4573)

- Evidence tier: Clinical-Trial (AZD4573); Established historical (flavopiridol — never approved as standalone)
- CDK9 phosphorylates RNA Pol II CTD → releases it from pausing → transcriptional elongation. BRD4 at super-enhancers recruits P-TEFb (which contains CDK9). CDK9 inhibition therefore attacks the same amplification circuit as BETi from a different angle.
- AZD4573: NCT03754530. Data primarily in hematologic malignancies.
- Fusion-confirmed or agnostic: FUSION-AGNOSTIC.

---

## PART 7: COMBINATION STRATEGIES WITH STRONGEST RATIONALE

Listed in order of mechanistic logic and available evidence:

1. Tazemetostat + checkpoint inhibitor (pembrolizumab/nivolumab): EZH2i restores MHC-I (V3→V4 bridge) + PD-1 blockade releases T-cell braking. This is the most clinically actionable combination. NCT04196738 (tazemetostat + pembrolizumab in solid tumors — verify current status). FUSION-AGNOSTIC.

2. BETi + anti-PD-1: BETi reduces PD-L1 → augments T-cell access. OTX015/BMS-986158 + nivolumab. FUSION-AGNOSTIC.

3. CDK4/6i + EZH2i: CDK4/6 inhibition causes G1 arrest → increases apoptotic sensitivity to EZH2i-induced tumor suppressor de-repression. Preclinical rationale in related sarcomas. FUSION-AGNOSTIC.

4. HDACi + EZH2i: Dual epigenetic de-repression as described in Epigenetic Therapy Specialist. FUSION-AGNOSTIC.

---

## FORWARD HYPOTHESES

[Forward Hypothesis 1] Whole-genome or transcriptomic re-analysis of this patient's tumor specimen to identify the cryptic fusion or driver event, enabling junction-specific ASO/PROTAC design.

Hypothesis: In the ~5% fusion-unconfirmed CIC-rearranged sarcoma subgroup, the "uncharacterized" status may reflect technical limitations of the original sequencing (insufficient read depth at repetitive DUX4 loci on 4q35/10q26, which are notoriously difficult to characterize by short-read WGS; alternatively, a genuinely novel fusion partner). Long-read whole-genome sequencing (Oxford Nanopore or PacBio) combined with RNA-seq junction analysis may identify the driver event, thereby converting a fusion-agnostic treatment plan into a fusion-targeted one. This is not a therapeutic intervention itself — it is a diagnostic step that unlocks therapeutic options currently blocked by the unknown junction.

Mechanistic basis: DUX4 loci in subtelomeric repeat arrays are poorly covered by standard short-read WGS. Long-read sequencing resolves repetitive regions. RNA-seq detection of a novel fusion transcript does not require knowing the DNA breakpoint. A successful identification would change this patient's PROTAC/ASO eligibility from "POSSIBLY INAPPLICABLE" to "potentially applicable."

Study design: Re-analysis of archived tumor specimen (FFPE or frozen) with long-read WGS and polyA-enriched RNA-seq. Primary endpoint: detection of any fusion transcript involving CIC, DUX4, or a related family member. This has been done in research cohorts; it is technically feasible and clinically available at specialized centers.

[Forward Hypothesis 2] Neoantigen-agnostic epigenetic re-sensitization followed by high-dose ifosfamide: pre-treating with EZH2i/BETi to collapse super-enhancer-driven DNA damage response programs before ifosfamide exposure, potentially enhancing cytotoxic efficacy.

Hypothesis: CIC-DUX4 super-enhancer programs may maintain elevated DNA damage response (DDR) gene expression (BRD4 occupancy at DDR super-enhancers including RAD51, BRCA2-target genes, and RAD52). BETi pre-treatment would collapse these DDR super-enhancers, reducing homologous recombination (HR) capacity and sensitizing cells to ifosfamide-induced DNA crosslinks. This "epigenetic sensitization before alkylating agent" sequence is mechanistically distinct from combination therapy and represents a timing-dependent strategy.

Mechanistic basis: BRD4 controls super-enhancers at DDR genes in multiple cancer types [Qiu et al. 2015 Cancer Cell]; BETi-mediated HR impairment has been published in BRCA-wild-type cancers [preclinical; no CIC-DUX4 specific data]. This is a testable sequencing hypothesis — short BETi course (days 1-3) → ifosfamide infusion (day 4). The ifosfamide timing is particularly relevant for this patient who is already scheduled for high-dose ifosfamide.

Study design: CIC-DUX4 PDX or cell line. Arm 1: ifosfamide equivalent (in vitro: chlorambucil as proxy). Arm 2: BETi 48h pre-treatment → ifosfamide. Primary endpoint: gamma-H2AX quantification, comet assay, cell survival. Why not yet done: this sequencing strategy has not been tested in CIC-DUX4 specifically; clinical translation would require a window-of-opportunity trial design.

---

## ATYPICAL-CASE NOTES

FUSION-CONFIRMED ONLY entries in this file:
- CIC-DUX4 junction-targeting ASOs
- CIC-DUX4 fusion protein-targeting PROTACs
Rationale: These require knowledge of the specific junction sequence, which has not been established for this patient. They are POSSIBLY INAPPLICABLE.

FUSION-AGNOSTIC entries (all others in this file): Tazemetostat/EZH2i, HDACi, BETi (OTX015, BMS-986158, AZD5153), CDK4/6i (palbociclib, ribociclib, abemaciclib), CDK7/9i, BET-PROTACs (ARV-771, ARV-825), EZH2-PROTACs — these target the epigenetic amplification and cell cycle machinery; applicable to the fusion-unconfirmed subgroup.

---

## WHAT I COULD NOT ESTABLISH

1. Any published clinical-stage ASO targeting the CIC-DUX4 mRNA junction. None exists in the current literature.

2. Any published PROTAC targeting the CIC-DUX4 fusion protein. None exists.

3. Exact NCT numbers for AZD5153 and valemetostat solid tumor trials — flagged rather than fabricated; verify at ClinicalTrials.gov.

4. Tazemetostat EMA current marketing authorisation status — requires independent verification against EMA database.

5. Any published combination trial of BETi + EZH2i + checkpoint inhibitor specifically in CIC-rearranged sarcoma. The combination rationale is strong; the clinical data are absent.

6. CDK4 amplification or CDK4 dependency status for this specific patient's tumor. The CDK4/6i rationale in CIC-DUX4 is extrapolated from downstream ETS-driven CCND1/CDK4 overexpression, not from CDK4 gene amplification. This is a weaker rationale than in CDK4-amplified liposarcoma.
