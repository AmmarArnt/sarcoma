# Vector 3 — Hot Patching Summary (v2)

**Summary:** Maps clinical-experimental (epigenetic, differentiation, PROTAC/ASO, synthetic-lethality) and dietary interventions that target the break-condition restoration, chromatin reprogramming, and forced-differentiation axes in cells carrying a CIC-rearrangement. TAZEMETOSTAT IS WITHDRAWN FROM ALL MARKETS AS OF 2026-03-09 — the EZH2-inhibition MECHANISM is preserved; the agent is rerouted to valemetostat and MAK683. Fusion-junction ASOs and fusion-specific PROTACs are flagged POSSIBLY INAPPLICABLE (fusion-unconfirmed patient). Dietary track is adjunctive only. Clinical track is for oncologist discussion — not a treatment plan.

**Confidence:** Medium — Clinical-track mechanisms are well-characterised in related fusion-driven sarcomas (Ewing, epithelioid, synovial); direct CIC-DUX4 experimental data are sparse for most entries; dietary contributions face severe in-vivo concentration mismatches. Three-axis scoring applied per ADR-0004.

**Patient case context (clean-slate — no stored personal memory):** Soft-tissue CIC-rearranged sarcoma, diagnosis June 2024. FUSION-UNCONFIRMED atypical subgroup (~5%). Primary: biceps femoris right thigh. 12 lung mets at diagnosis. EURO EWING (VDC/IE) ×14 cycles; surgery Jan 2025 (>95% necrosis); radiation to leg + whole-lung irradiation. NED May 2025–May 2026. Oligometastatic relapse (one lung lesion) May 2026. NOW PREPARING HIGH-DOSE IFOSFAMIDE. CDK4/6i additive myelosuppression flag active; tazemetostat withdrawal flag active.

**Not medical advice. Research simulation only.**

---

## MHC-I UPREGULATION CANDIDATES
### (V3 → V4 Bridge — Gate-Clearing Section for V4 Lead and Orchestrator)

V4 Wave 2 may proceed once this section is on disk. This section lists V3 interventions with documented or mechanistically grounded capacity to upregulate MHC-I (HLA-A/B/C) and/or antigen presentation machinery (APM: TAP1, TAP2, B2M, NLRC5) on tumor cells. That upregulation is the prerequisite for CD8+ T-cell recognition. NK strategies (V4) are complementary — NK cells exploit MHC-I-LOW states via missing-self logic; see V4.

### CRITICAL TAZEMETOSTAT STATUS UPDATE (live-verified 2026-06-03)

**TAZEMETOSTAT (TAZVERIK) — WITHDRAWN FROM ALL MARKETS 2026-03-09.**

Source: Ipsen press release 2026-03-09; FDA Drug Alert (FDA.gov/drugs, accessed 2026-06-03). Reason: SYMPHONY-1 trial IDMC advisory — 18/318 (5.7%) tazemetostat-arm patients developed hematologic secondary primary malignancies vs. 0 in the control arm; 3 deaths. Ipsen voluntarily withdrew all indications (follicular lymphoma and epithelioid sarcoma) from all Ipsen markets, including the US FDA-accelerated-approval indication (granted 2020-01-23 for epithelioid sarcoma). **EMA status: tazemetostat did NOT hold EMA marketing authorisation prior to withdrawal — it held orphan drug designation in the EU for epithelioid sarcoma and related conditions but was not centrally approved by EMA for any indication (confirmed via search of EMA medicines database, 2026-06-03).** Therefore the v1 claim "Established (epithelioid sarcoma FDA 2020-01-23)" is now moot: the FDA accelerated approval is withdrawn, and there was no EMA approval to lose.

**V3 v2 action:** The EZH2-inhibition MECHANISM (H3K27me3 reduction → APM de-repression → MHC-I upregulation) remains biologically valid and is the strongest V3→V4 bridge available. The agent is rerouted. Tazemetostat is listed in the MHC-I table only as WITHDRAWN/DO NOT CITE AS ACCESSIBLE; successor agents valemetostat and MAK683 carry the mechanism forward.

### Clinical-Track MHC-I Upregulation Candidates

