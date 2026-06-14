# V4 NK Cell Specialist — NK Cell Activation Report (Clean-Slate Run v3)

**One-line summary:** This output covers NK missing-self/KIR/NKG2D-ligand biology with the
**MHC-I-low → NK-visible paradox as its spine**, vitamin D3/zinc status framed as
deficiency-correction-vs-replete-supplementation, the IL-15-superagonist and NK-engager
clinical pipelines, adoptive NK transfer, and the NK-first-vs-MHC-I-priming sequencing question
(integrating the V3→V4 bridge, the NKG2A/HLA-E escape valve, and the VoI ranking of nectin/HLA-E/NK
fitness). It deliberately **excludes** checkpoint/T-cell-arm mechanics (`tcell-surveillance.md`),
microbiome-driven immune modulation (`microbiome-immune.md`), and neoantigen-vaccine design
(`neoantigen-vaccine.md`) except where they intersect the NK arm.

**Confidence: medium** — core NK missing-self/KIR/NKG2D biology is textbook-established;
vitamin D3/zinc-NK correlations are documented in cancer-broadly and healthy-volunteer
populations; the IL-15-superagonist and Nectin-axis clinical landscapes are real and
live-verified this session. What pulls confidence to "medium" rather than "high": **zero direct
CIC-DUX4 NK-killing, stress-ligand, or HLA-E data exist**, and the NK-first sequencing
recommendation is a mechanistic inference from a logic model (Sim 4/6), not an experimental
result.

---

## THE CENTRAL FRAMING CONCEPT: MHC-I-LOW IS A LIABILITY AGAINST NK CELLS

### NK missing-self detection — the core biology

NK cells integrate a balance of inhibitory and activating signals at the immune synapse:

- **Inhibitory receptors read MHC-I as a "self" password.** KIR family (KIR2DL1/2/3, KIR3DL1/2)
  and the CD94/NKG2A heterodimer engage classical HLA-A/B/C and non-classical HLA-E. When MHC-I is
  present at normal density, inhibitory ITIM signaling dominates and the NK cell stands down —
  this is "license to kill withheld."
- **Activating receptors read "stress."** NKG2D (KLRK1) engages MICA/MICB and the ULBP1–6 family;
  NKp30/NCR3 engages B7-H6; NKp46/NCR1 engages viral hemagglutinins and other stress ligands;
  DNAM-1/CD226 engages PVR/CD155 and Nectin-2/CD112 (the "Nectin axis" — see Critical Cross-Inputs
  below).
- **Missing-self logic:** when inhibitory signal drops (MHC-I-low) *and* activating ligands are
  present, the activation/inhibition balance tips toward killing. Tumor cells that downregulate
  MHC-I to escape CD8+ T-cells *remove their own inhibitory password for NK cells*.

Tier: **Established** (KIR/NKG2D/missing-self model — Ljunggren & Kärre 1990 "missing self"
hypothesis; foundational immunology, textbook-level, no single PMID needed for the framework
itself). Evidence in CIC-DUX4 specifically: **None direct**.

### The paradox, stated for this tumor

The V3 vector lead's epigenetic-reprogramming work (`v3-summary-v3.md`, MHC-I Upregulation
Candidates section) and the V4 expansion (`immune-watchdog-expansion.md`) both proceed from the
premise that CIC-DUX4 cells, like many fusion-driven sarcomas, downregulate MHC-I/HLA-A,B,C and
antigen-presentation-machinery (APM: TAP1/2, PSMB8/9, B2M) genes — the standard route by which a
fusion-positive tumor cell becomes invisible to CD8+ T-cell surveillance of its junction
neoantigen.

**That exact same downregulation is the signal NK cells are built to detect.** A cell that is
MHC-I-low has *removed its own inhibitory brake on NK cytotoxicity*. If CIC-DUX4 cells additionally
display NK-activating stress ligands (NKG2D ligands MICA/MICB/ULBPs, or DNAM-1 ligands PVR/CD155
and Nectin-2/CD112 — plausible under oncogenic replicative/proteotoxic stress, but **not measured
in CIC-DUX4**), the missing-self/stress-ligand combination predicts these tumor cells should be
NK-susceptible **precisely because** of the property that makes them T-cell-invisible.

This is, by a wide margin, the strongest *single mechanistic argument* in this vector for this
patient: it requires no new drug discovery, it is fusion-agnostic (the MHC-I-low phenotype is a
general tumor-immune-evasion strategy, not a CIC-DUX4-junction-specific one), and it converts the
V3 vector's headline finding (MHC-I-low CIC-DUX4) from a pure liability into a dual-edged
opportunity — IF the NK arm is engaged before that liability is "fixed." That "if" is the
sequencing question addressed next.

Tier: **Mechanistic** (the logic chain — MHC-I-low → reduced KIR/NKG2A inhibition → NK
susceptibility — is established immunology; its application to CIC-DUX4 is inferred, not
measured). Evidence in CIC-DUX4 specifically: **None direct**.

---

## THE SEQUENCING TENSION: NK-FIRST vs. MHC-I-PRIMING — RESOLVING THE CROSS-VECTOR CONFLICT

### The conflict as handed off from V3 and the V4 expansion

