# Metastatic Disease Considerations — CIC-Rearranged Sarcoma (Clean-Slate Run v3)

> Research-simulation / hypothesis-generation output. **Not medical advice. No dosing, no start/stop
> instructions, no treatment plan.** Metastatic-Disease Specialist sub-agent to the Orchestrator.

**Scope (one line):** This output asks, for each of the four vectors and the mRNA-team findings,
whether *metastatic / relapsed / oligometastatic* biology changes the picture for **this specific
patient** — it deliberately does **not** restate the vector mechanisms (those live in the four
`v{N}-summary-v3.md` files) and does **not** re-derive the chemo-interaction analysis (V1/V2/V3 own it).

**Confidence: low-to-medium.** The metastatic-biology *concepts* applied here (immunoediting/clonal
selection, the post-WLI TGF-β lung niche, antioxidant-metastasis signals, lymphodepletion windows,
oligometastatic favorability) are well-established cancer biology — but their application to **CIC-DUX4
specifically is essentially all `Mechanistic`/`Theoretical`**, there is **no CIC-DUX4 metastatic-biology
literature** beyond a handful of clinical-outcome series, and the single most decision-relevant variable
(whether the relapse clone differs from the 2024 primary) is **unmeasured in this patient**. Most claims
below are therefore explicitly low-confidence and framed as questions to resolve, not answers.

---

## Patient anchor (carried, not re-derived)

Soft-tissue CIC-rearranged sarcoma, dx June 2024, **FUSION-UNCONFIRMED** (~5% atypical subgroup). Biceps
femoris primary; 12 lung mets *at diagnosis* (so this was **metastatic from the outset** — a key framing
point below). VDC/IE ×14 → surgery Jan 2025 (>95% necrotic) → leg RT + whole-lung irradiation (WLI). NED
May 2025 → May 2026. May 2026: **oligometastatic relapse, single cluster, one lung**. Now beginning
**high-dose ifosfamide**.

**The one structural fact that conditions everything below:** the May-2026 relapse clone is not the
"average" tumor cell — it is the descendant of the rare cell(s) that survived 14 cycles of VDC/IE, a
>95%-necrotic resection, leg RT, **whole-lung irradiation**, and ~12 months of intact immune
surveillance. It is, by definition, a **selected survivor**. Whatever made it survive is the most
important unknown in this case, and it is the lens for the per-vector reads.

---

## Per-Vector Applicability in Metastatic Disease

### V1 — Rate Limiting → **APPLIES, with the caveat that V1 was always the weakest-effect vector and metastasis does not strengthen it**

V1's RAS/ERK–BRD4–CDK4/CCND1 throttling targets are **fusion-agnostic and not metastasis-specific** —
the ETV4/5→CCND1→CDK4 proliferation axis the relapse clone runs is the same axis the primary ran, so
nothing about lung-niche biology *removes* V1's rationale. But three metastatic-context points matter:
(1) the relapse clone has *already* demonstrated it can proliferate through cytotoxic pressure, so a
sub-threshold dietary throttle (V1's honest self-assessment: 1–3 orders of magnitude below cell-line-active
concentrations) is even less likely to bite on a treatment-hardened clone than on a treatment-naive one;
(2) the **CYP3A4 branch-point concern vs. imminent high-dose ifosfamide** (V1's headline finding —
piperine/curcumin/thymoquinone) is **independent of metastatic status** because it is host drug-metabolism,
not tumor biology, and is fully carried by V1/V2/V3 — I do not re-adjudicate it; (3) the metastatic setting
*raises the stakes* of that interaction question, because ifosfamide is now this patient's active
disease-control agent rather than a consolidation agent. **Net: V1 applies but is not differentially
helpful in metastasis; its most decision-relevant content (the ifosfamide interaction) is metastasis-agnostic.**
Tier for the metastasis-specific overlay: `Mechanistic`. CIC-DUX4-direct metastatic evidence: `None direct`.

### V2 — Compiler Protection → **DOES NOT APPLY as prevention; its metastatic relevance INVERTS into an active-disease harm-direction flag (the strongest V2↔metastasis interaction in this case)**

