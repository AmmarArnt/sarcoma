# 08 — Evidence Hierarchy, Confidence Scoring & Weak-Signal Handling

**Status:** Design proposal (responds to GitHub Issue #8 — *"Evidence hierarchy and confidence
scoring for generated hypotheses"*).
**Author:** Claude Code session, 2026-06-02.
**Scope of this document:** It (a) answers the three questions raised in the issue, (b) specifies a
concrete, implementable scoring layer, (c) works the scheme on real entries from `protocol-v1.md`,
and (d) lists the exact skill/doc edits that would wire it into the agents — *deferred to maintainer
approval, not applied in this PR*. Nothing here changes the existing `protocol-v1.md` or any skill.

> **Not medical advice.** This is a research-simulation framework document. It governs how hypotheses
> are *labeled and ranked*, not what anyone should take.

---

## 0. TL;DR — the three answers

**Q1 — "Would it be useful to introduce an evidence hierarchy and confidence-scoring layer?"**
Yes, with one important correction: the framework *already has* an evidence hierarchy (the 7-tier
vocabulary in `sarcoma-contract`). What it is missing is (i) a **clinician-facing roll-up** of those
tiers into the familiar A–E bands the issue describes, and (ii) a **confidence score that is
orthogonal to the tier**. Tier answers *"what kind of evidence is this?"*; confidence answers *"how
much should I believe this specific claim transfers to CIC-DUX4 in a living patient?"* Those are
different axes, and conflating them is the actual gap. We should **add** the confidence axis and the
A–E roll-up; we should **not replace** the 7-tier vocabulary (replacing it loses information — see §2).

**Q2 — "Should evidence level influence how strongly a hypothesis is *propagated* through the
simulation, rather than serving only as a descriptive label?"**
Yes for the **confirmatory catalog** (ranking and display prominence in the Naturally-Achievable and
Clinical/Experimental tracks) — and the orchestrator already does an informal version of this. **No
for the Forward-Hypotheses lane.** Gating idea-generation by evidence weight would directly violate
the framework's golden rule #5 ("known research is the floor, not the ceiling"). The design below is
therefore explicitly **two-lane**: evidence weight drives the confirmatory lane; the forward lane is
ranked by *plausibility × falsifiability × novelty* and is exempt from evidence-weight pruning (§4).

**Q3 (follow-up comment) — "How should the framework handle unusual but potentially informative
observations that fall outside conventional evidence hierarchies (investigator self-experimentation,
unusual case reports, weak signals — e.g. Beata Halassy)?"**
With a dedicated, **quarantined Weak-Signal Register** (§5). Such observations are *not* assigned an
evidence tier (assigning one would let them propagate as evidence, which is exactly the failure mode
to avoid). They are logged with full provenance, an honest weakness list, and — the key requirement —
a **falsifier**: the experiment that would convert the anecdote into a testable hypothesis. They feed
*only* the Forward-Hypotheses lane, never the confirmatory tracks. Worked on the Halassy case in §5.2.

---

## 1. What the framework already does

`sarcoma-contract` mandates that every claim carry exactly one **Evidence Tier**:

```
Established > Clinical-Trial > Preclinical-Animal > Preclinical-Cell > Mechanistic
            > Dietary-Observational > Theoretical
```

and the orchestrator (`sarcoma-orchestrator-intake`) already:
- preserves the **strongest tier** when deduplicating a compound across vectors;
- **ranks** by (a) tier, (b) mechanistic alignment with CIC-DUX4 specifically, (c) cross-vector
  synergy, (d) safety/feasibility — in that order;
- carries an output-level **Confidence: high/medium/low** line (per `sarcoma-output-schema`);
- separately tracks "**CIC-DUX4 specific?**", **concentration mismatch**, and **conflicts**.

So three of the four ingredients of a real confidence score (directness-to-CIC-DUX4,
concentration/exposure achievability, cross-source consistency, conflict overhang) are *already being
recorded* — just not composed into a single, consistently visible per-entry score. This proposal
formalizes what is already implicit rather than inventing a new apparatus.

---

## 2. Why not simply adopt the issue's A–E hierarchy?

The A–E scheme proposed in the issue is a clinical/GRADE-style hierarchy. It is excellent for a
*clinician reader* but, used as the **atomic label**, it loses information this framework depends on:

| Issue's band | Collapses these distinct 7-tier states into one |
|---|---|
| **D** — "preclinical / animal / cell-line" | `Preclinical-Animal`, `Preclinical-Cell`, **and** `Mechanistic` — three very different confidence states. A PDX result and a "pathway-plausible, no data" claim would share a band. |
| **E** — "computational / network / transcriptomic / hypothesis-generating" | `Theoretical` **and** the in-silico sims in `sims/` — but a DepMap CRISPR dependency (real public data) is not the same epistemic object as an untested idea. |

The framework's whole value is the granularity at the *bottom* of the evidence stack (where almost
all of its entries live: Mechanistic / Preclinical-Cell). A–E has its resolution at the *top* (RCTs,
guidelines) where this disease has essentially nothing. **So: keep the 7-tier as the atomic label,
and add A–E as a roll-up for readability.** Crosswalk:

