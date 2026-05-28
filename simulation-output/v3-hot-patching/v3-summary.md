# Vector 3 — Hot Patching Summary

Summary: Maps clinical (epigenetic, differentiation, PROTAC/ASO, synthetic lethality) and dietary interventions aiming to restore tumor-suppressor signaling and differentiation in cells of CIC-rearranged sarcoma; includes the mandatory V3→V4 MHC-I bridge; explicitly separates dietary and clinical tracks; covers the fusion-unconfirmed (atypical) subgroup.

Confidence: medium — clinical track mechanisms are well-characterised in related fusion sarcomas (Ewing, epithelioid, synovial); direct CIC-DUX4 experimental data are sparse for most entries; dietary track contributions are adjunctive at best and are clearly marked as such.

Patient case context: Soft-tissue CIC-rearranged sarcoma, fusion-UNCONFIRMED subgroup (no confirmed CIC-DUX4/CIC-NUTM1/CIC-FOXO4 by genome sequencing). Primary biceps femoris, right thigh; 12 lung mets at diagnosis. Completed 14 cycles EURO EWING (VDC/IE); surgery Jan 2025 (>95% necrosis); radiation leg + whole-lung irradiation; NED May 2025–May 2026; oligometastatic relapse one lung lesion; NOW PREPARING HIGH-DOSE IFOSFAMIDE. The clinical track is the dominant part of V3 for this patient. Dietary track is adjunctive and must not be oversold.

Self-administered regimen assessment: see Dietary Track below for per-compound V3 evaluation.

---

## MHC-I UPREGULATION CANDIDATES
### (V3 → V4 Bridge — gate-clearing section for V4 lead and orchestrator)

V4 Wave 2 may proceed once this section is available. This section lists V3 interventions with documented or mechanistically grounded capacity to upregulate MHC-I (HLA-A/B/C) surface expression on tumor cells — the prerequisite for CD8+ T-cell recognition. NK cell strategies (V4) benefit from MHC-I-LOW states via complementary missing-self recognition; see V4 NK-cell section for the parallel framing.

### Clinical Track MHC-I Upregulation Candidates (primary V3→V4 bridge)

| Candidate | Class | MHC-I Mechanism | Evidence Tier | Fusion tag | V4 priority |
|---|---|---|---|---|---|
| Tazemetostat | EZH2/PRC2 inhibitor | Reduces H3K27me3 at HLA-A/B/C, TAP1, TAP2, B2M, NLRC5 promoters; restores antigen presentation machinery (APM) | Clinical-Trial (CIC context); Established (epithelioid sarcoma FDA 2020-01-23) | FUSION-AGNOSTIC | HIGH — cleanest V3→V4 bridge |
| Entinostat | Class I HDACi (HDAC1/2/3) | Histone hyperacetylation at APM gene promoters; upregulates NLRC5 (master MHC-I transactivator); de-represses TAP1/TAP2 | Clinical-Trial | FUSION-AGNOSTIC | HIGH — well-characterised MHC-I mechanism [Tong et al. 2020 PMID 32179131 context; no direct CIC-DUX4 data] |
| Vorinostat | Pan-HDACi (HDAC1/2/3/6) | Same APM de-repression; broader class; higher toxicity profile | Established (CTCL FDA/EMA); Clinical-Trial (sarcoma) | FUSION-AGNOSTIC | MEDIUM — toxicity concern with concurrent ifosfamide |
| OTX015 / BETi | BRD4 inhibitor | Reduces PD-L1 super-enhancer occupancy → lower PD-L1; indirect benefit to T-cell access; MHC-I upregulation weaker than EZH2i/HDACi | Clinical-Trial | FUSION-AGNOSTIC | MEDIUM — PD-L1 suppression is stronger V3→V4 signal here than MHC-I |
| Azacitidine / Decitabine | DNMTi | ERV demethylation → cytosolic dsRNA → STING pathway → type I IFN → MHC-I upregulation (viral mimicry); also direct CpG demethylation at HLA loci [Chiappinelli et al. 2015 Cell; Roulois et al. 2015 Cell — no direct CIC-DUX4 data] | Established (MDS/AML FDA/EMA); Clinical-Trial (solid tumor) | FUSION-AGNOSTIC | MEDIUM — distinct immunostimulatory path via STING |

