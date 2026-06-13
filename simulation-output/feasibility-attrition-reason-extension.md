# Feasibility-Layer Extension — Why a Program Closed (Attrition-Reason Annotation)

**In response to the GitHub issue #9 follow-up** (@Cerimagic, 2026-06-12): a feasibility band tells you
the **access path is closed**, but not **why** — and "discontinued" / "withdrawn" must not be read as
**biological invalidation**. This layer adds an *interpretive annotation* (not a new scoring axis — the
contributor explicitly asked for none) that records the **reason** an asset's access closed and whether
that reason carries any negative biological information.

**One-line summary:** extends [`translational-feasibility-layer.md`](translational-feasibility-layer.md)
(ADR-0003) with an **attrition-reason taxonomy (R0–R5)** for F3/F4 entries; applies it to the catalog's
discontinued/withdrawn agents; and answers the specific regorafenib question (it was **results-pending +
mechanism-not-driver-directed**, *not* deprioritized for negative efficacy). It deliberately does **not**
add a score, change any biology, or re-rank the catalog.

**Confidence:** medium-high for the regulatory/trial facts (each re-verified against a live source this
run and dated — see Provenance), medium for the reason *assignments* (attribution of a program's closure
to one cause is interpretive and sometimes multi-causal — said so per entry). The taxonomy is a
transparency aid, not a validated instrument.

**Not medical advice. Not a recommendation to seek, start, stop, or enrol in any therapy or trial.**
Bands and statuses are jurisdiction- and date-stamped (as of **2026-06-13**) and perishable.

---

## 1. The point, restated

The parent feasibility layer (ADR-0003) deliberately **separates access from evidence**: a low band
(F4 = discontinued/withdrawn/on-hold) never prunes a hypothesis, it only labels its access honestly.
The follow-up sharpens this: the **F-band alone is lossy** about *causation*. Two F4 agents can be F4
for opposite reasons —

- one because **its target was invalidated** (the biology was wrong → genuinely negative information), vs.
- one because **a company shifted resources** (commercial deprioritization → *zero* biological
  information; the mechanism is untouched).

A future reader who sees only "F4 — discontinued" cannot tell these apart, and the default human
inference ("it failed, so the idea is dead") is exactly the error to prevent — most acutely in **rare
tumors**, where a **cohort-level** negative can hide a **subgroup-level** positive (the contributor's
core concern). The fix is to record the *reason*, and to state which reasons carry biological weight.

This is **not** a fifth axis and not a new band. The three orthogonal axes are unchanged (evidence tier /
confidence / feasibility — `sarcoma-contract`). This is a **why-column annotation** on the feasibility
axis only.

---

## 2. The attrition-reason taxonomy (annotation, not a score)

For any entry banded **F3 (in development, no route here)** or **F4 (discontinued / withdrawn / on
hold)**, record one or more reason codes. Reasons are not mutually exclusive — most real closures are
multi-causal; list the dominant one first.

| Code | Reason the access path closed | Biological information it carries about *this target/mechanism* |
|---|---|---|
| **R0** | **Never developed** — concept-only / no clinical-stage agent ever existed (this is the F5 case, included for completeness) | **None.** Absence of a drug is not absence of a target. |
| **R1** | **Target / biology invalidated** — the mechanism itself was tested and disproven (e.g. target shown non-essential in the relevant context; on-target engagement without effect) | **High, negative.** This is the one reason that genuinely argues against the hypothesis. |
| **R2** | **Clinical-trial efficacy failure despite a plausible mechanism** — endpoint missed in the *tested population* | **Intermediate, population-dependent.** Negative *for that population/design*; says little if the population was unselected or the schedule/exposure was wrong. |
| **R3** | **Subgroup-dilution failure** — a biomarker-defined responder subset was folded into a broad cohort, so a real subgroup signal was averaged away to a cohort-negative | **Low/none against the subgroup.** Cohort-negative ≠ subgroup-negative. The contributor's central case. |
| **R4** | **Regulatory action** — clinical hold, safety signal, or label withdrawal | **Usually about safety/risk-benefit, not target validity.** A *combination*-driven or off-target safety signal leaves the *mechanism* intact. Distinguish an FDA **revocation** (regulator acted) from a **voluntary/commercial withdrawal** (sponsor acted). |
| **R5** | **Commercial / portfolio deprioritization** — resources reallocated, sponsor exited the area, asset out-licensed and stalled | **None.** Biology-silent. The most misleading-looking closures (a whole class can "contract" with no negative data). |

