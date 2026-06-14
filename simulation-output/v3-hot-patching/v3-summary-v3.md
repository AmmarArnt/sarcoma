# Vector 3 — Hot Patching Summary (Clean-Slate Run v3)

**Summary:** This output covers approaches that restore the "break condition" inside cells already
carrying (or possibly carrying — see Atypical-Case Notes) the CIC-DUX4 fusion: epigenetic
reprogramming (HDACi/DNMTi/EZH2i/BETi and the MHC-I bridge to V4), differentiation therapy
(retinoid signaling, vitamin D3/VDR, butyrate), the published PROTAC/ASO/degrader landscape and
clinical-trial status of the major epigenetic/cell-cycle drug classes, and synthetic-lethal
dependency mapping (BRD4, EZH2/PRC2, CDK4/CCND1, MCL1). Reconciled from four parallel specialist
sub-agents
(`simulation-output/v3-hot-patching/v3/{epigenetic-reprogramming,differentiation-therapy,clinical-experimental,synthetic-lethality}.md`).
**Deliberately excludes:** V1's BRD4-throttling framing (referenced only where it intersects MHC-I
or synthetic lethality), V4's immune-effector mechanisms (referenced only at the V3→V4 bridge),
and any speculative gene-therapy construct not in the published literature or a registered trial.

**Confidence: medium-low overall**, with high-confidence sub-claims. The single highest-tier
direct CIC-DUX4 finding in this vector — MCL1 dependence in CIC::DUX4 tumoroids
(Preclinical-Cell + Preclinical-Animal, two independent 2025 *Nat Commun* papers) — is
**driver-contingent for this patient** (fusion-unconfirmed, ~5% atypical subgroup) and must be
held pending diagnostic resolution. The clinical-track epigenetic landscape underwent a major,
live-verified status change this session: **tazemetostat (Tazverik) was voluntarily withdrawn
worldwide from ALL indications on 2026-03-09** (Ipsen, SYMPHONY-1 secondary-malignancy signal,
5.7% vs. 0% hematologic second primary malignancies), removing what would otherwise have been the
clinical track's most accessible entry. The dietary track remains adjunctive-at-best with
consistent 10–10,000-fold concentration gaps between cell-line-active and dietary-achievable
exposures across every compound assessed.

---

## MHC-I Upregulation Candidates (V3 → V4 Bridge)

> This section was published early as
> `simulation-output/v3-hot-patching/v3-summary-v3.md` (preliminary) as soon as the Epigenetic
> Therapy Specialist completed, per the V3→V4 execution-bridge requirement — V4's Wave 2 was not
> blocked. This is the reconciled, final version of that section.

### Clinical-tier candidates (ranked)

| Rank | Candidate | Mechanism for MHC-I restoration | Tier | CIC-DUX4 direct evidence | Fusion-dependence |
|---|---|---|---|---|---|
| 1 | **HDAC inhibitors** (class I — vorinostat, romidepsin, panobinostat, belinostat) | Increased global histone acetylation (H3K27ac, H4ac) opens chromatin at antigen-presentation-machinery (APM) loci (*TAP1*, *TAP2*, *PSMB8/9*, *HLA-A/B/C*, *B2M*); HDACi-driven re-expression of endogenous retroviral elements triggers a viral-mimicry/type-I-interferon (STAT1) response that further drives APM transcription. Documented to upregulate MHC-I in glioma cell lines (Wang et al. 2019, PMC6843866) and to "reshape the tumoral immune landscape toward an immune-stimulatory profile" with romidepsin in liver cancer (*Nat Commun* 2025, DOI 10.1038/s41467-025-62934-0). | Preclinical-Cell (glioma, liver, lymphoma lines) / Clinical-Trial (vorinostat/romidepsin FDA-approved for cutaneous T-cell lymphoma — different indication, same mechanism class) | None direct in CIC-DUX4 | **Fusion-agnostic** — acts on host chromatin/APM machinery, not the fusion junction. Applies to the ~5% fusion-unconfirmed cohort. |
| 2 | **DNMT inhibitors** (azacitidine, decitabine, guadecitabine) | DNA hypomethylating agents reverse promoter hypermethylation of MHC-I/HLA and TAP genes; reactivate endogenous retroviral elements → cGAS-STING/type-I IFN → STAT1-driven APM transcription. Guadecitabine demethylates MHC-I gene promoters and upregulates MHC-I in response to IFN-γ (Luo et al., *Nat Commun* 2018, DOI 10.1038/s41467-017-02630-w). | Clinical-Trial (breast cancer; mechanism class established) | None direct in CIC-DUX4 | **Fusion-agnostic** — acts on host methylome/interferon machinery. Applies to the ~5% fusion-unconfirmed cohort. |
| 3 | **EZH2 inhibitors** (tazemetostat and class) — **DOWNGRADED, see caveats** | PRC2-mediated H3K27me3 deposition silences APM genes in PRC2-dependent tumors; EZH2i removes this mark, restoring MHC-I/HLA-A,B,C and TAP1/2 transcription. Well-established in PRC2-dependent contexts (SMARCB1-loss rhabdoid tumor / epithelioid sarcoma). | Clinical-Trial (mechanism, in PRC2-dependent tumors) — but **the premise itself is now contested for CIC-DUX4** and the lead clinical agent is **globally withdrawn** (see below) | None direct; a 2024 CIC-DUX4 chromatin-profiling study (PMC10814785/Bakaric et al., *Cancers* 2024;16(2):457, DOI 10.3390/cancers16020457) suggests CIC-DUX4 is a **p300/CBP-driven activator**, not primarily PRC2-dependent | Fusion-agnostic mechanism class, but **two independent caveats compound here** (premise + access) — see below |
| 4 | **BET inhibitors** (OTX015/birabresib, BMS-986158, AZD5153) | BRD4 reads H3K27ac at super-enhancers; BET inhibition has variable, context-dependent effects on immune-related transcription (interferon-stimulated genes, MHC-I/PD-L1) — direction less consistently "MHC-I up" than the other three classes. Included because BETi is V1/V3's dominant clinical-track candidate via the BRD4-throttling rationale, but flagged as the **weakest of the four classes for MHC-I specifically**. | Preclinical-Cell / Clinical-Trial (general oncology, incl. pediatric Ewing cohort NCT03936465) | None direct in CIC-DUX4 | Fusion-agnostic mechanism, but MHC-I direction not consistently "up" — lower confidence than ranks 1–3. |

### Why EZH2i moved from "cleanest example" to rank 3, with two compounding caveats

1. **Premise caveat (mechanistic):** PMC10814785 (Bakaric et al. 2024, GSE248040 ChIP-seq) found
   CIC-DUX4 functions as a **p300/CBP-driven transcriptional activator**, with p300/CBP inhibition
   (dCBP-1) — not EZH2/PRC2 inhibition — proposed as the CIC-DUX4-specific actionable epigenetic
   dependency. DepMap CRISPR cross-check (Sim 2, Ewing proxy, n=27 lines): **EZH2 is NOT a
   viability dependency** (mean Chronos +0.01, 0% of lines dependent). This **does not invalidate**
   the HDACi/DNMTi MHC-I mechanisms above (their viral-mimicry/interferon route is independent of
   PRC2 status) — it specifically undercuts the EZH2i-for-CIC-DUX4 premise.
