# CIC-Rearranged Sarcoma — Multi-Vector Hypothesis Catalog (v2)

> **v2 = a fresh full multi-agent re-run**, not an edit of v1. It re-executes all four vectors + the mRNA team + the Metastatic Disease Specialist with the **framework improvements contributed via Issues #7–#11 (ADRs 0001, 0003–0006) baked in natively**: the missing-data/biomarker value-of-information taxonomy (#7), the confidence-scoring axis (#8), the translational-feasibility bands (#9), the host-biology modifier layer (#10), and the V4 danger-signaling/ICD/Nectin expansion + inflammation-state lens (#11). `protocol-v1.md` is preserved as the baseline. **A "What changed from v1" changelog is at the bottom.**
>
> **This is a research-simulation output — not a treatment plan and not medical advice.**

---

## KEY-MAP CALLOUT — What Each Vector / Team Represents (read first)

| Label | Name | What it represents (one line) |
|---|---|---|
| **V1** | **Rate Limiting** | Throttle the oncogenic loop's speed/output — dampen RAS/ERK, BRD4 super-enhancer amplification, CDK4/CCND1 cell-cycle execution **downstream** of the fusion. Does **not** fix the fusion. |
| **V2** | **Compiler Protection** | Reduce the rate at which neighboring at-risk cells acquire a *new* translocation — lower ROS/DSB burden, support DNA-repair fidelity, calm inflammation. Upstream prevention; least relevant to an existing lesion. |
| **V3** | **Hot Patching** | Restore tumor-suppressor / differentiation signaling in cells that already carry the fusion — EZH2/EED-i, BETi, CDK4/6i, HDACi, DNMTi, differentiation. Dietary contribution weakest here. |
| **V4** | **Immune Watchdog** | Restore immune visibility + clearance — MHC-I restoration (depends on V3 priming), checkpoint, **NK missing-self**, danger-signaling/ICD, the **Nectin–TIGIT–DNAM-1 axis**, neoantigen vaccines. |
| **mRNA Team** | **mRNA COVID-19 Vaccine Research Team** | Supplementary. Does BNT162b2 modify the immune/inflammatory/genomic context relevant to this sarcoma? Feeds V2 + V4. Does not attack the tumor. |
| **Metastatic Specialist** | **Metastatic Disease Specialist** | Orchestrator sub-agent. Per vector: does metastatic (here: post-WLI lung) biology change the picture? |
| *Host-biology layer* | *Cross-cutting modifier (ADR-0005)* | Not a vector. Microbiome/SCFA, systemic inflammation, metabolic/nutrition, activity, sleep, autonomic — conditions V4 + SOC tolerability; weighted via the confidence axis. |

**Scoring axes used throughout (ADR-0004 / docs/08):** every confirmatory entry carries **Tier** (Established › Clinical-Trial › Preclinical-Animal › Preclinical-Cell › Mechanistic › Dietary-Observational › Theoretical), a **Confidence** label from four audited axes — **D**irectness-to-CIC-DUX4 / **A**chievability-of-exposure / **R**eproducibility / conflict-overhang **X** → High/Moderate/Low — and a **Feasibility band** F1 (accessible now) … F5 (concept only). Forward Hypotheses are *not* scored; they carry a **falsifier** instead (two-lane rule).

---

## Framing
Purpose, in order: (1) a forward-simulation research exercise; (2) personal literature exploration; (3) only if a non-obvious, mechanistically grounded hypothesis emerges, a conversation-starter with a qualified oncologist. **No entry is a dose, protocol, or start/stop instruction.** Direct evidence in CIC-rearranged sarcoma is essentially **absent for every dietary compound and for most clinical agents** — rationale is extrapolated from related fusion-driven sarcomas (Ewing, epithelioid, synovial); the **D-axis is `−` almost everywhere**, and the catalog says so rather than hiding it.

**Atypical / fusion-status note (load-bearing).** ~5% of clinically/histologically CIC-rearranged tumors have no confirmed fusion (CIC-DUX4/NUTM1/FOXO4/LEUTX). **This patient is in that fusion-unconfirmed subgroup.** Every entry is tagged:
- **`fusion-agnostic`** (downstream machinery: EZH2/PRC2, BRD4, CDK4/CCND1, differentiation, epigenetic MHC-I priming, all dietary V1/V2, checkpoint, NK, ICD, Nectin-axis, microbiome) — **still potentially applicable to this patient.**
- **`fusion-confirmed only — POSSIBLY INAPPLICABLE to this patient`** (junction ASOs, junction-specific vaccines/CAR-T/TCR-T, fusion PROTACs).

### Patient case (clean-slate; no stored individual memory used)
Soft-tissue CIC-rearranged sarcoma, dx June 2024, **fusion-UNCONFIRMED**. Primary: biceps femoris, R thigh. At dx: 12 lung mets. EURO EWING (VDC/IE) ×14, good response; surgery Jan 2025 (>95% necrotic); radiation to leg + **whole-lung irradiation (WLI)**. NED May 2025 → May 2026; **oligometastatic single-lung relapse**. **NOW preparing HIGH-DOSE IFOSFAMIDE.** This reality (imminent ifosfamide; prior doxorubicin/vincristine/etoposide/cyclophosphamide; prior WLI; lung-only pattern) drives the conflict and interaction sections.

