# The Mitochondrial / Endosymbiotic Layer — the Cell's Bacterial Legacy as Alarm, Commons, and Reservoir

> **Origin:** user question, 2026-09-17 — *"What if we approach sarcoma from a mitochondria angle? Treat it
> as rogue bacteria, considering a theory that the human body is mitochondria that started off as bacteria
> but ended up as an organism where these coordinate for a greater system and its wellbeing. And sarcoma
> being the outlier, trying to hoard resources for itself. Any ideas how sarcoma can be tackled long term
> after NED?"* — with the explicit rider that **NED ≠ absence of tumour cells** (dormant, or below CT
> resolution).
>
> **Status:** cross-cutting **metabolic/organelle layer**. **Not a fifth vector** (golden rule #8) — it
> supplies new mechanism to **V4** (danger signalling + immune metabolic fitness), re-weights **V1**
> (a reservoir-directed throttle rather than a bulk one), and extends the **persister/reservoir** spine of
> `chemosensitivity-ddr-cellstate-layer.md` (ADR-0021). Placed on the **modality axis** (ADR-0018) mostly at
> **M1** (systemic small-molecule) and **M8** (dietary/host-directed), with one **M3** read (cell-therapy
> manufacturing).
>
> **Research simulation / hypothesis generation only. NOT medical advice, NOT a diagnosis, NOT a testing or
> treatment recommendation. No dosing, no start/stop instructions for any therapy — including supplements.**
>
> **⚠ Verification status (ADR-0020).** Full-text literature egress is **blocked in this environment**
> (`pubmed.ncbi.nlm.nih.gov`, `pmc.ncbi.nlm.nih.gov`, `nature.com`, `ebi.ac.uk`, NCBI E-utilities and
> `clinicaltrials.gov` all refused CONNECT with **HTTP 403** on 2026-09-17; WebFetch returned
> `EGRESS_BLOCKED`). **Search-snippet/abstract level only.** Every citation below carries **`[VERIFY]`** and
> identifiers are reported as they appeared in search results — *not* as records I opened. Under ADR-0020's
> mandatory gate **nothing here may enter a `protocol-vN.md` until full-text-verified.** This is a
> **forward-lane** document. Trial/regulatory statuses are **perishable and unverified this session**.

---

## 1. One-paragraph answer

The framing is **productive, and it is aimed at the right compartment** — but it needs one correction to
become mechanistically usable, and it carries its own built-in warning. The correction: mitochondria are not
the rogue agent. They are *conscripted infrastructure*; the defection happens at the **multicellular** level
(the "cheater cell"), and the tumour then **renegotiates** its endosymbiotic bargain to serve that defection.
That renegotiation is what creates real, named targets — and it opens **three** surfaces, not one:
(**A**) the mitochondrion still carries **bacterial-pattern alarm molecules** (mtDNA, formyl peptides,
cardiolipin, mtdsRNA) that the innate immune system reads as infection — the tumour must actively silence
them; (**B**) the **resource commons** is real and the "hoarding" intuition is literally correct — tumours
impose a metabolic siege on T and NK cells; (**C**) mitochondria are **physically trafficked between cells**,
and in 2025 this was shown to run *outward* — tumours push defective mitochondria into T cells and
homoplasmically replace theirs, causing senescence. The built-in warning is the important part: because
mitochondria *are* the shared infrastructure, attacking them as a class hits the most OXPHOS-dependent
cooperators — neurons, heart, muscle — first. That is not a metaphor; it is the documented reason the
best-in-class complex-I inhibitor **IACS-010759 was discontinued** (neurotoxicity + lactic acidosis, no RP2D),
and why adjuvant **metformin was negative in MA.32** (n=3,649) in precisely the post-treatment,
recurrence-prevention setting this question is about. **So the honest conclusion inverts the intuitive move:
in this case the mitochondrion is a far better alarm than it is a target.** For the specific post-NED
question, the single best-specified new hypothesis the framing yields is a **node swap** — the surviving
reservoir's apoptotic dependency looks like **BCL-XL, not MCL1** — which is both falsifiable and a direct
correction to the catalog's demoted headline target.

---

## 2. Translating the theory honestly (what is right, what needs fixing)

Golden rule #3 requires mechanism, not analogy. So, first: what in the user's framing is established
biology, and what is the analogy doing work it hasn't earned?

| Element of the framing | Verdict | Basis |
|---|---|---|
| Mitochondria descend from a bacterial (alphaproteobacterial-like) endosymbiont | **Correct** | `Established` — endosymbiotic theory |
| Mitochondria retain bacterial-type molecular patterns that the innate immune system reads as danger | **Correct, and load-bearing** | `Established`/`Mechanistic` — "due to mitochondrial bacterial ancestry, mitochondria harbor a large number of DAMPs" `[VERIFY]` (see §4A) |
| Cells/organelles cooperate for organism-level function, and cancer is a defection from that cooperation | **Correct — and it is a formal research program**, not just a metaphor | `Established` (conceptual) — cancer as "the ultimate form of cellular cheating"; cheating across proliferation inhibition, cell death, division of labour, **resource allocation**, and extracellular-environment maintenance. Aktipis et al., "Cancer across the tree of life: cooperation and cheating in multicellularity," *Phil Trans R Soc B* 2015, DOI 10.1098/rstb.2014.0219 `[author list not captured beyond first author]` `[VERIFY]` |
| The tumour "hoards resources for itself" | **Correct, and more literal than expected** | `Preclinical-Animal`/`Mechanistic` — nutrient competition imposes a "metabolic siege" on T cells (§4B) |
| **"The human body *is* mitochondria"** | **Needs fixing** | Mitochondria are organelles *within* eukaryotic cells. There are **two nested cooperative levels**, and conflating them is what makes the analogy mis-predict. |
| **"Sarcoma = rogue bacteria / rogue mitochondria"** | **Needs fixing — and this is the productive correction** | The tumour's genome is **nuclear**. Its mitochondria are largely *loyal, conscripted infrastructure*. The rogue agent is the cell, not the organelle. |

### 2.1 The two-level correction, and why it matters

- **Level 1 — the endosymbiotic bargain (inside a cell):** nucleus ↔ mitochondrion. Ancient, and largely
  *intact* in tumour cells. Mitochondria still run OXPHOS, still gate apoptosis, still hold their own
  genome.
- **Level 2 — the multicellular social contract (between cells):** proliferation restraint, programmed
  death on demand, division of labour, fair resource use. **This is where cancer defects.**

The tumour defects at Level 2. But to *sustain* that defection it must **renegotiate Level 1** in three
specific ways — and each renegotiation is a target:

| The tumour needs its mitochondria to… | Because | Surface |
|---|---|---|
| **stop reporting** (suppress mtDNA/DAMP release and downstream IFN) | a cell breaking the Level-2 contract looks like an infected cell to innate immunity | **§4A — the alarm** |
| **out-compete neighbours for fuel** | Level-2 defection *is* unfair resource allocation | **§4B — the commons** |
| **be exportable / importable** | metabolic plasticity, and disabling the enforcers | **§4C — the trafficking channel** |

**This is the layer's central claim:** the endosymbiotic framing earns its place not by making mitochondria
the enemy, but by identifying that a defecting cell has to **silence an ancient alarm it cannot delete** —
and an alarm you cannot delete is a therapeutic opportunity.

### 2.2 The framing's self-imposed limit (please read before §4)

If mitochondria are the **shared cooperative infrastructure**, then any therapy that attacks mitochondria
*as a class* is an attack on the commons, and it will hit the **most** OXPHOS-dependent cooperators hardest.
Neurons, cardiomyocytes and skeletal muscle are more OXPHOS-dependent than most tumour cells are.

**The analogy therefore predicts its own principal clinical failure mode — and that failure is on record.**
See §3. Take §3 as the price of admission for §4.

---

## 3. The reality check first: what has already been tried and what happened

Golden rule #5 says known research is the floor, not the ceiling — *and* that we must ask **why** things
failed. Two hard negatives govern this whole area and both land squarely in the setting the question asks
about.

### 3.1 Systemic complex-I inhibition — discontinued for mechanism-based toxicity

**IACS-010759**, a potent selective mitochondrial complex-I inhibitor, entered two phase-1 dose-escalation
trials — relapsed/refractory AML (**NCT02882321**, n=17) and advanced solid tumours (**NCT03291938**, n=23).
Outcome: **narrow therapeutic index; dose-limiting elevated blood lactate and neurotoxicity; no RP2D
established; only modest target inhibition and limited antitumour activity at tolerated doses; both trials
discontinued.** Reverse-translational work in mice showed peripheral neuropathy, reduced neuronal oxygen
consumption and **myelin damage**, partly mitigated by an HDAC6 inhibitor. The authors' own conclusion urged
**caution in continued development of complex-I inhibitors as antitumour agents.**
*Nature Medicine* 2022, DOI 10.1038/s41591-022-02103-8, **PMID 36658425** `[Clinical-Trial, VERIFY]`

**Attrition-reason classification (ADR-0013):** this is **R2 (trial-fail) on *toxicity / therapeutic index*,
not on target invalidation (R1).** The distinction matters and cuts both ways:
- It does **not** refute OXPHOS dependence as tumour biology.
- It **does** refute *systemic catalytic complex-I blockade* as the delivery strategy, on a
  mechanism-based — i.e. not formulation-fixable — basis.

**Feasibility: F4** (discontinued) for this agent; **F3/F5** for the class in this disease. `[re-verify]`

### 3.2 Adjuvant metformin — negative in the exact setting of this question

**MA.32** randomised **3,649** patients with high-risk non-metastatic breast cancer to adjuvant metformin vs
placebo on top of standard therapy (2010–2013, follow-up to Oct 2020). Metformin **did not improve invasive
disease-free survival, distant recurrence-free survival, or overall survival** (HR 1.01, 95% CI 0.84–1.21,
P=.93 in ER/PR-positive disease). An exploratory HER2-positive signal (SNP rs11212617 C-allele) is
hypothesis-generating only. *JAMA* 2022, **PMID 35608580**; secondary analyses *JCO* 2023 `[Clinical-Trial, VERIFY]`

**Why it failed, mechanistically (golden rule #5, and #6):**
1. **Concentration mismatch — the decisive one.** Metformin's complex-I inhibition is demonstrated in vitro
   at **millimolar** concentrations; therapeutic plasma exposure is **low micromolar**. The "mitochondrial"
   mechanism is largely **not operating at achievable human exposure**. This is the canonical golden-rule-#6
   failure. `[Mechanistic, VERIFY]`
2. **Unselected population** — no metabolic or OXPHOS biomarker was used to enrich.
3. **Wrong tumour type for transfer here** — breast, not sarcoma (**P3** on the ADR-0014 ladder).

**Honest consequence for this case:** metformin is the single most-reached-for "mitochondrial" adjuvant, it
was tested properly in the recurrence-prevention setting, and it was negative. Under ADR-0013 this is **R2
with a biomarker-unenriched design**, so it does not fully invalidate the *biology* — but it decisively
removes "take metformin to starve the dormant cells" from the evidence-backed column. **F1** (accessible)
but with **negative phase-3 adjuvant evidence** — which is a worse position than merely unproven.

### 3.3 The one caution that runs the *other* way — autophagy inhibition may **awaken** dormancy

Dormant disseminated tumour cells use **autophagy/mitophagy** to recycle nutrients and survive. The intuitive
move is therefore to inhibit autophagy (hydroxychloroquine/chloroquine are the accessible agents, and are
popular in exactly this "long-term after NED" conversation).

**But the dormancy literature reports the opposite effect on the outcome that matters here:** autophagy
inhibition **elicited emergence from metastatic dormancy** by inducing and stabilising **Pfkfb3** expression;
targeted depletion of autophagy genes **reactivated** dormant breast cancer stem cells and drove outgrowth.
PMC6694140 `[Preclinical-Animal, VERIFY]`

> **This is a genuine "the popular adjunct may be actively wrong-signed in the NED setting" finding**, and the
> symmetric lane (ADR-0020) requires stating it. Dormancy-directed intervention is **not** a monotonic
> "suppress metabolism harder" problem — awakening a dormant reservoir in a patient whose disease is
> currently undetectable is a real, directional risk. `[Preclinical-Animal — no human data, and none in sarcoma]`

---

## 4. The three surfaces the framing actually opens

### 4A — The alarm the endosymbiont still carries (the strongest contribution; a V4 lever)

This is where the user's "started off as bacteria" framing stops being an analogy and becomes the mechanism.

Because of their bacterial ancestry, mitochondria carry molecules that the innate immune system evolved to
read as **infection**: **mtDNA** (circular, CpG-rich, hypomethylated), **N-formyl peptides**, **cardiolipin**,
and **mitochondrial double-stranded RNA**. When mtDNA escapes into the cytosol — under genomic instability,
metabolic stress, or **therapy-induced damage** — it is sensed by **cGAS–STING** (also TLR9, NLRP3), driving
**type-I interferon**, dendritic-cell maturation, T-cell infiltration and immunogenic cell death.
`[Established`(the sensing)`/ Mechanistic`(the tumour application)`, VERIFY]`
*Sources (snippet-level):* Exp Mol Med 2023, DOI 10.1038/s12276-023-00965-7; PMC10687031; PMC8873532.

**Why this matters more than it looks:** the framework already has an entire layer devoted to *manufacturing*
danger signals — the oncolytic-virotherapy M4 deep-dive (ADR-0019), whose honest conclusion was
`Theoretical` for this tumour, low Ewing/round-cell OV susceptibility, and access bounded by deep visceral
anatomy. **§4A describes the same objective with an endogenous generator instead of a viral one.** Mitochondrial
DAMP release is:
- **fusion-agnostic** → applies to the ~5% (golden rule #9);
- **not delivery-limited by anatomy** — no injectable lesion required, unlike intratumoral OV;
- **already partially engaged in this patient** — prior whole-lung irradiation and DNA-damaging chemotherapy
  are both documented mtDNA-release/STING-priming stimuli, which fits ADR-0021's existing MRD-window argument.

**And there is a specific, elegant twist in the data.** Two independent lines suggest the productive
perturbation is **structural/redox, not catalytic starvation**:
- Truncating mutations in the mtDNA complex-I gene **Mt-Nd5** produce a Warburg-like shift that **consistently
  elicits an anti-tumour immune response**, and sensitised tumours to checkpoint blockade in a
  **neutrophil-dependent** manner. Critically: partial complex-I loss **disrupted redox balance without
  significantly impacting energy homeostasis, oxygen consumption or proliferation** — and *inducing redox
  imbalance alone* was sufficient to reproduce the effect in mtDNA-wild-type tumours.
  *Nature Cancer* 2023, DOI 10.1038/s43018-023-00721-w / PMC11056318 `[Preclinical-Animal, VERIFY]`
- Patient lesions with **>50% mtDNA-mutation heteroplasmy** showed a checkpoint-blockade response rate
  **~2.5× higher** than mtDNA-wild-type. `[Clinical-correlative, VERIFY]`
- Independently: *selectively* affecting complex-I **structure**, rather than broadly inhibiting its
  **catalytic activity**, promoted anti-tumour immunity. (bioRxiv preprint — `Preclinical-Cell`, **preprint,
  lowest weight**) `[VERIFY]`

> **Headline reframe:** don't try to *starve* the endosymbiont (§3.1 says that fails on the commons). Try to
> make it **sound the alarm**. Catalytic OXPHOS blockade and redox/structural perturbation are **not the same
> intervention**, they have opposite toxicity profiles, and the immune payoff tracks the second one.

**Transferability (ADR-0014): P3** (solid tumour with a named mechanism) — melanoma/mouse models, **no
sarcoma and no round-cell data**. **Tier: `Preclinical-Animal` for the biology, `Theoretical` for this
tumour.** **Feasibility: F5/F3** — there is no clinical-stage agent whose mechanism is "selective
mitochondrial redox perturbation to trip cGAS-STING"; STING agonists exist but are a different (and largely
disappointing) intervention, and are **not** claimed here as a verified path. `[re-verify]`

### 4B — The resource commons: "hoarding" is literally correct (a V4 lever, and a host-biology one)

The user's intuition maps onto an established mechanism with almost no translation loss.

Tumour cells and effector lymphocytes have **overlapping metabolic profiles** and therefore compete directly
for **glucose and glutamine** in the microenvironment. The consequences for immunity are named:
- **Glucose restriction** suppresses the **mTOR–HIF-1α** axis in T cells, reducing glycolytic flux and
  **weakening IFN-γ production and cytolytic function**. `[Preclinical-Animal/Cell, VERIFY]`
- Depletion of glucose plus glutamine, arginine and methionine imposes a **"metabolic siege"** on T cells.
  `[Mechanistic, VERIFY]` (PMC4864363; PMC10776347; and *eLife* "The tumor microenvironment as a metabolic
  barrier to effector T cells and immunotherapy", article 55185 — `[DOI inferred from the eLife article
  number, not captured verbatim]`)
- **Lactate + acidosis** is the weapon, not just the waste: **MCT4** exports lactate and protons, acidifying
  the microenvironment; **low extracellular pH directly impairs CTL and NK cytotoxicity**; lactate stabilises
  HIF-1α and activates NF-κB toward an immunosuppressive phenotype. **MCT4 inhibition enhanced NK
  cytotoxicity** by blocking lactate flux and reversing acidification. `[Preclinical-Cell, VERIFY]` (PMC6143925)
- Terminally exhausted T cells uniquely upregulate **MCT11**; deleting it improved effector function.
  *Nat Immunol* 2024, DOI 10.1038/s41590-024-01999-3 `[Preclinical-Animal, VERIFY]`

**And the immune cell's own mitochondria are a target of the attack — this is the V4-specific find:**
tumour-infiltrating **NK cells have small, fragmented mitochondria** (vs. large tubular mitochondria in NK
cells outside the tumour), driven by hypoxia → **mTOR–Drp1** hyperactivation. Fragmentation correlates with
**reduced cytotoxicity and NK loss**, predicts poor survival, and **inhibiting fragmentation restores NK
metabolism, survival and antitumour capacity**. *Nature Immunology* 2019, DOI 10.1038/s41590-019-0511-1,
**PMID 31636463** `[Preclinical-Animal + human correlative, VERIFY]`. DRP1 depletion also protected NK cells
from hypoxia-induced dysfunction, and a **PKA–DRP1** axis preserved NK cytotoxicity under acidic stress.
`[Preclinical-Cell, VERIFY — one is a preprint]`

> **Why this is the most important §4 finding for *this* case.** The framework's standing immune
> recommendation is **NK-first** (Sims 4+5, reinforced by ADR-0021's MRD-window argument). This layer supplies
> something those files did not have: a named, mitochondrial reason NK cells **fail** in situ, plus the
> observation that **the same acidosis the tumour creates is what breaks them**. It converts "NK-first" from
> a sequencing preference into a claim with a **measurable failure mode** — NK mitochondrial morphology and
> the lesional lactate/pH environment.

**Transferability: P3** (liver cancer, other solid tumours; mechanism named) — **no sarcoma data**.
**Feasibility: F3/F5** — AZD3965 (MCT1) is clinical-stage, MCT4 inhibitors are preclinical/patent-stage,
DRP1 modulation has no clinical agent. **All `[re-verify]` — trial registries were unreachable this session,
so no status here is current.**

**One M3 (cell-therapy) corollary worth recording:** if NK effector failure is mitochondrial and
acidosis-driven, then *ex vivo* metabolic conditioning of an NK product — rather than the *in vivo*
microenvironment — is the tractable lever. That places the intervention on the **manufacturing** side, where
feasibility is governed by trial access rather than by drugging a transporter in a patient. `[Theoretical]`

### 4C — The trafficking channel: mitochondria move between cells, and it runs both ways

This is the part of the framing the user could not have known was quite so literal.

**Inbound (tumour gains fitness).** Cancer cells **acquire intact mitochondria** from stromal, endothelial and
immune cells via **tunnelling nanotubes** (Miro1/myosin-XIX-dependent), extracellular vesicles, cell fusion
and phagocytic uptake — **restoring OXPHOS, expanding metabolic plasticity, and conferring chemoresistance.**
Best-characterised in AML (bone-marrow MSC → leukaemic stem cell, boosting oxidative metabolism and
clonogenicity) and myeloma (CXCL12/CXCR4-mediated). PMC3668949; PMC6121133; and a *Trends in Cell Biology*
2025 review, "Mitochondrial transfer at the crossroads of cancer, stromal, and immune cells"
`[no DOI captured — title/journal/year only from search results]` `[Preclinical-Cell, VERIFY]`

**Outbound (tumour disables the enforcer) — the striking one.** In 2025, tumour cells were shown to transfer
**mtDNA-mutation-bearing, defective mitochondria into tumour-infiltrating lymphocytes**. The transferred
organelles **escape mitophagy** because mitophagy-inhibitory molecules are co-transferred with them, producing
**homoplasmic replacement** of the T cell's own mitochondria. The recipient T cells show **metabolic
abnormalities, senescence, and defects in effector function and memory formation**. Oxidative stress induces
the tunnelling nanotubes that carry it.
*Nature* 2025, DOI 10.1038/s41586-024-08439-0, **PMID 39843734** `[Preclinical-Cell/Animal + human TIL
sequencing, VERIFY]`

> **This is the literal version of the user's thesis** — and it is stranger than the thesis. The tumour is not
> merely hoarding; it is **exporting its damaged infrastructure into the cells sent to kill it, and
> permanently replacing their power supply.** In the endosymbiotic frame: the defector corrupts the
> enforcement mechanism by forcing a hostile endosymbiont swap.

**And it produces a genuinely new, measurable prediction for this repo.** The framework's existing immune
programme measures the **tumour's** phenotype — MHC-I, Nectins/CD155, HLA-E, NK fitness (Sims 4/6, ADR-0015).
None of those would detect this. The read here is **mtDNA-variant sharing between the tumour and its TILs** —
detectable in principle from the *same* sequencing data, because it is a variant-overlap analysis rather than
a new assay.

**Transferability: P3** (mechanism named; melanoma/other solid tumours) — **no sarcoma data**.
**Tier: `Preclinical-Cell`/`Mechanistic`.** **Feasibility: measurement F2/F3** (needs paired tumour + TIL
sequencing, i.e. fresh **P2** tissue under ADR-0011 — and a reanalysis question, not an off-the-shelf test);
**intervention F5** (no clinical agent blocks mitochondrial transfer).

---

## 5. Where the framing is best aimed: the post-NED reservoir

This is the user's actual question, and it is the part where the mitochondrial angle is **strongest** — not
because of the endosymbiotic story, but because of a convergent empirical finding.

### 5.1 The reservoir is OXPHOS-high. That is exactly the compartment NED leaves behind.

`CASE-BASELINE.md` §4 and ADR-0021 already establish that the unsolved problem is the **drug-tolerant
persister / dormant reservoir**, not the bulk (chemotherapy has cleared the bulk twice). Independently, a
consistent metabolic phenotype for that compartment has emerged across tumour types:

| Observation | Setting | Tier |
|---|---|---|
| DTP cells shift **away from glycolysis toward OXPHOS and fatty-acid oxidation**, with increased antioxidant capacity; elevated OXPHOS supports low proliferation **and limits ROS accumulation**, protecting them from oxidative death | multi-tumour review | `Preclinical-Cell`, VERIFY |
| **OXPHOS is a metabolic vulnerability of endocrine-therapy-tolerant persisters**; complex-I inhibition suppressed persister tumour-forming potential in mice and synergised with fulvestrant to regress PDXs | ER+ breast | `Preclinical-Animal`, **PMID 39777474**, VERIFY |
| Dormant disseminated tumour cells show **reduced glucose uptake but enhanced FAO and OXPHOS**, and use **autophagy/mitophagy** to meet energy demands | dormancy reviews | `Preclinical-Animal`, VERIFY |
| Reactivation is metabolically gated: **P4HA2** loss → collagen proteostasis disruption → autophagy → **ALDH4A1** proline catabolism → lowered **NAD⁺/NADH** → mitochondrial energetics → **DTC awakening** | breast DTC | `Preclinical-Animal`, PMC12265173, VERIFY |
| Persister ferroptosis is suppressed by **FSP1 and HDACs** (alongside the GPX4 axis the catalog already carries) | multi-tumour | `Preclinical-Cell`, *Sci Adv* 2025 DOI 10.1126/sciadv.aea8771, VERIFY |

**The repo already had one facet of this and did not recognise it as mitochondrial.** ADR-0021's persister row
is **GPX4-dependence / ferroptosis vulnerability** (Hangauer, *Nature* 2017, PMID 29088702). GPX4 defends
against **lipid peroxidation**, and the mitochondrion is both a principal ROS source and a key site of that
peroxidation. **The OXPHOS-high phenotype and the GPX4 dependency are two readings of one lipid-redox
vulnerability** — the persister survives by running oxidative metabolism *and* must therefore pay a
continuous antioxidant tax to do so. That unification is this layer's cleanest contribution to the existing
catalog, and it raises the prior on the (still `Low`-confidence) ferroptosis row rather than adding an
unrelated hypothesis.

### 5.2 The single best new hypothesis: the reservoir's BH3 node is **BCL-XL, not MCL1**

This is the most specified, most falsifiable, and most case-relevant item in this layer.

A genome-wide CRISPR screen in **doxorubicin-persistent, OXPHOS-high, quiescent** triple-negative breast
cancer cells identified **BCL-XL as the top survival dependency** — **in the persisters, not in their
untreated proliferating counterparts.** These quiescent cells were **highly sensitive to BCL-XL inhibitors
but *not* to BCL2 or MCL1 inhibitors.** BCL-XL inhibition rapidly collapsed mitochondrial elongation and
respiratory function, then triggered caspase-3/7 activation and death. Quiescent cells persisting after
**epirubicin or cyclophosphamide** were **also** BCL-XL-sensitive, suggesting the dependency generalises
across DNA-damaging chemotherapeutics. The platelet-sparing **BCL-XL PROTAC degrader DT2216** enhanced
doxorubicin efficacy in xenografts **without the thrombocytopenia** that limits first-generation BCL-XL
inhibitors (navitoclax).
**PMID 40909561 / PMC12524137** (also bioRxiv 2025.08.21.671546) `[Preclinical-Animal, VERIFY]`;
BCL-XL PROTAC context: *Cancer Res* 2023;83(21):3501 `[VERIFY]`

**Why this is pointed directly at this patient (and why it is a *correction*, not an addition):**

1. **The exposure history matches the model almost exactly.** This patient received **doxorubicin,
   cyclophosphamide and ifosfamide** — the model was built on doxorubicin persisters and validated on
   epirubicin and cyclophosphamide persisters.
2. **It supplies the node the catalog was missing.** `findings-ranking.md` demoted **MCL1i** twice over —
   driver-contingent (Sim 8) and phenotypically argued against (ADR-0021: apoptotic priming is intact, so
   there is no death programme needing "re-arming"), plus cardio-gated by prior anthracycline. That left the
   framework with a demotion and no replacement. **This says the BH3 node was the right idea aimed at the
   wrong protein, in the wrong compartment:** not MCL1 in the bulk, but **BCL-XL in the residual quiescent
   cells** — the compartment that actually causes relapse.
3. **It is consistent with ADR-0021 rather than in tension with it.** Intact apoptotic priming in the *bulk*
   and a specific BH3 dependency in the *reservoir* are different claims about different compartments.
4. **It is fusion-agnostic** → applies to the ~5% (golden rule #9), and needs no driver resolution.
5. **The feasibility objection has a named answer.** Navitoclax's dose-limiting **thrombocytopenia** (platelets
   are BCL-XL-dependent) is the reason this class stalled; the platelet-sparing **PROTAC degrader** route is
   the mechanistically motivated workaround — and the repo already has a **PROTAC/ASO specialist** in V3.

**Honest limits — these are large:**
- **Transferability P3→P4.** Breast (TNBC) → round-cell sarcoma. **No sarcoma persister model exists**; ADR-0021
  already noted Hangauer's panel excluded round-cell sarcoma. This is a **cross-lineage** transfer of a
  *persister-state* property, which is more defensible than a lineage-specific one but still unvalidated here.
- **The competing explanation is unexcluded and is not a minor one.** This tumour was **metastatic at
  diagnosis (12 lung nodules)**, so the relapse may be outgrowth of a **pre-existing metastatic clone**
  rather than a drug-tolerant persister state. If so, the whole persister frame — BCL-XL and ferroptosis
  alike — is the wrong model. ADR-0021 flagged this; it remains **the** load-bearing uncertainty.
- **BCL-XL inhibition is not benign.** Thrombocytopenia is on-target, and DT2216 is early-stage. `[re-verify]`
- **Tier: `Preclinical-Animal` in breast → `Theoretical` for this tumour.** **Feasibility: F3** (DT2216
  early-phase; navitoclax F3/F4) `[re-verify — registries unreachable this session]`.
- **Falsifier (stated up front):** if paired primary-vs-relapse sequencing shows a **selected genetic clone**
  with distinct driver/copy-number architecture, the persister model fails and this hypothesis dies with it.

### 5.3 The most transferable mitochondrial target under Era B: **SHMT2 / mitochondrial one-carbon metabolism**

Era B **up-weights Ewing/round-cell-family evidence** (`CASE-BASELINE.md` §5a — arguably the *closest
available* anchor, since D4 leads and the chemo phenotype independently matches this family). That makes the
following the **highest-Directness mitochondrial finding in this layer** — the only one at **P1**:

**Ewing sarcoma cells have an absolute dependence on mitochondrial one-carbon metabolism.** Genetic and
pharmacologic inhibition of **SHMT2** (the mitochondrial arm) substantially inhibits proliferation and
colony formation, via depletion of **glycine and one-carbon units required for de novo purine synthesis**;
the phenotype is **profound and prolonged growth suppression** with G1→early-S arrest. Tool/agent compounds:
**SHIN1** (SHMT1/2) and **AGF347** (multitargeted, SHMT1/2 + de novo purine biosynthesis).
*Cancer Res Commun* 2025;5(8):1298, **PMID 40698729** / PMC12332480 (also bioRxiv 2025.04.13.647987)
`[Preclinical-Cell, VERIFY]`

**Why it ranks despite being preclinical:** it is the one item here whose evidence sits at **P1** on the
ADR-0014 ladder rather than P3/P4. Under Era A it would have been discounted as "Ewing, not CIC"; under
Era B, with D4 (phenocopy/misclassified — including EWSR1::non-ETS and undifferentiated round-cell) leading
the posterior at 0.386, Ewing-family metabolic dependency is the **closest transferable mitochondrial
biology available for this case**.

**Honest limits:** `Preclinical-Cell` only (spheroids/colony formation); **no clinical agent** — SHIN1 and
AGF347 are **tool/early-preclinical compounds**, not accessible therapeutics (**F5**, possibly F4/F3 for
antifolate-adjacent chemistry) `[re-verify]`; one-carbon metabolism is **broadly essential**, so a
therapeutic window is unproven and the same commons objection from §2.2 applies. It is also a
**proliferation-directed** target — which per §5.1 aims at the **bulk**, not the reservoir. **It does not
answer the post-NED question**; it is recorded because its Directness is unusually high and Era B makes it
newly relevant.

### 5.4 Bonus: a mitochondrial-adjacent route on the framework's own SLFN11 falsifier branch

`CASE-BASELINE.md` §8 names **"SLFN11 IHC is negative"** as a scenario that breaks the Era-B DDR read. This
layer found a route that is specifically about that branch: **targeting glycerophospholipid (GPL)
biosynthesis overcomes chemoresistance driven by SLFN11 loss in Ewing sarcoma** — FSG67 **restored
DNA-damaging-agent sensitivity in SLFN11-deficient Ewing models.**
*Cell Death & Disease*, DOI 10.1038/s41419-026-08432-7 / PMC12877146 `[Preclinical-Cell, VERIFY]`

**Why it is worth a row:** the framework's contingency for "SLFN11 negative" was previously *"chemo-sensitivity
runs through another route (e.g. HR/ARID1A) and the ATR/CHK1i branch opens."* This adds a **second, lipid-
metabolic** branch, in the **Ewing (P1)** setting, that is about *restoring* sensitivity rather than
substituting a different agent. `Preclinical-Cell`; FSG67 is a **tool compound (F5)**; this is a
**contingency** item, live only if SLFN11 comes back negative.

---

## 6. What this layer changes in the framework's standing positions

| Standing position | Change |
|---|---|
| Persister reservoir is **GPX4-dependent / ferroptosis-vulnerable** (ADR-0021, `Low` confidence) | **Strengthened and unified** — the GPX4 dependency and the OXPHOS-high/FAO phenotype are two readings of one lipid-redox vulnerability; FSP1 and HDACs added as co-suppressors of persister ferroptosis. Confidence still `Low` (P4; no sarcoma model), but the prior rises on convergence. |
| **MCL1 "re-arm the DUX4 death program"** — demoted on two axes, with no replacement | **Replacement node proposed:** **BCL-XL in the quiescent post-anthracycline/alkylator reservoir** (not MCL1, not BCL2, not the bulk). Forward lane. |
| **NK-first immune sequencing** (Sims 4+5, ADR-0021) | **New mechanistic support + a measurable failure mode** — tumour-infiltrating NK cells suffer mTOR–Drp1-driven mitochondrial fragmentation, worsened by the tumour's own lactate/acidosis; reversing fragmentation restores cytotoxicity. Adds an *ex vivo* conditioning (M3) corollary. |
| **Immune-evasion axes measured** = MHC-I, Nectin/CD155, HLA-E, NK fitness | **New axis added: mitochondrial transfer into TILs** (homoplasmic replacement → T-cell senescence). Invisible to every existing assay in the catalog; detectable as tumour↔TIL **mtDNA-variant sharing**. |
| **Danger-signal generation** = oncolytic virus (ADR-0019, `Theoretical`, anatomy-limited) | **Second, endogenous generator identified** — mitochondrial DAMP/mtDNA→cGAS-STING, fusion-agnostic and not anatomy-limited; but **no clinical agent** implements it (F5), so it is a *concept* alongside OV, not a better-accessed one. |
| **"SLFN11 negative"** contingency = HR/ARID1A + ATR/CHK1i branch | **Second branch added** — GPL-biosynthesis inhibition (FSG67) restored sensitivity in SLFN11-deficient **Ewing** models (P1). |
| Host-biology layer (ADR-0005) covers nutrition/metabolic/exercise | **Extended with the competition mechanism** — nutrient competition and lactate/acidosis as *immunosuppressive* rather than merely metabolic, giving the host layer a named route to V4. |
| Feasibility/attrition register (ADR-0003/0013) | **Two entries added:** IACS-010759 = **R2-on-toxicity** (mechanism-based, F4 — *not* R1 target-invalidation); adjuvant metformin = **R2, biomarker-unenriched** (F1 access but **negative phase-3 adjuvant data**). |

**Not changed, deliberately:** the four fixed vectors (golden rule #8 — this is **not** a fifth vector); any
real-data vector finding (ADR-0009 — this layer is entirely `Preclinical`/`Theoretical` and all `[VERIFY]`);
and nothing in the forward lane is pruned (golden rule #5).

---

## 7. Red-team self-challenge (ADR-0017 / `sarcoma-pre-output-check`)

**Disconfirm — what would make this layer wrong?**
The persister/dormancy frame is the load-bearing assumption, and it is **unproven in this patient**. If the
relapse was outgrowth of a pre-existing metastatic clone (plausible — metastatic at diagnosis, 12 nodules),
then §5's entire reservoir argument, BCL-XL included, is aimed at a compartment that does not exist here.
Separately, **every** mechanism in §4 is P3/P4 with **zero sarcoma data**; a layer whose strongest items are
cross-lineage transfers of state-properties is exactly the kind of thing that reads well and replicates
poorly.

**Alternative explanation — is the mitochondrial framing doing real work, or is it a narrative?**
Partly a narrative, and it should be said. §4B (nutrient competition) and §5.1 (OXPHOS-high persisters) are
standard tumour-metabolism findings that need **no** endosymbiotic story to state. The framing earns its
keep in exactly two places: **§4A** (bacterial ancestry is the *reason* mitochondrial components are
immunogenic — a genuinely explanatory link) and **§4C** (organelle trafficking, where the parasitism reading
is literal). The rest is metabolism wearing an evolutionary costume. Stating that is more useful than
pretending the whole layer is novel.

**Flip-test — if the opposite were proposed, would it sound equally plausible?**
Yes, and revealingly so. "Boost mitochondrial function to restore differentiation and normal apoptotic
competence" is as narratively appealing as "inhibit OXPHOS to starve the reservoir" — and the §3.3 autophagy
finding shows the sign of these interventions is genuinely **not** predictable from the story. Any claim here
that cannot name its direction *and* a falsifier should be treated as decoration.

**Steer-audit — did the user's framing bias the output?**
It did, and the correction is in §2 and §3 by design: the question invited "attack the mitochondria," and the
two strongest pieces of *clinical* evidence in this whole area (IACS-010759, MA.32) say that specific move
fails. A version of this layer that led with §4 and buried §3 would have been a more satisfying answer and a
worse one. Note also that §3.3 **argues against** an intervention (autophagy inhibition) the framing points
toward — the symmetric-lane obligation under ADR-0020.

---

## 8. What I could not establish

1. **Any sarcoma-specific mitochondrial data for this case.** No CIC-DUX4 or CIC-like mitochondrial,
   OXPHOS, mtDNA-heteroplasmy, or mitochondrial-transfer data were found. The closest is Ewing-family
   (**P1** under Era B): SHMT2/one-carbon dependency and the GPL/SLFN11 result.
2. **Whether this tumour's reservoir is OXPHOS-high at all.** Never measured. The entire §5 argument is a
   class-level transfer.
3. **Whether a persister reservoir is the right model here** (vs. pre-existing metastatic clone). Unresolved
   and unresolvable without paired primary-vs-relapse sequencing. This is the dominant uncertainty.
4. **Any current regulatory or trial status.** `clinicaltrials.gov` was **unreachable** (HTTP 403) this
   session. Every F-band above is **inherited or inferred, not verified** — treat all as `[re-verify]`.
   DT2216, AZD3965, navitoclax, SHIN1/AGF347 and FSG67 statuses are **unverified**.
5. **Full-text verification of anything.** PubMed/PMC/Nature/EuropePMC/Crossref/E-utilities all returned
   HTTP 403. All identifiers are as they appeared in **search results**, not records I opened. Per ADR-0020
   this layer cannot enter a `protocol-vN.md` until that changes.
6. **Whether mitochondrial DAMP release is achievable pharmacologically without the §3.1 toxicity.** This is
   the crux of §4A and I could not resolve it — the Mt-Nd5 evidence is genetic/structural, and no agent
   translates it.
7. **Quantitative anything.** No simulation was run for this layer. There is no model, no posterior, no EVSI —
   unlike Sims 8/10, these are ranked by judgment only. A Boolean/flux sim of the reservoir's metabolic
   dependencies is the obvious next step and is **proposed, not executed** (§9).
8. **Entity grounding could not be run this session — it was attempted and is blocked, not skipped.** The
   repo venv is gitignored and absent in this fresh container, and `scripts/openmed_ner.py`'s self-bootstrap
   cannot complete because **`huggingface.co` is unreachable** (HTTP 000 through the proxy; PyPI itself
   returns 200, so this is specifically the model download). The following entities are **new to this
   repository and ungrounded** — they must be run through `--team v3-synthetic-lethality` (genes) and
   `--team v1-lead` (drugs+genes) before any promotion:
   **BCL2L1/BCL-XL, DT2216, navitoclax, SHMT2, SHIN1, AGF347, DRP1/DNM1L, MCT1/SLC16A1, MCT4/SLC16A3,
   MCT11, AZD3965, FSP1/AIFM2, P4HA2, ALDH4A1, MT-ND5, MIRO1/RHOT1, FSG67, IACS-010759, cardiolipin.**
   (Per CLAUDE.md §5, grounding confirms a *name* is a recognised biomedical term — it is not fact-checking,
   so its absence does not affect the tiering above, only the naming hygiene.)

---

## 9. Proposed next step (not executed)

**Sim 11 — reservoir metabolic-dependency model.** A constraint-based or Boolean model of the
quiescent/OXPHOS-high persister state, asking which of {complex I, FAO, GPX4/lipid-peroxidation defence,
BCL-XL, SHMT2/one-carbon} is (a) *necessary* for reservoir persistence and (b) *dispensable* for the
normal-tissue cooperators the commons objection (§2.2) protects — i.e. an explicit **therapeutic-window**
model rather than a target list. It would use real data (DepMap gene-effect for the Ewing proxy lines already
used in Sim 2; published persister expression signatures where accessible) and would let this layer's
judgment-only ranking be replaced by something falsifiable.

**Gating requirement before any promotion:** restore literature egress, full-text-verify §4A, §5.2, §5.3 and
§3.1/§3.2, and re-verify every F-band live.

---

*Layer authored 2026-09-17 under Era B (`CASE-BASELINE.md`, ADR-0022) and recorded as ADR-0023. Not a fifth
vector (golden rule #8). Forward-lane only under ADR-0020's `[VERIFY]` gate. Research simulation and
hypothesis generation only — not medical advice, not a diagnosis, not a testing or treatment recommendation.*
