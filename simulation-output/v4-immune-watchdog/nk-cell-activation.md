# V4 NK Cell Specialist — NK Cell Activation Report

**Summary:** Maps NK cell missing-self detection biology, the mechanistic basis for NK targeting of MHC-I-low CIC-DUX4 cells, dietary modulation of NK function (vitamin D3 and zinc: deficiency-correction vs. replete-supplementation distinction mandatory), and the clinical IL-15 superagonist and NK engager pipeline; frames the NK-MHC-I paradox as the mechanistically strongest dietary lever in V4.

**Confidence: medium** — NK biology is well-established; vitamin D3 and NK function correlation is documented; the specific application to CIC-DUX4 cells is mechanistically inferred but lacks direct CIC-DUX4 NK killing assay data. Clinical NK cell pipeline is early-stage for solid tumours.

---

## PATIENT CONTEXT INTEGRATION

This patient has completed 14 cycles VDC/IE, surgery (>95% necrosis), WLI, achieved NED, and now has oligometastatic relapse (one lung lesion) prior to high-dose ifosfamide. NK-specific flags:

1. **Chemotherapy-induced NK depletion:** VDC/IE chemotherapy depletes NK cells. Recovery is expected by the current timepoint (NED May 2025, now May 2026) but quantification of current NK compartment is not available. High-dose ifosfamide (imminent) will deplete NK cells again; the post-ifosfamide NK reconstitution window is relevant.

2. **Post-WLI lung immune microenvironment:** WLI alters the pulmonary NK cell compartment. Lung-resident NK cells are reduced post-irradiation acutely; partial recovery expected. The relapsing lung lesion's NK surveillance context may be compromised by prior WLI.

3. **Vitamin D3 status in this patient:** Patient is self-administering vitamin D3. The critical question is whether the patient is correcting a genuine deficiency (evidence-based) or supplementing in a replete state (thin evidence for additional NK benefit). Current 25(OH)D level is not available in this case summary; the clinical recommendation is to check 25(OH)D serum level.

4. **mRNA team findings incorporated:** No persistent NK compartment alteration from BNT162b2 at this timepoint. No adjustment required from vaccine history.

---

## THE CORE MECHANISTIC ARGUMENT: NK MISSING-SELF AND CIC-DUX4

This is the conceptually strongest entry in V4's dietary/lifestyle track:

**The same MHC-I downregulation that CIC-DUX4 cells use to evade CD8+ T-cells makes them MORE visible to NK cells.**

NK cells operate via an activation/inhibition balance:
- **Inhibitory receptors** (KIR family: KIR2DL1/2/3, KIR3DL1/2; CD94/NKG2A heterodimer) recognise MHC-I (HLA-A/B/C, HLA-E). When MHC-I is present at normal levels, inhibitory signalling predominates → NK cell does NOT kill.
- **Activating receptors** (NKG2D/KLRK1, NKp30/NCR3, NKp44/NCR2, NKp46/NCR1, DNAM-1/CD226) recognise stress ligands (MICA, MICB, ULBP1-6 for NKG2D; B7-H6 for NKp30; PVR/CD155 and Nectin-2/CD112 for DNAM-1).
- When MHC-I is downregulated ("missing self"), inhibitory signalling is reduced → activation threshold lowered → NK cell kills IF activating ligands are also present.

**In CIC-DUX4:**
- MHC-I downregulation (via PRC2/H3K27me3 at APM loci) is the expected evasion mechanism for T-cells.
- This same MHC-I-low phenotype removes inhibitory KIR/NKG2A signalling from NK cells.
- CIC-DUX4 cells proliferating rapidly under oncogenic stress likely also upregulate stress ligands (MICA/MICB, ULBPs) — not directly confirmed in CIC-DUX4 specifically; extrapolated from fusion-driven sarcoma stress response literature.
- Net prediction: CIC-DUX4 cells should be NK-susceptible when the patient's NK compartment is functional.

Evidence tier: **Mechanistic** — no direct CIC-DUX4 NK killing assay data in the published literature. CIC-DUX4 direct evidence: None.

**Critical implication:** V3 epigenetic priming (EZH2i, HDACi) that restores MHC-I will PARTIALLY REDUCE NK vulnerability while INCREASING T-cell visibility. There is a mechanistic tension between V3→V4 T-cell bridge (restore MHC-I → T-cell killing) and NK cell killing (MHC-I low → NK killing). This tension should be surfaced for the orchestrator.

Optimal sequencing hypothesis: NK cell activation BEFORE V3 epigenetic MHC-I restoration; T-cell checkpoint activation AFTER. Alternatively: concurrent NK + checkpoint + epigenetic, accepting that epigenetic priming reduces NK pressure while enabling T-cell pressure.

