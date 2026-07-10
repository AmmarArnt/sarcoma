# Findings Ranking — Master Register of Simulation & Analysis Results

> **One place to see every notable finding in this repository, scored on the framework's three orthogonal
> axes.** This is a *transparency and navigation aid*, not a validated instrument and **not medical advice**.
> Ranking reflects research-simulation judgment; every entry links to the artifact that owns the detail and
> the honest caveats.
>
> **Maintenance:** this file is a **standing deliverable** (ADR-0009). When a new sim, team output, or
> analysis produces a result that deserves to be compared against the others, **add a row here** in the
> same commit/PR that adds the artifact. See "Maintenance rule" at the bottom. Last updated: **2026-06-25**
> (evidence refresh `evidence-refresh-2026-06.md` **full-text-verified** + Sim 9 condensate/LLPS **executed**;
> rows for the p300/CBP multi-vector unification, DUX4-STAT1/ISG antagonism, dual-ICB case, MCL1 cardiotox
> flag, and the condensate forward hypothesis appended/updated with verified PMIDs. **One snippet-sourced
> WEE1/adavosertib claim was retracted on verification** (not in the Nat Commun MCL1 paper). Baselines
> v1/v2/v3 preserved.)
> **2026-07-10:** added `post-chemo-maintenance-strategy.md` (MRD/dormancy/consolidation lens on the four
> vectors + the apricot-seed/amygdalin AVOID row, Cochrane/FDA/EFSA-verified).

## How to read the three axes
- **Evidence tier** (what *kind* of evidence): `Established` › `Clinical-Trial` › `Preclinical-Animal` ›
  `Preclinical-Cell` › `Mechanistic` › `Dietary-Observational` › `Theoretical` (`sarcoma-contract`).
- **Confidence** (how much to believe it transfers to CIC-DUX4 *in vivo*): High / Medium / Low, from
  Directness (is it *in* CIC-DUX4?), Achievability (is the exposure reachable?), Reproducibility
  (≥2 concordant sources?) — `docs/08`.
- **Feasibility** (real-world access *for this patient*): **F1** Accessible-now › **F2** Via trial/
  named-patient › **F3** In development, no route here › **F4** Discontinued/withdrawn/on-hold › **F5**
  Concept-only (`translational-feasibility-layer.md` / ADR-0003). **Perishable — re-verify before any
  external use.** Diagnostics/strategy/safety items use F-bands where an "access" reading makes sense.

> **Bias note:** rank order is a judgment call and the two most recent sims (7, 8) were authored in the
> same session that created this file — they are deliberately *not* placed above the real-data findings on
> evidence strength. Promise ≠ proof.

---

## Top picks by criterion (the honest summary)

| If you care about… | The most promising finding | Why |
|---|---|---|
| **Most immediately consequential for this patient today** | **CYP3A4 interaction screen** (piperine/thymoquinone × imminent ifosfamide) | Safety of the *current* regimen; actionable now; no new drug. |
| **Highest-leverage *next action*** | **Resolve the driver first** (Sim 8 EVSI + protocol V3-FH3) | Two independent methods agree; a cheap test (DUX4 IHC) unlocks the whole contingent option set. |
| **Best-evidenced / most corrective** | **EZH2 is *not* a survival dependency** (Sim 2, real DepMap CRISPR) | Real data overturning an assumption → reposition EZH2i as MHC-I priming, not cytotoxic. |
| **Most convergent therapeutic target** | **WEE1 + ifosfamide** (Sims 2+3) / **CDK4** / **IGF1R** | Multiple orthogonal methods; WEE1 intersects the chemo backbone the patient is on. |
| **Most promising *novel* target (fusion-confirmed)** | **MCL1 dependency** ("re-arm the DUX4 death program") | Verified dependency (Nat Commun 2025); but driver-contingent (Sim 8) — hold for the unconfirmed patient. |
| **Most important conceptual reframe** | **MHC-I restoration gap / NK-vs-MHC-I sequencing tension** (Sims 4+5) | Ordering of immune interventions changes outcomes; the V3→V4 bridge. |

---

## Master register (grouped by role, then by promise)

