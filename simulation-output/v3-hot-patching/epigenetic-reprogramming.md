# V3 Sub-Agent: Epigenetic Therapy Specialist
# Epigenetic Reprogramming in CIC-Rearranged Sarcoma

Summary: Maps clinical and dietary epigenetic agents targeting HDAC, EZH2/PRC2, DNMT, and BET bromodomain axes in CIC-rearranged sarcoma, with mandatory MHC-I upregulation flags for V4; excludes fusion-specific ASOs/PROTACs (covered by PROTAC/ASO specialist) and differentiation agents (covered by Differentiation Therapy Specialist).

Confidence: medium — the clinical agent mechanisms are well-characterised in related fusion sarcomas (Ewing, epithelioid, synovial); direct CIC-DUX4 cell-line or patient data are sparse, and most mechanistic claims rest on extrapolation from the shared BAF/PRC2 biology.

Patient case note: Fusion-UNCONFIRMED subgroup (~5% of CIC-rearranged sarcoma). Epigenetic approaches targeting PRC2/EZH2, BET/BRD4, and HDAC are fusion-AGNOSTIC (they target the epigenetic machinery that maintains the oncogenic program, not the fusion protein directly). All entries in this file are therefore potentially applicable to this patient. Fusion-specific entries are explicitly tagged; none appear here.

---

## MHC-I UPREGULATION CANDIDATES
### (V3 → V4 bridge — mandatory section for V4 lead and orchestrator)

This section lists V3 epigenetic interventions with documented or mechanistically grounded capacity to upregulate MHC-I (HLA-A/B/C) surface expression on tumor cells. MHC-I upregulation is required for CD8+ T-cell recognition and is the mechanistic bridge enabling V4 immune clearance strategies. NK cell strategies (V4) benefit from MHC-I-LOW states — see V4 for that complementary framing.

| Candidate | MHC-I Upregulation Evidence | Mechanism | Evidence tier | Notes for V4 |
|---|---|---|---|---|
| Tazemetostat (EZH2i) | Documented in epithelioid sarcoma and other EZH2-dependent tumors; extrapolated to CIC-DUX4 | EZH2 inhibition reduces H3K27me3 at MHC-I gene loci (HLA-A/B/C, TAP1, TAP2, beta-2-microglobulin); restores antigen presentation machinery (APM) expression | Clinical-Trial (CIC context); Established (epithelioid sarcoma indication) | V4 must incorporate: EZH2i is the cleanest V3→V4 bridge. No direct CIC-DUX4 MHC-I data; extrapolated from SMARCB1-null and BAF-disrupted models [no direct citation; mechanism inferred from PMID 31285543, Bugide et al. 2018 epithelioid sarcoma; Kim et al. 2021 EZH2i+CPI synergy in NSCLC] |
| Vorinostat / Entinostat (class I HDACi) | Documented in multiple tumor types; sarcoma extrapolation | HDAC1/2/3 inhibition → histone H3/H4 hyperacetylation at MHC-I promoters → increased HLA expression; also upregulates TAP1/TAP2, NLRC5 (MHC-I transcriptional activator) | Clinical-Trial (sarcoma-adjacent); no direct CIC-DUX4 data | Strong mechanistic basis across tumor types; NLRC5 upregulation by HDACi is a published mechanism [no direct CIC-DUX4 citation; mechanism inferred from Tong et al. 2020 PMID 32179131; Li et al. HDACi + MHC-I in solid tumors] |
| Panobinostat (pan-HDACi) | Broader HDACi class; higher MHC-I upregulation but also higher toxicity | Class I + II HDAC inhibition; broader epigenetic de-repression including APM components | Clinical-Trial (hematologic malignancies, FDA approved; sarcoma extrapolation) | Flag: panobinostat FDA-approved for multiple myeloma only; toxicity profile more challenging than class-selective HDACi |
| BET inhibitors (BRD4i: JQ1 preclinical; OTX015/birabresib clinical) | Indirect; BETi reduces PD-L1 expression (reduces immune evasion) AND in some models upregulates MHC-I via secondary chromatin opening | BRD4 reads H3K27ac at super-enhancers; BETi collapse of super-enhancers at PD-L1 locus (CD274) reduces PD-L1, potentially enabling T-cell recognition even without direct MHC-I upregulation | Clinical-Trial | The PD-L1-suppression mechanism is better established than direct MHC-I upregulation; V4 should note this distinction [Zenere et al. 2021 BETi + PD-L1; no direct CIC-DUX4 citation] |
| Sulforaphane (dietary HDAC modulator) | Not established at dietary concentrations; mechanistically plausible | Weak class-I HDACi activity in cell lines; concentrations required for HDAC inhibition (typically 5-50 µM) far exceed tissue exposure from dietary broccoli intake | Preclinical-Cell | WHETHER DIETARY SULFORAPHANE ACHIEVES SUFFICIENT TUMOR EXPOSURE FOR MHC-I UPREGULATION: UNESTABLISHED. Do not claim equivalence with clinical HDACi. |
| Butyrate (dietary SCFA) | Not established systemically | HDAC inhibitor at mM colonic concentrations; systemic portal/peripheral concentrations are orders of magnitude lower | Preclinical | Same caveat as sulforaphane: systemic exposure to butyrate from dietary fiber is far below concentrations needed for tumor-cell MHC-I upregulation. UNESTABLISHED clinically. |

