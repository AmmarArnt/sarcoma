# Diagnostic Strategy & Expected-Information-Gain Layer ("What should we learn next?")

**In response to GitHub issue #31** — *"Diagnostic Strategy Optimization and Information Gain Analysis"*
(@Cerimagic).

> **See also (this layer composes, it does not replace):**
> [`biomarker-voi-stratification.md`](biomarker-voi-stratification.md) (Sim 6 /
> [ADR-0001](../docs/adr/0001-missing-data-taxonomy-and-voi-layer.md)) ranks unknown **variables**;
> [`biomarker-voi-provenance-extension.md`](biomarker-voi-provenance-extension.md)
> ([ADR-0011](../docs/adr/0011-voi-provenance-temporal-axis.md)) adds **where the answer comes from** and
> **at what acquisition burden**; the
> [driver-uncertainty model](tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md) (Sim 8 /
> [ADR-0008](../docs/adr/0008-driver-uncertainty-decision-model.md)) computes **EVSI** for the
> driver-resolving tests. This layer aggregates those to the **diagnostic-action** level and adds a
> constraint-aware *sequencing* rule.

**Status:** framework-enhancement (a new standing analytical layer / [ADR-0015](../docs/adr/0015-diagnostic-information-gain-layer.md)).
Research-simulation output, **not medical advice**, **not a recommendation to obtain any specific test**,
**not a diagnosis**. The goal, exactly as the issue framed it, is to let the framework ask *"what should we
**learn** next?"* alongside *"what should we **treat** next?"* — and to make the value, cost, and
sequencing of diagnostic actions explicit, **not** to mandate testing.

**Confidence: medium.** The action→variable resolution maps and the qualitative interactions are
well-grounded in standard molecular pathology and reuse two already-executed decision models; the
*sequencing* is a transparent heuristic over those, and the cross-currency composite is a **judgment, not a
single fabricated score** (see §6). **Evidence tier of this layer:** `Theoretical / Mechanistic` (a
decision-analytic composition over qualitative models — it does not outrank any real-data finding).

---

## 1. The question, restated

The issue observes that the framework can rank *therapeutic* hypotheses but has limited ability to evaluate
**diagnostic** ones — which test would most reduce uncertainty, which missing biomarker would most change
treatment selection, which investigations are **low-yield**, and how the diagnostic pathway should adapt
under **budget / time / tissue** constraints. It asks the framework to estimate the **expected information
gain (EIG)** of candidate diagnostic actions (molecular profiling, fusion analysis, immune profiling,
circulating biomarkers, imaging, histopathological reassessment, liquid biopsy).

**Short answer: most of the machinery already exists, but at the wrong granularity.** Sim 6 and Sim 8 score
*variables* and the *driver question*; the issue asks about *actions* (tests/orders). One test resolves a
**bundle** of variables at once, consumes a shared resource (tissue), and its value depends on **what
earlier tests already resolved**. This layer lifts the existing value estimates to the action level and
adds the missing piece — **sequential, constraint-aware prioritization** — without inventing new numbers.

---

## 2. The unit of decision is the diagnostic *action*, not the variable

A diagnostic action **A** is a single orderable test. It is characterized by four things:

1. **Variable bundle it resolves** — the set of latent variables it reports (e.g. a multiplex immune stain
   reports nectin, HLA-E, MHC-I/B2M, CD8 TIL, FoxP3 in one pass).
2. **Decision value (two currencies, kept separate — do not conflate):**
   - **EVSI** (decision-value / bits) for the **driver** sub-decision — *which vectors are on-target* —
     taken directly from Sim 8 (`test_value_of_information.csv`).
   - **Decision-flip VoI** (fraction of background states in which the answer changes the program) for the
     **immune-route** sub-decision — *which route inside V4* — taken from Sim 6 (`voi_ranking.csv`).
   - These answer **different** sub-decisions, so a test's leverage is a **small profile, not a scalar**.
     We deliberately do **not** fabricate a single blended EIG number (§6).