| 7-tier (atomic, keep) | A–E roll-up (add, clinician-facing) |
|---|---|
| Established (FDA/EMA/guideline) | **A** |
| Clinical-Trial (registered human trial) | **B** |
| Preclinical-Animal (mouse/rat/PDX) | **C** |
| Preclinical-Cell (cell line) | **D** |
| Mechanistic (pathway plausibility, no direct data) | **D** (flagged "mechanistic — no experimental data") |
| Dietary-Observational (epidemiology) | **C/E** — **C** if a large prospective cohort, **E** if associational only *(annotate which)* |
| Theoretical / Forward Hypothesis | **E** |

> Note the one genuine ambiguity: `Dietary-Observational` spans a large prospective cohort (closer to
> B/C) and a loose associational claim (E). The roll-up therefore **requires the annotation** rather
> than hard-coding a band — this is itself a small improvement the exercise surfaced.

---

## 3. The confidence axis (orthogonal to tier)

**Tier ≠ confidence.** A `Preclinical-Cell` finding can be high-confidence-for-what-it-is (consistent
across many lines, mechanism clear, concentration achievable) or near-worthless (one line, 50 µM, no
in-vivo route). The confidence score captures *that* second dimension. It is built from four axes that
the framework already tracks — so scoring is auditing existing fields, not new research:

| Axis | Question | `+` | `0` | `−` (hard-minus) |
|---|---|---|---|---|
| **D — Directness** | Is the evidence *in* CIC-DUX4 / a close fusion sarcoma? | In CIC-DUX4 or close fusion sarcoma | In generic cancer, defensible transfer | Pathway-inferred only / transfer weak |
| **A — Achievability** | Is the active concentration/exposure reachable in vivo by the proposed route? | Reachable (e.g. approved drug at label dose) | Uncertain / borderline | Concentration mismatch ≥10× (canonical dietary failure) |
| **R — Reproducibility** | Do independent sources agree? | ≥2 independent concordant sources | Single source | Sources conflict |
| **X — Conflict overhang** | Any unresolved SOC interaction or harm signal? | Clean | Manageable / monitorable | Unresolved SOC conflict or documented harm signal |

