# Metastatic Disease Considerations (v2) — CIC-Rearranged Sarcoma

> Orchestrator's Metastatic Disease Specialist analysis for the **v2 re-run**. Inputs: the four v2 vector summaries (`v1-summary-v2.md` … `v4-summary-v2.md`) + `mrna-vaccine-summary-v2.md`. Does NOT restate them — for each major finding it asks only whether metastatic biology changes the picture.
>
> **Not medical advice.** Any dietary/supplement consideration carries: "potential interactions with standard-of-care chemotherapy and concurrent medications — must be reviewed by the patient's oncologist before any change."

## Summary
Metastatic biology does not invalidate any vector but re-weights them and adds two structural caveats the primary-tumor framing understates: **(1)** metastatic cells are by definition an immune- and treatment-*selected* population — so V4 (immune evasion already "won" once) and any fusion-dependent target (clonal drift) carry more uncertainty than at diagnosis; **(2)** the **lung** — this patient's exclusive metastatic site, now **post-whole-lung-irradiation (WLI)** — is a distinct microenvironment whose altered vasculature, fibrosis, and resident-macrophage state change both drug/nutrient delivery and the immune context. **V2 is the least applicable vector** in established oligometastatic disease (the lesion already carries the driver). **V3 and the NK arm of V4 are the most metastasis-relevant.**

**Confidence: Low–Moderate** — the re-weighting is well-grounded in general metastasis biology, but CIC-rearranged sarcoma has essentially **no published metastasis-specific molecular data**, so every transfer is an extrapolation, tagged as such.

---

## Per-Vector Applicability in Metastatic Disease

**V1 — Rate Limiting — *applies, with caveats*.** BRD4/ETS/CDK4–CCND1 machinery is cell-intrinsic and fusion-agnostic → transfers to metastatic clones. But (a) clonal evolution through 14 cycles VDC/IE + radiation may have shifted the relapsed clone's dependency profile (cannot assume identical to primary without re-biopsy), and (b) dietary-compound penetration into a post-WLI fibrotic lung field is plausibly *reduced*, compounding V1's already-decisive plasma concentration-mismatch. Net: V1's "adjunctive, concentration-limited" framing is *weaker*, not stronger, here. CIC-DUX4 direct: None.

**V2 — Compiler Protection — *does not clearly apply to the established lesion*.** Preventing a *new* translocation does not address a clone that already carries the driver — V2 has the weakest claim on the current trajectory. Its only metastatic relevance is indirect: the post-WLI pulmonary inflammatory/oxidative field is both a genotoxic stressor and a tumor-supportive niche, so the omega-3/SPM arm can modify the metastatic *niche* (Mechanistic; Preclinical-Animal radiation-pneumonitis). The antioxidant arm carries a metastasis-specific hazard (Sayin/Le Gal, below). CIC-DUX4 direct: None.

**V3 — Hot Patching — *applies; arguably the most relevant vector, with one new caveat*.** The clinical track (EZH2-pathway-i, BETi, CDK4/6i, DNMTi, HDACi) targets the maintenance machinery of cells already carrying the lesion — exactly the metastatic population — and is fusion-agnostic. The metastatic addition is **target heterogeneity across sites/time**: MHC-I-low state, PRC2 dependency (inferred from CDKN2A), and BRD4 occupancy were (if ever) characterized on the *primary*; the relapsed lung clone may differ → argues for re-biopsy of the **relapse**, not reliance on the Jan 2025 resection. **v2 note:** the agent feeding the V3→V4 bridge is no longer tazemetostat (withdrawn 2026-03-09) — the **mechanism** is unchanged but the metastatic-consolidation plan now routes through **valemetostat/MAK683/entinostat**. Junction ASO/PROTAC remain POSSIBLY INAPPLICABLE regardless of site. CIC-DUX4 direct: None.

**V4 — Immune Watchdog — *applies, with the most metastatic-specific reinterpretation*.** (a) **Immune-evasion selection has already occurred** — a clone that seeded, survived dormancy, and regrew through treatment is selected for escape; antigen-loss/MHC-I-loss variants are more likely enriched → the V4 baseline assumption of restorable surveillance is more fragile, which *raises* the relative value of the **NK missing-self arm** (it targets exactly the MHC-I-low escapees that defeated the T-cell arm). (b) **Lung is an immunologically favorable checkpoint site** vs bone/liver/CNS, and prior WLI may have left a radiation-primed, STING-active pulmonary context (Deng *Immunity* 2014 PMID 25517614 — not CIC-DUX4). (c) **The NK-vs-MHC-I sequencing tension is *sharper* in metastasis** because the metastatic clone is more likely MHC-I-low by selection → an NK-first window before epigenetic MHC-I restoration is *more* defensible here than at primary. **v2 ADR-0006 additions:** the immune-selected clone is also the setting where **ligand-side Nectin blockade (anti-PVR, NTX1088-class)** is most attractive (restores DNAM-1 + lifts TIGIT/CD96/PVRIG on the residual NK arm) — and where the patient's **prior doxorubicin (an ICD inducer)** has *already* deposited danger-signal history into the antitumor-immunity ledger. CIC-DUX4 direct: None.