**Decoding rule (the whole point):**
> **The F-band tells you whether you can _get_ it. The reason code tells you whether the closure says
> anything about whether it _works_.** Only **R1** (and a well-powered, biomarker-*enriched* **R2**)
> carries negative biological information. **R3, R4-commercial, and R5 are biologically uninformative or
> nearly so** — an F4 for those reasons is an *access* fact, not an *efficacy verdict*, and the mechanism
> may still belong at the top of the **forward-hypotheses** lane (golden rule #5; two-lane rule).

---

## 3. Applied to the catalog's F3/F4 entries (as of 2026-06-13)

Evidence tier (axis 1) and the bands (axis 3) are unchanged from `translational-feasibility-layer.md`;
this adds only the **why**. Every status re-verified live this run (Provenance).

| Intervention (band) | Dominant reason | Read — does the closure argue against the *mechanism*? |
|---|---|---|
| **Tazemetostat — EZH2i** (F4 US / F3 EU) | **R5 + R4** | **No.** Ipsen's 2026-03-09 action was a **voluntary commercial withdrawal**, not an FDA revocation; the SYMPHONY-1 secondary-malignancy signal arose in a **combination**, not from EZH2 monotherapy biology. PRC2/EZH2→MHC-I de-repression is **intact**. *Mechanism survives; molecule swappable → valemetostat (EZH1/2) class.* (The catalog already flagged this in §5.1; the reason code makes the "no biological news" explicit and standing.) |
| **BET inhibitors as a class** (F3–F4) | **R5 (dominant) + R2 (one trial) ± on-target tox** | **Mostly no.** BMS dropping ezobresib and **AbbVie exiting** BET are **R5 (commercial/portfolio)** — biology-silent. The one efficacy datum (birabresib GBM trial terminated for lack of activity) is **R2 in glioblastoma, not in sarcoma** — i.e. R3-flavored (wrong tumor), not a CIC-DUX4 readout. BRD4 remains the catalog's "strongest mechanistic entry point"; the *access* contracted, the *mechanism* did not. ZEN-3694 survives. |
| **Molibresib / birabresib** (F4) | **R2 + R5** | **Partly.** Halted partly on narrow therapeutic window / modest single-agent activity (R2) and partly portfolio (R5) — neither tested in CIC-DUX4. |
| **Entinostat — class-I HDACi** (F3) | **R2** | **Population-specific.** The pivotal signal (E2112, +exemestane, breast `[VERIFY OS]`) is an HR+ breast readout, not a sarcoma/CIC one. HDAC-class and the differentiation/MHC rationale here are independent. |
| **Vorinostat — pan-HDACi** (F4/none EU) | **R4/R5 (EU)** | **No (for biology).** EU application **withdrawn** (regulatory/commercial) — not an efficacy refutation; US CTCL approval stands. |
| **IGF1R programs** (F3/F4, per `findings-ranking.md`) | **R2 + R5** | **Partly + diluted.** Most IGF1R programs in Ewing closed after **unselected** trials underperformed (R2) and sponsors exited (R5) — a textbook **R3 risk**: a biomarker-selected subset signal was diluted in all-comers. The dependency is real (Sim 1/2); the *programs* closed for design+commercial reasons. |
| **WEE1 — adavosertib** (F3, per register) | **R5** | **No.** Adavosertib development was **deprioritized/handed off** (commercial), while **azenosertib** continues `[re-verify]`. The WEE1+ifosfamide finding (Sims 2+3) is untouched. |
| **CIC-DUX4 junction ASO / PROTAC / vaccine / CAR-T** (F5) | **R0** | **None.** No agent ever existed — absence of a drug, not a failed one. Top forward-hypothesis material (fusion-confirmed cases). |

**Takeaway:** of the catalog's closed-access entries, **not one closed because its CIC-DUX4-relevant
mechanism was invalidated (R1).** They closed for commercial (R5), safety-in-combination (R4),
wrong-population/diluted (R2/R3), or never-built (R0) reasons. That is precisely why feasibility must not
be read as plausibility — and why the forward lane keeps them.

---

## 4. The rare-tumor subgroup caveat (R3) — the contributor's core point, with a worked example

In rare entities like CIC-rearranged sarcoma, dedicated trials are near-impossible (the
counterfactual-trial-forensics layer covers why), so these patients are usually **folded into broader
baskets** — Ewing-family, "other sarcomas," all-comers. That structurally invites **R3 (subgroup
dilution)**: a genuine responder signal in the CIC subset can be averaged into a cohort-level negative
and mis-recorded as "didn't work."

**Worked example (real, this run):** in **SARC024** (NCT02048371; Attia et al., *Cancer Medicine* 2023,
PMC9883574) — a phase II of regorafenib in advanced **Ewing-family** tumors — overall activity was modest
(median PFS 14.8 weeks; RR 10%). But the paper reports that **"one patient with [a partial response] had a
*CIC-DUX4* translocation"** (also carrying *NRAS* Q61K, *TP53* R282Q, and a *FUS-ERG* fusion). That is a
**subgroup-level partial response inside a cohort-level "modest" trial** — exactly the cohort-vs-subgroup
divergence the contributor flagged. The honest read: it is a **hypothesis-generating whisper, not
evidence of benefit** — n=1, a complex co-mutated genotype (so not cleanly attributable to the fusion),
and unreplicated. But it is the opposite of "deprioritized for negative data."

**Standing rule added:** when an asset is banded F3/F4 on the basis of a **basket/all-comers** trial,
tag **R3-risk** and, where the source reports it, **preserve any subgroup-level (especially
CIC/fusion-defined) signal** rather than collapsing to the cohort verdict.

---

## 5. The specific question — was the regorafenib CIC-rearranged cohort deprioritized?

> *"Regorafenib Phase II dedicated CIC-rearranged cohort is mentioned as a rare feasibility-positive
> signal. Was this deprioritized because of negative/neutral efficacy data, lack of available results, or
> simply because stronger hypotheses emerged later in the repo?"*

**Direct answer: not for negative efficacy data. It is (a) results-pending and (b) mechanistically not
driver-directed — so it scored as feasibility-positive but plausibility-modest, never as a discarded
lead.** Three components, all live-verified this run:

**(a) The dedicated cohort exists and has *not* read out.** The cohort is **Cohort E of REGOBONE**
(**NCT02389244**), a 5-arm non-comparative randomised placebo-controlled phase II run by the French
Sarcoma Group, whose arms are osteosarcoma, Ewing, chondrosarcoma, chordoma, **and metastatic
CIC-rearranged sarcoma** (ClinicalTrials.gov lists *CIC-Rearranged Sarcoma* among conditions). As of
**2026-06-13** the trial is **`ACTIVE_NOT_RECRUITING`** — primary completion **2024-10-25**, study
completion **2026-03-11**, last update posted **2025-09-16**, and **no results are posted on
ClinicalTrials.gov**. The other REGOBONE cohorts have published (osteosarcoma — Davis, *JCO* 2019;
chondrosarcoma — Duffaud, 2021; chordoma — *ESMO Open* 2023; Ewing — *Br J Cancer* 2023), but **the
CIC-rearranged Cohort E efficacy results are not yet published**. So this resolves the parent layer's
`[VERIFY current recruitment status]` flag to: **closed to enrolment, results pending** — the catalog
could not rank it on efficacy because **the efficacy data do not yet exist** (= *lack of available
results*, reason **R-pending**, not R1/R2).

**(b) The mechanism is host/stroma-directed, not CIC-DUX4-driver-directed.** Regorafenib is a
**multikinase / anti-angiogenic TKI** (VEGFR1–3, TIE2, PDGFR-β, FGFR, KIT, RET, RAF). It does **not**
engage the CIC-DUX4 fusion, its PEA3/ETS transcriptional output, or any of the catalog's prioritised
vector nodes. The simulation's hypotheses were selected by **driver mechanism** (V1 throttle the
RTK→ERK→ETV output; V3 epigenetic restoration / p300-CBP; cell-cycle CDK4; immune MHC-I/NK), so
regorafenib lands as a **feasibility-positive** (one of the very few registered trials that *names* this
entity) but **not** a high-plausibility driver hypothesis. This is the §5.3 pattern of the parent layer
("high feasibility + modest plausibility is a different object from low feasibility + high plausibility").