### Dietary Track MHC-I Upregulation (adjunctive — unestablished at achievable concentrations)

| Candidate | Mechanism | Evidence Tier | Critical caveat |
|---|---|---|---|
| Sulforaphane (broccoli) | Weak class-I HDACi at 5–30 µM in cell lines | Preclinical-Cell | WHETHER DIETARY SULFORAPHANE ACHIEVES SUFFICIENT TUMOR EXPOSURE FOR MHC-I UPREGULATION: UNESTABLISHED. Patient juicing broccoli — juicing likely inactivates myrosinase, reducing sulforaphane yield further. Do not equate with clinical HDACi in V4 planning. |
| Butyrate (fermented fiber) | HDACi at mM colonic concentrations; systemic exposure far lower | Preclinical | Same caveat: systemic butyrate from dietary fiber does not reach soft-tissue sarcoma tumor sites at MHC-I-upregulating concentrations. UNESTABLISHED. |

**Key message for V4 lead:** Build V4 planning around tazemetostat and entinostat as the V3→V4 clinical bridge. Dietary entries are listed for completeness but must not be relied upon as MHC-I upregulators at clinically meaningful levels.

---

## RANKED CANDIDATE LIST

Ranking criteria: Evidence tier first, then mechanistic alignment with CIC-DUX4 biology, then cross-vector synergy, then safety/feasibility.