**Summary for V4 lead:** The two cleanest MHC-I upregulation candidates requiring V4 attention are (1) tazemetostat / EZH2 inhibitors and (2) clinical class-I HDACi (entinostat, vorinostat). Both have registered sarcoma-adjacent or sarcoma-specific clinical trials. Dietary analogues (sulforaphane, butyrate) are mechanistically aligned but tumor exposure is unestablished — do not present them as equivalent to clinical agents in V4 planning.

---

## CLINICAL AGENTS

### 1. EZH2 Inhibitors

**Tazemetostat (Tazverik)**

- Evidence tier: Established (epithelioid sarcoma, FDA); Clinical-Trial (CIC-rearranged sarcoma extrapolation)
- Mechanism: Tazemetostat is a selective EZH2 methyltransferase inhibitor. EZH2, the catalytic subunit of PRC2, deposits H3K27me3 — the repressive chromatin mark that silences tumor suppressors and differentiation genes. In BAF-disrupted fusion sarcomas, loss of BAF antagonism allows PRC2 to run unopposed, creating EZH2 dependence. Tazemetostat reduces H3K27me3 genome-wide, de-represses tumor suppressors (CDKN2A, CDKN1A), and upregulates MHC-I (see above).
- FDA approval: Accelerated approval 2020-01-23 for metastatic/locally advanced epithelioid sarcoma in patients ≥16 years not eligible for complete resection. ORR ~15% (CR 1.6%, PR ~13%) in pivotal EZH-202 cohort. NOT approved for CIC-rearranged sarcoma.
- EMA status: As of knowledge cutoff (August 2025), tazemetostat does not hold a full EMA marketing authorisation for epithelioid sarcoma; EMA reviewed an application under exceptional circumstances. Agents citing tazemetostat as "Established" in a European context must verify current EMA label before doing so — the FDA accelerated approval does not transfer to EMA status. [Note: EMA status should be independently verified against the current EMA product database.]
- Rationale for CIC-DUX4: Extrapolated from PRC2 dependency in BAF-disrupted fusion sarcomas (epithelioid sarcoma SMARCB1 loss, synovial sarcoma SS18-SSX). CIC-DUX4 evidence is indirect: CIC-rearranged sarcomas show transcriptional signatures consistent with altered PRC2 regulation, but direct EZH2 dependency has not been established in CIC-DUX4-specific published studies as of knowledge cutoff. State this explicitly — the extrapolation is mechanistically defensible but not experimentally confirmed in CIC-DUX4.
- Atypical-case flag: FUSION-AGNOSTIC. The rationale does not require confirmed CIC-DUX4 fusion; it requires PRC2 activity in a mesenchymal sarcoma context. Applicable to fusion-unconfirmed subgroup.
- Relevant trials: NCT01897571 (EZH-202 pivotal, epithelioid sarcoma); NCT02601950 (basket study); NCT04204941 (pediatric/young adult sarcoma, tazemetostat combinations) — confirm current trial enrollment status independently.
- Chemo interaction note: Tazemetostat is a CYP3A4 substrate; co-administration with strong CYP3A4 inhibitors or inducers requires dose adjustment. Relevant to patient on high-dose ifosfamide (CYP3A4 pathway); discuss with oncologist.

**Valemetostat / MAK683 / PF-06821497 (next-generation EZH2i)**