**(c) So "stronger hypotheses emerged" is true but is about _selection criterion_, not chronology.** The
catalog's stronger leads didn't "supersede" regorafenib over time; they were chosen on a *different axis*
(driver mechanism vs. anti-angiogenesis). Regorafenib was never down-ranked for a negative result — it
was correctly recorded as access-positive / mechanism-indirect / **results-pending**.

**Net:** the right annotation for the regorafenib CIC entry is **not** R1/R2 (no negative efficacy data
exist) — it is **results-pending** on access, **R3-risk-aware** on interpretation (any eventual
cohort-negative should be read against the SARC024 subgroup PR, not instead of it), and
**plausibility-modest** because the mechanism is off-driver. Evidence tier for regorafenib in
CIC-rearranged: **`Clinical-Trial`** (registered, NCT02389244 Cohort E; results pending). The lone
efficacy signal anywhere is the SARC024 n=1 CIC-DUX4 partial response (§4) — `Clinical-Trial`,
anecdotal.

---

## 6. Forward hypotheses (idea-generation lane — exempt from feasibility/attrition pruning)

1. **[Forward Hypothesis] Add a standing "reason-decode" gate before any closed asset is dropped from
   consideration.** *Statement:* no F3/F4 entry is removed from the forward lane until its attrition
   reason is classified; only **R1** (target invalidated) and a **biomarker-enriched R2** justify
   demotion of the *mechanism*. *Basis:* §3 shows every catalog closure is R5/R4/R2-wrong-population/R0 —
   none R1. *Test/falsifier:* audit the catalog's discontinued agents; if any is found to be R1 in a
   CIC-relevant context, demote that mechanism and record it. *(Pure annotation discipline — no biology
   claim.)*