3. **Acquisition burden** — provenance class **P1 archived / P2 fresh / P3 liquid** and its marginal
   cost / procedural risk / **tissue consumption**, from ADR-0011.
4. **Timepoint** it characterizes — **T0 baseline / T1 current / TΔ change** (ADR-0011). For the
   therapy-modifiable immune markers, the *current* (T1) read dominates the cheap *baseline* (T0) read.

**Non-additivity (the load-bearing caveat).** Variable VoIs are **decision-flip frequencies**, not bits, so
a bundle's value is **not the sum** of its members' VoIs — overlapping flips double-count, and once one test
resolves the sub-decision the marginal value of a second test on the same sub-decision falls toward zero.
The register below therefore reports the **bundle profile** and ranks by *dominant* leverage + burden, not
by an arithmetic total.

---

## 3. Diagnostic-action register — current case (fusion-unconfirmed, post-VDC/IE, lung relapse)

Reusing Sim 8 EVSI and Sim 6 decision-flip VoI verbatim (no new numbers). Feasibility F-bands per
`translational-feasibility-layer.md` (ADR-0003) — **perishable, re-verify before external use**.

| Action | Resolves (bundle) | Driver EVSI (Sim 8) | Immune-route VoI (Sim 6) | Provenance / burden | Timepoint | Access |
|---|---|---|---|---|---|---|
| **A1 Nuclear DUX4 IHC** | DUX4-transactivation-domain Q (licenses MCL1 / junction lines) | **1.678** | — | **P1 archived**, near-zero risk, 1 slide | T0 (fixed) | **F1** |
| **A2 Genome-wide methylation array** | CIC methylation class vs BCOR/Ewing → collapses D4 phenocopy | **1.049** | — | **P1 archived**, low | T0 | **F1/F2** |
| **A3 Long-read WGS + RNA-seq** | Cryptic CIC-DUX4 junction + rare partner (D1/D2/D3) **and** genomic features (e.g. CDKN2A) | **1.865** (highest) | — | **P2 fresh preferred** (needs high-MW DNA), high cost/risk | T0/T1 | **F2** |
| **A4 Multiplex immune IHC panel** | **6 variables, one block** — nectin CD155/CD112 (0.625), HLA-E (0.500), FoxP3/Treg (0.312), TIGIT (0.312), MHC-I/B2M (0.188), CD8 TIL (0.188) | — | bundle, **0.625 → 0.188** | P1 archived **baseline** *or* P2 fresh **current** | T0 vs **T1 (dominant)** | meas. **F1** (nectin/HLA-E assay maturity `[VERIFY]`) |
| **A5 NK functional reserve assay** | Live NK count/fitness (post-WLI/chemo) | — | **0.250** | **P2/P3 only** — *unrecoverable from archive* | T1, host-side | F2 |
| **A6 ctDNA / liquid biopsy (junction MRD)** | Serial junction tracking / MRD — **requires a resolved junction first** | — (not a front-line resolver) | — | **P3**, lowest burden, repeatable | T1 serial | F2/F3 `[VERIFY CIC-DUX4]` |
| **A7 Restaging imaging (CT ± FDG-PET, oligomet mapping)** | Disease extent / local-therapy eligibility — a **staging** decision, not vector selection | not modeled | not modeled | imaging, non-tissue | T1 serial | **F1** |

**Reading.** Three actions carry most of the *driver* leverage (A1/A2/A3); one action (A4) carries most of
the *immune-route* leverage as a single archived-or-fresh bundle. A5 and A6 are narrow but each fills a gap
no other action can (live NK; non-invasive serial monitoring). A7 sits on a **different decision axis**
(staging) and is treated separately in §5.

---

## 4. The sequencing rule — "what should we learn next?"

The issue's core ask is *ordering under constraint*. The decision-analytic answer is a **greedy
realizable-VoI-per-unit-burden** loop, re-evaluated after each result because **(a)** tissue is consumed,
**(b)** results gate downstream value (a methylation "notCIC" zeroes the CIC-directed bundle — Sim 8
`test_unlock_map.csv`), and **(c)** cheap archived reads dominate the burden ratio.