---

## Top-Level Findings

1. **BRD4 / super-enhancer addiction is the strongest mechanistic entry point and it is fusion-agnostic** — BET inhibition collapses ETS super-enhancers (ETV4/5, MYC, CCND1) even if the fusion protein remains; the most robust target for a fusion-unconfirmed case. *[Clinical-Trial; Conf. Moderate; Feas. F3; no direct CIC-DUX4 data]*
2. **⚠️ CORRECTION FROM v1 — the V3→V4 MHC-I bridge is no longer tazemetostat.** Tazemetostat was **withdrawn from all markets 2026-03-09** (Ipsen; SYMPHONY-1 secondary hematologic malignancies; live-verified). The **EZH2-inhibition mechanism of MHC-I restoration stands**; the accessible agents are now **valemetostat / MAK683 (EZH2/EED) and entinostat (class I HDACi)**. *[Clinical-Trial; Conf. Moderate; Feas. F3; perishable — re-verify]*
3. **The NK missing-self arm is the non-obvious, well-grounded lever** — the same MHC-I-low state CIC cells use to hide from T-cells makes them NK targets, and the **relapsed/immune-selected clone is *more* likely MHC-I-low**. *[Mechanistic / Clinical-Trial; Conf. Low–Moderate]*
4. **An NK-vs-MHC-I sequencing tension is real and must not be papered over** — epigenetic MHC-I restoration helps T-cells but blunts NK missing-self *and may co-induce HLA-E* (a second brake). Suggested order: **NK-first → MHC-I restoration (paired with anti-NKG2A) → checkpoint.** *[Mechanistic]*
5. **The single highest-priority item for THIS patient is not adding anything — it is the interaction screen on what he already takes:** piperine + curcumin + thymoquinone are CYP3A4 inhibitors, and **ifosfamide is a CYP3A4-activated prodrug** → potential under-activation. *[Mechanistic/Preclinical PK; Conf. Low but X-axis conflict drives priority]*
6. **For dietary V1/V2 compounds the decisive limit is concentration mismatch (A-axis hard-minus)** — dietary plasma runs 10–500× below the cell-line active concentrations. Sulforaphane has the best ratio, but **juicing broccoli destroys myrosinase → near-zero sulforaphane.** *[Preclinical-Cell; Conf. Low]*
7. **Omega-3 EPA/DHA is the best cross-vector dietary compound** (V1 membrane/RAS, V2 SPM-resolution of the post-WLI lung, V4 NK), lowest interaction risk — and it is **absent** from the patient's regimen (a notable gap). *[Dietary-Observational + Mechanistic; Conf. Low–Moderate; Feas. F1]*
8. **The ADR-0006 expansion adds a third, orthogonal immune lever: danger-signaling/ICD** — and the patient's own **prior doxorubicin is a bona fide ICD inducer** (the SOC backbone already did immune work). The **Nectin axis** matters via **ligand-side blockade (anti-PVR / NTX1088)**, mechanistically distinct from the **failed anti-TIGIT receptor phase-3s**. *[Preclinical-Animal / Clinical-Trial]*
9. **mRNA COVID-19 vaccination is a null finding for this patient's current biology** — no persistent immune/inflammatory/genomic effect at >2 yr — with one carry-forward: **anti-PEG antibodies** could reduce delivery of a *future* LNP-mRNA cancer vaccine (measure titer first). *[Clinical observational]*
10. **V2 is the least applicable vector to the current disease** — the relapsed lesion already carries the driver; V2's value is narrow (modifying the post-WLI lung niche), not trajectory-changing. *[Mechanistic]*

---

## Naturally Achievable Track

> Every entry carries: **"Potential interactions with standard-of-care chemotherapy and concurrent medications — must be reviewed by the patient's oncologist before any change."** Doubly important with high-dose ifosfamide imminent.

### Diet (mechanistically grounded, food-level)