### A. Best-evidenced therapeutic-target findings (real public data, convergent)
| Finding | Source | Evidence tier | Confidence | Feasibility | Note |
|---|---|---|---|---|---|
| **EZH2 is not a survival dependency → reposition tazemetostat as MHC-I priming, not cytotoxic** | Sim 2 (+Sim 1, Sim 3); protocol #2 | Preclinical-Cell (real DepMap CRISPR) | **High** (3 convergent methods) | **F4 (US)** tazemetostat withdrawn 2026-03-09; other EZH2i F3 `[re-verify]` | Highest-confidence corrective result in the repo. |
| **WEE1 + ifosfamide is the only combination that robustly collapses viability** | Sims 2+3; `forward-simulation/WEE1-ifosfamide-oncologist-brief.md` | Preclinical-Cell (CRISPR + dynamical) | **Medium-High** | F3 (WEE1i in trials; adavosertib halted, azenosertib ongoing `[re-verify]`); ifosfamide F1 | Intersects the chemo backbone the patient is already on. |
| **CDK4 (not CDK6) is the selective cell-cycle dependency** | Sims 1+2; Sim 8 (driver-robust) | Preclinical-Cell | **High** (convergent) | **F1** (CDK4/6i approved, breast) | Pair to prevent CCNE1 bypass; cytostatic. |
| **IGF1R axis is a real, fusion-sarcoma-enriched dependency** | Sim 1 + Sim 2 + Kitra-SRS | Preclinical-Cell | **Medium-High** (3 lines) | F3/F4 (most IGF1R programs discontinued in Ewing) `[re-verify]` | Combine, don't solo; biomarker-selected subset. |
| **p300/CBP is the CIC-DUX4-specific super-enhancer *writer* (reversible)** | Epigenetic brief; Sim 7; Bakaric 2024 (PMID 38275898) | Preclinical-Animal/Cell (CIC-DUX4-direct) | **Medium-High** | F3 (p300i clinical-stage early) | Restores MHC-I → V3→V4 bridge; "deep but drainable" attractor. |
| **p300/CBP is a single node hitting THREE vectors** — drives transactivation (V1/V3), *stabilises* the fusion protein, **and suppresses MHC-I** (V4 priming) | `evidence-refresh-2026-06.md` §B; **Mol Cancer 2025;24(1):299 PMID 41299516 / PMC12659477** ✅; Oncogenesis 2021 PMID 34642317/PMC8511258 ✅; Cancers 2024 PMID 38275898 ✅ (all verified 2026-06-25) | Preclinical-Cell/Animal (CIC-DUX4-direct) | **Medium-High** (3 concordant papers, abstract-verified) | F3 — inobrodib/CCS1477 `NCT04068597` **RECRUITING**/`NCT03568656` **COMPLETED**, TT125-802 `NCT06403436` **ACTIVE-NOT-RECRUITING` (all 2026-06-25); no CIC arm; broad-essential → window risk | **Reframes the MHC-I bridge from EZH2i (now F4-US) to p300/CBPi.** The most actionable refresh delta. **Promotion candidate for protocol-v4.** |

### B. Strategic / decision / diagnostic findings
| Finding | Source | Evidence tier | Confidence | Feasibility | Note |
|---|---|---|---|---|---|
| **Resolve the driver first (fusion-unconfirmed): long-read WGS+RNA-seq > DUX4 IHC > methylation array** | Sim 8; protocol V3-FH3 | Mechanistic (decision model); diagnostics Established | **Medium-High** (two independent methods agree) | DUX4 IHC **F1**; methylation **F1/F2**; long-read **F2** | Highest-leverage next action *for this patient*; unlocks the contingent option set. |
| **Throttle/cell-cycle/immune vectors are robust regardless of the unknown driver** (BETi top-robust 96.6% of priors) | Sim 8 | Mechanistic (decision model) | **Medium** | composite F1–F4 | What's safe to pursue before the driver is known. |
| **Nectin CD155/CD112 is the highest-value *missing* biomarker** (not MHC-I; NK fallback covers antigen loss) | Sim 6; `biomarker-voi-stratification.md` | Mechanistic (decision model) | **Medium** | measurement **F1** (IHC/flow) | Tells you what to *measure*; HLA-E + NK-fitness select the immune route. |
| **VoI depends on tissue source + timepoint, not just the marker** (archived-FFPE baseline vs fresh-relapse vs the *change*; cheap diagnosis/baseline reads are FFPE-front-loaded, immune markers want the *current* read) | `biomarker-voi-provenance-extension.md` (issue #7 follow-up; ADR-0011) | Theoretical/Mechanistic (methodology refinement) | **Medium** | composite (P1 archived IHC/methylation **F1**; long-read/fresh **F2**; ctDNA monitoring needs resolved junction) | Refines Sim 6: separates information value from acquisition burden; magnitudes illustrative (no new numeric model). |
| **"Discontinued/withdrawn" ≠ biological invalidation** — attrition-reason annotation (R0 never-built / R1 target-invalidated / R2 trial-fail / R3 subgroup-dilution / R4 regulatory / R5 commercial); **only R1 (+ enriched R2) carries negative biology**. **None** of the catalog's closed-access agents closed for R1 in a CIC context. | `feasibility-attrition-reason-extension.md` (issue #9 follow-up; ADR-0013) | Theoretical/Mechanistic (methodology refinement) | **Medium-High** | annotation on F-axis (no band change) | Refines ADR-0003: separates *why access closed* from *whether mechanism works*; keeps R3/R4-commercial/R5 closures in the forward lane. |
| **Regorafenib CIC cohort = results-pending, not negative** (REGOBONE Cohort E / NCT02389244 `ACTIVE_NOT_RECRUITING`, primary completion 2024-10-25, no results posted; SARC024/NCT02048371 has an n=1 CIC-DUX4 partial response) | `feasibility-attrition-reason-extension.md` §5 (issue #9 follow-up) | Clinical-Trial (registered; Cohort-E results unpublished) | **Medium** | **F2/F3** (trial closed to enrolment; multikinase anti-angiogenic, off-driver) | Not deprioritized for efficacy — results-pending + mechanism not driver-directed; verified 2026-06-13. |
| **Rarity lowers the rung, never excludes** — graded biological-proximity ladder for the confidence Directness sub-axis (P0 CIC-DUX4 → P1 fusion round-cell family → P2 sarcoma → P3 solid-tumour-with-named-mechanism → P4 pathway-only); only a missing **mechanistic bridge** excludes, and the discount never prunes the forward lane | `docs/10-evidence-transferability-hierarchy.md` (issue #10 follow-up; ADR-0014) | Theoretical/Mechanistic (methodology refinement) | **Medium** | refines the confidence axis (no F-band change) | Refines ADR-0004: replaces coarse 3-level Directness; under fusion-uncertainty P1 is the robust anchor (P0 discounted by the driver posterior, ADR-0008). |
| **Build recipe: transformation = AND of 6 steps; MCL1 buffer non-substitutable; order matters** | Sim 7; `tumorigenesis-build-recipe.md` | Theoretical/Mechanistic (logic model) | **Low-Medium** | N/A (conceptual) | Structures forward hypotheses; reverse-engineers the construction; GIGO. |
| **"What to learn next" = diagnostic-action (test-level) information gain**: rank each *test* by its value profile (driver EVSI, Sim 8 + immune-route VoI, Sim 6 — kept separate) ÷ acquisition burden; **sequence** archived-P1 bundle first → fresh-P2 for the residual delta → liquid-P3 monitoring; imaging is an unmodeled staging-axis gap | `diagnostic-information-gain-layer.md` (issue #31; ADR-0015) | Theoretical/Mechanistic (decision-analytic composition) | **Medium** | composite (archived IHC/methylation **F1**; long-read/fresh **F2**; imaging **F1**) | Lifts Sim 6/8 to the *action* level + adds constraint-aware sequencing; no blended EIG score, no new numbers; quantitative Sim 9 proposed not executed. |
| **Selected relapse clone ≠ archived primary → fresh P2 relapse tissue decisively beats P1 archived for the *current* immune phenotype** (the MHC-I-low-NK-exposed vs. doubly-cold fork); paired primary-vs-relapse immune phenotyping is the v3 highest-value immune-learning step | `metastatic-disease-considerations-v3.md` (run v3); `protocol-v3.md` FH-2 | Mechanistic / Theoretical (immunoediting; no CIC-DUX4 metastatic-biology data) | **Low-Medium** (clone-divergence-contingent — tumour was metastatic-from-dx, so relapse may be pre-existing-clone outgrowth) | fresh **P2/F2** | Refines the VoI/diagnostic layers for the metastatic setting; NK-first immune lever most strengthened, but its "doubly cold?" assumption lacks a self-falsifying gate (asymmetry vs the checkpoint-arm biomarker gate). |

### C. Immune-program findings (mechanistic reframes)
| Finding | Source | Evidence tier | Confidence | Feasibility | Note |
|---|---|---|---|---|---|
| **MHC-I restoration gap + NK-vs-MHC-I sequencing tension** (suggested order: NK-first → epigenetic priming → checkpoint) | Sims 4+5; protocol #3-4 | Mechanistic | **Medium** | composite (NK F2/F3; checkpoint F1) | Epigenetic MHC-I restoration helps T-cells but hurts NK missing-self — don't paper over. |
| **NK missing-self arm: the metastatic/relapsed clone is *more* likely MHC-I-low** | Sim 4; protocol #3 | Mechanistic / Clinical-Trial | **Medium** | NK transfer F2/F3; IL-15 (N-803) F1(US) `[re-verify]` | Turns the immune-evasion state into an NK vulnerability. |
| **MCL1 dependency = "re-arm the DUX4 death program"** | Sim 7 driver-engineering brief; **two independent Nat Commun 2025 papers — PMID 40841513/PMC12370961 (MCL1 = direct CIC::DUX4 transcriptional target, xenograft growth inhibition, recurrent ARID1A) + PMID 40841360/PMC12371069 (SRCS tumoroid biobank, CIC::DUX4-selective MCL1i sensitivity)** ✅ both verified 2026-06-25 | Preclinical-Cell/Animal (independently replicated) | **Medium-High** (2 independent tumoroid papers) | Most promising *novel* target — but **driver-contingent** (Sim 8): hold for the unconfirmed patient. |
| **Oncolytic virus as "artificial danger-signal generator" (M4 deep-dive)** — one positive sarcoma signal (T-VEC+pembro phase-2 ORR 30%, NCT03069378) **but** nearest data (Ewing/round-cell) are *low-susceptibility* and CIC-DUX4 data are nil | `oncolytic-virotherapy-danger-signal-layer.md` (issue #11 follow-up; ADR-0019) | Clinical-Trial (sarcoma, non-CIC) → **Theoretical** for CIC-DUX4 | **Low** (P2 sarcoma; Ewing-family resists OV; permissiveness untested) | T-VEC **F2** if a lesion is injectable; systemic OVs **F3**; **RP1 FDA-rejected twice** `[re-verify]` | Fusion-agnostic (good for the ~5%); deep/visceral anatomy is the access limiter; gating experiment = CIC-DUX4 tropism screen. Modality moves feasibility, not tier (ADR-0018). |
| **DUX4 binds STAT1 and broadly inhibits interferon-stimulated genes (ISGs)** — a 2nd, MHC-I-independent immune-evasion arm; suppresses IFN-γ-induction of MHC-I via C-terminal (L)LxxL(L) motifs | `evidence-refresh-2026-06.md` §C; **eLife 2023;12:e82057 PMID 37092726** ✅ (peer-reviewed; upgraded from bioRxiv, verified 2026-06-25) | Preclinical-Cell (Mechanistic, peer-reviewed) | **Medium** | N/A (mechanism) | Explains the IFN-cold phenotype *beyond* MHC-I + is the mechanistic source of the IFN-γ-MHC-I block; predicts IFN-axis therapies are blunted at source. Fusion-relevant (DUX4 moiety). |
| **Documented CIC::DUX4 response to dual ICB (anti-PD-1 + anti-LAG-3; nivolumab+relatlimab)** with post-treatment CD8 influx + PD-1/LAG-3 exhaustion | `evidence-refresh-2026-06.md` §C; **npj Precis Oncol 2025;9(1):85 PMID 40128305** ✅ (verified 2026-06-25, MSKCC) | Clinical (single case) | **Low-Medium** | checkpoint **F1**; LAG-3 doublet (nivo+rela) **F1-US** `[re-verify]` | Updates "modest *monotherapy*" → a **doublet incl. LAG-3** signal; supports priming-then-checkpoint sequencing (Sims 4/5). |

### D. Safety / current-regimen / contextual findings
| Finding | Source | Evidence tier | Confidence | Feasibility | Note |
|---|---|---|---|---|---|
| **CYP3A4 interaction screen: piperine + thymoquinone × ifosfamide (CYP3A4-activated prodrug)** | protocol #5 | Mechanistic / Preclinical (PK) | **Medium-High** | **F1** (actionable today) | The single highest-priority *actionable* item — about what he already takes. |
| **Dietary concentration mismatch; broccoli *juicing* destroys myrosinase → near-zero sulforaphane** | protocol #6 | Preclinical-Cell | **High** | **F1** | Most dietary mechanisms operate 10–500× above achievable plasma levels. |
| **Omega-3 EPA/DHA is the best cross-vector dietary compound — and it's absent from the regimen** | protocol #7 | Dietary-Observational + Mechanistic | **Medium** | **F1** | Lowest chemo-interaction risk; addresses post-WLI lung inflammation. |
| **Antioxidant-vs-ROS-chemo & antioxidant-vs-metastasis conflicts are genuine and unresolved** | protocol #9; antioxidant brief | Preclinical-Animal | **Medium** | **F1** (caution item) | High-dose antioxidants during ROS-chemo / with residual disease → caution. |
| **Apricot seeds / amygdalin ("laetrile" / "vitamin B17") = AVOID — no anti-cancer efficacy + cyanide-toxicity risk, amplified by this patient's high-dose vitamin C and active ifosfamide** | `post-chemo-maintenance-strategy.md` §6; **Cochrane CD005476.pub4 (Milazzo & Horneber 2015) ✅**, FDA amygdalin warning ✅, EFSA 2016 opinion ✅ (all verified 2026-07-10); Moertel NEJM 1982 `[VERIFY 7033783]`; amygdalin+vitamin-C cyanide case report `[VERIFY]` | **Theoretical** (efficacy; negative Cochrane review) | **Low / negative** | N/A (risk–benefit negative) | Clearest AVOID in the catalog, with a *named* case-specific interaction (vitamin C ↑ cyanide release). Fusion-agnostic — atypical-case flag does not soften it. |
| **mRNA COVID-19 vaccination is a null finding for this patient's current biology** | protocol #8; `mrna-vaccine-research/` | Clinical-observational | **Medium** | N/A | Carry-forward: anti-PEG could blunt a *future* LNP-mRNA cancer vaccine. |
| **V2 (compiler-protection) is the least applicable vector to the current disease** | protocol #10 | Mechanistic | **Medium** | N/A | The relapsed lesion already carries the driver. |
| **MCL1's cardiotoxicity stacks on this patient's prior anthracycline (doxorubicin)** — class-wide cardiac signal (ABBV-467 troponin in 4/8 pts; AZD5991 cardiac-arrest AE-death; BRD-810 = next-gen optimised-clearance) | `evidence-refresh-2026-06.md` §D; **ABBV-467 PMID 37880389 ✅, AZD5991 PMID 39167622/PMC11528199 ✅, BRD-810 PMID 39179926 ✅** (verified 2026-06-25) | Clinical (class safety) | **Medium** | **F3–F4 cardio-gated** for THIS patient `[re-verify]` | Patient-conditioned down-weight the generic MCL1 row misses; an oncologist owns any cardiac-risk judgement. |
| **[Forward] CIC-DUX4 may nucleate a p300/CBP-dependent transcriptional condensate via the junction-invariant DUX4 C-term IDR — *heterotypic*, not prion-like** | Sim 9 (`09-condensate-llps/`); FH-9.1 (executed 2026-06-25) | **Theoretical** (no DUX4/CIC-DUX4 LLPS study exists) | **Low** (forward lane; not scored) | N/A — falsifier = p300/CBPi (A-485/inobrodib) condensate-dissolution test | Novel + fusion-agnostic (covers the ~5%) + anchored to an already-druggable node. **Sim 9 now executed:** 3 predictor families (localcider + metapredict + PLAAC) converge — DUX4 C-term is a disordered **acidic activation domain, NOT a FET-type prion-like LCD** (PLAAC PRDscore 0 vs EWSR1 77.6 / FUS 113.7). Refutes the naive EWSR1-analogy homotypic model; **redirects the mechanism onto p300/CBP coactivator-condensate partitioning** — same node as the §B refresh delta. |

---

## Maintenance rule

**When to add/update a row** — whenever a new artifact produces a result that is worth comparing against the
others: a new `sims/NN-*/RESULTS.md`, a new team/sub-agent output, a new layer in `simulation-output/`, or a
material update to an existing finding (e.g. a feasibility band changing, like the tazemetostat F1→F4 move).

**How** (keep it lightweight, in the *same* PR that introduces the artifact):
1. Add one row to the right group (A real-data targets / B strategic-decision-diagnostic / C immune /
   D safety-context) — create a new group only if none fits.
2. Fill all three axes (evidence tier · confidence · feasibility) using the scales above; write `N/A`
   where an axis genuinely doesn't apply (e.g. feasibility for a pure conceptual model). Tag perishable
   regulatory/trial facts `[re-verify]` with no invented status (golden rule #1).
3. Link the source artifact; one-line note with the honest caveat.
4. If the new result changes the **Top picks by criterion** table, update it and bump "Last updated".
5. Do **not** promote a logic/decision-model finding above a real-data finding on evidence strength;
   promise ≠ proof (keep the bias note honest).

This rule is recorded in `CLAUDE.md` (§0 reuse list + §4 sim conventions) and
`docs/adr/0009-findings-ranking-register.md`.

*Research simulation / hypothesis generation only. Not medical advice. Rankings are a navigation aid, not
a validated instrument; every claim's real caveats live in the linked artifact.*