2. **Access caveat (regulatory, [VERIFY] — live-verified 2026-06-14, concordant across two
   specialists):** On **2026-03-09, Ipsen voluntarily withdrew Tazverik (tazemetostat) worldwide
   from ALL markets and ALL indications** — both relapsed/refractory follicular lymphoma
   (EZH2-mutant) and metastatic/locally-advanced epithelioid sarcoma (the 2020-01-23 accelerated
   approval, ORR ~15%, NCT02601950). Trigger: an Independent Data Monitoring Committee finding from
   Phase Ib/III **SYMPHONY-1** — 18/318 (5.7%) of tazemetostat-treated patients developed
   hematologic second primary malignancies (predominantly MDS/AML) vs. 0/control. Ipsen is
   discontinuing all active tazemetostat trials and expanded-access programs worldwide. **EMA never
   approved tazemetostat** (pre-withdrawal EU access was via named-patient programs only); an EMA
   approval is now extremely unlikely. Sources: Ipsen press releases 2026-03-09 (ipsen.com/press-release/...-3251503,
   ...-3252192), OncLive, CancerNetwork, Cancer Therapy Advisor, Oncology Nurse Advisor,
   oncologynewscentral.com. Accessed 2026-06-14.
   - **Attrition reason (ADR-0013): R4-regulatory/safety-driven, NOT R1-target-invalidated** — the
     PRC2/EZH2-dependency mechanism in BAF-disrupted sarcomas is not biologically refuted by this
     withdrawal (it was an off-target genotoxicity signal in hematopoietic progenitors), but **the
     drug itself is now inaccessible through any normal channel, in any jurisdiction (F5)**.
   - **Valemetostat (dual EZH1/EZH2i, DS-3201b)** is an active successor (NCT07303387, SWI/SNF-altered
     solid tumors; FDA-approved 2022 for ATLL — different, hematologic indication) but **inherits an
     elevated index-of-suspicion for the same secondary-malignancy class effect** (broader PRC2
     blockade than tazemetostat) — this is an open, unresolved safety question, not a reassurance.

**Net assessment for V4:** the clinical-drug-class mechanism (HDACi/DNMTi → MHC-I up,
fusion-agnostic, Clinical-Trial tier) is real and should anchor V4's epigenetic-priming-bridge
discussion. EZH2i is now a **doubly-caveated, F5/concept-only entry** — premise-contingent
mechanistically and access-closed regulatorily — and should not be presented to V4 as an
actionable bridge candidate, only as historical/mechanistic context.

### Dietary-tier candidates — UNESTABLISHED at achievable exposure

- **Sulforaphane** (broccoli/broccoli-sprout glucosinolate-derived isothiocyanate): a documented
  weak class-I HDAC inhibitor in cell lines (HDAC3 depletion via a 14-3-3/Pin1-mediated mechanism;
  Rajendran et al., *Mol Cancer* 2011). The mechanistic chain to MHC-I upregulation (weak HDACi →
  H3K27ac↑ → MHC-I↑, by analogy to clinical HDACi) is *plausible* but **no study has measured tumor
  MHC-I after dietary sulforaphane exposure in any human tumor**. Cell-line effective
  concentrations are far above achievable dietary plasma levels. **Juicing destroys the activation
  step**: sulforaphane requires myrosinase released by chewing/chopping (3–4-fold bioavailability
  benefit from active endogenous myrosinase, PMC4629881); juice preparation yields a
  **non-quantitative conversion**, with sulforaphane partly trapped as conjugates
  (sulforaphanyl-amine, glutathione/protein conjugates — ScienceDirect S0308814618310628). Mature
  broccoli (as juiced) also starts from a lower glucoraphanin pool than sprouts. **This patient's
  broccoli-containing fresh juice is unlikely to deliver meaningful active sulforaphane.**
- **Butyrate** (colonic SCFA from fermented fiber): a well-characterized HDACi at colonic luminal
  concentrations (low-millimolar; PMC6346118), but systemic/portal plasma concentrations are
  reported in the **1–13 µM range** — roughly 2–3 orders of magnitude lower (figure indicative, not
  independently re-verified to a single primary source — see "What I Could Not Establish"). Same
  mechanistic chain as sulforaphane, but **systemic tumor exposure sufficient for HDAC inhibition
  in a deep soft-tissue/lung lesion is UNESTABLISHED** and considered unlikely. Few RCTs show
  high-fiber diet meaningfully raises plasma butyrate.

**Net assessment, dietary tier:** the clinical-drug-class mechanism is real (rank 1–2 above); the
dietary analogues are mechanistically aligned but **should not be presented as a "diet-based
MHC-I upregulation strategy" with any expectation of measurable clinical effect** — hypothesis,
not demonstrated intervention.

---

## Ranked Candidate List

