# Vector 4 — Immune Watchdog Summary

Summary: Maps immune surveillance and clearance strategies for CIC-rearranged sarcoma across checkpoint/T-cell, NK cell, microbiome-immune, and neoantigen vaccine domains; incorporates V3 MHC-I upregulation candidates as required priming inputs and the mRNA vaccine team's immune-modulation findings; clearly separates dietary and clinical tracks; anchored to a fusion-unconfirmed (atypical subgroup) patient preparing for high-dose ifosfamide with prior whole-lung irradiation and oligometastatic lung relapse. Does NOT cover V1 (rate limiting), V2 (compiler protection), or V3 (hot patching) mechanisms except where they directly gate V4 efficacy.

Confidence: medium — Checkpoint, NK, and microbiome mechanisms are well-established at the class level; clinical evidence in sarcoma is modest (SARC028 ORR 5-18% in most responsive subtypes); direct CIC-DUX4-specific immune data are essentially absent; dietary immune modulation in cancer patients at culinary doses is mechanistically plausible but clinically unvalidated. The NK missing-self rationale is the mechanistically strongest dietary lever.

---

## V3 MHC-I UPREGULATION BRIDGE — INCORPORATED

(From v3-summary.md, MHC-I Upregulation Candidates section — mandatory V4 input)

**Key message from V3 lead:** Build V4 planning around tazemetostat and entinostat as the V3→V4 clinical bridge. Dietary entries (sulforaphane, butyrate) are listed for completeness but must NOT be relied upon as MHC-I upregulators at clinically meaningful levels.

| V3 Candidate | MHC-I Mechanism | V4 Priority | V3→V4 dependency in this summary |
|---|---|---|---|
| Tazemetostat (EZH2i) | H3K27me3 reduction at HLA-A/B/C, TAP1, TAP2, B2M, NLRC5 promoters | HIGH — cleanest bridge | T-cell checkpoint entries (Ranks 1, 2) depend on this priming step |
| Entinostat (class I HDACi) | HDAC1/2/3 inhibition → H3K27ac at APM gene promoters → NLRC5 upregulation | HIGH — well-characterised | T-cell checkpoint entries (Ranks 1, 2) can use this as alternative or additive bridge |
| Vorinostat (pan-HDACi) | Same APM de-repression; higher toxicity | MEDIUM — toxicity concern with ifosfamide | Sequential scheduling required |
| OTX015/BETi | PD-L1 super-enhancer suppression; MHC-I upregulation weaker | MEDIUM — PD-L1 suppression primary signal | Supports Rank 3 checkpoint entry |
| Azacitidine/Decitabine (DNMTi) | ERV demethylation → STING → type I IFN → MHC-I | MEDIUM — distinct immunostimulatory path | Orthogonal to EZH2i/HDACi; potential triple-priming |
| Sulforaphane (dietary) | Weak HDACi at 5-30 µM in cell lines | UNESTABLISHED at dietary exposure — do not rely on | Not used as MHC-I priming lever in V4 clinical planning |
| Butyrate (dietary fiber) | HDACi at mM colonic; systemic far lower | UNESTABLISHED at achievable systemic exposure | Not used as MHC-I priming lever in V4 clinical planning |

---

## mRNA VACCINE TEAM FINDINGS — INCORPORATED

(From mrna-vaccine-summary.md, Section 7 — Relevance to V4)

The mRNA team's findings do not alter V4's core immune-surveillance framework, with two specific exceptions that are incorporated throughout this summary:

1. **No persistent BNT162b2 immune alteration at current timepoint:** At >2 years post-standard BNT162b2 vaccination, no persistent alteration of T-cell repertoire, NK compartment, or checkpoint (PD-1/PD-L1) axis is expected. The dominant immune landscape is now shaped by VDC/IE-induced lymphodepletion, post-WLI immune changes, and the imminent high-dose ifosfamide. Vaccine-attributable immune effects are a moot consideration in current V4 planning.

