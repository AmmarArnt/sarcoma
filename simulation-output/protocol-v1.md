# CIC-Rearranged Sarcoma — Multi-Vector Hypothesis Catalog (v1)

---

## KEY-MAP CALLOUT — What Each Vector / Team Represents (read first)

This catalog synthesizes four parallel "attack vectors" plus two supplementary teams. A later reader must know what the labels mean:

| Label | Name | What it represents (one line) |
|---|---|---|
| **V1** | **Rate Limiting** | Throttle the oncogenic loop's speed and output — dampen RAS/ERK amplitude, BRD4 super-enhancer amplification, and CDK4/CCND1 cell-cycle execution **downstream** of the fusion. Does not fix the fusion. |
| **V2** | **Compiler Protection** | Reduce the rate at which neighboring at-risk cells acquire a *new* translocation — lower ROS/DSB burden, support DNA-repair fidelity, calm inflammation. Upstream prevention, not tumor-directed. |
| **V3** | **Hot Patching** | Restore tumor-suppressor / differentiation signaling in cells that already carry the fusion — EZH2i, BETi, CDK4/6i, HDACi, DNMTi, differentiation agents; dietary contribution is weakest here. |
| **V4** | **Immune Watchdog** | Restore immune visibility and clearance — MHC-I restoration (depends on V3 priming), checkpoint blockade, NK missing-self killing, neoantigen vaccines. |
| **mRNA Team** | **mRNA COVID-19 Vaccine Research Team** | Supplementary. Asks whether BNT162b2 vaccination modifies the immune/inflammatory/genomic context relevant to this sarcoma. Feeds V2 and V4. Does not attack the tumor. |
| **Metastatic Specialist** | **Metastatic Disease Specialist** | Orchestrator sub-agent. Asks, per vector, whether metastatic (here: lung) biology changes the picture. |

---

## Framing

This is a **research-simulation output, not a treatment plan and not medical advice.** Its purpose, in order: (1) a structured forward-simulation research exercise; (2) personal exploration of the literature; (3) only if a non-obvious, mechanistically grounded hypothesis emerges, a starting point for a conversation with a qualified oncologist. No entry here is a dose, a protocol, or a start/stop instruction for any therapy. The intended value is the *structure, honest grounding, and the Forward Hypotheses* — not the number of entries. Most claims below are Mechanistic or Preclinical tier; direct evidence in CIC-rearranged sarcoma is essentially absent for every dietary compound and for most clinical agents (the rationale is extrapolated from related fusion-driven sarcomas — Ewing, epithelioid, synovial).

**Atypical / fusion-status note (load-bearing for this case).** Approximately 5% of tumors that present clinically and histologically as CIC-rearranged sarcoma do not have a confirmed fusion (CIC-DUX4, CIC-NUTM1, CIC-FOXO4, CIC-LEUTX) on genomic testing. **This patient is in that fusion-unconfirmed subgroup.** Throughout this catalog every recommendation is tagged:
- **`fusion-agnostic (may apply to atypical ~5% cases)`** — operates on downstream machinery (EZH2/PRC2, BRD4, CDK4/CCND1, differentiation, epigenetic MHC-I priming, all dietary V1/V2 compounds, immune checkpoint, NK). Still potentially applicable to this patient.
- **`fusion-confirmed only — POSSIBLY INAPPLICABLE to this patient`** — depends on the fusion junction itself (junction ASOs, junction-specific neoantigen vaccines, junction CAR-T/TCR-T, fusion PROTACs).

### Patient case (carried into framing; clean-slate, no stored individual memory used)
Soft-tissue CIC-rearranged sarcoma, diagnosed June 2024, **fusion-UNCONFIRMED atypical subgroup**. Primary: biceps femoris, right thigh. At diagnosis: 12 lung metastases. Treatment: EURO EWING (VDC/IE), 14 cycles, good response; surgery Jan 2025 (>95% necrotic); radiation to leg + whole-lung irradiation (WLI). NED May 2025 → May 2026; **oligometastatic relapse (one lung lesion)**. **NOW preparing HIGH-DOSE IFOSFAMIDE.** This clinical reality (imminent ifosfamide; prior doxorubicin/vincristine/etoposide/cyclophosphamide; prior WLI; lung-only metastatic pattern) drives the conflict-resolution and interaction sections below.

---

## Top-Level Findings

1. **The strongest mechanistic entry point for this tumor is BRD4/super-enhancer addiction, and it is fusion-agnostic** — BET inhibition collapses ETS super-enhancers even if the fusion protein remains; this is the most robust target for a fusion-unconfirmed case. *[Clinical-Trial; no direct CIC-DUX4 data]*
2. **The cleanest V3→V4 bridge is EZH2 inhibition (tazemetostat) restoring MHC-I**, enabling T-cell recognition; this is the catalog's central cross-vector dependency. *[Established (epithelioid sarcoma, FDA); Clinical-Trial (CIC context)]*
3. **The NK missing-self arm is a non-obvious, well-grounded angle**: the same MHC-I-low state CIC-rearranged cells use to hide from T-cells makes them targets for NK cells — and the metastatic/relapsed clone is *more* likely MHC-I-low by immune selection. *[Mechanistic / Clinical-Trial]*
4. **An NK-vs-MHC-I sequencing tension is real and must not be papered over**: epigenetic MHC-I restoration (helps T-cells) reduces NK missing-self visibility (hurts NK). Suggested ordering is NK-first → epigenetic priming → checkpoint. *[Mechanistic]*
5. **The single highest-priority actionable item for THIS patient is not a recommendation to add anything — it is the interaction screen on what he already takes**: piperine (in curcumin+piperine) and thymoquinone (black cumin seed oil) are CYP3A4 inhibitors, and ifosfamide is a CYP3A4-activated prodrug. *[Mechanistic / Preclinical; PK literature]*
6. **For dietary V1/V2 compounds, the decisive limitation is concentration mismatch**: dietary plasma levels run 10–500× below the cell-line concentrations at which the cited mechanisms operate. Sulforaphane has the most favorable ratio (3–10×), but the patient's broccoli *juicing* destroys myrosinase and likely yields near-zero sulforaphane. *[Preclinical-Cell]*
7. **Omega-3 EPA/DHA is the best cross-vector dietary compound** (V1 membrane/RAS, V2 SPM anti-inflammatory, V4 NK) with the least chemo-interaction risk — and it is **absent** from the patient's regimen (a notable gap), particularly given the post-WLI inflammatory lung field. *[Dietary-Observational + Mechanistic]*
8. **mRNA COVID-19 vaccination is a null finding for this patient's current biology** — no persistent immune/inflammatory/genomic effect at >2 years post-vaccination — with one practical carry-forward: anti-PEG antibodies could reduce delivery of any *future* LNP-mRNA cancer vaccine. *[Clinical observational]*
9. **The antioxidant-vs-ROS-chemo and antioxidant-vs-metastasis conflicts are genuine and unresolved**: high-dose liposomal vitamin C during ROS-contributing chemo (doxorubicin past; ifosfamide partial) and the Sayin 2014 metastasis signal both counsel caution in a patient with residual disease. Deferred to clinical judgment. *[Preclinical-Animal]*
10. **V2 is the least applicable vector to the current disease** — the relapsed lesion already carries the driver; V2's value here is narrow (modifying the post-WLI lung niche), not trajectory-changing. *[Mechanistic]*