`v3-summary-v3.md`'s MHC-I Upregulation Candidates section ranks **HDAC inhibitors (rank 1)** and
**DNMT inhibitors (rank 2)** as the fusion-agnostic, Clinical-Trial-tier route to restore MHC-I/APM
transcription via viral-mimicry/type-I-IFN signaling (EZH2i, rank 3, is now doubly caveated —
mechanistically de-prioritized by the p300/CBP-activator finding for CIC-DUX4, AND access-closed by
the 2026-03-09 worldwide tazemetostat withdrawal).

But MHC-I restoration is exactly the change that **removes the NK-activating missing-self signal**.
If HDACi/DNMTi successfully restore HLA-A,B,C/B2M/TAP on CIC-DUX4 cells, those cells re-acquire
their inhibitory KIR/NKG2A "self" password and become *less* NK-visible — even as they become
*more* T-cell-visible. The two arms of V4 are pulling on the same dial in opposite directions.

`immune-watchdog-expansion.md` (Forward Hypothesis 1, module C3) already identified the resolution
as **"NK-first"**: exploit the MHC-I-low window with NK-directed interventions *before* deploying
epigenetic MHC-I priming, then transition to T-cell/checkpoint strategies once MHC-I is restored.
I adopt and extend that position here rather than re-deriving it.

### My position: NK-first, with three refinements

1. **Sequencing order:** NK-directed activation (IL-15-superagonist support, deficiency-correction
   of vitamin D3/zinc, and — if ever clinically reachable — adoptive NK transfer or PVR-axis
   de-repression) should be considered the **earlier-phase lever**, while the tumor is in its
   native MHC-I-low state. HDACi/DNMTi-based MHC-I restoration (the V3→V4 bridge) is the
   **later-phase lever**, switching the dominant effector arm from NK to T-cell/checkpoint.
   This is the same ordering `immune-watchdog-expansion.md` Forward Hypothesis 1 proposes via
   PVR-axis blockade — I am stating it more generally (it applies to *any* NK-potentiating
   intervention, not only NTX1088-class agents) and tying it explicitly to the dietary/
   supplement-level NK levers this specialist covers.

