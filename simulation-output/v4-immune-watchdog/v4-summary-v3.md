# Vector 4 — Immune Watchdog Summary (Clean-Slate Run v3)

**Summary:** This output covers immune-visibility and immune-clearance approaches for this patient's
CIC-rearranged sarcoma — checkpoint/T-cell biology (PD-1/PD-L1/CTLA-4, Nectin-TIGIT-DNAM-1 axis), NK
missing-self/IL-15-axis approaches, gut microbiome/SCFA modulation of systemic immune tone, and
clinical-track personalized neoantigen vaccines/CAR-T — reconciled across four specialist sub-agents,
the V3 MHC-I-restoration bridge, the mRNA Vaccine Research Team's findings, and the standing V4
expansion (ADR-0006) and host-biology (ADR-0005) layers. It deliberately **excludes** re-deriving V1/V2/
V3 mechanisms (referenced only at hand-off points) and any prescriptive dosing.

**Confidence: medium-low overall, with sharp internal variation.** The NK missing-self framing and the
checkpoint/PD-1 mechanism class are well-established immunology (Established/Clinical-Trial tier in
general oncology); the V3→V4 MHC-I bridge is now anchored to FDA-approved, repurposable agent classes
(HDACi/DNMTi, both F1-accessible). What pulls confidence down across the board: **zero direct CIC-DUX4
data** for nearly every mechanism in this vector (MHC-I status, PD-L1 status, NKG2D/DNAM-1-ligand
expression, HLA-E baseline, TMB, and microbiome composition are all unmeasured in this patient), the
EZH2i route (the prior run's anchor) is now doubly invalidated (mechanistic premise contested +
tazemetostat globally withdrawn 2026-03-09), and the patient's **imminent high-dose ifosfamide** makes
the dominant near-term reality a sequencing/timing question, not an agent-selection one.

---

## PATIENT CONTEXT (carried across all four sub-agents)

Soft-tissue CIC-rearranged sarcoma, dx June 2024, **FUSION-UNCONFIRMED** (~5% atypical subgroup).
Primary biceps femoris right thigh; 12 lung mets at dx. EURO EWING (VDC/IE) ×14 cycles; surgery Jan 2025
(>95% necrotic); radiation to leg + whole-lung (WLI). NED May 2025→May 2026; May 2026 oligometastatic
relapse (single cluster, one lung). Patient **now beginning high-dose ifosfamide** — a profoundly
lymphodepleting event that dominates the near-term immune-state framing for every entry below.

**Self-administered regimen** (assessed across specialists): curcumin+piperine, liposomal vitamin C,
black cumin seed oil, vitamin D3, honey, fresh juice (celery, ginger, carrot, broccoli, apple,
beetroot).

---

## V3→V4 MHC-I BRIDGE — RECONCILED ANCHOR FOR THIS RUN

`simulation-output/v3-hot-patching/v3-summary-v3.md`'s MHC-I Upregulation Candidates section
(read in full) supersedes the prior run's EZH2i-anchored framing. All four V4 specialists independently
reconciled against this ranking:

| Rank | V3 candidate | MHC-I mechanism | Tier | Fusion-dependence | F-band |
|---|---|---|---|---|---|
| 1 | **Class-I HDAC inhibitors** (vorinostat, romidepsin, panobinostat, belinostat) | H3K27ac/H4ac opens APM loci (TAP1/2, PSMB8/9, HLA-A/B/C, B2M); viral-mimicry/type-I-IFN/STAT1 via ERV reactivation | Preclinical-Cell (mechanism, other tumor types) / Clinical-Trial (FDA-approved class, other indications) | Fusion-agnostic | F1 (repurposable, pending oncologist) |
| 2 | **DNMT inhibitors** (azacitidine, decitabine, guadecitabine) | Reverses APM/HLA/TAP promoter hypermethylation; ERV reactivation → cGAS-STING/type-I-IFN → STAT1-driven APM transcription | Clinical-Trial (mechanism class established, other indications) | Fusion-agnostic | F1 (repurposable) |
| 3 | EZH2 inhibitors (tazemetostat class) — **DOWNGRADED** | PRC2/H3K27me3 removal restores APM transcription in PRC2-dependent tumors | Doubly caveated | Fusion-agnostic mechanism, access-closed | **F5** (worldwide withdrawal 2026-03-09) |
| 4 | BET inhibitors (OTX015, BMS-986158, AZD5153) | Variable, context-dependent effect on ISGs/MHC-I/PD-L1; weakest of the four for MHC-I specifically | Preclinical-Cell / Clinical-Trial | Fusion-agnostic, low-confidence direction | F2-F3 |

**Two independently-compounding reasons EZH2i is no longer the lead bridge agent** (live-verified
2026-06-14): (1) Bakaric et al., *Cancers* 2024;16(2):457, PMC10814785 — CIC-DUX4 functions as a
**p300/CBP-driven transcriptional activator**, not primarily PRC2-dependent, undercutting the
EZH2i-specific rationale (does not undercut HDACi/DNMTi, whose MHC-I mechanism runs through
viral-mimicry/interferon biology independent of PRC2 status); (2) Ipsen voluntarily withdrew
tazemetostat (Tazverik) **worldwide, from all indications, on 2026-03-09** following a SYMPHONY-1
secondary-hematologic-malignancy signal (5.7% vs 0% MDS/AML) — now F5/concept-only.

**Net effect propagated to every V4 specialist:** the cleanest "epigenetic priming → V4 effector"
agents are now **class-I HDACi and DNMTi** — both FDA-approved for other indications (F1, repurposable
pending oncologist evaluation), not tazemetostat.