---

## Naturally Achievable Track

> Every entry below carries the orchestrator-level annotation: **"Potential interactions with standard-of-care chemotherapy and concurrent medications — must be reviewed by the patient's oncologist before any change."** This is doubly important here because high-dose ifosfamide is imminent.

### Diet (mechanistically grounded, food-level)

| Compound | Vector(s) | Mechanism (1 sentence) | Evidence tier | CIC-DUX4 specific? | Food sources | SOC contraindications |
|---|---|---|---|---|---|---|
| Omega-3 EPA/DHA | V1, V2, V4 | Alters membrane lipid-raft composition (impairs RAS clustering) and yields resolvins/protectins (ALX/FPR2 → ↓NF-κB/NOX2); supports NK membrane function | Dietary-Observational + Mechanistic | None direct | Mackerel, sardines, wild salmon, herring, oysters | Anti-platelet at high supplement doses — relevant peri-surgery/peri-ifosfamide; food-level intake low risk |
| Sulforaphane (properly activated) | V1, V3, V4 | Weak class-I HDAC inhibition (5–30 µM cell lines) + Nrf2 activation; possible MHC-I support (UNESTABLISHED at dietary exposure) | Preclinical-Cell | None direct | Broccoli **sprouts**, chopped/chewed (myrosinase) — **juicing destroys myrosinase → near-zero yield** | Nrf2/ROS-axis: theoretical interference with doxorubicin/ifosfamide at supplement doses; culinary intake subclinical |
| Quercetin | V1, V2 | Multi-kinase RTK/RAS inhibition + weak EZH2 modulation; severe concentration mismatch at dietary intake | Preclinical-Cell | None direct | Capers, raw red onion outer layers, apple skin | CYP3A4/P-gp modulation at supplement doses; juice-level below clinical threshold |
| Apigenin / Luteolin | V1 | Apigenin reduces ETS-factor expression; luteolin is a cell-cycle modulator (both 50–250× above food-achievable) | Preclinical-Cell | None direct | Celery leaves, parsley, chamomile | Apigenin: CYP2C9 + modest CYP3A4 at supplement doses; juice level low |
| Fisetin | V1 | CDK4 suppression + ETS inhibition in some lines; senolytic activity in aging models | Preclinical-Cell | None direct | Strawberries, apple skin, mango | None at food level documented |
| Vitamin D3 (deficiency correction) | V3, V4 | Calcitriol-VDR → CDKN1A/p21 (partial G1 exit) and NK NKG2D upregulation | Mechanistic | None direct | Sunlight, fatty fish (supplement if deficient) | No documented ifosfamide/VDC interaction; hypercalcemia monitoring |
| Zinc (deficiency correction) | V1, V2, V4 | Cofactor for Ku70/Ku80, p53 zinc finger, PARP1 (repair) and NK maturation (thymulin) | Mechanistic | None direct | Oysters, pumpkin seeds, meat | Excess (>40 mg/d) displaces copper → anemia/neuropathy |
| Whole-plant fiber / fermented foods | V4 (microbiome) | Fermentable fiber → SCFA; diversity associated with checkpoint response (melanoma/NSCLC — **not** sarcoma) | Dietary-Observational | None direct | Legumes, whole grains, vegetables; yogurt, kefir, kimchi | Avoid unpasteurized ferments during neutropenia post-ifosfamide |
| Lycopene | V1 (weak) | ERK downregulation reported (prostate models) | Dietary-Observational | None direct | Cooked tomato/paste + fat, watermelon | None at food level documented |

### Supplements (only where a safety profile is established; published trial dose-ranges cited — none for CIC-DUX4)

| Compound | Vector(s) | Mechanism | Tier | Published dose-range (indication ≠ CIC-DUX4) | SOC flag |
|---|---|---|---|---|---|
| Curcumin (± piperine) | V1, V2, V4 | BRD4-chromatin disruption (5–20 µM cell lines); NF-κB inhibition | Preclinical-Cell | Phase I safety 4–8 g/d conventional (Cheng AL et al., *Anticancer Res* 2001, PMID 11763884) | **HIGH** — piperine CYP3A4+P-gp; see Interaction Map |
| EGCG | V1, V2 | BRD4 BD1 binding + weak EZH2 modulation (10–50 µM, 10–100× above dietary plasma) | Preclinical-Cell | 400–800 mg/d prostate prevention (Bettuzzi S et al., *Cancer Res* 2006, PMID 16397214); hepatotoxicity signal high-dose | P-gp inhibition → vincristine/etoposide; consult oncologist |
| Vitamin D3 | V3, V4 | As above | Mechanistic | 2000 IU/d (VITAL, Manson JE et al., *NEJM* 2019, PMID 30415629; null for cancer incidence) | Low; correct deficiency first |
| Selenium | V1, V2 | Selenoprotein/TrxR cofactor; apoptosis-threshold modulation | Preclinical + Dietary-Observational | SELECT null (Lippman et al., *JAMA* 2009, PMID 19066370); UL 400 µg/d | Narrow window; prefer 1–2 Brazil nuts/d to supplements |
| Berberine | V1 | AMPK → mTORC1 suppression → ↓MYC translation; ~1% oral bioavailability | Preclinical-Cell | 500 mg TID metabolic trials (Zhang Y et al., *JCEM* 2008, PMID 18397984) | CYP3A4 inhibition — same ifosfamide concern |