---

## mRNA Team Findings — Metastatic Relevance
Net finding (no persistent BNT162b2 effect at >2 yr) → **no vaccine-attributable modifier of metastatic biology** to carry forward. Two reframings:
- **Anti-PEG / accelerated blood clearance** (Kozma 2022 PMID 35853896 [VERIFY]; Ishida 2006 PMID 16797763): a future LNP-mRNA therapeutic must reach *disseminated* sites + draining nodes, not a single mass → reduced delivery is *more* consequential systemically. PK flag, not contraindication.
- **Sayin 2014 / Le Gal 2015 antioxidant-metastasis signal** (PMID 24477002 / 25471168) is by construction *metastasis*-specific and is the single most metastasis-relevant cross-cutting safety item: the concern with high-dose liposomal vitamin C is ROS-suppression reducing oxidative clearance of disseminating tumor cells. Mouse models were KRAS/BRAF-driven (different ROS architecture) → transfer unconfirmed, but the setting that makes it matter (residual/disseminating disease) is exactly this patient's.

---

## Metastatic-Specific Forward Hypotheses

**[Forward Hypothesis M1] NK-first immunologic debulking in the post-ifosfamide lymphodepletion window, timed to the selected MHC-I-low metastatic clone, *before* any epigenetic MHC-I restoration.** Because the relapsed lung clone is immune-selected (enriched for MHC-I-low escape variants), the highest-yield immune step in *this metastatic* setting is NK-directed (IL-15 superagonist / anti-PVR / adoptive NK) in the homeostatic-expansion window after ifosfamide lymphodepletion — before EZH2-pathway/HDACi restore the very missing-self signal NK exploits. *Falsifier:* paired metastatic biopsies show the relapse is MHC-I-**normal** (removing the premise), or NK-window deployment yields no ctDNA/infiltration change. *Why untested:* needs paired metastatic biopsies + tight lymphodepletion scheduling; rarity precludes a dedicated trial; runs opposite the prevailing "prime-then-checkpoint" paradigm.

**[Forward Hypothesis M2] The irradiated lung as a defined metastatic-niche target — omega-3/SPM resolution of the post-WLI macrophage field to lower both genotoxic and pro-colonization signaling at the one organ this patient relapses in.** Resolving persistent radiation-induced alveolar/interstitial macrophage activation (EPA/DHA → resolvins/protectins → ALX/FPR2 → ↓NF-κB/NOX2, ↓IL-6/TGF-β) could lower the niche's pro-colonization signaling — converting V2's translocation-prevention omega-3 rationale into a *niche-modification* rationale. *Falsifier:* in a murine WLI + lung-seeding fusion-sarcoma model, EPA/DHA diet does not reduce metastatic colony count or shift macrophage polarization, or an ALX/FPR2 antagonist fails to abolish any effect. *Why untested:* SPM-resolution and metastatic-niche fields have not intersected for irradiated lung.

---

## What I Could Not Establish
1. **Any CIC-rearranged sarcoma metastasis-specific molecular data** — BRD4-addiction, PRC2 dependency, MHC-I, stress-ligand status of metastatic vs primary clones is unpublished; every caveat above is extrapolation.
2. The molecular profile of **this patient's relapsed lung clone** vs primary — not knowable without re-biopsy; clonal evolution through VDC/IE + radiation cannot be assumed neutral.
3. Dietary/supplement penetration into a **post-WLI fibrotic lung lesion** — plausibly reduced, unquantified.
4. Whether the **Sayin/Le Gal** effect transfers to a fusion-driven (non-KRAS/BRAF) sarcoma — plausible, unvalidated.
5. Persistence of any **radiation-primed STING/immune context** in lung >1 yr post-WLI in this patient.
6. Whether single-lesion relapse is **truly oligometastatic biology** (favorable) or the visible part of broader micrometastatic disease — changes the systemic-vs-local balance; unresolvable from the case description.