- Evidence tier: Clinical-Trial
- These are second-generation EZH2 inhibitors or EED inhibitors (MAK683 targets EED, a PRC2 complex component, rather than EZH2 directly — a mechanistic distinction that may overcome EZH2-mutant resistance). NCT04590079 (valemetostat in lymphoma/solid tumors); MAK683 NCT02900651. Sarcoma-specific data limited.
- Atypical-case flag: FUSION-AGNOSTIC.

### 2. HDAC Inhibitors

**Entinostat (class I selective: HDAC1/2/3)**

- Evidence tier: Clinical-Trial
- Mechanism: Class I HDAC inhibition increases histone acetylation at gene promoters previously silenced by HDACs, including MHC-I antigen presentation genes (TAP1, TAP2, HLA class I) and differentiation/tumor suppressor genes. Class I selectivity is clinically preferred over pan-HDACi for tolerability in solid tumors.
- FDA/EMA status: Not approved for sarcoma; breakthrough therapy designation withdrawn in HR+ breast cancer. In sarcoma context: Clinical-Trial tier.
- Relevant trials: NCT02890069 (entinostat + pembrolizumab in sarcoma — the combination strategy that bridges V3→V4); NCT01253278 (entinostat in Ewing sarcoma) — verify current status.
- Atypical-case flag: FUSION-AGNOSTIC.

**Vorinostat (SAHA, Zolinza)**

- Evidence tier: Established (CTCL, FDA-approved 2006); Clinical-Trial (solid tumor/sarcoma extrapolation)
- Mechanism: Pan-HDACi; HDAC1/2/3/6 inhibition. Upregulates MHC-I antigen presentation machinery. In sarcoma, vorinostat has shown modest preclinical activity; clinical sarcoma trials have had mixed results.
- FDA approval: Approved for cutaneous T-cell lymphoma. NOT approved for sarcoma.
- EMA status: Approved by EMA for CTCL (Zolinza). Not approved for sarcoma.
- Note: The pan-HDACi toxicity profile (fatigue, nausea, thrombocytopenia, QT prolongation) is more challenging than class-I selective agents. In the setting of concurrent high-dose ifosfamide, additional bone marrow suppression is a serious concern.
- Atypical-case flag: FUSION-AGNOSTIC.

**Panobinostat (Farydak)**

- Evidence tier: Established (multiple myeloma, FDA 2015); Clinical-Trial (sarcoma extrapolation)
- FDA/EMA: FDA and EMA approved for relapsed/refractory multiple myeloma. NOT approved for sarcoma.
- Caution: Pan-HDAC inhibition; significant toxicity. Lower priority in solid tumor setting given tolerability. Listed for completeness.
- Atypical-case flag: FUSION-AGNOSTIC.

### 3. BET Bromodomain Inhibitors

**OTX015 / birabresib (MK-8628)**

- Evidence tier: Clinical-Trial
- Mechanism: BRD4 bromodomain inhibition prevents BRD4 from reading H3K27ac marks at super-enhancers → collapse of CIC-DUX4-maintained ETS factor super-enhancers → reduced ETV4, ETV5, ETV1, MYC expression. BETi acts downstream of the fusion protein: even if CIC-DUX4 remains present, BRD4-dependent amplification of its output is reduced.
- Clinical status: Phase I/II trials in hematologic malignancies (NCT01713582) and solid tumors. Sarcoma data: modest monotherapy activity; combination strategies under evaluation.
- EMA/FDA: Not approved for any indication as of knowledge cutoff.
- Atypical-case flag: FUSION-AGNOSTIC. BRD4 dependence is an epigenetic amplification layer that does not require a specific fusion; it applies wherever super-enhancer addiction exists.

**BMS-986158**

- Evidence tier: Clinical-Trial
- Phase I/II, solid tumors including sarcoma. NCT02419417. Limited published efficacy data for CIC-rearranged sarcoma specifically.
- Atypical-case flag: FUSION-AGNOSTIC.

**AZD5153**

- Evidence tier: Clinical-Trial
- Bivalent BET inhibitor (binds both bromodomains simultaneously). NCT03107olean — [Note: I cannot confirm the exact NCT number for AZD5153 without a verified source; do not fabricate. Confirm independently from ClinicalTrials.gov search for AZD5153.] Preclinical activity reported in several solid tumors.
- Atypical-case flag: FUSION-AGNOSTIC.

### 4. DNMT Inhibitors

