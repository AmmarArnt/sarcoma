# Host-Biology Treatment-Response Modifier Layer

**In response to GitHub issue #10** — *"Host Biology and Treatment Response Modifiers"* (@Cerimagic).

**Status:** framework-enhancement proposal + an evidence-tiered factor catalog applied to the current
fusion-unconfirmed case. Research-simulation output, **not medical advice**, **not lifestyle prescription**,
and explicitly **not a substitute for evidence-based cancer treatment** — exactly the boundary the issue
itself drew. The contribution here is *structural*: deciding where host-level factors live in the
framework and how their evidence is weighted, then cataloguing which ones currently have enough evidence
to carry, each with an honest tier and transfer caveat.

This layer is governed by the standing contract (`sarcoma-contract`): every factor below carries an
evidence tier, a mechanism, a "direct CIC-DUX4 evidence?" line (almost always *None direct*), and the
three scoring axes where they apply.

---

## 1. The questions, restated

The issue and its follow-up comment ask four things, plus a psychoneuroimmunology (PNEI) direction:

1. Should host-level biological modifiers be represented as a **separate layer** within the framework?
2. Can they help **explain variability** in treatment response between patients with otherwise similar
   tumour biology?
3. Which host factors currently have **sufficient evidence** to justify inclusion?
4. How should evidence strength be **weighted** for host-level vs. tumour-targeted interventions?

Host factors named: gut microbiome, SCFA production, systemic inflammation, metabolic status, physical
activity, sleep/circadian biology, autonomic (ANS) regulation, nutritional status; and in the comment —
psychological stress / stress anticipation, placebo/nocebo biology, PNEI/neuroimmune signalling, and
perioperative immune conditioning.

---

## 2. Decision (Q1): yes — as a **cross-cutting modifier layer**, not a fifth attack vector

**The four attack vectors are fixed (golden rule §8); host biology does not become V5.** This mirrors the
resolution of issue #7, which became the value-of-information *layer* (ADR-0001), not a new vector. The
reason is structural, not bureaucratic:

- **The four vectors act *on the tumour cell*** — they throttle the CIC-DUX4 oncogenic loop (V1), reduce
  new-translocation risk (V2), restore the suppressor/differentiation program (V3), or restore immune
  visibility/clearance of fusion-positive cells (V4). Each names a molecular target inside or on the
  cancer cell.
- **Host factors act on the *system the tumour sits in*** — the immune compartment, the inflammatory and
  metabolic milieu, the microbiome, drug pharmacokinetics, and treatment tolerability. They rarely have a
  CIC-DUX4 target; they change the *gain* on the vectors and on standard-of-care, and the *probability* a
  given vector's effect is realised in a living patient.

So host biology is **orthogonal** to the vectors: a **conditioning / modifier layer** that multiplies or
attenuates vector and SOC efficacy and tolerability. Concretely it maps onto the existing structure as:

| Host axis | Primarily modifies | Mechanistic handle |
|---|---|---|
| Microbiome / SCFA, systemic immune tone | **V4** (immune watchdog) and any future checkpoint/NK approach | gut-immune axis sets baseline T-cell/NK competence and CPI responsiveness |
| Systemic inflammation (NLR, CRP, mGPS) | **V2** (inflammatory DSB context) + **V4** + prognosis | inflammatory tone is both a DSB/genomic-instability promoter and an immunosuppressive (MDSC/neutrophil) signal |
| Metabolic / nutritional / sarcopenia status | **SOC chemo tolerability & dose-intensity** (VDC/IE, high-dose ifosfamide) | body-composition and reserve drive toxicity, dose reductions, and delivered dose-intensity |
| Physical activity | SOC tolerability, fatigue, body composition | exercise preserves muscle, modulates inflammation and immune trafficking |
| Sleep / circadian, autonomic (ANS), psychological stress / PNEI | **V4** + SOC + (preclinically) metastatic seeding | β-adrenergic / glucocorticoid signalling → immune suppression and pro-metastatic stromal programs |
| Placebo / nocebo | **symptom and tolerability endpoints only** — *not* tumour control | expectancy → subjective symptom and adherence effects; no antitumour mechanism |
| Perioperative immune conditioning | the surgical/metastasectomy window | transient β-blockade + COX-2 inhibition blunt the surgery-induced pro-metastatic catecholamine/prostaglandin surge |

The layer therefore plugs in as an **annotation on V4 and on the SOC backbone**, plus a small set of
**forward hypotheses** — not as a competing list of tumour-targeted compounds.