| Compound | Vector(s) | Mechanism (1 line) | Tier | Conf. | Feas. | Fusion | CIC-DUX4? | Food sources | SOC flag |
|---|---|---|---|---|---|---|---|---|---|
| **Omega-3 EPA/DHA** | V1,V2,V4 | Lipid-raft remodeling impairs RAS clustering; resolvins/protectins → ALX/FPR2 → ↓NF-κB/NOX2; NK membrane support | Diet-Obs + Mech | Low–Mod | F1 | agnostic | None | Mackerel, sardines, herring, wild salmon | Anti-platelet at supplement doses peri-ifosfamide; food-level low risk |
| **Sulforaphane** (properly activated) | V1,V3,V4 | Weak class-I HDACi (5–30 µM) + Nrf2; possible MHC-I support (UNESTABLISHED at dietary exposure) | Preclin-Cell | Low | F1 | agnostic | None | Broccoli **sprouts**, chopped/chewed (myrosinase) — **juicing → ~0 yield** | Nrf2/ROS interference theoretical at supplement dose; culinary subclinical |
| **Quercetin** | V1,V2 | Multi-RTK/RAS inhibition + weak EZH2 modulation; severe concentration mismatch | Preclin-Cell | Low | F1 | agnostic | None | Capers, raw red onion, apple skin | CYP3A4/P-gp at supplement doses |
| **Apigenin/Luteolin** | V1 | Apigenin ↓ETS-factor expression; luteolin cell-cycle modulator (50–250× above food) | Preclin-Cell | Low | F1 | agnostic | None | Celery, parsley, chamomile | CYP2C9/CYP3A4 at supplement doses |
| **Vitamin D3** (deficiency-correction) | V3,V4 | Calcitriol-VDR → p21 (partial G1 exit); NK NKG2D ↑ | Mechanistic | Low–Mod (if deficient) | F1 | agnostic | None | Sun, fatty fish, supplement if deficient | Hypercalcemia monitoring; no VDC/ifosfamide interaction |
| **Zinc** (deficiency-correction) | V1,V2,V4 | Cofactor Ku70/80, p53 zinc-finger, PARP1; NK maturation | Mechanistic | Mod (if deficient) | F1 | agnostic | None | Oysters, pumpkin seeds, meat | >40 mg/d displaces copper |
| **Whole-plant fiber / fermented foods** | V4 | Fermentable fiber → SCFA; diversity ↔ checkpoint response (melanoma/NSCLC, **not** sarcoma) | Diet-Obs | Low | F1 | agnostic | None | Legumes, whole grains, veg; yogurt/kefir/kimchi | Avoid unpasteurized ferments during neutropenia |

### Supplements (only where safety profile established; published trial dose-ranges; **none for CIC-DUX4**)

| Compound | Vector(s) | Mechanism | Tier | Conf. | Published dose-range (indication ≠ CIC-DUX4) | SOC flag |
|---|---|---|---|---|---|---|
| **Curcumin (± piperine)** | V1,V2,V4 | BRD4-chromatin disruption (5–20 µM); NF-κB inhibition | Preclin-Cell | Low | Phase I safety 4–8 g/d (Cheng *Anticancer Res* 2001) | **HIGH** — piperine CYP3A4+P-gp; see Interaction Map |
| **EGCG** | V1,V2 | BRD4 BD1 + weak EZH2 (10–50 µM, 30–150× above dietary) | Preclin-Cell | Low | 400–800 mg/d prostate prevention; hepatotoxicity high-dose | P-gp → vincristine/etoposide |
| **Vitamin D3** | V3,V4 | as above | Mechanistic | Low–Mod | 2000 IU/d (VITAL PMID 30415629; null for cancer) | correct deficiency first |
| **Selenium** | V1,V2 | Selenoprotein/TrxR cofactor | Preclin + Diet-Obs | Low | SELECT null (PMID 19066370); UL 400 µg/d | narrow window; prefer 1–2 Brazil nuts |
| **Berberine** | V1 | AMPK→mTORC1↓→↓MYC translation; ~1% oral bioavailability | Preclin-Cell | Low | 500 mg TID metabolic trials | CYP3A4 inhibition — same ifosfamide concern |

### Lifestyle
- **Correct documented vitamin D deficiency** (clearer evidence than replete supplementation).
- **Whole-food fiber over juicing** — the juice-based approach removes prebiotic fiber *and* defeats sulforaphane (myrosinase). Whole broccoli/skin-on apple/legumes give far more substrate (host-biology layer).
- **Marine omega-3** (2–3 servings fatty fish/week) addresses the regimen's main gap and the post-WLI lung-inflammation context.
- **Sleep / activity** — supportive-care; no CIC-DUX4-specific claim. (See host-biology section.)

---

## Clinical / Experimental Track (For Oncologist Discussion Only)

> **Not naturally achievable; awareness only.** None approved for CIC-rearranged sarcoma. FDA/EMA columns refer to the cited *other* indication. **Status is perishable — re-verify live (`[VERIFY]`).**