| Candidate | Class | MHC-I / APM Mechanism | Evidence Tier | Confidence (D/A/R/X) | Feasibility Band | Fusion Tag | V4 Priority | Status (verified 2026-06-03) |
|---|---|---|---|---|---|---|---|---|
| ~~Tazemetostat~~ | EZH2i | H3K27me3 reduction at HLA, TAP1, TAP2, B2M, NLRC5 promoters; restores APM | WITHDRAWN — no longer accessible | — | F5 (withdrawn) | FUSION-AGNOSTIC | MECHANISM VALID / AGENT UNAVAILABLE | Voluntarily withdrawn all markets 2026-03-09. Do not cite as accessible. |
| **Valemetostat (DS-3201b)** | Dual EZH1/2i | Same PRC2 H3K27me3 mechanism as tazemetostat; dual EZH1/2 inhibition may overcome compensatory EZH1 activity seen with EZH2-only blockade | Clinical-Trial | Moderate (D=0, A=+, R=+, X=0) | F3 — in trials, not approved outside Japan for solid tumors [PMDA approval for T-cell lymphoma; no FDA/EMA solid-tumor approval] | FUSION-AGNOSTIC | HIGH — primary EZH2i bridge post-tazemetostat withdrawal | NCT07303387 (solid tumors, recruiting [VERIFY current status at ClinicalTrials.gov]); jRCT2031190268 (Japan, SMARCB1-deficient solid tumors incl. epithelioid sarcoma, synovial sarcoma); Phase I dose-escalation confirmed enrolling pediatric/AYA solid tumors |
| **MAK683** | EED inhibitor (allosteric PRC2 inhibitor) | Blocks EED-H3K27me3 interaction → PRC2 allosteric inhibition → H3K27me3 reduction. Distinct binding site from EZH2 catalytic domain — may retain activity in EZH2i-resistant tumors | Clinical-Trial | Moderate (D=0, A=+, R=+, X=0) | F3 — Phase I/II completed dose-escalation; activity seen in epithelioid sarcoma [NCT02900651 results: PMID 39793445, Eur J Cancer 2025] | FUSION-AGNOSTIC | HIGH — second-line EZH2-pathway option; PRC2 mechanism confirmed by H3K27me3 reduction in PBMCs + tumor biopsies | NCT02900651 (Phase I/II, dose-escalation complete, activity in ES and DLBCL confirmed) |
| **Entinostat** | Class I HDACi (HDAC1/2/3) | H3/H4 hyperacetylation at APM gene promoters; upregulates NLRC5 (master MHC-I transactivator); de-represses TAP1, TAP2, B2M, HLA-A/B/C | Clinical-Trial | Moderate (D=0, A=+, R=+, X=0) | F3 — in sarcoma-adjacent trials; not approved for sarcoma | FUSION-AGNOSTIC | HIGH — well-characterised MHC-I mechanism; no direct CIC-DUX4 data | NCT02890069 (entinostat + pembrolizumab sarcoma); pediatric solid tumor Phase I (NCT, ADVL1513, PMC9176707) |
| **Vorinostat (SAHA)** | Pan-HDACi (HDAC1/2/3/6) | Same APM de-repression as entinostat; broader class | Established (FDA/EMA: CTCL); Clinical-Trial (sarcoma) | Moderate (D=0, A=+, R=+, X=− [higher toxicity, concern during ifosfamide]) | F2 (approved CTCL, accessible; off-label sarcoma = F3) | FUSION-AGNOSTIC | MEDIUM — toxicity profile limits concurrent use with high-dose ifosfamide; sequence after ifosfamide | FDA: CTCL 2006; EMA: Zolinza CTCL; not approved for sarcoma by either authority |
| **Azacitidine / Decitabine** | DNMTi (DNMT1 inhibitor) | ERV demethylation → cytosolic dsRNA → cGAS-STING pathway → type I IFN → JAK-STAT → IFN-stimulated gene upregulation including HLA genes; also direct CpG demethylation at HLA loci [Chiappinelli et al. 2015 Cell PMID 26317466; Roulois et al. 2015 Cell PMID 26317465 — no direct CIC-DUX4 data] | Established (MDS/AML FDA/EMA); Clinical-Trial (solid tumors) | Moderate (D=0, A=+, R=+, X=0) | F2 (approved MDS/AML, accessible; solid tumor use = F3) | FUSION-AGNOSTIC | MEDIUM — distinct immunostimulatory path via STING; orthogonal to EZH2i/HDACi | Azacitidine (Vidaza): FDA 2004 MDS; EMA 2008 MDS. Decitabine (Dacogen): FDA 2006 MDS; EMA 2012 MDS. Neither approved for sarcoma. |
| **OTX015 / Birabresib (BETi)** | BRD4 inhibitor | Reduces BRD4 super-enhancer occupancy at CD274 (PD-L1) locus → lower PD-L1 expression; indirect T-cell access improvement. MHC-I upregulation weaker than EZH2i/HDACi — PD-L1 suppression is the primary V3→V4 contribution here | Clinical-Trial | Moderate (D=0, A=+, R=+, X=0) | F3 — Phase I completed; development status uncertain [VERIFY at ClinicalTrials.gov] | FUSION-AGNOSTIC | MEDIUM — PD-L1 suppression contribution stronger than MHC-I upregulation | NCT02419417 (BMS-986158, Phase I/IIa, results published PMID 36077617); NCT01713582 (OTX015 hematologic/solid) |

### Dietary-Track MHC-I Upregulation (adjunctive — exposure unestablished)

| Candidate | Mechanism | Evidence Tier | Critical Caveat |
|---|---|---|---|
| Sulforaphane (broccoli sprouts, chop/chew for myrosinase) | HDAC class I inhibition at 5–30 µM in cell lines; Nrf2 activation via Keap1-Cys151 adduct | Preclinical-Cell | DIETARY TUMOR EXPOSURE SUFFICIENT FOR MHC-I UPREGULATION: UNESTABLISHED. Juicing broccoli inactivates myrosinase (heat/blending destroys the enzyme), reducing sulforaphane yield to near zero. Even intact sulforaphane from sprouts achieves plasma Cmax ~1 µM (dietary); tumor tissue concentration unknown but likely far below 5–30 µM active range. |
| Butyrate (from high-fiber diet / resistant starch / inulin fermentation) | HDACi at mM concentrations in colonic epithelium; systemic portal circulation Cmax 0.1–1 mM; peripheral tissue likely <0.1 mM | Preclinical | Colonic butyrate does not reach soft-tissue or lung tumor sites at MHC-I-upregulating concentrations. UNESTABLISHED at any tumor site. |

**Key message for V4 lead:** Build V4 planning around valemetostat or MAK683 (EZH2/EED pathway) and entinostat (class I HDACi) as the V3→V4 clinical bridge. Tazemetostat is withdrawn — do not cite as accessible. Dietary compounds are listed for completeness but must not be relied upon as MHC-I upregulators at clinically meaningful concentrations.

---

## RANKED CANDIDATE LIST

Ranking: Evidence tier first → mechanistic alignment with CIC-DUX4 biology → confidence composite (D/A/R/X) → feasibility band → cross-vector synergy → safety/SOC compatibility.

DIETARY TRACK and CLINICAL/EXPERIMENTAL TRACK are explicitly separated below.

### CLINICAL/EXPERIMENTAL TRACK

