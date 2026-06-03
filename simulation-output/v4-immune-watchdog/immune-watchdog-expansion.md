# V4 Immune Watchdog — Expansion: Immunogenic Signaling, NK Surveillance & Danger Recognition

**Origin:** GitHub issue #11 (@Cerimagic) + its two follow-up comments.
**Status:** Incremental expansion of the existing V4 vector — **not a fifth vector** (golden rule §8). Conceptual scope is broadened *within* V4; see ADR-0006.
**Date written:** 2026-06-03. **Not medical advice — research-simulation hypothesis generation only.**

---

## One-line summary

This artifact broadens V4's conceptual space to explicitly cover **innate danger-recognition** (DAMPs, immunogenic cell death, HSP chaperones), the **Nectin–TIGIT–DNAM-1 axis** (with NTX1088 and the failed anti-TIGIT receptor-blockade programs), **NK exhaustion/rescue**, and — at the issue's request — adopts a standing analytical lens that **separates tumor-promoting inflammation from anti-tumor immune activation from treatment-related inflammatory toxicity**. It deliberately **excludes** re-deriving the checkpoint/NK/microbiome/neoantigen content already in `v4-summary.md` and its four sub-agent files; it *points to* and extends them. It is fusion-agnostic throughout except where noted.

## Confidence (whole output)

**Confidence: medium** — the danger-signal and Nectin-axis biology is well-established at the class level and several anchors are live-verified primary literature; but **direct CIC-DUX4 evidence is absent for every mechanism here** (as it is across all of V4), the most clinically advanced TIGIT-receptor program has *failed* its phase-3 readouts, and the inflammation-state distinction is a conceptual/methodological contribution, not a measured result in this disease.

## How this maps to the issue's four questions (direct answers first)

1. **Which mechanisms are most important for restoring immune recognition of CIC-rearranged tumors?**
   In CIC-rearranged sarcoma the rate-limiting lesion is almost certainly **antigen-presentation quality (MHC-I) plus a low mutational/neoantigen load**, not checkpoint ligand density alone — so the highest-leverage levers remain (a) **MHC-I restoration** (epigenetic priming — but note the tazemetostat withdrawal below) feeding the T-cell arm, and (b) **the MHC-I-independent NK arm** (missing-self + stress-ligand engagement), which is *complementary precisely because* it does not need the antigen-presentation machinery the tumor has downregulated. Danger-signaling/ICD is the third, **orthogonal** lever: it does not make a specific antigen, it raises the *adjuvanticity* of whatever antigen is released. See the ranked module table.

2. **Are there underexplored innate pathways deserving consideration alongside classical checkpoint biology?**
   Yes — three that the existing V4 files touch only glancingly: (i) the **DNAM-1 / TIGIT / CD96 / PVRIG (CD112R) "nectin axis"** as an NK *and* T-cell brake that is mechanistically distinct from PD-1; (ii) **NKG2D-ligand (MICA/MICB, ULBP) shedding** as an immune-evasion route with its own drug class (anti-MICA/B, shedding inhibitors); and (iii) **DAMP/ICD adjuvanticity**, including the often-overlooked fact that the patient's own SOC anthracycline (**doxorubicin**) is a *bona fide* ICD inducer.

3. **Could danger signaling and immunogenic cell death provide complementary routes for improving immune surveillance?**
   Mechanistically yes, and they are **complementary rather than alternative**: ICD supplies the "adjuvant" (calreticulin eat-me, ATP find-me, HMGB1/TLR4 danger) that the checkpoint/NK levers presuppose but do not themselves generate. The honest caveat is that **no ICD-potentiation strategy has been tested in CIC-rearranged sarcoma**, and ICD biology is heavily mouse-derived.

4. **How should evidence supporting these pathways be integrated within the framework?**
   Through the **existing three scoring axes** (tier / confidence-transfer / feasibility — ADR-0004), *not* a new score, and through the **two-lane rule**: these mechanisms enter the confirmatory lane only where there is real clinical evidence (mostly *outside* sarcoma, so confidence-axis down-weighted), while their CIC-DUX4-specific application stays in the Forward-Hypotheses lane. The inflammation-state lens (below) is the qualitative discipline that keeps "reduce inflammation" from being mis-scored as "improve anti-tumor immunity."

