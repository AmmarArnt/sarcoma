# ADR-0024: Surveillance-window host/mitochondrial lane — autophagy, food and natural agents while NED and off treatment

- **Status:** Accepted
- **Date:** 2026-09-17
- **Origin:** Maintainer question (2026-09-17), follow-up to ADR-0023 — asked for creative work on
  **autophagy, food and natural remedies** as they relate to mitochondrial function, explicitly because
  the anchored patient is now **in a control/observation arm: NED, monitored, on no medication**, and
  asked for hypothetical/theoretical ideas that might help **keep** the patient in NED.
- **Deciders:** maintainer + Claude Code session
- **Artifacts:** `simulation-output/surveillance-window-host-mitochondrial-lane.md`
- **Relates to:** ADR-0023 (mitochondrial/endosymbiotic layer — this extends it into the host-directed
  M8 modality), ADR-0005 (host-biology modifier layer — this **upgrades its exercise row** and surfaces an
  internal conflict in its autonomic row), ADR-0021 (persister/reservoir spine — the compartment this lane
  targets), ADR-0022 (Era B), ADR-0018 (modality axis — M8), ADR-0011 (provenance — FH-11.5 uses archived
  P1 tissue), ADR-0013 (attrition reasons), ADR-0014 (transferability ladder), ADR-0020 (`[VERIFY]` gate +
  the symmetric/refresh lane), ADR-0009 (findings register), ADR-0017 (red-team self-challenge).

## Context

Two gaps converged.