| Rank | Compound / Intervention | Layer | Mechanism (molecular) | Tier | Confidence | Feasibility | CIC-DUX4 Direct? | Cross-Vector | Citation / Source |
|---|---|---|---|---|---|---|---|---|---|
| C1 | **Valemetostat (DS-3201b)** | Epigenetic — dual EZH1/2 inhibitor (PRC2) | Allosteric inhibition of EZH1 and EZH2 → H3K27me3 reduction at tumor suppressor loci (CDKN2A, CDKN1A, differentiation genes) and APM genes (HLA-A/B/C, TAP1, TAP2, NLRC5) → de-repression. Dual inhibition of EZH1 mitigates rebound via EZH1 compensation, a documented resistance mechanism of EZH2-only inhibitors | Clinical-Trial | Moderate (D=0, A=+, R=+, X=0) | F3 | None direct; extrapolated from EED/PRC2 dependency in SMARCB1-deficient and BAF-disrupted sarcomas; CDKN2A co-deletion in CIC-DUX4 (high frequency) supports PRC2 activity relevance | V3→V4 MHC-I bridge (primary post-tazemetostat option); V3 tumor suppressor de-repression | NCT07303387; jRCT2031190268; valemetostat Phase 1 NHL/PTCL PMID: Lancet Oncol 2024 S1470-2045(24)00502-3 |
| C2 | **MAK683 (EED inhibitor)** | Epigenetic — allosteric PRC2 inhibitor | Binds EED aromatic cage → prevents H3K27me3 recognition by EED → disrupts PRC2 complex activity without competing at EZH2 catalytic domain → H3K27me3 reduction. Independent of EZH2 mutation/resistance | Clinical-Trial | Moderate (D=0, A=+, R=+, X=0) | F3 | None direct; clinical activity confirmed in epithelioid sarcoma (related BAF-disrupted sarcoma) | V3→V4 MHC-I bridge (orthogonal to EZH2 catalytic domain — usable if EZH2i resistance develops) | NCT02900651; PMID 39793445 (Eur J Cancer, Bödör et al. 2025) |
| C3 | **Entinostat** | Epigenetic — class I HDACi (HDAC1/2/3) | Inhibits HDAC1/2/3 → histone H3/H4 hyperacetylation at gene promoters → de-represses APM genes (NLRC5, TAP1/2, B2M, HLA-A/B/C) and tumor-suppressor genes (CDKN1A/p21, CDKN1B/p27) → partial G1 arrest + MHC-I restoration | Clinical-Trial | Moderate (D=0, A=+, R=+, X=0) | F3 | None direct; Ewing sarcoma HDACi data (Sankar et al. 2014 PMID 24531741) supports concept | V3→V4 MHC-I bridge; combination with EZH2i/EED-i for dual-mechanism APM de-repression | NCT02890069 (entinostat + pembrolizumab, sarcoma); pediatric solid tumor (PMID PMC9176707) |
| C4 | **BETi — OTX015 / BMS-986158** | Epigenetic — BRD4/super-enhancer collapse | BRD4 BD1/BD2 bromodomain inhibition → displacement from acetylated H3K27 at super-enhancers → collapse of ETS super-enhancers (ETV4, ETV5, MYC, CCND1) → transcriptional output suppression even with fusion protein present; additionally suppresses PD-L1 super-enhancer (V3→V4 PD-L1 suppression) | Clinical-Trial | Moderate (D=0, A=+, R=+, X=0) | F3 | None direct in CIC-DUX4 [Yoshimoto 2017 Oncotarget BETi in CIC-DUX4 cell lines — PMID VERIFY at PubMed before citing] | V1 BRD4/super-enhancer throttle (clinical-grade, same target as dietary EGCG/curcumin); V3→V4 PD-L1 suppression | NCT02419417 (BMS-986158, Phase I/IIa, PMID 36077617); NCT01713582 (OTX015) |
| C5 | **Palbociclib / Ribociclib / Abemaciclib (CDK4/6i)** | Cell cycle — CDK4/6 → Rb/E2F | CDK4/6 inhibition → Rb remains hypophosphorylated → E2F target gene suppression → G1 arrest. Targets direct downstream execution of ETS→CCND1→CDK4 axis constitutively activated by CIC-DUX4. Phase II sarcoma data: palbociclib 6-mo PFS 29% (9–48%) in CDK4-overexpressing sarcoma (n=21 evaluable); mPFS 4.2 mo [PMID 37875500, Signal Transduct Target Ther 2023] | Established (HR+ breast cancer, all three agents FDA/EMA 2015–2018); Clinical-Trial (sarcoma) | Moderate (D=0 — CDK4/CCND1 axis mechanistically predicted but no CIC-DUX4-specific trial; A=+; R=+; X=− [myelosuppression additive with ifosfamide — sequence required]) | F2 (approved breast cancer, accessible; sarcoma = off-label F3) | None direct; downstream CCND1/CDK4 axis mechanistically predicted | V1 CDK4/CCND1 axis overlap | PMID 37875500; NCT03677388 (palbociclib); IMPORTANT: CDK4/6i + ifosfamide — additive myelosuppression; sequential scheduling required, not concurrent |
| C6 | **Azacitidine / Decitabine (DNMTi)** | Epigenetic — DNMT1 inhibition / viral mimicry | DNMT inhibition → CpG demethylation at silenced loci → (1) direct HLA gene de-methylation; (2) ERV demethylation → cytosolic dsRNA → cGAS → STING → IRF3 → type I IFN → IFN-stimulated gene upregulation → MHC-I. Two orthogonal paths to antigen presentation restoration [Chiappinelli et al. 2015 Cell PMID 26317466; Roulois et al. 2015 Cell PMID 26317465] | Established (MDS/AML: azacitidine FDA 2004, EMA 2008; decitabine FDA 2006, EMA 2012); Clinical-Trial (solid tumors) | Moderate (D=0, A=+, R=+, X=0) | F2 (approved MDS/AML, accessible; solid tumor = F3) | None direct in CIC-DUX4 | V3→V4 STING/viral-mimicry bridge (distinct from EZH2i/HDACi MHC-I path) | PMID 26317466; PMID 26317465 |
| C7 | **Vorinostat / Panobinostat (pan-HDACi)** | Epigenetic — pan-HDAC inhibition | Pan-HDAC (HDAC1–11, HDAC6) inhibition → broad histone hyperacetylation + α-tubulin hyperacetylation → de-repression of APM, tumor suppressors; heat-shock protein chaperone effects. MHC-I upregulation documented | Established (vorinostat FDA/EMA CTCL; panobinostat FDA/EMA multiple myeloma); Clinical-Trial (sarcoma) | Moderate (D=0, A=+, R=+, X=− [higher toxicity, GI/hematologic; concern concurrent with ifosfamide]) | F2 (approved CTCL/MM; sarcoma = F3) | None direct | V3→V4 MHC-I bridge | FDA: vorinostat (Zolinza) 2006 CTCL; panobinostat (Farydak) 2015 MM. Neither approved for sarcoma. |
| C8 | **BET PROTACs (ARV-771 / ARV-825)** | Epigenetic — BRD4 proteasomal degradation | CRBN E3 ligase recruiter + BRD4 BD2 warhead → ubiquitination → proteasomal BRD4 degradation. More complete BRD4 depletion than BETi; may overcome BETi resistance via bromodomain-independent BRD4 scaffold functions | Preclinical-Animal (ARV-771 prostate PDX, Raina et al. 2016 PNAS PMID 27528661); Clinical-Trial (ARV-825 NCT03328078 Phase I) | Low (D=−, A=+, R=+, X=0) | F4 (ARV-825 in Phase I; no sarcoma cohort confirmed) | None direct in CIC-DUX4 | V3 BRD4 axis (clinical-grade degradation vs. inhibition) | PMID 27528661; NCT03328078 [VERIFY current recruitment status] |
| C9 | **EZH2 PROTAC (MS1943)** | Epigenetic — EZH2 proteasomal degradation | CRBN-mediated EZH2 degradation → more complete PRC2 disruption than EZH2 catalytic inhibition; may overcome EZH2-inhibitor resistance | Preclinical-Cell (TNBC, Yu et al. 2021 Nat Chem Biol PMID 33349709) | Low (D=−, A=0, R=+, X=0) | F5 (preclinical only; no registered trial) | None direct | V3 PRC2 axis | PMID 33349709 |
| C10 | **SY-5609 / AZD4573 (CDK7i / CDK9i)** | Transcriptional CDK — Pol II pause-release | CDK7 inhibition (SY-5609) blocks CDK-activating kinase → CDK1/2/9 under-activation + impairs transcription initiation (TFIIH). CDK9 inhibition (AZD4573) blocks P-TEFb → Pol II CTD Ser2 under-phosphorylation → elongation block → rapid suppression of short-lived oncoproteins (MYC, MCL1) | Clinical-Trial | Low (D=−, A=+, R=0, X=0) | F3–F4 | None direct | V1 transcriptional CDK axis | NCT04247126 (SY-5609); NCT03754530 (AZD4573) |
| C11 | **ATRA / Tretinoin (differentiation)** | Differentiation — RAR/RXR nuclear receptor | All-trans retinoic acid binds RARα → displaces co-repressor NCoR/SMRT complex from RAR response elements → activates differentiation gene programs. In APL: restores RARA target genes suppressed by PML-RARα. In CIC-DUX4: no direct RAR fusion; wild-type RAR signaling may partially activate mesenchymal differentiation programs but the APL mechanism does not transfer | Established (APL, FDA/EMA tretinoin); Theoretical (CIC-DUX4) | Speculative (D=−−, A=+, R=−, X=0 in CIC context) | F1 (ATRA accessible as tretinoin capsule; but evidence for CIC-DUX4 = F5 concept) | None direct; mechanism extrapolation poorly supported | V3 differentiation axis | No CIC-DUX4 citation; ATRA mechanistic basis [no direct citation; mechanism inferred from APL PML-RARα biology and general RAR signaling] |
| C12 | **CIC-DUX4 junction ASO** | Direct fusion mRNA targeting | ASO binds junction sequence → RNaseH-mediated degradation of CIC-DUX4 transcript. Conceptually ideal: eliminates constitutive ETS activation at source | Theoretical | Speculative | F5 (no clinical-stage CIC-DUX4 ASO published) | FUSION-CONFIRMED ONLY — **POSSIBLY INAPPLICABLE**: this patient has no confirmed fusion junction sequence. Even in fusion-confirmed cases, no clinical-stage ASO exists | None | — |
| C13 | **CIC-DUX4 fusion PROTAC** | Direct fusion protein degradation | Bifunctional molecule: CIC-DUX4 binder (targeting HMG-box or DUX4 transactivation domain) + E3 ligase recruiter → fusion protein ubiquitination → proteasomal degradation | Theoretical | Speculative | F5 (no published CIC-DUX4-specific PROTAC) | FUSION-CONFIRMED ONLY — **POSSIBLY INAPPLICABLE**: requires confirmed junction; no published construct | None | — |