---

## 3. Variability between similar tumours (Q2): yes — this is the mechanistically expected place for it

Two patients with histologically and genomically identical CIC-rearranged tumours can diverge in outcome
because **treatment response is an emergent property of tumour × host × therapy**, exactly as the issue
frames it. The best-evidenced channels for that divergence:

- **Immunotherapy responsiveness is partly host-encoded.** Gut-microbiome composition predicts anti-PD-1
  response in melanoma/NSCLC/RCC cohorts (Routy *et al.* Science 2018, PMID 29209380; Gopalakrishnan
  *et al.* Science 2018, PMID 29097493; FMT conversion of non-responders, Davar *et al.* Science 2021).
  *Evidence tier: Clinical-Trial / Clinical-observational — in melanoma/NSCLC, **not sarcoma.*** Already
  catalogued in `v4-immune-watchdog/microbiome-immune.md`; not re-derived here.
- **Systemic inflammation is independently prognostic in soft-tissue sarcoma.** Elevated
  neutrophil-to-lymphocyte ratio (NLR) and modified Glasgow Prognostic Score (mGPS; CRP + albumin) track
  worse OS/DFS in STS cohorts and meta-analysis (e.g. Bone Joint J 2022 international multicentre mGPS
  study, PMID 34969280; STS NLR meta-analysis, PMC6133428). *Evidence tier: Clinical (prognostic
  association) in STS broadly; none CIC-DUX4-specific.*
- **Reserve and body composition drive delivered dose-intensity.** Sarcopenia predicts higher
  chemotherapy toxicity and worse survival in STS — including a cohort treated with **adriamycin +
  ifosfamide**, the backbone closest to this case (Support Care Cancer 2025, PMID 39921759; advanced/
  metastatic STS, PMID 34318390). Two "identical" tumours treated at different effective dose-intensities
  are not receiving the same therapy.

So host factors are a *legitimate and partly measurable* source of inter-patient heterogeneity — not a
hand-wave. Crucially, several of them (NLR, CRP/albumin → mGPS, L3 skeletal-muscle index) are **already
measurable from routine bloods and the staging CT** — i.e. they are cheap Tier-A data in the VoI sense,
not exotic assays.

---

## 4. Which factors have sufficient evidence (Q3): the catalog

Each factor: dominant **mechanism** (molecular, not analogy), **evidence tier** (contract vocabulary),
**transfer/confidence** to CIC-DUX4 specifically, **what it modifies**, and **direction**. "Sufficient
to *include*" means there is a real, tiered mechanism worth carrying as a conditioning factor — **not**
that it is proven to change CIC-sarcoma outcomes (almost none are).