V2's core logic (reduce DSB/translocation rate in *at-risk healthy progenitors*) is a **primary-prevention**
frame that has essentially **no purchase in established metastatic disease** — the translocation already
happened, years ago, and protecting healthy progenitors does nothing to the existing lung clone. So V2's
*intended* mechanism does-not-apply here. **But metastasis flips V2 from "weak-but-harmless" to
"direction-of-harm matters," via two mechanisms V2 already flagged and which the metastatic context
sharpens:**
- **Sayin-2014-class antioxidant→metastasis signal (PMID 25214635; Le Gal 2015 follow-up).** Antioxidants
  (NAC, vitamin E) *accelerated* metastatic colonization in mouse Kras-lung/BRAF-melanoma models via
  reduced ROS-dependent BACH1 degradation. This patient is in an **active oligometastatic window** — the
  exact biological state (circulating/seeding tumor cells under oxidative stress) where that signal is
  most concerning. V2 correctly rates this `Mechanistic`/`Preclinical-Animal`-by-analogy (different
  compound, different route) — I concur and add only that **metastasis is what makes it load-bearing
  rather than academic**: in a NED patient the antioxidant-metastasis concern is hypothetical; in an
  actively-seeding oligometastatic patient it is the most defensible reason the patient's high-dose
  liposomal-vitamin-C habit deserves explicit oncology discussion. `Preclinical-Animal` (source models);
  CIC-DUX4-direct: `None direct`.
- **ROS-axis chemo-blunting (Heaney 2008, PMID 18829561).** V2's verdict (oral/liposomal vitamin C sits
  in the *protective* range, not the IV pro-oxidant range) is metastasis-independent in mechanism but
  metastasis-relevant in stakes, for the same reason as V1's ifosfamide point.