2. **Anti-PEG antibody flag (high practical importance):** A subset of BNT162b2 recipients develop anti-PEG IgG/IgM. Any future LNP-mRNA immunotherapeutic (mRNA-4157, BNT122, or related neoantigen vaccine) used in this patient should include pre-treatment anti-PEG titer measurement as a PK stratification step. Accelerated blood clearance could reduce lymph-node mRNA delivery and diminish vaccine efficacy. This is a design recommendation for any future LNP therapeutic, not a contraindication. Evidence tier: Clinical observational (Kozma et al., NPJ Vaccines 2022, PMID 35853896 — verify) + Mechanistic (ABC phenomenon, Ishida et al., J Controlled Release 2006, PMID 16797763).

---

## RANKED CANDIDATE LIST

### DIETARY TRACK

| Rank | Compound | Layer | Mechanism (molecular) | Tier | CIC-DUX4 direct? | Cross-vector | Source/citation |
|---|---|---|---|---|---|---|---|
| D1 | Vitamin D3 (deficiency correction) | NK cell function | 1,25(OH)2D3 → VDR on NK cells → upregulates NKG2D (activating receptor) → lowers NK activation threshold; also supports DC VDR-dependent tolerogenic/effector balance | Mechanistic + Clinical observational | None direct | V3 differentiation (VDR/CDKN1A) | Arango et al., J Clin Immunol 2010, PMID 20862597; VITAL trial Manson NEJM 2019, PMID 30415629 (null for cancer broadly) |
| D2 | Diverse whole-plant fiber (not juice) | Microbiome/SCFA | Fermentable fiber → SCFA (butyrate, propionate, acetate) production by colonic bacteria → supports gut barrier integrity and microbiome diversity; microbiome diversity associated with CPI response in melanoma/NSCLC cohorts | Dietary-Observational (melanoma/NSCLC — NOT sarcoma) | None direct | V3 butyrate/HDACi (colonic only) | Routy 2018 PMID 29209380; Gopalakrishnan 2018 PMID 29097493; Sonnenburg & Gardner, Cell 2022, PMID 35839772 |
| D3 | Omega-3 EPA/DHA (absent from regimen — gap) | NK cell activity + anti-inflammatory TME | EPA/DHA alter NK cell membrane lipid composition → enhanced receptor clustering and immune synapse; EPA→resolvin E1/DHA→protectin D1 reduce immunosuppressive TGF-β/IL-6 in TME | Preclinical-Animal + Clinical observational (healthy volunteers) | None direct | V1 RAS/ERK; V2 anti-inflammatory | Thies et al., Am J Clin Nutr 2001, PMID 11157327; [no direct CIC-DUX4 citation] |
| D4 | Zinc (deficiency correction only) | NK cell maturation | Zinc cofactor for thymulin (zinc-dependent thymic hormone) → NK cell maturation; zinc deficiency impairs NK cytotoxicity and NCR expression | Mechanistic + Preclinical | None direct | V2 DNA repair | Shankar & Prasad, Am J Clin Nutr 1998, PMID 9537623 |
| D5 | Beta-glucan (oats, barley, mushrooms) | NK activation via Dectin-1 | Soluble beta-glucan → Dectin-1/TLR2 on NK cells and macrophages → NK activation signal independent of MHC-I status | Mechanistic | None direct | V4 microbiome (prebiotic) | [No direct citation in cancer patients; mechanism inferred from Dectin-1 NK literature; no human RCT data in sarcoma] |
| D6 | Fermented foods (yogurt, kefir, kimchi) | Microbiome diversity | Live fermented food consumption → microbiome diversity increase → 19 inflammatory proteins decreased (Sonnenburg Cell 2022) | Clinical observational (healthy adults) | None direct | V4 microbiome | Sonnenburg & Gardner, Cell 2022, PMID 35839772 |

**Dietary track caveats:**
- D1 (Vitamin D3): Only applies to deficiency correction. Replete-supplementation benefit thin (VITAL trial null). Patient is self-administering — check 25(OH)D level.
- D2 (fiber): Juicing removes most fiber; microbiome benefit of patient's current juice-based approach is substantially lower than whole-food equivalent. Whole broccoli, apple with skin, legumes provide far more prebiotic substrate.
- D3 (omega-3): ABSENT from patient regimen — notable gap. Dietary marine fish (sardines, mackerel 2-3×/week) is the recommended approach over supplementation given high-dose ifosfamide context.
- D4 (zinc): Excess zinc (>40 mg/day) suppresses copper absorption → anaemia/neuropathy risk. Do not exceed UL without clinical indication.
- D5 (beta-glucan): Mechanism is Dectin-1 dependent; clinical evidence in cancer patients absent; listed as mechanistic exploration only.
- D6 (fermented foods): Avoid unpasteurised fermented foods during neutropenic windows post-ifosfamide.