---

## DIETARY TRACK

### Vitamin D3 — NK Cell Function

**Mechanism:** 1,25(OH)2D3 (calcitriol) acts via VDR expressed on NK cells. VDR signalling:
- Upregulates NKG2D (activating receptor) expression on NK cells [Arango et al., J Clin Immunol 2010, PMID 20862597 — NK subset study; no direct CIC-DUX4 data].
- Modulates NK cell cytotoxicity and cytokine production (IFN-γ).
- Supports maturation of NK cell precursors in bone marrow via VDR-dependent differentiation signals.

Evidence tier: **Mechanistic** (mechanism well-characterised) + **Clinical observational** (vitamin D deficiency associated with reduced NK activity in population studies; Supplement vs. replete distinction below).

**Deficiency correction vs. replete-supplementation:**
- **Correcting documented vitamin D deficiency (25(OH)D < 20 ng/mL):** Clear mechanistic basis. Restoring normal VDR signalling in NK cells is expected to restore normal NK cytotoxic function. Recommended: check 25(OH)D, correct deficiency if present.
- **Supplementation in vitamin D-replete individuals (25(OH)D > 30 ng/mL):** Evidence for additional NK benefit is thin. The VITAL trial (Manson et al., NEJM 2019, PMID 30415629) found no overall cancer incidence or mortality benefit from vitamin D3 2000 IU/day supplementation in a broad US population. NK-specific VITAL sub-analysis: not published for NK function outcomes.
- **Patient context:** Self-administering vitamin D3. Without current 25(OH)D level, cannot distinguish deficiency correction from replete-supplementation. **Clinical recommendation: check 25(OH)D level. If deficient, continue and correct. If replete, the NK benefit of additional supplementation is not established.**

Chemo interaction: No documented interaction between standard vitamin D supplemental doses (1000-4000 IU/day) and ifosfamide, vincristine, or other VDC/IE drugs. Hypercalcemia monitoring required at doses >4000 IU/day. No interaction found in DrugBank or NCCN integrative medicine guidelines at standard supplemental doses.

**Evidence in CIC-DUX4 specifically: None direct.**

### Zinc — NK Cell Development and Function

**Mechanism:** Zinc is required for NK cell maturation and function:
- Thymulin (zinc-dependent thymic hormone) supports lymphocyte maturation.
- Zinc deficiency impairs NK cell cytotoxicity, reduces NK cell numbers, and reduces natural cytotoxicity receptor expression [Shankar & Prasad, Am J Clin Nutr 1998, PMID 9537623].
- Zinc cofactor for metalloenzymes involved in NK cell perforin/granzyme pathway function.

Evidence tier: **Mechanistic** (zinc deficiency → NK impairment well-established) + **Preclinical** (zinc repletion in deficient animals restores NK activity).

**Deficiency correction vs. replete-supplementation:**
- Correcting zinc deficiency (serum Zn < 70 µg/dL): evidence-based NK support.
- Supplementation in replete individuals: no additional NK benefit documented. Excess zinc (>40 mg/day elemental zinc, the UL) suppresses copper absorption → secondary copper deficiency → risk of anaemia, neuropathy. Do not exceed UL without clinical indication.
- Patient: No explicit zinc supplementation mentioned in regimen, but juices (carrot, beetroot) provide dietary zinc at low levels. Check zinc status in the context of post-chemotherapy nutritional assessment.

Chemo interaction: No documented interaction between dietary/standard supplemental zinc and ifosfamide at normal intake. Excess zinc at very high doses may interfere with absorption of other minerals. Source: NCCN Integrative Medicine, DrugBank.

**Evidence in CIC-DUX4 specifically: None direct.**

### Omega-3 EPA/DHA — NK Activity (notable absence from patient regimen)

**Mechanism:** Omega-3 fatty acids (EPA/DHA) modulate NK cell activity:
- EPA/DHA alter lipid composition of NK cell membranes → affects receptor clustering and immune synapse formation.
- Some evidence that omega-3 supplementation increases NK cytotoxicity in healthy volunteers [Thies et al., Am J Clin Nutr 2001, PMID 11157327].
- Anti-inflammatory effects (via EPA→resolvin E, DHA→resolvin D/protectin) reduce immunosuppressive TME signalling.

Evidence tier: **Preclinical-Animal** + **Clinical observational** (healthy volunteer NK cytotoxicity data; no sarcoma-specific data).

**Patient note:** Omega-3 is ABSENT from this patient's regimen. This is a potential gap. The patient consumes fresh juices including sources with some ALA (plant omega-3), but ALA→EPA conversion is only ~5-10%. Marine EPA/DHA source is not mentioned. Adding fatty fish (sardines, mackerel) 2-3×/week provides EPA/DHA without supplement concerns.