---

## Module table — mechanisms, tiers, and the three axes

Legend — **Tier** per `sarcoma-contract`. **Conf.** = confidence/transfer-to-CIC-DUX4 (H/M/L, axis 2). **Feas.** = translational feasibility band F1–F5 (axis 3) for clinical/experimental entries. CIC-DUX4 direct evidence is `None` for every row unless stated.

### A. Danger signals / immunogenic cell death (innate adjuvanticity)

| # | Mechanism / entity | Molecular statement | Tier | Conf. | Feas. | Citation (verified this session unless tagged) |
|---|---|---|---|---|---|---|
| A1 | **Calreticulin (CALR) surface exposure** — the "eat-me" ICD signal | ER-stress–driven CALR translocation to the dying-cell surface → CD91 on DCs → phagocytosis + cross-priming; defines whether anthracycline-killed cells are immunogenic | Preclinical-Animal (mouse tumor vaccination) | M | — | Obeid et al., *Nat Med* 2007, **PMID 17187072** |
| A2 | **Doxorubicin as an ICD inducer** (patient's own SOC) | Anthracycline-induced caspase-dependent immunogenic death → protective anti-tumor immunity in immunocompetent mice; CALR/HMGB1/ATP emission | Preclinical-Animal | M | F1 (already in regimen) | Casares et al., *J Exp Med* 2005, **PMID 16365148** |
| A3 | **HMGB1 → TLR4/MyD88** — the "danger" alarmin | HMGB1 released by dying cells signals TLR4 on DCs → efficient antigen processing/cross-presentation; breast-cancer *TLR4* loss-of-function allele → faster relapse after chemo/RT | Preclinical-Animal + human genetic-association | M | — | Apetoh et al., *Nat Med* 2007, **PMID 17704786** |
| A4 | **Extracellular ATP → P2RX7 → NLRP3 inflammasome → IL-1β** — the "find-me" + adjuvant signal | Dying-cell ATP acts on DC P2RX7 → NLRP3/caspase-1 → IL-1β → IL-17/IFN-γ T-cell polarization; chemo fails in *P2rx7−/−*, *Nlrp3−/−*, *Casp1−/−* hosts; human *P2RX7* loss-of-function → faster metastasis | Preclinical-Animal + human genetic-association | M | — | Ghiringhelli et al., *Nat Med* 2009, **PMID 19767732** |
| A5 | **HSP70 / HSP90 as chaperone-DAMPs** | Surface/released HSP70–peptide complexes → CD91/LOX-1/TLR2-4 on APCs → cross-presentation; **membrane Hsp70** marks stressed tumor cells for NK recognition | Preclinical-Cell / Mechanistic | L | — | [no verified PMID this session; mechanism well-described in Multhoff/Calderwood membrane-Hsp70 literature — cite live before asserting a PMID] |
| A6 | **Type-I IFN / cGAS–STING as the ICD "fourth signal"** | Cytosolic dsDNA (post-RT or post-DNA-damage) → cGAS–STING → type-I IFN → DC licensing; this is the molecular bridge from the patient's prior whole-lung irradiation to a primed pulmonary niche | Preclinical-Animal | M | — | overlaps existing `tcell-surveillance.md` (radiation-ICD/STING); STING-RT abscopal: Deng et al., *Immunity* 2014, PMID 25517614 (already cited in `v4-summary.md`) |

### B. The Nectin axis — NK *and* T-cell co-stimulation vs. co-inhibition

| # | Mechanism / entity | Molecular statement | Tier | Conf. | Feas. | Citation |
|---|---|---|---|---|---|---|
| B1 | **DNAM-1 (CD226) activation** | Activating receptor on NK + CD8 T-cells; binds tumor **PVR/CD155** and **Nectin-2/CD112** → cytotoxicity. Tumor PVR can also down-modulate surface DNAM-1 (loses the activating arm) | Mechanistic / Preclinical | M | — | DNAM-1 ligands already noted in `nk-cell-activation.md` line 31 |
| B2 | **TIGIT inhibition** (the brake) | TIGIT on NK/T/Treg binds **PVR/CD155 with higher affinity than DNAM-1** → out-competes the activating receptor → ITIM signaling dampens cytotoxicity; enriched on exhausted TILs | Mechanistic + Clinical-Trial (target validated as druggable, efficacy **negative** — see B4) | M | — | mechanism: standard nectin-axis immunology [cite live for a specific PMID]; clinical: see B4 |
| B3 | **CD96 (TACTILE) and PVRIG/CD112R inhibition** | Additional inhibitory receptors of the same axis: CD96 competes for PVR; **PVRIG binds Nectin-2/CD112**. They provide redundancy that may explain single-node (TIGIT-only) blockade failure | Mechanistic | L | — | [no verified PMID this session; describe mechanism, cite live before asserting] |
| B4 | **Anti-TIGIT receptor blockade — phase-3 FAILURES (the floor, examined)** | Tiragolumab (anti-TIGIT) + atezolizumab **did not improve OS** in PD-L1-high NSCLC (SKYSCRAPER-01, final analysis Nov 2024) and failed in ES-SCLC (SKYSCRAPER-02, 2022). Receptor-level blockade of one node was insufficient | Clinical-Trial (negative) | — | F4 (program largely discontinued for this combo) | Roche SKYSCRAPER-01 release 2024-11-26 (verified this session); SKYSCRAPER-02: *JCO* 2023 |
| B5 | **NTX1088 — anti-PVR (CD155) ligand-side blockade** (mechanistically distinct from B4) | First-in-class mAb against **PVR/CD155**: removes the shared ligand for TIGIT/CD96/PVRIG **and** restores surface DNAM-1 → dual de-repression + co-stimulation in one target. Phase 1 ± pembrolizumab | Clinical-Trial (Phase 1, early) | L | F3 (recruiting Phase 1; not sarcoma-specific) | Nectin Therapeutics / Merck collab; **NCT05378425** (KEYNOTE-E92), verified this session — *status PERISHABLE, re-verify before relying on it* |

### C. NK surveillance, exhaustion, and stress-ligand evasion

| # | Mechanism / entity | Molecular statement | Tier | Conf. | Feas. | Citation |
|---|---|---|---|---|---|---|
| C1 | **MICA/MICB & ULBP shedding** as NKG2D evasion | Tumors proteolytically shed MICA/MICB (ADAM10/17) → soluble ligand engages and down-modulates NKG2D → blunts NK + γδ-T killing. Anti-MICA/B (e.g. shedding-resistant epitope mAbs) and metalloprotease inhibition are countermeasures | Preclinical-Animal / Mechanistic | L | F4 (anti-MICA/B agents early/experimental) | extends `nk-cell-activation.md`; [no verified sarcoma-specific PMID — cite live] |
| C2 | **NK exhaustion / hyporesponsiveness** | Chronic ligand exposure + TGF-β–rich TME → downregulated NKG2D/NKp30, metabolic exhaustion; rescue via IL-15 (see N-803, already `v4-summary.md` C4), TGF-β blockade, or checkpoint (TIGIT/NKG2A) relief | Mechanistic | M | — | overlaps existing N-803 entry; TGF-β arm [cite live] |
| C3 | **NKG2A/HLA-E inhibitory checkpoint** | HLA-E (often *up* when classical MHC-I is *down*) engages NKG2A → inhibits NK + CD8; monalizumab (anti-NKG2A) is the agent class. Relevant because epigenetic MHC-I restoration could paradoxically raise HLA-E too | Clinical-Trial (other tumors) | L | F3 | [no verified PMID this session; cite live] |

> **Sequencing tension carried forward (unchanged from `v4-summary.md` §Cross-Vector Flags):** NK killing wants MHC-I-**low**; T-cell killing wants MHC-I-**high**. Epigenetic MHC-I restoration helps the T arm but can blunt the NK arm — and may co-induce HLA-E (C3), a second reason to run **NK-first → then MHC-I restoration → then T-cell/checkpoint**.

---

## The inflammation-state lens (the issue's central conceptual request)

The contributor's strongest point: *"reducing inflammation is not always biologically equivalent to improving anti-tumor immunity."* The framework should — and from ADR-0006 onward, will — treat these as **three distinct states**, because an intervention helpful for one can be neutral or harmful for another:

| State | Dominant biology | Marker direction | What HELPS it | What an intervention that "reduces inflammation" does |
|---|---|---|---|---|
| **(1) Tumor-promoting inflammation** | NF-κB/STAT3, IL-6, TNF, COX-2/PGE₂, MDSC/M2-TAM recruitment, angiogenesis — an *enabling characteristic* of cancer (Hanahan & Weinberg, *Cell* 2011/2022; Mantovani/Coussens cancer-related-inflammation literature) | chronic, smoldering; ↑CRP, ↑NLR, ↑IL-6 | **Suppressing** it (COX-2/PGE₂, IL-6 axis) can *help* | **Beneficial** — this is the inflammation you want down |
| **(2) Anti-tumor immune activation** | IFN-γ, CXCL9/10/11, cytotoxic CD8/NK infiltration, Th1, DC maturation, productive ICD/DAMP signaling | acute, productive; "hot"/immunoscore-high (Galon immune-contexture concept, *Science* 2006) | **Amplifying** it (ICD, checkpoint relief, IL-15) | **Harmful** — broad anti-inflammatories/antioxidants can *blunt* the response you want |
| **(3) Treatment-related inflammatory toxicity** | irAEs (colitis, pneumonitis, myocarditis), CRS (IL-6/IL-1), chemo/RT mucositis, ifosfamide-related effects | iatrogenic, off-target | **Managing** it (often steroids/tocilizumab) — but immunosuppression here can cost efficacy | **Necessary for safety**, but a confound: it looks like (2) on a CRP panel yet means the opposite for the tumor |

**Why this matters operationally (and ties to existing guardrails):**
- It explains the **antioxidant/anti-inflammatory hazard** the framework already encodes (V2's ATBC/CARET/SELECT and NAC-metastasis cautions; ADR-0005's "direction is not assumed beneficial"). A blanket "lower inflammation" recommendation can move state (1) *and* state (2) the wrong way at once.
- It disciplines marker reading: **CRP/NLR up** is prognostically bad as state (1) but can also reflect a productive state (2) or toxic state (3) — the marker is not self-interpreting. This is the same "prognostic ≠ targetable" caution from ADR-0005, now generalized.
- It makes ICD/DAMP coherent: the goal is to push state **(2)** (productive danger signaling) *without* feeding state (1) (smoldering IL-6/PGE₂) — e.g., favoring ICD-competent SOC scheduling over chronic NF-κB activation.

This lens is **qualitative** and fusion-agnostic. It is recorded as a standing V4 analytical discipline (ADR-0006), not a scored entry.

---

## Standard-of-care interaction flags

- **Doxorubicin (A2) is an ICD inducer** — this is a *reason the existing anthracycline backbone may already be doing immune work*, not a recommendation to alter dosing. Corticosteroids and broad antioxidants given concurrently could theoretically dampen ICD adjuvanticity (state-2 suppression); this is **mechanistic/theoretical**, must not drive any steroid or supplement decision, and belongs to the oncologist.
- **Cyclophosphamide** at certain schedules is immunomodulatory (metronomic low-dose → Treg depletion) — mechanistic only; not a dosing claim.
- **Ifosfamide / etoposide / vincristine** are not classical ICD inducers; no ICD-potentiation claim is made for them.
- No dietary or supplement compound is recommended in this artifact, so the VDC/IE CYP3A4/CYP2C9/P-gp/ROS screens (see `sarcoma-chemo-interactions`) are not triggered here; they remain in force for the dietary entries in `v4-summary.md`.

## Perishable regulatory status (verified live 2026-06-03)

- **Tazemetostat (Tazverik, EZH2i)** — the agent `v4-summary.md` named the "cleanest V3→V4 MHC-I bridge" — was **voluntarily withdrawn from all indications and all markets on 2026-03-09** (Ipsen; secondary hematologic malignancies in the SYMPHONY-1 trial; FDA secondary-primary-malignancy warning). **The EZH2-inhibition *mechanism* of MHC-I priming is unchanged**, but tazemetostat is **no longer an accessible agent**; any MHC-I-priming hypothesis must now route through an alternative EZH2i (e.g., **valemetostat**, in trials — *verify recruitment live*) or a class-I HDACi (entinostat). This supersedes the access (not the mechanism) of `v4-summary.md` rows C1/C2 and the V3→V4 bridge table. Source: Ipsen press release + OncLive/CancerNetwork, accessed 2026-06-03.
- **Anti-TIGIT (tiragolumab)** — SKYSCRAPER-01 OS-negative (2024-11-26) and SKYSCRAPER-02 negative (2022); treat receptor-level TIGIT monoblockade as a **cautionary precedent**, not a recommendation.
- **NTX1088 (anti-PVR)** — Phase 1 NCT05378425, status perishable; re-verify before any reliance.

---

## Forward Hypotheses (CIC-DUX4-specific, not in the literature)

**[Forward Hypothesis 1] NK-first "missing-self + ligand-side de-repression" window in MHC-I-low CIC-DUX4 disease, using PVR-axis blockade instead of (failed) TIGIT-receptor blockade.**
*Hypothesis:* Because CIC-DUX4 cells are plausibly MHC-I-low (NK-susceptible) and the TIGIT-receptor programs failed, the productive innate node is the **ligand**: blocking tumor PVR/CD155 (NTX1088-class) should simultaneously lift TIGIT/CD96/PVRIG inhibition and restore DNAM-1 co-stimulation on NK cells *before* any epigenetic MHC-I restoration is applied — exploiting the MHC-I-low state while it lasts.
*Mechanistic basis:* DNAM-1↔PVR↔TIGIT competition (B1/B2/B5); NK missing-self; the sequencing tension above.
*Test:* CIC-DUX4 PDX or NK-humanized model; arms = anti-PVR alone / IL-15-superagonist alone / both / both → then EZH2i (or HDACi) MHC-I restoration → then anti-PD-1. Endpoints: NK infiltration/cytotoxicity, MHC-I and HLA-E trajectory, tumor volume. *Why untested:* no CIC-DUX4 syngeneic/humanized model; rarity; anti-PVR is itself Phase 1.

**[Forward Hypothesis 2] ICD-adjuvanted anthracycline window — schedule the existing doxorubicin to maximize danger-signal emission, then capture it.**
*Hypothesis:* If doxorubicin already induces ICD (A2), then the *timing* of an immune-capture step (DC-licensing, checkpoint relief, or NK activation) relative to the anthracycline pulse — not a new drug — is the lever. A capture step placed in the post-anthracycline CALR/HMGB1/ATP-emission window should out-perform the same step given out of phase.
*Mechanistic basis:* CALR/HMGB1/ATP kinetics (A1/A3/A4); the cancer-immunity cycle requires antigen + adjuvant + presentation co-occurring.
*Test:* mouse CIC-DUX4 (if/when available) or a fusion-driven sarcoma surrogate; vary the interval between a doxorubicin pulse and an immune-capture step; read DAMP emission, DC maturation, antigen-specific CD8 priming, and whether avoiding concurrent corticosteroid/antioxidant preserves the effect. *Why untested:* ICD scheduling is unstudied in CIC sarcoma; the steroid/antioxidant confound is rarely controlled.

**[Forward Hypothesis 3] HLA-E/NKG2A as the predictable escape valve of epigenetic MHC-I restoration.**
*Hypothesis:* EZH2i/HDACi restore *classical* MHC-I to enable T-cells but may **co-induce HLA-E**, engaging NKG2A and re-suppressing both the NK arm being relied on earlier and the new CD8 arm — so MHC-I restoration should be paired with NKG2A blockade (monalizumab-class), not checkpoint-PD-1 alone.
*Mechanistic basis:* HLA-E is frequently anti-correlated with classical MHC-I loss and is itself a de-repression-sensitive locus (C3); NKG2A is a shared NK/CD8 brake.
*Test:* CIC-DUX4 cell lines ± EZH2i/HDACi → quantify HLA-A/B/C *and* HLA-E by flow; functional NK/CTL killing ± anti-NKG2A. *Why untested:* HLA-E response to epigenetic therapy is uncharacterized in CIC sarcoma.

---

## Atypical-case note (~5% fusion-unconfirmed)

**Every mechanism in this artifact is fusion-agnostic** and therefore applies unchanged to the ~5% clinically/histologically CIC-rearranged but fusion-unconfirmed subgroup: danger-signaling/ICD, the Nectin–TIGIT–DNAM-1 axis, NK stress-ligand biology, NKG2A/HLA-E, and the inflammation-state lens all target host/tumor immune machinery, not the fusion junction. The only V4 items that remain fusion-**dependent** are the junction-specific neoantigen/CAR-T/TCR-T entries already flagged in `v4-summary.md` and `neoantigen-vaccine.md` — none of which this expansion adds to.

## What I could not establish

1. **Whether CIC-DUX4 cells actually expose CALR / release HMGB1/ATP under SOC anthracycline** — ICD competence is tumor-type-specific and unmeasured in this disease. A2 is a strong *prior*, not a CIC-DUX4 result.
2. **PVR/CD155, Nectin-2/CD112, and TIGIT/DNAM-1 expression on CIC-DUX4 tumors and TILs** — no published profiling; the entire Nectin-axis rationale (B1–B5) is extrapolated.
3. **NKG2D-ligand (MICA/MICB, ULBP) surface vs. shed levels on CIC-DUX4 cells** — unmeasured; this is the same gap flagged in `v4-summary.md` (#3) and gates both NK and γδ-T strategies.
4. **HLA-E baseline and its response to EZH2i/HDACi in CIC-DUX4** — the crux of Forward Hypothesis 3; entirely unknown.
5. **Whether any anti-TIGIT-axis agent has activity in *any* sarcoma** — the failed trials were NSCLC/SCLC; sarcoma data are absent, so transfer is doubly uncertain.
6. **Exact PMIDs for several mechanistic anchors** (HSP70 membrane/DAMP biology A5; CD96/PVRIG B3; NKG2A/HLA-E C3; the Galon immune-contexture and Hanahan–Weinberg hallmark references) — the *concepts* are well-established, but I did not live-verify a specific accession this session and have therefore **not** asserted one; verify before quoting a number.
7. **Whether the post-WLI pulmonary STING/IFN priming (A6) persists** at this patient's current timepoint — same open question as `v4-summary.md` (#8).

---

*Grounding (OpenMed NER, `--team v4-lead`; see `immune-watchdog-expansion.grounding.tsv`):* the gene/gene-product set (calreticulin, HMGB1, P2RX7, NLRP3, HSP70/90, STING, cGAS, DNAM-1/CD226, TIGIT, CD96, PVRIG, PVR/CD155, Nectin-2, NKG2D, MICA/MICB, ULBP, NKG2A, HLA-E), the drug set (tiragolumab, tazemetostat, doxorubicin, pembrolizumab), and "CIC-DUX4 sarcoma" (Cancer/Disease) were all recognized. **NTX1088 was not individually recognized** by NER (a novel antibody code, not in the model vocabulary) — its identity (anti-PVR mAb, NCT05378425) rests on the live-verified press/registry sources cited inline, not on NER.

*Reuse note:* this artifact extends, and does not replace, `v4-summary.md`, `nk-cell-activation.md`, `tcell-surveillance.md`, `microbiome-immune.md`, and `neoantigen-vaccine.md`. The baseline run is preserved. **Research-simulation note, not medical advice.**