**First, a context the framework had never modelled.** Every prior artifact assumes a patient either on
standard-of-care chemotherapy or choosing among candidate agents. The anchored patient is now in a
**no-treatment surveillance window** — NED, monitored, no medication. That regime has structurally
different properties, and the framework's own dominant safety gate behaves differently in it: the VDC/IE
chemo-interaction screen (golden rule #7) is the constraint that shapes most dietary reasoning in this
repo, and while nothing is being administered it **largely lifts** (and re-arms the moment treatment
resumes). Conversely, the *combination* framing that most of the promising host/dietary literature relies
on (FMD + chemotherapy, ketogenic + anti-PD-L1, DHA + drug) is **unavailable**, so every hypothesis in this
window must stand alone — which makes golden rule #5's "was it monotherapy?" question cut *against* the
interventions being proposed rather than for them.

**Second, a lane ADR-0023 opened but did not work.** ADR-0023 established that the post-NED reservoir is
the unsolved compartment and that its vulnerability is lipid-redox (GPX4/ferroptosis unified with the
OXPHOS-high/FAO phenotype), but it was written almost entirely in the **pharmacological** register
(BCL-XL/DT2216, SHMT2, complex-I inhibitors, MCT inhibitors). Its §3 also flagged, without developing it,
that **autophagy inhibition may awaken dormancy** — i.e. that the direction of autophagy-directed
intervention was unresolved. The host-directed (M8) half of the mitochondrial layer was therefore
unwritten precisely for the window the patient is actually in.

A third factor made this urgent rather than merely incomplete: a surveillance window is the setting with
**the most patient motivation and the least evidence** in oncology, which is exactly where
confident-sounding advice does damage. The framework's contract already carries the rule **"no 'natural =
safe' framing,"** naming β-carotene in smokers, vitamin E in SELECT, and selenium's narrow window — but it
carried those as unexplained empirical warnings. ADR-0023's reservoir model turns out to supply a
**mechanism** for them.

## Decision

Adopt a standing **surveillance-window host/mitochondrial lane**: the M8 (dietary/host-directed) working of
ADR-0023, scoped to the no-treatment window and governed by ADR-0005's host-biology weighting. **Not a
fifth vector** (golden rule #8).

Five rules follow.

1. **The window is a named context with its own constraint profile.** Any host/dietary reasoning must state
   which regime it assumes. While off treatment: the chemo-interaction gate is dormant *and re-arms on
   resumption*; the **antioxidant-vs-residual-disease** conflict is *more* relevant, not less, because
   residual disease is the window's entire premise; combination-only evidence does not transfer; and
   chronic-exposure risk replaces acute-interaction risk.
2. **Autophagy has no agreed direction in a dormant reservoir — do not assign it one.** The literature is
   genuinely split: autophagy **sustains** dormant cells and its inhibition kills them via
   damaged-mitochondria/ROS accumulation (Nat Commun 2018 PMC5964069; Breast Cancer Res 2024; and a human
   recurrence-prevention pilot, CLEVER/NCT03032406) **versus** autophagy inhibition **awakening** dormancy
   via Pfkfb3 (PMC6694140). Outputs state the split and decline to pick a side. Consequence: fasting,
   spermidine and especially **urolithin A** are **directionally ambiguous** for the reservoir, and
   interventions of this class are to be justified on **host-immune** grounds — where the evidence is more
   consistent — never on "autophagy fights cancer."
3. **A standing "wrong-signed register" is part of this lane.** Where the reservoir model predicts a
   *popular natural agent* works **for** the reservoir, that prediction is recorded with its mechanism and
   its tier, on equal footing with positive hypotheses. This is the symmetric-lane obligation (ADR-0020)
   applied to nutraceuticals, and it is the lane's most decision-relevant output because it argues against
   things that are easy to start and easy to take daily for years. Charter entries: **selenium above
   sufficiency** (GPX4 is a selenoprotein; PMID 29290465), **vitamin E / tocotrienols** (α-tocopherol
   hydroquinone inhibits 15-LO via iron reduction; PMID 30110365), **thiol antioxidants/NAC** (feeds the
   GSH-consuming GPX4 reaction; plus the pre-existing NAC-metastasis signal), **ketogenic diet** (the
   β-hydroxybutyrate paradox — oxidative cells *consume* ketones, PMC5331634 — against an OXPHOS-high
   reservoir), **urolithin A** (mitophagy induction relieves the damaged-mitochondria/ROS pressure that is
   the dormant-cell kill mechanism), and **iron manipulation** (recorded as *contested*, with the direct
   negative PMC13089158). The register never instructs anyone to stop anything, and it preserves the repo's
   standing rule: **correct deficiency, don't megadose.**
4. **Justification grounds must be stated, not just the intervention.** Items are organised by *why*
   (immune-surveillance · membrane-lipid · measurable-host-variable · not-justified), because in this
   evidence-thin setting the grounds carry more information than the list.
5. **Surveillance is not displaced.** Outputs in this lane state explicitly that the scans and visits
   remain the intervention with established value in this window, and that every item is a question for the
   treating team rather than a plan.

**Evidence-refresh action taken under ADR-0020.** **CHALLENGE (CCTG CO.21)** — phase 3, n=889, structured
exercise **after** adjuvant chemotherapy in resected colon cancer: **DFS HR 0.72**, 5-year DFS 80.3% vs
73.9%, 8-year OS 90% vs 83%, median follow-up 7.9 years (*NEJM* 2025, DOI 10.1056/NEJMoa2502760, PMID
40450658). This **upgrades ADR-0005's exercise row from "Mechanistic for outcome" to "Clinical-Trial
(phase 3, DFS and OS)"** in colon cancer; the row's "**not sarcoma**" caveat stands unchanged, and the
sarcoma literature remains function/gait/QoL only, with one review stating the effect of increased activity
on sarcoma progression is **unknown**. Its dissected mechanism (Pedersen, *Cell Metab* 2016, PMID 26895752:
>60% tumour reduction across five models, abolished by NK depletion, requiring epinephrine and IL-6) makes
it the **NK-dependent, fusion-agnostic** intervention best matched to the framework's standing NK-first
thesis. Per the Era-B rule, the Era-A artifact is **not rewritten**: an additive dated pointer was added to
`host-biology-modifier-layer.md` and the register row updated.

## Consequences

**What changed in the framework's standing positions:**

- **A new context exists** (the surveillance window) with a documented constraint profile, so future
  host/dietary questions are answered against the right regime rather than against an implied on-treatment
  one.
- **ADR-0005's exercise row is upgraded** to phase-3 outcome evidence (in colon), and exercise becomes the
  highest-tier item in the entire host-directed lane — ahead of every supplement.
- **An internal conflict in ADR-0005 is surfaced and given a proposed resolution**: its autonomic row
  (chronic sympathetic/β2 tone is pro-metastatic) versus Pedersen's finding that the **epinephrine pulse is
  required** for exercise's NK mobilisation and that β-blockade blunts it. Proposed reconciliation:
  **tonic vs pulsatile** adrenergic signalling (FH-11.3). Recorded as a hypothesis, not a finding — no
  source states it in those terms.
- **Omega-3 acquires a reservoir-specific mechanism.** The register's existing "best cross-vector dietary
  compound, absent from the regimen" row gains a named target: DHA induces ferroptosis in patient-derived
  organoids **and drug-tolerant cells** while **sparing normal-tissue organoids** (PMID 41963291) — which
  partially answers ADR-0023's **commons objection** — and PUFA peroxidation is potentiated by the **acidic**
  microenvironment ADR-0023 §4B describes as an immune weapon, closing a loop between the two surfaces.
- **The contract's "natural ≠ safe" rule gains a mechanism.** SELECT tested **selenium + vitamin E** —
  on this biology, the two most direct dietary reinforcements of the reservoir's anti-ferroptotic defence.
  The convergence is recorded as an explicitly **post-hoc mechanistic hypothesis** about a clinical
  finding whose endpoint was prostate-cancer incidence, not sarcoma recurrence.

**Costs and risks accepted:**

- **No sarcoma recurrence-outcome evidence exists for anything in this lane** — not one item. The strongest
  is colon cancer (P3).
- **Everything is `[VERIFY]`.** Literature egress and `clinicaltrials.gov` remained HTTP 403 on
  2026-09-17. CHALLENGE's numbers were **concordant across several independent secondary sources**, which
  raises confidence materially but is **not** verification; CLEVER's trial status is unverified. Forward
  lane; no protocol promotion.
- **The lane inherits ADR-0021/0023's load-bearing uncertainty.** If the relapse was a pre-existing
  metastatic clone rather than a persister state, the ferroptosis-reservoir premise fails and §5, most of
  §6, and three of five forward hypotheses lose their basis.
- **The ferroptosis-reservoir link is `Low`-confidence P4** with no sarcoma model, so the wrong-signed
  register is a *mechanistic argument*, not a demonstrated risk. It must never be read as "these
  supplements caused or will cause relapse."
- **A real counter-argument is left unresolved by design.** V2 (compiler protection) argues *for*
  antioxidant sufficiency to reduce new genomic damage; this lane argues *against* antioxidant excess near
  residual disease. Both can hold — they concern different compartments — but a reader who sees only one
  gets the wrong idea, so both are stated in-artifact.
- **Much of the top recommendation is not novel.** "Exercise, eat well, get your labs read" is standard
  survivorship guidance. The red-team pass concedes this explicitly: the mitochondrial frame's durable
  contribution here is the **wrong-signed register** (which no general guideline predicts), not the
  discovery of exercise.
- **No simulation was run.** The §7 ordering is judgment. Sim 11 (proposed in ADR-0023) now has a concrete
  first question from FH-11.2 (does selenium/α-tocopherol titration shift the GPX4-inhibitor IC₅₀ in a
  round-cell persister model?). Entity grounding remains blocked (`huggingface.co` unreachable).

**Guardrail — stronger than usual for this ADR.** This lane touches things a motivated patient can act on
today without a prescription, so its outputs carry **no dosing, no start/stop instructions, and no dietary
or supplement recommendations**, and they state that published human-trial ranges appear only as part of
describing what a study did. Outputs must also state that **surveillance itself remains the intervention of
established value** in this window, and that every item belongs to the treating oncology team.

## Alternatives considered

- **Answer the question conversationally without a new artifact.** Rejected: the maintainer's question
  named a context the framework had never modelled, and the wrong-signed register is exactly the kind of
  content that must be written down and maintained rather than delivered once in chat.
- **Fold it into ADR-0023 as another section.** Rejected: ADR-0023 is the mechanism catalogue; this is a
  **context** (the no-treatment window) with its own constraint profile, its own justification grammar, and
  a standing register. It also *upgrades* a different ADR (0005), which is cleaner as its own record.
- **Fold it into ADR-0005 (host biology).** Rejected for the same reason ADR-0023 was not folded there:
  ADR-0005 catalogues host modifiers generically and conditions SOC tolerability. This lane is
  reservoir-directed and window-specific, and it *changes* one of ADR-0005's rows — an amendment recorded
  from outside is more honest than a silent edit to an Era-A artifact.
- **Decline the "natural remedies" framing as unscientific.** Rejected: the framework already admits
  ethnopharmacology as a *mechanism source* under ADR-0018 provided it passes the standard gauntlet, and
  the honest answer to this question turned out to contain real, decision-relevant biology — including
  several findings that argue *against* popular natural interventions, which is more useful than a refusal.
- **Give a practical protocol (what to eat, how much to exercise).** Refused on the standing guardrail: no
  dosing, no prescriptive numbers, no start/stop instructions. The lane supplies mechanisms, tiers,
  falsifiers and honest negatives; a plan for a specific person is the treating team's.
- **Lead with the mechanisms (§4–5) and put the negatives later.** Rejected as the more satisfying and
  less honest ordering — the same reasoning ADR-0023 applied to its §3, and the steer-audit records that
  the question's framing pulled toward an enthusiastic list.