| Rank | Compound/Intervention | Layer | Mechanism (molecular) | Tier | CIC-DUX4 direct? | Cross-vector | Citation/source |
|---|---|---|---|---|---|---|---|
| 1 | Tazemetostat (EZH2i) | Epigenetic — PRC2/H3K27me3 | EZH2 inhibition → H3K27me3 reduction at tumor suppressor and APM gene loci → de-repression of CDKN2A, MHC-I, differentiation genes | Clinical-Trial (CIC); Established (epithelioid sarcoma FDA 2020-01-23) | Indirect (extrapolated from BAF-disrupted fusion sarcomas; CDKN2A co-deletion supports H3K27me3 activity in CIC-DUX4) | V3→V4 MHC-I bridge; V3 differentiation | NCT01897571 (pivotal); EMA status: verify independently |
| 2 | Entinostat (class I HDACi) | Epigenetic — H3K27ac/deacetylation | HDAC1/2/3 inhibition → histone H3/H4 hyperacetylation at APM and tumor suppressor promoters → MHC-I restoration, CDKN1A/p21 upregulation | Clinical-Trial | None direct | V3→V4 MHC-I bridge; combination with EZH2i | NCT02890069 (entinostat + pembrolizumab sarcoma); NCT01253278 (Ewing) |
| 3 | OTX015 / Birabresib (BETi) | Epigenetic — BRD4/super-enhancer | BRD4 bromodomain inhibition → collapse of ETS super-enhancers → reduced ETV4, ETV5, MYC, CCND1 transcription even in presence of fusion protein | Clinical-Trial | None direct (BET preclinical data in related fusion sarcomas; CIC-DUX4 cell line data limited — verify Yoshimoto 2017) | V1 BRD4 throttle; V3→V4 PD-L1 suppression | NCT01713582; NCT02419417 |
| 4 | Palbociclib / Ribociclib / Abemaciclib (CDK4/6i) | Cell cycle — Rb/E2F | CDK4/6 inhibition → Rb hypophosphorylation → E2F suppression → G1 arrest; targets downstream execution of ETS→CCND1→CDK4 axis | Established (breast cancer FDA/EMA 2015-2018); Clinical-Trial (sarcoma) | None direct (downstream pathway mechanistically predicted) | V1 CDK4/CCND1 overlap | NCT03677388; NCT02571829; NCT02664909 |
| 5 | Azacitidine / Decitabine (DNMTi) | Epigenetic — DNA methylation | DNMT inhibition → CpG demethylation at silenced loci + ERV demethylation → STING-mediated type I IFN → MHC-I | Established (MDS/AML FDA/EMA); Clinical-Trial (solid tumors) | None direct | V3→V4 viral mimicry/STING bridge | Chiappinelli 2015 Cell; Roulois 2015 Cell |
| 6 | ATRA (differentiation, APL model) | Differentiation — nuclear receptor | In APL: RAR alpha activation → co-repressor displacement → terminal granulocyte differentiation. In CIC-DUX4: indirect — wild-type RAR signaling may modulate mesenchymal differentiation genes; direct mechanism does not transfer from APL | Established (APL FDA/EMA); Theoretical (CIC-DUX4) | None direct; extrapolation poorly supported | V3 differentiation | FDA: tretinoin approved for APL; not for sarcoma |
| 7 | Vitamin D3 / calcitriol (VDR axis) | Differentiation — VDR/nuclear receptor | Calcitriol-VDR-RXR complex binds VDREs → upregulates CDKN1A/p21, CDKN1B/p27 → partial cell-cycle exit in some mesenchymal cell types; also modulates NK cell function (V4) | Mechanistic | None direct | V3 differentiation; V4 NK axis | [No direct CIC-DUX4 citation; mechanism inferred from mesenchymal cell VDR biology; VITAL trial for general cancer effect null] |
| 8 | BET PROTACs (ARV-771 / ARV-825) | Epigenetic — BRD4 degradation | CRBN-mediated proteasomal BRD4 degradation; more complete target depletion than BETi; potentially overcomes BETi resistance | Preclinical-Animal (prostate PDX Raina 2016 PMID 27528661); Clinical-Trial (ARV-825 NCT03328078) | None direct in CIC-DUX4 | V3 BRD4 axis | Raina et al. 2016 PNAS PMID 27528661 |
| 9 | EZH2 PROTACs (MS1943) | Epigenetic — EZH2 degradation | CRBN-mediated EZH2 degradation; may overcome EZH2-inhibitor resistance | Preclinical-Cell (TNBC Yu et al. 2021 Nat Chem Biol PMID 33349709) | None direct | V3 PRC2 axis | Yu et al. 2021 PMID 33349709 |
| 10 | Sulforaphane (dietary, broccoli sprouts) | Epigenetic — weak HDACi | HDAC class I/II inhibition at 5–30 µM (cell lines); Nrf2 activation via Keap1-Cys151 adduct at dietary doses | Preclinical-Cell | None direct | V1 (Nrf2/ROS); V3 MHC-I (UNESTABLISHED at dietary doses); V4 weak | Fahey et al. 1997 Science PMID 9383826 (glucoraphanin content); [HDACi: no direct CIC-DUX4 citation] |

---

## DIETARY TRACK

Note: Dietary contributions to V3 are the weakest part of this vector. Every dietary compound below faces a critical concentration mismatch — the concentrations required for epigenetic or differentiation effects in cell lines are not achievable in tumor tissue at dietary intake levels. Present these as adjunctive background, not as primary interventions.