2. **[Forward Hypothesis] Treat the SARC024 CIC-DUX4 partial responder as a kinase-dependency probe, not
   noise.** *Statement:* the n=1 PR (on regorafenib, in a tumor co-carrying *NRAS* Q61K) may reflect a
   **RAS/MAPK- or angiogenesis-dependent subset** of CIC-rearranged sarcoma rather than a fusion-driven
   effect. *Basis:* CIC-DUX4 up-regulates PEA3/ETS-RTK programs (catalog V1), and the responder's *NRAS*
   Q61K supplies parallel MAPK drive — a regorafenib-tractable axis. *Test/falsifier:* in CIC-DUX4
   models ± engineered *NRAS*/RTK activation, measure regorafenib sensitivity; if sensitivity tracks
   MAPK/angiogenic drive rather than the fusion, anti-angiogenic TKIs become a **biomarker-selected**
   (not all-comers) option — and the historical all-comers framing was an R3 dilution. *(Reframes a
   discarded-looking signal into a falsifiable, biomarker-defined hypothesis; tag `Theoretical`.)*

3. **[Forward Hypothesis] Mine *failed/closed* assets for preserved subgroup signals before the catalog
   calls anything dead.** *Statement:* for each R2/R3 closure (IGF1R in Ewing, BET in non-sarcoma,
   HDACi in breast), retrieve any reported fusion/CIC subgroup outcome from the primary publication.
   *Basis:* §4's cohort-vs-subgroup divergence is structural in rare-tumor baskets. *Test:* a literature
   pass on the closed programs' subgroup tables; surface any CIC/fusion-stratum signal into the
   forward lane. *(Operationalises the contributor's "informative responder signals" point.)*

---

## 7. What I could not establish (honest limits)

- **REGOBONE Cohort E efficacy is genuinely unknown.** No published results, no posted ClinicalTrials.gov
  results section, no conference abstract located this run. I can state the cohort exists and the trial
  is closed to enrolment; I **cannot** state whether regorafenib helped, hurt, or did nothing in the CIC
  subset. Flagged **results-pending**, not asserted either way.
- **Cohort E patient count is secondary-sourced.** One search summary gave "27 evaluable (18 regorafenib,
  9 placebo)"; I did not confirm this against a primary REGOBONE Cohort-E publication (none found).
  Treat the n as **`[VERIFY]`**.