| Intervention | Vector(s) | Mechanism | Tier | Conf. | Feas. | FDA | EMA | Trial IDs | Fusion / Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Valemetostat (dual EZH1/2i)** | V3→V4 | H3K27me3↓ at HLA/TAP/B2M/NLRC5 → MHC-I; de-represses CDKN2A | Clinical-Trial | Mod | F3 | not approved (solid) | not approved | NCT07303387 [VERIFY] | agnostic. **Primary post-tazemetostat MHC-I bridge** |
| **MAK683 (EED/PRC2 allosteric)** | V3→V4 | Blocks EED–H3K27me3; usable if EZH2i-resistant | Clinical-Trial | Mod | F3 | not approved | not approved | NCT02900651; PMID 39793445 | agnostic. Second EZH2-pathway option |
| **Entinostat (class I HDACi)** | V3→V4 | NLRC5/APM de-repression → MHC-I; p21 | Clinical-Trial | Mod | F3 | not approved (breakthrough elsewhere) | not approved | NCT02890069 | agnostic |
| **OTX015 / BMS-986158 (BETi)** | V1,V3,V4 | Collapse ETS super-enhancers; ↓PD-L1 super-enhancer | Clinical-Trial | Mod | F3 | not approved | not approved | NCT01713582; NCT02419417 (PMID 36077617) | agnostic. Strongest entry point |
| **Palbociclib / Ribociclib / Abemaciclib (CDK4/6i)** | V1,V3 | Rb hypophosphorylation → E2F↓ → G1 arrest | Established (HR+ breast); Clin-Trial (sarcoma) | Mod | F2 | approved breast | approved breast | PMID 37875500 (palbo sarcoma mPFS 4.2 mo); NCT03677388 | agnostic. **Additive myelosuppression with ifosfamide → sequential only** |
| **Azacitidine / Decitabine (DNMTi)** | V3→V4 | ERV demethylation → cGAS-STING → type-I IFN → MHC-I (viral mimicry) | Established (MDS/AML); Clin-Trial (solid) | Mod | F2/F3 | approved MDS/AML | approved MDS/AML | PMID 26317466; 26317465 | agnostic. Orthogonal STING route |
| **Pembrolizumab / Nivolumab ± Ipilimumab** | V4 | Checkpoint release on (primed) CD8; ipi adds Treg depletion | Established (mel/NSCLC/RCC); Clin-Trial (sarcoma, modest SARC028) | Mod | F2 | approved multiple | approved multiple | NCT02301039 (SARC028); NCT02978625 (A091401, PMID 30501812) | agnostic. **Efficacy depends on V3 MHC-I priming** |
| **N-803 (IL-15 superagonist)** | V4 (NK) | IL-15/IL-15Rα-Fc → NK vs MHC-I-low cells | Established (NMIBC+BCG); Clin-Trial (solid) | Mod | F2/F3 | approved NMIBC 2024 | [VERIFY] | NCT03055780 | agnostic. **Deploy BEFORE MHC-I restoration** |
| **NTX1088 (anti-PVR/CD155)** | V4 (Nectin) | Removes shared PVR ligand → lifts TIGIT/CD96/PVRIG **and** restores DNAM-1 | Clinical-Trial (Ph1) | Low | F3 | not approved | not approved | NCT05378425 [VERIFY] | agnostic. **Distinct from failed anti-TIGIT (SKYSCRAPER-01/-02)** |
| **Monalizumab (anti-NKG2A)** | V4 | Blocks NKG2A–HLA-E brake; pairs with MHC-I restoration | Clinical-Trial (other tumors) | Low | F3 | not approved | not approved | [VERIFY] | agnostic. Addresses the HLA-E escape valve |
| **Adoptive NK transfer** | V4 (NK) | Haploidentical NK in lymphodepleted host → kill MHC-I-low cells | Clin-Trial (heme); Preclin (solid) | Low | F4 | not approved | not approved | heme precedent PMID 11786547 | agnostic. Post-ifosfamide window |
| **Personalized neoantigen vaccine (somatic, NON-junction)** | V4 | Patient SNV/indel neoantigens via LNP-mRNA → DC → CD8 | Clin-Trial (melanoma) | Low | F4 | not approved | not approved | NCT03897881 (mRNA-4157); NCT04486378 (BNT122) | agnostic **only if non-junction**; check anti-PEG titer |
| ~~Tazemetostat (EZH2i)~~ | — | (mechanism valid) | **WITHDRAWN** | — | **F5 (withdrawn)** | **withdrawn 2026-03-09** | no central approval (orphan only) | — | **DO NOT cite as accessible** |
| **CIC-DUX4 junction ASO / PROTAC / junction vaccine / TCR-T / CAR-T** | V3,V4 | Junction-targeted | Theoretical/Preclin | Spec. | F5 | none | none | none clinical-stage | **fusion-confirmed only — POSSIBLY INAPPLICABLE** |

---

## Patient's Actual Self-Administered Regimen — Dedicated Assessment

Regimen: curcumin+piperine, liposomal vitamin C, black cumin seed oil (Nigella sativa / thymoquinone), vitamin D, honey, and (during chemo) fresh juice of celery/ginger/carrot/broccoli/apple/beetroot. **Verdict per item — helping / neutral / potentially harmful (timing-dependent):**