| Rank | Compound/Approach | Layer | Mechanism (brief) | Tier | CIC-DUX4 direct? | Cross-vector | Driver-contingency (ADR-0008) | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | **MCL1 inhibitors / BH3-mimetics** (S63845 tool compound; S64315/MIK665 clinical derivative) | Synthetic Lethality | CIC::DUX4's retained DUX4 transactivation domain directly transactivates *MCL1* (ChIP-seq peaks, H3K27ac), buffering an intrinsic pro-apoptotic "DUX4 death program." MCL1 inhibition "re-arms" that program. | **Preclinical-Cell (1–10 nM IC50) + Preclinical-Animal** (S64315, 20 mg/kg 2×/week → tumor regression in CIC::DUX4 xenograft) — highest-tier direct CIC-DUX4 evidence in this vector | **Direct** — two independent 2025 *Nat Commun* papers (PMID 40841513, DOI 10.1038/s41467-025-62629-6; PMID 40841360, DOI 10.1038/s41467-025-62673-2) | V3 only | **HOLD — gated on DUX4 transactivation domain (D1 full, D2 only if DUX4-family partner, D3–D5: not applicable).** Highest-ceiling, most driver-contingent entry. **Do not present as a current recommendation.** | Synthetic-Lethality specialist |
| 2 | **CDK4 inhibition** (palbociclib, ribociclib, abemaciclib — refines "CDK4/6i" to "CDK4i") | Synthetic Lethality / Clinical-Experimental | CDK4 (+ cyclin D) phosphorylates/inactivates Rb, releasing E2F-driven S-phase entry — re-imposes the G1 brake (CDKN2A/p16) most CIC-DUX4 tumors have lost. | Established (palbociclib/ribociclib/abemaciclib, FDA breast cancer 2015/2017/2017, EMA 2016-17/2017/2018) / Clinical-Trial (sarcoma — GEIS palbociclib phase 2, PMC10598203, CDK4-overexpression-selected, 6-mo PFS 29%; abemaciclib in dedifferentiated liposarcoma, median PFS 7 mo) / Preclinical-Cell (CDK4 strongest+most selective DepMap dependency, Chronos −1.53, 89% of Ewing-proxy lines) / Preclinical-Animal (palbociclib — **limited in vivo effect in CIC-DUX4 xenograft**, [VERIFY], honest negative-leaning signal) | None direct (selection criteria are CDK4/CDKN2A status, not fusion type) | V1 (cell-cycle execution overlap) | **Fully driver-robust (D1–D5: 1,1,1,1,1)** — cell-cycle execution dependency is driver-agnostic. Safest entry to discuss regardless of driver resolution, though in vivo translation is itself only modest. | Synthetic-Lethality + PROTAC/ASO specialists |
| 3 | **HDAC inhibitors** (vorinostat, romidepsin, panobinostat, belinostat) | Epigenetic / MHC-I bridge / Differentiation (overlapping mechanisms — merged entry) | (a) MHC-I/APM gene re-expression via H3K27ac↑ + viral-mimicry/IFN (see bridge section); (b) differentiation-gene de-repression via global histone hyperacetylation, mechanistically analogous to (much stronger than) dietary butyrate's HDACi action. | Clinical-Trial (FDA-approved for cutaneous T-cell lymphoma — different indication, same mechanism class) / Preclinical-Cell (CIC-DUX4-relevant MHC-I mechanism) | None direct in CIC-DUX4 | V4 (MHC-I bridge), V1 | **Fusion-agnostic** — applies to the ~5% atypical subgroup regardless of driver. | Epigenetic + Differentiation specialists (merged) |
| 4 | **dCBP-1 (p300/CBP PROTAC-class degrader)** | Clinical-Experimental / Epigenetic | CIC-DUX4's transactivation domain requires p300/CBP for H3K27 acetylation at target loci; dCBP-1 degrades p300/CBP, indirectly silencing the fusion's transcriptional output. The one entry in the PROTAC/ASO landscape with **direct CIC-DUX4 cell-line data**. | Preclinical-Cell | **Direct** (PMC8511258, "Inactivation of the CIC-DUX4 oncogene through P300/CBP inhibition") | V3 only | **Partially driver-contingent** (strongest under D1/D2 — DUX4 transactivation domain present; D3–D5 score 0.5, mechanism plausibly weaker without that domain). | PROTAC/ASO specialist |
| 5 | **DNMT inhibitors** (azacitidine, decitabine, guadecitabine) | Epigenetic / MHC-I bridge | DNA hypomethylation reverses MHC-I/HLA/TAP promoter hypermethylation; reactivates endogenous retroviral elements → cGAS-STING/IFN → STAT1-driven APM transcription. | Clinical-Trial (breast cancer; mechanism class established) | None direct in CIC-DUX4 | V4 (MHC-I bridge) | **Fusion-agnostic** — applies to the ~5% atypical subgroup. | Epigenetic specialist |
| 6 | **BET inhibitors** (OTX015/birabresib, BMS-986158, AZD5153) | Epigenetic / Synthetic Lethality / Clinical-Experimental | BRD4 reads H3K27ac at CIC-DUX4-built super-enhancers (ETV4/5 and other ETS targets); BETi displaces BRD4, collapsing super-enhancer-driven output. **DepMap: BRD4 essentiality is universal/non-selective (Chronos −0.96, 100% of Ewing-proxy lines, selectivity +0.01)** — "addiction" framing overstates CIC-DUX4-*selectivity*; BRD4 is essential pan-cancer. | Preclinical-Cell (Ewing proxy; essentiality real but non-selective) / Clinical-Trial (BMS-986158 NCT02419417 + pediatric NCT03936465 incl. Ewing; AZD5153 first-in-human, general solid tumors) / **Theoretical** for any CIC-DUX4-*selective* claim | None direct — no published CIC-DUX4 BETi dose-response | V1 (primary owner), V4 (MHC-I, weakest of the 4 classes) | **Driver-robust (D1–D5: 1,1,1,0.5,1)** — ETS/super-enhancer program present whenever ETV4/5 derepression occurs (shared across D1–D3, D5; partial D4). | Synthetic-Lethality + PROTAC/ASO + Epigenetic specialists (merged) |
| 7 | **Vitamin D3 / VDR axis** | Differentiation | Calcitriol/VDR/RXR heterodimer binds VDREs across ~hundreds–thousands of genes, including p21/p27 (cell-cycle arrest) and SNAI2/EMT-suppressive differentiation genes (documented in osteosarcoma, PMC10203545). | Mechanistic (general) / Preclinical-Animal-Cell (osteosarcoma, different sarcoma) | None direct in CIC-DUX4 | V3, V4 (NK function) | **Fusion-agnostic** — host nuclear-receptor pathway independent of fusion partner. | Differentiation specialist |
| 8 | **ARID1A-mutant status as MHC-I-priming biomarker** (FH-SL2, see Forward Hypotheses) | Synthetic Lethality / Epigenetic | ARID1A frameshift mutations recurrently found in CIC::DUX4 tumoroids (same 2025 papers as MCL1 entry) — a cBAF-disruption lesion mechanistically analogous to SMARCB1-loss (which drives PRC2/EZH2 dependency in epithelioid sarcoma). Could license EZH2i-for-MHC-I in an ARID1A-mutant-selected subset, independent of the MCL1/driver question. | Mechanistic (bridge inferred by analogy, not demonstrated in CIC-DUX4) | Partial — ARID1A mutations are direct CIC::DUX4 findings; the EZH2-dependency *bridge* is not | V3→V4 bridge | **Largely driver-robust** — ARID1A/1p-loss reported across CIC-rearranged cohorts broadly (Specht 2016, PMID 27664537), not strictly DUX4-domain-gated. | Synthetic-Lethality specialist |
| 9 | **ATRA / retinoic acid signaling** | Differentiation | APL existence-proof: ATRA displaces corepressor complexes from PML-RARA, restoring differentiation transcription. CIC-DUX4 is mechanistically different (not a nuclear-hormone-receptor fusion) — **no published CIC-DUX4 + ATRA study exists**. | Established (APL) / **Theoretical** (CIC-DUX4) | None direct | V3 only | **Fusion-agnostic in principle** (if a RAR-pathway vulnerability exists, it would be a chromatin-state property, not junction-specific) — but currently no mechanistic bridge published at all. | Differentiation specialist |

### Dietary modulators (adjunctive, all with documented concentration mismatches)

| Compound | Target dependency/mechanism | Cell-line active conc. | Dietary-achievable plasma conc. | Gap | Tier | Notes |
|---|---|---|---|---|---|---|
| EGCG (green tea) | BRD4 BD1 binding / weak EZH2 modulation | 10–50 µM | 0.1–1 µM | ~10–100× | Preclinical-Cell | Same compound flagged for V1; CYP3A4/P-gp modulator at higher conc — flag for ifosfamide awareness |
| Quercetin (capers, red onion) | MCL1 downregulation + BH3-mimetic activity; weak EZH2 modulation | 10–50 µM (MCL1); ~1.97 µM CYP3A4 IC50 | sub-µM to low-µM | up to **1,000–10,000×** for MCL1 (largest gap in this vector) | Preclinical-Cell | **CYP3A4 inhibitor (IC50≈1.97µM) + documented P-gp modulator** — raised etoposide oral bioavailability 8.9%→12.7-13.6% and doxorubicin bioavailability in rat PK (PMID 21544726, 19414395). **Flag for oncologist awareness given current high-dose ifosfamide** — supplement-bolus quercetin (not whole-food) is the relevant concern. |
| Sulforaphane (broccoli/sprouts) | weak HDACi (HDAC3 depletion) | cell-line | likely sub-threshold; juicing destroys myrosinase activation | large, route-dependent | Preclinical-Cell | See MHC-I bridge section — patient's juicing practice likely delivers low active-sulforaphane exposure |
| Butyrate (fermented fiber) | HDACi | low-mM colonic | 1–13 µM systemic (indicative) | ~2–3 orders of magnitude | Preclinical (colonic) / Mechanistic (systemic) | Fusion-agnostic, low-risk, general-health-supportive via gut-immune axis (cross-ref V4 microbiome) |
| Fisetin / Genistein | CDK4 suppression (cell-line) | low-to-mid µM | nM-to-low-µM, extensively conjugated | order-of-magnitude | Preclinical-Cell | CDK4 dependency (rank 2) is genuinely validated; dietary lever is almost certainly too weak — target valid, lever weak |
| Thymoquinone (black cumin seed oil) | reported UHRF1/DNMT1/HDAC1/G9a "epidrug" downregulation | ~20 µM (Jurkat, MDA-MB-468) | no human PK data establishing tissue conc. | unknown but likely large | Preclinical-Cell, high concentration | See chemo-interaction flag below — epigenetic claims are the weaker, more overreach-prone part of the thymoquinone literature |