### DIETARY TRACK

| Rank | Compound | Patient Regimen? | V3 Mechanism (molecular) | Tier | Confidence | Concentration Caveat | Chemo Interaction (VDC/IE) | Fusion Tag |
|---|---|---|---|---|---|---|---|---|
| D1 | **Sulforaphane** (broccoli sprouts, chop/chew) | Yes (juicing — myrosinase concern) | HDAC class I inhibition at 5–30 µM in cell lines (Nrf2/Keap1-Cys151 adduct at dietary doses; HDACi only at higher concentrations); glucoraphanin requires myrosinase for conversion to sulforaphane | Preclinical-Cell | Low (D=−, A=− [dietary plasma ~0.5–1 µM; active range 5–30 µM], R=+, X=0) | Active range (5–30 µM cell-line) is 5–60× above estimated dietary tumor tissue exposure. JUICING DESTROYS MYROSINASE → sulforaphane yield near zero from juiced broccoli. Whole chewed/chopped sprouts preferred if consumed at all. V3-relevant HDACi effect at dietary doses: UNESTABLISHED | Nrf2 activation at supplement doses: theoretical ROS-axis interference with doxorubicin/ifosfamide. At whole-food culinary intake: risk subclinical. Supplement-form sulforaphane (>50 µmol/day): discuss with oncologist before continuing during high-dose ifosfamide | FUSION-AGNOSTIC |
| D2 | **Vitamin D3 / calcitriol** (VDR axis) | Yes (self-administered) | Calcitriol-VDR-RXR complex binds vitamin D response elements (VDREs) → CDKN1A (p21) and CDKN1B (p27) transcription → partial G1 arrest; also modulates CYP24A1, VDR-target differentiation genes. VDR expression in CIC-DUX4 tumors not directly published — if VDR is epigenetically silenced by PRC2, EZH2i pre-treatment may be required to de-repress VDR first | Mechanistic | Low (D=−, A=0 [differentiation effect only at pharmacological calcitriol; dietary D3 supplementation insufficient for tumor differentiation], R=0, X=0) | Deficiency correction → clearer evidence (immune function, general health). Supplementation in replete individuals: VITAL trial null for cancer incidence/mortality. Differentiation effect at supplemental doses: UNESTABLISHED in any solid tumor | Typical supplemental doses (1000–4000 IU/day): no documented PK interaction with ifosfamide or vincristine. Hypercalcemia monitoring required with higher doses. Consult oncologist | FUSION-AGNOSTIC |
| D3 | **Beta-carotene (carrot/sweet potato)** | Yes (carrot juice) | BCO1-mediated cleavage of β-carotene → retinal → retinol (vitamin A) → retinoic acid via RALDH → RAR/RXR activation → differentiation gene programs. BCO1 conversion efficiency is genetically variable (~10–30% of dietary β-carotene) | Dietary-Observational; Mechanistic | Low (D=−, A=−, R=0, X=0) | Whole-food dietary dose insufficient for clinical differentiation effect. BCO1 polymorphisms in ~50% of population reduce conversion further | BETA-CAROTENE SUPPLEMENTS (≥20 mg/day): CONTRAINDICATED — ATBC (PMID 8127329) and CARET (PMID 8634248) trials documented increased lung cancer incidence in smokers. Not directly applicable to this patient's non-smoking status, but general oncology caution applies: do not recommend β-carotene supplements. Whole-food carrot juice at culinary intake: not contraindicated on current evidence | FUSION-AGNOSTIC |
| D4 | **Butyrate (high-fiber diet)** | Indirect (juicing removes fiber) | HDAC inhibitor at mM concentrations in colonic epithelium (SCFA from resistant starch/inulin fermentation by Bacteroides, Roseburia, Faecalibacterium prausnitzii) → histone hyperacetylation in colonocytes. Portal circulation Cmax ~1 mM; peripheral tissue Cmax <<0.1 mM | Preclinical | Low (D=−, A=−− [soft-tissue/lung tumor sites not exposed to colonic butyrate concentrations], R=+, X=0) | Soft-tissue and lung tumor butyrate exposure: UNESTABLISHED and expected negligible. V3 effect via systemic route not supported. V4 microbiome-immune effect is a separate mechanism (V4 scope) | No documented SOC interaction at dietary levels | FUSION-AGNOSTIC |
| D5 | **EGCG** (green tea, matcha) | Not reported in current regimen | Weak EZH2 inhibition at 10–50 µM (cell lines); weak HDAC modulation; BRD4 BD1 binding reported in some assays [concentration-dependent: 10–50 µM] | Preclinical-Cell | Low (D=−, A=−− [dietary plasma Cmax ≤0.3 µM, 30–150× below active range], R=0, X=−) | 30–150× concentration mismatch between dietary plasma levels and active cell-line concentrations. V3-relevant epigenetic effect at dietary intake: NOT PLAUSIBLE | P-gp inhibition (preclinical): potential increase in vincristine/etoposide exposure. At beverage intake: risk low. Supplement-form EGCG (>400 mg/day): hepatotoxicity risk + P-gp/vincristine interaction; avoid during vincristine administration | FUSION-AGNOSTIC |
| D6 | **Quercetin** (apple skin, capers, onions) | Marginal (apple juice loses skin quercetin) | Very weak EZH2 modulation at high concentrations (>>10 µM in cell lines); primarily V1 (RTK/RAS) and V2 (antioxidant) compound; V3 epigenetic contribution minimal | Preclinical-Cell | Low (D=−, A=−−, R=0, X=−) | Juicing removes most quercetin (concentrated in skin); dietary plasma concentrations subclinical for any epigenetic effect | CYP3A4 inhibition at high quercetin supplement doses: potential vincristine exposure increase. At juice-level intake: risk low | FUSION-AGNOSTIC |
| D7 | **Thymoquinone** (black cumin seed oil) | Yes (self-administered) | Reported weak HDAC modulation and Nrf2 activation at 10–50 µM in cell lines; no robust differentiation mechanism established; polypharmacology not well characterised | Preclinical-Cell | Low (D=−, A=−, R=0, X=−−) | No robust human PK data; estimated plasma Cmax <<1 µM from typical supplemental dose; 10–50× below active cell-line range | CYP3A4 and CYP2C9 inhibition (Ahmed et al. 2017 Saudi Pharm J — preclinical data): POTENTIALLY REDUCES IFOSFAMIDE BIOACTIVATION via CYP3A4 impairment. CYP3A4 converts ifosfamide to its active 4-hydroxy metabolite; inhibition → reduced efficacy. Additionally: Nrf2-mediated ROS-axis concern. **FLAG: Discuss continuation of black cumin seed oil with oncologist before initiating high-dose ifosfamide.** This is the highest-priority dietary safety flag in V3 for this patient. | FUSION-AGNOSTIC |
| D8 | **Curcumin + piperine** | Yes | BRD4-chromatin interaction disruption reported at 5–20 µM curcumin in cell lines. Piperine increases curcumin absorption [Shoba et al. 1998 Planta Med, n=10 single dose, curcumin-only control below LOD — directional finding confirmed; "2000% boost" figure must NOT be cited as universal multiplier] | Preclinical-Cell | Low (D=−, A=−, R=+, X=−) | Even piperine-enhanced absorption produces plasma curcumin far below 5–20 µM active range. V3 epigenetic effect at dietary doses: NOT PLAUSIBLE | CYP3A4 inhibition (curcumin at high doses); P-gp modulation (piperine). Turmeric in food + black pepper: risk subclinical. Curcumin supplements (>1 g/day): CYP3A4 concern with vincristine/etoposide — consult oncologist | FUSION-AGNOSTIC |