| Item | Active(s) | Verdict | Why (mechanism + interaction) |
|---|---|---|---|
| **Curcumin + piperine** | curcumin (BRD4/NF-κB), **piperine (CYP3A4/P-gp inhibitor)** | **POTENTIALLY HARMFUL pre-ifosfamide — oncologist review** | Piperine + curcumin inhibit CYP3A4, which **activates** the ifosfamide prodrug → possible ↓4-OH-ifosfamide/efficacy; P-gp inhibition could ↑vincristine/etoposide exposure. **Shoba 1998 caveat (verbatim):** the popularized "2000% bioavailability boost" is from Shoba et al. 1998 (Planta Med) — **n=10, single oral dose, control arm below limit of detection** — a directional finding, **not** a universal multiplier. Therapeutic anti-tumor effect at dietary dose: not plausible (concentration mismatch). |
| **Black cumin seed oil** | thymoquinone (CYP3A4 + CYP2C9 inhibitor) | **POTENTIALLY HARMFUL pre-ifosfamide — oncologist review** | Same CYP3A4-mediated ifosfamide-activation concern; no robust human PK; no established anti-tumor mechanism at dietary exposure. Highest-priority dietary safety flag alongside piperine/curcumin. |
| **Liposomal vitamin C** | high-dose ascorbate | **POTENTIALLY HARMFUL (timing-dependent) — oncologist timing decision** | ROS-axis interference was highest with **doxorubicin** (completed). Ifosfamide is alkylation-primary → lower but real precaution against high-dose antioxidants during active cytotoxic therapy. Plus the **Sayin 2014/Le Gal 2015** antioxidant-metastasis signal (Preclinical-Animal; KRAS/BRAF models — transfer to fusion sarcoma unproven) matters precisely because the patient has **residual/disseminating disease**. |
| **Carrot juice (β-carotene)** | β-carotene | **NEUTRAL at food level — do NOT misapply ATBC/CARET** | ATBC/CARET harm is from **isolated pharmacological-dose supplements** in smokers; food-level juice (plasma ~0.4–0.8 µmol/L) is far below pro-oxidant range. β-carotene *supplements* remain contraindicated. |
| **Broccoli juice** | (sulforaphane) | **NEUTRAL → suboptimal** | **Juicing destroys myrosinase** → near-zero sulforaphane; whole chopped/chewed sprouts needed for any yield, and even then MHC-I/HDAC effect is UNESTABLISHED at dietary exposure. |
| **Celery / ginger / apple / beetroot juice** | apigenin/luteolin, 6-gingerol, quercetin, nitrate | **NEUTRAL (low-risk) at culinary dose** | Mechanisms real but concentration mismatch decisive; no significant CYP interaction at juice level (ginger only at high supplement doses). Juicing strips fiber (host-biology: less SCFA substrate). |
| **Vitamin D** | cholecalciferol | **HELPING if correcting deficiency; otherwise neutral** | VDR → p21 (V3) + NK NKG2D (V4). Replete-supplementation benefit thin (VITAL null). No ifosfamide/VDC interaction; hypercalcemia monitoring. Check 25(OH)D. |
| **Honey** | — | **NEUTRAL** | No CIC-DUX4 mechanism; no interaction at culinary dose. (Avoid for infants — N/A here.) |
| **Notable gap** | marine omega-3 EPA/DHA | **MISSING — would be the best-supported addition** | Best cross-vector dietary compound, lowest interaction risk, directly relevant to the post-WLI lung niche (see Forward Hyp). |

**Net:** the regimen's most important issue is **not** efficacy — it is the **CYP3A4 cluster (piperine + curcumin + thymoquinone) vs the imminent ifosfamide prodrug**, plus the **high-dose liposomal vitamin C timing** question. Both are clinical conversations the oncologist must have *before* the next cycle.

---