**Red-team flag carried from the checkpoint specialist (load-bearing, unresolved):** the entire bridge
assumes CIC-DUX4's antigen-presentation-machinery (APM) loci are *baseline-repressed* and therefore have
something for HDACi/DNMTi to restore. The same p300/CBP-activator finding that downgraded EZH2i could
mean APM loci are **not** repressed in CIC-DUX4 at all (a ceiling effect, nothing to restore). No study
addresses this directly. If true, this would shift the vector's center of gravity toward the NK/Nectin-
axis arm (which works on the tumor's *current* MHC-I-low state, no priming required) — see Ranked
Candidates below.

---

## RANKED CANDIDATE LIST

| Rank | Candidate | Track | Layer | Mechanism (1 sentence) | Tier | CIC-DUX4 direct? | Fusion-dependence | Cross-vector | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **NK missing-self exploitation** (no new agent — a framing/sequencing priority) | Dietary+Clinical | NK | MHC-I-low CIC-DUX4 cells lose the KIR/NKG2A "self" password, making them paradoxically NK-susceptible if NKG2D/DNAM-1 ligands (MICA/MICB/ULBP, PVR/CD155) are co-expressed | Mechanistic | None direct | Fusion-agnostic | V3 MHC-I bridge (tension), VoI ranking (Sim 6) | `v3/nk-cell-activation.md` |
| 2 | **HDACi/DNMTi MHC-I priming → checkpoint blockade, biomarker-gated sequence** | Clinical | Checkpoint, V3 bridge | HDACi/DNMTi restore APM transcription via viral-mimicry/IFN route; sequenced with anti-PD-1 once MHC-I/APM increase is confirmed on-treatment | Clinical-Trial (component mechanisms) / Theoretical (the specific sequenced+gated design) | None direct | Fusion-agnostic | V3 ranks 1-2; PEMDAC precedent (uveal melanoma) | `v3/tcell-surveillance.md` |
| 3 | **IL-15 / IL-15-superagonist (N-803/Anktiva) timed to post-ifosfamide NK reconstitution** | Clinical | NK | IL-15 drives post-lymphodepletion NK reconstitution (count, NKG2D/DNAM-1 density) without Treg expansion (unlike IL-2) | Established (bladder cancer indication) / Clinical-Trial (solid-tumor/NSCLC program) | None direct | Fusion-agnostic | mRNA-team lymphodepletion framing | `v3/nk-cell-activation.md` |
| 4 | **NTX1088 (anti-PVR/CD155) — dual NK + exhausted-CD8 de-repression** | Clinical | NK + Checkpoint | Removes shared TIGIT/CD96/PVRIG ligand (PVR/CD155) while restoring surface DNAM-1 on T and NK cells | Clinical-Trial (Phase 1, MoA signal reported April 2026) | None direct | Fusion-agnostic | Bridges NK and checkpoint files | `v3/tcell-surveillance.md`, `v3/nk-cell-activation.md` |
| 5 | **Vitamin D3 / zinc deficiency-correction** (dietary, contingent on unmeasured status) | Dietary | NK | VDR/zinc-cofactor signaling supports NK precursor differentiation and cytotoxic-receptor expression | Mechanistic + Dietary-Observational | None direct | Fusion-agnostic | V3 differentiation specialist cross-ref | `v3/nk-cell-activation.md` |
| 6 | **Fermented foods (whole-food, not supplement-probiotic)** | Dietary | Microbiome | Increases gut microbiome alpha-diversity, decreases 19 inflammatory serum markers incl. IL-6 (state-1 reduction) | Clinical-Trial (healthy adults, n=18/arm) | None direct | Fusion-agnostic | — | `v3/microbiome-immune.md` |
| 7 | **Dietary fiber, whole-food/smoothie not juice** | Dietary | Microbiome | High fiber intake associated with improved PFS on ICB in melanoma; juicing strips most insoluble-fiber/SCFA substrate | Clinical-observational (melanoma) | None direct | Fusion-agnostic | — | `v3/microbiome-immune.md` |
| 8 | **Fusion-agnostic personalized neoantigen vaccine** (intismeran autogene / autogene cevumeran platform mechanism, applied to this patient's tumor sequencing) | Clinical | Neoantigen | WES/RNA-seq-discovered somatic neoantigens, independent of CIC-DUX4 junction confirmation | Clinical-Trial (melanoma/pancreatic) / Mechanistic (applied to this tumor) | Low-TMB finding (PMID 27664537) is CIC-DUX4-direct; platform application is None direct | Fusion-agnostic (the only neoantigen-vaccine-class entry that is) | Anti-PEG flag (mRNA team) | `v3/neoantigen-vaccine.md` |
| 9 | **CIC-DUX4 junction-specific neoantigen vaccine / TCR-T** | Clinical | Neoantigen | Junction peptide as tumor-specific MHC-I-restricted neoantigen | Theoretical | None direct | **FUSION-CONFIRMED ONLY** — possibly inapplicable to this patient | Driver-uncertainty model (ADR-0008) | `v3/neoantigen-vaccine.md` |

**Probiotic supplements (commercial, multi-strain): explicitly NOT recommended** — Spencer et al.
2021 (*Science*, PMID 34941392) showed broad commercial probiotic use was associated with *reduced*
ICB benefit in melanoma (human cohort + mouse mechanism), and high-dose ifosfamide-induced neutropenia
adds an infection-risk argument against live-culture supplements during that window. This is a
melanoma-derived signal, not a sarcoma finding, but argues against the "more probiotics = better"
framing generically. (See Cross-Vector Flags.)

---

## DIETARY TRACK

### NK-relevant: vitamin D3 and zinc (`v3/nk-cell-activation.md`)

Both follow the **deficiency-correction-vs-replete-supplementation** framing mandated by the contract:

- **Vitamin D3:** 1,25(OH)₂D₃ signals through VDR on NK cells and precursors, modulating cytotoxic
  receptor expression and IFN-γ production [Mechanistic]; deficiency correlates with reduced circulating
  NK cytotoxic activity [Dietary-Observational]. The large VITAL trial (Manson et al., *NEJM* 2019, PMID
  30415629) found no overall cancer-incidence/mortality benefit from supplementation in a
  non-deficiency-selected population. **This patient's 25(OH)D level is not recorded** — the framework
  cannot currently distinguish "this self-administered vitamin D3 is correcting a real deficiency
  (clear rationale)" from "supplementation in an already-replete person (additional NK benefit thin)."
  Flagged as a value-of-information gap, not assumed beneficial or neutral.
- **Zinc:** zinc-dependent pathways (thymulin, zinc-finger TFs) support lymphoid/NK maturation
  [Mechanistic + Preclinical-Animal]. No zinc supplement is in this patient's documented regimen; dietary
  intake from the juice ingredients is not zinc-dense (zinc-dense foods — oysters, pumpkin seeds, meat —
  are absent from the regimen). Serum zinc unrecorded. **Excess zinc (>~40 mg/day elemental) displaces
  copper, risking copper-deficiency anemia/neuropathy** — the textbook "natural ≠ unlimited"
  counter-example for zinc; not currently relevant since no supplement is being taken, but would be if
  one were added.

**Chemo-interaction screening (`sarcoma-chemo-interactions`, both compounds):** No documented CYP3A4,
P-gp, or ROS-axis interaction with vincristine/doxorubicin/cyclophosphamide/ifosfamide/etoposide at
deficiency-correction doses. Vitamin D metabolism runs through CYP2R1/CYP27B1/CYP24A1, distinct from the
CYP3A4 axis that activates ifosfamide/cyclophosphamide. The only monitoring-relevant note: hypercalcemia
risk at sustained high vitamin D3 intake combined with ifosfamide's nephrotoxicity profile is a
monitoring consideration, not a pharmacologic interaction.

### Microbiome/SCFA axis (`v3/microbiome-immune.md`)

**Mandatory transfer caveat, stated once and applying to this entire subsection:** the
microbiome↔checkpoint-response literature (Routy 2018 PMID 29209380, Gopalakrishnan 2018 PMID 29097493,
Davar 2021 PMID 33542131, Spencer 2021 PMID 34941392) is **entirely melanoma/NSCLC/RCC**. No published
microbiome–CPI association study exists in any sarcoma, including CIC-rearranged sarcoma. CIC-DUX4's
lower TMB/TIL baseline means even the *magnitude* of any transferred effect, if real at all, is unknown.
This sits at Directness rung **P3** (solid-tumor-with-named-mechanism, ADR-0014) — admitted at low
confidence, not excluded.

- **Butyrate** (V3→V4 reused framing): a class I/IIa HDACi at colonic luminal concentrations
  (low-millimolar, PMC6346118), but systemic/portal plasma concentrations are 1-13 µM — 2-3 orders of
  magnitude lower; V3 concluded systemic tumor-site HDAC inhibition is **unestablished**. The
  *gut-immune-axis* claim (Tregs, barrier integrity) does not require tumor-site delivery, so it is not
  defeated by the same gap — but it carries its **own directional ambiguity**: butyrate promotes FOXP3+
  Treg differentiation (Furusawa 2013 PMID 23463760; Arpaia 2013 PMID 24226773) — a **tolerogenic** shift
  — while also strengthening gut-barrier integrity (reduces LPS-driven inflammation). Applying the
  inflammation-state lens: barrier effect → plausibly reduces state-(1) tumor-promoting inflammation;
  Treg effect → plausibly **dampens** state-(2) anti-tumor activation. **No study resolves the net
  balance in a cancer patient.** This output does not resolve it either.
- **Fermented foods** (Wastyk et al., *Cell* 2021, PMID 34256014 — corrects the prior run's incorrect
  PMID): 17-week RCT (n=18/arm, healthy adults) — high-fermented-food arm showed increased microbiome
  alpha-diversity and decreased 19 inflammatory markers including IL-6; high-fiber arm's effect was
  baseline-dependent, not uniformly beneficial. Clinical-Trial tier, **healthy adults, not cancer
  patients**. Whether a microbiome already disrupted by 14 cycles of VDC/IE responds the same way is
  unestablished.
- **Dietary fiber** (Spencer et al. 2021, PMID 34941392 — the single best-verified finding in this
  output): every 5g/day fiber increase ≈ 30% lower progression/death risk on ICB in 128 melanoma
  patients — but **only in patients NOT taking commercial probiotics**; mouse experiments in the same
  paper showed probiotic supplementation impaired anti-tumor immunity and ICB efficacy. This directly
  undercuts "probiotics = good gut health = good for cancer."

### Patient regimen assessment (juice + honey) — `v3/microbiome-immune.md`

**Net assessment: neutral-to-mildly-positive, not harmful, but a missed opportunity.** Juicing strips
most insoluble fiber/prebiotic substrate (inulin, resistant starch, beta-glucan, much pectin) —
exactly the substrate that feeds the SCFA-producing taxa discussed above. The juice still delivers a
diverse polyphenol load (celery apigenin/luteolin, ginger gingerols/shogaols, beetroot betalains) that
reaches the colon and is metabolized by gut microbiota — real, but smaller than whole-food fiber
delivery. **Honey's prebiotic-oligosaccharide content is real in the literature (Saraiva et al. 2022,
PMC9367972) but is a small minority of honey's carbohydrate content at culinary intake — the simple-sugar
load dominates; net effect closer to neutral.** No CYP3A4/P-gp/ROS-axis interaction was found for any
juice/honey/fermented-food component with VDC/IE or ifosfamide at dietary intake. The one timing
consideration: live-culture fermented foods carry a theoretical infection-risk during the neutropenic
window expected from high-dose ifosfamide — a timing consideration, not a pharmacokinetic interaction.

**Beta-glucan/Dectin-1** (oats, barley, mushrooms) is flagged as the one prebiotic-fiber mechanism that
acts on innate immune cells (NK, macrophage) directly via pattern-recognition rather than exclusively
through microbiome diversity — mechanistically the most "fusion-agnostic, immune-direct" lever in this
table — but **the patient's regimen contains no beta-glucan source**.

### PD-L1 modulation by diet (`v3/tcell-surveillance.md`) — honest, not padded

Curcumin (NF-κB→PD-L1, 10-30 µM cell-line), sulforaphane (Nrf2/weak HDACi), and EGCG (DNMT inhibition)
all have **Preclinical-Cell/Mechanistic** PD-L1-modulation claims at concentrations **10-10,000× above
dietary-achievable plasma levels** — the same exposure gap V3 documented for the clinical HDACi/DNMTi
bridge itself. **No patient-level PD-L1 modulation data exist for any tumor type from dietary intake.**
Diet is not a substitute for the clinical-track HDACi/DNMTi agents.

---

## CLINICAL / EXPERIMENTAL TRACK
**(Clinical / Experimental — not naturally achievable; for awareness only.)**

### Checkpoint inhibitors in sarcoma — honest reality check (`v3/tcell-surveillance.md`)

- **SARC028 (NCT02301039)**, pembrolizumab, phase 2: primary endpoint **not met overall**; UPS/DDLPS
  carried the signal. CIC-rearranged sarcoma not enrolled as a distinct cohort — too rare for a
  dedicated arm. Tier: **Clinical-Trial** (Tawbi et al., *Lancet Oncology* 2017;18(11):1493-1501, PMID
  **28988646** — corrected from a transposed-digit error in a prior session).
- **Alliance A091401 (NCT02500797)**, nivolumab ± ipilimumab, phase 2: nivolumab monotherapy 2/38 (5%)
  ORR; nivolumab+ipilimumab 6/38 (16%) ORR — combination met its endpoint, monotherapy "does not warrant
  further study in an unselected sarcoma population" per authors. UPS/DDLPS again carried most signal.
  D'Angelo et al., *Lancet Oncology* 2018;19(3):416-426 (**a prior session's "NEJM 2018, PMID 30501812"
  citation is INCORRECT and retracted here** — the paper is in Lancet Oncology, not NEJM; 2024 expansion
  cohort PMID 39343511 verified live this session).
