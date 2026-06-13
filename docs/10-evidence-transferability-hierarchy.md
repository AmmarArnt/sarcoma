# 10 — Evidence-Transferability Hierarchy (Biological-Proximity Ladder)

**Status:** Accepted methodology refinement (responds to the **issue #10 follow-up comment**,
@Cerimagic, 2026-06-12). Recorded as **ADR-0014**; refines the confidence axis of **ADR-0004 /
`docs/08`** and directly supports the host-biology layer (**ADR-0005**) it was raised against.
**Author:** Claude Code session, 2026-06-13.

> **Not medical advice.** This is a research-simulation framework document. It governs how evidence is
> *weighted by biological distance from CIC-DUX4*, not what anyone should take. It changes no existing
> `protocol-v*.md` entry and invents no new score.

---

## 0. TL;DR — the answer to the follow-up

The commenter's concern is correct and the proposed hierarchy is **adopted**, with one framing
correction and a completion of the ladder downward.

- **Correction of framing:** this is **not a new axis or a new score.** It is a *refinement of one
  existing sub-axis* — the **Directness (D)** sub-score of the confidence axis (`docs/08` §3). Today D
  has only three coarse levels (`+` CIC-DUX4 or close fusion sarcoma / `0` generic cancer, defensible
  transfer / `−` pathway-inferred). The commenter is right that the collapsed middle hides a real
  gradient: "another fusion-driven round-cell sarcoma (Ewing)" and "a generic carcinoma" should not
  share one bucket. This doc replaces the 3-level D with a **graded proximity ladder (P0–P4 + a
  mechanistic-bridge floor).**
- **Operating rule (the heart of the request):** *rarity is never a reason to exclude.* A candidate is
  excluded only when there is **no mechanistic bridge** to the named CIC-DUX4 target/pathway — never
  because CIC-DUX4 is too rare to have generated a dedicated study. Disease-rarity moves a candidate
  **down the proximity ladder (lower confidence), it never removes it from the search space.** This is
  exactly what golden rules #5 ("known research is the floor") and #6 ("distinguish evidence in
  CIC-DUX4 from evidence in cancer broadly") already intend; the ladder makes the attenuation **graded
  and auditable** instead of a coarse three-way cut.
- **Where it plugs in:** it feeds the **confidence label** (`docs/08` §3) and therefore the
  **confirmatory-lane** ordering only. Per the **two-lane rule**, proximity discounting *attenuates
  confidence; it never prunes the Forward-Hypotheses lane.* A long-transfer-distance host-biology idea
  stays alive as a forward hypothesis — which is precisely the outcome the commenter wants.

---

## 1. The concern, restated

From the follow-up comment: keep CIC-specific evidence at the top, but do **not** narrow the search
space so aggressively that mechanistically conserved host-biology / immune-context evidence becomes
*artificially excluded*. Many relevant pathways (exercise, systemic inflammation, autonomic signalling,
perioperative biology, NK-cell fitness, COX-2, sleep/circadian, nutrition) are **not inherently
CIC-DUX4-specific** — they are conserved across sarcomas and across solid tumours. With the fusion
status unresolved and CIC-specific datasets extremely limited, the commenter proposes an **explicit
hierarchy rather than a hard restriction**:

> 1. CIC-rearranged / CIC-DUX4 evidence (highest)
> 2. Fusion-driven round-cell sarcomas
> 3. Sarcomas in general
> 4. Solid tumours with strong mechanistic transferability
>
> …broader evidence does not need to be excluded; it can simply enter at lower confidence.

That is right, and it is the correct *shape* for the Directness sub-axis. Below is the formalization.

---

## 2. The proximity ladder (the refined Directness sub-axis)

The four levels the commenter proposed become **P0–P3**; the framework's existing `−` ("pathway
inferred only") becomes **P4**, and a hard floor (no mechanistic bridge → not admitted as evidence) is
made explicit. Each tier carries a confidence handle, **not** a numeric weight (bands over false
precision, per `docs/08` §3).

