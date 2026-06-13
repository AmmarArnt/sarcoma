# Translational Feasibility Layer — Clinical-Trial & Regulatory Awareness

**In response to GitHub issue #9** — *"Translational Feasibility Layer: Clinical Trial and Regulatory
Awareness"* (@Cerimagic).

**Status:** framework-enhancement proposal + applied result for the current catalog
(`protocol-v1.md`). Research-simulation output, **not medical advice**, **not a recommendation to seek,
start, stop, or enroll in any therapy or trial**. The goal, exactly as the issue framed it, is to
**clearly distinguish biological plausibility from practical feasibility** — *not* to exclude
early-stage or experimental ideas (doing so would violate golden rule #5, "known research is the floor,
not the ceiling").

**Confidence:** medium-high for the regulatory/trial facts (each verified against a live source this
run and dated; see Provenance), lower for the few items flagged `[VERIFY]`. The *scoring scheme* is a
transparency aid, not a validated instrument.

---

## 1. The question, restated

The issue asks whether therapeutic hypotheses should be evaluated through a **translational feasibility
layer** that captures real-world accessibility and development maturity, so that two biologically
equivalent hypotheses are distinguished when one is in an actively recruiting Phase 3 trial, one is
preclinical, one's drug was discontinued, one is under regulatory hold, and one is approved elsewhere
and repurposable. Proposed dimensions: development stage, regulatory status, trial availability,
geographic accessibility, repurposing potential, and major translational barriers.

**Short answer: yes — and it is a distinct, third axis the framework was not tracking explicitly.** It
is also the axis most likely to *change without any new biology*, because regulatory and commercial
status move on their own timeline. This run already surfaced one such change that materially affects the
existing catalog (§5, the tazemetostat withdrawal). We add a standing feasibility-banding scheme (§3),
apply it to `protocol-v1.md` (§4), and record the headline divergences between plausibility and
feasibility (§5).

---

## 2. Where this sits — three orthogonal axes (composition, not duplication)

The framework now reasons on **three independent axes**. Conflating them is the gap each contributor
issue has identified in turn:

| Axis | Question it answers | Where it lives |
|---|---|---|
| **1. Evidence tier** (7-tier) | *What kind of evidence is this?* | `sarcoma-contract` (established) |
| **2. Confidence** (Directness / Achievability / Reproducibility / conflict) | *How much should I believe this works in CIC-DUX4 in vivo?* | `docs/08-evidence-confidence-scoring.md` — **in-flight in PR #16 / issue #8, not yet merged** |
| **3. Translational feasibility** *(this layer)* | *Could a patient actually access it, and how soon?* | this document (issue #9) |

**Critical delineation vs. the issue-#8 axis.** The issue-#8 confidence rubric contains an
**"Achievability"** sub-axis — but there it means *can the active molecular concentration be reached in
vivo by the proposed route* (a pharmacokinetic/biological question; the canonical dietary
concentration-mismatch failure). **This layer's "feasibility" is different and complementary**: it is
the *clinical-development and regulatory access* question — is there a marketed drug, an open trial, a
jurisdiction. The two do not collide:

- A BRD4 **degrader** could be biologically high-achievability (engages target, defeats wash-back —
  high on axis 2) yet translationally **F4** here because every clinical BET program has contracted
  (low on axis 3).
- **Omega-3 / vitamin D** are translationally **F1** (in any grocery store) yet low-confidence on axis
  2 (concentration mismatch, no CIC-DUX4 data).

So feasibility is **not** a proxy for plausibility, and a low feasibility band is **not** a reason to
drop a hypothesis — it is a reason to *label* it honestly. The two-lane rule from PR #16 carries over
verbatim: **feasibility annotates the confirmatory lane for clinician/patient awareness; it never prunes
the Forward-Hypotheses lane.** A concept-only idea (F5) can still be the most valuable forward
hypothesis.

---

## 3. The feasibility scheme (the framework layer)

For every confirmatory-lane intervention, record the issue's six dimensions. Collapse
**development-stage + regulatory-status + trial-availability** into a single **Feasibility Band** (bands,
not false-precision numbers — same rationale as PR #16 §3); keep **geography, repurposing, and barriers**
as explicit columns.

| Band | Definition (access path *for a patient with this disease*) |
|---|---|
| **F1 — Accessible now** | Approved & marketed in ≥1 major jurisdiction; an on-label-adjacent, off-label, or expanded-access route plausibly exists. |
| **F2 — Accessible via trial / named-patient** | Not approved for this use, but in **active human trials** (ideally enrolling a relevant population) or reachable via expanded-access/compassionate-use. |
| **F3 — In development, no clear route here** | Clinical-stage somewhere, but no trial open to this disease/geography and no access path. |
| **F4 — Discontinued / withdrawn / on hold** | Mechanism may be strong, but the **access path is closed** — program halted, drug withdrawn, or under regulatory hold. The issue's explicit "discontinued / FDA-EMA hold" case. |
| **F5 — Concept only** | No clinical-stage agent exists (preclinical/theoretical). |

**Banding is jurisdiction- and time-stamped.** FDA ≠ EMA ≠ PMDA access can differ for the *same* drug,
and a band can change overnight on a regulatory action (the tazemetostat case below moved
F1→F4 in the US in March 2026 with no change in biology). Every band carries an "as of" date.

**Design principle (ties to issue #8 / PR #16):** a hypothesis whose only access path is F4/F5 should be
displayed with that label adjacent to its evidence tier, so a reader never mistakes "mechanistically
attractive" for "obtainable." Uncertainty/closure on the feasibility axis attenuates *display
prominence in the confirmatory lane*, not the idea's place in the forward lane.

**Why an F3/F4 closure happened matters as much as the band (issue #9 follow-up).** An F4 band says
*access is closed* but not *why* — and "discontinued/withdrawn" must never be read as **biological
invalidation**. The companion [feasibility-attrition-reason extension](feasibility-attrition-reason-extension.md)
(ADR-0013) adds an **attrition-reason annotation (R0–R5)** — never-developed (R0) / target-invalidated
(R1) / trial-efficacy-failure (R2) / subgroup-dilution (R3) / regulatory action (R4) / commercial
deprioritization (R5) — and the decoding rule that **only R1 (and a biomarker-enriched R2) carries
negative biological information**; R3/R4-commercial/R5 are biology-silent. It is an annotation on this
axis, **not a new scoring axis**.

---

## 4. Applied to `protocol-v1.md` (Clinical / Experimental track) — as of June 2026

Every regulatory/trial fact below was checked against a live source this run (Provenance). Bands are
**US-centric unless noted**; EMA/PMDA divergence is called out because this patient's geography is not
encoded and access differs by jurisdiction. **Evidence tier (axis 1) is unchanged from the catalog;
this table adds axis 3 only.** Nothing here is a recommendation to obtain, enroll in, or avoid any of it.

| Intervention (vector) | Feasibility band (as of Jun 2026) | Development stage / regulatory status | Trial availability | Geography | Repurposing route | Major translational barrier |
|---|---|---|---|---|---|---|
| **Tazemetostat — EZH2i** (V3→V4) | **F4 (US), F3 (EU)** ⬇ **was F1** | FDA accelerated approval epithelioid sarcoma (2020-01-23) + FL (2020-06-18), **both voluntarily withdrawn by Ipsen 2026-03-09 (all US indications)**; **never EMA-approved** | Withdrawal followed SYMPHONY-1 safety signal; oncology trials affected | US (now closed), never EU | Off-label route **closed** by market withdrawal | **Secondary hematologic malignancies** in the SYMPHONY-1 *combination*; commercial withdrawal — see §5.1 |
| **Valemetostat — EZH1/2i** (V3→V4; alternative to tazemetostat) | **F2 (trials), F1 (Japan only, distant indication)** | Approved **Japan** (EZHARMIA): aggressive ATL 2022-09, R/R PTCL 2024-06; no US/EU approval | Solid-tumor trials recruiting (NCT06244485 + DXd-ADC combos; NCT07303387; pediatric NCCH1904 showed activity in **INI1-negative** tumors) | Japan (approved); US/EU trial-only | Hematologic→solid-tumor trial expansion | No CIC-DUX4 data; geography; combos are with ADCs, not standalone |
| **Entinostat — class-I HDACi** (V3→V4) | **F3** | No approval anywhere; pivotal breast trial (E2112, +exemestane) did **not** meet OS `[VERIFY]` | Earlier-phase combos persist `[VERIFY]` | — | — | Repeated late-phase failures; narrow window |
| **Vorinostat — pan-HDACi** (V3→V4) | **F1 (US), F4/none (EU)** | FDA CTCL approval 2006; **not approved in EU** (application withdrawn) `[VERIFY EU specifics]` | Investigator trials in solid tumors exist | US (CTCL), not EU | CTCL→off-label | Toxicity overlap with ifosfamide; pan-HDAC non-selectivity |
| **BET inhibitors as a class** (V1/V3/V4) | **F3–F4** ⬇ | Class has **contracted sharply**: BMS-986158/ezobresib **dropped by BMS**; **AbbVie exited** BET; **birabresib** GBM trial **terminated** (lack of activity); **molibresib** development **halted** | **ZEN-3694 is the main survivor** — FDA Fast Track + Orphan Drug (NUT carcinoma, +abemaciclib); +niraparib NCT06161493 | US-centric trials | None approved → trial-only | On-target toxicity (thrombocytopenia/GI); reversible occupancy; **no BETi is approved anywhere** |
| **CDK4/6 inhibitors** (palbociclib/ribociclib/abemaciclib) (V1/V3) | **F1** | FDA + EMA approved HR+ breast (2015–2017) | Sarcoma trials small/mixed; abemaciclib in combos | US + EU + more | Breast→off-label/basket | Cytostatic-only; CCNE1 bypass; additive myelosuppression with ifosfamide |
| **Azacitidine / decitabine — DNMTi** (V3→V4) | **F1** | FDA + EMA approved MDS/AML | Solid-tumor immune-priming trials exist | US + EU + more | MDS/AML→off-label/trial | Solid-tumor efficacy unproven; myelosuppression |
| **Pembrolizumab / nivolumab ± ipilimumab** (V4) | **F1** | FDA + EMA approved across many indications | SARC028 (NCT02301039) + successors done; sarcoma trials ongoing | US + EU + more | Broad→off-label/basket | Modest sarcoma monotherapy ORR; needs V3 MHC-I priming |
| **N-803 / nogapendekin alfa inbakicept (Anktiva) — IL-15 superagonist** (V4 NK) | **F1 (US), F2/F1 (EU pending)** | **FDA approved 2024-04-22** (NMIBC + BCG, CIS); **EMA CHMP positive opinion** for conditional MA | Solid-tumor combo trials exist | US (approved); EU advancing | NMIBC→off-label/trial | Approved indication is intravesical NMIBC — systemic-solid-tumor route is trial-stage |
| **Personalized neoantigen mRNA vaccine** (V940/mRNA-4157 *intismeran autogene*; BNT122) (V4) | **F2** | **Phase 3 recruiting** — V940-001/INTerpath-001 (melanoma), INTerpath-002 (NSCLC); KEYNOTE-942 5-yr RFS HR 0.510 (Jan 2026) | Phase 3 enrolling, but in **melanoma/NSCLC**, not sarcoma | Global Phase 3 sites | Platform repurposable to any solid tumor with tissue | Indication-distant; **needs tumor tissue**; anti-PEG titer caveat (catalog §mRNA); manufacturing lead-time |
| **Adoptive NK transfer** (V4 NK) | **F2 (heme) / F3 (solid sarcoma)** | Clinical-stage in heme; solid-tumor sarcoma is early | Heme trials; few solid-sarcoma trials | Specialized centers | Heme→solid (unproven) | Solid-tumor trafficking/persistence; manufacturing |
| **CIC-DUX4 junction ASO / PROTAC / junction vaccine / CAR-T / TCR-T** (V3/V4) | **F5** | No clinical-stage agent | None | — | — | Undruggable-TF + solid-tumor delivery; **fusion-confirmed only — POSSIBLY INAPPLICABLE to this fusion-unconfirmed patient** |
| **Transcriptional-condensate disruptors** (V3, forward) | **F5** | Preclinical concept only | None | — | — | CIC-DUX4 condensate behavior uncharacterized |

**Naturally-Achievable track (diet/supplements):** all **F1 on access** (grocery-store / OTC) — but
that high feasibility is exactly why the catalog's honesty lives on axes 1–2 (concentration mismatch,
no CIC-DUX4 data, the curcumin-piperine/CYP3A4–ifosfamide interaction). **F1 access ≠ established
benefit** — the clearest illustration of why feasibility must stay orthogonal to plausibility, not
collapse into it.

**Disease-specific trial note (rare positive):** a Phase II of **regorafenib** in metastatic bone/soft-tissue
sarcomas (**NCT02389244**, REGOBONE Cohort E) includes a **CIC-rearranged cohort** — one of the very few
registered trials to name this entity rather than fold it into an undifferentiated basket. Tier for
regorafenib in CIC-rearranged: `Clinical-Trial`. **Status updated 2026-06-13:** the trial is
**`ACTIVE_NOT_RECRUITING`** (primary completion 2024-10-25; completion 2026-03-11; last update
2025-09-16) and the **CIC Cohort-E efficacy results are not yet published / not posted** — so this entry
is **results-pending**, *not* a negative result (ClinicalTrials.gov API, accessed 2026-06-13). For the
full answer to "was it deprioritized?" — and the **attrition-reason taxonomy (R0–R5)** that distinguishes
a commercial/safety/diluted closure from genuine biological invalidation — see the
[feasibility-attrition-reason extension](feasibility-attrition-reason-extension.md) (issue #9 follow-up /
ADR-0013). Short version: results-pending + mechanism not driver-directed, **not** negative efficacy.

---

## 5. Headline findings — where feasibility and plausibility diverge

### 5.1 The catalog's central bridge agent changed access status (the load-bearing finding)
`protocol-v1.md` Top-Level Finding #2 names **tazemetostat (EZH2i) restoring MHC-I as "the cleanest
V3→V4 bridge … the catalog's central cross-vector dependency,"** and Top-Level Finding #1's strongest
rival rests on the EZH2i route. As of **2026-03-09**, **Ipsen voluntarily withdrew tazemetostat
(Tazverik) from all approved US indications** (epithelioid sarcoma + follicular lymphoma) after the
**SYMPHONY-1** combination trial raised a **secondary-hematologic-malignancy** signal that an
independent monitoring committee judged might outweigh benefit. Two things must be stated precisely:

- **This is a commercial/voluntary market withdrawal by the manufacturer, not an FDA revocation of the
  approval or a finding that EZH2 inhibition is wrong.** The *mechanism* (PRC2/EZH2 → APM/MHC-I
  de-repression) is unchanged; the *access path in the US* closed.
- **It was never EMA-approved** (US-only as of early 2025), so EU access was already trial-only.

**Consequence for the catalog (axis 3 only; axes 1–2 unchanged):** the single most-cited clinical agent
in the catalog moved **F1 → F4 (US)** with no biological news. The mechanism survives; the *named drug*
does not, in its main jurisdiction. The constructive substitution is the **EZH2/EZH1 class, not the
molecule**: **valemetostat** (Japan-approved for ATL/PTCL; active solid-tumor and pediatric
INI1-negative trials) keeps the *mechanism* reachable via trials — at lower feasibility (no US/EU
approval, no CIC-DUX4 data). This is precisely the issue's thesis: a biologically central hypothesis
can have its practical footing shift overnight, and the framework should see it.

### 5.2 The "strongest mechanistic entry point" sits on a contracting clinical pipeline
Top-Level Finding #1 calls **BRD4/BET inhibition the strongest mechanistic entry point**. On axis 3, the
clinical BETi field has **contracted sharply**: BMS dropped ezobresib/BMS-986158, AbbVie exited the
space, birabresib's GBM trial was terminated for lack of activity, and molibresib development halted.
**No BET inhibitor is approved anywhere**, and the main surviving clinical asset is **ZEN-3694** (Fast
Track/Orphan in NUT carcinoma, in combinations). So the catalog's strongest *mechanism* is, today, among
its weaker *access* stories — F3–F4, not F1. The honest read: pursue BRD4 biology, but expect the route
to be a single trial-stage asset or a degrader concept (F5), not an off-the-shelf drug.

### 5.3 Where feasibility is genuinely favorable (and why that is not the same as "best")
The highest-feasibility clinical entries are the **repurposable approved drugs** — CDK4/6 inhibitors,
azacitidine/decitabine, checkpoint antibodies (all **F1**, FDA+EMA) and **N-803/Anktiva** (US-approved
2024, EMA advancing). These have real off-label/basket access. But each is **modest or unproven in
CIC-DUX4** on axes 1–2 (CDK4/6i cytostatic + CCNE1 bypass; checkpoint monotherapy modest in sarcoma;
N-803's approved route is intravesical, not systemic). **High feasibility + modest plausibility is a
different object from low feasibility + high plausibility** — and the whole point of separating the axes
is to keep the reader from averaging them into a single misleading score.

### 5.4 The most developmentally mature *platform* is indication-distant
The personalized **neoantigen mRNA vaccine** platform (V940/intismeran autogene; BNT122) is the most
trial-mature immunotherapy concept relevant to V4 — **Phase 3 recruiting** with positive 5-year
melanoma data (HR 0.510). But it is **F2, not F1**, for this patient: the trials are in melanoma/NSCLC,
it needs tumor tissue, and the catalog's anti-PEG caveat applies. Platform maturity ≠ access for *this*
disease.

---

## 6. Forward feasibility hypotheses (idea-generation lane — exempt from feasibility pruning)

Tagged `Theoretical`; these are *access-path* hypotheses, not biological claims. They illustrate that a
feasibility layer can also generate ideas, not only flag closures.

1. **[Forward Hypothesis] Treat the EZH2 *mechanism* as the durable target and the *molecule* as
   swappable.** With tazemetostat's US access closed, re-anchor the V3→V4 bridge on the EZH2/EZH1
   *class* via **valemetostat** solid-tumor trials (incl. the pediatric INI1-negative arm that is
   mechanistically adjacent to BAF-related dependencies). Falsifier/test: confirm a PRC2 dependency and
   MHC-I induction in a CIC-DUX4 model under valemetostat before treating feasibility as transferable
   from tazemetostat. *This keeps the catalog's central bridge alive on axis 1–2 while honestly
   re-banding axis 3.*
2. **[Forward Hypothesis] Use the rare disease-named cohort as the realistic enrollment surface.** The
   regorafenib CIC-rearranged cohort (NCT02389244) shows dedicated cohorts *do* occasionally exist;
   the highest-feasibility forward move for any V1/V3 candidate is to seek **basket/umbrella trials with
   a molecularly-defined fusion-sarcoma stratum** rather than a CIC-DUX4-dedicated trial (which the
   rarity makes near-impossible — counterfactual-trial-forensics cross-cutting §). Test: map current
   sarcoma baskets for fusion-defined strata that would admit a fusion-unconfirmed case.
3. **[Forward Hypothesis] Maintain a standing "regulatory-watch" trigger on the catalog's load-bearing
   agents.** Because feasibility moves without biology (this run caught a 3-month-old withdrawal),
   the highest-value low-cost addition is a periodic re-check of the ≤5 most-cited clinical agents'
   status. Test: re-run §4's verification on a cadence; a band change (e.g., an EMA approval, a clinical
   hold) is the trigger to revise the clinician brief.

---

## 7. What this layer does **not** do (honest limitations)

- **It is not a recommendation to enroll, obtain, or avoid anything.** Bands describe the *access
  landscape*, not what this patient should do — that is the oncologist's decision.
- **It ranks access, not benefit.** F1 ≠ "works"; F5 ≠ "worthless." The dietary track is F1 and mostly
  low-confidence; junction ASOs are F5 and (if the fusion were confirmed) high-plausibility.
- **Jurisdiction- and date-stamped, and perishable.** Every band is "as of June 2026" and US-centric
  unless noted. Regulatory status changes; the tazemetostat case is the proof. Re-verify before any use.
- **It does not gate the forward lane.** Per golden rule #5 and PR #16's two-lane rule, low feasibility
  never removes a hypothesis from idea-generation.
- **`[VERIFY]` items are not asserted.** Entinostat's pivotal-trial outcome, vorinostat's precise EU
  status, and the regorafenib cohort's current recruitment were not fully confirmed this run and are
  flagged, not stated as fact.
- **Atypical-case flag unchanged.** The fusion-unconfirmed status makes the **F5** junction-specific
  rows POSSIBLY INAPPLICABLE regardless of feasibility; the fusion-agnostic rows (EZH2-class, BET,
  CDK4/6, DNMTi, checkpoint, NK, dietary) remain in-scope.
- **No new biology, no fabricated citations.** Every accession/approval is sourced (§Provenance) or
  flagged `[VERIFY]`.

**Evidence tier of this layer:** `Established` for the verified regulatory/trial facts (FDA/EMA/PMDA
actions and registered trials, each cited); the *scheme itself* is a transparency/prioritization tool,
not evidence about the patient.

---

## Provenance — sources verified this run (June 2026)

- **Tazemetostat FDA approvals:** epithelioid sarcoma accelerated approval 2020-01-23; follicular
  lymphoma 2020-06-18 (FDA; *FDA granted accelerated approval to tazemetostat for follicular lymphoma*).
- **Tazemetostat US market withdrawal:** Ipsen, **2026-03-09**, all approved US indications, SYMPHONY-1
  secondary-hematologic-malignancy signal; **commercial/voluntary withdrawal, not an FDA revocation**
  (OncLive, *FDA Indications for Tazemetostat … Are Voluntarily Withdrawn*; CancerNetwork,
  *Tazemetostat Withdrawn From Follicular Lymphoma, Sarcoma Markets*, 2026-03-09).
- **Tazemetostat EU status:** not EMA-approved / US-only as of early 2025 (everyone.org,
  *Tazemetostat's EMA approval*). `[VERIFY any post-2025 EU filing]`.
- **Valemetostat (EZHARMIA, DS-3201):** Japan approval aggressive ATL 2022-09, R/R PTCL 2024-06; dual
  EZH1/2; solid-tumor trials NCT06244485 (+DXd ADCs), NCT07303387, pediatric NCCH1904 (INI1-negative
  activity) (Daiichi Sankyo; OncLive; *Valemetostat Tosilate: First Approval*, Drugs 2022, PMID
  36310058).
- **N-803 / nogapendekin alfa inbakicept (Anktiva):** FDA approval **2024-04-22** (NMIBC + BCG, CIS,
  QUILT-3.032); EMA CHMP positive opinion for conditional MA (FDA; OncLive; Urology Times).
- **BET inhibitors:** BMS dropped BMS-986158/ezobresib; AbbVie exited BET (oncologypipeline/ApexOnco,
  *Bristol backs out of BET inhibition*); birabresib GBM trial terminated for lack of activity
  (ClinicalTrials.gov NCT02296476); molibresib development halted (JNCI Cancer Spectrum 2020); ZEN-3694
  FDA Fast Track + Orphan in NUT carcinoma (+abemaciclib), +niraparib NCT06161493 (Zenith Epigenetics;
  OncLive; CancerNetwork). Class review: *Bromodomain inhibitors a decade later*, Br J Cancer 2020.
- **V940 / mRNA-4157 (intismeran autogene):** Phase 3 V940-001/INTerpath-001 (melanoma) + INTerpath-002
  (NSCLC) recruiting; KEYNOTE-942/mRNA-4157-P201 5-year RFS HR 0.510 reported Jan 2026 (Merck/Moderna
  press releases; CancerNetwork).
- **Regorafenib CIC-rearranged cohort:** Phase II NCT02389244, cohort for CIC-rearranged sarcoma
  (ClinicalTrials.gov). `[VERIFY current recruitment status]`.
- **CDK4/6i, azacitidine/decitabine, pembrolizumab/nivolumab/ipilimumab:** FDA + EMA approvals in their
  on-label indications — `Established` common knowledge, consistent with `protocol-v1.md` Clinical track.
- **Vorinostat:** FDA CTCL 2006; not EU-approved — `[VERIFY EU specifics]`. **Entinostat:** no approval;
  pivotal breast outcome `[VERIFY]`.

*Decision record:* this layer is adopted via
[ADR-0003](../docs/adr/0003-translational-feasibility-layer.md) (issue #9 / PR).

*No new biology, no fabricated citations, not medical advice. Bands are jurisdiction- and date-stamped
(as of June 2026) and perishable — re-verify before any external use.*