| Compound | Patient's regimen? | V3 mechanism | Tier | Concentration caveat | Chemo interaction |
|---|---|---|---|---|---|
| Sulforaphane (broccoli) | Yes (broccoli juice — myrosinase issue) | Weak HDAC class I inhibition at 5–30 µM; Nrf2 activation | Preclinical-Cell | Dietary tumor exposure: UNESTABLISHED; juicing inactivates myrosinase → reduced sulforaphane yield | Nrf2 activation at supplement doses: theoretical ROS-axis interference with doxorubicin/ifosfamide. At culinary whole-food intake: risk considered subclinical. Supplement-form sulforaphane: avoid during active ifosfamide without oncologist approval. |
| Beta-carotene (carrot juice) | Yes | Retinoid precursor → RA synthesis via BCO1; RAR activation → differentiation gene modulation | Dietary-Observational; Mechanistic | Whole-food dietary dose: insufficient for clinical differentiation effect | BETA-CAROTENE SUPPLEMENTS (≥20 mg/day): CONTRAINDICATED — ATBC/CARET signal (↑lung cancer incidence in smokers; general caution in oncology). Whole-food carrot juice at culinary intake: not contraindicated on current evidence. |
| Vitamin D3 | Yes (self-administered) | Calcitriol → VDR → CDKN1A/p21 upregulation, partial G1 arrest in mesenchymal cells; also NK function (V4) | Mechanistic | Differentiation effect at deficiency-correction doses: modest; replete-supplementation benefit: thin (VITAL trial null for cancer) | Typical supplemental dose (1000–4000 IU/day): no documented PK interaction with ifosfamide/vincristine. Hypercalcemia monitoring required. Consult oncologist. |
| EGCG (green tea) | Not listed (patient drinks juices, not green tea) | Weak EZH2 inhibition, weak HDAC modulation at 10–50 µM cell lines | Preclinical-Cell | Dietary plasma Cmax ≤0.3 µM — 30-150x below active range | P-gp inhibition (preclinical): potential increase in vincristine/etoposide CNS exposure. At beverage intake: risk low. Supplement-form EGCG (>400 mg/day): hepatotoxicity risk + P-gp interaction; avoid during vincristine. |
| Quercetin (apple skin, limited in juice) | Yes (apple juice — quercetin in skin, partially lost in juicing) | Very weak EZH2 modulation; primarily V1/V2 | Preclinical-Cell | Juicing removes most quercetin (in skin); dietary plasma concentrations subclinical for epigenetic effect | CYP3A4 inhibition at high quercetin supplement doses: potential vincristine exposure increase. At juice-level intake: risk considered low. |
| Thymoquinone (black cumin seed oil) | Yes | Reported weak HDAC modulation, Nrf2 activation at 10–50 µM in cell lines; no robust differentiation mechanism | Preclinical-Cell | No robust human PK data; estimated plasma Cmax <<1 µM from typical supplemental dose | CYP3A4 and CYP2C9 inhibitor (preclinical data — Ahmed et al. 2017 Saudi Pharm J): potentially reduces ifosfamide bioactivation via CYP3A4; also Nrf2-mediated ROS-axis concern. FLAG: discuss with oncologist whether to continue black cumin seed oil during high-dose ifosfamide. |
| Butyrate (fermented fiber — limited from juicing) | Indirect (juicing removes most fiber) | HDACi at mM colonic concentrations; systemic exposure far lower | Preclinical | Soft-tissue/lung tumor site not exposed to colonic butyrate concentrations | No documented SOC interaction at dietary levels. |
| Curcumin + piperine | Yes | BRD4 chromatin disruption reported at 5–20 µM curcumin (cell lines); piperine increases curcumin absorption (Shoba et al. 1998 Planta Med, n=10, single dose, control below LOD — directional finding, "2000% boost" cited with caveat, NOT a universal multiplier) | Preclinical-Cell | Even with piperine-enhanced absorption, plasma curcumin from dietary turmeric is far below cell-line active concentrations | CYP3A4 inhibition (curcumin at high doses); P-gp modulation (piperine). At dietary turmeric + black pepper in food: risk considered subclinical. Curcumin supplements: CYP3A4 concern with vincristine/etoposide; consult oncologist. |

### Patient regimen items with no V3 mechanism

| Item | Assessment |
|---|---|
| Liposomal vitamin C | No V3 (epigenetic/differentiation) mechanism established. V2 ROS axis only. High-dose IV vitamin C is a distinct clinical intervention; liposomal oral form is intermediate. ROS-axis concern with doxorubicin/ifosfamide at high doses — consult oncologist. |
| Honey | No V3 mechanism. Not relevant to hot patching. |
| Beetroot juice | No V3 mechanism. Vascular/NO pathway only. Not V3-relevant. |
| Ginger | No V3 mechanism. Anti-inflammatory (V2) classification. Not V3-relevant. |
| Celery juice | Apigenin (weak ETS expression modulation, V1 classification). No meaningful V3 epigenetic/differentiation effect at culinary dose. |