- **Mandatory honest flag:** checkpoint monotherapy response in sarcoma is modest overall and
  concentrated in high-TMB/complex-karyotype histotypes (UPS, DDLPS) — the **opposite** of CIC-DUX4's
  genomically simple, single-driver, presumed-low-TMB profile. This is a **negative-leaning prior**, not
  a positive one, for CPI monotherapy in this patient — independent of the MHC-I-visibility question.
- **New finding this run — first CIC::DUX4-direct immunotherapy data point:** a March 2025 case report
  (*npj Precision Oncology*, PMID 40128305, PMC11933392 — **[VERIFY]**) describes a CIC::DUX4-confirmed
  sarcoma, immunologically cold at baseline (scarce CD3+/CD8+/FOXP3+, negligible PD-L1/PD-1), converting
  to an actively-infiltrated "exhausted-but-present" phenotype after **nivolumab + relatlimab** (dual
  ICB, anti-PD-1 + anti-LAG-3). Tier: **Clinical-Trial (single case report)**. This is a precedent that
  CIC::DUX4 tumors are **not immunologically inert** — a cold-to-hot transition is achievable by some
  route. This patient is fusion-*unconfirmed*, so this case report is a **disease-class precedent, not a
  directly transferable data point** for this specific patient.

### "Epigenetic priming → checkpoint" combination evidence — what actually exists