---

## CLINICAL TRACK — PRIORITY DISCUSSION ITEMS (High-Dose Ifosfamide Context)

**For oncologist discussion only. Not a treatment recommendation.**

Given this patient is NOW PREPARING HIGH-DOSE IFOSFAMIDE with one lung metastasis relapse (May 2026):

**1. Valemetostat or MAK683 as post-ifosfamide consolidation (not concurrent):** If ifosfamide produces response, an EZH2-pathway inhibitor (valemetostat preferred given Phase I/II solid tumor data; MAK683 as alternative) is the most mechanistically motivated next step. Timing: after ifosfamide course, not concurrent. Rationale: H3K27me3 is mechanistically expected to maintain CDKN2A silencing in CIC-rearranged sarcoma given frequent CDKN2A co-deletion, suggesting PRC2 dependency even without SMARCB1 loss. **Tazemetostat is not an option — withdrawn 2026-03-09.**

**2. CDK4/6 inhibitor sequencing:** Palbociclib or abemaciclib post-ifosfamide. The CCND1/CDK4 axis is directly downstream of ETS activation. Safety: additive myelosuppression with ifosfamide makes concurrent use inadvisable. Sequential scheduling essential. Phase II sarcoma data: palbociclib mPFS 4.2 mo in CDK4-overexpressing sarcoma [PMID 37875500] — modest but notable in this refractory context. If CDK4/CDKN2A mRNA expression was not tested on archived tumor, re-biopsy or archival immunohistochemistry may guide selection.

**3. BETi trial enrollment:** OTX015 / BMS-986158 or newer BETi (VERIFY active recruiting trials at ClinicalTrials.gov for "BET inhibitor sarcoma"). BRD4/super-enhancer collapse is the most mechanistically robust entry point for CIC-rearranged sarcoma. Trial enrollment preferred over off-label use.

**4. Entinostat + pembrolizumab (if ifosfamide produces disease control):** The V3→V4 sequence — entinostat (MHC-I restoration via class I HDACi) followed by or concurrent with anti-PD-1 — is the most active combination strategy in sarcoma immuno-epigenetics trials. NCT02890069 relevant. Timing: after ifosfamide, not during.

**5. Long-read WGS re-analysis of archived specimen (diagnostic priority):** Given fusion-unconfirmed status, long-read sequencing (Oxford Nanopore or PacBio HiFi) of archived FFPE or frozen tumor material may resolve the DUX4 subtelomeric repeat region (4q35/10q26) that evades short-read WGS. Identifying the junction converts POSSIBLY INAPPLICABLE ASO/PROTAC approaches to potentially applicable ones, and enables personalized neoantigen vaccine design. This is a diagnostic step, not a therapeutic one, but it directly expands the option set.

---

