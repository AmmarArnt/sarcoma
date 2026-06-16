# Clay-Colloid Analogy → Forward-Hypothesis Layer (patient-anchored)

> **What this is.** A reconciled exploration that takes an analogy — *raw, unfired pottery clay as a
> colloidal system* — and asks whether the molecular **principles** of clay (charge-buffering, reversible
> self-assembly, narrow stability windows, history-dependence, and a covalent "firing" step) generate
> **mechanistically defensible forward hypotheses** for how a CIC-rearranged sarcoma cell is built and how it
> might be reverse-engineered. Four such hypotheses (FH-Clay-1…4) were derived, then a focused four-specialist
> team mapped each to concrete **effectors across four achievement routes — biological / pharmacological /
> chemical / natural** — grounded in the run-**v3** artifacts and anchored to the simulation's patient case.
>
> **What this is NOT.** Not a fifth attack vector (golden rule #8). Not a new biological axis. Not a treatment
> plan, not medical advice, no dosing, no start/stop instructions. The analogy is a *hypothesis generator*; it
> never supplies an evidence tier and never prunes the forward lane. Every biology claim carries a tier; every
> regulatory/trial fact is dated or `[VERIFY]` (perishable). **There is zero CIC-DUX4-specific evidence for any
> effector below** — the value is the structure and the honest grounding, not the count.
>
> **Provenance.** Derived from the conceptual thread in `tumorigenesis-reverse-engineering/` (the "build
> recipe," ADR-0007) and reconciled against `protocol-v3.md`, `metastatic-disease-considerations-v3.md`,
> `host-biology-modifier-layer.md`, `driver-uncertainty-specialist.md`, and the diagnostic/VoI layers. Team run
> 2026-06-16. **Cross-link, don't duplicate:** the vectors/layers own the detail; this file only adds the
> analogy-derived framing + the effector mapping.

---

## 0. The unfired-clay principle (the one move)

Raw clay's behavior is **not** governed by its most permanent feature. A clay platelet carries a fixed
negative charge baked into the lattice by *isomorphous substitution* (a wrong-valence atom in the crystal) —
un-removable without destroying the sheet. Yet the material's whole macroscopic behavior (swell vs tighten,
disperse vs flocculate, flow vs hold a form) is set by the **swappable counter-ions** balancing that charge.
Swap Na⁺ for Ca²⁺ and the *same defective lattice* changes behavior completely. **The defect never moves; the
counter-ions do.**

**Read onto the tumor:** the CIC-DUX4 fusion is the *fixed lattice defect* (and in this fusion-unconfirmed
patient, you cannot even confirm it). Trying to pry it out (degrade the fusion, junction ASOs) is fragile and
fusion-specific. But the build recipe's strongest real finding is that the malignant **behavior** is set by an
*exchangeable maintenance layer* — the MCL1 buffer, the p300/CBP super-enhancer writing, the open-chromatin
environment — a *"deep but drainable attractor"* that collapses when the writer stops (p300i restores MHC-I;
Bakaric 2024, PMID 38275898). **That is cation exchange.** The clay model relocates the target from the
immovable driver to the exchangeable counter-ion layer — which is exactly the intervention class the v3 data
already favors (MCL1, p300/CBP, differentiation), and which is mostly **fusion-agnostic** (good for the ~5%).

The Qur'anic framing the user raised — *man made from clay, but not fired* — has a precise molecular echo:
the build recipe found **no demonstrated covalent point-of-no-return** ("firing") in CIC-DUX4. The state is
maintained, not vitrified. The one possible exception is **telomere maintenance** (the kiln question →
FH-Clay-4).

---

## 1. The four clay hypotheses (restated)

| ID | Clay principle | Molecular goal | Fusion dependence | Maps to |
|---|---|---|---|---|
| **FH-Clay-1** | Atterberg plasticity window has a **wet limit**: past the *liquid limit* the form collapses | "Flood past the liquid limit" — drive chromatin/transcription **past** its plasticity ceiling (max de-repress the embryonic/ERV/dsRNA program) so the cell undergoes ICD/apoptosis rather than transforms | **Two arms:** ERV/viral-mimicry flood = **fusion-agnostic**; DUX4-domain "re-arm" (MCL1) = **fusion-contingent** | build-recipe FH-A; protocol-v3 FH-3 (agnostic arm) & FH-4 (contingent arm) |
| **FH-Clay-2** | DLVO **valence switch**: Na⁺→dispersed sol, Ca²⁺→flocculated gel, same platelets | A biological valence/adhesion switch flips cells between **cohesive** and **dispersed/invasive** states — a metastasis lever (integrins/cadherins, LOX crosslinking, FAK-Src-YAP) | **Fusion-agnostic** | metastatic-considerations-v3; Sayin-2014 conflict |
| **FH-Clay-3** | Amphoteric **edge charge flips with pH**; acid sets the rigid "house-of-cards" gel | Warburg acidity (pHe ≈ 6.5–6.9) is a **set-point** stabilizing the aggressive/immunosuppressive/chemoresistant state; reverse the proton gradient to destabilize it | **Fusion-agnostic** | host-biology metabolic layer |
| **FH-Clay-4** | Irreversibility requires **firing** (covalent dehydroxylation); below it, re-slakable | "Find the kiln" — **telomere maintenance** is the only candidate irreversible commitment; resolve **TERT vs ALT** (mutually-exclusive effector worlds) | Diagnostic = **fusion-agnostic**; DUX4-driven-TERT sub-hypothesis = contingent | build-recipe Step 6 / FH-C |

---

## 2. Reconciled cross-cutting findings (the part worth keeping)

Four specialists worked independently; the convergences are the signal.

1. **Leverage relocation (the headline).** All four hypotheses point the same way as the v3 data: act on the
   **exchangeable maintenance layer**, not the immovable driver. The clay analogy supplies a *physical reason*
   why the catalog's strongest hits (MCL1, p300/CBP) and the differentiation premise should work — they are the
   counter-ions, and the state is drainable because nothing was fired.

2. **Two independent red-teams converged on "direction beats potency."** For an **actively-seeding,
   oligometastatic, pre-ifosfamide** patient, the *naïve* reading of two clay hypotheses is dangerous and the
   specialists flipped them:
   - **FH-Clay-2:** the "disperse the gel" pole is the **pro-metastatic** direction. The desirable pole here is
     the opposite — **reinforce cohesion / suppress invasion-EMT**. And the "add crosslinker to make it cohesive"
     instinct is also wrong: LOX-driven matrix stiffening is *itself* pro-metastatic (it activates YAP/FAK and
     builds the lung pre-metastatic niche — this patient's relapse organ, post-WLI fibrotic). The right move is
     **lowering** stiffness-driven mechanosignalling **and** preserving cadherin cohesion. This sits beside the
     existing **Sayin-2014 antioxidant→metastasis** flag: in an active-seeding window, wrong-direction
     interventions accelerate disease.
   - **FH-Clay-3:** systemic alkalinization collides head-on with the patient's most fragile system — high-dose
     ifosfamide causes a **Fanconi-type renal tubular acidosis** with bicarbonate/Mg/PO₄/K wasting. *Every*
     systemic pH-axis effector (CA-IX sulfonamides, amiloride, oral bicarbonate, metformin) perturbs the exact
     acid-base homeostasis ifosfamide is injuring. The legitimate biology is **tumor-local proton-transport
     targets**, not systemic alkalinization.

3. **Fusion-agnostic vs fusion-contingent split (decisive for this patient).** Most clay routes are
   fusion-agnostic — they read host/microenvironment biology downstream of or parallel to the fusion, so they
   apply to the ~5% atypical subgroup. The **only** fusion-contingent route is the **DUX4-domain "re-arm" (MCL1)**
   arm of FH-Clay-1, which stays **HOLD** until the driver is resolved (driver-uncertainty model: MCL1i scores 0
   for D2–D5).

4. **Diagnostic-first dominates FH-Clay-4 (and echoes v3 FH-1).** "Is there a kiln?" is an *information*
   question answerable cheaply on **archived P1 tissue** (ATRX/DAXX IHC + telomere-FISH + TERT-promoter seq),
   fusion-agnostically, before committing to any effector. The effector worlds (telomerase-inhibitor for TERT⁺;
   ATR-inhibitor for ALT⁺) are **mutually exclusive** — a wrong-arm bet is inert.

5. **Timing: almost nothing is "now."** The only things actionable *today* are **information** (the diagnostics)
   and the **safety screen of the self-regimen** (the convergent piperine/curcumin/thymoquinone × ifosfamide
   CYP3A4 signal already in v3). Every therapeutic effector here is **post-ifosfamide / future-line**: the
   strongest ones (HDACi/DNMTi flood, imetelstat, ATRi) all stack **myelosuppression** on the imminent chemo,
   and the immune payoff of the "flood" needs a reconstituting — not aplastic — lymphocyte compartment (the
   post-ifosfamide IL-7/IL-15 window).

---

## 3. Effector tables (condensed from the four specialist briefs)

Tiers per `sarcoma-contract`; transferability rung (ADR-0014) noted where ranking turns on transferred
evidence. **All entries are `Theoretical` for CIC-DUX4 specifically** unless a CIC-DUX4-direct citation is
given. F-bands perishable — re-verify live.

### FH-Clay-1 — "Flood past the liquid limit" (ICD via over-saturating the embryonic/ERV/dsRNA program)

| Effector | Route | Mechanism | Tier | Fusion-agnostic? | F-band | Ifosfamide/VDC-IE | Falsifier |
|---|---|---|---|---|---|---|---|
| **Class-I HDAC inhibitors** (vorinostat, romidepsin, entinostat) | Pharma | H3/H4 acetylation de-represses ERV/LTR → cytoplasmic dsRNA → MDA5/RIG-I/MAVS → type-I IFN ("viral mimicry"); also opens APM → MHC-I↑ | Clinical-Trial (mechanism, other tumors; ERV-IFN class effect, P3) | **Yes** | F1 (US repurposable; EU differs `[VERIFY]`) | Additive myelosuppression; vorinostat/romidepsin are CYP3A4 substrates → branch-point flag `[VERIFY direction]` | No ERV/dsRNA-sensor/APM transcript induction in a CIC-DUX4 model |
| **DNMT inhibitors** (azacitidine, decitabine, guadecitabine) | Pharma | Demethylate ERV promoters → dsRNA → MDA5/cGAS-STING → IFN (Roulois 2015 PMID 26317466; Chiappinelli 2015 PMID 26343579 — cancer-broadly) | Established (MDS/AML) / Preclinical (immune-priming use) | **Yes** | F1 (approved MDS/AML) | Myelosuppression additive; weak CYP actor | Same — no ERV/IFN induction |
| **MCL1 inhibitors / BH3-mimetics** (S63845 tool; S64315/MIK665) | Pharma | Remove the anti-apoptotic buffer the DUX4 transactivation domain forces ON → resident DUX4 death program executes (PMID 40841513/40841360 — reconcile) | Preclinical-Cell + Animal (**highest-tier CIC-DUX4-direct**; P0) | **NO — contingent (D1 only)** | F2/F3; cardiac-tox caution | Additive apoptotic/marrow stress | Removing MCL1 in an established line does not increase death |
| **STING agonist / poly(I:C)/BO-112 / oncolytic virus** | Pharma/Bio | Supply the "artificial flood" — direct PAMP (dsRNA→TLR3/MDA5) + DAMP (lysis) danger signal | Clinical-Trial *in sarcoma broadly* (T-VEC+pembro, NCT03069378) → **Theoretical** for CIC-DUX4 | **Yes** | F3–F4 (deep/visceral anatomy; Ewing/round-cell low OV susceptibility; ADR-0019) | Live agent in neutropenic window = timing hazard | CIC-DUX4 tropism screen shows no productive infection/lysis |
| **Ascorbate as TET/DNMT cofactor** | Chemical | Pharmacologic IV → TET-mediated 5hmC → ERV demethylation (Cimmino 2017 PMID 28825709, AML) | Preclinical-Cell / Mechanistic | **Yes** | F1 oral / F2 IV — **but needs IV pharmacologic range, opposite of oral/liposomal** | **TRAP:** oral/liposomal sits in the antioxidant (chemo-blunting + Sayin metastasis) range, not the pro-oxidant TET range. Do **not** treat as a flood tool here | No 5hmC/ERV induction at achievable plasma level |
| **Sulforaphane / EGCG** | Natural | Weak HDAC/DNMT nudge | Preclinical-Cell | **Yes** | F1 (food) | **Juicing destroys myrosinase** → near-zero sulforaphane; EGCG hepatotox ≥~800 mg/d `[VERIFY]` + CYP3A4/P-gp | Concentration mismatch (100–1000× below cell-line active) defeats the mechanism |

### FH-Clay-2 — "Valence switch" (desirable pole here = anti-invasion / pro-cohesion, NOT dispersion)

| Effector | Route | Mechanism | Tier | F-band / attrition (R0–R5) | Ifosfamide/VDC-IE | Falsifier |
|---|---|---|---|---|---|---|
| **FAK inhibitors** (defactinib) | Pharma | Block stiffness→FAK→Src→YAP mechanotransduction; gates stemness/immune-evasion | Clinical-Trial (P2–P3) | F2–F3 / no negative-biology attrition | CYP3A4 substrate/modulator → branch-point flag `[VERIFY]` | No suppression of YAP-target output/invasion in CIC-DUX4 cells |
| **Dasatinib** (Src) | Pharma | ↓FAK-Src outside-in adhesion/invadopodia | Clinical-Trial (P2; modest in unselected sarcoma) | F1–F2 / R2 (modest in all-comers, not invalidated) | **CYP3A4 substrate+inhibitor; P-gp/BCRP — genuine interaction flag** | Src-independent migration in CIC-DUX4 |
| **YAP/TAZ–TEAD inhibitors** (VT3989, IK-930) | Pharma | Block terminal mechanotransduction node | Clinical-Trial (early; P3–P4) | F3 / R0-to-pending | Unscreened CYP liabilities `[VERIFY]` | CIC-DUX4 cells not YAP/TAZ-dependent |
| **LOX/LOXL inhibition** (BAPN tool; **simtuzumab — FAILED**) | Bio/Chem | ↓collagen crosslinking → ↓stiffness-driven mechanosignalling/niche | Preclinical (BAPN); Clinical-Trial-failed (simtuzumab) | BAPN F5/R0 (no negative biology); **simtuzumab F4/R2(+R5)** — failed IPF + multiple cancers, **not R1** (LOXL2 biology stands) | mAb: none; BAPN not a clinical agent | LOX not elevated in the lung niche / no stiffness-invasion link in CIC-DUX4 |
| **Integrin antagonist** (**cilengitide — FAILED**) | Pharma | Block RGD-integrin–ECM engagement | Clinical-Trial-failed | **F4 / R2 (+R3-risk)** — CENTRIC ph3 missed OS in GBM (Stupp 2014 PMID 25304325); **not R1**, never tested in CIC | Peptide; renal-clearance overlap w/ nephrotoxic ifosfamide (theoretical) | αvβ3/αvβ5 low/absent on CIC-DUX4 cells |
| **Omega-3 EPA/DHA** | Natural | Lipid-raft/RAS-cluster + pro-resolving (RvD1, Yatomi 2015 PMID 26660549) | Mechanistic / Dietary-Obs (P4) | F1 | Antiplatelet at high dose (surgery-relevant); "natural≠anti-metastatic" | No adhesion/invasion change at achievable plasma |

> **Direction note (load-bearing):** the analogy's "dispersed sol" is the *adverse* state for this patient.
> Pursue the **anti-invasion / cohesion-preserving** pole only. **Clone-divergence counterweight:** the tumor
> was metastatic-from-diagnosis (12 lung mets), so the relapse may be outgrowth of a pre-existing disseminated
> clone — this axis more plausibly restrains an established clone's colonizing behavior than prevents a fresh
> dispersion event. Natural options on this axis are thin/concentration-mismatched (EGCG/curcumin/quercetin/
> resveratrol carry CYP3A4+P-gp baggage and are **not** clean valence levers).

### FH-Clay-3 — "Acidity as the set-point" (legitimate target biology; systemic alkalinization is wrong here)

| Effector | Route | Mechanism | Tier | F-band | Ifosfamide/VDC-IE (renal/acid-base!) | Falsifier |
|---|---|---|---|---|---|---|
| **CA-IX inhibitor** (SLC-0111) | Pharma | Block CA-IX → raise pHe/lower pHi in hypoxic/stem compartment | Clinical-Trial (ph Ib; P3) `[VERIFY NCT03450018]` | F3–F4 | Sulfonamide → **metabolic acidosis + electrolyte/stone risk additive to ifosfamide Fanconi acidosis** | pHe normalization doesn't reduce clonogenicity/stemness or improve drug/immune access in CIC-DUX4 |
| **PPI repurposing** (esomeprazole, high-dose; V-ATPase/lysosomal pH; Fais/Spugnini) | Pharma | Raise lysosomal/endosomal pH → reduce ion-trapping of weak-base chemo (vincristine, doxorubicin) | Preclinical + weak human signals (osteosarcoma pilot `[VERIFY PMID]`) | F2–F3 (drug available; oncology use off-label) | **Hypomagnesemia additive to ifosfamide Mg wasting**; CYP2C19/3A4 low-magnitude | No tumor/lysosomal pH rise or weak-base-chemo retention gain (concentration-mismatch risk) |
| **MCT1 inhibitor** (AZD3965) | Pharma | Block lactate/H⁺ co-export | Clinical-Trial (ph I; P3) `[VERIFY NCT01791595]` | F4 (retinal/cardiac DLT) | Cardiac DLT compounds **doxorubicin cardiotox** vigilance | Inert if CIC-DUX4 is MCT4-high |
| **Oral bicarbonate** (systemic buffer; Robey 2009 PMID 19276390) | Chem / "natural-ish" | Buffer interstitial pHe | Preclinical-Animal (mouse; no human efficacy) | F3 nominal, **safety-bounded** | **Dominant constraint:** Na/base load on a bicarbonate-wasting tubule → alkalosis/hypokalemia/Na overload; overlaps clinician acid-base management. **Clinician-only.** | Buffering to mouse-model pHe doesn't destabilize the state (likely falsified on *achievability* first) |
| **DCA / metformin** | Pharma/metabolic | Lower lactate/acid production upstream | Preclinical + small/negative human | F4 (DCA) / F2 drug, F4–F5 efficacy (metformin) | **DCA neuropathy additive to vincristine**; **metformin lactic-acidosis risk rises with ifosfamide nephrotoxicity** | AMPK activation doesn't lower (or raises) intratumoral acid |

> **Pseudoscience guard (named explicitly):** "alkaline diet / lemon water / baking soda cures cancer" is
> false — blood pH is tightly regulated and **urine pH ≠ tumor pHe**; the patient's honey/sweet-juice intake
> delivers a glycemic load that, if anything, *feeds* the glycolysis producing the acidity (directionally
> against FH-Clay-3). What survives is the **target biology** (CA-IX, MCT1/4, NHE1, V-ATPase are bona fide
> oncology targets; tumor acidity genuinely suppresses CD8/NK and drives chemoresistance). The honest home for
> FH-Clay-3 is a **CIC-DUX4 PDX pHe-clamp study**, not a patient on cumulative ifosfamide.

### FH-Clay-4 — "Find the kiln" (diagnostic-first; mutually-exclusive effector worlds)

**Diagnostic (run first — fusion-agnostic, mostly archived-P1):**

| Test | Resolves | Tier | Provenance | Value |
|---|---|---|---|---|
| **ATRX/DAXX IHC** | ALT surrogate (loss → ALT prior) | Established (IHC) | **P1** | Cheapest first pass; retained ≠ ALT-excluded |
| **Telomere-FISH (+ APB IF)** | ALT yes/no (ultrabright foci) | Established | **P1** | **Highest single-test value** — forks the effector tree |
| **TERT-promoter sequencing** | Mutational TERT (expected *negative*; Koelsche 2014 PMID 24726063) | Established | **P1** | High NPV — a negative leaves *non-mutational-TERT vs ALT* |
| **C-circle assay / TRAP / TERT mRNA** | Confirm ALT / confirm telomerase ON | Established / Mechanistic | **P2 preferred** | Residual delta on fresh relapse tissue (also a TΔ primary-vs-relapse question) |

**Effectors (conditional on the diagnostic):**

| Effector | Route | Context | Tier | F-band | Ifosfamide/VDC-IE | Falsifier |
|---|---|---|---|---|---|---|
| **Imetelstat (Rytelo)** | Pharma (oligo) | hTR template antagonist — **TERT⁺ only; inert in ALT** | Established *for MDS*; Theoretical for CIC-DUX4 | F2–F3 (FDA-approved 2024-06-06 lower-risk MDS; off-label here) `[VERIFY]` | **Myelosuppression stacks on ifosfamide/VDC-IE**; slow (telomere-shortening) — poor match to rapid relapse | Tumor is ALT⁺ / no telomere shortening under exposure |
| **ATR inhibitors** (ceralasertib, berzosertib) | Pharma (synthetic-lethal) | **ALT⁺ only** — ALT cells are ATR-dependent (Flynn 2015 PMID 25593184) | Preclinical-Cell (ALT-SL) / Clinical-Trial (class) | F3 `[VERIFY NCT]` | Potentiates alkylators → narrows ifosfamide window; sequencing matters | Tumor is ALT-negative |
| **G-quadruplex stabilizers** | Chem/Pharma | G4 at telomeres (and *MYC* promoter) — both contexts | Preclinical-Cell | F4–F5 (programs stalled) `[VERIFY]` | Uncharacterized PK overlap | No G4-dependent telomere dysfunction in CIC-DUX4 |
| **Natural route** | Natural | **Empty** — no credible natural telomerase *inhibitor* at achievable conc. **Telomerase *activators* (TA-65/cycloastragenol) are COUNTER-INDICATED** (push the oncogenic direction) | Mechanistic (harm direction clear) | F5 / activators actively counter-indicated | Activators: direct pro-tumor concern, not a chemo interaction | n/a |

---

## 4. Patient-specific synthesis (the fusion-unconfirmed, pre-ifosfamide, oligometastatic case)

**Actionable to *think about* now (information + safety only — for oncologist discussion):**
- **Resolve the driver** (nuclear DUX4 IHC on archived P1; Macedo 2025 DOI 10.1111/his.15341) — gates the
  fusion-contingent MCL1 "flood." Already v3 FH-1.
- **The telomere/"kiln" archived-tissue trio** (ATRX/DAXX IHC + telomere-FISH + TERT-promoter seq) — cheap,
  fusion-agnostic, no new procedure; tells you whether there is even a candidate point-of-no-return.
- **The self-regimen CYP3A4 safety screen** (piperine + curcumin + thymoquinone × imminent ifosfamide
  branch-point) — the single highest-priority actionable item, already v3's #1 finding.

**Future-line forward hypotheses (post-ifosfamide; myelosuppression/timing-gated):**
- **Fusion-agnostic ERV/viral-mimicry "flood"** via HDACi/DNMTi timed to the post-ifosfamide IL-7/IL-15
  reconstitution window, **biomarker-gated** on ERV/dsRNA-sensor + APM induction (the falsifier) before any
  downstream immune step — this is v3 FH-3, with the clay framing supplying the "why."
- **Telomere effector** conditional on the diagnostic: imetelstat (TERT⁺) **or** ATRi (ALT⁺) — never both.

**HOLD (driver-contingent):** MCL1 "re-arm," all junction-specific constructs — until the driver is resolved.

**Counter-indicated / do-not (consolidated):**
- Telomerase-*activator* "anti-aging" supplements (TA-65/cycloastragenol) — wrong direction.
- Self-administered **oral bicarbonate / "alkalinizing" protocols** on an ifosfamide-injured tubule.
- Treating **oral/liposomal vitamin C as a "flood" tool** — it sits in the antioxidant range (chemo-blunting +
  Sayin metastasis concern), not the pro-oxidant TET range.
- Any intervention aimed at **dispersing** the tumor (loosening adhesion / inducing EMT) in this active-seeding
  window.

---

## 5. How this maps back to the fixed framework

The analogy **re-describes** existing surfaces; it does not add one. FH-Clay-1 → V3 (epigenetic/differentiation,
MCL1) + V4 (viral-mimicry/ICD danger signal). FH-Clay-2 → metastatic-disease layer + host-biology (ECM/mechanics).
FH-Clay-3 → host-biology (metabolic) + modality M1. FH-Clay-4 → build-recipe Step 6 + diagnostic/VoI layers.
**Not a fifth vector; not a new axis.** Its contribution is (a) a unifying physical rationale for "target the
maintenance layer, not the driver," and (b) two new falsifiable forward hypotheses (FH-Clay-2 mechanotransduction
direction; FH-Clay-3 tumor-local pH) plus a sharpened diagnostic framing for the telomere gap.

## 6. What this layer cannot tell you

- **Zero CIC-DUX4-specific evidence** for any effector; all viral-mimicry, mechanics, pH, and telomere-effector
  data transfer at P3–P4 from other tumors. The fundamental questions — *is CIC-DUX4 mechanotransduction-
  dependent? MCT1- or MCT4-dominant? TERT⁺ or ALT⁺?* — are **all unanswered**.
- **The CIC-DUX4 telomere-maintenance mechanism is genuinely unreported** — the single biggest gap in the build
  recipe. `[no direct citation — UNKNOWN]`.
- **Ceiling-effect risk on the flood:** the V3→V4 bridge assumes ERV/APM loci are baseline-repressed; the
  p300/CBP-activator biology could mean less to "flood" than assumed (untested).
- The analogy is a **principle-isomorphism, not literal chemistry** — a cell is not charged aluminosilicate
  platelets. It generates hypotheses; the lab kills them.

---

## Citations (deduped; perishable items dated/`[VERIFY]`)

**CIC-DUX4-direct:** Bakaric 2024 PMID 38275898 (p300/CBP); MCL1 tumoroids *Nat Commun* 2025 PMID 40841513 /
40841360 (reconcile); Macedo 2025 DOI 10.1111/his.15341 (DUX4 IHC); Koelsche 2014 PMID 24726063 (TERT-promoter
mutations rare in STS). **Viral mimicry (cancer-broadly):** Roulois 2015 PMID 26317466; Chiappinelli 2015 PMID
26343579; Cimmino 2017 PMID 28825709 (ascorbate/TET). **Mechanics/metastasis:** Stupp 2014 PMID 25304325
(cilengitide CENTRIC); simtuzumab program failure `[no single PMID; VERIFY registry]`; Yatomi 2015 PMID 26660549
(RvD1); Sayin 2014 PMID 25214635 (antioxidant→metastasis); Heaney 2008 PMID 18829561. **pH:** Robey 2009 PMID
19276390 (bicarbonate); Benjamin 2018 PMID 30157426 (MCT); Michelakis 2010 PMID 20505214 (DCA); Fais 2010
`[VERIFY PMID]`; SLC-0111 NCT03450018 / AZD3965 NCT01791595 `[VERIFY live]`. **Telomere:** Flynn 2015 PMID
25593184 (ALT/ATR); imetelstat FDA approval 2024-06-06, NDA 217779 `[VERIFY live]`. **OV:** T-VEC+pembro
NCT03069378.

*Research simulation / hypothesis generation only. Not medical advice. No dosing, no start/stop instructions.
Regulatory/trial status dated or `[VERIFY]` and perishable — re-verify before any external use.*