- **PEMDAC** (entinostat + pembrolizumab, uveal melanoma, NCT02697630, Johnson et al., *Nat Commun* 2021,
  PMID 34376667) is the closest real mechanism-matched precedent: class-I HDACi to restore
  HLA/antigen-presentation machinery + reduce MDSCs, then anti-PD-1, in a checkpoint-monotherapy-refractory,
  low-TMB tumor type (uveal melanoma) — directionally similar to CIC-DUX4's expected profile. Tier:
  **Clinical-Trial (uveal melanoma, P3 rung)**. **No sarcoma-specific HDACi+CPI combination trial was
  identified.** A prior session's citation ("NCT02890069...sarcoma cohort") is **retracted as
  inaccurate** — that NCT is an unrelated PDR001/LCL161/everolimus/panobinostat trial.
- **DNMTi + checkpoint**: viral-mimicry → cGAS-STING → type-I-IFN → MHC-I rationale explored in multiple
  solid-tumor trials; **no CIC-DUX4 or CIC-rearranged-sarcoma-specific trial identified**. Tier:
  Mechanistic, anchored to Clinical-Trial-tier component mechanisms.
- **What the evidence does NOT establish:** that HDACi/DNMTi priming produces a *measurable* MHC-I
  increase on the actual tumor *before* CPI is given. Most combination trials co-administer rather than
  sequence-and-confirm. The "prime, confirm, then release" design — sequenced and biomarker-gated — is
  **Theoretical**, not an established trial design. (See Forward Hypothesis 1.)

### The Nectin–TIGIT–DNAM-1 axis (`v3/tcell-surveillance.md`, `v3/nk-cell-activation.md`)

- **DNAM-1 (CD226)** is an activating receptor on CD8 T-cells *and* NK cells, engaging PVR/CD155 and
  Nectin-2/CD112. **TIGIT** binds the same ligands with higher affinity, out-competing DNAM-1 and
  delivering inhibitory signal — enriched on exhausted TILs.
- **Cautionary precedent:** anti-TIGIT receptor blockade has **failed at phase 3** — tiragolumab +
  atezolizumab did not improve OS in PD-L1-high NSCLC (SKYSCRAPER-01, final analysis 2024-11-26) and
  failed in extensive-stage SCLC (SKYSCRAPER-02, 2022). Tier: **Clinical-Trial (negative)**. Lesson: be
  skeptical of "just add another checkpoint inhibitor" — CD96 and PVRIG/CD112R provide redundant
  inhibitory backup on the same axis; single-node blockade may be systematically insufficient.
- **NTX1088 (anti-PVR/CD155)** — live-verified 2026-06-14: a first-in-class mAb against the **shared
  ligand** PVR/CD155, removing it for TIGIT/CD96/PVRIG simultaneously while restoring surface DNAM-1 on T
  and NK cells — mechanistically distinct from the failed receptor-level approach. Phase 1
  (NCT05378425, monotherapy + pembrolizumab) confirmed **RECRUITING** (Nov 2024), with **April 2026
  preliminary data reporting the first-ever clinical restoration of DNAM1 (CD226) expression/function on
  peripheral T and NK cells across multiple dose levels**. Tier: **Clinical-Trial (Phase 1, early; MoA
  signal reported, efficacy not yet reported)**. F-band: **F3** (recruiting, not externally accessible).
  **`[VERIFY before relying on this]`** — perishable. Because TIGIT is expressed on exhausted CD8 T-cells
  (not only NK cells), this is **not purely an NK-cell consideration** — a single ligand-side blockade
  could in principle de-repress both arms simultaneously, **if** this tumor expresses PVR/CD155
  (unmeasured). Theoretical for CIC-DUX4.

### IL-15 axis and adoptive NK (`v3/nk-cell-activation.md`)

- **N-803 (nogapendekin alfa inbakicept-pmln, "Anktiva")**: IL-15 superagonist (IL-15N72D:IL-15Rα-Fc).
  **FDA-approved** for BCG-unresponsive non-muscle-invasive bladder cancer (QUILT-3.032, NEJM Evidence)
  — `[VERIFY exact label scope]`. Solid-tumor program: a Phase 3 trial (nogapendekin alfa + tislelizumab
  vs. docetaxel, second-line NSCLC) reported active as of early 2026. **No CIC-DUX4 or sarcoma-specific
  trial identified.** Tier: **Established** (bladder) / **Clinical-Trial** (NSCLC program). Mechanism
  (NK/CD8 expansion without Treg expansion, unlike IL-2) is fusion-agnostic.
- **NK engager bispecifics**: AFM13 (acimtamig, CD30/CD16A) is active only in CD30+ lymphomas — CD30 is
  not a CIC-DUX4-relevant target. GPC2-directed constructs are preclinical, GPC2 expression in CIC-DUX4
  unconfirmed. **No NK engager in active development targets a CIC-DUX4-relevant antigen** — ETV4/ETV5
  (the hallmark CIC-DUX4 transcriptional targets) are intracellular, not surface-accessible.
- **Adoptive NK transfer**: established track record in hematologic malignancies (haploidentical,
  cord-blood, memory-like NKG2C+ subsets), increasingly with IL-15-axis support. **No CIC-DUX4-specific
  data.** Relevance to this patient: lymphodepleting chemotherapy creates the "immunological space"
  (reduced cytokine competition) that is the rationale for lymphodepletion-preconditioning in adoptive
  cell therapy generally (Established in CAR-T/TIL) — the post-ifosfamide NK-reconstitution window is
  mechanistically the most plausible point for any future NK-supportive intervention (Forward Hypothesis
  2 below).

### Neoantigen vaccines and CAR-T (`v3/neoantigen-vaccine.md`) — TAG: Clinical/Experimental, awareness only

- **HEADLINE: this patient's fusion-unconfirmed status makes any CIC-DUX4-junction-specific neoantigen
  vaccine, TCR-T, or pan-variant cocktail POSSIBLY INAPPLICABLE** — the junction nucleotide sequence (the
  design input) has not been identified. This is the dominant fact for this entire sub-section, per the
  mRNA team's Section 5c.
- **Fusion-agnostic track (the only potentially-applicable neoantigen-vaccine pathway for this
  patient):** intismeran autogene (mRNA-4157/V940, Moderna/Merck) and autogene cevumeran (BNT122,
  BioNTech/Genentech) are platforms for discovering/encoding **patient-specific somatic neoantigens from
  WES/RNA-seq**, independent of fusion status. Live-verified status (2026-06-14):
  - **Intismeran autogene**: KEYNOTE-942 5-year follow-up (Jan 2026) showed **49% reduction in
    recurrence/death risk** vs. pembrolizumab alone in resected high-risk melanoma — strongest durability
    data yet. Phase 3 (NCT05933577) ongoing, completion ~2029. **No sarcoma cohort.**
  - **Autogene cevumeran**: mixed picture — pancreatic (IMCODE-003) shows durable T-cell responses in a
    responder subset (Rojas et al., *Nature* 2023 + 3-yr update); colorectal (BNT122-01, NCT04486378)
    **crossed a futility boundary** at first interim analysis (Q3-2025 disclosure, not a confirmed
    negative, trial continues blinded to 2027); bladder (IMCODE-004) reportedly on clinical hold for a
    safety event `[VERIFY directly at clinicaltrials.gov]`. **No sarcoma cohort.**
  - **Net read:** personalized-neoantigen efficacy is **not a settled question even in
    better-characterized indications** — this should temper expectations for a much-lower-TMB tumor like
    CIC-rearranged sarcoma (Italiano et al., PMID 27664537 — CIC-DUX4 sarcomas are low-mutational-burden,
    **CIC-DUX4-direct evidence**), fusion status aside.