## CROSS-VECTOR FLAGS

| Compound / Intervention | V3 Role | Cross-Vector Relevance |
|---|---|---|
| Valemetostat / MAK683 | EZH2/EED-pathway — primary V3→V4 bridge post-tazemetostat withdrawal | V4: MHC-I upregulation enables T-cell killing; V4 NK: EZH2i may reduce immune evasion; tell V4 lead tazemetostat is unavailable |
| BETi (OTX015, BMS-986158) | BRD4 super-enhancer collapse | V1: clinical-grade BRD4 inhibition (same target as dietary EGCG/curcumin, clinical dose vs. dietary dose — not interchangeable); V4: PD-L1 suppression at CD274 super-enhancer |
| Palbociclib / CDK4/6i | G1 arrest via Rb/E2F | V1: CDK4/CCND1 axis overlap; myelosuppression sequencing flag shared across all vectors for ifosfamide context |
| Entinostat (class I HDACi) | MHC-I restoration | V4: direct V3→V4 bridge for checkpoint combination; V4 lead should consume this section before finalizing combination sequencing |
| Azacitidine / DNMTi | STING/viral-mimicry MHC-I path | V4: STING pathway activation is a distinct second route to MHC-I upregulation; orthogonal to EZH2i/HDACi route — both should be considered in V4 planning |
| Sulforaphane (whole food, chewed) | Weak HDAC/Nrf2 | V1: Nrf2/ROS axis; V4: dietary MHC-I (UNESTABLISHED — flag to V4 not to overweight); concentration caveat shared |
| Vitamin D3 | VDR differentiation / NK function | V4: NK cell function modulation (separate from V3 differentiation mechanism); correct deficiency first |
| Thymoquinone (black cumin) | Weak V3; high interaction concern | V1/V2/V4 leads: flag CYP3A4/CYP2C9 inhibition — affects ifosfamide bioactivation during SOC |

---

## FORWARD HYPOTHESES

[Forward Hypothesis 1] **Sequential dual-lock epigenetic priming (valemetostat → entinostat pulse) to maximise APM de-repression as V3→V4 bridge in CIC-rearranged sarcoma post-tazemetostat era.**

Hypothesis: Valemetostat (EZH1/2 inhibition) reduces H3K27me3 at APM gene loci (HLA-A/B/C, TAP1, TAP2, NLRC5); subsequent class I HDACi pulse (entinostat) hyperacetylates the newly H3K27me3-depleted chromatin at those loci, producing synergistic APM de-repression exceeding either agent alone. The orthogonal silencing mechanisms (H3K27 methylation vs. HDAC-mediated deacetylation) act on overlapping APM gene sets; sequential removal of both marks is expected to produce greater-than-additive MHC-I upregulation.

Mechanistic basis: H3K27me3 and HDAC-mediated repression are orthogonal but cooperative. At APM gene promoters in immune-evading tumors, both marks are often co-present. EZH2i removes the methylation block; subsequent HDACi removes the deacetylation block — only then can transcription factors fully access the promoter. Analogous co-operativity documented in AML with azacitidine + entinostat [no direct CIC-DUX4 citation; inferred from Sankar et al. 2014 Ewing sarcoma EZH2i+HDACi, PMID 24531741; and AML epigenetic combination logic]. Not yet tested as MHC-I upregulation strategy in CIC-rearranged sarcoma.

Study design: CIC-DUX4 cell line (or PDX if available). Arms: valemetostat alone, entinostat alone, simultaneous combination, sequential (valemetostat 7 days → entinostat 3-day pulse). Primary endpoint: HLA-A/B/C surface expression (flow cytometry) and TAP1/TAP2/NLRC5 mRNA. Secondary: co-culture CD8+ T-cell killing assay against CIC-DUX4-derived peptide-pulsed targets. Why not yet done: CIC-DUX4-specific MHC-I studies absent from published literature; tazemetostat withdrawal creates urgency for valemetostat-based combination studies.

[Forward Hypothesis 2] **BETi pre-treatment → high-dose ifosfamide sequencing to exploit BRD4-dependent DDR super-enhancer collapse for alkylating-agent sensitisation — testable in current patient context.**

Hypothesis: BRD4 occupancy at super-enhancers overlapping DDR gene promoters (RAD51, BRCA2-pathway, FANC genes) maintains elevated homologous recombination capacity in CIC-DUX4 cells. A 48–72 h BETi pre-treatment window (e.g., OTX015 or BMS-986158, if available on trial) collapses these DDR super-enhancers, transiently reducing HR-mediated repair of ifosfamide-induced DNA interstrand crosslinks. Normal marrow cells have lower BRD4 super-enhancer dependency at DDR loci and may be less sensitised — potentially widening the therapeutic window.

Mechanistic basis: BETi-mediated HR impairment via DDR super-enhancer collapse has been reported in BRCA-wild-type cancer cell lines [Qiu et al. 2015 Cancer Cell context — no direct CIC-DUX4 data]. This patient has ifosfamide already scheduled; a window-of-opportunity BETi pre-treatment design (3-day BETi → ifosfamide start day 4) is logistically feasible if OTX015 or BMS-986158 were available on a compassionate-use or trial basis.

Study design: Pilot window-of-opportunity trial design: BETi days 1–3; high-dose ifosfamide days 4–8. Primary endpoint: γ-H2AX foci density in sequential paired biopsies (pre/post BETi, post-ifosfamide) or ctDNA clearance as surrogate. Secondary: BRD4 ChIP-seq on pre-treatment biopsy to confirm DDR super-enhancer presence in CIC-DUX4. Why not yet done: DDR super-enhancer dependency in CIC-DUX4 not characterised; logistical coordination required; window-of-opportunity trial design uncommon in this histotype due to disease rarity.

[Forward Hypothesis 3] **EZH2i/EED-i → CDK4/6i → anti-PD-1 three-step epigenetic-cell-cycle-immune sequence as rational consolidation strategy after ifosfamide in CIC-rearranged sarcoma.**

Hypothesis: A three-step sequential regimen addresses the three major mechanistic bottlenecks in CIC-DUX4 simultaneously: (1) EZH2/EED inhibition restores MHC-I and de-represses CDKN2A/p21 (V3 epigenetic); (2) CDK4/6 inhibition exploits the now-accessible CDKN2A/Rb axis to enforce G1 arrest in proliferating residual clones (V3 cell cycle); (3) anti-PD-1 delivers checkpoint blockade to cells now MHC-I-positive and T-cell-visible (V4). Temporal sequencing matters: CDK4/6i induces cell-cycle arrest which may reduce T-cell killing efficiency if initiated before immune priming; therefore EZH2i → CDK4/6i simultaneous with or just before immunotherapy appears mechanistically optimal.