**Regimen items assessed — no significant V4 dietary benefit:**
- Curcumin + piperine: cell-line NF-κB/PD-L1 data only; dietary dose insufficient; FLAG for CYP3A4 and P-gp interaction with ifosfamide/vincristine.
- Black cumin seed oil (thymoquinone): no checkpoint mechanism at dietary dose; FLAG CYP3A4/CYP2C9 inhibition — discuss with oncologist during ifosfamide.
- Honey: no V4 mechanism at culinary dose.
- Sulforaphane (broccoli juice): juicing inactivates myrosinase; MHC-I upregulation UNESTABLISHED at achievable concentrations.
- Liposomal vitamin C: no established checkpoint/NK mechanism; ROS-axis concern at high dose with ifosfamide.

### CLINICAL TRACK
### (Clinical / Experimental — not naturally achievable; for awareness only.)

| Rank | Intervention | Layer | Mechanism | Tier | CIC-DUX4 direct? | V3 priming dependency | Source/citation | Fusion tag |
|---|---|---|---|---|---|---|---|---|
| C1 | Tazemetostat + anti-PD-1 (pembrolizumab or nivolumab) | Epigenetic priming → checkpoint | EZH2i restores MHC-I (V3 bridge) → tumour cells become visible to T-cells; anti-PD-1 removes inhibitory brake on primed CD8+ T-cells | Clinical-Trial (EZH2i: Established epithelioid sarcoma FDA 2020-01-23; PD-1: Established melanoma/multiple; sarcoma: Clinical-Trial) | None direct | YES — tazemetostat V3 priming required for T-cell component | NCT01897571 (tazemetostat); NCT02301039 (SARC028 pembrolizumab); NCT04196738 (combination — verify status) | FUSION-AGNOSTIC |
| C2 | Entinostat + pembrolizumab | Epigenetic priming → checkpoint | Class I HDACi restores MHC-I via NLRC5/APM de-repression → anti-PD-1 checkpoint release | Clinical-Trial | None direct | YES — entinostat V3 priming required | NCT02890069 (entinostat + pembrolizumab sarcoma cohort) | FUSION-AGNOSTIC |
| C3 | OTX015/BETi + anti-PD-1 | BRD4 super-enhancer → PD-L1 suppression + checkpoint | BRD4 inhibition collapses CD274 super-enhancer → reduces PD-L1; anti-PD-1 then acts on partially reduced PD-L1 axis | Clinical-Trial | None direct (BETi CIC-DUX4 preclinical data limited) | PARTIAL — BETi also V3 BRD4 throttle; MHC-I upregulation weaker than EZH2i | NCT01713582; NCT02419417 | FUSION-AGNOSTIC |
| C4 | N-803 (nogapendekin alfa inbakicept, IL-15 superagonist) | NK cell expansion | IL-15/IL-15Rα-Fc complex → NK cell proliferation, survival, cytotoxicity enhancement → killing of MHC-I-low CIC-DUX4 cells | Established (bladder cancer FDA 2023, with BCG); Clinical-Trial (solid tumours) | None direct | PREFERRED BEFORE V3 MHC-I restoration — NK benefit is MHC-I-low specific | NCT03055780 (bladder); solid tumour trials — verify current status | FUSION-AGNOSTIC |
| C5 | Nivolumab + ipilimumab (combination checkpoint) | Dual checkpoint blockade | Anti-PD-1 + anti-CTLA-4 → concurrent T-cell exhaustion relief + Treg depletion in TME → superior ORR vs. monotherapy in some sarcoma subtypes | Clinical-Trial (sarcoma); Established (melanoma, RCC, NSCLC FDA/EMA) | None direct | YES — V3 MHC-I priming would enhance efficacy | NCT02978625 (Alliance A091401; D'Angelo NEJM 2018, PMID 30501812) | FUSION-AGNOSTIC |
| C6 | Azacitidine/decitabine + anti-PD-1 | DNMTi viral mimicry → STING → checkpoint | ERV demethylation → cytosolic dsRNA → STING pathway → type I IFN → MHC-I upregulation + IFN-stimulated gene expression + DC activation; anti-PD-1 acts on newly activated T-cell response | Established (MDS/AML FDA/EMA); Clinical-Trial (solid tumours) | None direct | INDEPENDENT of EZH2i/HDACi bridge — orthogonal STING-dependent path | Chiappinelli 2015 Cell; Roulois 2015 Cell; [no direct CIC-DUX4 citation] | FUSION-AGNOSTIC |
| C7 | Personalised neoantigen vaccine (mRNA-4157 style, somatic WES/RNA-seq neoantigens) | Neoantigen-specific T-cell priming | Tumour-specific SNV/indel-derived peptides encoded in patient-specific mRNA → LNP delivery → DC presentation → neoantigen-specific CD8+ T-cell expansion | Clinical-Trial (melanoma NCT03897881; other solid tumours expanding) | None direct | YES — EZH2i V3 MHC-I priming required for T-cell killing after vaccine priming | Weber et al., Lancet 2024 (mRNA-4157 + pembrolizumab melanoma — verify PMID); NCT04486378 (BNT122) | FUSION-AGNOSTIC (for non-junction somatic neoantigen approach) |
| C8 | Adoptive NK cell transfer (post-ifosfamide lymphodepletion window) | NK cell reconstitution + anti-tumour NK killing | Haploidentical NK cells infused into lymphodepleted host → homeostatic expansion driven by IL-7/IL-15 → NK killing of residual MHC-I-low tumour cells | Clinical-Trial (AML/haematological); Preclinical (solid tumours) | None direct | PREFERRED BEFORE V3 MHC-I restoration | [no specific solid tumour CIC-DUX4 citation; AML NK reconstitution: Ruggeri et al., Science 2002, PMID 11786547 — not directly transferable] | FUSION-AGNOSTIC |

---

## DIETARY TRACK — EXPANDED

### Patient Regimen Assessment Against V4 Framework

This patient self-administers: curcumin + piperine, liposomal vitamin C, black cumin seed oil, vitamin D3, honey, fresh juices (celery, ginger, carrot, broccoli, apple, beetroot).

| Compound | V4 mechanism (if any) | Tier | Concentration caveat | Chemo interaction (ifosfamide) | Recommendation |
|---|---|---|---|---|---|
| Vitamin D3 | NK cell NKG2D upregulation via VDR; DC immune priming | Mechanistic | Deficiency correction: clear benefit. Replete: benefit thin. VITAL trial null for cancer incidence broadly. | No documented interaction at supplemental doses (1000-4000 IU/day) with ifosfamide. Hypercalcemia monitoring required. | Check 25(OH)D level. If deficient, correct. If replete, no additional NK benefit established. |
| Curcumin + piperine | Cell-line NF-κB/PD-L1 inhibition at 10-30 µM; dietary dose 100-fold insufficient | Preclinical-Cell | Plasma Cmax from dietary curcumin far below active range even with piperine. "2000% boost" from Shoba 1998 (n=10, single dose, control below LOD) — directional finding; not a universal multiplier. | CYP3A4 inhibitor (Chen 2007, PMID 17065205) — may ↑ vincristine/etoposide AUC or ↓ ifosfamide activation; P-gp inhibitor (Anuchapreeda 2002, PMID 12126956) — ↑ CNS exposure of etoposide/vincristine. Discuss supplement-form curcumin with oncologist during ifosfamide. | At dietary turmeric in food: low risk. Curcumin supplement: discuss with oncologist. |
| Liposomal vitamin C | No established V4 mechanism | Mechanistic | No checkpoint/NK evidence at liposomal oral dose | ROS-axis concern at high IV dose with ifosfamide mechanism. Liposomal oral: intermediate. | Discuss with oncologist. |
| Black cumin seed oil (thymoquinone) | No checkpoint/NK mechanism at dietary dose | Preclinical-Cell | No human PK data; estimated plasma Cmax <<1 µM from typical dose | CYP3A4 + CYP2C9 inhibitor (Ahmed 2017, Saudi Pharm J) — may reduce ifosfamide CYP3A4-dependent activation. FLAG: discuss with oncologist whether to continue during ifosfamide. | Discuss with oncologist — possible reduction of ifosfamide bioactivation. |
| Honey | No V4 mechanism | — | — | No known interaction at culinary intake | Continue at culinary levels; no V4-specific benefit. |
| Broccoli juice | Sulforaphane: dietary dose via juicing insufficient (myrosinase inactivated by juicing); MHC-I upregulation UNESTABLISHED | Preclinical-Cell | Active sulforaphane yield from juice substantially lower than chopped/chewed broccoli sprouts | At juice intake: low interaction risk with ifosfamide | Switch to chopped raw broccoli sprouts for any sulforaphane benefit; even then, MHC-I effect UNESTABLISHED at dietary exposure. |
| Apple/carrot/celery/beetroot/ginger juice | Polyphenols at subclinical doses after juicing; no V4 mechanism | Dietary-Observational | — | Ginger at very high doses: P-gp modulation (not at juice level) | Continue; modest diversity contribution to microbiome if fiber retained (juice removes most). |
| Omega-3 EPA/DHA | ABSENT from regimen — NK cell membrane modulation, anti-inflammatory TME | Preclinical-Animal + Clinical observational | No supplement-form concern at dietary fish intake | Anti-platelet at high supplement doses — relevant peri-surgery or peri-ifosfamide | Add dietary marine fish (sardines, mackerel 2-3×/week). If supplement considered, discuss dose with oncologist. |

---

## CLINICAL TRACK — EXPANDED

### Case-Specific Clinical Prioritisation

**Imminent context:** High-dose ifosfamide is the immediate clinical reality. V4 clinical track planning must account for:
1. High-dose ifosfamide will produce profound lymphodepletion — NK cells, T-cells, and B-cells all depleted.
2. The post-ifosfamide immune reconstitution window (weeks 4-8) is a mechanistically exploitable opportunity for NK cell activation and/or checkpoint therapy initiation.
3. MHC-I priming (V3 EZH2i/HDACi) would ideally be started AFTER adequate ifosfamide recovery and before CPI initiation.
4. The prior WLI has created a radiation-primed pulmonary immune context that may enhance checkpoint responsiveness at the relapse site.

**Priority sequence for oncologist discussion (post-ifosfamide response assessment):**

Step 1: If ifosfamide produces response in the lung relapse → reassess resectability; if resected, R0 margin.

Step 2: Post-response, assess for maintenance/consolidation:
- If V3 epigenetic priming is discussed: tazemetostat (EZH2i) could be initiated as MHC-I priming step (4 weeks) before CPI.
- Checkpoint inhibitor (pembrolizumab monotherapy or nivolumab + ipilimumab) initiation after V3 priming window.
- NCT04196738 (tazemetostat + pembrolizumab combination — verify current enrollment status) or similar trial enrollment.

Step 3: If ifosfamide produces insufficient response:
- Consider BETi trial enrollment (OTX015, BMS-986158) ± checkpoint combination.
- Consider BETi + ifosfamide sequencing (Forward Hypothesis from V3).

Step 4 (longer horizon — if tissue available):
- WES + RNA-seq on archived Jan 2025 resection specimen or current relapse biopsy.
- If sufficient somatic neoantigens identified: personalised neoantigen vaccine trial enrollment (mRNA-4157 compassionate use or trial).
- Pre-treatment anti-PEG antibody titer measurement before any LNP-mRNA therapeutic.

---

## CROSS-VECTOR FLAGS

| Compound/Intervention | V4 role | Cross-vector relevance |
|---|---|---|
| Tazemetostat (EZH2i) | MHC-I restoration → T-cell killing (V3→V4 primary bridge) | V3: primary epigenetic therapy; V4: enables T-cell checkpoint function. Critical dependency: V4 T-cell entries require V3 priming. |
| Entinostat (HDACi) | MHC-I restoration → T-cell killing (V3→V4 secondary bridge) | V3: epigenetic de-repression; V4: enables T-cell checkpoint function. Orthogonal to EZH2i — additive if combined (V3 Forward Hypothesis 1). |
| OTX015/BETi | PD-L1 suppression → checkpoint support | V1: BRD4 throttle (same target, clinical-grade); V3: super-enhancer collapse; V4: PD-L1 reduction for T-cell checkpoint. |
| Vitamin D3 | NK NKG2D upregulation | V3: VDR/CDKN1A differentiation axis; V4: NK cell function. |
| Omega-3 EPA/DHA (absent) | NK membrane function + anti-inflammatory TME | V1: RAS/ERK; V2: anti-inflammatory; V4: NK. Absence from regimen is a cross-vector gap. |
| Fiber (whole-plant, not juice) | Microbiome diversity → SCFA → CPI response correlation | V3: butyrate/HDACi colonic (not systemic); V4: microbiome-immune. |
| Sulforaphane | Weak HDACi (MHC-I UNESTABLISHED) | V1: Nrf2/ROS; V3: weak HDACi; V4: MHC-I UNESTABLISHED. Juicing reduces yield further. |

### Cross-Vector Synergy Candidates for Orchestrator

**Strongest cross-vector synergy: EZH2i (tazemetostat) + BETi (OTX015) + anti-PD-1**
- V3: EZH2i restores MHC-I; BETi collapses PD-L1 super-enhancer.
- V4: MHC-I restoration → T-cell killing; PD-L1 suppression → checkpoint blockade more effective.
- Three-drug combination has not been tested in CIC-rearranged sarcoma (V3 Forward Hypothesis 2). Highest priority cross-vector synergy candidate.
- Evidence tier for combination: Theoretical / early Clinical-Trial components individually.

**NK MHC-I tension — orchestrator flag:**
V3 epigenetic MHC-I restoration (Ranks C1, C2) partially REDUCES NK cell visibility (NK killing requires MHC-I-low). V4 NK entries (Rank C4, C8) are optimally deployed BEFORE V3 MHC-I restoration. This sequencing tension must be surfaced in the orchestrator's final catalog. Suggested orchestrator note: NK-first (exploit MHC-I-low) → then epigenetic priming (restore MHC-I) → then T-cell/checkpoint.

---

## FORWARD HYPOTHESES

**[Forward Hypothesis 1] Sequential NK → epigenetic priming → checkpoint sequence exploiting the MHC-I-low CIC-DUX4 state as a two-phase immune attack.**

Hypothesis: CIC-DUX4 cells are MHC-I-low (NK-susceptible); after NK cytoreduction, V3 epigenetic priming (EZH2i, restoring MHC-I) converts residual cells to T-cell-visible targets; anti-PD-1 then prevents T-cell exhaustion. The three-phase sequence (NK activation phase → epigenetic MHC-I restoration phase → checkpoint blockade phase) exploits both immune killing arms sequentially, avoiding the mechanistic trade-off between NK targeting (needs MHC-I-low) and T-cell targeting (needs MHC-I-high).

Mechanistic basis: NK missing-self mechanism + EZH2i MHC-I restoration mechanism + anti-PD-1 checkpoint mechanism are mechanistically orthogonal and temporally separable. This three-phase approach is not documented in any published clinical trial for any tumour type.

Study design: CIC-DUX4 PDX or humanised mouse model. Phase 1: adoptive NK transfer or IL-15 superagonist days 1-14. Phase 2: tazemetostat days 15-35. Phase 3: anti-PD-1 day 36 onward. Arms: each phase alone, sequential pairs, full triplet. Primary endpoint: tumour volume, NK/T-cell infiltration dynamics, MHC-I expression trajectory. Why untested: no CIC-DUX4 syngeneic/humanised mouse model available; disease rarity; complexity of three-phase design.

**[Forward Hypothesis 2] Post-ifosfamide lymphodepletion window as optimal timing for checkpoint + EZH2i initiation in oligometastatic CIC-rearranged sarcoma, exploiting radiation-primed STING context in lung.**

Hypothesis: This specific patient presents a rare convergence of three immune-enabling factors: (1) ifosfamide-induced lymphodepletion creates reconstituting lymphocyte compartment enriched for naive/central memory cells with higher proliferative potential; (2) prior WLI has established a radiation-primed STING-active pulmonary immune microenvironment; (3) one residual lung lesion is in this primed context. Initiating tazemetostat (EZH2i, weeks 4-6 post-ifosfamide) followed by pembrolizumab (weeks 6-8 onward) could exploit all three factors simultaneously: lymphodepleted background supports homeostatic T-cell expansion, radiation-primed TME provides co-stimulation, EZH2i makes residual tumour cells visible.

Mechanistic basis: Post-lymphodepletion homeostatic T-cell expansion (IL-7/IL-15 driven); STING-mediated IFN-γ/DC priming from radiation (Deng et al., Immunity 2014, PMID 25517614 — not CIC-DUX4 specific); EZH2i MHC-I mechanism from V3.

Study design: Phase Ib window-of-opportunity in post-high-dose-ifosfamide oligometastatic sarcoma patients (any histotype) with prior thoracic radiation: tazemetostat initiation day 28 post-ifosfamide → pembrolizumab initiation day 42. Primary endpoints: T-cell reconstitution quality (TCR repertoire diversity, neoantigen-reactive T-cell frequency), ORR at 16 weeks. Stratify by prior WLI yes/no to test the radiation-primed STING hypothesis.

**[Forward Hypothesis 3] Anti-PEG antibody titer-stratified LNP-mRNA therapeutic dosing as a personalised PK framework for BNT162b2-primed sarcoma patients.**

Hypothesis: Anti-PEG antibody induction from BNT162b2 vaccination in this patient population is a known but unquantified variable that could reduce delivery efficiency of any future LNP-mRNA therapeutic (neoantigen vaccine, therapeutic mRNA). Pre-treatment anti-PEG titer measurement and titer-stratified dosing protocols (higher dose for high-titer patients; or alternative non-PEG-LNP formulation) could improve the probability of therapeutic response to mRNA-based cancer vaccines in this patient population.

Mechanistic basis: Anti-PEG IgG opsonizes PEG-LNP → complement activation → macrophage clearance in Kupffer cells/spleen → reduced lymph-node delivery → diminished neoantigen-specific T-cell priming (Ishida et al., J Controlled Release 2006, PMID 16797763). Kozma et al. (NPJ Vaccines 2022, PMID 35853896 — verify) confirmed anti-PEG antibody induction post-BNT162b2.

Study design: PK sub-study in an mRNA cancer vaccine trial (NCT03897881 or NCT04486378): stratify by pre-treatment anti-PEG titer (ELISA). Primary endpoint: correlation of titer with mRNA payload delivery to draining lymph nodes (radiolabeled lipid biodistribution in preclinical arm) and with neoantigen-specific CD8+ T-cell response magnitude. Longitudinal arm: repeat titer measurement at 3, 6, 12 months to assess titer dynamics relative to vaccine dosing.

---

## ATYPICAL-CASE NOTES

**This patient is fusion-UNCONFIRMED (~5% subgroup). CIC-DUX4, CIC-NUTM1, CIC-FOXO4 — none confirmed on genomic sequencing.**

FUSION-CONFIRMED ONLY — POSSIBLY INAPPLICABLE to this patient:
- CIC-DUX4 junction-specific neoantigen vaccine (no confirmed junction sequence → cannot design junction peptide component).
- Junction-specific TCR-T (same reason).
- Pan-CIC-DUX4 junction vaccine (same reason).
- Any junction-specific neoantigen in a personalised vaccine pipeline.
- Note from mRNA team (incorporated): "A CIC-DUX4-junction-specific neoantigen vaccine is not applicable to this patient without confirmatory fusion identification."

FUSION-AGNOSTIC — applicable to this patient:
- ALL checkpoint inhibitor entries (C1-C6): target PD-1/PD-L1/CTLA-4, not the fusion protein.
- ALL epigenetic priming entries (tazemetostat, entinostat, OTX015 as V3→V4 bridge): target PRC2, HDAC, BRD4 machinery, which is active in CIC-rearranged sarcoma phenotype regardless of which upstream fusion drives it.
- ALL NK cell entries (D1-vitamin D3, D4-zinc, C4-N-803, C8-adoptive NK): NK missing-self killing is fusion-agnostic.
- Personalised neoantigen vaccine from somatic WES/RNA-seq (non-junction) neoantigens: fusion-agnostic if implemented from tumour mutational landscape analysis (not junction peptide).
- ALL dietary entries.
- ALL microbiome entries.

---

## RECONCILIATION NOTES

Reconciled from four specialist outputs:

1. **Vitamin D3:** Appeared in NK Cell Specialist (NKG2D upregulation on NK cells) and as cross-reference from V3 (VDR/CDKN1A differentiation). Merged into D1 with both mechanisms preserved; NK mechanism primary for V4.

2. **Omega-3:** Appeared in NK Cell Specialist (membrane lipid/NK synapse). Noted absent from patient regimen. V1 cross-vector (RAS/ERK) noted. Single merged entry D3.

3. **Curcumin + piperine:** Appeared in Checkpoint/T-cell Specialist (PD-L1 NF-κB) and Microbiome Specialist (microbiome modulation). Merged into D-track "no significant V4 benefit" with chemo interaction flags from both specialists preserved. V3 BRD4 cross-reference retained.

4. **Black cumin seed oil:** Appeared in Checkpoint/T-cell (no mechanism) and Microbiome (antimicrobial concern). Merged; CYP3A4/CYP2C9 interaction flag from V3 retained; ifosfamide activation concern is the key clinical flag.

5. **Tazemetostat:** Appears as V3→V4 bridge input (from v3-summary.md MHC-I section) and as primary clinical entry C1. Single merged entry. FDA approval (epithelioid sarcoma, 2020-01-23) from V3; EMA status: requires independent verification against EMA product database — not confirmed here.

6. **Melanoma microbiome evidence:** Routy 2018, Gopalakrishnan 2018, Davar 2021 all originated from melanoma/NSCLC cohorts. These citations do not transfer cleanly to sarcoma. Explicitly noted throughout and in the microbiome section. Orchestrator should not treat these as sarcoma-specific evidence.

7. **NK–MHC-I tension:** Identified by NK Cell Specialist. Surfaced as cross-vector synergy tension in this reconciliation. Orchestrator must sequence NK before epigenetic MHC-I restoration, or accept partial attenuation of NK effect after EZH2i initiation.

8. **Neoantigen vaccine — fusion-unconfirmed flag:** Most impactful case-specific constraint for the neoantigen specialist's output. All junction-specific entries labeled POSSIBLY INAPPLICABLE. Non-junction personalised approach retained as conceivable if tissue available.

9. **Anti-PEG antibody flag:** From mRNA team, Section 5a. Applied to all LNP-mRNA therapeutic entries (Ranks C7, and any future neoantigen vaccine). This is a PK stratification flag, not a contraindication.

---

## WHAT I COULD NOT ESTABLISH

1. **CIC-DUX4-specific T-cell infiltration (TIL) density and phenotype.** Whether these tumours are immunologically "hot," "excluded," or "cold" is not established from published data. This is the most fundamental gap for V4 planning.

2. **Direct NK killing assay in CIC-DUX4 cell lines.** The NK missing-self rationale is mechanistically strong; direct experimental confirmation is absent from the published literature.

3. **Stress ligand (MICA/MICB, ULBP1-6) expression on CIC-DUX4 tumour cells.** Missing-self alone is insufficient for NK killing; activating ligands must also be present. CIC-DUX4 stress ligand expression profiling is not published.

4. **PD-L1 expression data in a large CIC-DUX4 series.** Small case series suggest variable expression; no dedicated IHC dataset.

5. **This patient's TMB.** CIC-rearranged sarcomas are typically TMB-low; without WES data on this specific tumour, the neoantigen landscape is unknown.

6. **This patient's 25(OH)D level and NK compartment status.** Both are required to grade the clinical relevance of vitamin D3 and NK reconstitution recommendations.

7. **Microbiome composition in any CIC-rearranged sarcoma patient.** No published data. All microbiome–CPI associations come from melanoma/NSCLC cohorts (explicitly noted throughout).

8. **Whether radiation-STING-mediated pulmonary immune priming persists >1 year post-WLI in this patient.** Documented acutely; long-term persistence unknown.

9. **Anti-PEG antibody titer in this specific patient.** Measurable only by ELISA; prevalence ~30-50% of BNT162b2 recipients (Kozma 2022 — verify).

10. **Junction sequence.** The most clinically constraining unknown for this specific patient — limits junction-specific neoantigen vaccine and TCR-T applicability. V3 Forward Hypothesis 3 (long-read WGS re-analysis) is the recommended diagnostic intervention to address this.