- **CAR-T/TCR-T**: no published CIC-DUX4-specific construct exists. The CIC-DUX4 fusion protein is
  **intracellular** (transcription factor) — not a CAR target. A junction-peptide-MHC complex could in
  principle be a TCR-T target, but only if (a) junction confirmed, (b) HLA type known, (c) the peptide is
  MHC-I-presented — which requires the MHC-I restoration this entire vector is built around. Tier:
  **Theoretical**. Fusion tag: **FUSION-CONFIRMED ONLY** for TCR-T; CAR-T generally has no identified
  surface target regardless of fusion status.
- **Junction-variant landscape**: the CIC-DUX4 junction (CIC exon ~20 / DUX4 exon 1) varies at the
  nucleotide level across patients (`docs/02-cic-sarcoma-knowledge.md`). A pan-CIC-DUX4 vaccine would
  need a multi-variant cocktail; the prior run's "3-8 major variants" estimate remains
  **`[VERIFY] — unresolved`**. Per-patient sequencing is the safer design assumption — moot for this
  patient at the current information state, since no junction has been confirmed at all.
- **Manufacturing timeline vs. ifosfamide**: personalized vaccine manufacturing (WES/RNA-seq →
  neoantigen prediction → per-patient synthesis) takes ~6-9 weeks — incompatible with the urgent,
  imminent high-dose ifosfamide course, and ifosfamide's own lymphodepletion would be a poor backdrop
  for vaccine priming regardless. **This is a feasibility/timing reality, not a biology one.**

---

## CROSS-VECTOR FLAGS

1. **The NK-vs-MHC-I-priming sequencing tension is the single most important cross-vector finding in
   this run.** Restoring MHC-I (V3 ranks 1-2, HDACi/DNMTi) helps the T-cell/checkpoint arm but
   simultaneously **removes the NK-activating missing-self signal** by re-arming KIR/NKG2A inhibition.
   `immune-watchdog-expansion.md` Forward Hypothesis 1 already identified the resolution as **NK-first**;
   this run's NK specialist adopts and extends it: NK-directed measures (deficiency-correction,
   IL-15-axis support, PVR-axis de-repression if reachable) should be the **earlier-phase lever**, while
   the tumor is in its native MHC-I-low state, with HDACi/DNMTi-based MHC-I restoration as the
   **later-phase lever** switching the dominant effector arm from NK to T-cell/checkpoint.
2. **The HLA-E/NKG2A escape valve compounds (not just complicates) the NK-first case.** HLA-E is often
   *upregulated* precisely when classical MHC-I is downregulated; epigenetic MHC-I restoration could
   paradoxically co-induce HLA-E, re-suppressing the NK arm via NKG2A. If so, the MHC-I-low window may be
   the **only** window where NK isn't *also* checked by HLA-E/NKG2A — sharpening "do NK things first
   because it's convenient" to "the NK window may close, not just shift."