**Azacitidine / Decitabine (DNMTi)**

- Evidence tier: Established (MDS/AML, FDA/EMA); Clinical-Trial (sarcoma extrapolation)
- Mechanism: DNA methyltransferase inhibition → passive demethylation of CpG islands at silenced tumor suppressor and differentiation gene promoters. Also demethylates MHC-I pathway genes and endogenous retroviral elements (ERVs), which can serve as immunostimulatory dsRNA (the "viral mimicry" mechanism).
- FDA/EMA: FDA and EMA approved for MDS and AML. NOT approved for sarcoma.
- V3→V4 bridge note: DNMTi-induced viral mimicry (demethylation of ERVs → cytosolic dsRNA → STING activation → type I IFN → MHC-I upregulation) is an emerging immunostimulatory mechanism described in multiple solid tumor types [Chiappinelli et al. 2015 Cell; Roulois et al. 2015 Cell]. This is mechanistically relevant but: (a) direct CIC-DUX4 evidence absent, (b) these drugs are generally used at lower doses for epigenetic effect than for direct cytotoxicity.
- Atypical-case flag: FUSION-AGNOSTIC.

---

## DIETARY MODULATORS

### Sulforaphane (from broccoli/broccoli sprouts)

- Patient context: Patient consumes fresh broccoli juice. Key note: juicing destroys myrosinase (the enzyme required to convert glucoraphanin → sulforaphane). Sulforaphane formation requires myrosinase activity, which is activated by cell disruption (chopping/chewing) AND requires intact myrosinase enzyme. Juicing at high speed may inactivate myrosinase. Additionally, cooking broccoli inactivates myrosinase. Gut microbiome can partially compensate (microbial myrosinase-like activity), but yield is lower.
- Evidence tier: Preclinical-Cell
- Mechanism: Sulforaphane inhibits class I and II HDACs in cell-line studies (typically at 5–30 µM concentrations). This is far above plasma concentrations achievable from dietary broccoli consumption (~0.1–1 µM). Additionally sulforaphane activates Nrf2 → HO-1, NQO1 — an antioxidant pathway that may indirectly affect chromatin through redox-sensitive histone acetyltransferases. No published CIC-DUX4 data.
- MHC-I upregulation: UNESTABLISHED at dietary concentrations. Mechanistically plausible via HDAC modulation but concentration mismatch is prohibitive.
- Evidence in CIC-DUX4: None direct.
- Chemo interaction: Nrf2 activation by sulforaphane at supplement doses (standardized extracts) is a theoretical concern for reducing ROS-dependent cytotoxicity of doxorubicin and ifosfamide. At culinary dietary intake (broccoli as a vegetable), this concern is considered subclinical by most oncology dietitian guidance, but high-dose sulforaphane supplements should be avoided during active ifosfamide therapy. [No direct citation for culinary broccoli + ifosfamide; concern extrapolated from Nrf2-pathway literature. Confirm with oncologist.]
- Preparation note: For maximum glucoraphanin-to-sulforaphane conversion: chop or blend raw broccoli sprouts, allow to stand 40 minutes at room temperature before consuming. Cooking eliminates myrosinase. Broccoli sprouts (3–5 days old) have 10–100x higher glucoraphanin content than mature broccoli [Fahey et al. 1997 Science PMID 9383826].

### EGCG (epigallocatechin-3-gallate, from green tea)

- Evidence tier: Preclinical-Cell
- Mechanism: Reported weak EZH2 inhibition (reduces H3K27me3) and DNMT inhibition in cell-line models, concentrations typically 10–50 µM. Oral bioavailability poor (≤5% of ingested dose as parent compound). Plasma concentrations from tea consumption typically 0.05–0.3 µM — 50–500x below cell-line active concentrations.
- MHC-I upregulation: No direct evidence even in cell lines.
- Evidence in CIC-DUX4: None.
- Chemo interaction: EGCG inhibits P-gp (preclinical); may increase vincristine/etoposide exposure. CYP3A4 modulation reported at high concentrations. At green tea beverage intake, clinical significance likely low, but supplement-form EGCG at high doses (>800 mg/day) raises hepatotoxicity concerns independent of chemo interaction. [Wang et al. P-gp review; FDA hepatotoxicity warning for high-dose EGCG supplements.] Consult oncologist before EGCG supplements during ifosfamide.

### Quercetin (apple skin — present in patient's juice)