**Net: V2-as-prevention does-not-apply; V2-as-harm-direction-flag applies and is, for this patient,
the vector whose relevance metastasis changes the most.** Note the **doxorubicin-already-given** point:
the ROS/ICD-generating anthracycline is in the *past* (2024–25 VDC/IE), so the antioxidant↔doxorubicin
ROS-blunting concern is now retrospective, not active — the *active* ROS-relevant agent is ifosfamide,
whose alkylation mechanism is less clearly ROS-dependent (V2's own red-team flag, point 3). I carry that
nuance forward: the antioxidant concern that **is** active is the **Sayin metastatic-seeding** one, more
than the chemo-blunting one.

### V3 — Hot Patching → **APPLIES (fusion-agnostic entries), but metastatic clonal selection both RAISES the value of biopsying the relapse and SHARPENS the driver-contingent HOLD**

V3's fusion-agnostic clinical-track entries (CDK4i, HDACi/DNMTi MHC-I bridge, BETi) are **driver-robust
and therefore metastasis-robust** — they act on host chromatin / cell-cycle machinery the relapse clone
still runs. Metastasis does not remove them. Two metastasis-specific modifications:
- **The MCL1 "re-arm the DUX4 death program" entry (V3 rank 1, highest-ceiling, `Preclinical-Cell`+`Preclinical-Animal`,
  PMID 40841513 / 40841360) is driver-contingent AND now clone-contingent.** It is already on HOLD pending
  driver resolution for this fusion-unconfirmed patient. Metastatic clonal evolution adds a *second* layer:
  even if the 2024 primary had a confirmable DUX4-transactivation-domain driver, **the relapse clone that
  survived WLI + 14 cycles may have altered, downregulated, or epigenetically silenced that very
  dependency** — MCL1-buffering being a plausible *survival* adaptation, this could cut either way (the
  survivor clone might be *more* MCL1-dependent, or might have escaped the dependency entirely). This is
  unknowable without **relapse tissue**, and it strengthens the case that if the MCL1 line is ever to be
  considered, it should be licensed off the **current** clone, not the archived 2025 specimen. Tier:
  `Mechanistic` (the clonal-evolution overlay); the underlying MCL1 biology stays `Preclinical-Cell/Animal`.
- **dCBP-1 / p300-CBP dependency (V3 rank 4, `Preclinical-Cell`, PMC8511258)** is likewise partially
  driver-contingent and would carry the same "is it still true in the survivor clone?" caveat.

**Provenance call (ties to ADR-0011, P1 archived vs P2 fresh):** for the **fusion-agnostic** V3 entries,
the archived Jan-2025 P1 FFPE block is adequate (CDK4/CDKN2A status, ARID1A status, MHC-I/APM baseline are
unlikely to be the load-bearing difference between primary and relapse for those mechanisms). For the
**driver-contingent / clone-sensitive** entries (MCL1, dCBP-1, any junction-targeted approach), the
relapse clone is the right substrate, and a **fresh P2 biopsy of the single lung lesion** would carry
disproportionate value *if* those high-ceiling lines are to be pursued — but that biopsy's value is
gated entirely by whether the driver is first resolved (DUX4 IHC on the cheaper archived block first,
per ADR-0008 EVSI ordering). **Net: V3 applies; metastasis re-weights V3's diagnostic sequencing toward
"resolve driver on archived tissue → only then consider fresh relapse tissue for the contingent lines."**

### V4 — Immune Watchdog → **APPLIES, and is the vector whose RATIONALE metastasis most strengthens — but also the one where the selected-survivor logic cuts hardest against the leading hypothesis**

This is the richest metastasis interaction, so I separate the two directions:

**Why metastasis strengthens V4's rationale.** (a) **Oligometastatic, single-cluster, one-lung relapse is
the textbook favorable, surveillance-dependent setting** — exactly where an immune/NK-surveillance or
local-control (metastasectomy/SBRT) framing has the most plausible leverage, because the disease burden
is low enough that a surveillance mechanism (rather than bulk cytoreduction) could matter. (b) The
**post-ifosfamide lymphodepletion/reconstitution window** (V4 rank 3 / Forward Hypotheses 1–2) is an
*active, imminent, time-limited* opportunity in this patient — metastasis/relapse is precisely the context
that makes the IL-15-axis-timed-to-NK-reconstitution idea worth raising now rather than abstractly.
(c) **Prior doxorubicin ICD** (Casares 2005 PMID 16365148; Obeid 2007 PMID 17187072) and **prior WLI
cGAS-STING priming** are both *historical immunogenic events* whose residue, if any, would be most
relevant in the lung — the relapse site.

**Why the selected-survivor logic cuts against V4's leading hypothesis.** The relapse clone survived
~12 months of intact immune surveillance. Under immunoediting theory (Schreiber/Dunn "elimination →
equilibrium → escape"; foundational, no single PMID), a clone that emerges from a year of NED is, by
selection, **enriched for immune-escape phenotypes** — most plausibly **MHC-I-low** (T-cell escape) and/or
**antigen-loss / further-reduced-TMB** variants. This has two opposite implications V4 already half-captures
but which metastasis makes concrete:
- It **strengthens the NK-missing-self argument** (V4 rank 1): a clone that escaped *T-cells* by dropping
  MHC-I is, in principle, *more* exposed to NK missing-self recognition — **if** it co-expresses NK-activating
  stress ligands (MICA/MICB/ULBP, PVR/CD155). So the selected, MHC-I-low relapse clone could be the
  *best* NK-missing-self target this patient's disease has presented. `Mechanistic`.
- It **simultaneously raises the "doubly cold" failure mode** (V4's own load-bearing red-team flag): a
  clone selected through both T-cell *and* (possibly) early NK pressure could be MHC-I-low **and**
  stress-ligand-low, in which case NK has no purchase either. Whether the survivor clone is "NK-exposed"
  or "doubly cold" is **the single highest-value unmeasured immune question for the relapse**, and it can
  only be answered on **relapse tissue** (the archived 2025 block predates the selection event). This is
  the clearest place in the whole analysis where **P2 fresh-relapse provenance (ADR-0011) beats P1 archived**
  — the immune-escape phenotype is, almost by definition, a property the archived primary cannot report.

**The one CIC::DUX4-direct immunotherapy data point** (V4's nivolumab+relatlimab cold-to-hot case report,
PMID 40128305 / PMC11933392, `[VERIFY]`) was in a fusion-**confirmed** patient and is a **disease-class
precedent only** for this fusion-unconfirmed patient — it shows CIC::DUX4 tumors are *not* immunologically
inert, which is mildly encouraging for the relapse setting, but transfers at low confidence (P0→P1 rung
at best, and only if this patient's tumor is in the same disease class). `Clinical-Trial (single case)`.

**Microenvironment-specific point — the post-WLI lung niche.** This patient's relapse sits in a lung that
received **whole-lung irradiation**. The mRNA team and V2 both flag the resulting **TGF-β-dominant,
fibrotic milieu** (V2 Forward Hypothesis 2; mRNA team §2c/§9.8). For V4 this is a **double-edged
metastatic modifier**: TGF-β is immunosuppressive and fibrosis impedes immune-cell trafficking (argues
*against* immune approaches working in this niche), **while** residual cGAS-STING priming from the
radiation (if it persists >1 yr — unestablished, mRNA team §9.8) could be a standing immunogenic
*advantage* in that same niche. These pull in opposite directions and **neither is measured**. This is a
genuinely metastasis-site-specific tension that none of the four vectors fully owns because it is a
property of *where the relapse is*, not of any vector's mechanism. Tier: `Mechanistic`; CIC-DUX4-direct:
`None direct`.

**Net: V4 applies and metastasis strengthens its rationale (oligometastatic favorability +
lymphodepletion window), but the selected-survivor immune-escape logic makes the relapse-tissue immune
phenotype — MHC-I-low-but-NK-exposed vs. doubly-cold — the decisive unknown, answerable only on fresh
relapse tissue.**

---

## mRNA Team Findings — Metastatic Relevance

The mRNA team's net finding is **no persistent BNT162b2 effect at this patient's 2+-year timepoint**, and
nothing about metastasis changes that null — the relapse clone's biology is dominated by VDC/IE
selection, WLI, and imminent ifosfamide, not by a vaccine administered before diagnosis. Two mRNA-team
items *do* have a metastasis-specific read, both already surfaced by the team and carried here without
inflation:
- **Post-WLI cGAS-STING persistence (mRNA team §9.8)** and the **TGF-β fibrotic lung niche (§2c)** are
  the team's most metastasis-relevant observations — not because of the vaccine, but because the team
  correctly identified the *lung relapse niche itself* as a dominant inflammatory context. I fold this
  into the V4 microenvironment paragraph above: the irradiated lung is simultaneously immunosuppressive
  (TGF-β/fibrosis) and possibly immune-primed (residual STING) — a metastasis-site property, both
  `Mechanistic`, both unmeasured at this timepoint.
- **Anti-PEG flag (Kozma 2022, PMID 35853896, `[VERIFY]`)** is metastasis-agnostic in mechanism but
  becomes *practically* relevant only in the metastatic/relapse setting where a future LNP-mRNA
  personalized-neoantigen vaccine might actually be considered — i.e., metastasis is what could make a
  design-level flag into a real PK covariate. Still `Mechanistic`/design-level only; not actionable now.

No mRNA-team finding argues for or against any metastatic intervention on its own evidence.

---

## Metastatic-Specific Forward Hypotheses

**[Forward Hypothesis 1] — The May-2026 relapse clone is immunoedited toward an MHC-I-low *but
NK-ligand-retained* phenotype, making the post-ifosfamide NK-reconstitution window the single best-timed
opportunity for NK-directed surveillance against oligometastatic residual disease — and a paired
archived-primary-vs-fresh-relapse immune-phenotype comparison would test it directly.**

*Statement.* A clone that emerges from ~12 months of NED has been selected for immune escape; the most
common escape route in fusion-driven, low-TMB sarcoma is MHC-I/APM downregulation (T-cell escape). If
that clone *retains* NKG2D/DNAM-1 stress ligands (MICA/MICB/ULBP, PVR/CD155), it is paradoxically *more*
NK-exposed than the original primary was — and high-dose ifosfamide's lymphodepletion creates an
IL-15-rich reconstitution window in which NK-supportive measures (IL-15 superagonist N-803-class; or, if
deficient, vitamin-D3/zinc correction) would have their clearest rationale, against a low disease burden
(oligometastatic = favorable for surveillance).
*Mechanistic basis.* Cancer immunoediting (elimination→equilibrium→escape) predicts MHC-I-low selection
under T-cell pressure; NK missing-self (Ljunggren/Kärre) predicts MHC-I-low + ligand-positive cells are
NK targets; post-lymphodepletion homeostatic IL-7/IL-15 expansion is the established basis for timing
NK/T support to reconstitution (V4 ranks 1–3, Forward Hypotheses 1–2). This hypothesis is the **explicit
metastatic-clonal-evolution upgrade** of V4's NK-first framing: V4 argues NK-first on the *current* tumor;
this argues the *selected relapse clone is a better NK substrate than the primary was* — a claim only the
relapse-vs-primary comparison can settle.
*Falsifier / what would test it.* IHC / flow / RNA-seq for HLA-A,B,C + B2M + TAP1/2 **and** MICA/MICB,
ULBP, PVR/CD155, HLA-E on **paired** archived 2025 primary (P1) and **fresh 2026 relapse (P2)** tissue.
Predicted result if true: relapse MHC-I lower than primary, stress ligands retained. **Falsified** if the
relapse is MHC-I-low *and* stress-ligand-low ("doubly cold" — NK has no purchase, shift to ICD/danger-signal
induction per V4 expansion module A) or if MHC-I is unchanged (no T-cell-escape selection occurred — then
the escape route was something else, e.g., a microenvironmental/T-cell-exclusion mechanism). Tier:
`Mechanistic`/`Theoretical`. Fusion-agnostic — **fully applicable to this fusion-unconfirmed patient.**
*Why not yet tested.* Paired primary-vs-relapse immune-phenotyping is rare in any sarcoma and absent in
CIC-DUX4 (too few cases with both timepoints biopsied); the NK-exposure-of-the-survivor-clone framing has
not been articulated for this disease.

**[Forward Hypothesis 2] — In a patient who was metastatic-from-diagnosis and is now oligometastatic
after a long NED interval, ctDNA/fusion-junction-or-surrogate liquid-biopsy kinetics across the
ifosfamide course would be a higher-value, lower-burden monitor of the *selected* clone than serial
imaging alone — and would partially substitute for repeat tissue biopsy of a single deep lung lesion.**

*Statement.* The relapse clone's defining feature is that it is a survivor; its trajectory under
ifosfamide is the most decision-relevant dynamic quantity in the case. A liquid-biopsy readout (P3
provenance, ADR-0011) — ctDNA tumor fraction, or, if the driver is ever resolved, a junction-specific
assay — sampled before/during/after the ifosfamide course would track whether the selected clone is
responding, and would do so without repeated sampling of a single deep lung lesion (low burden, repeatable,
captures clonal dynamics a one-time biopsy cannot).
*Mechanistic basis.* ctDNA shed scales with tumor burden and turnover; oligometastatic single-lesion
disease is low-burden (a sensitivity challenge) but a *relapse* clone under cytotoxic pressure is exactly
when shedding/turnover transiently rises. This is a **monitoring** hypothesis, not a treatment one — it
addresses the metastatic-specific problem that the *current* clone, not the archived primary, is what
matters, and tissue access to it is limited.
*Falsifier / what would test it.* Serial plasma ctDNA (tumor-fraction or methylation-based, fusion-agnostic
panels exist) at baseline + each ifosfamide cycle + post-course, correlated with imaging response of the
single lung lesion. **Falsified** if ctDNA is undetectable throughout (burden below assay floor — a real
risk in oligometastatic disease, and an honest limitation) or fails to track imaging. Tier: `Mechanistic`
for the application to this disease; the underlying ctDNA-monitoring methodology is `Clinical-Trial`/`Established`
in other tumors but **`None direct` in CIC-DUX4**, and **fusion-unconfirmed status removes the
junction-specific (most sensitive) assay option** — only fusion-agnostic ctDNA panels apply (atypical-case
flag). `[VERIFY]` that a validated fusion-agnostic ctDNA assay is accessible before relying on this.
*Why not yet tested.* No published CIC-DUX4 ctDNA-monitoring series of meaningful size exists (rarity);
fusion-unconfirmed cases are doubly disadvantaged because the most sensitive (junction) assay is unavailable.

---

## What I Could Not Establish

1. **Whether the May-2026 relapse clone differs from the 2024 primary in any load-bearing way** (MHC-I/APM
   status, stress-ligand expression, MCL1/p300-CBP dependency, TMB, driver) — the central unknown of this
   entire analysis. No relapse tissue has been molecularly characterized; the archived 2025 block predates
   the selection event by definition. Every "the selected clone may be X" claim above is `Mechanistic`/`Theoretical`.
2. **Any CIC-DUX4-specific metastatic-biology literature** — lung-niche colonization mechanism,
   organotropism, immunoediting trajectory, or clonal-evolution data. None located; the field is too rare.
   All metastasis biology here is transferred from other tumors (P3–P4 Directness, ADR-0014) and admitted
   at correspondingly low confidence.
3. **Whether post-WLI cGAS-STING priming persists in this lung at >1 year** (mRNA team §9.8) and whether
   the TGF-β fibrotic niche net-helps or net-hurts an immune approach in the relapse site — both unmeasured,
   pulling in opposite directions.
4. **Whether the relapse clone is NK-exposed (MHC-I-low, ligand-positive) or "doubly cold"** — the decisive
   fork for V4's NK-first framing in the metastatic setting; answerable only on fresh relapse tissue.
5. **The patient's smoking status, 25(OH)D/zinc status, current NK/T-cell compartment, and microbiome** —
   all carried as unknowns from the vector outputs; each conditions a metastatic read but none is recorded.
6. **Whether ifosfamide's cytotoxic mechanism is meaningfully ROS-dependent** (V2 red-team point 3) — bears
   on how strongly the antioxidant-during-active-metastatic-disease concern applies to the *imminent* agent
   specifically vs. the already-given doxorubicin.
7. **Oligometastatic local-control framing (metastasectomy / SBRT) is named, not evaluated** — whether a
   single-lung-lesion local therapy is appropriate is a clinical-staging/operability question outside this
   simulation's scope and this sub-agent's mandate; flagged as the obvious oligometastasis-specific option
   for the oncologist/MTB, not assessed here.

### Red-Team Self-Challenge (ADR-0017, one pass)

1. **Load-bearing assumption.** That the relapse clone is *immunoedited / phenotypically different* from the
   primary in a direction that matters (esp. MHC-I-low). Everything in the V4 read and Forward Hypothesis 1
   hinges on it.
2. **Disconfirmation.** The strongest evidence *against* it: this tumor was **metastatic from diagnosis**
   (12 lung mets at dx) and the relapse is in the same organ — so the relapse may not represent *new*
   immune escape at all, but **outgrowth of a pre-existing, already-disseminated clone** that was merely
   chemo-suppressed, never immune-edited. Under that reading the "selected-for-immune-escape" premise is
   weaker and the primary↔relapse immune phenotype might be *similar*, not divergent. I did search for this
   (it is why FH1's falsifier explicitly includes the "MHC-I unchanged" outcome). The metastatic-from-dx
   history genuinely undercuts the immunoediting narrative more than a primary-then-late-met history would.
3. **Alternative (outside V1–V4).** The relapse may be driven less by tumor-cell-intrinsic escape than by a
   **metastatic-niche / host-biology** property — the post-WLI TGF-β fibrotic lung creating a
   sanctuary/immune-excluded microenvironment. That is a **host-biology-modifier-layer (ADR-0005)** thread
   (niche conditioning, not a tumor-cell vector) and I flag it there rather than forcing it into V4.
4. **Flip test.** If the load-bearing assumption is wrong (relapse ≈ primary, no meaningful editing), does
   anything survive? Yes, partially: the **oligometastatic-favorability** and **post-ifosfamide
   lymphodepletion-window** framings (V4 strengthening) survive — they depend on disease *burden/timing*,
   not on clonal divergence. But Forward Hypothesis 1's "better NK substrate than the primary" claim does
   **not** survive and is tagged **clone-divergence-contingent**. FH2 (ctDNA monitoring) survives regardless.
5. **Steer audit.** The prompt explicitly steered toward "the relapse clone is selected → implications for
   MHC-I-low / antigen-loss / NK." I treated that as a hypothesis to *test* (FH1 is built as falsifiable,
   and the disconfirmation in point 2 actively weakens the steer) rather than a conclusion to confirm —
   the metastatic-from-diagnosis history is the honest counterweight I surfaced against the steer, not a
   detail I smoothed over.

---

## Atypical-Case Note (~5% fusion-unconfirmed — this patient)

The metastatic reads above are **overwhelmingly fusion-agnostic** and therefore apply to this
fusion-unconfirmed patient: immunoediting/clonal-selection logic, the NK-missing-self relapse argument,
the post-ifosfamide lymphodepletion window, the antioxidant-metastatic-seeding (Sayin-class) concern, the
post-WLI niche tensions, the oligometastatic-favorability framing, and ctDNA *fusion-agnostic* monitoring
all hold without a confirmed fusion. **Fusion-CONFIRMED-only / driver-contingent in the metastatic
setting:** the MCL1 "re-arm" line and any junction-targeted approach (already on HOLD), and the
junction-specific (most-sensitive) ctDNA assay option in Forward Hypothesis 2 — for which only the
fusion-agnostic ctDNA fallback applies here. Resolving the driver (DUX4 IHC on archived tissue first, per
ADR-0008) remains the gate for the contingent metastatic lines, exactly as in the primary-tumor analysis.

---

*Research-simulation / hypothesis-generation output. Not medical advice. No dosing, start/stop, or
treatment recommendations are made or implied. Perishable trial/regulatory items tagged `[VERIFY]` are
carried from the vector inputs and must be re-confirmed live before any external use.*