3. **The Sim 6 VoI ranking independently supports NK-axis primacy**: nectin CD155/CD112 (#1, VoI 0.625)
   and HLA-E (#2, VoI 0.500) are the two highest-value unmeasured biomarkers — both NK-arm variables —
   because DNAM-1 is a shared AND-gate for *both* T-cell and NK non-cytotoxic clearance, with no
   fallback if lost. MHC-I/B2M/TAP integrity ranks only #6 (VoI 0.188), because NK provides a fallback if
   MHC-I/T-cell fails — but nothing provides a fallback if the nectin/DNAM-1 axis is lost. **This is
   documentation of uncertainty / "what would change the route," not a testing mandate.**
4. **mRNA Vaccine Team findings, incorporated per-arm (no single "relevant/not relevant" verdict — it
   varies by sub-mechanism):**
   - T-cell/checkpoint, Nectin axis, NK activation: **no documented persistent effect at this patient's
     current timepoint** (2+ years post-BNT162b2). Kared et al. (PMID 35087044) showed transient NK
     activation-marker increases resolving within ~30 days. The patient's immune landscape is dominated
     by VDC/IE-induced lymphodepletion/reconstitution, post-WLI remodeling, and imminent ifosfamide — not
     the vaccine.
   - Microbiome: **not in the mRNA team's scope at all** — "no relevant finding / not addressed" is the
     accurate statement, distinct from "investigated and found no effect."
   - Neoantigen vaccine: **the anti-PEG antibody flag is the one actionable item** (Kozma et al., *NPJ
     Vaccines* 2022, PMID 35853896, `[VERIFY]`, Confidence: Low) — BNT162b2 can induce anti-PEG IgG/IgM;
     both intismeran autogene and autogene cevumeran use PEGylated LNP-mRNA, the same chemistry class.
     Theoretical ABC-phenomenon mechanism (Ishida 2006, PMID 16797763) could reduce vaccine delivery.
     **Design-level flag only** — if this patient were ever considered for an LNP-mRNA neoantigen
     vaccine trial (fusion-agnostic track, longer horizon), pre-treatment anti-PEG titer would be a
     reasonable PK-stratification covariate to raise for trial design. Not actionable today.
5. **Doxorubicin-as-ICD-inducer (V4 expansion module A2, this patient's own 2024-2025 VDC/IE regimen
   already contained an anthracycline)**: Casares 2005 (PMID 16365148) and Obeid 2007 (PMID 17187072)
   document CALR/HMGB1/ATP-driven immunogenic cell death under anthracycline. Whether this generated any
   tumor-antigen-specific T-cell priming in this patient that survived WLI + 1-year NED + is about to
   face ifosfamide-induced lymphodepletion is **entirely unmeasured** — see Forward Hypothesis 2 (T-cell
   specialist).
6. **Inflammation-state lens (ADR-0006), applied throughout this run**: no component of any specialist's
   regimen assessment was found to clearly and unambiguously promote state-(2) anti-tumor immune
   activation. The strongest "good news" finding (Spencer 2021 fiber/no-probiotic) is itself
   melanoma-CPI-context-dependent and the patient is not currently on CPI. Butyrate's two effects (barrier
   anti-LPS → state-1 reduction; Treg expansion → state-2 dampening) pull in opposite directions and are
   unresolved. **Lowering inflammation ≠ improving anti-tumor immunity** remains the operative caution.
7. **Microbiome specialist's checkpoint-response evidence is explicitly melanoma/NSCLC-derived
   (Routy 2018, Gopalakrishnan 2018, Davar 2021, Spencer 2021) and does not transfer cleanly to sarcoma**
   — categorical absence of any sarcoma microbiome–CPI study, plus CIC-DUX4's lower TMB/TIL baseline
   means even the *magnitude* of any transferred effect is unknown. P3 rung (ADR-0014), low confidence,
   admitted not excluded.
8. **Possible downstream-of-the-bottleneck framing for the microbiome axis**: if CIC-DUX4's primary
   immune-evasion problem is antigen-presentation failure (MHC-I-low) and low neoantigen load (TMB), a
   microbiome shift addresses neither — it could be immunologically inert in this tumor regardless of
   melanoma data, because the rate-limiting step (antigen presentation) is upstream of where the
   microbiome acts (T-cell/NK priming threshold). No study tests microbiome-CPI effects in low-TMB/
   MHC-I-low models specifically. The orchestrator should weigh microbiome candidates **below** the
   MHC-I-bridge and NK candidates, not as a parallel-strength alternative.

---

## FORWARD HYPOTHESES

**[Forward Hypothesis 1] Post-ifosfamide lymphocyte-reconstitution window as the entry point for an
HDACi/DNMTi-anchored, biomarker-gated "epigenetic priming → checkpoint" sequence.**

*Hypothesis:* High-dose ifosfamide produces profound lymphodepletion; the reconstitution window
(roughly weeks 4-12 post-completion, by analogy to other lymphodepleting-chemotherapy contexts) is a
period of homeostatic T-cell proliferation with elevated IL-7/IL-15 signaling. If a class-I HDACi
(vorinostat/romidepsin/panobinostat/belinostat — FDA-approved, F1-repurposable) or DNMTi
(azacitidine/decitabine, also F1) were introduced during/just before this window to upregulate tumor
MHC-I, followed by anti-PD-1 as the reconstituting T-cell compartment expands, the **timing** — not a
novel agent — could be the lever that makes an otherwise-modest CPI prior (SARC028/A091401's
low-TMB-unfavorable signal) more favorable for this patient.

*Mechanistic basis:* IL-7/IL-15-driven homeostatic T-cell proliferation + HDACi/DNMTi-driven MHC-I/APM
re-expression (V3 ranks 1-2, viral-mimicry/type-I-IFN route) + anti-PD-1 release of the (newly visible)
tumor-T-cell interaction.

*What would test it:* A window-of-opportunity phase 1b design — post-high-dose-ifosfamide, Day 28-35, a
short HDACi/DNMTi course with **on-treatment biopsy or ctDNA/RNA readout for MHC-I/APM transcript change
(TAP1/2, HLA-A/B/C, B2M) as a mandatory gate** before proceeding to anti-PD-1. Primary endpoints: MHC-I/
APM induction (gate), T-cell reconstitution kinetics (flow, TCR-repertoire diversity), tumor response at
12 weeks.

*Why not yet tested:* the HDACi/DNMTi-anchored version is new to this run (the prior run anchored to
now-withdrawn tazemetostat); ifosfamide as a deliberate lymphodepleting platform for subsequent
epigenetic-priming-plus-CPI has not been formally tested in sarcoma. **Falsifier (self-falsifying by
design):** if on-treatment biopsy/ctDNA shows no MHC-I/APM induction after the HDACi/DNMTi step, the
priming half has failed and the trial should not proceed to the CPI arm — a "no" answer would also
strengthen the NK/Nectin-axis-first framing (Forward Hypothesis 3).

**[Forward Hypothesis 2] Post-high-dose-ifosfamide NK reconstitution kinetics, gated by IL-15-axis
support, as a determinant of oligometastatic-relapse control.**

*Hypothesis:* Following ifosfamide-induced lymphodepletion, NK cells reconstitute from bone-marrow
progenitors in an IL-15-dependent manner. The *quality* of that reconstitution (absolute NK count,
NKG2D/DNAM-1 receptor density, KIR/NKG2A repertoire) at the nadir-to-recovery window predicts whether the
host can mount NK-mediated surveillance against the residual oligometastatic lung lesion — and
IL-15-superagonist support (N-803-class, Established in bladder cancer, Clinical-Trial in solid tumors)
timed to this window could be tested as a reconstitution-quality booster.

*Mechanistic basis:* IL-15 is the principal driver of post-lymphodepletion NK reconstitution
(hematopoietic-transplant literature); N-803/Anktiva has an existing solid-tumor safety/efficacy
dataset; the oligometastatic, single-lung-cluster presentation is a favorable setting for a
surveillance-dependent (rather than bulk-cytoreduction-dependent) immune mechanism to matter.

*What would test it:* A prospective cohort design (study-design proposal, not patient-specific) —
measure NK absolute count, NKG2D/DNAM-1 expression density, and KIR/NKG2A repertoire at baseline and
days 14/28/42/90 post-high-dose-ifosfamide in oligometastatic sarcoma patients, with a parallel arm
receiving IL-15-superagonist support timed to the reconstitution window vs. observation, radiologic
response of residual lesions as the endpoint, and serial HLA-A,B,C/HLA-E/MICA-MICB/ULBP profiling to test
whether reconstitution quality correlates with control specifically in MHC-I-low lesions.

*Why not yet tested:* no dedicated NK-reconstitution study following high-dose ifosfamide exists in
sarcoma; the IL-15-axis-timed-to-reconstitution framing is novel even in better-studied tumor types.

**[Forward Hypothesis 3] NK-first deficiency-correction window — time vitamin D3/zinc-status assessment
and correction (if indicated) to precede, not follow, MHC-I-restoring epigenetic priming.**

*Hypothesis:* If a documented vitamin D3 or zinc deficiency exists (currently unknown), correcting it
would have its clearest NK-functional rationale **while the tumor remains in its native MHC-I-low
state** — before any HDACi/DNMTi-based MHC-I restoration shifts the tumor toward T-cell visibility and
potentially raises HLA-E/NKG2A inhibition of the NK arm (per Forward Hypothesis 3 of
`immune-watchdog-expansion.md`).

*Mechanistic basis:* NK missing-self logic (this output's Rank-1 candidate); VDR→NK cytotoxic-receptor
signaling; zinc-dependent NK maturation; the NK-first sequencing position (Cross-Vector Flag 1).

*What would test it:* A CIC-DUX4 (or fusion-driven-sarcoma-surrogate) PDX/NK-humanized model with arms =
(a) replete host, no priming; (b) deficient host, no priming; (c) deficient host corrected
before-priming; (d) deficient host corrected after-priming — readouts: NK infiltration/cytotoxicity at
each MHC-I state (serial flow for HLA-A,B,C, HLA-E, MICA/MICB/ULBP, tumor volume).

*Why not yet tested:* requires both a CIC-DUX4 model system (does not exist) and controlled
micronutrient-status manipulation in that model — a combination not attempted in any fusion-sarcoma
context.

**[Forward Hypothesis 4] In-silico CIC-DUX4 junction-variant landscape mapping — pre-emptive, independent
of this patient's own driver resolution.**

*Hypothesis:* Aggregating published CIC-DUX4 breakpoint sequences (e.g., Macedo et al. 2025, 48
molecularly confirmed cases, DOI 10.1111/his.15341, plus other public depositions) and clustering the
resulting junction peptides could convert the unresolved "[VERIFY] — 3-8 major variants" question into an
actual number — informing whether a pan-CIC-DUX4 vaccine cocktail is a 3-variant or 30-variant product,
and what per-patient sequencing buys beyond matching to a known cluster, for the ~95% who ARE
fusion-confirmed.

*Mechanistic basis:* fusion breakpoints in other fusion-driven sarcomas (e.g., EWSR1-FLI1 in Ewing
sarcoma) cluster into a tractable number of recurrent classes despite nucleotide-level variability —
whether CIC-DUX4 shows similar clustering is an empirical question answerable from existing published
sequence data without any new patient.

*What would test it:* A bioinformatic study — aggregate published CIC-DUX4 breakpoint coordinates, align/
cluster junction peptide sequences, report the number of clusters needed to cover 80%/95% of cases and
the predicted HLA-binding promiscuity of each cluster's peptides across common HLA alleles.

*Why not yet tested:* CIC-DUX4's rarity (<200 reported cases worldwide) means breakpoint depositions are
scattered across case reports rather than centralized; Macedo et al. 2025 instead pursued an IHC-based
detection shortcut for diagnosis that sidesteps the sequence-variability problem entirely.

---

## ATYPICAL-CASE NOTES (~5% fusion-unconfirmed, this patient)

**FUSION-AGNOSTIC — fully applicable to this patient regardless of driver-resolution status:**
- NK missing-self/KIR/NKG2D-ligand biology (Rank 1) — triggered by the general MHC-I-low + stress-ligand
  phenotype, not by any specific fusion protein.
- All checkpoint-inhibitor mechanisms (PD-1/PD-L1/CTLA-4) — target host immune-checkpoint machinery.
- HDACi/DNMTi-mediated MHC-I/APM restoration (V3 ranks 1-2) — acts on host chromatin/methylome,
  independent of which driver (D1-D5, ADR-0008) is present.
- The Nectin-TIGIT-DNAM-1 axis (TIGIT, DNAM-1, PVR/CD155, NTX1088) — host receptor-ligand biology.
- IL-15/IL-15-superagonist pipeline, NK engagers, adoptive NK transfer — host cytokine-receptor biology,
  no tumor antigen required.
- Vitamin D3/zinc deficiency-correction — host-side VDR/zinc-cofactor biology.
- The entire microbiome/SCFA/fermented-food/fiber axis — acts on host immune machinery (Tregs, DCs,
  barrier, systemic cytokine milieu), independent of fusion partner or confirmation status. This is one
  of the layers where the atypical-case caveat is **fully relieved**, not merely "still applies."
- The fusion-agnostic personalized neoantigen vaccine track (somatic WES/RNA-seq discovery) and the
  anti-PEG antibody flag (about the LNP delivery vehicle, not the payload).
- The doxorubicin-as-ICD-inducer framing (Forward Hypothesis 2's basis) — depends on how this patient's
  tumor cells die under anthracycline, not on the fusion junction sequence per se.
- The inflammation-state lens — a host-biology interpretive framework, fully fusion-agnostic.

**FUSION-CONFIRMED ONLY — possibly inapplicable to this patient without confirmatory fusion
identification:**
- CIC-DUX4 junction-specific neoantigen vaccine (any platform, any payload format).
- CIC-DUX4 junction-peptide-specific TCR-T.
- Any "pan-CIC-DUX4" vaccine product, regardless of variant-cluster count.
- The npj Precision Oncology dual-ICB case report (PMID 40128305) was in a fusion-**confirmed** patient —
  relevant to this patient only as a disease-class precedent, not a transferable data point.

**Net assessment:** the large majority of this vector — including its top-ranked candidate (NK
missing-self) — remains fully applicable to this patient's fusion-unconfirmed status. The only entries
that lose applicability are the junction-specific neoantigen-vaccine/TCR-T constructs, which were already
the lowest-ranked, most speculative entries in this vector.

---

## WHAT I COULD NOT ESTABLISH

1. **CIC-DUX4-specific MHC-I (HLA-A/B/C, B2M, TAP1/2) and PD-L1 expression status** — the entire "double
   shield" framing (MHC-I-low + PD-L1-high) underlying the checkpoint arm is mechanistic extrapolation,
   not measured in this disease.
2. **CIC-DUX4 NKG2D/DNAM-1 stress-ligand expression (MICA/MICB, ULBPs, PVR/CD155, Nectin-2/CD112)** — the
   single largest gap gating the NK-first hypothesis (Rank 1). If CIC-DUX4 cells are "doubly cold"
   (MHC-I-low AND stress-ligand-low), the NK-first argument collapses to "NK has no purchase here," and
   the danger-signaling/ICD axis (V4 expansion module A) becomes the primary route, not a complementary
   one.
3. **Whether HDACi/DNMTi actually raise MHC-I on CIC-DUX4 cells specifically** — real in
   glioma/liver/lymphoma/breast contexts; untested in CIC-DUX4. Compounded by the open question of whether
   APM loci are baseline-repressed in CIC-DUX4 at all (red-team flag, V3→V4 bridge section above).
4. **CIC-DUX4 tumor mutational burden for this patient** — the "low-TMB → poor CPI-monotherapy prior"
   argument is itself an extrapolation from the translocation-driven-sarcoma class (PMID 27664537 is
   CIC-DUX4-direct for the class, not this tumor).
5. **HLA-E baseline in CIC-DUX4 and its response to MHC-I-restoring intervention** — central to whether
   the MHC-I-low window for NK-first strategies is a true window (closes only when MHC-I is restored) or
   narrower (HLA-E already high, NK arm already NKG2A-checked regardless of timing).
6. **This patient's vitamin D3 and zinc status (25(OH)D, serum zinc)** — neither recorded. The difference
   between "self-administered vitamin D3 corrects a real deficiency" and "supplementation in an
   already-replete person" cannot be resolved without these values.
7. **This patient's current NK/T-cell compartment status** (absolute counts, receptor densities, KIR/
   NKG2A repertoire) following VDC/IE ×14, surgery, and WLI, and how high-dose ifosfamide will further
   perturb it — the #5-VoI item (NK functional reserve, 0.250), directly relevant to Forward Hypothesis 2.
8. **This patient's actual current microbiome composition** — no stool data; whether 14 cycles of VDC/IE
   (with near-certain antibiotic exposure during neutropenic episodes, a mechanistic expectation not a
   documented fact) has left the microbiome depleted, partially recovered, or recovered is unknown.
9. **Whether post-WLI cGAS-STING/IFN priming persists in this patient's lung at the current (>1 year
   post-WLI) timepoint** — acute radiation-ICD/STING activation is documented; persistence at this
   timepoint is unknown.
10. **Whether any ICD priming occurred in this patient under 2024-2025 doxorubicin exposure** — Forward
    Hypothesis 2 (T-cell specialist's, retrospective TCR-repertoire analysis of archived blood) proposes a
    test; no data exist either way.
11. **An exact PMID for the Alliance A091401 2018 Lancet Oncology paper** — cite by journal/year/volume/
    NCT until a PMID is live-verified.
12. **NEO-PV-01's current independent development status, definitive CIC-DUX4 junction-variant count,
    this patient's HLA type, and WES/RNA-seq yield from the >95%-necrotic Jan 2025 resection specimen** —
    all `[VERIFY]`/unresolved per the neoantigen specialist.

### Red-team synthesis across all four specialists (one consolidated pass)

- **Load-bearing assumption (vector-wide):** that CIC-DUX4 cells display the "double-shield" phenotype
  (MHC-I-low + PD-L1-high) AND co-express NK-activating stress ligands (NKG2D/DNAM-1 ligands). Both halves
  are unmeasured. If the MHC-I-low half is wrong (APM loci not actually repressed — the p300/CBP ceiling-
  effect concern), the entire bridge has nothing to restore. If the stress-ligand half is wrong ("doubly
  cold"), the NK-first Rank-1 candidate has no purchase.
- **Disconfirmation:** the strongest evidence against the NK-first framing is the general tumor-immunology
  observation that many MHC-I-low tumors are *also* poorly NK-infiltrated in practice — MHC-I loss does
  not guarantee NK-ligand co-expression; "doubly cold" tumors are a recognized failure mode (not
  CIC-DUX4-specific, no single PMID).
- **Alternative outside V1-V4:** if CIC-DUX4 is "doubly cold," the higher-leverage lever shifts to the
  danger-signaling/ICD axis (V4 expansion module A) — *inducing* stress-ligand expression and DAMP
  release (e.g., via the patient's own doxorubicin) rather than relying on a pre-existing missing-self
  signal. This does not require a new vector — it is already inside V4 — but it would become primary
  rather than complementary.
- **Flip test:** Forward Hypothesis 1's on-treatment biomarker gate is specifically designed to catch a
  wrong MHC-I-restoration assumption (self-falsifying). The NK-first framing (Rank 1, Forward Hypothesis
  3) does **not** have an equivalent built-in gate for the stress-ligand assumption — this is a genuine
  asymmetry the orchestrator should note: the checkpoint arm's leading hypothesis is self-falsifying by
  design, the NK arm's is not (yet).
- **Steer audit:** the brief asked the NK specialist to build around "arguably the strongest single
  mechanistic lever in this whole vector." The specialist complied but explicitly tagged the framing as
  Mechanistic/inferred rather than upgrading it to Preclinical on the strength of the framing alone — the
  steer reframed the search, it did not supply an evidence tier. This lead concurs with that discipline.

---

## BIBLIOGRAPHY (consolidated, new/corrected citations this run)

- Tawbi H et al., *Lancet Oncology* 2017;18(11):1493-1501, **PMID 28988646** (SARC028; corrects
  transposed-digit error from a prior session).
- D'Angelo SP et al., *Lancet Oncology* 2018;19(3):416-426 (Alliance A091401; corrects prior "NEJM 2018,
  PMID 30501812" — wrong journal, retracted). 2024 expansion: PMID 39343511.
- Johnson DB et al., *Nat Commun* 2021, **PMID 34376667** (PEMDAC, entinostat+pembrolizumab, uveal
  melanoma).
- Bakaric et al., *Cancers* 2024;16(2):457, **PMC10814785**, DOI 10.3390/cancers16020457 (CIC-DUX4
  p300/CBP-activator finding, downgrades EZH2i premise).
- Casares N et al., *J Exp Med* 2005, **PMID 16365148**; Obeid M et al., *Nat Med* 2007, **PMID
  17187072** (doxorubicin ICD).
- Ljunggren & Kärre, "missing self" hypothesis (foundational NK immunology, no single PMID).
- Manson JE et al., *NEJM* 2019, **PMID 30415629** (VITAL trial, vitamin D3).
- Furusawa Y et al., *Nature* 2013, **PMID 23463760**; Arpaia N et al., *Nature* 2013, **PMID 24226773**
  (butyrate→Treg via HDAC inhibition at Foxp3 locus).
- Trompette A et al., *Nat Med* 2014, **PMID 25240432** (propionate, gut-lung axis).
- Routy B et al., *Science* 2018, **PMID 29209380** (NSCLC/RCC/urothelial, microbiome-CPI).
- Gopalakrishnan V et al., *Science* 2018, **PMID 29097493** (melanoma, microbiome diversity-CPI).
- Davar D et al., *Science* 2021, **PMID 33542131** (melanoma FMT; corrects prior-run citation
  ambiguity).
- Spencer CN et al., *Science* 2021, **PMID 34941392** (fiber-good/probiotic-bad, melanoma+mouse; corrects
  prior-run incorrect PMID 33579778).
- Wastyk HC et al., *Cell* 2021, **PMID 34256014** (fermented foods; corrects prior-run incorrect PMID
  35839772).
- Saraiva A et al., *Front Nutr* 2022, **PMC9367972** (honey prebiotic oligosaccharides).
- Italiano A et al., **PMID 27664537** (CIC-DUX4 low-TMB finding, CIC-DUX4-direct).
- Kozma GT et al., *NPJ Vaccines* 2022, **PMID 35853896** `[VERIFY]` (anti-PEG antibodies post-BNT162b2).
- Ishida T et al., *J Controlled Release* 2006, **PMID 16797763** (ABC phenomenon, PEGylated
  nanoparticles).
- Kared H et al., **PMID 35087044** (transient NK activation post-BNT162b2, resolves ~30 days).
- A March 2025 *npj Precision Oncology* case report, **PMID 40128305**, PMC11933392 `[VERIFY]`
  (CIC::DUX4-confirmed sarcoma, cold-to-hot conversion under nivolumab+relatlimab — first CIC::DUX4-direct
  immunotherapy data point).
- Macedo et al. 2025, DOI 10.1111/his.15341 (48 molecularly confirmed CIC-DUX4 cases, IHC-based
  detection).
- NTX1088, NCT05378425 (Phase 1, anti-PVR/CD155, recruiting Nov 2024, April 2026 MoA data) `[VERIFY]`.
- Tiragolumab, SKYSCRAPER-01 (final analysis 2024-11-26) and SKYSCRAPER-02 — anti-TIGIT phase-3 failures.
- N-803/Anktiva (nogapendekin alfa inbakicept-pmln) — QUILT-3.032, bladder cancer `[VERIFY label scope]`;
  NSCLC Phase 3 (tislelizumab combination) `[VERIFY]`.
- Intismeran autogene (mRNA-4157/V940) — KEYNOTE-942 5-yr follow-up (Jan 2026), Phase 3 NCT05933577.
- Autogene cevumeran (BNT122) — pancreatic IMCODE-003; colorectal BNT122-01/NCT04486378 (futility
  boundary crossed, Q3-2025) `[VERIFY]`; bladder IMCODE-004 (hold, `[VERIFY]`).
- Tazemetostat (Tazverik) — worldwide withdrawal 2026-03-09 (Ipsen, SYMPHONY-1 secondary-malignancy
  signal) — F5/concept-only.

---

*Research-simulation output, not medical advice. No dosing, start/stop, or treatment recommendations are
made or implied.*