Chemo interaction: Fish oil at high supplement doses (>3g/day EPA+DHA) has anti-platelet effect — relevant around surgery. At dietary fish intake levels: low concern. If fish oil supplement considered, discuss with oncologist given potential platelet effects during ifosfamide.

**Evidence in CIC-DUX4 specifically: None direct.**

---

## CLINICAL TRACK
### (Clinical / Experimental — not naturally achievable; for awareness only.)

### IL-15 / IL-15 Superagonist Pathway

IL-15 is the primary homeostatic cytokine for NK cell proliferation and survival. IL-15 superagonists (IL-15/IL-15Rα-Fc fusion proteins, also called "heterodimeric IL-15" or "hetIL-15") amplify NK cell expansion.

| Agent | Class | Status | Trial ID | Notes |
|---|---|---|---|---|
| N-803 (Nogapendekin alfa inbakicept) | IL-15 superagonist (IL-15N72D:IL-15Rα-Fc) | FDA approved 2023 for BCG-unresponsive non-muscle-invasive bladder cancer (in combination with BCG); investigation ongoing in solid tumours | NCT03055780 (bladder); multiple solid tumour trials | CIC-DUX4-specific data: None. Sarcoma-specific trials: Limited. Evidence tier: Established (bladder cancer); Clinical-Trial (other solid tumours) |
| ALT-803 (precursor to N-803) | IL-15 superagonist | Phase I/II completed; data published | NCT01946789; NCT02523469 | Evidence tier: Clinical-Trial |
| IL-15 (recombinant) | Native cytokine | Phase I dose-finding; limited by systemic toxicity | NCT01572493 | Evidence tier: Clinical-Trial; systemic IL-15 AE profile limits utility |

**Fusion tag: FUSION-AGNOSTIC** — IL-15 expands NK cells regardless of tumour fusion status.

**V3→V4 synergy opportunity:** IL-15 superagonist NK expansion + V3 epigenetic priming (maintain MHC-I-low via timing before EZH2i) could maximise NK killing of CIC-DUX4 MHC-I-low cells. After NK phase, EZH2i → MHC-I restoration → T-cell/checkpoint phase.

### NK Engager Bispecifics

NK engager bispecifics (NKCE, BiKE, TriKE) recruit NK cells to tumour cells by linking an NK activating receptor (NKG2D, NKp30, CD16) to a tumour-associated antigen (TAA).

| Agent | Format | Target (NK side / Tumour side) | Status | Notes |
|---|---|---|---|---|
| AFM13 | Tetravalent bispecific NK cell engager | CD30/CD16A | Clinical-Trial (NCT04074746, NK cell + AFM13) | Primarily haematological; CD30 not a CIC-DUX4 target |
| NKCE targeting EpCAM, HER2, etc. | Various | Various | Preclinical-Clinical | No CIC-DUX4-specific TAA-targeted NKCE published |
| GPC2-directed NK engager | NKG2D/GPC2 | Preclinical | GPC2 expressed in Ewing-like sarcomas; CIC-DUX4 GPC2 expression: unconfirmed | Evidence tier: Preclinical-Cell [no CIC-DUX4 specific data] |

**Key gap:** No NK engager bispecific targets an antigen specifically overexpressed in CIC-DUX4. ETV4/ETV5 overexpression is a hallmark but these are intracellular — not accessible to bispecifics. Surface antigens overexpressed in CIC-DUX4 are not well-catalogued.

**Fusion tag: FUSION-AGNOSTIC for any NK engager that does not target the junction peptide.**

### Adoptive NK Cell Transfer

- Haploidentical NK cell infusion (from donor) + cytokine support has been explored in AML and some solid tumours.
- Memory NK cells (adaptive NK cells, NKG2C+) are a distinct subset with higher persistence.
- No published CIC-DUX4 adoptive NK data.
- Evidence tier: **Clinical-Trial** for AML/haematological; **Preclinical** for solid tumours broadly.
- In the context of this patient's high-dose ifosfamide-induced lymphodepletion: the post-ifosfamide window creates a lymphodepleted background that could support adoptive NK cell engraftment (analogous to post-lymphodepletion CAR-T). This is an unexplored approach.

---

## FORWARD HYPOTHESES

**[Forward Hypothesis 1] Sequential NK cell activation (leveraging MHC-I-low CIC-DUX4 state) BEFORE epigenetic MHC-I restoration — a mechanistically optimal immune attack sequencing for CIC-rearranged sarcoma.**