| Proximity | What it is | Example (CIC context) | Old D | Confidence handling |
|---|---|---|---|---|
| **P0 — Index disease** | CIC-rearranged / CIC-DUX4 sarcoma itself | a CIC-DUX4 cell-line or patient series | `+` | **Full weight** for its tier. The reference point. |
| **P1 — Same molecular family** | Other fusion-driven **undifferentiated round-cell sarcomas** — the WHO "Ewing-like" family: Ewing (EWSR1-FLI1/ERG), *BCOR*-rearranged, DSRCT (EWSR1-WT1), round-cell sarcoma with EWSR1-non-ETS fusions | BET/BRD4 dependence shown in Ewing; epigenetic MHC-I priming in a fusion round-cell line | `+` (lumped) | **Small discount.** Shared transcription-factor-fusion / super-enhancer / epigenetic biology makes transfer the most defensible non-index case. |
| **P2 — Sarcoma broadly** | Other sarcomas (soft-tissue, osteosarcoma, synovial, RMS) | NLR/mGPS prognostic in STS; sarcopenia → ifosfamide toxicity in an adria+ifosfamide STS cohort | `0` (lumped) | **Moderate discount.** Shared mesenchymal lineage + frequently shared SOC backbone (VDC/IE). |
| **P3 — Solid tumour + explicit mechanistic bridge** | Carcinoma / melanoma / NSCLC etc., admitted **only when the *named molecular mechanism* is conserved and the bridge is stated** | microbiome → anti-PD-1 response (melanoma/NSCLC); EZH2i → antigen-presentation (epithelioid sarcoma / other PRC2-context tumours) | `0` (lumped) | **Larger discount.** Admitted *with* the explicit conserved mechanism; the transfer chain's length is itself a confidence cost. |
| **P4 — Pathway-inferred only** | Mechanism plausible but **no tumour-context data**, or transfer rests on a long lossy inductive chain | "butyrate is an HDAC inhibitor, therefore…" with no tumour data | `−` | **Hard-minus on D.** Mechanistic-tier at best; forward-lane unless/until tumour-context data appear. |
| **floor — no mechanistic bridge** | No conserved, *named* link to a CIC-DUX4 target/pathway | a finding whose only connection is "it's cancer" | n/a | **Not admitted as evidence.** May still enter the **Weak-Signal Register** (`docs/08` §5) as a forward-lane signal *if* it is a real observation with a falsifier. |

**Reading the ladder:** P0→P4 is monotonic confidence attenuation on the **Directness sub-axis only**.
The other three confidence sub-axes — **A**chievability-in-vivo, **R**eproducibility, conflict over**X**hang
(`docs/08` §3) — are unchanged and still apply independently. Proximity does not touch them: a P1
finding can still be Low-confidence overall if it has a ≥10× concentration mismatch (A-axis hard-minus).

**The one bright line:** the boundary that excludes is **mechanistic, not taxonomic.** A solid-tumour
finding with a conserved, named mechanism (P3) is *in*; a finding with no mechanistic bridge is *out of
the evidence tracks* (but may route to the weak-signal register). Rarity of CIC-DUX4 affects only which
*rung* a candidate sits on, never whether it is admitted.

---

## 3. Why this is admission-with-downgrade, not exclusion (the two-lane guarantee)

The commenter's worry — "discarding potentially useful host-biology signals not because the biology is
implausible, but because CIC-DUX4 is too rare" — is exactly the failure the **two-lane rule** already
forbids (`docs/08` §4, golden rule #5):

- The proximity discount feeds the **confidence label**, which **orders and annotates the confirmatory
  lane**. A P3/P4 host-biology item enters the confirmatory lane at *attenuated confidence* — it is not
  deleted, it is ranked honestly.
- The **Forward-Hypotheses lane is exempt from evidence-weight (and therefore proximity) pruning.** It
  is ranked by *plausibility × falsifiability × novelty*. A P3 conserved-mechanism idea with a clean
  falsifier can rank **first** in the forward lane while ranking low in the confirmatory lane. That is
  the designed escape hatch for "mechanistically conserved but disease-distant" evidence — i.e. most of
  the host-biology layer.

So "keep CIC-specific at the top, admit broader evidence at lower confidence, never discard plausible
biology" is not a new policy — it is the two-lane rule plus this graded D-axis, working together.

---

## 4. Interaction with fusion-uncertainty (why the ladder matters *more* here, ADR-0008)

The commenter notes the fusion status is unresolved. That observation strengthens the case for the
ladder, via the **driver-uncertainty decision model** (`sims/08-driver-uncertainty/`, ADR-0008):

- When the driver is a **latent variable**, P0 ("CIC-DUX4-specific") evidence is itself **contingent on
  the driver actually being CIC-DUX4** — its effective weight is multiplied by the posterior probability
  of the cryptic-fusion hypothesis (D1 in the driver model).
- **P1 evidence (the fusion-round-cell family) is driver-robust** — it transfers across most of the
  plausible driver hypotheses (CIC-DUX4, CIC-other-partner, BCOR, Ewing-like), because the shared
  biology is the fusion-oncoprotein/super-enhancer/round-cell program, not the exact junction.
- **Consequence:** under fusion-uncertainty the *effective* gap between P0 and P1 **narrows.** Broader
  fusion-family and conserved-mechanism evidence becomes *relatively more* valuable, not less — exactly
  the commenter's intuition, now with a mechanism. (This mirrors the driver-uncertainty finding that
  throttle/cell-cycle/immune vectors are driver-robust while the junction-specific "re-arm" hypothesis
  is driver-contingent.)