- Evidence tier: Preclinical-Cell
- Mechanism: Weak EZH2 modulation reported in some cell lines; primary mechanisms are RTK/RAS inhibition (V1) and NF-κB modulation (V2). Epigenetic effects at achievable concentrations are marginal.
- Evidence in CIC-DUX4: None.
- Chemo interaction: CYP3A4 inhibition documented at higher quercetin concentrations; P-gp modulation. At juice-level intake (apple + vegetable juice), clinical significance low. Supplement-dose quercetin warrants caution with vincristine.

### Thymoquinone (from black cumin seed oil, Nigella sativa — patient's regimen)

- Evidence tier: Preclinical-Cell
- Mechanism: Thymoquinone has reported HDAC inhibitory activity and DNMT modulation in cell lines; also Nrf2 activation and NF-κB suppression. Concentrations required for epigenetic effects in cell-line studies (10–50 µM) exceed likely plasma concentrations from black seed oil consumption (estimated plasma Cmax <1 µM from typical supplemental doses — no robust human PK study confirmed as of knowledge cutoff). Tier is Preclinical-Cell; claims of epigenetic "hot-patching" at dietary doses would be overclaiming.
- V3 relevance: Weak epigenetic modulation is mechanistically plausible but unestablished at achievable human concentrations. Tag tier honestly: Preclinical-Cell, concentration-mismatch caveat applies.
- MHC-I upregulation: No evidence.
- Evidence in CIC-DUX4: None.
- Chemo interaction: Thymoquinone is a CYP3A4 inhibitor and CYP2C9 inhibitor in preclinical studies. This is potentially significant with ifosfamide (CYP3A4 activation) and may reduce ifosfamide bioactivation. Additionally, Nrf2 activation raises the same theoretical ROS-axis concern as sulforaphane during doxorubicin/ifosfamide. Consult oncologist before continuing black cumin seed oil during ifosfamide therapy. [Preclinical CYP data: Ahmed et al. 2017 Saudi Pharm J; no robust human PK CYP interaction study confirmed.]

### Vitamin D3 (patient's regimen — note on deficiency vs. replete supplementation)

- Evidence tier: Mechanistic (epigenetic axis); see Differentiation Therapy Specialist for the differentiation axis
- Mechanism (epigenetic component): VDR (vitamin D receptor) is a nuclear receptor that recruits chromatin remodeling complexes (SWI/SNF/BAF members, histone acetyltransferases) to VDR response elements. VDR activation can modulate DNA methylation at specific loci in some cell types. However, the primary differentiation/VDR axis is covered by the Differentiation Therapy Specialist.
- Evidence in CIC-DUX4: None.
- Priority for this specialist: Lower than differentiation specialist; defer epigenetic mechanistic detail to that output and focus on MHC-I pathway here (vitamin D has a separate immune modulation role covered in V4).

---

## MECHANISTIC OVERLAPS WITH DIFFERENTIATION THERAPY SPECIALIST

HDAC inhibitors (especially class I: entinostat) and EZH2 inhibitors (tazemetostat) both have dual effects: (1) epigenetic de-repression of tumor suppressors [this specialist's primary domain] AND (2) reactivation of differentiation programs [differentiation specialist's domain]. The V3 Lead should merge these entries into single entries in the v3-summary.md, preserving both mechanisms.

---

## FORWARD HYPOTHESES

[Forward Hypothesis 1] Sequential EZH2i → clinical HDACi pulsing to maximize MHC-I upregulation while minimizing adaptive resistance in CIC-rearranged sarcoma.

Hypothesis: EZH2 inhibition alone may be insufficient to fully de-repress MHC-I antigen presentation machinery (APM) in CIC-rearranged sarcoma because both H3K27me3 (reduced by EZH2i) and HDAC-mediated deacetylation contribute to APM silencing. Sequential treatment — EZH2i to reduce H3K27me3, followed by pulse HDACi (class-I selective) to hyperacetylate the newly accessible chromatin — may produce synergistic APM de-repression greater than either agent alone, thereby maximizing the V3→V4 immune bridge.