---

## CLINICAL TRACK
### (For Oncologist Discussion Only — not naturally achievable)

**Tag: Clinical / Experimental — not naturally achievable; for awareness only.**

### Most actionable clinical interventions for this patient (imminent high-dose ifosfamide context)

The clinical track is where V3 has genuine potential. Given imminent high-dose ifosfamide:

**Priority discussion items with oncologist:**

1. Tazemetostat timing: Could be discussed as maintenance or consolidation post-ifosfamide response, not concurrent (CYP3A4 interaction concern; marrow sparing during active ifosfamide). The EZH2i + checkpoint inhibitor combination (NCT04196738 type trials — verify current status) is the most mechanistically compelling downstream sequence.

2. CDK4/6 inhibitors: Palbociclib/ribociclib/abemaciclib are potentially relevant post-ifosfamide. The CDK4/CCND1 axis is directly downstream of CIC-DUX4 ETS signaling. Safety concern: additive myelosuppression with ifosfamide. Discuss sequential scheduling. NCT03677388.

3. BET inhibitor enrollment: If ifosfamide produces a response and disease remains oligometastatic, enrollment on a BETi trial (OTX015, BMS-986158) or BETi + checkpoint inhibitor combination trial is worth exploring. BRD4 addiction is the most mechanistically robust entry point for CIC-DUX4.

4. CRISPR/long-read sequencing to identify junction: If fusion-unconfirmed status persists, targeted re-sequencing of archived tumor specimen (long-read WGS + RNAseq splice-junction analysis) could identify the driver event and open junction-specific approaches currently unavailable.

### Clinical trial landscape summary

| Intervention | Mechanism | Development stage | Key trial IDs | Fusion tag |
|---|---|---|---|---|
| Tazemetostat | EZH2i | Approved (epithelioid); Phase I/II others | NCT01897571, NCT02601950 | FUSION-AGNOSTIC |
| Valemetostat | EZH1/2i | Phase I/II | NCT04703192 | FUSION-AGNOSTIC |
| MAK683 | EED inhibitor | Phase I/II | NCT02900651 | FUSION-AGNOSTIC |
| OTX015 / birabresib | BETi | Phase I/II | NCT01713582 | FUSION-AGNOSTIC |
| BMS-986158 | BETi | Phase I/II | NCT02419417 | FUSION-AGNOSTIC |
| AZD5153 | Bivalent BETi | Phase I | Verify at ClinicalTrials.gov | FUSION-AGNOSTIC |
| Palbociclib | CDK4/6i | Approved (breast); sarcoma trial | NCT03677388 | FUSION-AGNOSTIC |
| Ribociclib | CDK4/6i | Approved (breast); sarcoma trial | NCT02571829 | FUSION-AGNOSTIC |
| Abemaciclib | CDK4/6i | Approved (breast); sarcoma trial | NCT02664909 | FUSION-AGNOSTIC |
| SY-5609 | CDK7i | Phase I | NCT04247126 | FUSION-AGNOSTIC |
| AZD4573 | CDK9i | Phase I | NCT03754530 | FUSION-AGNOSTIC |
| ARV-825 | BET PROTAC | Phase I | NCT03328078 — verify | FUSION-AGNOSTIC |
| CIC-DUX4 junction ASO | ASO, junction-specific | NONE CLINICAL STAGE | — | FUSION-CONFIRMED ONLY — POSSIBLY INAPPLICABLE (no confirmed junction) |
| CIC-DUX4 fusion PROTAC | PROTAC, junction-specific | NONE PUBLISHED | — | FUSION-CONFIRMED ONLY — POSSIBLY INAPPLICABLE |
| Elimusertib / berzosertib | ATRi | Phase I/II | NCT03188965; NCT02278110 | FUSION-AGNOSTIC |

---

## CROSS-VECTOR FLAGS