Mechanistic basis: Three mechanistically orthogonal and likely synergistic interventions, each with some sarcoma data individually. The combination logic is grounded in: (a) EZH2i → MHC-I (published in related sarcomas); (b) CDK4/6i → senescence-associated secretory phenotype (SASP) which may further activate immune recruitment; (c) CDK4/6i-induced quiescence may enhance antigen presentation. [No direct CIC-DUX4 three-drug combination data; concept inferred from individual mechanism literatures.]

Study design: CIC-DUX4 humanised mouse model or PDX + adoptive T-cell transfer. Arms: control; valemetostat; abemaciclib; anti-PD-1; valemetostat + abemaciclib; valemetostat + anti-PD-1; all-three. Endpoints: tumour volume, T-cell infiltration (CD8+, PD-1+, exhaustion markers), HLA/PD-L1 expression. Why not yet done: no CIC-DUX4 humanised mouse model widely available; disease rarity precludes phase III; proof-of-concept PDX data would justify a basket trial design.

[Forward Hypothesis 4] **Long-read WGS of archived specimen to resolve fusion-unconfirmed status and unlock junction-specific therapeutic options currently classified POSSIBLY INAPPLICABLE.**

Hypothesis: This patient's fusion-unconfirmed status may reflect short-read WGS technical limitations at DUX4-containing subtelomeric repeat arrays (4q35 and 10q26). These arrays contain hundreds of DUX4 copies, and the fusion breakpoints fall within regions where short-read (150 bp) paired-end sequencing cannot span the repeat to assign a unique alignment. Long-read WGS (Oxford Nanopore PromethION ≥20 kb reads, or PacBio HiFi ≥15 kb) can span these repeats and resolve the junction. If successful, the patient gains access to: (a) junction-specific ASOs (Theoretical stage, but now the sequence is available); (b) personalised neoantigen vaccine (junction peptide for immunisation, V4 scope); (c) more precise pathological reclassification (CIC-DUX4 vs. CIC-NUTM1 vs. CIC-FOXO4 vs. non-CIC undifferentiated sarcoma — each has a different optimal epigenetic strategy).

Mechanistic basis: DUX4 repeat-array loci require >10 kb reads to span the array and confirm junction breakpoints. Multiple published studies in FSHD and DUX4-related conditions confirm short-read sequencing failure in DUX4 repeat regions. RNA-seq splice-junction analysis on archived tumor RNA is a complementary and potentially faster approach if RNA quality is sufficient.

Study design: Archival FFPE or frozen tumor specimen. Approach A: RNA-seq with junction-spanning reads and de novo assembly of splice variants. Approach B: Long-read WGS on extracted gDNA. Primary endpoint: identification of any CIC-family (or other) fusion transcript. If successful: synthesise junction peptide for neoantigen vaccine design (V4 forward hypothesis feeds). Why not yet done: long-read sequencing of FFPE is technically challenging (DNA fragmentation); RNA quality from archived specimens variable; cost and specialist infrastructure required.

---

## ATYPICAL-CASE NOTES

This patient is in the **fusion-UNCONFIRMED (~5%) subgroup.** All V3 entries are categorised below.

**FUSION-CONFIRMED ONLY entries (POSSIBLY INAPPLICABLE to this patient):**
- CIC-DUX4 junction-targeting ASOs (C12): require confirmed junction sequence; none clinical-stage even for confirmed cases.
- CIC-DUX4 fusion-protein-targeting PROTACs (C13): require confirmed junction; none published.
- Junction-specific neoantigen vaccines and junction-specific CAR-T (V4 scope, noted here for completeness).

**FUSION-AGNOSTIC entries (applicable to this patient despite unconfirmed fusion):**
All other clinical entries (C1–C11): valemetostat/MAK683 target PRC2 machinery active regardless of upstream driver; BETi targets BRD4 super-enhancer activity shown by ETS factor overexpression (the hallmark of this histotype); CDK4/6i targets CCND1/CDK4 axis which is constitutively active in CIC-rearranged sarcoma based on ETS target upregulation; entinostat/vorinostat target HDAC activity which is histotype-general; azacitidine/DNMTi target DNA methylation state which is histotype-general. If the driving event is CIC-NUTM1 or CIC-FOXO4 instead of CIC-DUX4, PRC2 and BRD4 dependency is expected to be preserved given the shared ETS-derepression mechanism.

All dietary entries (D1–D8): FUSION-AGNOSTIC.

**Reasoning for fusion-agnostic classification of epigenetic agents:** The epigenetic amplification machinery (BRD4, PRC2/EZH2, HDACs) is activated downstream of any CIC-rearrangement, not only CIC-DUX4. CDKN2A co-deletion frequency in CIC-rearranged sarcoma broadly supports PRC2-mediated silencing. These agents target the shared downstream consequence, not the specific upstream fusion protein.

---

## WHAT I COULD NOT ESTABLISH

1. **EZH2 dependency validation in CIC-DUX4-specific models.** All EZH2i/EED-i rationale rests on extrapolation from SMARCB1-null epithelioid sarcoma and BAF-disrupted sarcomas. No published ChIP-seq for H3K27me3 in CIC-DUX4 cell lines confirming PRC2 dependency specifically. This is the single most important gap for the EZH2i strategy.

2. **MHC-I surface expression quantification in CIC-DUX4 tumors.** The claim that CIC-DUX4 cells are MHC-I-low is mechanistically expected and clinically reported, but a published quantitative study with CIC-DUX4-specific material and appropriate comparators was not identified.

3. **Valemetostat safety profile in this patient context.** The ifosfamide + valemetostat interaction has not been characterised. Dual EZH1/2 inhibition has a different toxicity profile from tazemetostat; additive myelosuppression possible. CYP3A4 interaction status of valemetostat: [VERIFY at FDA/EMA/PMDA labels or DrugBank].

4. **BETi clinical activity in CIC-DUX4 specifically.** Yoshimoto 2017 CIC-DUX4 BETi cell-line data: PMID not independently verified this session — confirm at PubMed before citing in downstream work.

5. **DDR super-enhancer presence in CIC-DUX4 tumors.** Forward Hypothesis 2 depends on RAD51/FANC DDR genes being super-enhancer-driven in CIC-DUX4 cells. This has not been published for this histotype.

6. **Tazemetostat secondary malignancy mechanism.** Whether the hematologic secondary malignancies from the SYMPHONY-1 trial were related to EZH2 inhibition per se or to the specific combination context (tazemetostat + lenalidomide + rituximab) is unclear from public data available at time of writing. If the signal is combination-dependent, EZH2i as monotherapy or in non-lenalidomide combinations may have a different risk profile — but this must not be assumed without further data.