Hypothesis: CIC-DUX4 tumours are MHC-I-low, making them NK-susceptible. Administering an NK cell activator (IL-15 superagonist N-803, or adoptive NK transfer) BEFORE EZH2i/HDACi priming maximises NK killing while tumour cells are maximally NK-visible. After NK cytoreduction, switch to V3 epigenetic priming (EZH2i → MHC-I restoration) + checkpoint blockade for T-cell killing of residual MHC-I-restored tumour cells. This "NK first, then T-cell" sequential immunotherapy could exploit both immune killing arms in parallel with the tumour's shifting MHC-I landscape.

Mechanistic basis: NK missing-self mechanism + MHC-I/T-cell mechanism are complementary and mechanistically opposed by the same tumour adaptation (MHC-I up/down). Sequential deployment (NK first in MHC-I-low phase; T-cell second in MHC-I-restored phase) could avoid the trade-off.

Study design: In a CIC-DUX4 PDX or humanised mouse model: (1) NK cell infusion or IL-15 days 1-14; (2) tazemetostat + anti-PD-1 days 15-35. Arms include each component alone and the full sequence. Primary endpoint: tumour volume, MHC-I dynamics (serial tumour biopsies at days 0, 14, 35), NK/T-cell infiltration. Why untested: The sequencing hypothesis requires both a humanised immune model and a CIC-DUX4 tumour model; neither is widely available; disease rarity.

**[Forward Hypothesis 2] Post-ifosfamide NK reconstitution kinetics as a determinant of oligometastatic response — monitoring NK cell absolute count and NKG2D expression at reconstitution as a predictive biomarker for subsequent IL-15 agonist response.**

Hypothesis: After high-dose ifosfamide, NK cells reconstitute from bone marrow progenitors. The quality of NK reconstitution (absolute NK count, NKG2D expression density, KIR repertoire) predicts the patient's capacity to mount NK-mediated surveillance against residual tumour cells. Patients with deficient NK reconstitution (absolute NK count <100/µL at day 42 post-ifosfamide, or NKG2D low) may benefit from IL-15 superagonist supplementation to boost reconstitution quality.

Mechanistic basis: IL-15 drives NK cell reconstitution post-lymphodepletion; lower NK counts at reconstitution predict inferior outcomes in AML post-SCT (Ruggeri et al., Science 2002, PMID 11786547 — NK reconstitution context, not ifosfamide/sarcoma). Translating NK reconstitution monitoring to the high-dose ifosfamide → oligometastatic sarcoma context is novel.

Study design: Prospective longitudinal cohort: NK absolute count, NKG2D expression, KIR repertoire at baseline, day 14, day 28, day 42, day 90 post-high-dose ifosfamide. Correlate with radiological response (oligometastatic lesion dynamics). Sub-study: IL-15 superagonist (N-803) in patients with deficient NK reconstitution (counts below predetermined threshold). Why untested: no dedicated NK reconstitution study post-high-dose ifosfamide in sarcoma exists.

---

## ATYPICAL-CASE NOTES

This patient is fusion-UNCONFIRMED (~5% subgroup).

ALL NK cell entries are FUSION-AGNOSTIC:
- NK missing-self killing: triggered by MHC-I downregulation regardless of upstream driver.
- Vitamin D3/zinc deficiency correction: supports NK function regardless of fusion status.
- IL-15 superagonist: expands NK cells regardless of tumour fusion status.
- NK engager bispecifics: fusion-agnostic unless targeting junction-specific antigen (none identified for CIC-DUX4).
- Adoptive NK transfer: fusion-agnostic.

The NK strategy is therefore fully applicable to this fusion-unconfirmed patient.

---

## WHAT I COULD NOT ESTABLISH

1. Direct NK killing assay data for CIC-DUX4 cell lines. Whether CIC-DUX4 cells are in fact NK-susceptible in vitro has not been published to the knowledge base used here. The mechanistic prediction is strong but direct experimental confirmation is absent.

2. Stress ligand (MICA/MICB, ULBP1-6) expression on CIC-DUX4 tumour cells. Missing-self alone is not sufficient for NK killing; activating ligands must also be present. CIC-DUX4-specific stress ligand expression profiling is not published.

3. This patient's current 25(OH)D level and NK compartment status. Both are required to grade the clinical relevance of vitamin D3 and post-chemotherapy NK reconstitution recommendations.

4. Whether high-dose ifosfamide produces qualitatively different NK reconstitution compared with standard VDC/IE. Ifosfamide-specific NK reconstitution kinetics are not documented in published sarcoma studies.

5. NK cell numbers and function in the lung-resident compartment post-WLI. Whether WLI has durably depleted or altered pulmonary NK cells at the current timepoint is unknown.

6. Omega-3 supplementation effect on NK cytotoxicity in cancer patients (not healthy volunteers). The Thies et al. healthy volunteer data are not transferable to post-chemotherapy cancer patients without study.