> **D-axis refinement (ADR-0014, issue #10 follow-up):** the three-level Directness above is coarse — it
> lumps "another fusion-driven round-cell sarcoma (Ewing)" with "a generic carcinoma." Use the graded
> **biological-proximity ladder** in **`docs/10-evidence-transferability-hierarchy.md`** when scoring D:
> **P0** index disease (CIC-DUX4) → **P1** same molecular family (Ewing/BCOR/DSRCT/EWSR1-non-ETS) →
> **P2** sarcoma broadly → **P3** solid tumour *with a named conserved mechanism* → **P4** pathway-only
> → **floor** (no mechanistic bridge → not admitted; route to §5 register). The operating rule: *rarity
> moves a candidate down the ladder (lower confidence), it never excludes it* — only the absence of a
> mechanistic bridge excludes. Proximity sets **D only**; A/R/X are unchanged.

**Confidence label** (deterministic rubric — *bands, not false-precision numbers*):

- **High** — tier is `Established`/`Clinical-Trial`, **and** ≥3 axes `+`, **and** no hard-minus.
- **Moderate** — mechanism is direct **or** achievable (≥1 of D/A is `+`), no hard-minus dominates,
  mixed otherwise.
- **Low** — tier ≤ `Preclinical-Cell` **and** at least one hard-minus (most commonly the A-axis
  concentration mismatch).
- **Speculative** — `Theoretical` / Forward Hypothesis. **Confidence is not scored**; a *falsifier* is
  required instead (see §4/§5).

Rationale for bands over a single number: a 0–100 "confidence %" invites exactly the over-precision
the issue warns against ("reduced risk of over-weighting promising but early-stage findings"). Four
auditable axes + a four-value label is transparent and reproducible; a magic number is neither.

---

## 4. Propagation: the two-lane rule (answer to Q2)

Define **propagation weight** = used *only* to order entries and decide display prominence. It applies
to the **confirmatory lane** and is computed as the existing orchestrator ranking, now made explicit:

```
propagation weight (confirmatory lane) =
    tier rank  (Established > … > Dietary-Observational)
    then CIC-DUX4 directness (D axis)
    then confidence label (High > Moderate > Low)
    then cross-vector synergy (R axis), then safety/feasibility
```

That is what the issue asks for in Q2, and it is a light formalization of `sarcoma-orchestrator-intake`
§3 + the confidence axis from §3.

**The Forward-Hypotheses lane is exempt.** It is ranked by:

```
forward-lane rank = biological plausibility × falsifiability (is there a clean experiment?) × novelty
                    — NOT by evidence weight
```

This is non-negotiable and follows golden rule #5. The two lanes must stay visibly separate in any
output (they already are, in `protocol-v1.md`: "Naturally Achievable" / "Clinical / Experimental" vs.
"Forward Hypotheses"). A `Theoretical`/`Speculative` entry that would rank last in the confirmatory
lane can legitimately rank *first* in the forward lane if it is highly falsifiable and novel. **Letting
evidence weight prune the forward lane would convert this framework from a hypothesis generator into a
literature summarizer — the exact failure the README forbids.**

---

## 5. The Weak-Signal Register (answer to the follow-up: n-of-1, self-experimentation, case reports)

### 5.1 Why a separate lane

Observations like investigator self-experimentation, single unusual case reports, and "biologically
plausible but hard to publish/replicate" findings are real information, but they **do not fit any
evidence tier**:

- they are *not* `Theoretical` (a `Theoretical` claim is untested; an n-of-1 *is* an observation);
- they are *not* `Clinical-Trial` / `Preclinical-*` (no controlled design, n=1, uncontrolled
  confounding, publication/selection bias, often concurrent standard therapy);
- forcing them into a tier would let them **propagate as evidence** — the precise over-weighting the
  issue wants to prevent.

So they get a **quarantined register** that is *explicitly not evidence-tiered*. Required fields per
entry:

| Field | Purpose |
|---|---|
| Observation | What was seen, in one sentence. |
| Provenance | Who, where, peer-reviewed?, n, design. Real citation or `[no direct citation]`. |
| Confounders / weaknesses | The honest list — concurrent therapy, selection/publication bias, no control, etc. |
| Plausible mechanism | If any — tagged `Mechanistic` *for the mechanism only*, never for the anecdote. |
| **Falsifier** | The experiment that would convert this signal into a testable hypothesis. **Mandatory.** |
| Routing | Which Forward Hypothesis (and vector) it feeds. Never the confirmatory tracks. |
| Quarantine stamp | Literal: *"Weak signal — NOT evidence-tiered, NOT propagated as evidence."* |

A signal **leaves** the register only by being tested (then it enters the normal tier system at
whatever tier the new data earns) or by being discarded as noise. Until then it lives only in the
forward lane.

### 5.2 Worked example — Beata Halassy (the case the commenter raised)

| Field | Entry |
|---|---|
| Observation | A virologist self-administered intratumoural oncolytic virotherapy (Edmonston-Zagreb measles strain, then VSV-Indiana) for recurrent breast cancer at a mastectomy site; reported tumour shrinkage/softening enabling resection and ~4 years disease-free. |
| Provenance | Peer-reviewed **case report**, n=1, self-experimentation. Forčić D. *et al.* (B. Halassy, senior/subject author), *Vaccines (Basel)* 2024, 12(9):958. DOI 10.3390/vaccines12090958 (PMC11435696). Nature news coverage d41586-024-03647-0. Rejected by >12 journals over self-experimentation ethics. |
| Confounders / weaknesses | n=1; uncontrolled; **concurrent/subsequent standard therapy** (post-OVT trastuzumab + surgery) confounds attribution; investigator is the subject; breast cancer ≠ CIC-rearranged sarcoma; no immune-correlate time-course in the tumour. |
| Plausible mechanism | OVT drives **immunogenic cell death + type-I IFN**, recruiting immune effectors independent of tumour MHC-I level — `Mechanistic` *(mechanism only)*. |
| **Falsifier** | In a CIC-DUX4 PDX or syngeneic model: does intratumoural MeV/VSV produce immune-mediated regression of an **MHC-I-low** tumour, and is the effect lost on NK **and** CD8 depletion? If regression requires intact MHC-I, the "MHC-I-independent visibility" rationale for CIC-rearranged disease fails. |
| Routing | **V4 (Immune Watchdog)** Forward Hypotheses — see below. **Not** routed to any confirmatory track. |
| Quarantine stamp | *Weak signal — NOT evidence-tiered, NOT propagated as evidence.* |

**Forward Hypothesis it generates (V4):** *Oncolytic virotherapy could restore immune visibility of
MHC-I-low CIC-rearranged cells through a route that does not depend on epigenetic MHC-I restoration.*
This is genuinely complementary to the catalog's central V3→V4 bridge (EZH2i/HDACi → MHC-I → T-cells)
and to its NK missing-self arm: an MHC-I-low clone that has escaped T-cell surveillance is the *hardest*
case for the epigenetic-priming strategy, and OVT-driven ICD plus NK missing-self recognition is a
mechanistically distinct second route at exactly that failure point. Tag: `Theoretical`; tested by the
falsifier above. (This is hypothesis space — deliberately bold per golden rule #5, and explicitly *not*
evidence.)

The point of the worked example: the framework **uses** the Halassy signal (it produced a real,
non-obvious forward hypothesis that plugs into V4) **without ever** letting an n-of-1 self-experiment
masquerade as evidence. That is the behavior the issue is asking for.

---

## 6. Worked re-scoring of existing `protocol-v1.md` entries

Applying §2–§3 to four real Top-Level Findings, to show the layer adds signal (nothing in
`protocol-v1.md` is modified — this is illustrative):

| Entry (abbrev.) | Current tag | Tier | A–E | D | A | R | X | **Confidence** | What the score surfaces |
|---|---|---|---|---|---|---|---|---|---|
| BRD4/super-enhancer (BET) as fusion-agnostic entry point | *Clinical-Trial; no direct CIC-DUX4 data* | Clinical-Trial | **B** | 0 | + | + | 0 | **Moderate→High** | Strong tier + achievable + reproducible BETi data, but D=0 (no direct CIC-DUX4 trial) keeps it off "High". Honest. |
| EZH2i (tazemetostat) → MHC-I, V3→V4 bridge | *Established (epithelioid sarcoma); Clinical-Trial (CIC)* | Established | **A** | 0/+ | + | + | 0 | **High** | Top of confirmatory lane — correctly. |
| Dietary sulforaphane MHC-I / HDAC effect | *Preclinical-Cell* | Preclinical-Cell | **D** | − | − (juicing → ~0 yield; 5–30 µM) | 0 | 0 | **Low** | The A-axis hard-minus is the real story; the layer makes "do not over-weight this" explicit and visible, which is the issue's stated goal. |
| OVT for MHC-I-low visibility (from §5.2) | n/a | Theoretical | **E** | − | n/a | n/a | n/a | **Speculative** | Not scored for confidence; carries a falsifier; lives in the forward lane only. |

The scheme behaves: it pushes the genuinely strong items up, makes the dietary concentration-mismatch
demotion *explicit per entry* (today it is narrated in prose), and keeps the bold idea in the forward
lane without dressing it as evidence.

---

## 7. Implementation plan (deferred — for maintainer approval, NOT applied in this PR)

If accepted, wiring this in is small and additive (no rewrite of existing outputs):

1. **`sarcoma-contract` skill** — add an "A–E roll-up" crosswalk table (§2) and the four-axis
   confidence rubric (§3) beside the existing tier vocabulary. Keep the 7-tier as the atomic label.
2. **`sarcoma-output-schema`** — add two columns to the per-entry tables (`A–E` and `Confidence
   (D/A/R/X)`) and a new top-level **Weak-Signal Register** section to the orchestrator schema.
3. **`sarcoma-orchestrator-intake`** — state the propagation-weight formula (§4) explicitly and add
   the two-lane rule (confirmatory ranked by evidence weight; forward lane exempt).
4. **`sarcoma-pre-output-check`** — add one failure mode: *"weak signal / n-of-1 / self-experiment
   assigned an evidence tier or propagated to a confirmatory track."*
5. **A `protocol-v2.md`** (new file, per CLAUDE.md §0 — do not clobber `protocol-v1.md`) regenerated
   under the layer, so the baseline is preserved.

Each is an additive edit; none changes the no-fabrication / mechanism-before-recommendation /
SOC-interaction rules. Recommend doing 1–4 as one PR after sign-off, then 5 as a separate regeneration.

---

## 8. What I could not establish / limitations

- **No external validation of the rubric.** The four axes and band thresholds are a defensible design,
  not a measured instrument; inter-rater reliability is untested. They should be treated as a
  *transparency aid*, not a quantitative truth claim.
- **The `Dietary-Observational` → A–E mapping is genuinely ambiguous** (§2) and is left as a required
  annotation rather than a fixed band. That is a limitation, not a fully solved mapping.
- **Confidence bands are deliberately coarse (4 values).** This is a choice against false precision,
  but it means two "Moderate" entries can differ materially; the four-axis breakdown is what
  disambiguates them, so it must always be shown, not just the label.
- **The Weak-Signal Register's value depends on discipline.** Its entire safety rests on the quarantine
  stamp and the mandatory falsifier being enforced (proposed `pre-output-check` failure mode, item 4).
  Without that enforcement the register would become a back door for anecdote-as-evidence — the very
  thing it exists to prevent.

---

## 9. Bibliography

- Forčić D., Mršić K., Perić-Balja M., Kurtović T., Ramić S., Silovski T., Pedišić I., Milas I.,
  Halassy B. *An Unconventional Case Study of Neoadjuvant Oncolytic Virotherapy for Recurrent Breast
  Cancer.* **Vaccines (Basel)** 2024; 12(9):958. DOI 10.3390/vaccines12090958. PMC11435696.
- *This scientist treated her own cancer with viruses she grew in the lab.* **Nature** (news), 2024.
  d41586-024-03647-0. *(secondary/news source — context only.)*
- Internal: `docs/00-README.md` (golden rules, two-lane principle), `.claude/skills/sarcoma-contract`
  (7-tier vocabulary), `.claude/skills/sarcoma-orchestrator-intake` (existing ranking),
  `simulation-output/protocol-v1.md` (entries re-scored in §6).