| Host factor | Mechanism (molecular) | Tier | CIC-DUX4 direct? | Modifies | Direction / honest caveat |
|---|---|---|---|---|---|
| **Gut microbiome / SCFA** | Microbiota-trained DC/T-cell priming; SCFA (butyrate/propionate) HDAC + Treg/Teff balance; barrier integrity reduces LPS-driven suppression | Clinical-Trial (melanoma/NSCLC CPI); Mechanistic for systemic SCFA | None | V4 / future CPI | **Beneficial for CPI responsiveness — but directionally double-edged:** systemic butyrate promotes Treg (potentially *pro*-tolerogenic). Reuse `microbiome-immune.md`. |
| **Systemic inflammation (NLR, CRP, mGPS)** | Neutrophil/MDSC expansion, IL-6/CRP axis; immunosuppressive + pro-genomic-instability milieu | Clinical (prognostic, STS) | None direct | V2, V4, prognosis | High inflammatory index = worse prognosis and likely poorer immune-approach yield. Prognostic ≠ a treatment target by itself. |
| **Metabolic status / sarcopenia / body composition** | Muscle reserve & inflammatory-metabolic state govern chemo clearance, toxicity, dose-intensity | Clinical (STS, incl. adria/ifosfamide) | None direct | SOC tolerability | Sarcopenia → more toxicity, reduced delivered dose-intensity. Directly relevant to imminent high-dose ifosfamide. |
| **Nutritional status** | Protein-energy reserve, albumin, micronutrient sufficiency support marrow recovery and mucosal integrity | Clinical (supportive-care, general oncology) | None direct | SOC tolerability | Malnutrition worsens tolerance/outcomes. **Correct deficiency, not "boost" — no megadose framing** (see §6). |
| **Physical activity / exercise** | Preserves muscle; modulates systemic inflammation (↓IL-6/CRP), insulin/IGF axis, immune-cell mobilisation | Clinical-Trial (tolerability/fatigue/QoL across cancers); Mechanistic for outcome | None | SOC tolerability, body composition | ACSM 2019 roundtable consensus supports exercise during treatment (Patel *et al.* Med Sci Sports Exerc 2019;51:2391, PMC6814265). Outcome benefit best evidenced in breast/colon, **not sarcoma**. |
| **Sleep / circadian biology** | Circadian control of cortisol, cell-cycle (clock genes), DNA-repair timing; chronotherapy hypotheses | Mechanistic / Preclinical; limited Clinical chronotherapy | None | V2/V4, SOC timing | Plausible and biologically grounded; *clinical* chronotherapy evidence in sarcoma is essentially absent. Tag honestly as Mechanistic. |
| **Autonomic / β-adrenergic (ANS) tone** | Sympathetic norepinephrine → β2-AR on tumour/stroma/immune cells → pro-angiogenic, pro-metastatic, immunosuppressive signalling | Preclinical-Animal (strong); retrospective clinical mixed | None direct | V4, metastatic seeding | Robust mouse mechanism; β-blocker clinical-outcome data inconsistent. Do not over-read retrospective β-blocker "survival" associations. |
| **Psychological stress / PNEI / CTRA** | Conserved Transcriptional Response to Adversity: SNS β-adrenergic + HPA glucocorticoid signalling → ↑inflammatory, ↓type-I-IFN leukocyte gene programs (Cole, Curr Opin Behav Sci 2019, PMID 31592179) | Mechanistic / Preclinical-Animal; human gene-expression observational | None | V4, immune competence | Real, well-characterised neuroimmune pathway. **Human cancer-*survival* effect of stress interventions is weak/unproven** — carry as immune-context modifier, not an antitumour therapy. |
| **Placebo / nocebo** | Expectancy → descending modulation of symptom perception, autonomic/endocrine shifts; adherence effects | Established (for *symptom/subjective* endpoints) | N/A | **Symptom & tolerability endpoints only** | **Honest boundary: placebo does not control tumours.** Relevant to fatigue/nausea/pain and adherence, and to trial design (nocebo inflating "toxicity"); not an anticancer mechanism. |
| **Perioperative immune conditioning** | Surgery triggers catecholamine/prostaglandin surge that is pro-metastatic & immunosuppressive; brief perioperative propranolol + etodolac (COX-2) blunts it | Clinical-Trial (biomarker endpoints) | None direct | Surgical / metastasectomy window | Phase-II biomarker RCTs in breast (Shaashua *et al.* Clin Cancer Res 2017, PMID 28490464) and colorectal (Haldar *et al.* Cancer 2020, doi:10.1002/cncr.32950) improved metastasis biomarkers; **survival benefit not established; not tested in sarcoma.** Pharmacologic, not lifestyle — screen vs SOC (§6). |

**Inclusion verdict:** all ten clear the bar to be *carried as conditioning factors* because each has a
real tiered mechanism. Only three reach **Clinical-grade evidence usable for stratification today** in
sarcoma specifically — **systemic inflammation (NLR/mGPS), sarcopenia/body composition, and nutritional
status** — and these are notable precisely because they are *measurable from routine labs and the
staging CT*. The rest are Mechanistic-to-Clinical-in-other-tumours and belong in the **forward lane**.

---

## 5. How to weight host vs. tumour-targeted evidence (Q4): reuse the three existing axes — do **not** invent a new score

The framework already has the machinery to weight this honestly (ADR-0004's three scoring axes, loaded by
every agent via `sarcoma-contract`). Host modifiers are scored on the **same** axes; the weighting falls
out naturally:

1. **Evidence tier** (axis 1) — unchanged vocabulary. Most host factors land Mechanistic → Clinical
   (rarely in sarcoma).
2. **Confidence / transfer-to-CIC-DUX4** (axis 2, `docs/08`) — **this is the axis that does the
   down-weighting.** Nearly all host evidence is from *other tumour types* (melanoma/NSCLC microbiome) or
   *general oncology* (exercise, nutrition), so the **Directness** sub-score is low and the
   transfer-distance discount is large. That is not a new rule — it is the existing confidence axis doing
   its job. The microbiome chain ("melanoma microbiome → CPI response → sarcoma CPI → CIC-DUX4 CPI") is
   the canonical example of a long, lossy inductive path.