---

## DIETARY TRACK

### Patient regimen — differentiation/epigenetic-relevant components

| Component | Mechanism assessed | Assessment | Tier | Chemo-interaction flag |
|---|---|---|---|---|
| **Vitamin D3** | VDR/RXR target-gene differentiation signaling (p21/p27, SNAI2/EMT-suppression) | **Neutral-to-possibly-helpful, contingent on deficiency status (unknown).** Correcting a documented deficiency is a defensible VDR-pathway rationale (fusion-agnostic); if already replete, continued supplementation is most honestly "Neutral" for the differentiation axis specifically — "correct deficiency" ≠ "supplement further for added effect." | Mechanistic / Dietary-Observational | **Theoretical CYP3A4-induction interaction** — calcitriol induces intestinal CYP3A4 (PMC9262690; demonstrated for atorvastatin clearance in humans). Ifosfamide/cyclophosphamide are CYP3A4 prodrug-activation substrates; IV administration limits the practical relevance of *intestinal* first-pass induction, but flag for oncologist awareness — not a contraindication. |
| **Carrot/beetroot juice** (whole-food carotenoids) | Provitamin-A (β-carotene/α-carotene → retinal/RA via BCO1) | **Neutral-to-mildly-helpful.** Mechanistically and epidemiologically **distinct from the ATBC/CARET isolated-high-dose-β-carotene-in-smokers harm signal** (see below) — whole-food intake via juice does not directly fall under that signal. Two honest caveats: (1) juicing removes fiber/concentrates sugars — a glycemic-load consideration during active chemo; (2) patient's smoking status is unknown — relevant only to whether to *add* an isolated β-carotene supplement (this regimen does not contain one). | Dietary-Observational | None found for whole-food carotenoids + ifosfamide/VDC-IE. |
| **Broccoli (in juice)** | Sulforaphane (glucoraphanin → myrosinase-dependent conversion) | **Likely low/negligible sulforaphane delivery — Neutral, not harmful.** Juicing's non-quantitative conversion + mature-broccoli's lower glucoraphanin pool (vs. sprouts) means the "broccoli → sulforaphane → HDAC modulation" mechanism is probably not meaningfully delivered by this preparation. Still contributes fiber-precursors, vitamin C, folate, other glucosinolates. | Preclinical-Cell (mechanism) with strong delivery-route caveat | None specific. |
| **Black cumin seed oil / thymoquinone** | Reported "epidrug" (UHRF1/DNMT1/HDAC1/G9a downregulation) at ~20 µM in leukemia/breast lines | **Be skeptical — mechanism claims are cell-line-only at a concentration with no demonstrated human dietary achievability.** Better-supported activity is antioxidant/Nrf2 (V1/V2 territory, not duplicated here); the epigenetic/differentiation claims are the weaker, overreach-prone part of the literature. | Preclinical-Cell, high concentration | **[VERIFY] — THE SINGLE MOST ACTIONABLE CHEMO-INTERACTION FLAG IN THIS ENTIRE REGIMEN.** Whole *Nigella sativa* extracts show time-dependent CYP3A4 (and CYP2C19/CYP2C9) inhibition in microsome studies and have been reported able to "alter pharmacokinetics of chemotherapeutic agents by increasing plasma concentrations to above safety margins" in herb-drug-interaction reviews; however, isolated thymoquinone alone was reported in one source as **not** a CYP inhibitor or P-gp substrate (PMC12161580) — the whole-oil-vs-isolated-compound discrepancy is **unresolved**. If the whole-oil CYP3A4-inhibition signal applies, this could **reduce ifosfamide bioactivation** (the prodrug requires CYP3A4 activation) — opposite-direction concern from a CYP3A4 inducer. **Given the patient is starting high-dose ifosfamide now, raise this with the oncology team before/while starting the course.** |
| **Curcumin + piperine** | BRD4/H3K27ac modulation (carried from V1 cross-vector table) | **No direct citation for this mechanism could be located this session** ([no direct citation; mechanism inferred from general curcumin-polypharmacology literature carried in `sarcoma-vector-context v1`]). Curcumin's bioavailability limitation (Shoba 1998 caveat — n=10, single-dose, "2000% boost" not a universal multiplier) further limits any tumor-relevant exposure. Reported here for completeness/honesty, not as an active V3 mechanism for this patient. | Mechanistic at best, **mechanism-citation gap** | None specific identified this session. |
| **Liposomal vitamin C, honey, ginger/celery/apple juice components** | Not differentiation/epigenetic-axis-specific per this specialist's scope | Not assessed in this V3 output — see V1/V2 outputs for antioxidant/ROS-axis framing of vitamin C. | N/A | N/A |

### β-carotene/Vitamin A — ATBC/CARET harm signal (re-confirmed, mandatory framing)

Two large RCTs of **isolated, high-dose β-carotene supplements** in smokers/asbestos-exposed
cohorts found **harm, not benefit**:
- **ATBC** (~29,133 male Finnish smokers): β-carotene supplementation **increased lung cancer
  incidence ~18%**, overall mortality ~8%.
- **CARET** (smokers, former smokers, asbestos workers): β-carotene + retinyl palmitate combination
  showed **~28% more lung cancers**, 17% increase in overall mortality — trial terminated early.

This is a canonical "natural ≠ safe" example. **It does not directly indict this patient's
carrot/beetroot juice** (whole-food carotenoid mixture, not an isolated supplement) — but it is the
reason **no isolated β-carotene/vitamin-A supplement should be added** to this regimen, particularly
if the patient has any smoking history (unknown — flagged as a gap).

---

## CLINICAL/EXPERIMENTAL TRACK

**Tag: Clinical / Experimental — not naturally achievable; for awareness only.**

### 1. ASOs targeting CIC-DUX4 — none exist