Mechanistic basis: Two orthogonal silencing mechanisms (H3K27me3 deposition by PRC2; histone deacetylation by HDAC1/2/3) act on overlapping gene sets including HLA-A/B/C, TAP1/2, beta-2-microglobulin, NLRC5. Removing both marks simultaneously (or sequentially) should produce additive or synergistic de-repression. This has been shown for tumor suppressor genes in Ewing sarcoma PDX models [no direct CIC-DUX4 citation; mechanism inferred from Sankar et al. 2014 PMID 24531741 EZH2i+HDACi in Ewing; Fillmore et al. 2015 PMID 25686801]. Not yet tested as an immune-priming (MHC-I upregulation) strategy specifically in CIC-rearranged sarcoma.

Study design to test: CIC-DUX4 cell line (e.g., NCC-CDS2-X1 if available) or PDX model treated with tazemetostat alone, entinostat alone, simultaneous combination, and sequential (tazemetostat 7 days → entinostat 3 days pulse) regimens. Primary endpoint: flow cytometric HLA-A/B/C surface expression + TAP1/TAP2 mRNA. Secondary: T-cell killing assay with co-cultured CIC-DUX4-antigen-specific T cells. Why not yet done: CIC-DUX4 cell line availability is limited; the combination has been studied in Ewing/synovial but not specifically as an MHC-I upregulation strategy in CIC-rearranged tumors.

[Forward Hypothesis 2] BETi-mediated PD-L1 suppression + EZH2i-mediated MHC-I upregulation as a tandem epigenetic immune-priming strategy upstream of checkpoint blockade, testable in CIC-rearranged sarcoma.

Hypothesis: CIC-DUX4 cells simultaneously downregulate MHC-I (immune evasion toward T-cells) and upregulate PD-L1 (checkpoint braking). These two mechanisms are maintained by distinct epigenetic programs: MHC-I silencing is PRC2/H3K27me3-dependent; PD-L1 upregulation is BRD4/super-enhancer-dependent. Combining EZH2i (restores MHC-I) with BETi (suppresses PD-L1) should simultaneously "un-hide" the tumor cell and "un-brake" the T-cell response — potentially synergizing with subsequent PD-1 checkpoint blockade in a three-drug epigenetic-immunotherapy sequence.

Mechanistic basis: BRD4 occupancy at CD274 (PD-L1) super-enhancer is documented in multiple tumor types; BETi reduces PD-L1 expression in preclinical models [Zenere et al. 2021; Ott et al. BETi+immune in solid tumors]. EZH2i MHC-I mechanism described above. The combination has been studied in melanoma and NSCLC preclinically, but not in CIC-rearranged sarcoma.

Study design: CIC-DUX4 PDX or humanized mouse model. Arm 1: tazemetostat alone. Arm 2: BETi alone. Arm 3: combination. Arm 4: combination + anti-PD-1. Endpoints: tumor volume, T-cell infiltration, MHC-I and PD-L1 surface expression on tumor cells, tumor-specific T-cell activity. Why not yet done: CIC-rearranged sarcoma is too rare for dedicated in vivo immunotherapy studies; no CIC-DUX4 syngeneic mouse model widely available.

---

## WHAT I COULD NOT ESTABLISH

1. Direct EZH2 dependency in CIC-DUX4 (as opposed to SMARCB1-null sarcomas): the extrapolation from epithelioid sarcoma is mechanistically defensible but not experimentally confirmed in CIC-DUX4 cell lines or patients. No published ChIP-seq study confirming H3K27me3 enrichment at specific loci in CIC-DUX4 tumors was identified.

2. Direct MHC-I status in CIC-DUX4 primary tumors: the claim that CIC-DUX4 cells are MHC-I-low is reported (doc 02-cic-sarcoma-knowledge.md) but I could not identify a peer-reviewed quantitative study of MHC-I surface expression in CIC-DUX4 vs. normal mesenchymal cells. This is a significant gap for V4 planning.

3. EMA tazemetostat current status: requires independent verification against EMA product database. I have flagged the uncertainty; I have not fabricated an EMA approval date.

4. AZD5153 NCT number: I declined to fabricate. Verify at ClinicalTrials.gov.

5. Dietary epigenetic modulators at tumor-relevant concentrations: none of the dietary compounds (sulforaphane, EGCG, quercetin, thymoquinone) achieve concentrations in the 10-50 µM range required for the epigenetic effects observed in cell-line studies. This is the single most important caveat for the dietary track.

6. Thymoquinone human PK data: no robust published human pharmacokinetic study for black cumin seed oil (thymoquinone) plasma concentrations was identified. CYP interaction data are from preclinical studies only.