---

## 5. Worked examples (drawn from the host-biology layer this was raised against)

Applying §2 to real entries from `host-biology-modifier-layer.md` and `protocol-v1.md` (nothing in
those files is modified — illustrative):

| Entry | Proximity | Mechanistic bridge (named) | Net confidence read |
|---|---|---|---|
| **Sarcopenia → ifosfamide toxicity / reduced dose-intensity**, shown in an **adriamycin+ifosfamide** STS cohort (PMID 39921759) | **P2** (sarcoma; near-exact regimen) | body-composition reserve governs cytotoxic clearance/toxicity | **Highest** host-biology read — small discount; the regimen overlap pulls it toward P1 in practice. Usable for stratification today. |
| **NLR / mGPS prognostic in soft-tissue sarcoma** (PMID 34969280) | **P2** (sarcoma broadly) | systemic inflammation = MDSC/neutrophil-skewed immunosuppressive + pro-genomic-instability milieu | Moderate discount; prognostic, **not** shown targetable — `Clinical (prognostic)`, confidence moderate. |
| **BET/BRD4 dependence** (catalog V1/V3) demonstrated in **Ewing** | **P1** (fusion round-cell family) | shared transcription-factor-fusion → super-enhancer addiction | **Small discount** — the ladder's headline gain: the old coarse D lumped this at `0`; it is genuinely closer than a carcinoma result and should rank above one. |
| **Gut microbiome → anti-PD-1 response** (melanoma/NSCLC; Routy 2018 PMID 29209380) | **P3** (solid tumour + bridge) | gut-immune axis sets baseline T-cell/NK competence & CPI responsiveness | **Larger discount** — long lossy chain (melanoma → sarcoma → CIC). Admitted *with* the named mechanism; forward-lane / immune-context modifier, not a confirmatory top pick. |
| **EZH2i → MHC-I / antigen presentation** (epithelioid sarcoma approval context) | **P3 on disease, but P0/P1 on mechanism** | PRC2 / H3K27me3 de-repression of the antigen-presentation program is *directly* relevant to the V3→V4 MHC-I bridge | Admitted at higher confidence than its disease-distance alone implies, **because the mechanism is the conserved object** — illustrates that the bridge, not the tumour label, sets the rung. |
| **"Butyrate is an HDAC inhibitor, therefore antitumour in CIC"** with no tumour data | **P4** | HDAC inhibition (mechanism only) | Hard-minus on D; Mechanistic tier; forward-lane only until tumour-context data exist. |

The EZH2i row is the important subtlety: **proximity is scored on the *mechanism being transferred*,
not on the disease label of the source paper.** When the conserved molecular mechanism *is* the
candidate (PRC2 → MHC-I), a disease-distant source can still sit high on the ladder. The doc therefore
instructs scorers to identify *what is being transferred* before assigning a rung.

---

## 6. How to apply it (scorer instructions)

When assigning the **D (Directness)** sub-score for any entry:

1. **Name the mechanism being transferred** (the molecular object, per golden rule #3 — not an analogy,
   not "anti-cancer effect"). If you cannot name a conserved mechanistic bridge, the item is **floor /
   not admitted as evidence** → consider the Weak-Signal Register instead.
