# The Surveillance-Window Host/Mitochondrial Lane — Autophagy, Food and Natural Agents While NED and Off Treatment

> **Origin:** user question, 2026-09-17 (follow-up to ADR-0023) — *"As much as you're focusing on
> medication, I want you to be creative with autophagy, food and natural remedies for how mitochondria
> work. Especially since this patient is in a control group now, monitoring NED and no medication. So
> apply any hypothetical or theoretical idea that may help keep the patient in NED."*
>
> **Status:** extension of the **mitochondrial / endosymbiotic layer** (ADR-0023) into the **host-directed
> (M8) modality** under the **host-biology modifier layer** (ADR-0005), scoped to a **new context the
> framework had never modelled: the no-treatment surveillance window.** **Not a fifth vector** (golden
> rule #8). Recorded as **ADR-0024**.
>
> **Research simulation and hypothesis generation only. NOT medical advice, NOT a diagnosis, NOT a
> treatment, testing, dietary or supplement recommendation. No dosing and no start/stop instructions for
> anything — including food and supplements.** Published human-trial ranges appear below **only** where
> they are part of citing what a study did, never as a suggestion for this or any person. Anything in here
> that anyone might act on belongs to the treating oncology team, not to this document — and "natural"
> carries no safety presumption (§6 is entirely about natural agents that the framework's own model says
> may be **wrong-signed**).
>
> **⚠ Verification status (ADR-0020).** Literature egress remains **blocked** (PubMed/PMC/nature.com/
> EuropePMC/NCBI E-utilities **and clinicaltrials.gov** all refused CONNECT, HTTP 403, re-tested
> 2026-09-17; WebFetch returns `EGRESS_BLOCKED`). Everything below is **search-snippet/abstract level**,
> carries **`[VERIFY]`**, and identifiers are reported **as they appeared in search results — not as
> records I opened.** Forward-lane only; nothing here may enter a `protocol-vN.md` until full-text-verified.

---

## 0. What this covers, what it excludes, and how much to believe it

**Covers:** mechanisms by which **autophagy/mitophagy, food, dietary pattern and natural agents** intersect
mitochondrial biology in the **no-treatment NED surveillance window**, scored on the framework's three axes,
plus forward hypotheses with falsifiers and a **wrong-signed register** of popular natural agents the
reservoir model predicts are pointed the wrong way.

**Deliberately excludes:** any protocol, dose, amount, schedule, brand, or start/stop instruction; any
claim that diet or supplements substitute for surveillance or treatment; pharmacological reservoir-directed
agents (those are ADR-0023 §5); and any assertion that a listed agent has caused or will cause relapse.

> **Confidence: LOW for every intervention claim, MEDIUM for the negatives and the context model.**
> Why: **no sarcoma recurrence-outcome evidence exists for anything here** — the strongest item is a colon-cancer
> phase-3 trial (**P3** transfer), the food mechanism is organoid-level (**P3/P4**), the autophagy literature
> is **self-contradictory**, and the ferroptosis-reservoir premise it all rests on is itself `Low`-confidence
> **P4** with no sarcoma model. The **wrong-signed register (§6)** and the **window-constraint model (§2)** are
> the more defensible parts, because they rest on published harm signals and on the framework's own rules
> rather than on transfer.

**Evidence in CIC-DUX4 (or any round-cell sarcoma) specifically: `None direct` for every single entry in
this document.** Where a mechanism is **fusion-agnostic** — exercise/NK mobilisation, omega-3 membrane
lipids, the antioxidant/ferroptosis register, host-immune conditioning — it applies regardless of driver and
therefore **still applies to the ~5% fusion-unconfirmed case** (golden rule #9); **nothing** in this lane is
fusion-contingent, which is one of the few genuine advantages of the host-directed route.

---

## 1. One-paragraph answer

Three honest headlines, and the first one is the one nobody wants. **(1) The autophagy literature does not
support the popular story, and it is genuinely split on the sign.** One body of work says autophagy
*sustains* dormant tumour cells and that **inhibiting** it kills them by letting damaged mitochondria and
ROS accumulate; another says inhibiting it **awakens** dormancy. Both are real, both are preclinical, and
they point in opposite directions — which means fasting, spermidine and especially **urolithin A (a
mitophagy inducer) are directionally ambiguous for the reservoir**, and the most mitochondria-specific
natural supplement on the market is the one most plausibly *protecting* the cells you care about, because
its mechanism is precisely the cleanup of the damaged mitochondria that would otherwise kill a dormant
cell. **(2) Exactly one intervention in this entire space has phase-3 randomised *recurrence* evidence in
the post-chemotherapy surveillance setting — structured exercise** (CHALLENGE, NEJM 2025: DFS HR 0.72), and
its mechanism in mice is **NK-cell-dependent and adrenaline/IL-6-driven**, which lands directly on this
framework's standing NK-first thesis. It is also mitochondrial at its core (PGC-1α biogenesis). It is colon
cancer, not sarcoma. **(3) Food gets a *specific* target for the first time in this repo, and it is
ferroptosis.** Omega-3 **DHA induces ferroptosis in patient-derived organoids and, by title, in
drug-tolerant cells**, while sparing normal-tissue organoids — which answers the commons objection ADR-0023
raised — and PUFA peroxidation is *potentiated by the acidic tumour microenvironment* the tumour itself
creates. The mirror image of that is §6, the **wrong-signed register**: because GPX4 is a **selenoprotein**
and vitamin E is the most mechanistically direct dietary ferroptosis *inhibitor* known, high-dose
selenium and vitamin E plausibly **strengthen** the reservoir's main defence — and those are the two agents
SELECT tested, with harm signals. **Ketogenic diet is on that list too**, because the β-hydroxybutyrate
paradox says oxidative cells *consume* ketones and the reservoir is OXPHOS-high. Net: the defensible moves
in this window are justified on **immune-surveillance** and **membrane-lipid** grounds, not on
"autophagy/keto starves cancer" grounds — and the most valuable output here may be the list of popular
things to *not* do.

---

## 2. What actually changes in a no-treatment window (the framework had never modelled this)

This is a genuinely different regime from every prior artifact in the repo, and three of the changes matter.

| Feature of the window | Consequence |
|---|---|
| **No concurrent cytotoxic therapy** | The framework's **dominant** safety gate — the VDC/IE chemo-interaction screen (golden rule #7, `sarcoma-chemo-interactions`) — **largely lifts.** CYP3A4/P-gp competition with ifosfamide, and the antioxidant-vs-ROS-chemo conflict, are *not live* while nothing is being given. This is the one window in which dietary questions are structurally least hazardous. **It re-arms the moment any treatment resumes** — and the repo's standing flags (piperine/thymoquinone × CYP3A4-activated ifosfamide) become live again immediately. |
| **No drug to combine with** | Every hypothesis here must stand **alone**. Most of the promising literature in this space is *combination* data (FMD + chemotherapy, ketogenic + anti-PD-L1, DHA + drug). Monotherapy host-intervention evidence is much thinner than the combination literature makes it look — and golden rule #5's "was it monotherapy?" question now cuts **against** the things being proposed here. |
| **Long duration, surveillance cadence** | Chronic-exposure interventions become feasible where pulsed ones were not — but so does **chronic** exposure to anything wrong-signed. A supplement taken daily for two years in a wrong direction is a materially different risk from one taken for a week. This is why §6 exists and why it is longer than §5. |
| **The target compartment is the reservoir, by definition** | NED with possible dormant/sub-radiographic disease *is* the persister/dormancy compartment (`CASE-BASELINE.md` §4, ADR-0021). So everything here is aimed at the compartment the framework says causes relapse — which is the right aim, and also the compartment with the **least** evidence and the **most** contested biology. |

**One thing that does not change:** there is **no sarcoma recurrence-outcome evidence** for any
intervention in this document. Not one. The strongest item (§4) is colon cancer.

---

## 3. The autophagy problem — the literature is split, and the popular story is the weaker side

The user asked to be creative with autophagy. The honest creative move is to report that **the field
contradicts itself on the direction**, because that contradiction is the single most decision-relevant
fact in this whole document.

### 3.1 Camp A — autophagy *sustains* dormant cells, so inhibiting it kills them

- Autophagy is **required for the survival of disseminated dormant breast cancer cells**; pharmacologic or
  genetic inhibition **decreased dormant-cell survival and metastatic burden** across 3D in vitro and in
  vivo dormancy models. **ATG7** is essential. *Nature Communications* 2018, PMC5964069 `[Preclinical-Animal, VERIFY]`
- **The mechanism is mitochondrial, and it is the crux of this section:** blocking autophagic flux in
  dormant cells causes **accumulation of damaged mitochondria and ROS → apoptosis.** `[Preclinical-Animal, VERIFY]`
- Autophagy is **required for mammary tumour recurrence** by promoting dormant tumour-cell survival after
  therapy. *Breast Cancer Research* 2024, DOI 10.1186/s13058-024-01878-7 `[Preclinical-Animal, VERIFY]`
- This has reached humans as a **recurrence-prevention** concept: the **CLEVER pilot trial
  (NCT03032406)** — hydroxychloroquine, everolimus, or the combination, *for prevention of recurrent
  breast cancer*. `[Clinical-Trial (pilot/phase-2), VERIFY — status NOT verifiable this session; registry unreachable]`

### 3.2 Camp B — autophagy inhibition *awakens* dormancy

- Autophagy inhibition **elicited emergence from metastatic dormancy** by inducing and stabilising
  **Pfkfb3**; depleting autophagy genes **reactivated** dormant breast cancer stem cells and drove
  outgrowth. PMC6694140 `[Preclinical-Animal, VERIFY]`

### 3.3 What follows — and the sharp corollary about the most popular mitochondrial supplement

Both camps are preclinical, both are in breast models, and they disagree. So:

> **No confident direction exists for autophagy modulation in a dormant reservoir.** An intervention
> justified as "it induces autophagy, which fights cancer" is resting on the *contested* side of a split
> literature — and the better-developed side (Camp A, which has a human prevention trial) says the
> opposite.

**The corollary is specific and worth stating plainly.** Camp A's kill mechanism is *"damaged mitochondria
and ROS accumulate until the dormant cell dies."* **Urolithin A** — the pomegranate/walnut ellagitannin
metabolite, the most mitochondria-specific natural product with human data, marketed precisely as a
mitophagy activator — does the **exact opposite** of that: it *clears* damaged mitochondria efficiently.

> **[Forward Hypothesis FH-11.4] Mitophagy induction is plausibly wrong-signed for a dormant reservoir.**
> If dormant-cell death under autophagy blockade proceeds via damaged-mitochondria/ROS accumulation
> (Camp A), then a selective **mitophagy inducer** should *relieve* that pressure and **support** dormant-cell
> persistence. *Basis:* PMC5964069 mechanism + urolithin A's characterised mitophagy induction
> `[Mechanistic, VERIFY]`. *Falsifier:* urolithin A in a dormancy model showing reduced, not increased,
> dormant-cell survival. *Status:* `Theoretical`; **no urolithin A dormancy or sarcoma data exist**, and I
> found none in either direction.

What urolithin A actually has: human RCTs showing **safety** and mitophagy-marker/muscle-endurance effects
in older adults `[Clinical-Trial for those endpoints, VERIFY]`; **not FDA-approved for any indication**;
and a notable dependency — it is a **gut-microbial** metabolite, and a majority of adults (estimates ~60%,
or "a third or fewer convert efficiently") **cannot reliably produce it from food at all** `[VERIFY]`. That
microbiome dependency is itself a host-biology variable (ADR-0005) and is why food-based ellagitannin
intake and supplemental urolithin A are not interchangeable. **None of its human endpoints is a cancer
endpoint.**

**Fasting / time-restricted eating / FMD sit in the same ambiguity — with one asymmetry that rescues them
partially.** Their autophagy rationale is subject to everything above. But their *immune* effects run on a
separate, more consistent track: cyclic fasting **remodels tissue niches to reprogram NK metabolic and
functional state**, priming splenic and marrow NK cells to secrete more IFN-γ (PMC11684419), and FMD
alongside standard therapy increased antitumour immunity partly via NK expansion in a ~101-participant
study `[Preclinical-Animal + small Clinical, VERIFY]`. They are also **cyclic**, so any "feeding the
reservoir" concern is time-limited rather than chronic.

> **So the defensible justification for fasting-type interventions here is immunological, not autophagic** —
> and that reframe changes what you would measure (NK number/function, not autophagy markers).

Spermidine (wheat germ, natto, mature cheese, soy, and microbiota-produced) is the same case: it
**stimulates anticancer immunosurveillance in animal models** and its documented cancer effects are
**T-cell-mediated and in *combination* with chemotherapy** `[Preclinical-Animal, VERIFY]` — i.e. the
combination caveat from §2 applies squarely, and a surveillance window has no chemotherapy to boost.
Human trials exist only for cognitive/safety endpoints (a 3-month phase-2 RCT, n=30, in subjective
cognitive decline) `[Clinical-Trial for that endpoint only, VERIFY]`.

---

## 4. The one thing with phase-3 recurrence evidence: structured exercise (and it is mitochondrial)

This is the strongest item in the document by a wide margin, and it deserves to be stated before any
supplement.

**CHALLENGE (CCTG CO.21)** — phase 3, 55 centres, **n=889** with resected stage-III/high-risk-stage-II
colon cancer who had **completed adjuvant chemotherapy**, randomised to a **3-year structured exercise
programme** vs health-education materials:

| Endpoint | Exercise | Control |
|---|---|---|
| **Disease-free survival** | **HR 0.72** (recurrence, new primary, or death) | — |
| 5-year DFS | **80.3%** | 73.9% (+6.4 points) |
| 8-year overall survival | **90%** | 83% |
| Median follow-up | 7.9 years | |
| Musculoskeletal adverse events | 18.5% | 11.5% (~10% of exercise-arm events attributed to the intervention) |

*NEJM* 2025 (published 1 June 2025), **DOI 10.1056/NEJMoa2502760**, **PMID 40450658**; presented ASCO 2025
as LBA3510. `[Clinical-Trial — phase 3, VERIFY]`
**Confidence note:** unusually for this session, the numbers above were **concordant across several
independent sources** (NEJM, the ASCO press release, ASCO Post, the JCO abstract record, PubMed). That
raises my confidence materially — but it is **still snippet-level and still `[VERIFY]`**; I could not open
the paper.

**Why it belongs in a mitochondrial layer, and why it fits *this* case:**

1. **The mechanism is mitochondrial at the host level.** Endurance exercise is the best-characterised
   physiological inducer of **mitochondrial biogenesis (PGC-1α)** in existence. `[Established — exercise physiology]`
2. **The antitumour mechanism, where it has been dissected, is NK-dependent.** Voluntary wheel running
   reduced tumour incidence and growth by **>60% across five tumour models**; NK infiltration rose;
   **depleting NK cells abolished the benefit**; mobilisation required **epinephrine**, and IL-6 blockade
   blunted tumour suppression, intratumoral NK infiltration and NK activation. Pedersen et al.,
   *Cell Metabolism* 2016, **PMID 26895752** `[Preclinical-Animal, VERIFY]`
3. **That is the framework's own thesis.** The repo's standing immune position is **NK-first** (Sims 4+5;
   reinforced by ADR-0021's MRD-window argument; given a mitochondrial failure mode by ADR-0023 §4B). An
   NK-dependent, **fusion-agnostic** (golden rule #9), zero-access-barrier intervention with phase-3
   recurrence data in *some* tumour is the closest thing this catalog has to a coherent
   surveillance-window lever.

**Framework update this forces (ADR-0020 refresh action).** The host-biology layer's exercise row
(ADR-0005 §4) currently reads tier **"Clinical-Trial (tolerability/fatigue/QoL); Mechanistic for
outcome"** with the note *"outcome benefit best evidenced in breast/colon, not sarcoma."* CHALLENGE
**upgrades the outcome claim from Mechanistic to Clinical-Trial (phase 3, DFS *and* OS)** in colon. The
"not sarcoma" caveat stands unchanged.

**Honest limits — and they are real:**
- **Transferability P3** (solid tumour, named mechanism). Colon ≠ round-cell sarcoma; different biology,
  different recurrence kinetics, and CHALLENGE's population was post-adjuvant-chemo colon cancer.
- **Sarcoma has no recurrence-outcome exercise data at all.** What exists in osteosarcoma/Ewing is
  **function, gait, disability and QoL** — and one review states explicitly that *the effect of increasing
  activity on sarcoma growth/progression remains unknown* `[VERIFY]`.
- **This patient's anatomy is directly relevant and cuts both ways.** Prior **leg radiotherapy** and
  lower-extremity involvement put them squarely in the population the sarcoma literature describes as
  having impaired gait, reduced walking velocity and lower-extremity weakness after limb-sparing surgery
  or RT. Any exercise question here is a **rehabilitation-medicine** question about a specific irradiated
  limb — which is exactly the kind of thing that belongs to the treating team and a physiotherapist, not
  to a document like this one. The musculoskeletal-AE rate in CHALLENGE (18.5% vs 11.5%) is not nothing.

**An internal conflict in the repo, now surfaced.** ADR-0005's autonomic row says sympathetic/β2-adrenergic
signalling is **pro-metastatic and immunosuppressive** (strong mouse mechanism; perioperative propranolol
blunts it). Pedersen says the **epinephrine surge is required** for exercise's NK mobilisation, and
β-blockade **blunted** the benefit. These are not actually contradictory — the likely reconciliation is
**tonic vs pulsatile** adrenergic signalling (chronic stress tone vs an acute exercise pulse) — but the
framework had never stated it, and it generates a concrete flag:

> **Flag:** chronic β-blockade would be predicted to **blunt** the NK-mobilisation arm of exercise's
> antitumour effect. `[Mechanistic — extrapolated from PMID 26895752; no human outcome data]` Purely a
> mechanistic observation for the record; medication decisions are the treating team's.

---

## 5. Food with a *specific* target for once: omega-3 and the reservoir's ferroptosis vulnerability

The repo's dietary track has always suffered from golden rule #6 — most food mechanisms operate 10–500×
above achievable plasma (protocol #6: the broccoli-juicing/myrosinase point). **Omega-3 is the exception,
because the mechanism is membrane *incorporation*, not enzyme inhibition at a concentration you cannot
reach** — and it now has a named target in this patient's hypothesised reservoir.

`findings-ranking.md` §D already carries **"omega-3 EPA/DHA is the best cross-vector dietary compound — and
it's absent from the regimen"** (`Dietary-Observational + Mechanistic`, **F1**, lowest chemo-interaction
risk, addresses post-WLI lung inflammation). ADR-0023 then established that the reservoir's vulnerability
is **lipid-redox** (GPX4/ferroptosis unified with the OXPHOS-high/FAO phenotype). Those two rows connect:

- **DHA induces ferroptosis in colorectal cancer patient-derived organoids *and drug-tolerant cells*** —
  lipid-peroxide accumulation, partially rescued by ferroptosis inhibitors; organoids were sensitive
  **irrespective of KRAS or TP53 status**; and, critically, **organoids from normal colon tissue were less
  affected.** *Cell Death & Disease*, DOI 10.1038/s41419-026-08744-8, **PMID 41963291** / PMC13180983
  `[Preclinical-Cell (PDO), VERIFY]`
- **The mechanism is the membrane.** Omega-3 PUFAs are highly peroxidation-susceptible; **diacyl-PUFA
  phosphatidylcholine content is a marker of ferroptosis sensitivity** and drives it via mitochondrial ROS
  and lipid peroxidation. Enhanced DHA uptake from the medium largely accounted for the rise in
  malondialdehyde. `[Preclinical-Cell, VERIFY]`
- **The tumour's own microenvironment potentiates it.** Peroxidation of n-3 and n-6 PUFAs **in the acidic
  tumour environment** leads to ferroptosis-mediated anticancer effects. *Cell Metabolism* 2021,
  "Peroxidation of n-3 and n-6 polyunsaturated fatty acids in the acidic tumor environment leads to
  ferroptosis-mediated anticancer effects" `[no DOI or PMID captured — journal/year/title only, from
  search results]` `[Preclinical-Cell/Animal, VERIFY]`

> **Two things make this the most interesting food item in the repo.** First, it **answers the commons
> objection** ADR-0023 raised as a standing constraint: normal-tissue organoids were *less* affected, so
> there is at least a hint of a therapeutic window rather than an attack on shared infrastructure.
> Second, it **closes a loop with ADR-0023 §4B** — the acidosis the tumour creates as an immune weapon is
> the same acidosis that potentiates PUFA peroxidation. The tumour's own microenvironment is the trigger.

> **[Forward Hypothesis FH-11.1] Dietary omega-3 membrane enrichment as a ferroptosis-sensitising prime
> for the dormant reservoir.** *Hypothesis:* sustained dietary EPA/DHA raises diacyl-PUFA
> phosphatidylcholine content in residual cells, lowering the GPX4 threshold at which they tip into
> ferroptosis — plausibly the only reservoir-directed lever in this document that is both food-based and
> mechanistically specific. *Basis:* PMID 41963291 (incl. drug-tolerant cells) + the PUFA-PC
> sensitivity-marker mechanism + acidic-TME potentiation. *Why untested:* no ferroptosis or lipidomic data
> exist in CIC-DUX4 or any round-cell sarcoma; no dormancy model has been tested with dietary PUFA.
> *Falsifiers:* (a) reservoir lipidomics showing PUFA-PC content is not rate-limiting; (b) a
> round-cell-sarcoma model where DHA enrichment fails to lower the GPX4-inhibition threshold; (c) the
> reservoir turns out to be a pre-existing clone rather than a persister state, in which case the whole
> premise fails (the inherited ADR-0021/0023 uncertainty). *Tier:* `Preclinical-Cell` for the mechanism →
> `Theoretical` for this tumour. **P3/P4.**

**Honest limits:** organoid/cell-level only; achievable human membrane enrichment is real but the
*magnitude* needed for a ferroptosis effect in vivo is unestablished; and there is a legitimate opposing
consideration — the repo's own §D row flags that **high-dose antioxidant and pro-/anti-oxidant
manipulations near residual disease are genuinely unresolved** (the NAC-metastasis literature), and
lipid-peroxidation biology is exactly where that tension lives. Also, fish-oil at high intake has real
antiplatelet/bleeding considerations that are a clinical matter, not a mechanism footnote.

---

## 6. The wrong-signed register — natural agents the framework's own model says may *help* the reservoir

The contract's hard rule is **"no 'natural = safe' framing,"** naming β-carotene in smokers, vitamin E in
SELECT, and selenium's narrow window. ADR-0023's reservoir model now supplies a **precise mechanism** for
why those particular counter-examples are the ones that bite — and it makes this the most useful section
of the document for a patient in a long surveillance window, because these are all things that are easy to
start and easy to take daily for years.

**The logic is one sentence:** if the residual reservoir survives by paying a continuous antioxidant tax to
defend its membranes against lipid peroxidation (ADR-0023 §5.1), then **anything that helps pay that tax is
working for the reservoir.**

### 6.1 Selenium — because GPX4 *is* a selenoprotein

- **GPX4 is a selenoenzyme**, and **selenium utilisation by GPX4 is required to prevent
  hydroperoxide-induced ferroptosis**; GPX4 synthesis **depends on selenium availability** (plus a
  functional mevalonate pathway for selenocysteine-tRNA). **PMID 29290465** `[Preclinical-Cell, VERIFY]`
- Selenocysteine (vs a cysteine variant) is what confers GPX4's **resistance to irreversible
  overoxidation** — cells with the cysteine variant are **highly sensitive** to peroxide-induced
  ferroptosis. `[Preclinical-Cell, VERIFY]`
- **Selenoprotein P** transports selenium and preserves GPX4 via cycling-selenium storage, driving
  **ferroptosis resistance** (shown in glioblastoma). *Sci Rep* 2024, PMC10770386 `[Preclinical-Cell, VERIFY]`

> **Read:** selenium **sufficiency** is required for normal physiology and is not in question.
> **Supra-sufficiency selenium** is mechanistically predicted to **increase GPX4 capacity** — i.e. to
> reinforce the exact defence the reservoir depends on. `[Mechanistic, VERIFY]` This is not a claim that
> selenium causes relapse; it is a claim that the *direction* of a popular supplement is opposite to the
> direction the reservoir model wants, and that "more" has no supporting rationale here.

### 6.2 Vitamin E — the most mechanistically direct dietary ferroptosis *inhibitor* known

- α-Tocopherol is a lipophilic antioxidant that **inhibits ferroptosis** in cancer cells in vitro and in
  neurons and haematopoietic stem cells in vivo; tocopherols scavenge lipid hydroperoxyl and alkoxyl
  radicals. `[Preclinical-Cell/Animal, VERIFY]`
- The mechanism is sharper than generic scavenging: the metabolite **α-tocopherol hydroquinone** is a
  *dramatically more potent* ferroptosis inhibitor than the parent, and **inhibits 15-lipoxygenase by
  reducing its non-heme iron from active Fe³⁺ to inactive Fe²⁺**. *PLOS One* 2018, **PMID 30110365** /
  PMC6093661 `[Preclinical-Cell, VERIFY]`
- Tocotrienols reportedly **exceed** tocopherols at ferroptosis inhibition `[Preclinical-Cell, VERIFY]`
  — relevant because tocotrienol supplements are marketed as the "superior" vitamin E.

> **The convergence is striking and worth naming explicitly.** **SELECT tested selenium + vitamin E** —
> which, on the biology above, is *the two most direct dietary reinforcements of the reservoir's
> anti-ferroptotic defence* — and it produced harm signals rather than benefit. The framework already
> carried SELECT as a cautionary datum; ADR-0023 now gives it a **candidate mechanism** rather than leaving
> it an unexplained empirical warning. `[Mechanistic hypothesis about a Clinical-Trial finding — explicitly
> post-hoc, and SELECT's endpoint was prostate cancer *incidence*, not sarcoma recurrence.]`

### 6.3 High-dose antioxidants / NAC — the repo's existing flag, now with a mechanism

**The convergence here is the strongest argument in this section, and it is not mine — it is the repo's own
oldest safety flag.** `protocol-v1.md` §Conflicts carries **Sayin et al., *Sci Transl Med* 2014
(PMID 24477002)**: **NAC *and vitamin E* accelerated metastasis** in KRAS/BRAF mouse lung models via ROS
suppression → reduced apoptosis and reduced oxidative clearance of circulating tumour cells. protocol-v1
already called it *"the most metastasis-relevant safety item across the whole catalog... by construction
about disseminating disease — exactly this patient's setting."*

> **Note what just happened.** The ferroptosis/GPX4 argument in §6.1–6.2 was derived independently, from
> reservoir biology, and it predicts **exactly the two agents Sayin tested** — vitamin E (the direct
> lipid-peroxyl scavenger) and NAC (the thiol/GSH supply feeding the GPX4 reaction). An *a priori*
> mechanistic argument and a decade-old *in vivo* metastasis signal land on the same two compounds. That is
> the closest thing to corroboration anything in this document has.
>
> **The honest counter, also already in the repo:** CIC-rearranged sarcoma is **not** KRAS/BRAF-driven — a
> different ROS architecture — so the transfer is *biologically plausible but unconfirmed*
> (`Preclinical-Animal`). And the contract's other named counter-examples belong here for completeness:
> **β-carotene harmed smokers (ATBC, CARET)**, **vitamin E in SELECT**, and **selenium's narrow window**.

`findings-ranking.md` §D already carries *"antioxidant-vs-ROS-chemo & antioxidant-vs-metastasis conflicts
are genuine and unresolved"* (`Preclinical-Animal`, caution item), including the NAC-metastasis literature.
The ferroptosis frame sharpens **why**: general glutathione/thiol-axis support feeds the GPX4 reaction
(which consumes GSH), and lipophilic radical scavengers act directly on the lipid-peroxidation cascade.
**The chemo-interaction half of that conflict is dormant in this window (§2); the
antioxidant-vs-residual-disease half is not — it is arguably *more* relevant now**, because residual
disease is the entire premise of the window.

### 6.4 Ketogenic diet — wrong-signed by this framework's own reservoir model

This one matters because ketogenic diet is probably the single most popular "metabolic" intervention in
cancer patient communities, and the repo's model argues against it *for this compartment*:

- The ketogenic rationale is **anti-Warburg**: restrict glucose to starve glycolysis-dependent cells.
  `[Mechanistic]` But ADR-0021/`CASE-BASELINE.md` §4 say chemotherapy has already cleared the
  **glycolytic, cycling bulk** — twice. The rationale is aimed at the solved problem.
- **The β-hydroxybutyrate paradox** is the direct hit: the effect **depends on tumour oxidative
  phenotype** — *"oxidative cells would use 3-OHB as an additional energy source, so tumours with
  predominantly oxidative cells increase growth when this metabolite is available."* In HeLa xenografts a
  **ketogenic diet increased tumour growth and reduced mouse survival**, attributed to active ketone
  consumption. PMC5331634 `[Preclinical-Animal, VERIFY]`
- **The reservoir is OXPHOS-high and FAO-dependent** (ADR-0023 §5.1). Ketones are a **preferred OXPHOS
  substrate**. So the model predicts ketosis **supplies** the reservoir's fuel of choice.

> **Balance, because this cuts both ways and I should not overstate it.** Other models show ketogenic diet
> *helping*: β-hydroxybutyrate suppressed bladder cancer growth and enhanced anti-PD-L1 efficacy
> (*Cancer Science* 2026, DOI 10.1111/cas.70447), ketogenic diet enhanced PD-L1 blockade in renal cell
> carcinoma (PMC11154604), inhibited CT26 colon allograft growth via immune mechanisms, and combined with
> chemotherapy in pancreatic models. Also relevant: *low ketolytic enzyme levels predict ketogenic
> response* (PMC5880499) — i.e. the effect is **enzyme-expression-dependent and measurable**, which is a
> real forward-hypothesis handle. **The honest verdict is not "keto is bad" — it is "keto's direction is
> tumour-phenotype-dependent, and this patient's hypothesised reservoir phenotype is the one predicted to
> benefit from ketones."** Nearly all the positive data are also **combination-with-immunotherapy** data,
> which §2 says is unavailable in this window.

### 6.5 Iron — genuinely contested, recorded at low weight

Ferroptosis needs labile iron, so iron status looks like a dietary lever. The literature disagrees:

- **For:** elevated ferritin reduces free iron and **suppresses** ferroptosis, while low ferritin raises
  labile iron and **promotes** it; exogenous iron can potentiate ferroptosis via GPX4-dependent and
  -independent routes. `[Preclinical-Cell, VERIFY]`
- **Against:** **"Labile iron pool dynamics do *not* drive ferroptosis in colorectal cancer cells"** —
  *J Biol Chem* 2026 / bioRxiv 2025.07.01.662602, PMC13089158 `[Preclinical-Cell, VERIFY]`

> **Verdict: contested; do not build on it.** I am recording it only because ferritin is measurable from
> routine labs and someone will otherwise reason from the "iron feeds ferroptosis" half. Iron
> supplementation or restriction in a cancer patient is a clinical decision with haematological
> consequences far outside this mechanism.

### 6.6 The register, compactly

| Natural agent | Popular rationale | What the reservoir model predicts | Tier / confidence |
|---|---|---|---|
| **Selenium (supra-sufficiency)** | "antioxidant, immune support, cancer prevention" | **Wrong-signed** — GPX4 is a selenoprotein; more selenium → more GPX4 capacity → *more* ferroptosis resistance | `Preclinical-Cell` mechanism → `Mechanistic` here / **Low-Medium**, and SELECT is a real clinical warning |
| **Vitamin E / tocotrienols (high-dose)** | "antioxidant, membrane protection" | **Wrong-signed** — the most direct dietary ferroptosis inhibitor known (α-TQH₂ → 15-LO inhibition) | `Preclinical-Cell` → `Mechanistic` / **Low-Medium**, SELECT again |
| **NAC / high-dose thiol antioxidants** | "detox, glutathione support" | **Wrong-signed** — feeds the GSH-consuming GPX4 reaction; plus the pre-existing NAC-metastasis signal | `Preclinical-Animal` / **Medium** (already a repo caution) |
| **Ketogenic diet** | "starve the Warburg tumour" | **Plausibly wrong-signed *for this compartment*** — ketones fuel OXPHOS-high cells; aimed at the bulk chemo already clears. Direction is phenotype-dependent; positive data are mostly combination-with-ICB | `Preclinical-Animal`, **conflicting** / **Low** |
| **Urolithin A (mitophagy inducer)** | "mitochondrial renewal" | **Plausibly wrong-signed** — clears the damaged mitochondria whose accumulation is Camp A's dormant-cell kill mechanism | `Mechanistic` / **Low** (no dormancy data either way) |
| **Iron manipulation** | "iron drives ferroptosis" | **Contested** — direct negative evidence exists | `Preclinical-Cell`, **conflicting** / **Low** |

**What this register is not:** a claim that any of these causes relapse, or an instruction to stop anything
anyone is taking. Several are essential nutrients where **deficiency** is the real risk and correction is
standard care. The repo's long-standing rule applies unchanged: **correct deficiency, don't megadose** — and
the only party who can tell the difference for a specific person is the treating team with their labs.

---

## 7. If I had to say what is defensible in this window, and on what grounds

Reorganised by *justification*, because the grounds matter more than the list:

**A. Justified on immune-surveillance grounds (the strongest lane).**
Structured exercise is the only item with phase-3 recurrence data anywhere (§4), its dissected mechanism is
NK-dependent, and it is fusion-agnostic with no access barrier — subject entirely to the irradiated-limb
rehabilitation caveat, which is a clinical question. Cyclic fasting-type eating patterns and adequate
fibre/fermented intake (microbiome→SCFA→immune priming, ADR-0005) belong here too, **justified as immune
conditioning rather than as autophagy induction** (§3.3) — and at much lower evidence weight. Sleep and
circadian regularity sit in the same lane at `Mechanistic`.

**B. Justified on membrane-lipid grounds (the one specific food mechanism).**
Dietary omega-3 EPA/DHA, per FH-11.1 — the repo's existing best-cross-vector dietary compound, now with a
reservoir-specific rationale, a hint of a normal-tissue window, and `Preclinical-Cell` evidence that
includes drug-tolerant cells. Its mirror is the §6 restraint: **not** stacking lipid-soluble antioxidant
megadoses on top, which would work against the same mechanism.

**C. Justified as measurable host variables rather than interventions.**
ADR-0005 already noted that the only host factors at clinical-grade evidence in sarcoma are the ones
**readable from routine labs and the surveillance CT**: systemic inflammation (NLR/CRP/mGPS),
sarcopenia/body composition, and nutritional status. A surveillance window generates those numbers anyway
at no extra cost. **This is the cheapest genuinely informative thing in the document**, and it is
measurement, not intervention. Micronutrient **sufficiency** (including selenium and vitamin D) is a lab
question with a defined target, not a maximisation target.

**D. Not justified on current evidence:** ketogenic diet for this compartment (§6.4), autophagy-directed
supplementation in either direction (§3), urolithin A (§3.3), iron manipulation (§6.5), and every
high-dose antioxidant (§6.3).

**The framing I would keep:** in this window the best-supported moves act on the **host and the immune
system**, not on the tumour cell — and the second-best act on **membrane lipid composition**. Nothing
available acts on the reservoir directly with any evidence behind it. That is an honest description of a
thin field, not a hedge.

---

## 8. Forward hypotheses

**[FH-11.1]** Dietary omega-3 membrane enrichment as a ferroptosis-sensitising prime for the dormant
reservoir — stated in full in §5, with three falsifiers.

**[FH-11.2] The lipid-antioxidant protection paradox is a modifiable determinant of reservoir
ferroptosis susceptibility.** *Hypothesis:* in a patient whose residual reservoir is GPX4-dependent,
**selenium and vitamin E status above sufficiency measurably raises the ferroptotic threshold** of residual
cells — making "antioxidant optimisation" a net-negative intervention in the surveillance window
specifically, and offering a mechanistic account of SELECT's harm signal. *Mechanistic basis:* GPX4 is a
selenoprotein whose synthesis is selenium-limited (PMID 29290465); selenoprotein P preserves GPX4 →
ferroptosis resistance (PMC10770386); α-tocopherol hydroquinone inhibits 15-LO via iron reduction
(PMID 30110365). *Test:* in a round-cell-sarcoma persister model, titrate selenium and α-tocopherol and
measure the GPX4-inhibitor (RSL3) IC₅₀ shift and lipid-peroxidation markers. *Falsifier:* no IC₅₀ shift
across a physiological-to-supraphysiological range → selenium/vitamin E are not rate-limiting and the
concern dissolves. *Tier:* `Mechanistic`. **This is the most decision-relevant hypothesis in the document
because it argues against something easy to do, rather than for something hard to get.**

**[FH-11.3] Exercise as NK-window maintenance, and the tonic-vs-pulsatile adrenergic distinction.**
*Hypothesis:* the antitumour component of exercise in a surveillance window operates through **repeated
acute epinephrine/IL-6 pulses mobilising and redistributing cytotoxic NK cells** — mechanistically distinct
from, and compatible with, ADR-0005's finding that *chronic* sympathetic tone is pro-metastatic. Prediction:
chronic β-blockade blunts it; stress-reduction (lowering tonic tone) and exercise (adding pulsatile tone)
are **not** antagonistic. *Basis:* PMID 26895752 (NK-depletion abolishes the effect; β-blockade blunts it) +
CHALLENGE's clinical result + ADR-0005's autonomic row. *Test:* NK number/function and NKG2D/CD107a
kinetics before and after acute exercise bouts in survivors, stratified by β-blocker use. *Falsifier:* no
NK mobilisation difference, or equal benefit under β-blockade. *Tier:* `Mechanistic` (bridging a
`Preclinical-Animal` mechanism to a `Clinical-Trial` outcome in another tumour). **Resolves a real internal
conflict in the repo.**

**[FH-11.4]** Mitophagy induction is plausibly wrong-signed for a dormant reservoir — stated in full in
§3.3, with its falsifier.

**[FH-11.5] Ketolytic-enzyme expression is a cheap predictive gate that would settle the keto question
for this patient.** *Hypothesis:* the reservoir's ketone-utilisation capacity (OXCT1/SCOT, BDH1) determines
whether ketosis starves or **feeds** it, so a ketolytic-enzyme read on **archived P1 FFPE** would convert an
unanswerable diet question into a testable one. *Basis:* "low ketolytic enzyme levels in tumors predict
ketogenic diet responses in cancer cell lines in vitro and in vivo" (PMC5880499) + the β-hydroxybutyrate
paradox (PMC5331634) + the OXPHOS-high reservoir read (ADR-0023 §5.1). *Why it is attractive:* it uses
**archived tissue** — the cheapest provenance tier in ADR-0011 — and it is **fusion-agnostic**. *Honest
caveats:* the archived primary may not represent the reservoir (the ADR-0011 P1-vs-P2 problem, and
ADR-0021's clonal-divergence caveat), IHC for these enzymes is not a standard assay, and this is emphatically
**not a testing recommendation** — it is a proposal for how the question *could* be made empirical. *Tier:*
`Theoretical`.

---

## 9. Red-team self-challenge (ADR-0017)

**Disconfirm — what would make this document wrong?**
Everything inherits ADR-0021/0023's load-bearing uncertainty: if the relapse was outgrowth of a
**pre-existing metastatic clone** (this tumour was metastatic at diagnosis with 12 nodules) rather than a
drug-tolerant persister state, then the ferroptosis/GPX4 reservoir model is the wrong frame and §5, §6.1–6.4
and three of the five forward hypotheses lose their premise. Separately, the ferroptosis-reservoir link is
`Low`-confidence **P4** with no sarcoma model, so §6 is a mechanistic argument, not a demonstrated risk.

**Alternative explanation — is the mitochondrial framing doing the work, or is the answer just "exercise
and eat well"?**
Largely the latter, and it should be said. §4 would be the top recommendation from any general
cancer-survivorship guideline without a word of mitochondrial biology. What the mitochondrial frame adds is
**(a)** the reason exercise belongs in *this* layer (PGC-1α, NK mitochondrial fitness), **(b)** a specific
target for omega-3 instead of generic anti-inflammatory hand-waving, and **(c)** §6 — which is where the
frame genuinely earns its place, because *no general guideline predicts that selenium and vitamin E might
be wrong-signed in a patient with a GPX4-dependent residual reservoir.* If §6 is the only durable
contribution here, that is still a contribution.

**Flip-test — would the opposite sound equally plausible?**
For autophagy, yes — and that is precisely §3's finding, which is why I refused to pick a side. For the
antioxidant register the flip is *"antioxidants protect normal tissue and reduce genomic instability"*
(the repo's own V2 rationale), which is a real and unresolved counter-argument that §6.3 states rather
than hides. Note the framework contains both: V2 argues for antioxidant sufficiency to reduce new damage;
§6 argues against antioxidant excess near residual disease. Both can be true — they concern different
compartments — but anyone reading only one will get the wrong idea.

**Steer-audit — did the user's framing bias the output?**
It did, twice, and in opposite directions. The request was to be *creative with autophagy, food and natural
remedies*, which invites an enthusiastic list; the honest answer turned out to be that **the autophagy lane
is directionless, the highest-value item is exercise (unglamorous, and a rehabilitation question in an
irradiated limb), and the most useful section is a list of popular natural agents to be wary of.** I have
also deliberately resisted the pull of the "control group / no medication" framing toward implying that
diet can substitute for surveillance: **it cannot, and the surveillance itself is the intervention with
established value here.** The document argues against several things the question pointed toward, which is
the symmetric-lane obligation under ADR-0020.

---

## 10. What I could not establish

1. **Any recurrence-outcome evidence for any of this in sarcoma.** None exists. The sarcoma exercise
   literature covers function, gait, disability and QoL, and one review states outright that the effect of
   increased activity on sarcoma growth/progression is **unknown**.
2. **The direction of autophagy modulation in a dormant reservoir.** The literature is genuinely split
   (§3.1 vs §3.2) and I could not resolve it. This is a real scientific controversy, not a gap in my search.
3. **Whether this patient's reservoir is GPX4-dependent, OXPHOS-high, or ferroptosis-susceptible at all.**
   Never measured; no assay has been done; no sarcoma model exists. Everything in §5 and §6 is class-level
   transfer.
4. **Whether dietary omega-3 can reach a membrane PUFA-PC enrichment sufficient for a ferroptosis effect
   in vivo.** The mechanism is real and incorporation is achievable, but the required magnitude is
   unestablished — this is golden rule #6 applied to the one dietary mechanism that plausibly escapes it,
   and I could not close it.
5. **Any current trial or regulatory status.** `clinicaltrials.gov` was **unreachable** (HTTP 403). The
   CLEVER trial (NCT03032406) status is **unverified**; urolithin A's regulatory position is reported from
   search text only.
6. **Full-text verification of anything**, CHALLENGE included. PubMed/PMC/Nature/EuropePMC/E-utilities all
   returned HTTP 403. CHALLENGE's numbers were concordant across several independent secondary sources,
   which raises confidence but is **not** verification.
7. **Whether the tonic-vs-pulsatile adrenergic reconciliation (FH-11.3) is correct.** It is my proposed
   resolution of a conflict between two repo rows; I found no source that states it in those terms.
8. **Quantitative anything.** No simulation was run. No posterior, no EVSI. The §7 ordering is judgment.
   Sim 11 (proposed in ADR-0023) would be the place to make the reservoir's metabolic dependencies and
   therapeutic window explicit, and §6/FH-11.2 give it a concrete first question.
9. **Entity grounding.** Still blocked — `huggingface.co` unreachable, repo venv absent in this container.
   New ungrounded entities: **ATG7, PFKFB3, OXCT1/SCOT, BDH1, SELENOP, ALOX15, urolithin A, spermidine,
   α-tocopherol hydroquinone, DHA/EPA, hydroxychloroquine, everolimus, β-hydroxybutyrate.**

---

## 11. The honest bottom line

The surveillance window is the setting with the **most patient motivation and the least evidence** in all
of oncology, and that asymmetry is what makes it a target for confident-sounding advice. What this analysis
actually supports is modest: **one intervention with real randomised recurrence data in a different cancer**
(exercise, mechanistically NK-dependent and therefore well-matched to this framework's immune thesis, but
constrained here by an irradiated limb), **one food mechanism with a specific reservoir target and
cell-level evidence** (omega-3 → membrane PUFA → ferroptosis threshold), **a set of measurements the
surveillance window already generates for free** (NLR/CRP, body composition, nutritional sufficiency), and
**a genuinely useful list of popular natural agents whose direction the framework's own model says is
probably backwards** (selenium and vitamin E megadoses, thiol antioxidants, ketogenic diet for an
OXPHOS-high compartment, mitophagy inducers).

And one thing that is not a mechanism at all: **the surveillance itself — the scans and the visits — remains
the intervention with established value in this window.** Nothing in this document competes with it, and
every item here is a question for the treating oncology team, not a plan.

---

*Authored 2026-09-17 under Era B (`CASE-BASELINE.md`, ADR-0022); extends ADR-0023 (mitochondrial/
endosymbiotic layer) and ADR-0005 (host-biology modifier layer); recorded as ADR-0024. Not a fifth vector
(golden rule #8). Forward-lane only under ADR-0020's `[VERIFY]` gate. Research simulation and hypothesis
generation only — not medical advice, not a diagnosis, and not a dietary, supplement, testing or treatment
recommendation.*