Compounds the V1, V2, and V4 leads should also see:

| Compound | V3 role | Cross-vector relevance |
|---|---|---|
| Tazemetostat | EZH2i — primary V3→V4 bridge | V4: MHC-I upregulation enables T-cell killing; V4 NK: EZH2i reduces immune evasion |
| BETi (OTX015 etc.) | BRD4/super-enhancer collapse | V1: overlaps BRD4 throttle (same target, clinical-grade effect vs. dietary effect); V4: PD-L1 suppression |
| Palbociclib/CDK4/6i | G1 arrest via Rb/E2F | V1: overlaps CDK4/CCND1 axis (same downstream target) |
| Sulforaphane | Weak HDACi / Nrf2 | V1 (Nrf2 ROS); V4 (MHC-I UNESTABLISHED) — cross-vector compound, but dietary concentration caveat applies to all three vectors |
| Vitamin D3 | VDR differentiation | V4: NK cell function modulation; V2: immune baseline |
| Curcumin + piperine | Weak BRD4 disruption | V1 BRD4/super-enhancer (same target, dietary doses insufficient for same mechanism as BETi); chemo interaction flags shared across all vectors |
| Beta-carotene (carrot) | Retinoid precursor | V2: antioxidant caution; ATBC/CARET supplement caveat shared |

---

## FORWARD HYPOTHESES

[Forward Hypothesis 1] Sequential EZH2i → class-I HDACi pulsing to maximize MHC-I upregulation and V3→V4 bridge efficacy in CIC-rearranged sarcoma.

Hypothesis: EZH2 inhibition reduces H3K27me3 at APM loci; subsequent class-I HDACi pulse (entinostat) hyperacetylates the newly accessible chromatin at those loci, producing synergistic APM de-repression (HLA-A/B/C, TAP1, TAP2, NLRC5) exceeding either agent alone. This would maximize the V3→V4 bridge for checkpoint immunotherapy sequencing.

Mechanistic basis: H3K27me3 and HDAC-mediated deacetylation are orthogonal silencing mechanisms acting on overlapping APM gene sets. Sequential de-repression of both marks is analogous to azacitidine + entinostat synergy in AML [no direct CIC-DUX4 citation; inferred from Sankar et al. 2014 Ewing sarcoma EZH2i+HDACi PMID 24531741 context]. Not yet tested as MHC-I upregulation strategy in CIC-rearranged sarcoma.

Study design: CIC-DUX4 cell line or PDX. Arms: tazemetostat alone, entinostat alone, simultaneous, sequential (tazemetostat 7 days → entinostat 3-day pulse). Primary endpoint: HLA-A/B/C surface expression (flow cytometry) + TAP1/TAP2 mRNA. Secondary: co-culture T-cell killing assay with CIC-DUX4-antigen-specific T cells. Why not yet done: CIC-DUX4-specific MHC-I studies not published; combination studied in Ewing/synovial but not as immune-priming strategy specifically.

[Forward Hypothesis 2] BETi-mediated PD-L1 suppression + EZH2i-mediated MHC-I upregulation as tandem epigenetic immune-priming upstream of checkpoint blockade in CIC-rearranged sarcoma.

Hypothesis: CIC-DUX4 cells simultaneously downregulate MHC-I (PRC2-dependent) and upregulate PD-L1 (BRD4-super-enhancer-dependent). EZH2i + BETi addresses both evasion mechanisms simultaneously: restores visibility (MHC-I up) and removes the braking signal (PD-L1 down) — maximizing the probability that subsequent PD-1 blockade produces a T-cell response. The three-drug epigenetic-immunotherapy sequence (EZH2i + BETi + anti-PD-1) has not been tested in CIC-rearranged sarcoma.

Mechanistic basis: BRD4 super-enhancer at CD274 (PD-L1) locus documented in multiple tumor types [Zenere 2021 context; no CIC-DUX4 data]; EZH2i MHC-I mechanism described above. Orthogonal mechanisms with additive immune-enabling effect.