2. **The HLA-E/NKG2A escape valve compounds the case for NK-first, it doesn't just complicate
   timing.** `immune-watchdog-expansion.md` module C3 and Forward Hypothesis 3 flag that HLA-E
   is frequently *upregulated* precisely when classical MHC-I is *downregulated*, and that
   epigenetic MHC-I restoration could **paradoxically co-induce HLA-E** — engaging NKG2A on both
   NK cells and CD8+ T-cells and re-suppressing the very arms MHC-I-priming was meant to enable.
   If that is correct, the MHC-I-low window may be the **only** window in which the NK arm is
   *not* simultaneously checked by an HLA-E/NKG2A brake (assuming HLA-E tracks with classical
   MHC-I rather than being constitutively high — **this is unmeasured in CIC-DUX4**, see "What I
   Could Not Establish"). That sharpens the NK-first argument from "do NK things first because
   it's convenient" to "the NK window may close, not just shift, once epigenetic priming begins."

3. **The VoI ranking independently supports NK-axis primacy.** `biomarker-voi-stratification.md`
   ranks **Nectin CD155/CD112 IHC** (#1, VoI 0.625) and **HLA-E expression** (#2, VoI 0.500) as the
   two highest-value unmeasured biomarkers for this case — both NK-arm variables — because in the
   Sim 4/6 kill-rule logic the DNAM-1 activating signal is a shared AND-gate for *both* T-cell and
   NK non-cytotoxic clearance, so losing it collapses the entire program with no fallback. **NK
   functional reserve post-WLI/chemo** ranks #5 (VoI 0.250) — lower, but directly actionable for
   this patient (see below). MHC-I/B2M/TAP integrity itself ranks only #6 (VoI 0.188) — because in
   this model, NK provides a fallback route if MHC-I/T-cell fails, but **nothing provides a
   fallback if the nectin/DNAM-1 axis is lost**. Read together: the model says the NK arm's
   *inputs* (nectin ligands, HLA-E, NK fitness) are collectively more decision-critical than the
   MHC-I axis itself — independently consistent with running the NK arm early, while those inputs
   are most likely to be favorable (pre-epigenetic-priming).

**My sequencing position, stated plainly:** **NK-directed measures first (current MHC-I-low
window) → HDACi/DNMTi-based MHC-I restoration second → T-cell/checkpoint (± NKG2A blockade per
Forward Hypothesis 3 below) third.** This is consistent with, and extends, the existing V4
expansion's Forward Hypothesis 1 — it is not a new claim, but I am the specialist asked to anchor
V4's NK-specific contribution to it, so I state it as my landed position rather than only
referencing it.

**Caveat on what "NK-directed measures" can realistically mean for this patient right now:** the
clinical pipeline (IL-15 superagonists, NK engagers, adoptive NK transfer, PVR-axis blockade) is
overwhelmingly early-phase/non-sarcoma (see Clinical Track below) — so in practice, "NK-first" for
*this patient at this moment* mostly means (a) not deferring vitamin D3/zinc deficiency-correction
(below), (b) being aware that the post-ifosfamide NK-reconstitution window is a window where IL-15
support has the clearest existing rationale (N-803/QUILT precedent), and (c) flagging to any future
trial discussion that an HDACi/DNMTi-based MHC-I-priming approach, if pursued, has a "before NK
arm is engaged" vs. "after" timing question worth raising. This is **not** a recommendation to
delay any SOC component.

---

## DIETARY TRACK

### Vitamin D3 — NK cell function

**Mechanism:** 1,25(OH)₂D₃ (calcitriol) signals through the vitamin D receptor (VDR), which is
expressed on NK cells and their bone-marrow precursors. VDR signaling has been reported to:
- Modulate NK cytotoxic receptor expression and IFN-γ production [Mechanistic; reviewed in
  immunology literature, e.g. Mihaela Surcel/Pal-Yu Wang-style reviews of vitamin D and NK
  function — no single landmark CIC-DUX4-relevant PMID located this session; tier kept at
  Mechanistic for the receptor-signaling chain].
- Support NK precursor differentiation in bone marrow via VDR-dependent transcriptional programs.
- Be associated, in population studies, with vitamin D deficiency correlating with reduced
  circulating NK-cell cytotoxic activity [Dietary-Observational / Clinical observational —
  population-level association, not interventional proof of causation].

Tier: **Mechanistic** (VDR→NK signaling chain) + **Dietary-Observational** (deficiency↔reduced NK
activity association). Evidence in CIC-DUX4 specifically: **None direct.**

**The mandatory framing — correcting a documented deficiency vs. supplementing a repleted
individual:**

- **Correcting a documented deficiency (serum 25(OH)D below the assay's deficiency threshold,
  commonly cited around <20 ng/mL):** the mechanistic chain (low VDR ligand → reduced VDR-driven
  NK transcriptional programs → reduced NK cytotoxicity/IFN-γ) is coherent and the deficiency
  state itself is a well-established immune-relevant abnormality independent of any cancer
  application. Restoring 25(OH)D toward a normal range in a *documented-deficient* person has a
  clear, defensible rationale.
- **Supplementing in a vitamin-D-replete individual:** evidence for *additional* NK benefit above
  a normal baseline is thin. The large VITAL trial (vitamin D3 2000 IU/day vs placebo, general US
  adult population) found no overall cancer-incidence or cancer-mortality benefit from
  supplementation in a population not selected for deficiency [Clinical-Trial — Manson et al.,
  *NEJM* 2019, PMID 30415629]. No published VITAL sub-analysis specifically reports NK-function
  outcomes by baseline 25(OH)D status to my knowledge.
- **This patient's status is the open question.** The patient is self-administering vitamin D3 as
  part of the regimen, but **no 25(OH)D serum level is recorded in the case as presented.** This
  means the framework currently **cannot distinguish** "this is correcting a real deficiency
  (clear rationale)" from "this is supplementation in an already-replete person (rationale for
  *additional* NK benefit is thin)." **The honest framing is that vitamin D3 supplementation in
  this patient is currently of *unknown* marginal value for the NK arm specifically** — it may be
  doing real immunological work (if deficient) or have a primarily bone-health/general-wellness
  rationale with NK benefit not separable from "already adequate" (if replete). I flag this
  explicitly as a value-of-information gap below rather than assuming either direction.
- **"Naturally achievable ≠ unlimited":** standard over-the-counter D3 dosing used for deficiency
  correction is not "more is better" — the goal is restoring a normal range, not maximizing serum
  25(OH)D, and hypercalcemia is a real risk at sustained high intake.

**Chemo-interaction screening (`sarcoma-chemo-interactions`):**
```
Vitamin D3 — chemo screening:
  CYP3A4: Vitamin D3 itself is not a notable CYP3A4 inhibitor/inducer at typical supplemental
    doses; vitamin D metabolism (25-hydroxylation/1-alpha-hydroxylation/24-hydroxylation) involves
    CYP2R1, CYP27B1, CYP24A1 — distinct from the CYP3A4 axis that activates ifosfamide/
    cyclophosphamide and metabolizes vincristine/etoposide. No documented competitive interaction
    at standard supplemental intake.
  P-gp: no documented P-gp modulation by vitamin D3 at supplemental doses.
  ROS-axis: vitamin D3 is not a high-dose antioxidant in the NAC/vitamin-C/vitamin-E sense; no
    documented interference with doxorubicin/ifosfamide ROS-dependent mechanisms.
  Other: hypercalcemia risk at high sustained intake — relevant to renal monitoring given
    ifosfamide's nephrotoxicity profile (a hypercalcemia + nephrotoxic-agent combination is a
    monitoring consideration, not a documented pharmacologic interaction).
  Citation: no DrugBank or NCCN Integrative Medicine interaction flagged between vitamin D3 (at
    typical supplemental intake) and vincristine/doxorubicin/cyclophosphamide/ifosfamide/
    etoposide; general pharmacology references for vitamin D metabolism (CYP2R1/CYP27B1/CYP24A1
    vs CYP3A4) are textbook-level.
```

### Zinc — NK cell development and function

**Mechanism:** zinc is required as a cofactor and structural element across NK-cell-relevant
pathways:
- Zinc-finger transcription factors and zinc-dependent enzymes participate broadly in lymphocyte
  development; thymulin, a zinc-dependent thymic hormone, supports lymphoid maturation.
- Zinc deficiency is associated with reduced NK cell numbers and reduced NK cytotoxic activity in
  both animal models and human deficiency states [Mechanistic + Preclinical-Animal — zinc
  deficiency/NK literature, e.g. Shankar & Prasad-type reviews of zinc and immune function; no
  CIC-DUX4-relevant PMID located this session].
- Zinc is also a cofactor relevant to V1/V2 (DNA repair, Ku70/Ku80, p53 zinc finger — see
  `sarcoma-vector-context` cross-vector table) — the NK-relevant role is additive to, not separate
  from, those other roles.

Tier: **Mechanistic** (zinc-dependent pathways in lymphocyte/NK development) + **Preclinical-Animal**
(zinc-deficient models show restorable NK deficits on repletion). Evidence in CIC-DUX4
specifically: **None direct.**

**Deficiency correction vs. replete-supplementation — same framing as vitamin D3:**

- **Correcting documented zinc deficiency** (low serum zinc, or clinical signs consistent with
  deficiency — which is plausible in a post-VDC/IE, post-surgical, nutritionally-stressed cancer
  patient): a defensible rationale for NK (and broader immune) support.
- **Supplementing a replete individual:** no additional NK benefit is established, and **excess
  zinc has a real, documented harm mechanism** — chronic intake above the tolerable upper intake
  level (commonly cited around 40 mg/day elemental zinc for adults) displaces copper absorption,
  risking copper-deficiency anemia and neuropathy. This is the textbook "natural ≠ unlimited"
  counter-example for zinc specifically and must not be soft-pedaled.
- **This patient's regimen, as documented for this clean-slate run, does not list an explicit
  zinc supplement** (the self-administered regimen is: curcumin+piperine, liposomal vitamin C,
  black cumin seed oil, vitamin D3, honey, and fresh celery/ginger/carrot/broccoli/apple/beetroot
  juice). Zinc intake from this regimen is therefore **dietary-level only** (juice vegetables are
  not notable zinc sources; zinc-dense foods are oysters, pumpkin seeds, meat — none of which
  appear in the documented regimen). **No serum zinc level is recorded.** As with vitamin D3, the
  framework cannot currently distinguish "this patient is zinc-replete" from "this patient has an
  unrecognized zinc deficiency that NK function would benefit from correcting" — flagged below as
  a value-of-information gap.

**Chemo-interaction screening (`sarcoma-chemo-interactions`):**
```
Zinc — chemo screening:
  CYP3A4: no documented CYP3A4 modulation by zinc at dietary or standard supplemental
    (correction-level) doses.
  P-gp: no documented P-gp modulation by zinc.
  ROS-axis: zinc is a cofactor for Cu/Zn-superoxide dismutase (antioxidant enzyme); at
    deficiency-correction doses this is not equivalent to the high-dose isolated-antioxidant
    concern (NAC/vitamin C/vitamin E) flagged elsewhere in V2 — but at supraphysiologic doses,
    secondary copper deficiency could in principle affect Cu/Zn-SOD balance. Not established as
    a clinically meaningful chemo interaction at correction-level doses.
  Other: excess zinc (>UL, ~40 mg/day elemental) displaces copper absorption → secondary copper
    deficiency → anemia/neuropathy risk. This is a general nutritional-toxicity concern, not
    specific to VDC/IE, but relevant in a patient already at nutritional risk post-chemo.
  Citation: no DrugBank or NCCN Integrative Medicine interaction flagged between zinc (at
    deficiency-correction doses) and vincristine/doxorubicin/cyclophosphamide/ifosfamide/
    etoposide; zinc-copper antagonism at excess intake is well-documented general nutrition
    pharmacology (NIH ODS zinc fact sheet — general reference, not live-fetched this session).
```

### Omega-3 EPA/DHA and microbiome-relevant fiber — brief cross-reference

Per the cross-vector compound table and `microbiome-immune.md`'s scope, omega-3 EPA/DHA and
dietary fiber/microbiome diversity both have *Mechanistic*/*Dietary-Observational* relevance to
NK/anti-tumor immune activation broadly, but I do not re-derive that content here — it belongs to
`microbiome-immune.md` (fiber/SCFA/microbiome) and the cross-vector table (omega-3). I note only
that the patient's fresh-juice regimen (celery, ginger, carrot, broccoli, apple, beetroot) provides
fiber and phytochemical diversity potentially relevant to microbiome-mediated immune tone, but
**this is `microbiome-immune.md`'s analysis to make, not mine** — flagged here only as a
cross-reference so the V4 lead does not need two specialists independently scoring the same juice.

---

## CLINICAL TRACK
### (Clinical / Experimental — not naturally achievable; for awareness only.)

### IL-15 / IL-15-superagonist pipeline

IL-15 is the dominant homeostatic cytokine for NK cell survival, proliferation, and cytotoxic
maturation — and, unlike IL-2, does **not** preferentially expand regulatory T-cells (Tregs lack
the high-affinity IL-15 signaling that drives their IL-2-mediated expansion), making IL-15-axis
agents mechanistically attractive for NK-directed strategies without the immunosuppressive Treg
cost of IL-2.

| Agent | Class | Status (live-checked this session) | Trial ID(s) | Notes |
|---|---|---|---|---|
| **N-803 (nogapendekin alfa inbakicept-pmln, "Anktiva")** | IL-15 superagonist (IL-15N72D:IL-15Rα-Fc fusion) | **FDA-approved** (BCG-unresponsive non-muscle-invasive bladder cancer, in combination with BCG — QUILT-3.032 registrational trial, published NEJM Evidence) [VERIFY exact approval date/label scope before relying on it; ImmunityBio press materials and NEJM Evidence publication confirm the bladder-cancer approval and trial]. **Solid-tumor program active**: a Phase 3 trial of nogapendekin alfa + tislelizumab vs. docetaxel in second-line NSCLC was reported active as of early 2026; broader solid-tumor and checkpoint-refractory-NSCLC investigation ongoing (Targeted Oncology, accessed this session). | Bladder: registrational trial underlying Anktiva approval; NSCLC: Phase 3 (tislelizumab combination) per 2026 reporting | **CIC-DUX4-specific data: none. Sarcoma-specific trials: none identified this session.** Mechanism (NK/CD8 expansion without Treg expansion) is fusion-agnostic. |
| **ALT-803 (precursor to N-803)** | IL-15 superagonist | Phase I/II historical data published (now superseded by N-803/Anktiva in development) | Historical (e.g. NCT01946789-class trials) | Evidence tier: Clinical-Trial (historical); largely subsumed by N-803 program. |
| **Recombinant IL-15 (native cytokine)** | Native cytokine | Early-phase dose-finding historically limited by systemic toxicity (capillary leak-like effects at higher doses) | Historical Phase I dose-finding | Evidence tier: Clinical-Trial; toxicity profile is why superagonist fusion formats (N-803) were developed. |

Tier (whole IL-15 entry): **Established** (N-803/Anktiva — bladder cancer indication) /
**Clinical-Trial** (solid-tumor/NSCLC program). Evidence in CIC-DUX4 specifically: **None direct.**
Fusion tag: **FUSION-AGNOSTIC** — IL-15 expands NK (and CD8) cells regardless of the tumor's
fusion status; applies to the ~5% fusion-unconfirmed subgroup.

**[VERIFY] note:** the bladder-cancer approval and NSCLC Phase 3 status above were checked via
WebSearch this session (ImmunityBio press release re: NEJM Evidence QUILT-3.032 publication;
Targeted Oncology reporting on checkrpoint-refractory NSCLC, accessed 2026-06-14) but I did not
independently confirm against the FDA label database or ClinicalTrials.gov directly — **re-verify
against `docs/09-verification-sources.md` registries before any external use**, per the perishable-
status rule.

### NK engager bispecifics

NK engager constructs (NKCEs, BiKEs, TriKEs) link an NK-activating receptor (typically CD16A/FcγRIIIa,
sometimes NKG2D or NKp46) to a tumor-associated surface antigen, forcing an immune synapse between
NK cell and tumor cell independent of KIR/MHC-I status.

| Agent | Format | Target (NK side / tumor side) | Status (live-checked this session) | Notes |
|---|---|---|---|---|
| **AFM13 (acimtamig)** | Tetravalent CD30/CD16A bispecific NK engager | CD30 (tumor) / CD16A (NK) | **Active development, but in hematologic malignancies (CD30+ lymphomas — Hodgkin lymphoma, peripheral T-cell lymphoma), not solid tumors.** A 2025 Nature Medicine paper reported a Phase 1 trial of allogeneic NK cells pre-complexed with AFM13 in refractory/relapsed lymphoma (92.9% ORR, 66.7% CR in 42 patients); a Phase II acimtamig monotherapy study in CD30+ PTCL was published January 2025. No solid-tumor program identified this session. | CD30/CD16A target is **not relevant to CIC-DUX4** (CD30 is a lymphoma marker, not described as overexpressed in CIC-DUX4 sarcoma). Included for pipeline-landscape completeness only. |
| **GPC2-directed NK/T-cell engagers** | NKG2D- or CD3-based engager constructs | GPC2 (tumor) | Preclinical; GPC2 is overexpressed in some pediatric fusion-driven/neuroendocrine tumors (e.g., neuroblastoma, some Ewing-family contexts) | CIC-DUX4 GPC2 expression: **unconfirmed**. No published CIC-DUX4-specific construct. |

**Key gap, stated plainly:** **no NK engager bispecific in active development targets an antigen
specifically associated with CIC-DUX4.** ETV4/ETV5 (the hallmark CIC-DUX4 transcriptional targets)
are intracellular transcription factors — not accessible to a surface-binding bispecific. A
CIC-DUX4-relevant surface antigen for NK-engager targeting has not been catalogued in the
literature surveyed here.

Tier: **Clinical-Trial** (AFM13, in lymphoma — different indication/target) / **Preclinical**
(GPC2 constructs). Evidence in CIC-DUX4 specifically: **None direct.** Fusion tag:
**FUSION-AGNOSTIC for any construct that does not target the CIC-DUX4 junction peptide itself**
(none currently do, in either direction — no junction-targeted NK engager exists, but also no
non-junction CIC-DUX4-relevant NK engager exists).

### Adoptive NK cell transfer

- Haploidentical/allogeneic NK cell infusion (often cord-blood-derived, sometimes cytokine-
  pre-activated) has an established track record in hematologic malignancies, increasingly paired
  with bispecific engagers (see AFM13 above) or IL-15-axis support for persistence.
- "Memory-like" or adaptive NK cells (NKG2C+ subsets) are a distinct, more persistent NK population
  under active clinical investigation.
- **No published CIC-DUX4-specific adoptive NK data.**
- Tier: **Clinical-Trial** (hematologic malignancies, increasingly solid-tumor pilot studies) /
  **Preclinical** (solid tumors broadly). Evidence in CIC-DUX4 specifically: **None direct.**

**Relevance to this patient's imminent high-dose ifosfamide:** lymphodepleting chemotherapy
creates a transient "immunological space" — reduced competition for homeostatic cytokines (IL-15,
IL-7) — that is the rationale behind lymphodepletion-preconditioning for adoptive cell therapies
generally (an Established principle in the CAR-T/TIL literature, though that specific application
to NK cells in this patient's context is **Theoretical**). The post-ifosfamide NK-reconstitution
window is therefore mechanistically the most plausible point at which **any** future NK-supportive
intervention (IL-15-axis support in particular) would have the clearest rationale — see Forward
Hypothesis 2.

Fusion tag: **FUSION-AGNOSTIC.**

---

## FORWARD HYPOTHESES

**[Forward Hypothesis 1] NK-first deficiency-correction window: time vitamin D3/zinc-status
assessment and correction (if indicated) to precede, not follow, any future MHC-I-restoring
epigenetic intervention.**

*Hypothesis:* If a documented vitamin D3 or zinc deficiency exists in this patient (currently
unknown — see "What I Could Not Establish"), correcting it would have its clearest NK-functional
rationale **while the tumor remains in its native MHC-I-low state** — i.e., before any HDACi/DNMTi-
based MHC-I-restoration strategy (V3→V4 bridge) is introduced. This is not because deficiency
correction is harmful after MHC-I restoration, but because the *marginal value* of an NK-functional
boost is plausibly higher when the tumor is maximally NK-visible (missing-self signal intact) than
after MHC-I restoration shifts the tumor toward T-cell visibility and (per Forward Hypothesis 3 of
`immune-watchdog-expansion.md`) potentially raises HLA-E/NKG2A inhibition of the NK arm.

*Mechanistic basis:* NK missing-self logic (this document, "Central Framing Concept"); the
NK-first sequencing position (this document, "Sequencing Tension"); VDR→NK cytotoxic-receptor
signaling (vitamin D3 entry above); zinc-dependent NK maturation (zinc entry above).

*What experiment/study design would test it:* a CIC-DUX4 (or fusion-driven-sarcoma-surrogate) PDX
or NK-humanized model with arms = (a) vitamin-D/zinc-replete host + no epigenetic priming, (b)
vitamin-D/zinc-deficient host + no priming, (c) deficient host corrected-before-priming, (d)
deficient host corrected-after-priming; readouts = NK infiltration/cytotoxicity against tumor
cells at each MHC-I state (serial flow for HLA-A,B,C, HLA-E, MICA/MICB/ULBP, tumor volume). *Why
untested:* requires both a CIC-DUX4 model system (does not exist) and controlled micronutrient-
status manipulation in that model — a combination not attempted in any fusion-sarcoma context to
my knowledge.

**[Forward Hypothesis 2] Post-high-dose-ifosfamide NK reconstitution kinetics, gated by IL-15-axis
support, as a determinant of oligometastatic-relapse control in this patient's specific treatment
sequence.**

*Hypothesis:* Following high-dose ifosfamide-induced lymphodepletion, NK cells reconstitute from
bone-marrow progenitors in an IL-15-dependent manner. The *quality* of that reconstitution
(absolute NK count, NKG2D/DNAM-1 receptor density, KIR/NKG2A repertoire) at the reconstitution
nadir-to-recovery window predicts whether the post-ifosfamide host can mount NK-mediated
surveillance against the residual oligometastatic lung lesion — and IL-15-superagonist support
(N-803-class, Established in bladder cancer, Clinical-Trial in solid tumors per this session's
verification) timed to this window could be tested as a reconstitution-quality booster specifically
in the **lymphodepletion-to-NK-recovery interval**, rather than as a generic "more NK cells"
intervention.

*Mechanistic basis:* IL-15 is the principal driver of post-lymphodepletion NK reconstitution
(established in the hematopoietic-transplant NK-reconstitution literature broadly); N-803/Anktiva
is an IL-15 superagonist with an existing solid-tumor safety/efficacy dataset (this session's
verification); the oligometastatic, single-lung-cluster presentation is a favorable setting for a
surveillance-dependent (rather than bulk-cytoreduction-dependent) immune mechanism to matter.

*What experiment/study design would test it:* a prospective cohort design (not specific to this
patient — a study design proposal) measuring NK absolute count, NKG2D/DNAM-1 expression density,
and KIR/NKG2A repertoire at baseline, and at days 14/28/42/90 post-high-dose-ifosfamide in
oligometastatic sarcoma patients; a parallel arm receiving IL-15-superagonist support timed to the
reconstitution window vs. observation, with radiologic response of residual oligometastatic
lesions as the endpoint, and serial tumor-marker (if accessible) HLA-A,B,C/HLA-E/MICA-MICB/ULBP
profiling to test whether NK-reconstitution quality correlates with control specifically in
MHC-I-low lesions. *Why untested:* no dedicated NK-reconstitution study following high-dose
ifosfamide exists in sarcoma; the IL-15-axis-timed-to-reconstitution framing is novel even in
better-studied tumor types.

---

## ATYPICAL-CASE NOTES (~5% fusion-unconfirmed subgroup)

**This is one of the most robust entries in the entire V4 vector for this patient precisely
because none of it depends on the CIC-DUX4 fusion junction.**

- **NK missing-self/KIR/NKG2D-ligand biology:** triggered by the *general* tumor phenotype
  (MHC-I-low + stress-ligand-positive), not by the presence of any specific fusion protein or
  junction peptide. Fully applicable whether or not a CIC-DUX4 (or CIC-NUTM1/CIC-FOXO4) fusion is
  ultimately confirmed.
- **Vitamin D3/zinc deficiency-correction:** supports NK function via host-side VDR/zinc-cofactor
  biology, entirely independent of tumor genotype. Fully applicable.
- **IL-15/IL-15-superagonist pipeline (N-803/Anktiva):** expands NK (and CD8) cells via host
  cytokine-receptor biology; mechanism does not require any tumor antigen, let alone a
  fusion-junction antigen. Fully applicable.
- **NK engager bispecifics (AFM13-class) and adoptive NK transfer:** as currently constituted,
  none of the surveyed agents target a CIC-DUX4-junction epitope (AFM13 targets CD30, a lymphoma
  marker, not a CIC-DUX4-associated antigen) — so fusion status is simply **not a gating variable**
  for this entire category, in either direction.
- **The NK-first sequencing position:** depends only on the MHC-I-low/HLA-E/nectin-axis state of
  the tumor cells, which (per `immune-watchdog-expansion.md`'s atypical-case note) is a general
  tumor-immune-evasion phenotype, not a fusion-junction-specific one.

**Net:** every entry in this report remains **fully applicable** to the ~5% fusion-unconfirmed
subgroup, including this patient. The only V4 entries that are fusion-*dependent* are the
junction-specific neoantigen-vaccine/CAR-T/TCR-T constructs covered in `neoantigen-vaccine.md` and
`v4-summary.md` — none of which this report adds to or depends on.

---

## WHAT I COULD NOT ESTABLISH

### Red-team self-challenge (ADR-0017, one pass)

- **Load-bearing assumption:** the entire "MHC-I-low → NK-visible paradox" spine rests on CIC-DUX4
  cells (a) actually being MHC-I-low *in vivo* in this patient (carried over from V3's premise,
  itself unconfirmed in CIC-DUX4) **and** (b) co-expressing NKG2D/DNAM-1 activating ligands. If
  either is false — e.g., if CIC-DUX4 cells are MHC-I-low *and* stress-ligand-low/-negative (a
  "doubly cold" phenotype, immunologically invisible to both T-cells and NK cells) — the entire
  NK-first argument collapses to "NK cells have no purchase here at all," not merely "wrong
  sequencing."
- **Disconfirmation search:** I looked for, and did not find, any published NK-killing or
  NKG2D/DNAM-1-ligand profiling data in CIC-DUX4 cell lines (DepMap/Cellosaurus-style screens were
  not re-run for this report — that was Sim 2's scope, not mine). The strongest *general* caution
  against the missing-self argument is that many MHC-I-low tumors are *also* poorly NK-infiltrated
  in practice — MHC-I loss does not guarantee NK ligand co-expression, and "doubly cold" tumors
  are a recognized failure mode in tumor immunology broadly (not CIC-DUX4-specific; no single PMID
  asserted here).
- **Alternative hypothesis outside this lane:** if CIC-DUX4 cells turn out to be "doubly cold"
  (MHC-I-low, NKG2D/DNAM-1-ligand-low), the higher-leverage V4 lever would shift entirely toward
  the **danger-signaling/ICD axis** (`immune-watchdog-expansion.md` module A) — i.e., *inducing*
  stress-ligand expression and DAMP release (e.g., via the patient's own doxorubicin) rather than
  relying on a pre-existing missing-self signal. That mechanism already exists in this V4 vector
  (module A, Forward Hypothesis 2 of `immune-watchdog-expansion.md`) — it does not require a new
  vector, but it would become the *primary* route rather than a complementary one if (b) above is
  false.
- **Flip test:** if assumption (b) (activating-ligand co-expression) is wrong, this report's
  central framing concept and both sequencing-position arguments (NK-first, deficiency-correction
  timing) lose their mechanistic floor — they would need to be reframed around *inducing*
  ligand expression (ICD/danger-signaling) rather than *exploiting* a pre-existing missing-self
  state. **I am tagging the central framing concept and the NK-first sequencing position as
  contingent on unmeasured CIC-DUX4 stress-ligand expression** (item 2 below) — this is the same
  gap `v4-summary.md` and `immune-watchdog-expansion.md` already flag, carried forward here as a
  load-bearing rather than peripheral uncertainty.
- **Steer audit:** the assignment brief asked me to build this report's spine around the
  MHC-I-low/NK-visible paradox as "arguably the strongest single mechanistic lever in this whole
  vector." I have done so because the *logic* of the argument is sound and well-established
  immunology — but I have not treated the steer as itself evidence that CIC-DUX4 cells display
  this phenotype. The paradox is real *immunology*; whether it applies to *this tumor* remains
  Mechanistic/inferred, and I have tagged it as such throughout rather than upgrading it to
  Preclinical on the strength of the framing alone.

### Remaining gaps

1. **This patient's actual vitamin D3 and zinc status (25(OH)D, serum zinc).** Neither value is
   recorded in the case as presented. This is the single largest gap in this report — it is the
   difference between "this self-administered vitamin D3 is correcting a real deficiency with a
   clear NK-functional rationale" and "this is supplementation in an already-replete person where
   *additional* NK benefit is not established." I cannot resolve this without the lab values;
   I have stated both possibilities honestly rather than assuming either.

2. **CIC-DUX4 stress-ligand expression (MICA/MICB, ULBP1–6, PVR/CD155, Nectin-2/CD112).** The
   missing-self argument requires *both* reduced inhibitory signal (MHC-I-low — plausible per V3)
   *and* present activating ligands. No published study has profiled NKG2D or DNAM-1 ligand
   expression on CIC-DUX4 cells. This is the same gap `v4-summary.md` (#3) and
   `immune-watchdog-expansion.md` (#2, #3) already flag — I am not resolving it, only confirming
   it remains the single largest unknown gating the entire NK-directed hypothesis.

3. **CIC-DUX4 NK-killing assay data of any kind.** Whether CIC-DUX4 cells are in fact NK-susceptible
   in vitro has, to my knowledge, never been tested. The mechanistic prediction (missing-self →
   NK-susceptible) is strong; direct confirmation is absent.

4. **HLA-E baseline and its response to any future MHC-I-restoring intervention in CIC-DUX4** — the
   crux of `immune-watchdog-expansion.md` Forward Hypothesis 3 and central to whether the
   "MHC-I-low window" for NK-first strategies is a true window (closes only when MHC-I is restored)
   or a narrower one (HLA-E already high, NK arm already checked by NKG2A regardless of timing).
   Entirely unknown for CIC-DUX4.

5. **This patient's current NK compartment status** (absolute count, NKG2D/DNAM-1 density, KIR/
   NKG2A repertoire) following VDC/IE ×14, surgery, and whole-lung irradiation, and how high-dose
   ifosfamide will further perturb it. This is the #5-ranked VoI item (NK functional reserve,
   VoI 0.250) and is directly relevant to Forward Hypothesis 2's premise — unmeasured.

6. **Whether AFM13 or any other CD16A-based NK engager has ever been evaluated in any sarcoma
   subtype** — the active development I found this session is exclusively in CD30+ hematologic
   malignancies; I did not find a solid-tumor or sarcoma program for this specific construct.

7. **Exact FDA label scope and current recruitment status for N-803/Anktiva's solid-tumor/NSCLC
   programs** — checked via WebSearch this session (ImmunityBio press materials, Targeted Oncology
   reporting) but **not independently verified against the FDA label database or
   ClinicalTrials.gov directly**; tagged `[VERIFY]` per the perishable-status rule
   (`docs/09-verification-sources.md`) and must be re-checked before any external use.

8. **Omega-3 EPA/DHA NK effects in cancer patients specifically (vs. healthy volunteers)** — noted
   as a cross-reference to `microbiome-immune.md`/the cross-vector table, but I did not
   independently verify this; flagged so the V4 lead does not double-count an unverified claim
   across two sub-agent files.

---

*Grounding (`--team v4-nk`, see `nk-cell-activation.grounding.tsv`): all core NK/immune
gene-and-protein entities were recognized — NK cells, KIR, NKG2D, MICA, MICB, ULBP, DNAM-1, CD226,
PVR, CD155, Nectin-2, CD112, NKG2A, HLA-E, HLA-A, HLA-B, HLA-C, B2M, TAP1, TAP2, VDR, IL-15, AFM13,
acimtamig, CD30, CD16A, GPC2, EZH2, HDAC, DNMT. **Not recognized** by this protein/anatomy-oriented
model set (expected — they are drug brand names, dietary compounds, or disease names outside its
vocabulary, not a grounding failure of the underlying concepts): vitamin D3, zinc, N-803/
nogapendekin alfa/Anktiva, tazemetostat, monalizumab, CIC-DUX4, and the chemotherapy agent names
(ifosfamide, vincristine, doxorubicin, cyclophosphamide, etoposide). Grounding confirms entity
recognition only — it is not fact-checking; status/approval claims were checked separately via
WebSearch and tagged `[VERIFY]` where not independently confirmed against `docs/09-verification-
sources.md` registries.*

*Reuse note: this artifact is the v3 (clean-slate) NK Cell Specialist output, written fresh per
the v3 run's instructions. It is informed by, and explicitly extends/adopts positions from,
`v4-immune-watchdog/nk-cell-activation.md` (baseline), `v4-immune-watchdog/immune-watchdog-
expansion.md` (ADR-0006), `v3-hot-patching/v3-summary-v3.md` (MHC-I bridge), and
`biomarker-voi-stratification.md` (Sim 6 VoI ranking) — all cited inline above. Research-simulation
output, not medical advice.*