### Lifestyle
- **Vitamin D status via sunlight/diet** — correct documented deficiency (clearer evidence than replete supplementation).
- **Whole-food fiber over juicing for microbiome** — the patient's juice-based approach removes most prebiotic fiber; whole broccoli, skin-on apple, legumes provide far more substrate. (Juicing also defeats sulforaphane — see Diet table.)
- **Marine omega-3 intake** (2–3 servings fatty fish/week) addresses the regimen's main nutritional gap and the post-WLI lung-inflammation context.
- **Sleep / exercise** — general supportive-care, no CIC-DUX4-specific claim made.

---

## Clinical / Experimental Track (For Oncologist Discussion Only)

> Tag: **Clinical / Experimental — not naturally achievable; for awareness only.** None of these is approved for CIC-rearranged sarcoma. FDA/EMA columns refer to the cited *other* indication.

| Intervention | Vector(s) | Mechanism | Evidence tier | Status FDA | Status EMA | Trial IDs | Fusion tag / Notes |
|---|---|---|---|---|---|---|---|
| Tazemetostat (EZH2i) | V3→V4 | ↓H3K27me3 at HLA-A/B/C, TAP1/2, B2M, NLRC5 → MHC-I restoration; de-represses CDKN2A | Established (epithelioid sarcoma) / Clinical-Trial (CIC context) | Accelerated approval epithelioid sarcoma 2020-01-23 (also FL) | **Must be verified independently — not confirmed here**; status differs from FDA | NCT01897571, NCT02601950 | fusion-agnostic. Cleanest V3→V4 bridge |
| Entinostat (class-I HDACi) | V3→V4 | HDAC1/2/3 inhibition → APM/NLRC5 de-repression → MHC-I; p21 | Clinical-Trial | Not approved (breakthrough designations elsewhere) | Not approved | NCT02890069, NCT01253278 | fusion-agnostic |
| Vorinostat (pan-HDACi) | V3→V4 | Same APM de-repression; broader, more toxic | Established (CTCL) / Clinical-Trial (sarcoma) | Approved CTCL 2006 | **Not approved for CTCL in EU** (withdrawn/never authorized — verify current status) | — | fusion-agnostic; toxicity concern with ifosfamide |
| OTX015 / BMS-986158 / AZD5153 (BETi) | V1, V3, V4 | BRD4 bromodomain inhibition → collapse ETS super-enhancers (↓ETV4/5, MYC, CCND1) + ↓PD-L1 super-enhancer | Clinical-Trial | Not approved | Not approved | NCT01713582, NCT02419417; AZD5153 verify at ClinicalTrials.gov | fusion-agnostic; strongest mechanistic entry point |
| Palbociclib / Ribociclib / Abemaciclib (CDK4/6i) | V1, V3 | CDK4/6 inhibition → Rb hypophosphorylation → E2F suppression → G1 arrest | Established (HR+ breast) / Clinical-Trial (sarcoma) | Approved HR+ breast (2015–2017) | Approved HR+ breast (EMA, 2016–2018) | NCT03677388, NCT02571829, NCT02664909 | fusion-agnostic; additive myelosuppression with ifosfamide — sequential scheduling |
| Azacitidine / Decitabine (DNMTi) | V3→V4 | ERV demethylation → dsRNA → STING → type-I IFN → MHC-I (viral mimicry) | Established (MDS/AML) / Clinical-Trial (solid) | Approved MDS/AML | Approved MDS/AML | (mechanism: Chiappinelli 2015 Cell; Roulois 2015 Cell) | fusion-agnostic; orthogonal STING path |
| Pembrolizumab / Nivolumab (anti-PD-1) ± Ipilimumab | V4 | Checkpoint release on (epigenetically primed) CD8+ T-cells; ipilimumab adds Treg depletion | Established (melanoma/NSCLC/RCC) / Clinical-Trial (sarcoma, modest ORR SARC028) | Approved multiple | Approved multiple | NCT02301039 (SARC028); NCT02978625 (D'Angelo, *NEJM* 2018, PMID 30501812) | fusion-agnostic; efficacy depends on V3 MHC-I priming |
| N-803 (nogapendekin alfa inbakicept, IL-15 superagonist) | V4 (NK) | IL-15/IL-15Rα-Fc → NK proliferation/cytotoxicity vs MHC-I-low cells | Established (NMIBC, with BCG) / Clinical-Trial (solid) | Approved NMIBC + BCG 2024 (Anktiva) | **Not approved (verify current EMA status)** | NCT03055780 | fusion-agnostic; deploy BEFORE MHC-I restoration |
| Adoptive NK transfer | V4 (NK) | Haploidentical NK in lymphodepleted host → IL-7/15 homeostatic expansion → kill MHC-I-low cells | Clinical-Trial (heme) / Preclinical (solid) | Not approved | Not approved | (heme precedent: Ruggeri, *Science* 2002, PMID 11786547 — not directly transferable) | fusion-agnostic; post-ifosfamide window |
| Personalized neoantigen vaccine (mRNA-4157 / BNT122 style, **somatic non-junction**) | V4 | Patient SNV/indel neoantigens via LNP-mRNA → DC → CD8+ priming | Clinical-Trial (melanoma) | Not approved | Not approved | NCT03897881 (mRNA-4157; Weber et al., *Lancet* 2024 — verify PMID), NCT04486378 (BNT122) | fusion-agnostic ONLY if non-junction; check anti-PEG titer first |
| CIC-DUX4 **junction** ASO / PROTAC / junction-specific vaccine / TCR-T / CAR-T | V3, V4 | Junction-targeted degradation/recognition | Theoretical / Preclinical | None | None | None clinical-stage | **fusion-confirmed only — POSSIBLY INAPPLICABLE to this patient** |

---

## mRNA COVID-19 Vaccine — Research Findings

The mRNA Vaccine Research Team surveyed peer-reviewed evidence on whether BNT162b2 modifies immune/inflammatory/genomic context relevant to this sarcoma. **Net finding: no relevant persistent effect for this patient — a complete null finding, stated explicitly rather than omitted.**

- **Immune modulation:** Robust but **transient**. Acute LNP-driven cytokine pulse (IL-6, TNF-α, IL-1β via TLR4/NLRP3) resolves <72 h (Established; Ndeupen et al., *iScience* 2021, PMID 34825150; Arunachalam et al., *Nature* 2021, PMID 33951659). Spike-specific Th1/CD8+ memory wanes by 12 months. Transient NK activation resolves ~30 days (Kared et al., *Nat Commun* 2022, PMID 35087044 — flagged for verification). No persistent PD-1/PD-L1 modulation. → At >2 years post-vaccination, **no residual effect** on this patient's T-cell, NK, or checkpoint landscape; that landscape is now dominated by VDC/IE lymphodepletion, post-WLI changes, and imminent ifosfamide.
- **Inflammatory context (→ V2):** No documented persistent NF-κB or cytokine elevation. Dominant inflammatory inputs are WLI and ifosfamide, **not** the vaccine. V2 framework unchanged. *Verified incorporated in v2-summary.md.*
- **Genomic stability:** No peer-reviewed evidence of integration or chromosomal instability. The Alden et al. 2022 Huh7 reverse-transcription claim is Preclinical-Cell under non-physiological conditions and is contradicted by the structural biology and peer-reviewed rebuttals. No genomic-instability signal.
- **Oncogenesis surveillance:** No sarcoma signal in pharmacovigilance (VAERS/EudraVigilance/Yellow Card). **Detection-floor caveat:** CIC-rearranged sarcoma incidence (~1–2/million/yr) makes a subtype-specific signal statistically undetectable — absence reflects the floor, not confirmed safety for this subtype.
- **Relevance to future mRNA cancer vaccines (→ V4):** **Anti-PEG antibodies** post-BNT162b2 (Kozma et al., *NPJ Vaccines* 2022, PMID 35853896 — verify) could accelerate clearance of LNP-mRNA therapeutics (ABC phenomenon; Ishida et al., *J Control Release* 2006, PMID 16797763). → Practical carry-forward: measure anti-PEG titer before any future LNP-mRNA neoantigen vaccine. *Verified incorporated in v4-summary.md.*
- **Atypical-case flag from the mRNA team:** a CIC-DUX4-junction-specific vaccine is not designable without a confirmed junction → **POSSIBLY INAPPLICABLE to this patient**; non-junction somatic neoantigen approaches remain conceivable if tumor tissue is available.

---

## Metastatic Disease Considerations

Full analysis: `simulation-output/metastatic-disease-considerations.md`. Summary of how metastatic (lung, post-WLI) biology re-weights each vector:

- **V1 — applies with caveats.** Amplification machinery is cell-intrinsic and should persist, but (a) clonal evolution through VDC/IE + radiation may have shifted BRD4/CDK4 dependency in the relapsed clone (argues for re-biopsy), and (b) delivery of dietary compounds into a post-WLI fibrotic lung lesion is unknown and plausibly reduced — compounding the existing concentration-mismatch problem.
- **V2 — least applicable.** The lesion already carries the driver; preventing a *new* translocation does not address it. Narrow residual value: omega-3/SPM modification of the post-WLI pulmonary inflammatory *niche*.
- **V3 — most relevant vector here.** Targets the maintenance machinery of cells already carrying the lesion; fusion-agnostic. New caveat: target heterogeneity across sites/time — re-biopsy of the *relapse* (not reliance on the Jan 2025 resection) strengthens any V3 plan.
- **V4 — most reinterpreted by metastasis.** The relapsed clone is immune-*selected*, so it is more likely MHC-I-low/antigen-escaped → this **raises** the value of the NK arm and **sharpens** the NK-first sequencing argument. Lung is a relatively favorable checkpoint site; prior WLI may provide a radiation-primed STING context (V4 Forward Hypothesis 2; Deng et al., *Immunity* 2014, PMID 25517614 — not CIC-DUX4).
- **Most metastasis-relevant safety item across the whole catalog:** the Sayin 2014 antioxidant-metastasis signal is, by construction, about disseminating disease — exactly this patient's setting (see Conflicts).

---

## Forward Hypotheses (Not Yet in the Literature)

Curated and ranked across all vectors and the Metastatic Specialist by biological plausibility × research feasibility. The orchestrator selects and ranks; it does not author new hypotheses.

1. **[Forward Hypothesis] BETi pre-treatment → ifosfamide sequencing to exploit DDR super-enhancer collapse (V3-FH4).** Brief BETi (48–72 h) before ifosfamide collapses BRD4-maintained DDR super-enhancers (RAD51/HR genes), transiently impairing crosslink repair and sensitizing tumor cells; normal marrow has lower DDR super-enhancer dependency. *Most feasible — the patient has ifosfamide already scheduled; OTX015 Phase I safety exists.* Test: window-of-opportunity pilot, γ-H2AX/ctDNA endpoints. Untested because no CIC-DUX4 DDR ChIP-seq confirms the dependency and logistics are unaligned. (Mechanism precedent: Qiu et al. 2015 Cancer Cell context — no CIC-DUX4 data.)
2. **[Forward Hypothesis] NK-first immunologic debulking in the post-ifosfamide lymphodepletion window, before epigenetic MHC-I restoration (Metastatic M1 / V4-FH1).** Because the relapsed lung clone is immune-selected (enriched MHC-I-low), deploy IL-15 superagonist/adoptive NK during homeostatic expansion *before* EZH2i/HDACi remove the missing-self signal. Resolves the NK-vs-MHC-I tension by temporal separation. Test: paired metastatic-lesion MHC-I biopsy + NK deployment day ~14–28, ctDNA/NK-infiltration endpoints.
3. **[Forward Hypothesis] Sequential EZH2i → class-I HDACi pulse to maximize APM/MHC-I de-repression as the V3→V4 bridge (V3-FH1).** Orthogonal silencing marks (H3K27me3 + deacetylation) on overlapping APM loci; sequential de-repression may exceed either agent alone. Test: tazemetostat 7 d → entinostat 3-d pulse in CIC-DUX4 line/PDX; HLA-A/B/C flow + TAP1/2 mRNA + T-cell killing co-culture.
4. **[Forward Hypothesis] EZH2i (MHC-I up) + BETi (PD-L1 down) + anti-PD-1 tandem epigenetic immune-priming (V3-FH2 / V4 synergy).** Addresses both evasion mechanisms simultaneously then releases the checkpoint. Highest cross-vector synergy candidate. Test: CIC-DUX4 PDX/humanized model, four arms; tumor volume, TIL, MHC-I/PD-L1 trajectories.
5. **[Forward Hypothesis] Long-read WGS + RNA-seq junction re-analysis of archived tumor to resolve the "fusion-unconfirmed" status (V3-FH3).** Short-read WGS struggles across DUX4 subtelomeric repeats (4q35/10q26); long-read (Nanopore/PacBio) may identify a cryptic driver, converting fusion-agnostic → fusion-specific options. *Diagnostic, directly changes the option set for this patient.* Highest immediate clinical leverage of any item here.
6. **[Forward Hypothesis] Omega-3/SPM resolution of the post-WLI lung as a defined metastatic-niche target (Metastatic M2 / V2-FH1).** Resolvins/protectins on ALX/FPR2 reduce pulmonary-macrophage NOX2/NF-κB and IL-6/TGF-β — lowering both genotoxic and pro-colonization signaling at the one organ this patient relapses in. Test: murine WLI + lung-seeding fusion-sarcoma, EPA/DHA diet ± ALX/FPR2 antagonist; colony count, macrophage polarization.
7. **[Forward Hypothesis] Myrosinase-rescued broccoli-sprout protocol to move plasma sulforaphane from ~0 into the 0.5–2 µM range (V1-FH3).** Chop → 40-min stand → cold consumption + daikon/mustard myrosinase source; the only dietary V1 compound with a plausibly closeable concentration gap. Test: Phase-0 PK feasibility in rest weeks; plasma/urinary isothiocyanates. No therapeutic claim required.
8. **[Forward Hypothesis] Anti-PEG titer-stratified LNP-mRNA cancer-vaccine dosing in BNT162b2-primed patients (mRNA-FH2 / V4-FH3).** Pre-treatment anti-PEG ELISA as a PK stratification variable; high-titer patients may need dose adjustment or non-PEG LNP. Test: PK sub-study within NCT03897881/NCT04486378, titer vs lymph-node delivery vs neoantigen T-cell response.

*(Not carried forward as top-tier: the piperine "boosting" of CYP3A4-cleared targeted agents [V1-FH2] — clever but depends on a BETi+ifosfamide trial that does not yet exist; the post-ifosfamide NAD+ repletion window [V2-FH2] and thymoquinone washout PK [V2-FH3] are retained in the source summaries and noted in the Interaction Map discussion.)*

---

## Cross-Vector Synergies

Ranked by total evidence weight, not number of vectors touched.

1. **EZH2i (V3) → MHC-I → checkpoint/T-cell (V4).** The catalog's backbone dependency; best-grounded bridge. Several V4 entries (C1, C2, C5, C7) are explicitly *gated* on this priming — flagged: their feasibility depends on V3 priming working.
2. **BETi across V1 + V3 + V4.** Same BRD4 target: V1 throttling, V3 super-enhancer collapse, V4 PD-L1 suppression. One clinical-grade lever touching three vectors.
3. **EZH2i + BETi + anti-PD-1 triple (V3+V4).** MHC-I up + PD-L1 down + checkpoint release — highest-synergy *hypothesis* (Forward Hypothesis 4); components are individually Clinical-Trial, the combination is Theoretical.
4. **CDK4/6i overlap (V1 ↔ V3).** Same CDK4/CCND1 axis; dietary "weak CDK modulators" (fisetin) are NOT equivalent to clinical CDK4/6i — different track.
5. **Omega-3 EPA/DHA across V1 + V2 + V4.** Best dietary cross-vector compound, lowest interaction risk; absent from regimen.
6. **Sulforaphane across V1 + V3 + V4** — but the exposure-mismatch is honest and large, and juicing defeats it; do **not** equate dietary sulforaphane with a clinical HDACi (different track).
7. **V1 ↔ V2 dietary overlap** (quercetin, selenium, zinc, omega-3): reducing transcriptional load (V1) reduces Topo II DSBs at active loci (V2).

---

## Conflicts and Open Questions

Surfaced explicitly, not resolved by the orchestrator — these are clinical-judgment calls.

1. **High-dose liposomal vitamin C vs. ROS-dependent chemo.** Doxorubicin (completed) is strongly ROS-dependent — concern was real, now moot. Ifosfamide is alkylation-*primary* (ROS contributory) → lower but non-zero concern. Standard oncology guidance advises against high-dose antioxidants during cytotoxic therapy. **Resolution: the oncologist must know the patient self-administers liposomal vitamin C; the timing decision around ifosfamide cycles belongs to them.** The simulation flags, does not decide.
2. **Antioxidants vs. metastasis (Sayin 2014, PMID 24477002).** NAC and vitamin E accelerated metastasis in KRAS/BRAF mouse lung models via ROS suppression → reduced apoptosis/oxidative CTC clearance. **Relevance:** liposomal vitamin C could act analogously; the patient has residual/oligometastatic disease (the setting that makes this matter). **Counter:** CIC-rearranged sarcoma is not KRAS/BRAF-driven — different ROS architecture; transfer is biologically plausible but unconfirmed (Preclinical-Animal). NAC itself is not in the regimen and is not recommended. Carry the flag; defer to oncologist.
3. **Thymoquinone (black cumin seed oil) & piperine (in curcumin+piperine) CYP3A4 vs. imminent ifosfamide.** Both inhibit CYP3A4; ifosfamide is a CYP3A4-activated prodrug → inhibition could *reduce* activation (efficacy) while P-gp inhibition could *increase* vincristine/etoposide exposure (toxicity). **HIGHEST-priority case-specific interaction.** Resolution: oncologist review before the ifosfamide course; the V2 lead's proposed 72–96 h washout (Forward Hypothesis, untested) is a candidate mitigation but not validated. The piperine PK enhancement and the chemo interaction are the *same* mechanism and cannot be separated.
4. **β-carotene: food vs. supplement.** ATBC (PMID 8127329) and CARET (PMID 8602180) showed harm from *isolated supplements* (20–30 mg/d) in smokers. **Food-level carrot juice (plasma ~0.4–0.8 µmol/L) is categorically different and not implicated.** Do not misapply ATBC/CARET to the patient's carrot juice; do flag against any β-carotene supplement.
5. **NK vs. MHC-I sequencing tension (V4).** Epigenetic MHC-I restoration helps T-cells but removes NK missing-self visibility. Suggested ordering: **NK-first → epigenetic priming → checkpoint.** Especially salient in the metastatic, immune-selected (MHC-I-low) clone. Unresolved in the literature for any tumor type.
6. **Vitamin E (SELECT, PMID 21990298) and selenium narrow window.** High-dose vitamin E increased prostate cancer; selenium was null with a narrow safety window (UL 400 µg/d). Neither at supplement dose is supported; prefer food-level/deficiency-correction only.
7. **Probiotics during therapy.** Microbiome diversity associates with checkpoint response (melanoma/NSCLC — Routy 2018 PMID 29209380, Gopalakrishnan 2018 PMID 29097493), but some broad-probiotic data show *reduced* checkpoint response, and unpasteurized ferments are unsafe during post-ifosfamide neutropenia. Favor dietary fiber/whole fermented foods over probiotic supplements; time around neutropenia.
8. **Sub-agent claims the orchestrator adjusted/flagged.** Several mechanism citations across summaries were marked "verify before citing" (e.g., omega-3 RAS lipid-raft, EGCG-BRD4, fisetin-CDK in V1; Yoshimoto 2017 BETi CIC-DUX4 in V3; Kared/Kozma/Karaba/Weber PMIDs in mRNA). These are carried with their verification flags and **not** asserted as established. No fabricated PMID was promoted to a firm citation.
9. **Open biology gaps** (limit every entry): no published CIC-DUX4 MHC-I quantification, no CIC-DUX4 NK-killing or stress-ligand (MICA/MICB/ULBP) data, no CIC-DUX4 DepMap dependency screen, no metastasis-specific molecular data, and EMA status for tazemetostat/vorinostat/N-803 not confirmed here.

---

## Standard-of-Care Interaction Map

SOC = VDC/IE (vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide). **Imminent: high-dose ifosfamide** (CYP3A4-activated prodrug; chloroacetaldehyde CNS/renal toxicity; ROS contributory). Screened via `/sarcoma-chemo-interactions`. Annotation applies to all: review with oncologist before any change.

| Compound | CYP3A4 | CYP2C9 | P-gp | ROS-axis | Priority for THIS patient | Source |
|---|---|---|---|---|---|---|
| **Piperine** (in curcumin+piperine) | Inhibitor → ↓ifosfamide activation | — | Inhibitor → ↑vincristine/etoposide CNS exposure | — | **HIGHEST — discuss before ifosfamide** | PK literature; Shoba 1998 (absorption); Anuchapreeda 2002 PMID 12126956 (P-gp) |
| **Curcumin** | Modulator | — | Modulator | Antioxidant (relevant during doxorubicin, completed) | HIGH | Chen 2007 PMID 17065205; Chatterjee 2019 PMID 30865445 (BRD4) |
| **Thymoquinone** (black cumin seed oil) | Inhibitor → ↓ifosfamide activation | Inhibitor | Inhibitor | Nrf2 → ROS-axis | **HIGH — discuss before ifosfamide** | Ahmed 2017 *Saudi Pharm J* (preclinical) |
| **Liposomal vitamin C (high-dose)** | — | — | — | Reduces ROS-mediated cytotoxicity; possible pro-metastatic (Sayin analog) | **MODERATE — timing decision with oncologist** | Sayin 2014 PMID 24477002 (analogous mechanism) |
| **EGCG (supplement dose)** | — | — | Inhibitor → ↑vincristine/etoposide | Antioxidant + Topo II activity (cell-free) — flag, do not extrapolate | MODERATE at supplement dose; low at beverage | Bettuzzi 2006 PMID 16397214 (safety/hepatotoxicity) |
| **Quercetin (supplement dose)** | Modulator | — | Modulator | Antioxidant | LOW at juice level; relevant at supplement dose | Standard polyphenol PK literature |
| **Apigenin** | Modest | Inhibitor | — | — | LOW at celery-juice level | Standard flavone PK literature |
| **Berberine (supplement)** | Inhibitor | — | — | — | LOW–MODERATE if used | Metabolic-trial PK literature |
| **Ginger (6-gingerol)** | — | Modest (high-dose only) | Modest in vitro | — | LOW at juice level | High-dose ginger literature |
| **Selenium / Vitamin E** | — | — | — | Antioxidant; harm signals (SELECT) | LOW interaction but harm-signal flag | SELECT PMID 19066370 / 21990298 |
| **Omega-3 (high-dose)** | — | — | — | — | LOW; anti-platelet peri-procedure note | — |
| **Vitamin D3, honey, beetroot/carrot/celery/apple juice (food level)** | — | — | — | — | LOW / none documented at culinary intake | — |

**Timing note:** the patient takes these in *rest weeks*. ROS-axis concern peaks during active cytotoxic infusion; CYP3A4/P-gp concerns apply whenever the compound and a substrate drug overlap in time. The decisive question is whether curcumin+piperine and black cumin seed oil will be continued during/just before the ifosfamide course — this requires direct oncologist communication.

---

## Patient's Actual Self-Administered Regimen

Each component the patient actually takes, assessed and labeled **helping / neutral / potentially harmful (context-dependent)**, with the head-on interaction analysis the vectors produced. **All assessments are context- and timing-dependent and must be reviewed by the treating oncologist; nothing here is a start/stop instruction.**

| Component | Label (context-dependent) | Assessment & head-on analysis |
|---|---|---|
| **Curcumin + piperine** | **Potentially harmful around ifosfamide** | Piperine inhibits CYP3A4 (ifosfamide is a CYP3A4-activated prodrug → potential ↓activation/efficacy) and P-gp (↑vincristine/etoposide exposure/toxicity). **The PK "boost" of curcumin and the chemo interaction are the same mechanism — inseparable.** V1 relevance (BRD4-chromatin disruption) is real mechanistically but dietary/supplement plasma is far below the active range. **Shoba 1998 caveat (verbatim):** *"The widely-cited '~2000% bioavailability increase' comes from Shoba et al., Planta Medica 1998 — a single-dose pharmacokinetic study, n=10 healthy volunteers, 2 g curcumin + 20 mg piperine. The curcumin-only control arm produced serum levels below the assay's limit of detection, so the '20×' number is computed against a near-zero baseline. The directional finding (piperine increases curcumin absorption) is real and reproduced; the specific 2000% figure should not be cited as a universal multiplier."* **Highest-priority item to raise before the ifosfamide course.** |
| **Liposomal vitamin C** | **Neutral in NED/rest periods; potentially harmful during active ROS-chemo and in residual-disease setting** | Two distinct concerns: (1) ROS-axis — reduces ROS-mediated cytotoxicity; high relevance during doxorubicin (completed), lower during alkylation-primary ifosfamide but standard guidance still cautions against high-dose antioxidants during cytotoxic therapy. (2) **Metastasis — NAC/Sayin 2014 (PMID 24477002):** antioxidant ROS-suppression accelerated metastasis in KRAS/BRAF mouse models; liposomal vitamin C could act analogously, and the patient has residual/oligometastatic disease (the setting that makes this matter). Counter: CIC-rearranged sarcoma is not KRAS/BRAF-driven (Preclinical-Animal; transfer unconfirmed). The oncologist must be told the patient takes this; the around-ifosfamide timing is their call. |
| **Black cumin seed oil (thymoquinone)** | **Potentially harmful around ifosfamide** | CYP3A4 + CYP2C9 inhibitor (and Nrf2/ROS-axis) → same ifosfamide-activation concern as piperine (Ahmed 2017, preclinical). No human sarcoma dose to report. V2 lead proposed an untested 72–96 h washout as a possible mitigation — candidate hypothesis, not validated. Discuss before ifosfamide. |
| **Vitamin D** | **Helping if correcting deficiency; neutral if replete** | VDR axis: CDKN1A/p21 (V3 differentiation) and NK NKG2D (V4). Deficiency correction has clearer evidence than replete supplementation (VITAL null for cancer incidence, PMID 30415629). No documented ifosfamide/VDC interaction; hypercalcemia monitoring. **Check 25(OH)D level.** |
| **Honey** | **Neutral** | Trace polyphenols at culinary intake; no CIC-DUX4-relevant concentration; no chemo interaction at culinary dose. |
| **Celery juice (apigenin / luteolin)** | **Neutral (mildly helpful at most)** | Apigenin reduces ETS-factor expression / luteolin modulates cell cycle — but at 50–250× above juice-achievable concentrations. Apigenin: CYP2C9 + modest CYP3A4 (low at juice level). |
| **Ginger juice (6-gingerol)** | **Neutral** | MAPK/NF-κB mechanism at 50–200× above dietary intake — concentration mismatch decisive. CYP2C9/P-gp modulation only at high-dose supplements, not juice. |
| **Carrot juice (β-carotene)** | **Neutral; food ≠ supplement** | Provitamin-A/retinoid axis (V3). **ATBC/CARET harm was from isolated supplements (20–30 mg/d) in smokers — does NOT apply to food-level carrot juice (plasma ~0.4–0.8 µmol/L).** Do not stop carrot juice on ATBC/CARET grounds; do avoid β-carotene *supplements*. |
| **Broccoli juice (sulforaphane)** | **Neutral as prepared (likely near-zero active compound) — preparation is the issue** | Sulforaphane is the best-bioavailable V1 compound (3–10× mismatch), BUT **juicing destroys myrosinase → sulforaphane will not form.** For any benefit: chop → ~40 min stand → consume cold (or add daikon/mustard as exogenous myrosinase); even then MHC-I effect is UNESTABLISHED at dietary exposure. Low chemo-interaction concern. |
| **Apple juice (quercetin via skin)** | **Neutral** | Quercetin RTK/RAS inhibition at 10–50 µM cell lines vs ~0.05–0.2 µM dietary plasma; most quercetin is in the skin and largely lost in juicing. CYP3A4/P-gp modulation only at supplement doses. |
| **Beetroot juice (nitrate)** | **Neutral** | Vascular/NO pathway; no V1–V4 mechanism. No documented chemo interaction at culinary dose. |

**Sulforaphane preparation note (head-on):** juicing inactivates myrosinase, the enzyme required to convert glucoraphanin → sulforaphane; the patient's broccoli juice likely delivers near-zero sulforaphane. **β-carotene food-vs-supplement note (head-on):** the ATBC/CARET signal is supplement-specific and does not extend to dietary carrot intake. **NAC/Sayin note (head-on):** NAC is not in the regimen and is not recommended; the same ROS-suppression-promotes-metastasis concern is carried, at lower certainty, to high-dose liposomal vitamin C given the patient's residual disease.

---

## What This Catalog Cannot Tell You

- **Whether any of this works in CIC-rearranged sarcoma.** There is essentially no direct evidence in this tumor; nearly every entry is extrapolated from related fusion sarcomas or other cancers, and is tagged accordingly.
- **What this patient should do.** No doses, no start/stop instructions, no regimen changes. Those are clinical decisions for the treating oncologist.
- **The patient's actual cofactor/vitamin status, tumor molecular profile, MHC-I/PD-L1/TMB, microbiome, or anti-PEG titer** — all are measurement questions the catalog cannot answer.
- **Whether the relapsed lung clone matches the primary** — clonal evolution through treatment cannot be assumed neutral; re-biopsy + long-read sequencing (Forward Hypothesis 5) is the way to find out.
- **Confirmation of the fusion** — this is the fusion-unconfirmed subgroup; all fusion-junction-specific approaches remain POSSIBLY INAPPLICABLE until/unless a junction is identified.
- **Verification of every citation** — citations flagged "verify" in the source summaries are carried with those flags; the reader must independently verify any PMID/NCT before relying on it.

---

## Bibliography

Verifiable citations used above. Entries marked **[verify]** were flagged by the source teams as requiring independent confirmation and are not asserted as established.

**Clinical/mechanism (drugs, epigenetics, immune):**
- Tazemetostat epithelioid sarcoma — FDA accelerated approval 2020-01-23 (EZH-202 / NCT02601950); EMA status **[verify]**.
- D'Angelo SP et al. Nivolumab ± ipilimumab in metastatic sarcoma (Alliance A091401). *NEJM* 2018. PMID 30501812.
- Chiappinelli KB et al. DNMTi → ERV/viral mimicry → immune. *Cell* 2015. (companion: Roulois D et al. *Cell* 2015.)
- Deng L et al. STING-dependent radiation immunogenicity. *Immunity* 2014. PMID 25517614.
- Ruggeri L et al. Alloreactive NK cells in haploidentical transplant. *Science* 2002. PMID 11786547.
- Weber JS et al. mRNA-4157 (V940) + pembrolizumab, KEYNOTE-942. *Lancet* 2024. NCT03897881 — PMID **[verify]**.

**Dietary / supplement / PK:**
- Shoba G et al. Curcumin + piperine bioavailability. *Planta Medica* 1998 (n=10; caveat reproduced verbatim).
- Cheng AL et al. Curcumin Phase I. *Anticancer Res* 2001. PMID 11763884.
- Bettuzzi S et al. Green tea catechins, prostate. *Cancer Res* 2006. PMID 16397214.
- Manson JE et al. VITAL (vitamin D). *NEJM* 2019. PMID 30415629.
- Chen J et al. Curcumin CYP3A4. 2007. PMID 17065205. · Anuchapreeda S et al. Curcumin P-gp. 2002. PMID 12126956.
- Myzak MC et al. Sulforaphane HDAC inhibition (HCT116). *Cancer Res* 2004. PMID 15205379. · Clarke JD et al. sulforaphane bioavailability. *Cancer Prev Res* 2011. PMID 21593198.
- Russo M et al. Quercetin RTK inhibition. *Biochem Pharmacol* 2012. PMID 22261127.

**Harms / null trials:**
- ATBC Study Group. β-carotene, smokers. *NEJM* 1994. PMID 8127329.
- Omenn GS et al. CARET. *NEJM* 1996. PMID 8602180.
- Lippman SM et al. SELECT. *JAMA* 2009. PMID 19066370. · Klein EA et al. SELECT vitamin E. *JAMA* 2011. PMID 21990298.
- Sayin VI et al. Antioxidants accelerate metastasis (mouse). *Sci Transl Med* 2014. PMID 24477002.

**Microbiome–immune (melanoma/NSCLC — NOT sarcoma):**
- Routy B et al. *Science* 2018. PMID 29209380. · Gopalakrishnan V et al. *Science* 2018. PMID 29097493. · Sonnenburg/Gardner fermented foods. *Cell* 2022. PMID 35839772.

**mRNA vaccine team:**
- Ndeupen S et al. LNP inflammatory. *iScience* 2021. PMID 34825150. · Arunachalam PS et al. *Nature* 2021. PMID 33951659. · Sahin U et al. *Nature* 2020. PMID 33028802. · Oberhardt V et al. *Nature* 2021. PMID 34384875. · Goel RR et al. *Sci Immunol* 2021. PMID 34385704. · Kared H et al. NK, *Nat Commun* 2022. PMID 35087044 **[verify]**. · Karaba AH et al. *Cell Rep Med* 2022. PMID 36099914 **[verify]**. · Barda N et al. *NEJM* 2021. PMID 34432976. · Kozma GT et al. anti-PEG. *NPJ Vaccines* 2022. PMID 35853896 **[verify]**. · Ishida T et al. ABC phenomenon. *J Control Release* 2006. PMID 16797763. · Netea MG et al. trained immunity. *Science* 2016. PMID 27102489.

**NER grounding:** all genes, drugs, and biomedical entities in this catalog were run through `scripts/openmed_ner.py --team orchestrator` (oncology + pharma + disease models) and recognized at high confidence; no unrecognized/fabricated entity remained (N-803 = nogapendekin alfa inbakicept confirmed via pharma model; tokenization artifacts for CDK4/6 and ETV4/ETV5 noted and benign).

---

*End of catalog v1. This is a research-simulation hypothesis catalog, not medical advice. Every dietary/supplement entry: "potential interactions with standard-of-care chemotherapy and concurrent medications — must be reviewed by the patient's oncologist before any change."*