Study design: CIC-DUX4 PDX or humanized mouse model. Arms: tazemetostat; OTX015; combination; combination + anti-PD-1. Endpoints: tumor volume, T-cell infiltration, MHC-I/PD-L1 expression on tumor cells. Why not yet done: no CIC-DUX4 syngeneic or humanized mouse model widely available; disease rarity.

[Forward Hypothesis 3] Long-read WGS + RNA-seq splice junction re-analysis of this patient's archived tumor specimen to identify the cryptic driver event, converting fusion-agnostic to fusion-specific treatment strategy.

Hypothesis: This patient's "fusion-unconfirmed" status may reflect short-read WGS limitations at the DUX4-containing subtelomeric repeat arrays (4q35, 10q26), which are notoriously difficult to characterize by standard sequencing. Long-read WGS (Oxford Nanopore or PacBio HiFi) and RNA-seq junction analysis may identify the true driver, unlocking junction-specific ASO and PROTAC approaches currently classified as POSSIBLY INAPPLICABLE.

Mechanistic basis: DUX4 repeat-array loci require read lengths of >10 kb to span the repeat region and confirm junction breakpoints. Multiple published case studies in FSHD have demonstrated that long-read sequencing resolves DUX4 repeat variants that short-read sequencing misses. Applying the same technology to archived tumor material is technically feasible.

Study design: Re-analysis of archived FFPE or frozen tumor specimen. Primary endpoint: identification of any fusion transcript involving CIC or a related HMG-box TF. This is a diagnostic intervention, not a therapeutic hypothesis per se — but its outcome directly changes the therapeutic option set.

[Forward Hypothesis 4] BETi pre-treatment → ifosfamide sequencing to exploit BETi-mediated DDR super-enhancer collapse for alkylating agent sensitization, testable in the current clinical context.

Hypothesis: BRD4 occupancy at DDR gene super-enhancers (RAD51, BRCA2-pathway genes) maintains elevated HR capacity in CIC-DUX4 cells. Brief BETi pre-treatment (48–72h before ifosfamide infusion) collapses these DDR super-enhancers, transiently reducing HR-mediated repair of ifosfamide-induced DNA crosslinks, thereby sensitizing tumor cells to the scheduled ifosfamide course. Normal marrow cells have lower BRD4 super-enhancer dependency at DDR loci and may be less sensitized.

Mechanistic basis: BETi-mediated HR impairment via DDR super-enhancer collapse has been published in BRCA-wild-type cancer cell lines [Qiu et al. 2015 Cancer Cell context — no CIC-DUX4-specific data]. This patient has ifosfamide already scheduled; a window-of-opportunity BETi pre-treatment design (3-day BETi → ifosfamide start) is logistically feasible if a BETi with adequate safety data (OTX015 Phase I complete) were available.

Study design: Pilot window-of-opportunity trial design: OTX015 (or BMS-986158) days 1–3; high-dose ifosfamide day 4–8. Primary endpoint: gamma-H2AX in sequential biopsies (or circulating tumor DNA clearance as proxy). Why not yet done: the sequencing hypothesis is novel; the clinical logistics require coordination; no CIC-DUX4 DDR ChIP-seq data to confirm DDR super-enhancer dependency in this histotype.

---

## ATYPICAL-CASE NOTES

This patient is in the fusion-unconfirmed (~5%) subgroup. Impacts on each entry:

FUSION-CONFIRMED ONLY entries (POSSIBLY INAPPLICABLE to this patient):
- CIC-DUX4 junction-targeting ASOs: require confirmed junction sequence. None published clinically even for confirmed cases.
- CIC-DUX4 fusion protein-targeting PROTACs: require confirmed junction. None published.
- Any junction-specific neoantigen vaccine or CAR-T (V4 scope, but noted here for completeness).