- **The SARC024 PR is n=1 and confounded.** The responder also carried *NRAS* Q61K, *TP53* R282Q, and a
  *FUS-ERG* fusion — benefit is **not** cleanly attributable to CIC-DUX4. Hypothesis-generating only.
- **Reason-code assignment is interpretive.** Real closures are multi-causal; I listed the dominant cause
  and noted co-causes, but a sponsor's internal rationale (esp. R5 vs R2 weighting) is rarely fully
  public. The codes are a reading aid, not adjudicated fact.
- **Entinostat E2112 OS outcome and vorinostat EU specifics remain `[VERIFY]`** (carried from the parent
  layer; not re-resolved this run).
- **Perishable.** All statuses are as of **2026-06-13** and US/registry-centric; re-verify before any use.

---

## 8. What this extension does NOT do

- **No new scoring axis** — the contributor explicitly asked for none. It is a why-annotation on the
  existing feasibility axis. The three axes (tier / confidence / feasibility) are unchanged.
- **No re-ranking of the catalog and no new biology.** It re-reads existing closures; it does not move
  any hypothesis up or down on plausibility.
- **No pruning of the forward lane** — per golden rule #5 / the two-lane rule, R0/R3/R4-commercial/R5
  closures stay available as forward hypotheses.
- **Not a diagnosis or treatment recommendation.** It is about how to *read* program closures, not what
  any patient should do.
- **Atypical-case flag unchanged** — F5 junction-specific rows (R0) remain POSSIBLY INAPPLICABLE for the
  fusion-unconfirmed patient; the fusion-agnostic mechanisms remain in scope.

**Evidence tier of this layer:** the regulatory/trial *facts* are `Established`/`Clinical-Trial` (each
cited, re-verified 2026-06-13); the *taxonomy itself* is a transparency tool (methodology), not evidence
about the patient.

---

## Provenance — sources verified this run (2026-06-13)

- **REGOBONE / NCT02389244 status:** ClinicalTrials.gov API v2 — `OverallStatus = ACTIVE_NOT_RECRUITING`;
  start 2014-09; **primary completion 2024-10-25**; completion 2026-03-11; last update posted 2025-09-16;
  conditions include **CIC-Rearranged Sarcoma**; **no results section posted** (accessed 2026-06-13).
- **REGOBONE design / cohorts:** 5-arm non-comparative randomised placebo-controlled phase II, French
  Sarcoma Group (Cohort E = metastatic CIC-rearranged sarcoma). Published sibling cohorts: osteosarcoma
  (Davis et al., *J Clin Oncol* 2019), chondrosarcoma (Duffaud et al., 2021), chordoma (*ESMO Open*
  2023), Ewing (*Br J Cancer* 2023, s41416-023-02413-9). Cohort-E CIC results **not located / unpublished**
  as of 2026-06-13. Cohort-E n **`[VERIFY]`** (secondary-source figure only).
- **SARC024 CIC-DUX4 partial response:** Attia et al., *Cancer Medicine* 2023, **NCT02048371**,
  PMC9883574 — *"One patient with [a partial response] had a CIC-DUX4 translocation"* (also NRAS Q61K,
  TP53 R282Q, FUS-ERG); trial overall median PFS 14.8 weeks, RR 10% (accessed 2026-06-13).
- **Tazemetostat US withdrawal (R5+R4):** Ipsen voluntary market withdrawal of all US indications
  2026-03-09 (commercial, not FDA revocation); SYMPHONY-1 combination secondary-malignancy signal — as
  recorded and sourced in `translational-feasibility-layer.md` §5.1 / Provenance (carried, not re-fetched
  this run).
- **BET contraction, IGF1R, WEE1, entinostat, vorinostat statuses:** carried from
  `translational-feasibility-layer.md` and `findings-ranking.md`; efficacy/regulatory specifics flagged
  `[VERIFY]` where the parent layer flagged them.

*Decision record:* adopted via [ADR-0013](../docs/adr/0013-feasibility-attrition-reason-annotation.md)
(issue #9 follow-up / PR). Parent layer: [ADR-0003](../docs/adr/0003-translational-feasibility-layer.md).

*No new biology, no fabricated citations, not medical advice. Statuses are date-stamped (2026-06-13) and
perishable — re-verify before any external use.*
