# Chemo-Sensitivity as a Cell-State Readout — DDR/SLFN11 State, the Persister Reservoir, and the Immunotherapy Window

> **Origin:** user question, 2026-08-02 — an Ewing-like, CIC-like but **fusion-unconfirmed** tumour that
> (a) responded well to first-line chemotherapy and (b) achieved **complete radiographic resolution of
> relapsed lung nodules after 4 cycles of ifosfamide**, which is *atypical* for canonical CIC-DUX4.
> Question: what does that say about the epigenetics and cell state, and which attack vector works best
> in a novel immunotherapy setup?
>
> **Status:** cross-cutting **cell-state layer** — reads the clinical response as evidence and re-conditions
> the existing framework. **Not a fifth vector** (golden rule #8); it re-weights V1/V3/V4 and extends the
> driver-uncertainty model (ADR-0008). Quantitative backing: **`sims/10-chemoresponse-cellstate/`**.
>
> **Research simulation / hypothesis generation only. NOT medical advice, NOT a diagnosis, NOT a testing
> or treatment recommendation. No dosing, no start/stop instructions for any therapy.**
>
> **⚠ Verification status (ADR-0020):** direct literature egress (PubMed/PMC/nature.com/EuropePMC/Crossref)
> was **blocked HTTP 403** in this session. Every citation below is **search-snippet/abstract-level** and
> carries `[VERIFY]`. Under ADR-0020's mandatory gate, **nothing here may enter a `protocol-vN.md` until
> full-text-verified.** This artifact is a forward-lane document.

---

## 1. One-line answer

The chemotherapy response is the **most informative measurement anyone has taken on this tumour**, and it
points at a specific, coherent cell state: **cycling, apoptotically primed, and DNA-repair–limited
(SLFN11-competent)** — the *opposite* of the POLE-high/repair-proficient phenotype that defines canonical
CIC::DUX4. That state resolves to **~94% confidence** in the model, and it makes the **single highest-value
attack a dual-purpose epigenetic one: block PRC2/EZH2-mediated SLFN11 silencing** — because the same
intervention that preserves the chemo-sensitivity this tumour has already demonstrated *also* de-represses
MHC-I, which is the framework's existing V3→V4 immune bridge. The best **immunotherapy** vector is **V4,
NK-first, deployed inside the post-ifosfamide minimal-residual-disease window** — a window this
chemotherapy created for free and which **closes on its own**.

---

## 2. What the observation actually is: evidence, not just a clinical fact

Two response events are on record:

| | Observation | Date |
|---|---|---|
| **O1** | Excellent histologic response to first-line VDC/IE — **>95% necrosis** at resection | Jan 2025 |
| **O2** | **Complete radiographic response** of relapsed lung nodules after **4 cycles of ifosfamide** | 2026 |

These are functional assays already run on this patient's tumour. They are informative because the two
leading driver hypotheses carry **opposite, molecularly named DNA-damage-response phenotypes**:

| Hypothesis | DDR phenotype | Named mechanism | Published response |
|---|---|---|---|
| Canonical **CIC::DUX4** | repair-**proficient** | **POLE upregulation + proficient DNA repair** | **~30%** of CIC patients respond well `[Clinical-genomic, VERIFY]` |
| **Ewing / EWSR1-FET** | repair-**limited**, sensing-competent | **EWS-FLI1 transactivates SLFN11** → irreversible replication-fork arrest | **~53%** good histologic response `[Clinical, VERIFY]` |

*Sources (all `[VERIFY]`, snippet-level):* POLE/repair-proficiency in CIC::DUX4 — *npj Precision Oncology*
2025, DOI 10.1038/s41698-025-00985-8. CIC ~30% good response, "lower than Ewing" — Connolly et al.,
*Cancer Medicine* 2022 (PMC9041083). SLFN11 as an EWS-FLI1 target driving Ewing chemo-sensitivity —
Tang et al., *Clin Cancer Res* 2015, DOI 10.1158/1078-0432.CCR-14-2112.

**So the user's premise is correct and it is load-bearing:** a deep, twice-repeated chemotherapy response
is genuinely atypical for canonical CIC-DUX4, and it is atypical *for a reason that is molecularly named* —
which is what makes it usable as evidence rather than just an anecdote.

---

## 3. Deciphering the cell state — four reads, from the strongest to the weakest

### Read 1 — The cells are cycling, and the tumour is *reachable* (two different things)
Ifosfamide's mustard forms DNA crosslinks that are lethal at replication forks; killing most of a
multi-nodule burden requires most of the population to be in cycle. `[Established — alkylator pharmacology]`

**One distinction worth making precisely.** The user's framing — "the cells are in a state of division that
allows chemo to penetrate" — bundles two separate axes that have *different* therapeutic implications:

| Axis | What the CR demonstrates | What it implies |
|---|---|---|
| **Delivery / penetration** (perfusion, interstitial pressure, lesion size) | small, well-perfused lung nodules were reached at cytotoxic concentration | favours **any** systemic agent — including antibodies and cell therapies, which are far more delivery-limited than small molecules |
| **Cellular sensitivity** (DDR state, apoptotic priming) | the cells that were reached actually died | favours **DNA-damaging** agents specifically |

Both are good news, but only the first generalises to immunotherapy. It is a real and under-appreciated
point in this patient's favour: **lung is the most accessible metastatic compartment for cell-based and
antibody therapeutics**, and this tumour has just demonstrated that its lesions are pharmacologically
reachable. `[Mechanistic]`

### Read 2 — Mitochondrial apoptotic priming is INTACT
The cells convert DNA damage into actual apoptosis rather than surviving it. This is effectively a BH3
profile obtained without the assay: the death machinery downstream of damage is functional. `[Mechanistic,
high confidence — it is a direct read of the observed phenotype]`

**This has a concrete consequence for the existing catalog.** The framework's most promising *novel* target,
**MCL1 inhibition framed as "re-arming the DUX4 death program"**, presupposes a death program that needs
re-arming. A tumour that reliably dies to an alkylator does not obviously have that problem. Sim 8 already
held MCL1 as **driver-contingent**; this is a **second, independent, phenotypic argument** for the same
conclusion. In Sim 10, MCL1i drops out of the pursue-set in **99.1%** of sampled parameterisations.
(It also stacks against this patient's prior anthracycline exposure on cardiac grounds — see
`findings-ranking.md` §D.)

### Read 3 — The DDR is "sensing-competent, repair-limited" → predicted **SLFN11-positive**
This is the mechanistic core. SLFN11 is the best-validated single determinant of sensitivity to DNA-damaging
agents across tumour types: it binds stressed replication forks and enforces irreversible arrest rather than
allowing repair and restart. `[Preclinical-Cell / Clinical-correlative, VERIFY]`

- In **Ewing**, EWS-FLI1 directly transactivates SLFN11 — the named reason Ewing is chemo-sensitive. `[VERIFY]`
- In **canonical CIC::DUX4**, the published DDR phenotype is the opposite (POLE-high, repair-proficient). `[VERIFY]`

**Transferability (ADR-0014):** this sits at **P1** (fusion-driven round-cell family) — not P0. There are
**no SLFN11 data in CIC-DUX4 sarcoma at all.** The prediction is therefore `Mechanistic`, and it is offered
as *the measurement to make*, not as an established property of this tumour.

### Read 4 — A reservoir survived, and it is epigenetically, not genetically, defined
This is the read that matters most strategically, and it comes from the *relapse*, not the response.

After 14 cycles of VDC/IE, >95% necrosis at resection, whole-lung irradiation, and a year of NED, disease
returned. A subpopulation survived a regimen the bulk was exquisitely sensitive to. That is the definition
of a **drug-tolerant persister (DTP)** population, and DTP state is characteristically:

- **epigenetic and reversible**, not a resistance mutation — so it is in principle *addressable*, unlike a
  selected clone `[Preclinical-Cell]`
- **slow-cycling / quiescent** — which is precisely why it survives S-phase-dependent chemotherapy, and a
  warning that **cell-cycle-directed agents (CDK4/6i) target the bulk, not the reservoir**
- **KDM5A/KDM5B-associated** (H3K4me2/3 demethylation, global chromatin change) `[Preclinical-Cell, VERIFY]`
- **GPX4-dependent → selectively ferroptosis-vulnerable**; GPX4 loss kills persisters and *prevented tumour
  relapse in mice* — Hangauer et al., *Nature* 2017, **PMID 29088702** `[Preclinical-Animal]` (PMID seen as a
  literal PubMed record; abstract-level only)

> **The strategic reframe:** chemotherapy has now solved the *bulk* problem twice. The unsolved problem is
> the **reservoir** — and the reservoir has a **different vulnerability profile than the bulk**. Any "novel"
> therapy that simply adds more cytotoxicity to the bulk is aimed at the part of the disease that is already
> being handled.

---

## 4. The epigenetic unification — one node, two vectors

Here is the non-obvious convergence, and it is the main new contribution of this layer.

The framework already uses the **PRC2/EZH2 → H3K27me3** node for one purpose: **MHC-I restoration**, the
V3→V4 immune bridge (repositioned after Sim 2 showed EZH2 is *not* a survival dependency, and re-routed
toward p300/CBP after tazemetostat's 2026-03-09 withdrawal).

That same node is the **documented mechanism of chemo-sensitivity loss**:

> EZH2 deposits H3K27me3 across the **SLFN11** locus, silencing it, and this is how a chemo-*sensitive*
> tumour becomes chemo-*resistant* at relapse. Adding an EZH2 inhibitor to cytotoxic therapy **prevented the
> emergence of acquired resistance** in SCLC models. — Gardner et al., *Cancer Cell* 2017 `[Preclinical-Animal,
> VERIFY]`. Class-I HDAC inhibitors (entinostat, romidepsin) and 5-azacytidine **reactivate** silenced
> SLFN11 and re-sensitise cells to DNA-damaging agents — Murai et al., *Clin Cancer Res* 2018;24(8):1944
> `[Preclinical-Cell, VERIFY]`.

The clinical phenotype that paper describes — **"chemosensitive relapse"** — is *this patient's exact
pattern*: deep response, then relapse, then response again.

**So a single epigenetic intervention at PRC2/H3K27me3 is dual-purpose for this specific patient:**

| Axis | Effect | Framework location |
|---|---|---|
| **V3 — keep the tumour killable** | keeps SLFN11 de-repressed → preserves the chemo-sensitivity that is this patient's single best-demonstrated asset | new (this layer) |
| **V4 — make the tumour visible** | de-represses MHC-I → antigen presentation for the T-cell arm | existing V3→V4 bridge |

Both are **maintenance-phase** effects, which matches exactly where this patient is: post-response, minimal
residual disease. **This is the strongest argument the catalog now contains for an epigenetic agent in this
case, and it did not exist before the chemo-response information arrived.**

**Transferability + honesty:** the EZH2–SLFN11 axis is **P3** on the ADR-0014 ladder (solid tumour —
SCLC — with a named mechanism). It has never been tested in any sarcoma, let alone this one. Under
ADR-0014 that lowers the rung (confidence), it does not exclude — but "lower confidence" is doing real work
here and should not be read past.

**Feasibility is the binding constraint, not mechanism** (ADR-0003/0013): tazemetostat was **withdrawn from
all US indications 2026-03-09** (secondary malignancies) — an **R4 regulatory/safety** closure, so the
*mechanism* survives but the agent does not. Any route now goes through an alternative EZH2i
(e.g. valemetostat, in trials) or a class-I HDACi (entinostat) — **F3, and every status here is perishable
and must be re-verified live.** Adding an epigenetic drug to a working chemotherapy backbone also carries
its own myelosuppression and secondary-malignancy risk in a patient who has already had extensive
alkylator + anthracycline + radiation exposure. **That is an oncologist's judgement, not this document's.**

---

## 5. The immunotherapy answer — V4, NK-first, in a window that is already open

### Why *now* is the best immunological moment this patient will have

The chemotherapy did four immunologically useful things at once, and their overlap is the window:

1. **Lowest tumour burden** (CR) → maximal effector:target ratio. Immunotherapy efficacy is inversely
   related to tumour burden across essentially every modality. `[Established]`
2. **Lymphodepletion → homeostatic-proliferation rebound.** Chemotherapy vacates the IL-7/IL-15 "cytokine
   sinks" and preferentially depletes highly-proliferative Tregs; transferred or endogenous effectors then
   expand in the rebound. This is the window adoptive-cell-therapy protocols *deliberately manufacture*
   with cyclophosphamide/fludarabine — here it arises as a **by-product of therapy already given**.
   `[Preclinical-Animal + Clinical (ACT practice), VERIFY]` — *Cancer Res* 2005;65(20):9547.
3. **Synchronous antigen release** from a large kill → transient peak in available tumour antigen.
   `[Mechanistic]`
4. **Prior whole-lung irradiation** already primed the pulmonary niche (cGAS–STING/type-I IFN) — the
   framework's existing V4 entry A6. `[Preclinical-Animal]`

> **This window is perishable.** It closes as lymphocytes fully reconstitute and/or disease regrows. The
> actionable content of this whole layer is *timing*, and timing is the one axis that cannot be recovered
> later.

### Why NK-first (and why that is stronger here than in the generic case)

The framework's existing sequencing rule (Sims 4+5) is **NK-first → epigenetic MHC-I priming →
T-cell/checkpoint**, because NK killing wants MHC-I-*low* while T-cell killing wants MHC-I-*high*, and
epigenetic restoration can also co-induce **HLA-E** (the NKG2A brake).

Three reasons that rule is *more* strongly indicated for this patient than for the generic case:

1. **The residual/persister population is the most immunoedited compartment the tumour has** — it survived
   chemotherapy, radiation, and a year of immune surveillance. MHC-I-low is the expected escape phenotype,
   which is the NK-favourable state. `[Mechanistic]`
2. **NK cells reconstitute FIRST after chemotherapy lymphodepletion**, weeks-to-months ahead of the T-cell
   compartment. The innate arm is therefore the effector population that is actually *available* inside the
   window, whereas a T-cell-dependent strategy is asking the slowest-recovering compartment to do the work
   at its weakest moment. `[Established — haematopoietic reconstitution kinetics; VERIFY specific source]`
   **This is a new argument for NK-first that is specific to the post-chemo setting** and is not in the
   existing V4 files.
3. **NK strategies are fusion-agnostic** — they need no junction, so they apply unchanged to the ~5%
   fusion-unconfirmed subgroup this patient belongs to (golden rule #9).

### Ranked immunotherapy reads for this patient

| Rank | Approach | Tier | Confidence | Feasibility | Why here |
|---|---|---|---|---|---|
| 1 | **NK-directed (missing-self) in the MRD window** — IL-15 superagonist (N-803) and/or NK transfer | Mechanistic (CIC) / Clinical-Trial (other tumours) | **Medium** | N-803 **F1-US** `[re-verify]`; NK transfer **F2/F3** | Right effector for the window; fusion-agnostic; MHC-I-low residual clone |
| 2 | **Epigenetic priming (EZH2i / class-I HDACi)** — dual SLFN11 + MHC-I | Preclinical (P3 transfer) | **Low-Medium** | **F3**; tazemetostat **F4-US** | The dual-purpose node of §4 — but sequence it *after* the NK arm (MHC-I tension) |
| 3 | **Checkpoint doublet incl. LAG-3** (nivolumab + relatlimab) | Clinical (single CIC::DUX4 case report) | **Low-Medium** | **F1-US** `[re-verify]` | Only documented CIC::DUX4 immunotherapy response in the catalog; belongs *after* priming, not first |
| 4 | **Nectin/PVR-axis (ligand-side, NTX1088-class)** | Clinical-Trial (phase 1) | **Low** | **F3** | Existing V4 forward hypothesis; unchanged by this layer |
| — | **Junction-specific vaccine / TCR-T / CAR-T** | — | — | — | **HELD** — fusion-contingent, and Sim 10 pushes the fusion-confirmed drivers *down* (payoff −0.700) |

---

## 6. Forward hypotheses (new, with falsifiers)

**[FH-10.1] The dual-purpose epigenetic maintenance hypothesis.**
*Hypothesis:* In this chemo-sensitive, relapsing tumour, PRC2/EZH2-mediated H3K27me3 spreading over
**SLFN11** is the route by which the *next* relapse becomes chemo-**resistant**. Epigenetic intervention at
that node during the response/maintenance phase should (a) preserve chemo-sensitivity and (b) de-repress
MHC-I — two effects, one node, both in the same window.
*Mechanistic basis:* EZH2–SLFN11 chemosensitive-relapse axis `[VERIFY]`; existing V3→V4 MHC-I bridge.
*Falsifier:* SLFN11 IHC negative on relapse tissue → the premise fails outright. Or: paired
primary-vs-relapse H3K27me3 ChIP shows **no** gain over the SLFN11 locus → the proposed mechanism is not
operating in this tumour.
*Why untested:* the EZH2–SLFN11 axis has never been examined in any sarcoma.

**[FH-10.2] The reservoir has a different vulnerability profile than the bulk.**
*Hypothesis:* The relapse-seeding population is a drug-tolerant persister state — slow-cycling, KDM5A/B-
associated, GPX4-dependent — so the interventions that work on it (**ferroptosis induction**) are disjoint
from those that work on the bulk (**chemotherapy, CDK4/6i**). Sequential bulk-then-reservoir targeting
should outperform either alone.
*Mechanistic basis:* Hangauer et al., *Nature* 2017 (PMID 29088702) — GPX4 loss kills persisters and
prevents relapse in mice; persister state is reversible/epigenetic.
*Falsifier:* if the relapse specimen shows a **selected genetic clone** (new driver mutations, distinct
copy-number profile) rather than a reversible state, the persister model is the wrong frame and this
collapses. **Paired primary-vs-relapse sequencing distinguishes these directly** — and note that this
tumour was metastatic from diagnosis, so pre-existing-clone outgrowth is a live competing explanation
(the same caveat `metastatic-disease-considerations-v3.md` raises).
*Why untested:* no CIC-DUX4 or CIC-like persister model exists; ferroptosis induction in this disease is
entirely unexplored.

**[FH-10.3] The window, not the agent, is the scarce resource.**
*Hypothesis:* For this patient the *timing* of any immune intervention relative to the ifosfamide-induced
lymphodepletion nadir and rebound matters more than which immune agent is chosen — and the NK arm is
favoured over the T-cell arm inside the window purely on reconstitution kinetics.
*Mechanistic basis:* homeostatic proliferation / cytokine-sink biology `[VERIFY]`; NK-before-T
reconstitution `[VERIFY]`; the framework's existing NK-first sequencing result (Sims 4+5).
*Falsifier:* serial lymphocyte-subset immunophenotyping showing **no** NK-before-T reconstitution
asymmetry, or no Treg trough, in this patient would remove the kinetic argument.
*Why untested:* immune-reconstitution-timed intervention has never been studied in CIC-rearranged sarcoma.

---

## 7. What this changes in the existing catalog

| Existing position | Change | Basis |
|---|---|---|
| "**Resolve the driver first**" is the highest-leverage next action (Sim 8) | **Qualified.** Still the top-EVSI *test*, but its purpose has narrowed: it now almost exclusively serves to re-open the two fusion-contingent options. The therapeutically decisive variable (DDR state) has *already* been resolved to ~94% by the clinical course. | Sim 10 §Finding 4 |
| Driver prior: D1 cryptic CIC::DUX4 most likely (0.45) | **Flipped** to D4 phenocopy/misclassified (0.386 vs 0.264) in 75.2% of swept parameterisations — **while entropy over D *rises*.** The driver question got *harder*, not easier. | Sim 10 §Finding 1 |
| **MCL1 "re-arm the DUX4 death program"** — most promising novel target, held as driver-contingent | **Further demoted**, now on a second independent (phenotypic) axis: intact apoptotic priming argues against a death program needing re-arming. Out of the pursue-set in 99.1% of samples. | Sim 10 §Finding 3 |
| **EZH2i repositioned as MHC-I priming only, not cytotoxic** (Sim 2, real DepMap CRISPR) | **Unchanged but given a second rationale** — SLFN11 maintenance. Sim 2's finding (EZH2 is not a *survival dependency*) is not contradicted: neither proposed effect is cytotoxicity. | §4 |
| CDK4/6i as a robust cell-cycle lever | **Caveat added:** it targets the cycling bulk; the slow-cycling persister reservoir is the compartment that actually causes relapse. | §3 Read 4 |
| V4 sequencing: NK-first → priming → checkpoint | **Reinforced**, with a new patient-specific kinetic argument (NK reconstitutes first post-chemo). | §5 |

---

## 8. Red-team self-challenge (ADR-0017)

**Disconfirm.** The strongest case *against* this whole layer: a complete response of small lung nodules to
high-dose ifosfamide in an oligometastatic relapse is a **favourable-setting** result as much as a
favourable-*biology* result. Burden, lesion size, perfusion, and dose intensity all push the same direction,
and ~30% of genuine CIC patients *do* respond well — this patient could simply be in that 30%. Sim 10
handles this by treating the observation probabilistically rather than diagnostically (D1 retains 26.4%),
but the model attributes **all** of the signal to cell state and **some of it belongs to setting**.

**Alternative hypothesis.** Chemo-sensitivity need not run through SLFN11 at all. A homologous-recombination
defect would produce the same phenotype — and the CIC::DUX4 MCL1 literature already noted **recurrent
ARID1A** alterations, which would point at SWI/SNF rather than SLFN11 and carry entirely different
therapeutic implications (ATR inhibition, different immune consequences). **SLFN11 IHC discriminates these
and is cheap** — which is exactly why the near-zero EVSI in Sim 10 §Finding 4 should *not* be read as "don't
measure it": EVSI scores a test's power to flip a decision under the model's assumptions, not its power to
catch the model being wrong.

**Flip-test.** If this tumour were *chemo-resistant* instead, would this layer's logic have produced the
opposite recommendation with equal confidence? Largely yes — it would have pointed at the ATR/CHK1i branch
and at the POLE/repair-proficient phenotype. That symmetry is a point in the framework's favour (it is not
a one-directional confirmation engine), but it also means the layer's conclusions are only as good as the
two response observations, which are **clinical impressions of imaging and pathology, not molecular data**.

**Steer audit.** The user's framing supplied both the observation *and* the interpretation ("this means the
subtype reacts well to chemotherapy," "this means the cells are in a state of division"). Both readings are
well-supported and I have adopted them — but I have deliberately separated *penetration* from *sensitivity*
(§3 Read 1), because collapsing them would have over-generalised the result to modalities it does not
actually support. The `[VERIFY]` gate is doing heavy lifting throughout and is not decoration: **the entire
mechanistic spine of §4 rests on snippet-level sources this session could not open.**

---

## 9. Standard-of-care interaction flags

- **Ifosfamide is a CYP3A4/CYP2B6-activated prodrug.** The catalog's standing top-priority safety item —
  the convergent piperine + curcumin + thymoquinone CYP3A4 signal — is **unchanged and still the single most
  actionable item**, because the same enzyme sits at the branch point between activation (efficacy) and
  N-dechloroethylation (chloroacetaldehyde neuro/nephrotoxicity), so the *direction* of any modulator's
  effect is not predictable. Flag for oncologist/pharmacist review; **not** a stop/start instruction.
- **If chemo-sensitivity is this patient's principal asset, anything that plausibly blunts it deserves more
  scrutiny than usual** — this sharpens the framework's existing antioxidant caution (high-dose antioxidants
  during ROS-dependent chemotherapy) rather than adding a new one. Mechanistic; oncologist's call.
- **Epigenetic agents (EZH2i/HDACi) stack myelosuppression and secondary-malignancy risk** on top of
  extensive prior alkylator + anthracycline + radiation exposure. Tazemetostat's withdrawal was itself for
  secondary malignancies. This is a hypothesis-space discussion only.
- **No dietary or supplement compound is recommended in this artifact**, so the VDC/IE screens are not
  newly triggered here; they remain in force for the dietary entries elsewhere in the catalog.

---

## 10. What I could not establish (honest)

1. **Whether SLFN11 is expressed in this tumour — or in CIC-DUX4 sarcoma generally.** No SLFN11 data exist
   in this disease. The entire §4 argument is a *prediction* awaiting a single cheap IHC. `P(S_hi|D1)=0.20`
   is inferred from the POLE paper, not from a measured SLFN11 distribution — the weakest parameter in Sim 10.
2. **Full-text verification of any citation here.** PubMed/PMC/nature.com/EuropePMC/Crossref all returned
   HTTP 403 this session. Only PMID 29088702 (Hangauer) was seen as a literal PubMed record identifier.
   **Everything else is `[VERIFY]` and gated out of protocol promotion by ADR-0020.**
3. **Whether the relapse is a persister-derived population or a pre-existing metastatic clone.** This
   tumour was metastatic at diagnosis, so clonal outgrowth is a live competing explanation. FH-10.2 depends
   on which it is, and paired primary-vs-relapse sequencing would settle it.
4. **Whether the radiographic CR (O2) is a true pathologic CR.** Post-WLI lungs are a confounded imaging
   compartment. If O2 is weaker than modelled the S posterior softens (though the sweep's 90% CI stays ≥0.83).
5. **This patient's actual lymphocyte-subset kinetics.** The entire window argument (§5) is generic
   immunology applied to an assumed reconstitution pattern; no counts for this patient were available.
6. **Whether EZH2i/HDACi affect SLFN11 in *any* sarcoma.** The axis is SCLC-derived (P3 transfer).
7. **Whether the persister/GPX4 biology applies to round-cell sarcoma.** Hangauer's panel did not include
   this disease; the claim is class-level, not tumour-specific.

---

*Grounding: entity list in `sims/10-chemoresponse-cellstate/entities.txt`. **OpenMed NER was NOT run** —
HuggingFace egress blocked (HTTP 403, 2026-08-02); no grounding scores are invented. Newly-introduced
entities not previously grounded anywhere in this repo (**SLFN11, POLE, KDM5A/KDM5B, GPX4**) are flagged in
`grounding.tsv` for a later pass.*

*Reuse note: this layer extends — and does not replace — `sims/08-driver-uncertainty/`,
`tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`,
`v4-immune-watchdog/immune-watchdog-expansion.md`, and `metastatic-disease-considerations-v3.md`.
Baselines preserved. **Research simulation only — not medical advice, not a diagnosis.***