FUSION-AGNOSTIC entries (applicable to this patient):
All clinical agents in this summary (tazemetostat/EZH2i, entinostat/HDACi, OTX015/BETi, palbociclib/CDK4/6i, azacitidine/DNMTi, ATRA, CDK7i/CDK9i, ATRi, all PROTACs targeting BRD4/EZH2).
Rationale: These target the downstream epigenetic amplification machinery and cell cycle execution machinery. This machinery is active in CIC-rearranged sarcoma based on shared transcriptional features, regardless of which upstream fusion drives it. If no fusion is confirmed, PRC2 activity (as evidenced by CDKN2A deletion), BRD4/super-enhancer activity (as evidenced by ETS factor overexpression), and CDK4/CCND1 upregulation remain mechanistically expected in cells with the CIC-rearranged sarcoma phenotype.

All dietary entries in this summary are FUSION-AGNOSTIC.

---

## RECONCILIATION NOTES
### (Merged entries from sub-agents)

- Tazemetostat: Appears in both Epigenetic Therapy Specialist (EZH2i mechanism) and PROTAC/ASO Specialist (clinical trial landscape). Merged into single entry; FDA/EMA status from epigenetic file; trial IDs from PROTAC/ASO file.
- EZH2i + HDACi combination: Mechanistic overlap flagged by both Epigenetic and Differentiation specialists. Merged into Forward Hypothesis 1.
- BET inhibitors (OTX015, BMS-986158, AZD5153): Appeared in both Epigenetic Therapy Specialist (super-enhancer collapse) and Synthetic Lethality Specialist (BRD4 addiction). Merged; both mechanisms preserved.
- CDK4/6 inhibitors: Appeared in both Synthetic Lethality Specialist (CDK4/CCND1 dependency) and PROTAC/ASO Specialist (clinical trial landscape). Merged.
- Sulforaphane: Appeared in Epigenetic (weak HDACi) and Differentiation (weak differentiation signal). Merged under dietary track with cross-vector flags. Both mechanisms retained; concentration caveat applies to both.
- Vitamin D3: Appeared in Epigenetic (VDR/chromatin) and Differentiation (calcitriol/VDR differentiation axis). Merged; differentiation mechanism is primary for V3; epigenetic mechanism is secondary. V4 NK-axis flagged.

No irreconcilable conflicts between specialist outputs. Where mechanisms overlapped, both were retained in the merged entry.

---

## WHAT I COULD NOT ESTABLISH

1. Direct EZH2 dependency validation in a CIC-DUX4-specific model (ChIP-seq, tazemetostat sensitivity assay). All EZH2i rationale rests on extrapolation from SMARCB1-null epithelioid sarcoma and related BAF-disrupted sarcomas.

2. Direct MHC-I surface expression quantification in CIC-DUX4 tumors vs. matched controls. The claim that CIC-DUX4 cells are MHC-I-low is mechanistically expected and reported clinically, but a published quantitative study confirming this in CIC-DUX4-specific material was not identified.

3. Published clinical-stage ASO or PROTAC targeting the CIC-DUX4 junction. None exists in the published literature.

4. Yoshimoto 2017 BETi CIC-DUX4 cell line data: PMID not independently verified; confirm at PubMed before citing in downstream work.

5. AZD5153 registered trial NCT ID: not fabricated; confirm at ClinicalTrials.gov by searching "AZD5153."

6. Tazemetostat current EMA marketing authorisation: requires independent verification against EMA product database. FDA accelerated approval (2020-01-23, epithelioid sarcoma) is confirmed; EMA status is not.

7. Whether any dietary compound achieves V3-relevant (epigenetic or differentiation) effects at concentrations achievable in tumor tissue from dietary or supplemental intake. For all dietary entries, this remains unestablished.

8. CRISPR dependency screen data in CIC-DUX4 cell lines. Not available in public DepMap as of knowledge cutoff; direct CIC-DUX4-specific screens not published.

9. BCO1 conversion efficiency (beta-carotene → retinol) in this specific patient: genetically variable, not testable without pharmacogenomic data.

10. VDR expression status in CIC-DUX4 tumors: not published. If VDR is epigenetically silenced, calcitriol-driven differentiation requires prior EZH2i to de-repress VDR first.