3. **Translational feasibility** (axis 3, `translational-feasibility-layer.md`) — host modifiers tend to
   score *high* on access (exercise, nutrition, sleep are F1 "accessible now"), which is exactly why the
   feasibility axis must be kept distinct from confidence: **easy to access is not the same as likely to
   work.** Conflating the two is the central risk with lifestyle factors.

**Weighting principle (the answer to Q4):** host-modifier hypotheses enter the **confirmatory lane at
attenuated confidence** relative to a direct tumour-targeted mechanism of equal tier, because the
transfer distance (axis 2) is almost always larger. They are catalogued as **conditioning / tolerability
/ immune-context modifiers**, not as tumour-targeted hypotheses competing for the top of `protocol-v1.md`.
But — **two-lane rule (golden rule §5)** — a high-feasibility, low-confidence host idea is **not pruned**;
it can be a strong **Forward Hypothesis**. This is the same principle ADR-0001 articulated for issue #8:
uncertainty in an input attenuates how strongly the downstream recommendation is propagated, it does not
delete the idea.

> **Follow-up refinement (issue #10 follow-up / ADR-0014):** the "transfer distance" invoked above is now
> scored on an explicit graded **biological-proximity ladder** — P0 CIC-DUX4 → P1 fusion round-cell family
> → P2 sarcoma → P3 solid-tumour-with-named-mechanism → P4 pathway-only — see
> `docs/10-evidence-transferability-hierarchy.md`. It confirms the commenter's point directly: broader
> host-biology evidence (most of this layer is P2/P3) is **admitted at downgraded confidence, never
> excluded on CIC-DUX4-rarity grounds** — only a missing mechanistic bridge excludes. §5's worked
> examples (sarcopenia P2, microbiome→CPI P3) are scored against the ladder in that doc.

**Three guardrails specific to host factors (where they most often go wrong):**
- **Directionality is not assumed beneficial.** Systemic butyrate → Treg can be *pro*-tolerogenic;
  broad probiotics *reduced* anti-PD-1 response in a melanoma cohort. "Gut health = good" is not safe to
  assume.
- **Prognostic ≠ targetable.** NLR/mGPS/sarcopenia predict outcome; that does not mean an intervention
  moving the marker moves the outcome. Carry them as stratifiers and tolerability levers, not as targets.
- **"Natural ≠ safe," correct-deficiency ≠ supraphysiologic-boost** (contract hard-refusal rule). The
  ATBC/SELECT antioxidant-harm precedents apply to the nutrition axis.

---

## 6. Standard-of-care interaction flags (this layer is not interaction-free)

Most host axes (exercise, sleep, microbiome diet, psychological support) carry **no pharmacologic SOC
interaction** at non-supplement levels. Two need explicit flags:

- **Perioperative immune-conditioning drugs are real drugs.** Propranolol (β-blocker) and **etodolac /
  any NSAID-COX-2 inhibitor** are pharmacologic. NSAIDs + **ifosfamide** raise nephrotoxicity concern
  (both nephro-stressing; ifosfamide tubular toxicity), and NSAIDs affect platelet function around
  surgery; β-blockade interacts with anaesthesia haemodynamics. **Any perioperative β-blockade/COX-2
  protocol is a clinician-run trial-context decision, never a self-administered adjunct.** Screen via
  `sarcoma-chemo-interactions`.
- **Nutrition/supplement overlap.** Megadose antioxidant "nutritional support" collides with the V2
  antioxidant-harm analysis and with ROS-dependent chemo; defer to `v2-compiler-protection/` and the
  chemo-interaction skill. Probiotic caution during the peri-CPI / neutropenic window is already covered
  in `microbiome-immune.md`.

---

## 7. Atypical-case note (fusion-unconfirmed ~5%)

**Every factor in this layer is FUSION-AGNOSTIC.** Host modifiers act on the immune/metabolic/inflammatory
host system, not on the CIC-DUX4 junction. They therefore apply **unchanged** to the ~5% clinically/
histologically CIC-rearranged tumours with no confirmed fusion — this is, in fact, one of the few layers
where the atypical-case caveat is *fully relieved* rather than triggered. (Contrast with junction ASOs or
junction-specific vaccines, which the atypical case may exclude.)

---

## 8. Forward Hypotheses

**[Forward Hypothesis 1] A composite host-inflammatory/reserve index (mGPS + NLR + L3 skeletal-muscle
index) as a pre-treatment stratifier for whether V4 immune approaches and full-dose ifosfamide are worth
attempting in CIC-rearranged sarcoma.**
*Mechanistic basis:* high systemic inflammation (MDSC/neutrophil-skewed) and sarcopenia both predict
immunosuppression and poor chemo tolerance; in an already immunologically "cold" tumour, a high-inflammation/
low-reserve host may be the patient in whom checkpoint approaches are least likely to yield and dose
reductions most likely. *Test:* retrospective then prospective correlation of baseline mGPS/NLR/SMI with
(a) delivered ifosfamide dose-intensity and toxicity and (b) any checkpoint-exposure response, pooled
across sarcoma histotypes (CIC is too rare alone). All inputs are routine bloods + staging CT — zero new
assays. *Axes:* tier Clinical (prognostic), confidence moderate (STS-broad, not CIC-specific), feasibility
F1 (data already collected).

**[Forward Hypothesis 2] Pre-/peri-cytotoxic "prehabilitation" (resistance exercise + protein-energy
nutrition) to preserve skeletal-muscle reserve and delivered dose-intensity through high-dose ifosfamide.**
*Mechanistic basis:* sarcopenia drives ifosfamide toxicity and dose reduction (PMID 39921759); preserving
muscle could protect delivered dose-intensity — the thing that actually treats the tumour. The hypothesis
is about **protecting the SOC**, not replacing it. *Test:* randomised prehabilitation vs standard care in
sarcoma patients entering anthracycline/ifosfamide, primary endpoint delivered dose-intensity and
grade-3+ toxicity, secondary SMI change. *Axes:* tier Clinical-Trial (exercise oncology, other cancers),
confidence moderate, feasibility F1.

**[Forward Hypothesis 3] A perioperative β-adrenergic + COX-2 blockade window around sarcoma
metastasectomy (e.g. pulmonary metastasectomy) to blunt the surgery-induced pro-metastatic surge.**
*Mechanistic basis:* the catecholamine/prostaglandin surge after surgery is pro-metastatic and
immunosuppressive; brief propranolol + etodolac improved metastasis biomarkers in breast/colorectal
Phase-II RCTs (PMID 28490464; Cancer 2020). Sarcoma lung metastasectomy is a defined surgical window.
*Test:* biomarker-endpoint pilot RCT in sarcoma patients undergoing metastasectomy, mirroring the
Ben-Eliyahu design; endpoints = tumour/circulating metastasis biomarkers, not survival initially.
*Axes:* tier Clinical-Trial (biomarker, other cancers), confidence low-moderate (no sarcoma data),
feasibility F2–F3 (repurposed generics, but needs a trial and careful ifosfamide/NSAID-nephrotoxicity
and perioperative screening). **Forward-lane only — not an adjunct to self-administer.**

---

## 9. What I could not establish

1. **Any host-factor → outcome data in CIC-rearranged sarcoma specifically.** Every entry transfers from
   other sarcoma histotypes, other tumour types, or general oncology. None is CIC-DUX4-validated.
2. **Whether moving a prognostic host marker (NLR, mGPS, SMI) changes outcome.** These are associations;
   the interventional question is open in sarcoma.
3. **Sarcoma-specific microbiome–CPI data** — none exists (see `microbiome-immune.md`).
4. **Survival (not biomarker) benefit of perioperative β-blockade/COX-2**, in any tumour — the trials are
   biomarker-endpoint; and none is in sarcoma.
5. **Clinical chronotherapy / sleep-timing benefit** in sarcoma — mechanistic only.
6. **Magnitude of any stress-intervention effect on cancer immunity in humans** — the CTRA pathway is well
   characterised at the gene-expression level, but the downstream clinical-outcome effect of modifying it
   is weak/unproven.
7. **Exact PMIDs for two cited items** were not independently reopened here: the ACSM 2019 roundtable is
   anchored to PMC6814265 (Med Sci Sports Exerc 2019;51:2391) and the colorectal perioperative trial to
   Haldar *et al.* Cancer 2020 (doi:10.1002/cncr.32950); both titles/journals were verified via live
   search, the breast-trial PMID 28490464 and Cole PMID 31592179 were confirmed. Treat the two
   PMC/DOI-anchored items as `[VERIFY]` for the exact PubMed ID before any external citation.

---

*Research-simulation note, not medical advice. This layer documents how host-level factors are
*represented and weighted* in the framework; it is not a recommendation to start, stop, or modify any
lifestyle, supplement, drug, or treatment.*