## mRNA COVID-19 Vaccine — Research Findings
Net: **no relevant persistent effect for this patient — a complete null, stated explicitly.** Acute LNP/TLR4-NLRP3 cytokine pulse resolves <72 h; spike-specific T-cell memory + transient NK activation wane by ~12 months / ~30 days; no persistent PD-1/PD-L1, NK, or Nectin-axis modulation; no peer-reviewed genomic-integration/instability signal (the Alden Huh7 claim is non-physiological and rebutted); no sarcoma pharmacovigilance signal (with an honest **detection-floor caveat** — CIC sarcoma ~1–2/million/yr is below any database's resolving power). **Inflammation-state framing (ADR-0006):** the vaccine's effect was a transient State-1 pulse, long resolved; dominant inflammatory inputs are now **WLI lung + ifosfamide + relapse TME**, not the vaccine. **Carry-forward (→V4):** measure **anti-PEG titer** before any future LNP-mRNA neoantigen vaccine (ABC phenomenon; Kozma 2022 PMID 35853896 [VERIFY]; Ishida 2006 PMID 16797763). Full brief: `mrna-vaccine-research/mrna-vaccine-summary-v2.md`.

---

## Metastatic Disease Considerations
Full analysis: `metastatic-disease-considerations-v2.md`. Re-weighting: **V1** applies but is *weaker* in a post-WLI fibrotic lung (delivery↓ on top of concentration mismatch); **V2** does not clearly apply to the established lesion (only the post-WLI niche); **V3** is arguably *most* relevant (targets maintenance machinery of cells already carrying the lesion) but argues for **re-biopsy of the relapse**, not the Jan 2025 specimen; **V4** has the most metastatic reinterpretation — the relapsed clone is **immune-selected → more likely MHC-I-low → NK-first is *more* defensible here**, and lung is a comparatively favorable, possibly STING-primed checkpoint site. Two metastasis-specific forward hypotheses (NK-first in the lymphodepletion window; omega-3/SPM resolution of the irradiated-lung niche) are carried below.

---

## Host-Biology Modifier Layer (ADR-0005 — cross-cutting, NOT a fifth vector)
Conditions V4 efficacy + SOC tolerability; weighted via the confidence axis (it down-weights, it does not add a score). Most-relevant modifiers for this patient:
- **Microbiome / SCFA:** the **juice-over-whole-food** pattern lowers fermentable-fiber substrate → less butyrate/propionate; whole foods would give more. Diversity ↔ checkpoint response is melanoma/NSCLC data, **not** sarcoma. *Actionable, low-risk.*
- **Systemic inflammation (NLR / mGPS):** prognostic, but **prognostic ≠ targetable** — and lowering it can hit anti-tumor State-2 too (inflammation-state lens). Post-WLI pneumonitis risk = State-3 toxicity confound.
- **Nutrition / sarcopenia:** relevant to ifosfamide tolerability; standard supportive-care territory.
- **Perioperative/peri-cytotoxic conditioning, sleep/circadian, autonomic/β-adrenergic, PNEI, placebo-nocebo:** plausible modifiers; no CIC-DUX4-specific evidence — kept as conditioning context, not recommendations.

---

## Biomarker Value-of-Information / Missing-Data (Issue #7 / ADR-0001)
*"What is unknown, and what would change the recommendation?"* — three-tier taxonomy + VoI ranking (full layer: `biomarker-voi-stratification.md`).
- **Known (this case):** fusion-UNCONFIRMED status; lung-only pattern; prior VDC/IE + WLI; imminent ifosfamide; self-administered regimen.
- **Missing — decision-relevant (HIGH VoI; would re-order vectors):**
  1. **Relapse-lesion MHC-I status** — pivots the entire NK-first-vs-MHC-I-restoration order (the catalog's central sequencing decision).
  2. **Junction sequence via long-read WGS/RNA-seq of archived/relapse tissue** — converts all `POSSIBLY INAPPLICABLE` junction approaches (ASO, junction vaccine, TCR-T) to *applicable*, and refines histo-classification.
  3. **PD-L1 / TIL density / immune contexture** of the relapse — grades checkpoint plausibility.
  4. **CDKN2A status + BRD4/PRC2 dependency on the *relapse* clone** — grades V3 agent selection (EZH2-pathway vs CDK4/6i vs BETi).
  5. **Nectin-axis (PVR/CD155, TIGIT/DNAM-1) + MICA/MICB shed levels** — grades the anti-PVR/NK strategy.
- **Missing — low-impact:** anti-PEG titer (only matters if an LNP-mRNA vaccine is actually pursued); 25(OH)D / Zn / Se / B12 (matter only for deficiency-correction, not trajectory).

---

## Forward Hypotheses (curated, ranked by plausibility × feasibility)

1. **[FH-1] NK-first ligand-side de-repression (anti-PVR), not TIGIT-receptor blockade, in the MHC-I-low window** *(V4 + Metastatic M1).* Block tumor PVR/CD155 (NTX1088-class) ± IL-15 *before* MHC-I restoration — lifts TIGIT/CD96/PVRIG **and** restores DNAM-1 while missing-self still favors NK; timed to the post-ifosfamide reconstitution window. *Falsifier:* in a CIC-DUX4 PDX/NK-humanized model, anti-PVR ± IL-15 gives no NK infiltration/control gain, or the relapse proves MHC-I-normal.
2. **[FH-2] ICD-adjuvanted anthracycline timing — capture the danger window the existing doxorubicin already creates** *(V4).* Time an immune-capture step (DC-licensing/checkpoint/NK) into the post-anthracycline CALR/HMGB1/ATP window — no new drug. *Falsifier:* CIC-DUX4 cells are ICD-incompetent under anthracycline, or in-phase vs out-of-phase capture shows no CD8-priming difference.
3. **[FH-3] HLA-E/NKG2A is the predictable escape valve of epigenetic MHC-I restoration** *(V4).* Pair EZH2i/HDACi MHC-I restoration with **anti-NKG2A (monalizumab)**, not anti-PD-1 alone, because classical-MHC-I restoration may co-induce HLA-E. *Falsifier:* lines ± EZH2i/HDACi show MHC-I↑ without HLA-E co-induction, or anti-NKG2A adds no killing.
4. **[FH-4] Sequential dual-lock epigenetic priming (valemetostat → entinostat pulse) to maximize APM de-repression** *(V3).* Remove H3K27me3 then hyperacetylate the same APM loci for greater-than-additive MHC-I. *Falsifier:* sequential ≠ better than single-agent on HLA-A/B/C surface expression + CD8 killing.
5. **[FH-5] Post-WLI pulmonary niche resolution via omega-3/SPM** *(V2 + Metastatic M2).* RvD1/PD1 → ALX/FPR2 → ↓NOX2/IL-6/TGF-β in the irradiated lung → fewer DSBs **and** a less pro-colonization niche at the one organ this patient relapses in. *Falsifier:* EPA/DHA diet doesn't reduce lung-stromal γ-H2AX or metastatic colony count, or an ALX/FPR2 antagonist abolishes nothing.
6. **[FH-6] BETi → ifosfamide sequencing to exploit BRD4-dependent DDR super-enhancer collapse** *(V3).* 48–72 h BETi pre-treatment collapses DDR super-enhancers → transiently lowers HR repair of ifosfamide crosslinks; testable in this patient's imminent context. *Falsifier:* no DDR super-enhancer dependency on ChIP-seq, or no γ-H2AX/ctDNA difference with sequencing.
7. **[FH-7] Long-read WGS of archived specimen to resolve fusion-unconfirmed status** *(V3; highest VoI diagnostic).* Short-read WGS fails across DUX4 subtelomeric repeats (4q35/10q26); long-read/RNA-seq could recover the junction and unlock junction approaches + reclassification. *Falsifier:* long-read recovers no CIC-family fusion.

---

## Cross-Vector Synergies
- **Strongest:** **EZH2-pathway-i (MHC-I↑, V3→V4) + BETi (PD-L1 super-enhancer↓, V1/V3) + anti-PD-1 (V4)** — three orthogonal mechanisms, components individually Clinical-Trial; untested in CIC sarcoma. *(Note: now built on valemetostat/MAK683, not tazemetostat.)*
- **NK arm + Nectin (anti-PVR) + IL-15** before MHC-I restoration — the fusion-agnostic innate package for an MHC-I-low, immune-selected clone.
- **Omega-3 EPA/DHA** — the rare compound active across V1/V2/V4 with minimal interaction risk; the regimen's main gap.
- **Doxorubicin-ICD (already delivered)** latent immune synergy with any V4 capture step (FH-2).

---

## Conflicts and Open Questions
1. **NK-vs-MHC-I (+HLA-E) sequencing** — restoring MHC-I helps T-cells but blunts NK and may raise HLA-E. Resolved direction: NK-first → MHC-I restoration (with anti-NKG2A) → checkpoint. *Unresolved quantitatively.*
2. **High-dose antioxidants vs ROS-chemo vs metastasis** — liposomal vitamin C during/after ROS-contributing chemo, plus the Sayin/Le Gal metastasis signal in residual disease. Genuine, unresolved → clinical judgment.
3. **CYP3A4 cluster vs ifosfamide activation** — piperine/curcumin/thymoquinone could under-activate the prodrug. Mechanistically real; magnitude at the patient's doses unquantified.
4. **Tazemetostat withdrawal** — mechanism preserved, agent gone; successors (valemetostat/MAK683) are less mature and their ifosfamide-interaction/CYP profiles need verification.
5. **Silent literature** — no CIC-DUX4-specific data for MHC-I status, TIL contexture, Nectin/MICA expression, ICD competence, HLA-E response, or any metastasis molecular profile. Most of this catalog is extrapolation, tagged D=−.

---

## Standard-of-Care Interaction Map

| Compound | Interaction class | Concern vs this patient's SOC | Flag |
|---|---|---|---|
| Curcumin + piperine | CYP3A4 inhibitor; P-gp | ↓ifosfamide activation; ↑vincristine/etoposide | **HIGH — review before ifosfamide** |
| Thymoquinone (black-cumin oil) | CYP3A4 + CYP2C9; P-gp | ↓ifosfamide activation | **HIGH — review before ifosfamide** |
| Liposomal vitamin C | ROS-axis; possible pro-metastatic at pharmacological dose | doxorubicin (past) ROS; ifosfamide timing; residual-disease metastasis signal | **MODERATE — oncologist timing** |
| EGCG / berberine / quercetin (supplement doses) | CYP3A4 / P-gp | vincristine/etoposide/ifosfamide | **MODERATE if supplement-dose** |
| CDK4/6i (clinical) | additive myelosuppression | with high-dose ifosfamide | **Sequential scheduling, not concurrent** |
| Vorinostat/pan-HDACi (clinical) | additive toxicity | with ifosfamide | sequence after ifosfamide |
| Ginger/honey/vitamin-D (deficiency dose)/juice | none at culinary/deficiency dose | — | **LOW** |

---

## What This Catalog Cannot Tell You
- Whether any intervention will help **this** patient — it cannot; it is a research catalog.
- Doses, timing, or start/stop decisions — clinical, by definition out of scope.
- The molecular profile of the relapse clone, the relapse MHC-I status, the junction sequence, or this patient's cofactor/immune labs — all unknown here and **decision-relevant** (see VoI).
- Whether mouse-derived ICD/antioxidant-metastasis/STING biology transfers to fusion-driven sarcoma — untested.
- Perishable regulatory/trial status beyond the live-verification date stamped on each `[VERIFY]` item.

---

## Bibliography (verifiable; perishable items tagged `[VERIFY]`)
- ATBC, *NEJM* 1994, **PMID 8127329** · Omenn (CARET), *NEJM* 1996, **PMID 8602180** · Lippman (SELECT), *JAMA* 2009, **PMID 19066370** · Klein (SELECT vit E), *JAMA* 2011, **PMID 21990298**
- Sayin, *Sci Transl Med* 2014, **PMID 24477002** · Le Gal, *Sci Transl Med* 2015, **PMID 25471168** · Estruch (PREDIMED), *NEJM* 2018, **PMID 29897866** · Manson (VITAL), *NEJM* 2019, **PMID 30415629**
- Hainaut & Milner, *Cancer Res* 1993, **PMID 8422923** [VERIFY] · Shoba (curcumin+piperine), *Planta Med* 1998 (n=10 caveat)
- Casares (doxorubicin ICD), *J Exp Med* 2005, **PMID 16365148** · Obeid (calreticulin), *Nat Med* 2007, **PMID 17187072** · Apetoh (HMGB1/TLR4), *Nat Med* 2007, **PMID 17704786** · Ghiringhelli (ATP/P2RX7/NLRP3), *Nat Med* 2009, **PMID 19767732** · Deng (STING/RT), *Immunity* 2014, **PMID 25517614**
- D'Angelo (nivo+ipi, A091401), *NEJM*/Lancet 2018, **PMID 30501812** · SARC028, NCT02301039, D'Angelo *Lancet Oncol* 2017, **PMID 28792305** [VERIFY]
- Chiappinelli, *Cell* 2015, **PMID 26317466** · Roulois, *Cell* 2015, **PMID 26317465** · Sankar (Ewing EZH2i+HDACi), 2014, **PMID 24531741** · MAK683, **PMID 39793445** · BMS-986158, **PMID 36077617** · palbociclib sarcoma, **PMID 37875500**
- Routy 2018 **PMID 29209380** · Gopalakrishnan 2018 **PMID 29097493** · Sonnenburg/Gardner *Cell* 2022 **PMID 35839772** · Kozma *NPJ Vaccines* 2022 **PMID 35853896** [VERIFY] · Ishida *J Control Release* 2006 **PMID 16797763**
- Trials: NCT07303387 (valemetostat) [VERIFY] · NCT02900651 (MAK683) · NCT02890069 (entinostat+pembro) · NCT01713582 / NCT02419417 (BETi) · NCT03677388 (palbociclib) · NCT02978625 (A091401) · NCT03055780 (N-803) · NCT05378425 (NTX1088) [VERIFY] · NCT03897881 (mRNA-4157) · NCT04486378 (BNT122)
- Tazemetostat withdrawal: Ipsen press release + FDA Drug Alert, **2026-03-09** (live-verified 2026-06-03) · Anti-TIGIT: SKYSCRAPER-01 (OS-negative 2024-11-26), SKYSCRAPER-02 (negative 2022)

---

## What Changed From v1 (changelog for reviewers)
1. **Tazemetostat correction (load-bearing).** v1's Top-Finding #2 and clinical-track #1 named tazemetostat the "cleanest V3→V4 bridge / Established (epithelioid sarcoma)." v2 reflects its **2026-03-09 withdrawal**: mechanism retained, agent rerouted to **valemetostat / MAK683 / entinostat**; tazemetostat marked WITHDRAWN / F5 / do-not-cite-as-accessible.
2. **Three scoring axes native (#8/ADR-0004).** Every confirmatory entry now carries Tier + **Confidence (D/A/R/X → High/Moderate/Low)** + **Feasibility band (F1–F5)**, not tier alone.
3. **Translational-feasibility layer (#9/ADR-0003).** Feasibility bands + FDA/EMA-divergence + `[VERIFY]` live-status discipline applied across the clinical track.
4. **Host-biology modifier layer (#10/ADR-0005)** added as a cross-cutting section (microbiome/SCFA, inflammation, nutrition…), explicitly **not a fifth vector**.
5. **V4 expansion native (#11/ADR-0006).** Danger-signaling/ICD (doxorubicin as ICD inducer; CALR/HMGB1/ATP/HSP), the **Nectin–TIGIT–DNAM-1 axis** (anti-PVR/NTX1088 vs the failed anti-TIGIT phase-3s), NKG2A/HLA-E, MICA/MICB shedding, and the **inflammation-state lens** are integrated into V4 and the synthesis — not bolted on.
6. **Biomarker VoI / missing-data section (#7/ADR-0001)** added — explicit "what's unknown / what would re-order the vectors."
7. **Dedicated "Patient's Actual Self-Administered Regimen" assessment** with per-item helping/neutral/harmful verdicts and the Shoba 1998 caveat verbatim.
8. **Forward Hypotheses re-curated** to lead with the NK-first/anti-PVR and ICD-timing ideas enabled by the #11 expansion.

*Provenance: fresh full multi-agent re-run on branch `sim-protocol-v2`. Wave-1 (mRNA, V1, V3) + Wave-2 (V2, V4) leads + Metastatic Specialist; V2/V4 consolidated directly in the orchestrator thread after two background-dispatch ECONNRESET failures (per CLAUDE.md "practical caveat" — substance over delivery vehicle), using the vetted v1 artifacts + the ADR-0006 expansion as substrate. Orchestrator synthesis on Opus. v1 artifacts preserved. **Not medical advice.**)*