No published CIC-DUX4-specific ASO exists (targeted searches for "CIC-DUX4 antisense
oligonucleotide," fusion-junction ASO, etc. returned nothing). The fusion junction is, in
principle, the cleanest possible ASO target (a sequence unique to the cancer cell, absent from
both wild-type transcripts) — the barrier is rarity (no dedicated drug-discovery program),
unsolved delivery to deep soft-tissue/lung-metastatic disease (no validated extrahepatic-solid-tumor
ASO delivery route exists; the milasen N-of-1 precedent, PMID 31597037, shows custom ASOs are
*possible* but were CNS-delivered intrathecally for a different disease), and — for this patient —
**a doubly-contingent applicability**: requires both a confirmed fusion (D1/D2 only, score 0 under
D3–D5) AND a resolved junction sequence.
**Tag: driver-contingent — HOLD until the driver is resolved.**

### 2. PROTACs / degraders — landscape

- **BET-protein PROTACs** (ARV-771, dBET6): Preclinical-Cell/Animal only (osteosarcoma PMC6814818,
  prostate PNAS 2016 PMID 27274050); **no BET-PROTAC has reached a registered human trial**. All
  clinical BETi remain occupancy-based inhibitors, not degraders.
- **EZH2/PRC2 degraders**: none in clinical development; current clinical agents (tazemetostat,
  valemetostat) are catalytic inhibitors, not degraders.
- **dCBP-1 (p300/CBP degrader)**: see Ranked Candidate List rank 4 — the one entry with direct
  CIC-DUX4 cell-line data (PMC8511258).
- **Cross-fusion templates (not CIC-DUX4-specific, cited as technology watch-items)**:
  - Bimodal degrader-siRNA for DNAJB1::PRKACA (fibrolamellar carcinoma) — bioRxiv preprint
    2025-04-24, DOI 10.1101/2025.04.24.650501, **not peer-reviewed**.
  - EWSR1::FLI1 "rewiring" via chemically-induced-proximity bivalent small molecules (EB-TCIP) —
    *JACS* 2025, PMC12851799/PMID 41307210 — a genuinely different mechanism class (proximity/
    rewiring rather than degradation), conceptually portable to CIC-DUX4 (see Forward Hypothesis
    below).

### 3. Clinical-trial landscape — live-verified 2026-06-14

| Drug class | Status | Key facts |
|---|---|---|
| **Tazemetostat (Tazverik)** | **WITHDRAWN WORLDWIDE FROM ALL INDICATIONS, 2026-03-09 (F5)** | Ipsen voluntary withdrawal across follicular lymphoma AND epithelioid sarcoma (the only CIC-adjacent approval, 2020-01-23, ORR ~15%, NCT02601950); SYMPHONY-1 secondary-malignancy signal (5.7% vs 0%); all active trials/expanded-access discontinued; EMA never approved it. Attrition reason **R4-regulatory/safety**, not R1-target-invalidated. |
| **Valemetostat (DS-3201b)** | Active — NCT07303387 (SWI/SNF-altered solid tumors), pediatric phase 1 (NCCH1904, ASCO 2025); FDA-approved 2022 for ATLL (different, hematologic indication) | Dual EZH1/EZH2i — broader PRC2 blockade than tazemetostat; **secondary-malignancy risk relative to tazemetostat is an open, unresolved safety question** (not assumed favorable). CIC-DUX4 eligibility for NCT07303387 uncertain (trial's literal criteria are SWI/SNF-gene alterations, not PRC2-dependency by analogy). |
| **BMS-986158** (BETi) | Active — NCT02419417 (83 patients, results published PMC9454848/PMID 36077617) + NCT03936465 (pediatric, incl. Ewing) | Clinical-Trial tier; ~30% "clinical benefit" (not RECIST) in NCT02419417; diarrhea (43%), thrombocytopenia (39%) as common AEs. |
| **AZD5153** (bivalent BRD4i) | First-in-human Phase 1 completed (AACR/MCT 2023, 34 monotherapy + 15 +olaparib) | General solid-tumor population; no sarcoma-specific cohort identified. |
| **OTX015/birabresib** | Phase 1, recurrent GBM (NCT02296476) | DLTs (thrombocytopenia) motivated development of bivalent BETi (AZD5153). No active sarcoma trial identified. |
| **ZEN-3694** | No sarcoma trial identified | Possible over-inclusion in the upstream V3 vector-context table — flagged for awareness, not removed. |
| **Palbociclib / Ribociclib / Abemaciclib** | Established (FDA/EMA, breast cancer 2015-2018); sarcoma Clinical-Trial (palbociclib GEIS phase 2, PMC10598203; abemaciclib in dedifferentiated liposarcoma) | See Ranked Candidate List rank 2. |

### 4. Driver-robustness summary (ADR-0008 applicability, this patient)

| Intervention | D1 | D2 | D3 | D4 | D5 | Tag for this patient |
|---|---|---|---|---|---|---|
| CDK4i (palbociclib/ribociclib/abemaciclib) | 1 | 1 | 1 | 1 | 1 | **Fully driver-robust** |
| BETi | 1 | 1 | 1 | 0.5 | 1 | Driver-robust |
| HDACi / DNMTi (MHC-I bridge) | 1 | 1 | 0.5 | 0.5 | 0.5 | Driver-robust (partial under D3–D5) |
| dCBP-1 (p300/CBP degrader) | 1 | 0.5 | 0.5 | 0.5 | 0.5 | Partially driver-contingent |
| EZH2i/EZH1i (valemetostat — tazemetostat off-table regardless) | 1 | 1 | 0.5 | 0.5 | 0.5 | Partially driver-robust, moot given access |
| **MCL1i / "re-arm DUX4 death program"** | **1** | **0 (0.5 DUX4-family)** | **0** | **0** | **0** | **DRIVER-CONTINGENT — HOLD** |
| **Junction-specific ASO / fusion-PROTAC** | **1** | **1** | **0** | **0** | **0** | **DRIVER-CONTINGENT — HOLD** |

**Practical implication for this patient**: CDK4i, BETi, and HDACi/DNMTi-class agents remain
relevant to discuss with an oncologist **regardless of whether the driver is ever resolved**. The
MCL1 and junction-ASO/fusion-PROTAC entries are **not actionable until and unless** the driver is
resolved (top action: **nuclear DUX4 IHC**, per ADR-0008 EVSI ranking — cheap, fast, directly
licenses or excludes the MCL1 line; long-read WGS+RNA-seq next if DUX4 IHC is ambiguous/positive
and partner identity matters; methylation array collapses D4). EZH2i is off the table as a *drug*
regardless of driver status (tazemetostat withdrawn; valemetostat unproven + open safety question).
**Resolving the driver is flagged as the single highest-value next diagnostic action for this
vector's two highest-ceiling entries (MCL1, junction-targeted approaches).**

---

## Cross-Vector Flags

- **EZH2i + retinoic acid combination** (PMC10588044, Clinical Epigenetics 2023, PAX3-FOXO1+
  rhabdomyosarcoma, Preclinical-Cell, P1-rung/ADR-0014): RA potentiates EZH2i via
  interferon-pathway activation — mechanistically adjacent to MHC-I upregulation. For V4/orchestrator
  to evaluate whether this combination logic could apply to the HDACi/DNMTi MHC-I candidates
  (rank-1/2 above) instead of EZH2i specifically, given EZH2i's now-compounded caveats.
- **BETi + MCL1i synergy** (PMID 40841513 drug-screen finding — BET inhibitors were top synergy
  hits with S64315): connects ranked candidates 1 and 6. See Forward Hypothesis FH-SL1 below.
  Driver-contingent overall (gated by the MCL1 entry's contingency).
- **dCBP-1 (p300/CBP) × BETi**: both act on the same super-enhancer axis (p300 writes H3K27ac;
  BRD4 reads it) — sequential-step combination logic (Forward Hypothesis 2, PROTAC/ASO specialist).
- **Quercetin / EGCG CYP3A4-P-gp flags**: relevant to V1 (same compounds appear there for
  RAS/ERK and BRD4 framing) — both flagged here for the patient's current high-dose-ifosfamide
  course.
- **Vitamin D3 ↔ V4 NK-cell axis**: differentiation specialist's deficiency-vs-replete framing
  should be reused by V4's NK-cell specialist rather than re-derived.
- **Butyrate ↔ V4 microbiome-immune**: colonic-vs-systemic concentration framing (this file,
  dietary modulators table) should be reused by V4's microbiome specialist.
- **ARID1A-mutant biomarker (FH-SL2)**: cross-references the V3→V4 MHC-I bridge — if this
  patient's archived tissue (P1, ADR-0011) has NGS data, ARID1A status is a near-zero-additional-cost
  readout that could independently support (or not) the EZH2i-for-MHC-I rationale, separate from
  the MCL1/driver question.

---

## Forward Hypotheses

**[Forward Hypothesis 1] — BET inhibitor + MCL1 inhibitor combination as a two-"construction-debt" attack (FH-SL1, driver-contingent).**
*Statement*: In driver-confirmed (D1/DUX4-family-D2) CIC::DUX4 cells, combining a BET inhibitor
(collapsing the p300/BRD4-built super-enhancer state sustaining ETS-driven proliferation) with an
MCL1 inhibitor (removing the anti-apoptotic buffer the DUX4 domain forces the cell to install)
acts on two independent, non-redundant "construction debts" (build-recipe Steps 5 and 3)
simultaneously — potentially durable response where either alone gives transient arrest/apoptosis
with resistance. *Mechanistic basis*: PMID 40841513 already identified BET inhibitors as the top
synergy hits with S64315 in a drug-screening library. *Experiment*: in CIC::DUX4
tumoroids/xenografts (same models as PMID 40841513), compare BETi monotherapy / MCL1i monotherapy
/ combination at matched sub-maximal doses, with long-term (weeks) regrowth/resistance readouts
and RNA-seq to test whether BETi-driven super-enhancer collapse *reduces* MCL1 transactivation
(testing whether the two debts are coupled). *Falsifier*: if BETi does not reduce MCL1
expression/dependency and the combination shows no benefit over the better single agent in durable
assays, the "two independent debts" framing is wrong (acute/additive synergy only — still useful,
weaker claim). *Why not yet tested*: the acute synergy screen exists (2025); durable-response and
mechanistic-coupling data were not reported in sources reviewed this session.

**[Forward Hypothesis 2] — ARID1A-mutant status as a driver-uncertainty-robust biomarker for EZH2i-as-MHC-I-primer (FH-SL2).**
*Statement*: If this patient's tumor carries an ARID1A loss-of-function (frameshift/truncating)
mutation — recurrently reported in CIC::DUX4 tumoroids (PMID 40841513) and, more broadly, across
CIC-rearranged cohorts independent of fusion-confirmation status (Specht 2016, PMID 27664537) —
this could serve as an **independent, driver-uncertainty-robust biomarker** supporting the
EZH2i-for-MHC-I-priming rationale via the cBAF-disruption → PRC2-dominance mechanism documented in
SMARCB1-deficient sarcomas, applied here via ARID1A instead of SMARCB1. *Mechanistic basis*: cBAF
and PRC2 are in epigenetic antagonism at shared loci (BAF normally evicts PRC2; BAF loss → PRC2
dominance); ARID1A truncation causes cBAF-assembly failure, mechanistically analogous (though not
subunit-identical) to SMARCB1 loss. *Experiment*: (1) test whether ARID1A-mutant CIC::DUX4
tumoroids show greater EZH2i-induced MHC-I/H3K27me3 change than ARID1A-WT tumoroids (if comparator
lines exist); (2) check this patient's archived NGS data (P1, ADR-0011) for ARID1A status at
near-zero additional cost. *Falsifier*: if EZH2i-induced MHC-I/H3K27me3 changes are equivalent in
ARID1A-mutant vs. ARID1A-WT models, ARID1A status is not a useful stratifier and the SMARCB1
analogy does not transfer via ARID1A. *Why not yet tested*: the ARID1A finding is from a 2025
paper whose primary focus was MCL1, not EZH2/MHC-I — this cross-connection has not, to this
catalog's knowledge, been explicitly drawn before. **Note**: this hypothesis is independently
weakened by the broader EZH2i premise caveat (PMC10814785) above — it is offered as a
biomarker-stratification idea *if* EZH2i is ever revisited (e.g., a future EZH1/2i with a better
safety profile than tazemetostat/valemetostat), not as a reason to prioritize EZH2i now.

**[Forward Hypothesis 3] — CIC-DUX4 chromatin-accessibility screen for RAR/RXR target loci (differentiation specialist).**
*Statement*: If CIC-DUX4's p300-dependent super-enhancer program represses a meaningful subset of
canonical RAR/RXR target genes, ATRA exposure in a CIC-DUX4 cell model would produce measurable
de-repression of a defined RAR-target panel (RARB, CYP26A1, CRABP2), even without reproducing
APL's terminal-differentiation phenotype. *Mechanistic basis*: CIC-DUX4 ChIP-seq/ATAC-seq data
(PMC10814785) already show differentiation-pathway genes repressed in the CIC-DUX4-on state and
re-activated on CIC-DUX4 depletion — the open question is whether this repressed program overlaps
the RAR/RXR target-gene set, and whether ATRA alone (vs. CIC-DUX4 depletion) can access it.
*Experiment*: treat existing CIC-DUX4 patient-derived lines (PMC10814785/PMC8511258) with ATRA at
clinically-achievable concentration (~1 µM, per PMC5399637 PBPK data), ATAC-seq/RNA-seq readout on
the RAR/RXR panel and the CIC-DUX4-repressed differentiation-gene set. A positive result (even
partial de-repression) would be the first direct bridge from the APL existence-proof to CIC-DUX4
and would motivate an ATRA+EZH2i combination study (building on the PMC10588044 rhabdomyosarcoma
precedent — itself a P1-rung, different-fusion signal). *Falsifier*: no de-repression of the
RAR/RXR panel at clinically-achievable ATRA concentration. *Why not yet tested*: CIC-DUX4 is
ultra-rare with very few patient-derived models; differentiation approaches have historically been
deprioritized relative to the EZH2i/BETi/CDK4i clinical-track candidates — this is a low-cost,
hypothesis-generating screen runnable on existing lines without new patient material.

**[Forward Hypothesis 4] — VDR-status stratification as a tumor-intrinsic biomarker, independent of supplementation (differentiation specialist).**
*Statement*: Tumor-intrinsic VDR expression (not serum vitamin D status) predicts whether a
CIC-DUX4 (or fusion-unconfirmed atypical) tumor retains any responsiveness to VDR-pathway
engagement — a tumor with epigenetically silenced VDR would be unresponsive to any vitamin D
intervention regardless of serum 25-OH-D, while one retaining VDR/RXR/coactivator function might
show the SNAI2/EMT-suppressive effect documented in osteosarcoma (PMC10203545) if calcitriol
signaling were locally augmented (e.g., a VDR agonist with better tumor PK than dietary D3, or
CYP24A1 inhibition — CYP24A1 catabolizes active vitamin D and is sometimes a tumor resistance
mechanism). *Mechanistic basis*: the osteosarcoma finding establishes the mechanism is real in at
least one sarcoma; whether CIC-DUX4 retains the receptor/complex is unknown. *Experiment*: IHC or
RNA-seq for VDR and CYP24A1 in available CIC-DUX4 specimens/lines — a low-cost addition to existing
biomarker panels (cross-ref ADR-0011, candidate low-burden archived-tissue P1 assay); if VDR
expressed and CYP24A1 not markedly overexpressed, motivates a follow-up calcitriol-dose-response or
CYP24A1-inhibitor (e.g., VID400, Theoretical) experiment. *Falsifier*: no VDR expression or no
SNAI2/EMT-marker change under calcitriol exposure in VDR-expressing lines. *Why not yet tested*:
VDR status has not been a standard CIC-DUX4 characterization biomarker (focus has been
fusion-detection and p300/EZH2 dependency); requires no new patient recruitment, only an additional
stain/probe on existing archived material.

**[Forward Hypothesis 5] — Repurpose EWSR1::FLI1 "transcriptional rewiring" chemical biology as a CIC-DUX4 template (PROTAC/ASO specialist).**
*Statement*: Both EWSR1::FLI1 and CIC::DUX4 are "undruggable" transcription-factor fusions whose
oncogenic activity comes from aberrant transcriptional output (super-enhancer hijacking), not an
enzymatic active site. The 2025 EB-TCIP chemically-induced-proximity approach (PMC12851799)
degrades/rewires EWSR1::FLI1's transcriptional consequences via proximity-induced chromatin
remodeling. *Mechanistic basis*: same "undruggable fusion via transcriptional output" class;
proximity/rewiring is a third mechanism category (neither ASO nor classical PROTAC). *Experiment*:
engineer a CIC::DUX4 cell-line model (PMC10814785 lines) with an FKBP12^F36V tag on
endogenous/exogenous CIC-DUX4, treat with a bivalent small molecule recruiting it to a
pro-apoptotic chromatin locus (e.g., BCL6-bound sites, as in the EWSR1::FLI1 paper), read out
fusion-target-gene suppression and apoptosis by RNA-seq/flow cytometry. *Falsifier*: no
fusion-target suppression or apoptosis induction despite successful tagging and proximity
induction. *Why not yet tested*: EB-TCIP is brand-new (2025), developed specifically for
EWSR1::FLI1; cross-application to CIC-DUX4 would require new academic collaboration, not yet a
published/funded direction. **Tag: this is also a fusion-protein-targeted approach — driver-contingent (D1/D2 only) like the MCL1 and junction-ASO entries**, but is recorded here as a *technology* watch-item rather than a near-term clinical candidate.

---

## Atypical-Case Notes (ADR-0008, ~5% fusion-unconfirmed)

| Category | Entries | Applies to fusion-unconfirmed (D3–D5)? |
|---|---|---|
| **Fully driver-robust (fusion-agnostic)** | CDK4i, HDACi/DNMTi (MHC-I bridge), Vitamin D3/VDR, ATRA/retinoid signaling, butyrate, carotenoids, sulforaphane, ARID1A-bridge biomarker (FH-SL2/4 — largely robust) | **Yes, fully** (or largely, for ARID1A) |
| **Driver-robust, partial under D4** | BETi | Yes, with reduced confidence under D4 (phenocopy) |
| **Partially driver-contingent** | dCBP-1 (p300/CBP degrader) — strongest D1/D2, score 0.5 under D3–D5; EZH2i/EZH1i (moot regardless given access) | Partial |
| **FULLY DRIVER-CONTINGENT — HOLD UNTIL DRIVER RESOLVED** | **MCL1 inhibitors/BH3-mimetics** (rank 1, highest-ceiling entry in this vector); **junction-specific ASOs**; **hypothetical fusion-protein-targeted PROTACs/CIPs** (FH5) | **NO for D3–D5.** Score 0 under D3, D4, D5; D2 only 0.5 if rare partner is itself DUX4-family. |

**For this patient specifically**: the **single highest-value next diagnostic action across this
entire vector** is **nuclear DUX4 IHC** (cheap, fast, per ADR-0008 EVSI ranking) — a positive result
strongly implicates D1 and directly licenses the MCL1 and junction-targeted lines (rank-1 entry
and Forward Hypothesis 5); a negative result takes them off the table, leaving the fully
driver-robust entries (CDK4i, HDACi/DNMTi MHC-I bridge, ATRA/VDR differentiation axis, BETi) as the
standing V3 candidates. Long-read WGS+RNA-seq (resolves D1/D2/D3, recovers cryptic junctions) and
genome-wide methylation array (collapses D4) are next-tier tests if DUX4 IHC is ambiguous/positive
and partner identity matters. **This file does not re-derive the EVSI ranking** — see
`simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md` and
`simulation-output/diagnostic-information-gain-layer.md`.

---

## What I Could Not Establish

1. **No published CIC-DUX4 + ATRA (or any retinoid) study exists** — the ATRA/APL generalization to
   CIC-DUX4 is, at present, analogical at the "differentiation therapy is a strategy class" level,
   with no demonstrated mechanistic bridge (Forward Hypothesis 3 proposes how to close this gap).
2. **Patient's serum 25-OH-vitamin-D level and smoking status are unknown** — both materially change
   the assessment of the vitamin D3 and carrot/beetroot-juice components (deficient-vs-replete;
   ATBC/CARET smoking-interaction relevance for any *future* supplement decisions).
3. **No human PK data establishing that black cumin seed oil reaches the ~20 µM thymoquinone
   concentration used in the cell-line "epidrug" studies** — likely a concentration mismatch.
4. **Whole-extract vs. isolated-thymoquinone CYP3A4/P-gp discrepancy is unresolved** — two
   different characterizations exist in the literature; cannot adjudicate which applies to a
   commercial black cumin seed oil product. **[VERIFY]** flagged for oncologist review given the
   timing (starting high-dose ifosfamide now).
5. **Quantitative plasma-butyrate citation (1–13 µM)** came from aggregated search summaries, not a
   single pinned primary source — qualitative colonic-vs-systemic gap is well-supported across
   multiple sources, but the precise figure should be re-verified if it becomes load-bearing.
6. **BETi sensitivity has no direct CIC-DUX4 dose-response data** — the closest CIC-DUX4 chromatin
   paper (PMC10814785) targets p300/CBP, not BRD4 directly; "BRD4 addiction" is better supported as
   "BRD4 is essential like almost everywhere" (DepMap: non-selective) than as CIC-DUX4-*selective*
   synthetic lethality.
7. **The ARID1A→EZH2-dependency mechanistic bridge (FH-SL2) is inferred by analogy to
   SMARCB1-deficient sarcomas, not demonstrated in CIC-DUX4** — DepMap shows EZH2 is not a CRISPR
   dependency in the Ewing proxy (+0.01, 0% dependent), which argues against an EZH2
   *survival*-dependency framing regardless of ARID1A status (though the Ewing-proxy lines were not
   selected for ARID1A status, so an ARID1A-mutant-selective effect is not specifically ruled out).
8. **Whether the MCL1 dependency reported in PMID 40841360's biobank is truly CIC::DUX4-*selective*
   vs. shared with the biobank's Ewing models** was not independently verified beyond
   abstract-level framing — the direct ChIP-seq transactivation evidence in PMID 40841513 is the
   stronger argument for driver-specificity and is what this reconciliation leans on.
9. **The palbociclib CIC-DUX4 in-vivo "limited effect" claim and the CCNE1-CDK2/dinaciclib JCI 2019
   PMID** were both flagged `[VERIFY]` by the synthetic-lethality specialist — found via search
   summaries, not independently re-opened at the primary source this session.
10. **Whether the tazemetostat withdrawal's "all active clinical trials" language formally includes
    NCT04917042 (MPNST phase 2)** — the announcements name follicular lymphoma and epithelioid
    sarcoma specifically as withdrawn indications while separately stating "all active
    tazemetostat clinical trials and expanded access programs" are discontinued; no trial-by-trial
    confirmation found. **[VERIFY]** before assuming any tazemetostat trial access exists anywhere.
11. **Curcumin's BRD4/H3K27ac mechanism claim** (carried from the V1 cross-vector table into V3 via
    `sarcoma-vector-context v3`) — **no direct citation for this specific mechanism was located by
    the epigenetic specialist this session.** Reported in the dietary track above as a
    citation gap, not re-asserted as established.
12. **Red-team self-challenge (Part D, recorded per ADR-0017):**
    - *Load-bearing assumption*: CIC-DUX4's actionable epigenetic dependency is p300/CBP
      (PMC10814785), not PRC2/EZH2 — this single finding cascades through the EZH2i downgrade,
      the dCBP-1 entry's prominence, and FH-SL2's framing as "if EZH2i is ever revisited."
    - *Disconfirmation*: the strongest evidence *against* this assumption is the historical
      tazemetostat-for-epithelioid-sarcoma approval itself (PRC2/EZH2 dependency is real in
      SMARCB1-loss contexts) and the ARID1A-mutation finding (a real cBAF-disruption lesion in
      CIC::DUX4 that, by the SMARCB1 analogy, *would* predict PRC2 dependency) — but DepMap's
      EZH2-non-dependency finding in the Ewing proxy and PMC10814785's direct CIC-DUX4 chromatin
      data both point the other way. Both sides were searched with equal effort.
    - *Alternative*: a hypothesis outside this vector's lane — if ARID1A loss creates a
      synthetic-lethal vulnerability to something *other* than EZH2 (e.g., a different
      BAF-PRC2-antagonism-pathway target, or a DNA-damage-repair vulnerability ARID1A-mutant
      tumors are known to carry in other cancers), that would sit closer to a V2/DNA-repair framing
      than V3 — flagged for the orchestrator as a possible cross-vector thread, not forced into V3.
    - *Flip test*: if PMC10814785 is wrong and CIC-DUX4 *is* meaningfully PRC2-dependent, EZH2i
      regains mechanistic plausibility — but it remains **F5/inaccessible** regardless (tazemetostat
      withdrawn, valemetostat's safety profile unresolved). The practical conclusion ("EZH2i is not
      an actionable V3→V4 bridge candidate for this patient right now") **survives the flip test**;
      only the *reason* (premise vs. access) would change.
    - *Steer audit*: the prompt's framing flagged tazemetostat as needing careful, non-blurred
      handling — this reconciliation treated that as a verification target (live-checked,
      concordant across two independent specialists), not a conclusion to confirm by default; the
      withdrawal finding was *additional* to, not a substitute for, the premise-level caveat from
      PMC10814785, which neither specialist was steered toward and both found independently.

---

## Bibliography

All citations below are reproduced from the four specialist sub-agent files; access date for all
live-verified web sources is **2026-06-14**.

- Bakaric et al., *Cancers* 2024;16(2):457, PMID 38275898, DOI 10.3390/cancers16020457, GSE248040 —
  CIC-DUX4 p300/CBP chromatin profiling.
- PMC8511258 — "Inactivation of the CIC-DUX4 oncogene through P300/CBP inhibition" (dCBP-1).
- PMID 40841513, DOI 10.1038/s41467-025-62629-6, PMC12370961 — "Patient-derived tumoroids from
  CIC::DUX4 rearranged sarcoma identify MCL1 as a therapeutic target," *Nat Commun* 2025.
- PMID 40841360, DOI 10.1038/s41467-025-62673-2 — "Small round cell sarcoma tumoroid biobank
  reveals CIC::DUX4 sarcoma vulnerability to MCL-1 inhibition," *Nat Commun* 2025.
- Wang et al. 2019, PMC6843866 — HDACi MHC-I upregulation, glioma.
- *Nat Commun* 2025, DOI 10.1038/s41467-025-62934-0 — romidepsin immune-landscape reshaping, liver
  cancer.
- Luo et al., *Nat Commun* 2018, DOI 10.1038/s41467-017-02630-w — guadecitabine MHC-I demethylation.
- Ipsen press releases 2026-03-09 (ipsen.com/press-release/...-3251503, ...-3252192) — tazemetostat
  worldwide withdrawal; corroborated by OncLive, CancerNetwork, Cancer Therapy Advisor, Oncology
  Nurse Advisor, oncologynewscentral.com.
- ClinicalTrials.gov NCT02601950 (tazemetostat sarcoma basket), NCT04917042 (tazemetostat MPNST),
  NCT07303387 (valemetostat SWI/SNF-altered solid tumors), NCT02419417 + PMC9454848/PMID 36077617
  (BMS-986158), NCT03936465 (BMS-986158 pediatric incl. Ewing), NCT02296476 (OTX015/birabresib).
- ASCO 2025 abstract JCO.2025.43.16_suppl.10003 — valemetostat pediatric phase 1.
- AACR *Molecular Cancer Therapeutics* 2023 — AZD5153 first-in-human.
- PMC10598203, *Signal Transduct Target Ther* 2023 — palbociclib phase 2 sarcoma (GEIS).
- ASCOPubs *JCO Precision Oncology* PO.21.00211 — abemaciclib dedifferentiated liposarcoma.
- Yoshimoto et al., *Cancer Res* 2017;77(11):2927-37, PMID 28404587 — Ccnd2 upregulation via
  ETV4/PEA3 in mouse CIC-DUX4 models.
- Specht K et al., *Hum Pathol* 2016;58:161-170, PMID 27664537 — ARID1A/1p loss in CIC-rearranged
  cohorts.
- bioRxiv 10.1101/2025.04.24.650501 — DNAJB1::PRKACA degrader-siRNA (preprint, not peer-reviewed).
- PMC12851799/PMID 41307210, *JACS* 2025 — EWSR1::FLI1 EB-TCIP rewiring.
- PMC6814818 — ARV-771 in osteosarcoma; PMID 27274050 (PNAS 2016) — ARV-771 original.
- PMID 31597037, *NEJM* 2019 — milasen N-of-1 ASO precedent.
- PubMed 20929432 — ATRA/APL mechanism.
- PMC10588044, DOI 10.1186/s13148-023-01583-w — EZH2i + RA in PAX3-FOXO1+ rhabdomyosarcoma.
- PMC11119684 — retinoic acid in Ewing sarcoma stemness/cell-cycle.
- PMC5399637 — ATRA PBPK model (clinical concentration reference).
- AACR Abstract 2289; AJCN; Tanvetyanon & Bepler 2008 (Cancer/Wiley) — ATBC/CARET β-carotene harm
  signal and smoking-status interaction.
- PMC9003440; PubMed 10064337 — Vitamin D / VDR target genes.
- PMC10203545 — vitamin D, SNAI2/EMT, osteosarcoma.
- PMC9262690; ScienceDirect S0960076012001689; PMC8528301 — vitamin D/CYP3A4 interaction.
- PMC4629881 — sulforaphane bioavailability, myrosinase.
- ScienceDirect S0308814618310628 — glucoraphanin/sulforaphane evolution in juice preparation.
- PMC6346118; PMC6806744; PMC8253137 — butyrate HDACi, colonic vs. systemic.
- PubMed 31058255; MDPI 2073-4425/12/5/622 — thymoquinone "epidrug" claims.
- PMC12161580/PLOS ONE 10.1371/journal.pone.0323804; Academia.edu Nigella sativa CYP3A4 PDF
  (lower-confidence secondary source) — thymoquinone/whole-extract CYP3A4-P-gp discrepancy.
- Clin Cancer Res 2010;16(23):5679, PMC3142809/PMC3069720 — quercetin/Mcl-1.
- PMID 21544726; PMID 19414395 — quercetin-doxorubicin/etoposide rat PK (P-gp).
- `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md` (ADR-0008)
  and `tumorigenesis-build-recipe.md` (ADR-0007) — driver-hypothesis space, applicability matrix,
  build-recipe steps referenced throughout.
- `sims/02-dependency-mining/RESULTS.md` — DepMap 24Q4 CRISPR proxy analysis (BRD4, EZH2, CDK4,
  CCND1/2 dependency figures).

*Research simulation / hypothesis generation only. Not medical advice. No dosing, start/stop, or
treatment recommendations are made or implied.*