2. **Find the closest rung** at which that mechanism has *tumour-context* data: P0 (CIC-DUX4) → P1
   (fusion round-cell family) → P2 (sarcoma) → P3 (solid tumour + bridge) → P4 (pathway-only).
3. **Record the rung explicitly** alongside the D sub-score (e.g. `D = P2 (sarcoma; mGPS prognostic)`),
   so the transfer distance is auditable rather than hidden inside a single `+/0/−`.
4. **Combine with A/R/X unchanged** to get the confidence label (`docs/08` §3). Proximity sets D only.
5. **If the driver is unconfirmed (atypical ~5%)**, down-weight P0 by the cryptic-fusion posterior and
   treat P1 as the robust anchor (§4 / ADR-0008).
6. **Never let the rung prune the forward lane.** A low rung lowers confirmatory-lane confidence; the
   item can still be a top Forward Hypothesis.

This is additive: it replaces three D values with six labelled rungs and one "name the bridge" step.
Nothing else in the scoring changes.

---

## 7. Atypical-case note (fusion-unconfirmed ~5%)

The ladder is itself the framework's principled response to the atypical case: when fusion status is
unresolved, **P1 (the fusion round-cell family) is the robust evidence anchor** and P0 is discounted by
the driver posterior (§4). The ladder is fusion-agnostic in construction — it classifies *evidence by
biological proximity*, a classification that does not depend on the patient's junction being confirmed.

---

## 8. What I could not establish / limitations

- **The rungs are ordinal, not metric.** P0 > P1 > P2 > P3 > P4 is a defensible ordering of transfer
  distance; the *size* of each discount is a judgement, deliberately left as bands (per `docs/08` §3's
  argument against false-precision numbers). Inter-rater reliability is untested.
- **P3 admission depends on the scorer naming a real conserved mechanism.** The safeguard against P3
  becoming a back door for "it's cancer" hand-waving is the §6 step-1 requirement to name the molecular
  bridge — its discipline, like the Weak-Signal Register's, rests on enforcement (a `pre-output-check`
  failure mode is proposed in the ADR, deferred to maintainer sign-off, not applied here).
- **No new external citations were introduced.** Every PMID/example reused here is already cited and
  was previously checked in `host-biology-modifier-layer.md` / `docs/08` / the catalog. The WHO
  "undifferentiated small round cell sarcoma" family membership of CIC-rearranged sarcoma (P1
  definition) is established pathology (WHO 2020, 5th ed., soft-tissue & bone tumours).
- **This does not re-score `protocol-v1.md`.** Applying the ladder to regenerate a `protocol-v2.md` is
  deferred (same staging as `docs/08` §7) — this doc defines the method; a regeneration is separate.
- **It cannot manufacture data.** The ladder makes the *handling* of disease-distant evidence honest
  and graded; it does not create CIC-DUX4-specific evidence where none exists. The "what I could not
  establish" gaps in `host-biology-modifier-layer.md` §9 stand unchanged.

---

## 9. References (all internal / previously verified — no new accessions asserted)

- `docs/08-evidence-confidence-scoring.md` — the confidence axis whose D sub-axis this refines.
- `.claude/skills/sarcoma-contract` — the three scoring axes; axis-2 row now points here.
- `simulation-output/host-biology-modifier-layer.md` (ADR-0005) — the layer the comment was raised
  against; §5 weighting and §9 limitations.
- `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md` +
  `sims/08-driver-uncertainty/` (ADR-0008) — the latent-driver model behind §4.
- `docs/adr/0014-evidence-transferability-hierarchy.md` — the decision record for this doc.
- WHO Classification of Tumours, Soft Tissue and Bone Tumours, 5th ed. (2020) — places CIC-rearranged
  sarcoma in the *undifferentiated small round cell sarcomas* family with Ewing / BCOR / EWSR1-non-ETS
  (basis for the P1 rung). *(Established classification; cited, not a novel claim.)*

---

*Research-simulation note, not medical advice. This document defines how evidence is *weighted by
biological distance from CIC-DUX4*; it is not a recommendation to start, stop, or modify any therapy.*