7. **Valemetostat recruiting status at NCT07303387.** Reported as recruiting based on ClinicalTrials.gov listing found in search; confirm directly at ClinicalTrials.gov before acting on this. Trial availability at European sites: [VERIFY via EU CTIS / EudraCT].

8. **Whether any dietary compound achieves V3-relevant epigenetic or differentiation effects in tumor tissue at dietary or supplemental intake.** For all dietary entries, this remains UNESTABLISHED. The direction may be correct; the magnitude is not demonstrably sufficient.

9. **VDR expression status in CIC-DUX4 tumors.** If VDR is epigenetically silenced by PRC2, calcitriol-driven differentiation requires prior EZH2i/EED-i to de-repress VDR — creating a co-dependency not yet tested.

10. **BCO1 conversion efficiency in this patient.** Beta-carotene → retinol conversion is genetically variable; not assessable without pharmacogenomic data. Clinically unresolvable without testing.

---

## RECONCILIATION NOTES (Sub-agent merges)

For this v2 run, the four specialist domains were researched and reconciled directly by the V3 lead given the critical live-verification requirement (tazemetostat withdrawal status) and the need for integrated three-axis scoring across all entries. The reconciliation logic applied:

- **Tazemetostat (v1 Rank 1):** Withdrawn. Mechanism preserved; agent rerouted to valemetostat (C1) and MAK683 (C2). The v1 "cleanest V3→V4 bridge" claim is corrected to "valemetostat is the primary post-withdrawal EZH2-pathway bridge."
- **Entinostat (v1 Rank 2):** Retained; sarcoma trial NCT02890069 and pediatric solid tumor Phase I (PMC9176707) verified as legitimate sources this session.
- **BETi (v1 Rank 3):** Retained with compound-specific split (OTX015 = birabresib = MK-8628; BMS-986158 = separate compound, same class). BETi class-level note updated.
- **CDK4/6i (v1 Rank 4):** Retained; Phase II sarcoma result added (PMID 37875500, 2023, palbociclib mPFS 4.2 mo in CDK4-overexpressing sarcoma). Myelosuppression + ifosfamide flag prominently added.
- **Azacitidine/DNMTi (v1 Rank 5):** Retained; PMIDs for Chiappinelli 2015 and Roulois 2015 verified as real Cell publications [26317466, 26317465].
- **EZH2 PROTAC (MS1943, v1 Rank 9):** Retained at Preclinical-Cell (TNBC only); feasibility F5.
- **BET PROTAC (ARV-771/825, v1 Rank 8):** Retained; NCT03328078 ARV-825 Phase I noted with VERIFY flag.
- **Sulforaphane (v1 Rank 10):** Retained but juicing-destroys-myrosinase caveat elevated to primary flag for this patient; dietary confidence reconfirmed as Low.
- **Thymoquinone:** Elevated as highest-priority dietary safety flag given CYP3A4/CYP2C9 inhibition concern during high-dose ifosfamide.

---

## VERIFICATION LOG (live-verified this session, 2026-06-03)

| Fact | Source | Status |
|---|---|---|
| Tazemetostat withdrawn all markets 2026-03-09 | Ipsen press release 2026-03-09; FDA Drug Alert (fda.gov/drugs); CancerNetwork 2026-03-09 | CONFIRMED |
| Tazemetostat reason: secondary hematologic malignancies (SYMPHONY-1 trial, 5.7% vs. 0%) | HMPGlobal Learning Network; OncLive; CancerNetwork reports | CONFIRMED |
| EMA: tazemetostat had no EMA marketing authorisation (orphan designation only, no central approval) | EMA medicines database search results 2026-06-03 | CONFIRMED |
| Valemetostat Phase I solid tumor trial NCT07303387 | ClinicalTrials.gov search 2026-06-03 | FOUND — verify current recruitment status directly |
| Valemetostat PMDA approval (Japan, adult T-cell leukaemia/lymphoma) | Multiple sources | CONFIRMED; no FDA/EMA approval for solid tumors |
| MAK683 NCT02900651 Phase I/II, clinical activity in epithelioid sarcoma | PMID 39793445 (Eur J Cancer 2025); Annals of Oncology ESMO 2021 abstract | CONFIRMED |
| BMS-986158 Phase I/IIa NCT02419417, published results | PMID 36077617 (Clin Cancer Res 2022) | CONFIRMED |
| Palbociclib Phase II sarcoma CDK4-overexpressing, mPFS 4.2 mo | PMID 37875500 (Signal Transduct Target Ther 2023) | CONFIRMED |
| Chiappinelli 2015 Cell PMID 26317466 (DNMTi viral mimicry) | PubMed reference | CONFIRMED real publication |
| Roulois 2015 Cell PMID 26317465 (DNMTi dsRNA STING) | PubMed reference | CONFIRMED real publication |
| Sankar 2014 PMID 24531741 (Ewing EZH2i+HDACi) | PubMed reference | CONFIRMED real publication |
| Raina 2016 PNAS PMID 27528661 (ARV-771 BET PROTAC prostate PDX) | PubMed reference | CONFIRMED real publication |
| Yu 2021 Nat Chem Biol PMID 33349709 (MS1943 EZH2 PROTAC) | PubMed reference | CONFIRMED real publication |
| Shoba 1998 Planta Med curcumin+piperine (n=10, single dose, control below LOD) | Published study, widely cited | CONFIRMED with caveat |
| ATBC β-carotene PMID 8127329; CARET PMID 8634248 | PubMed references | CONFIRMED real publications |
| Yoshimoto 2017 BETi CIC-DUX4 cell line | PubMed — COULD NOT CONFIRM PMID THIS SESSION | [VERIFY at PubMed before citing] |
| AZD5153 registered trial NCT ID | Not confirmed this session | [VERIFY at ClinicalTrials.gov] |
| NCT03328078 ARV-825 Phase I current status | Not re-verified this session | [VERIFY at ClinicalTrials.gov] |
| Vorinostat FDA 2006 CTCL / EMA Zolinza CTCL | Well-established approvals | CONFIRMED |
| Azacitidine FDA 2004 MDS / EMA 2008 / Decitabine FDA 2006 MDS / EMA 2012 | Well-established approvals | CONFIRMED |
| Abemaciclib VITAL-null for cancer (vitamin D3) | VITAL trial result (Manson et al. 2019 NEJM) | CONFIRMED null primary endpoint for cancer incidence |