> **Standing rule (proposed).** Rank candidate diagnostic actions by **dominant decision value ÷
> acquisition burden**, subject to tissue/budget/time. Run the **archived (P1) bundle first** (it is
> near-zero marginal risk and front-loads both driver-resolution and route-selection leverage); spend the
> one **expensive fresh (P2)** action only on the **residual delta** that archive cannot answer; treat
> **liquid (P3)** as downstream monitoring; run **imaging on its own staging cadence** in parallel.
> Re-rank after every result — a resolved sub-decision drops every remaining test that only informed it.

Applied to the current case (assuming a usable diagnostic block exists — itself unknown to the simulation):

1. **Archived bundle first (P1, F1, one block):** A1 DUX4 IHC + A2 methylation + A4 *baseline* immune IHC.
   This is the highest realizable VoI-per-burden step — it can resolve the phenocopy question, license-or-
   exclude the contingent MCL1/junction lines, and give a first immune-route read at **no new procedural
   risk**. (Mirrors the ADR-0011 finding that cheap leverage is FFPE-front-loaded.)
2. **Fresh increment only for the residual delta (P2, F2):** A3 long-read junction recovery (the *one* test
   that genuinely needs high-MW DNA), the **current (T1)** immune read (A4 repeated — the markers most
   subject to immune editing under VDC/IE + whole-lung RT), and A5 live NK — **and only if** a contingent
   program (junction-specific therapy, or the V4 NK-first route) is actually on the table. If the archived
   bundle already commits you to the five driver-robust vectors (Sim 8 Finding 1), the fresh biopsy's
   marginal decision value may be small — spend it deliberately, not reflexively.
3. **Liquid (P3):** A6 ctDNA only **after** a junction is resolved — then it is a low-burden serial MRD tool,
   not a front-line resolver.
4. **Imaging (A7):** independent staging track (§5).

This is precisely the "expand-then-narrow, learn-before-treat" loop the issue describes, made explicit and
auditable.

---

## 5. The two honest gaps the issue surfaces

**5a. Imaging is not modeled.** The issue lists imaging modalities, and none of the existing sims assign
imaging an information value. Imaging's decision value here is real but lives on a **different axis** —
*staging / local-therapy eligibility* (is the lung relapse still oligometastatic and amenable to
metastasectomy/SBRT?), not *vector selection*. That value is genuine and often **management-changing**, but
we have **no quantitative VoI model** for it and will **not fabricate one**. Treated qualitatively:
restaging CT and (where indicated) FDG-PET inform the local-control decision and biopsy targeting; their
"information gain" is in the staging decision tree, which this catalog does not yet represent. Flagged as
forward work (§7). `Theoretical` / `[VERIFY clinical cadence with treating team]`.

**5b. Low-yield register (the action-level Tier C).** Investigations unlikely to change *this* decision —
recorded with the reason, per the Tier-C discipline:

- **Static baseline PD-L1 IHC** — low VoI in the model because PD-L1 is encoded as IFN-induced/adaptive
  (Sim 6 Tier C); a static pre-treatment value rarely enters the program choice. *Caveat: a modeling
  property, stated not hidden.*
- **Repeat short-read FISH / targeted panel for the fusion** after a prior negative — the cryptic-junction
  problem (DUX4 D4Z4 repeats; FISH false-negative 14–46%, Sim 8) means a *repeat of the same modality* adds
  little; the information lives in a **different** modality (long-read), not a re-run.
- **ctDNA before a junction is resolved** — no patient-specific assay target exists yet (§3 A6).
- **Generic serum tumor markers with no CIC linkage** — no path to a vector or route decision in this model.
- **Re-imaging inside the restaging interval** with no new clinical question — burden without decision value.

---

## 6. Honest limitations (what this does and does NOT claim)

- **No single blended EIG number.** Driver EVSI (bits / decision-value) and immune-route VoI (decision-flip
  frequency) are **different currencies answering different sub-decisions**; collapsing them into one score
  would require weighting assumptions that are not data. We present the **profile** and a **qualitative**
  composite ordering, explicitly labeled as judgment. (Same discipline as ADR-0011's uncomputed
  "realizable VoI.")
- **Bundle values are non-additive.** Decision-flip frequencies cannot be summed across a panel; §2 states
  this. The register ranks by dominant leverage + burden, not by a total.
- **Acquisition-burden bands are qualitative.** No dollar/time costs are invented; P1/P2/P3 + low/high are
  ordinal, per ADR-0011.
- **Imaging VoI is unquantified** (§5a) — a real gap, named not papered over.
- **Inherits all Sim 6 / Sim 8 / Sim 4 limitations** — qualitative Boolean kill-rule logic, a
  literature-anchored (swept) driver prior, transferred (non-CIC-DUX4-validated) mechanism edges,
  single-cell-line baseline (GSE60740). A decision-analytic layer cannot exceed the models it composes.
- **Not a testing recommendation, not a diagnosis.** Whether the patient's archived block exists, is
  exhausted, or matches the relapse lesion is **unknown to the simulation**; the timing of any fresh biopsy
  relative to imminent high-dose ifosfamide is a clinical-stewardship question for the treating team, **not
  medical advice**.

**What I could not establish:**
- A defensible single composite EIG metric across the two value currencies (left deliberately uncomputed).
- Quantitative information value for **imaging** (no model; §5a).
- CIC-DUX4-specific ctDNA performance (extrapolated from EWSR1-fusion ddPCR; `[VERIFY]`, inherited from
  ADR-0011).
- Whether this patient's prior work-up already included DUX4 IHC / methylation — if it did, condition the
  register on those results (several actions would drop to low-yield).
- Clinical-grade assay maturity for nectin (CD155/CD112) and HLA-E IHC `[VERIFY]` (inherited).

---

## 7. Forward work (mechanistically defensible, not executed here)

- **[Forward / proposed Sim 9] A quantitative test-level diagnostic-strategy simulation.** Model each
  diagnostic action as a **variable-bundle** with an explicit tissue/budget/time constraint and compute a
  **greedy EVSI-per-burden** sequence (with tissue as a depletable resource and result-gated downstream
  value). *Why not now:* the action→variable resolution map and per-test burden weights would be
  **assumptions**, and the sims obey a real-data-only rule — so this is flagged as forward work, not
  fabricated. *Falsifier of the current heuristic:* if a fresh-only quantity (live NK reserve, or a selected
  relapse **subclone** with a distinct vulnerability) flips the program regardless of any archived read,
  then "archived bundle first" is wrong for that case and the fresh biopsy carries the decisive VoI.
- **[Forward] An imaging/staging decision sub-tree** so restaging and local-therapy eligibility carry an
  explicit (even qualitative) decision value rather than sitting outside the framework (§5a).

---

## 8. Atypical-case flag (unchanged)

The **driver-resolution actions (A1–A3) *are* the resolution of the fusion-unconfirmed status** — they are
the highest-leverage learning step for this ~5% subgroup (Sim 8). The **fusion-agnostic** actions (A4
immune IHC, A5 NK assay, A7 imaging) inform the driver-robust vectors and apply **regardless** of fusion
status. The junction-dependent downstream (A6 ctDNA junction-MRD, and any junction-specific therapy it
would monitor) remains **contingent on a confirmed, resolved fusion**.

---

*Provenance:* composes `simulation-output/biomarker-voi-stratification.md` (Sim 6 —
`voi_ranking.csv`), `simulation-output/biomarker-voi-provenance-extension.md` (ADR-0011), and
`simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md` +
`sims/08-driver-uncertainty/` (`test_value_of_information.csv`, `test_unlock_map.csv`). All EVSI / VoI
figures are reproduced verbatim from those artifacts — **no new biology, no new numeric model, no fabricated
citations.** Entities ground to genes/markers already grounded in Sims 6/8.

*Decision record:* adopted via [ADR-0015](../docs/adr/0015-diagnostic-information-gain-layer.md)
(issue #31). Not medical advice. Research simulation / hypothesis generation only.
