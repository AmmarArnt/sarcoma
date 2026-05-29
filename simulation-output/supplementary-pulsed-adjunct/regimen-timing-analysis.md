# Supplementary Analysis — The Alternating-Week ("Pulsed Rest-Week Adjunct") Schedule

**Role:** Supplementary analyst (a supplementary team, not a fifth attack vector). Feeds the orchestrator; does not modify the four-vector catalog.
**Skills loaded:** `sarcoma-contract`, `sarcoma-chemo-interactions`, `sarcoma-pre-output-check`.
**Clean-slate:** No stored memory about any individual was used. This document reasons only from the case description provided and the public literature.

---

## One-line summary

This output evaluates the *steelman* of the patient's actual behavior — chemotherapy on-weeks, polypharmacology pulse (curcumin+piperine, liposomal vitamin C, black-cumin-seed-oil/thymoquinone, vitamin D, honey, fresh juice) during chemo-FREE rest weeks — as a *deliberately timed* schedule rather than naïve co-administration. It deliberately **excludes** any dosing, start/stop, or schedule instruction; it does not credit or recommend the regimen; it does not re-open the four-vector compound rankings.

**Confidence: medium** — the PK reasoning (competitive/reversible CYP inhibition with finite washout) is mechanistically solid and supported by real human-PK literature for piperine; the timing-separation principle is defensible; but there is **zero direct evidence in CIC-rearranged sarcoma**, the efficacy question is unanswerable from an n=1 with a concurrent known-effective regimen, and several of the steelman's load-bearing PK numbers (notably a precise thymoquinone CYP3A4 inhibition half-life in humans) have **no direct citation**.

---

## Framing: what "the steelman" actually claims, and what would falsify it

The prior catalog flagged curcumin/piperine, ascorbate, and thymoquinone as *potentially harmful around ifosfamide* — chiefly via (a) CYP3A4 modulation impairing ifosfamide's CYP3A4-dependent activation to 4-hydroxy-ifosfamide / isofosforamide mustard, and (b) ROS-axis antagonism of alkylator/anthracycline mechanisms by antioxidants.

The steelman is narrower and more disciplined than "natural = safe":

> "I never co-administered these *with* chemo. I pulsed them in the rest weeks. If the inhibitors have washed out before the next infusion, the CYP3A4 and ROS concerns the catalog raised do not apply to my actual schedule."

That is a **temporal-separation** argument. It is falsifiable on two axes:
1. **PK axis** — does the inhibition actually clear before the next ifosfamide exposure? (Sections 1.)
2. **Biology axis** — even with clean PK separation, does a rest-week antioxidant/polyphenol pulse do anything helpful, neutral, or harmful to *residual/oligometastatic* disease? (Sections 2, 3, 4, 5.)

A clean answer can be "PK-defensible AND biologically-unproven AND possibly-net-neutral" — those are not contradictory.

---

## 1. PK feasibility of the rest-week pulse as a *designed* washout

**Claim under test:** piperine and thymoquinone are competitive/reversible CYP3A4 inhibitors whose inhibition reverses fast enough that a rest-week pulse leaves no CYP3A4 inhibition standing when the next ifosfamide cycle starts.

### Mechanism (molecular, not analogical)
- **Ifosfamide** is a prodrug 4-hydroxylated chiefly by **CYP3A4** (and CYP2B6) to 4-hydroxy-ifosfamide → tautomerizes to aldoifosfamide → isophosphoramide mustard (the active alkylator) + acrolein; a competing N-dechloroethylation (CYP3A4-heavy) yields chloroacetaldehyde (neurotoxic/nephrotoxic). *Net:* CYP3A4 sits on the activation path, so a standing CYP3A4 inhibitor at infusion time could shift activation/toxification balance. **Tier: Established** (ifosfamide CYP3A4/2B6 activation is textbook pharmacology; e.g., Brain EGC et al., and the ifosfamide FDA label). [Mechanism Established; precise quantitative shift in this patient — no direct citation.]
- **Piperine** is a **mechanism-based (and partly reversible/competitive) inhibitor** of CYP3A4 and an inhibitor of P-gp; this is the basis of the curcumin bioavailability effect. **Tier: Preclinical-Cell / human-PK for the interaction direction.** The canonical human bioavailability datum is Shoba et al., *Planta Medica* 1998 (PMID 9619120) — **n=10, single dose, 2 g curcumin ± 20 mg piperine, curcumin-only control below LOD**; the widely-quoted "~2000% increase" is computed against a near-zero baseline and **must not be cited as a universal multiplier** (mandated caveat reproduced).
- **Thymoquinone** (active constituent of *Nigella sativa* / black cumin seed oil) inhibits CYP3A4 and CYP2C9 in vitro/animal models. **Tier: Preclinical-Cell / Preclinical-Animal.** A precise *human* CYP3A4 inhibition half-life for thymoquinone is **[no direct citation; I could not find a human PK study quantifying it].**

### The honest washout arithmetic
The defensible PK principle is: for a **reversible/competitive** inhibitor, enzyme function returns as the inhibitor is cleared — recovery tracks the inhibitor's elimination half-life, so ~**4–5 half-lives** gives effectively complete washout. For a **mechanism-based (irreversible/quasi-irreversible)** inhibitor, recovery instead tracks **enzyme resynthesis**, which for hepatic CYP3A4 has an estimated turnover/recovery on the order of **~1–3 days (t½ ~26–140 h across published estimates)** — i.e., recovery can lag the inhibitor's own clearance. This distinction is the crux:

- **Piperine** has mechanism-based components, so the conservative model is "CYP3A4 recovery follows enzyme resynthesis," not piperine's plasma half-life. Even on that conservative model, **a multi-day-to-one-week gap between the last rest-week piperine and the next infusion is comfortably within the enzyme-resynthesis window** — a **full 7-day chemo-free week is, on the published CYP3A4 turnover numbers, a defensible washout** for restoring baseline CYP3A4 before re-dosing ifosfamide. **Tier: Mechanistic (quantitative), built on Established CYP3A4-turnover pharmacology; the specific adequacy in this patient — no direct citation.**
- **Thymoquinone**: if competitive/reversible (the in-vitro signal), washout follows its elimination half-life and a several-day gap is more than sufficient; if it has mechanism-based components, the same ~1–3 day CYP3A4-resynthesis logic applies. Either way **a 7-day gap is defensible**, but I am explicit that the **human half-life underpinning this is not directly cited.**

### What washout interval is defensible?
**A defensible, conservatively-reasoned interval is "stop the CYP3A4-active pulse components at least several days — and ideally the full chemo-free week — before the next ifosfamide infusion,"** grounded in CYP3A4 enzyme-resynthesis kinetics (t½ ~1–3 days) rather than the inhibitors' plasma half-lives. **This is a PK-plausibility statement, not a schedule instruction.** The patient's described pattern (pulse confined to rest weeks, nothing on chemo on-weeks) is **PK-consistent with this principle** *if* the pulse genuinely ends before the on-week begins. The residual uncertainties: (i) no human thymoquinone CYP3A4 half-life; (ii) inter-individual CYP3A4 expression varies several-fold; (iii) the actual gap length in this patient is not specified to the day.

> **`sarcoma-chemo-interactions` screening lines**
> **Piperine** — CYP3A4: inhibitor, mechanism-based component (Shoba 1998 PMID 9619120 for the bioavailability consequence; mechanism reviewed broadly) | P-gp: inhibitor | ROS-axis: not a primary antioxidant at culinary dose | Other: enhances absorption of co-ingested compounds | Citation: PMID 9619120 + class pharmacology.
> **Thymoquinone / black cumin seed oil** — CYP3A4: inhibitor in vitro/animal | CYP2C9: inhibitor reported | P-gp: modulation reported | ROS-axis: context-dependent (antioxidant at low dose, pro-oxidant at high dose in some cell models) | Other: antiplatelet signal reported — relevant near surgery | Citation: in-vitro/animal only; **no human CYP-PK citation found**.
> **Curcumin** — CYP3A4: inhibitor (in vitro) | P-gp: inhibitor | ROS-axis: pleiotropic, low systemic exposure orally | Other: antiplatelet; bioavailability is the dominant limiter | Citation: in-vitro; human relevance bioavailability-limited.
> **Liposomal vitamin C (oral)** — CYP3A4: none clinically meaningful found | P-gp: none meaningful found | ROS-axis: see Section 2 — **oral cannot reach pharmacologic pro-oxidant plasma range** | Citation: Padayatty 2004 PMID 15068981 (oral vs IV ceiling).

---

## 2. Sensitizer-vs-antagonist, and the IV-vs-oral ascorbate distinction (the most-conflated point)

### Curcumin, timed before/after vs during cytotoxic therapy
The literature is genuinely **bidirectional and context-dependent**:
- Some preclinical work reports curcumin **sensitizes** tumor cells to chemo/radiation (NF-κB suppression, chemoresistance-pathway modulation). **Tier: Preclinical-Cell / some Preclinical-Animal; none in CIC-DUX4.**
- Other preclinical work raises an **antagonism** concern specifically for **ROS-dependent cytotoxics** (e.g., the antioxidant arm of curcumin scavenging the ROS that contributes to anthracycline/alkylator action) — this is the catalog's original worry. **Tier: Preclinical-Cell; clinical relevance unresolved.**
- **The timing logic:** the antagonism concern is overwhelmingly a *concurrent-exposure* concern (drug + scavenger in the same tissue at the same time). A pulse confined to chemo-free weeks, washed out before infusion, **largely sidesteps the during-chemo antagonism worry** — which is exactly the steelman's point and it is, on this axis, **valid**. What it does *not* do is convert curcumin into a demonstrated sensitizer; "doesn't interfere" ≠ "helps."
- **Evidence in CIC-DUX4 specifically? None direct.**

### Ascorbate — the critical IV-vs-oral split (often conflated)
This distinction is **load-bearing and the steelman partly mis-uses it in both directions**, so state it plainly:
- **High-dose IV pharmacologic ascorbate** reaches **millimolar plasma** concentrations and acts as a **pro-oxidant**, generating extracellular **H₂O₂** (Fenton chemistry, ascorbate radical), with downstream redox/KEAP1–NRF2-axis effects; this is the rationale in registered trials (e.g., adjunct to chemo in pancreatic/other cancers). **Tier: Clinical-Trial (other cancers); none in CIC-DUX4.** Pharmacology basis: Chen et al., *PNAS* 2005 (PMID 16157892); plasma-ceiling pharmacokinetics: Padayatty et al., *Ann Intern Med* 2004 (PMID 15068981).
- **Oral vitamin C — including "liposomal"** — is **capped by intestinal absorption and renal threshold at low-micromolar-to-~low-hundreds-µM plasma**; liposomal formulations raise absorption modestly but **do not reach the millimolar pharmacologic pro-oxidant window** that IV achieves. **Tier: Established (oral ceiling) — Padayatty 2004 PMID 15068981.** Therefore:
  - The patient's **oral liposomal vitamin C cannot be credited with the IV pro-oxidant anti-tumor mechanism** — that mechanism requires IV.
  - **And** the symmetric correction: because oral liposomal C stays in the *antioxidant* (not pro-oxidant) range, the relevant concern for it is the **antioxidant-during/around-chemo** worry and the **Sayin metastasis caveat** (Section 5), **not** the pro-oxidant trial mechanism. Conflating the two (assuming oral liposomal C "does what IV vitamin C does in trials") is the single most common error here and the steelman should not lean on it.

**Net for Section 2:** rest-week timing genuinely defuses the *concurrent* antagonism concern for curcumin and oral C; but it buys *neutrality*, not demonstrated benefit, and it cannot borrow the IV-ascorbate pro-oxidant story for an oral formulation.

---

## 3. The honest confounding analysis (n=1 with a concurrent known-effective therapy)

State this without hedging:

- **The >95% necrosis at the Jan 2025 surgery is attributable to VDC/IE**, a regimen with established high activity in Ewing-family/CIC-rearranged disease. A >90% necrosis response is a recognized good-response benchmark *for the chemotherapy*. The rest-week supplements **cannot be credited** — there is no counterfactual arm, and the known-effective agent is sufficient to explain the result. **Tier: Established (VDC/IE activity); supplement contribution unestablished and unmeasurable here.**
- **The symmetric, equally-important point:** the patient **relapsed (single-lung oligometastatic) during the NED year *while taking the maintenance supplement regimen*.** So "it worked last time" **cannot stand** — the same regimen was running when relapse occurred. An honest reading is that the maintenance pulse **did not prevent relapse**; whether it delayed, accelerated, or had no effect is **unknowable from n=1**.
- **What an n=1 with a concurrent known-effective therapy can and cannot establish:**
  - *Can:* establish tolerability/feasibility of the schedule in this person; establish that gross harm was not obvious (a weak signal — absence of obvious harm ≠ safety).
  - *Cannot:* establish efficacy in **either** direction; cannot attribute the good chemo response to the pulse; cannot exonerate the pulse from any role in relapse; cannot distinguish "helped," "neutral," or "harmed." The concurrent presence of a known-effective cytotoxic regimen makes the supplement effect **non-identifiable**.

This section is the strongest reason the overall verdict lands on "defensible to have done, says nothing about efficacy."

---

## 4. The metronomic / chemo-free-interval adjunct concept — is "pulse in the gaps" a recognized strategy?

- **Metronomic chemotherapy** (low-dose, frequent, anti-angiogenic/immunomodulatory) is a recognized, literatured strategy — but it refers to *cytotoxic dosing schedules*, not to dropping a polyphenol cocktail into the rest weeks of a conventional regimen. **Tier: Clinical-Trial / Established concept (for cytotoxics), not for supplement cocktails.** Mapping "metronomic" onto a supplement pulse is an **analogy, not an established strategy** — flag it as such.
- **"Pulse a polypharmacology cocktail in the chemo-free interval" as a designed adjunct strategy:** I found **no recognized, named strategy with supporting trial literature** for this specific construct. **[No direct citation — this is not an established strategy.]** It is a *hypothesis*, addressed in Section 6.
- **Is there a CIC-DUX4 / BRD4 / super-enhancer-specific rationale for the rest-week timing?** A *mechanistic* one can be sketched but is **untested**: cytotoxic on-weeks debulk and partially synchronize surviving cells; cells re-entering cycle during the recovery/rest week transiently up-regulate the proliferative, BRD4-amplified ETV4/ETV5→CCND1/MYC program (the "loop" of file 02). A rate-limiting pulse (V1-type BRD4/cell-cycle friction) *timed to that re-entry window* is **conceptually aligned** with hitting cells when the super-enhancer program is most active. **BUT:** (i) dietary BRD4 "inhibitors" (curcumin, EGCG) act at concentrations not achievable from oral intake (concentration-mismatch — file 05 bioavailability caveats); (ii) there is **no CIC-DUX4 evidence** that rest-week cell-cycle re-entry is a real exploitable window; (iii) thymoquinone/curcumin antioxidant activity in that same window could, per Section 5, be unhelpful in residual disease. **Tier: Mechanistic / Theoretical; none direct in CIC-DUX4.**

---

## 5. The Sayin-2014 antioxidant-promotes-metastasis caveat in residual/oligometastatic disease

- **Sayin et al., *Sci Transl Med* 2014 (PMID 24477002):** antioxidants (NAC, vitamin E) **accelerated progression and metastasis** in mouse lung-cancer/melanoma models — the mechanistic reading is that antioxidants relieve oxidative stress on disseminating/residual tumor cells, reducing a barrier to metastatic outgrowth (later work implicated reduced oxidative stress and altered redox/BACH1 and related axes). **Tier: Preclinical-Animal.** Reinforced by the human supplement-harm record the contract mandates citing: **β-carotene increased lung cancer in smokers (ATBC/CARET)**, **vitamin E increased prostate cancer (SELECT)** — "natural ≠ safe."
- **Applied to this patient's situation specifically — residual/oligometastatic disease + *oral liposomal* vitamin C:**
  - This is the **highest-relevance caveat in the whole document**, because the concern is precisely about **antioxidant support of residual/disseminating cells during a tumor-bearing interval** — which is exactly the rest-week, NED/oligometastatic context, **not** the during-infusion context. Timing separation from chemo **does not** address this; if anything the rest-week pulse sits squarely in the window the Sayin model warns about.
  - The oral-vs-IV split (Section 2) makes it **worse, not better, for the steelman**: oral liposomal C stays in the **antioxidant** range, so it is the *Sayin-relevant* form, whereas only IV reaches the pro-oxidant range that might cut the other way.
  - **Honest magnitude:** the Sayin signal is **mouse, supraphysiologic NAC/vitamin-E dosing, not vitamin C, not CIC-DUX4, not oligometastatic sarcoma.** It is a **mechanistic red flag, not a demonstrated effect** for oral liposomal vitamin C in this disease. **It should temper — not veto — but it specifically argues that the rest-week antioxidant pulse is the component least exonerated by the timing argument**, because its theoretical risk window is the tumor-bearing rest week itself.

---

## 6. Forward Hypotheses (hypothesis generation, NOT recommendation; no doses, no start/stop)

> Explicit framing: these are mechanistically-defensible, testable formulations of a "designed pulsed rest-week adjunct." None is a recommendation, dose, or schedule instruction. Each is labeled with what would test it and why it has not been tested.

### [Forward Hypothesis 1] — Rest-week BRD4/cell-cycle-friction pulse timed to post-cytotoxic cycle re-entry
- **Statement:** In CIC-DUX4 sarcoma, surviving cells re-entering cycle during the chemo-free recovery week transiently maximize BRD4-amplified ETV4/ETV5→CCND1/MYC output; a rate-limiting intervention (a *clinical-grade* BET or CDK4/6 modulator — explicitly **not** a dietary polyphenol at culinary exposure) delivered in that window would impose maximal friction with minimal overlap-toxicity against the cytotoxic on-week.
- **Mechanistic basis:** super-enhancer dependency of the fusion program (file 02); cell-cycle synchronization after cytotoxic debulking.
- **Test:** PDX or cell-line model of CIC-DUX4 with alternating cytotoxic / BET-or-CDK4-6-inhibitor scheduling vs continuous vs on-week-concurrent; endpoints = residual viable fraction, ETV4/ETV5 and CCND1/MYC transcript levels, EdU re-entry kinetics across the rest week. **Biomarkers:** ETV4/ETV5 mRNA, Ki-67/EdU, H3K27ac ChIP at ETS super-enhancers.
- **Why not tested:** scheduling-interaction studies are expensive, CIC-DUX4 is ultra-rare, and the obvious agents are clinical (not dietary) — outside the usual "supplement timing" literature. **Tier: Theoretical (CIC-DUX4).** *Note: this hypothesis deliberately replaces the dietary cocktail with clinical agents, because the dietary versions fail the concentration test.*

### [Forward Hypothesis 2] — Rest-week as a *redox-neutral* (not antioxidant-loaded) interval to avoid the Sayin window
- **Statement:** If the Sayin-type concern is real for residual CIC-DUX4 cells, then the *correct* designed rest-week is one that **avoids systemic antioxidant loading** during the tumor-bearing interval — i.e., the testable hypothesis is that **removing** the rest-week antioxidant pulse (oral C, thymoquinone, curcumin) is non-inferior or superior for metastasis-free survival, inverting the patient's actual behavior.
- **Mechanistic basis:** Sayin 2014 (PMID 24477002); redox-dependence of disseminating-cell survival.
- **Test:** PDX metastasis-outgrowth model (CIC-DUX4 lung-colonization) ± physiologic-range antioxidant exposure during chemo-free intervals; endpoint = metastatic burden / lung-colony count, circulating tumor-cell viability. **Biomarkers:** intratumoral ROS markers, NRF2/BACH1-axis readouts.
- **Why not tested:** "does the popular supplement *hurt*?" is under-incentivized and ethically/logistically hard in humans; mouse work is feasible but unfunded for this rare entity. **Tier: Theoretical (CIC-DUX4) / Preclinical-Animal-supported direction.**

### [Forward Hypothesis 3 — bonus] — PK-verified washout as the enabling condition, made measurable
- **Statement:** A designed pulsed adjunct is only PK-defensible if CYP3A4 activity has demonstrably returned to baseline by infusion day; this is directly measurable.
- **Test:** CYP3A4 phenotyping (e.g., midazolam or 4β-hydroxycholesterol probe) at end-of-rest-week vs start-of-on-week in volunteers taking the pulse, to empirically confirm the ~enzyme-resynthesis washout assumed in Section 1. **Endpoint:** probe-drug clearance recovery to baseline.
- **Why not tested:** no one has formalized this specific lay schedule as a study; the probe-PK design is standard and cheap, which is exactly why it's a clean forward test. **Tier: Mechanistic (directly testable).**

---

## What I Could Not Establish

1. **A human thymoquinone CYP3A4 inhibition half-life** — the steelman's PK claim for black cumin seed oil rests on in-vitro/animal data; **no direct human-PK citation found.** The washout argument for thymoquinone therefore borrows the general reversible-vs-mechanism-based framework rather than a measured value.
2. **Whether the patient's actual gap was long enough** — the case says "rest weeks," not the exact last-dose-to-infusion interval; PK-defensibility is conditional on that gap.
3. **Any efficacy signal in either direction** — non-identifiable in this n=1 (Section 3).
4. **Any CIC-DUX4-specific data** for curcumin, thymoquinone, ascorbate, honey, vitamin D, or the juice components — **None direct** for all.
5. **Honey and the fresh juice** — not separately PK/efficacy-analyzed here beyond noting honey is a sugar matrix with trace polyphenols (no plausible systemic anti-tumor mechanism at intake) and the juices are whole-food micronutrient/polyphenol sources (Dietary-Observational at most); neither is a known strong CYP3A4 actor at culinary intake, but grapefruit-class furanocoumarins are absent from this list (a point in the schedule's favor). **Tier: Dietary-Observational / Mechanistic.**
6. **Vitamin D** — its relevance is deficiency-correction (clearer evidence) vs replete-supplementation (thin); not a chemo-timing concern; not analyzed as a CYP3A4 risk.

---

## Atypical-case note (~5% fusion-unconfirmed)

This patient is **fusion-UNCONFIRMED** (the ~5% subgroup). Nothing in this timing analysis depends on the CIC-DUX4 fusion protein being present: the PK washout argument (Section 1), the IV-vs-oral ascorbate distinction (Section 2), the confounding logic (Section 3), and the Sayin caveat (Section 5) are all **fusion-agnostic** and apply regardless of fusion status. Only Forward Hypothesis 1's super-enhancer rationale is fusion-dependent and would not apply if the tumor is truly not CIC-DUX4-driven — flagged accordingly.

---

## Calibrated bottom line

**Does the alternating-schedule framing change the catalog's "potentially harmful around ifosfamide" verdict?**

**It softens it for the CYP3A4/co-administration axis, and it makes the rest-week *use* defensible — but it says nothing about efficacy, and it does NOT soften the antioxidant-in-residual-disease (Sayin) axis.**

Concretely:
- **CYP3A4 / ifosfamide-activation concern:** **softened/largely defused** *if* the pulse genuinely ends several days-to-a-week before infusion. Temporal separation is a real PK principle; CYP3A4 enzyme-resynthesis kinetics make a full chemo-free week a defensible washout. The catalog's "harmful *around* ifosfamide" flag was implicitly a *concurrent-exposure* flag; the patient was not concurrent. **This part of the steelman is honest and holds.**
- **Antioxidant ROS-antagonism *during* chemo:** **defused by timing** — same reasoning.
- **Antioxidant support of residual/oligometastatic cells (Sayin):** **NOT defused — arguably the opposite.** The theoretical risk window for the oral liposomal vitamin C / thymoquinone / curcumin antioxidant pulse is the tumor-bearing rest week itself. Timing separation from chemo does not touch this, and the oral-vs-IV split means the oral C cannot claim the pro-oxidant trial mechanism that would cut the other way.
- **Efficacy:** **unestablished in either direction.** The >95% necrosis is VDC/IE's; relapse occurred *on* the maintenance pulse. "It worked last time" does not survive examination.

**Single sentence:** *The alternating-week framing is a legitimate, PK-defensible reason to stop calling the rest-week pulse "harmful around ifosfamide" on the CYP3A4/concurrent-ROS axis — it makes the rest-week use defensible — but it provides no evidence of benefit, leaves the Sayin antioxidant-in-residual-disease concern intact (and pointed straight at the rest week), and the n=1 history establishes nothing about efficacy in either direction.*

> **Orchestrator annotation (mandatory):** potential interactions with standard-of-care chemotherapy and concurrent medications — must be reviewed by the patient's oncologist before any change. Nothing in this document is a dose, schedule, or start/stop instruction.

---

### Pre-output self-audit (sarcoma-pre-output-check)
- **Part A:** (1) Citations — Shoba PMID 9619120, Chen PMID 16157892, Padayatty PMID 15068981, Sayin PMID 24477002 are real; everything else marked `no direct citation`. ✓ (2) Concentration mismatch — flagged for dietary BRD4 inhibitors and IV-vs-oral ascorbate. ✓ (3) Cancer-class generalization — "None direct in CIC-DUX4" stated throughout. ✓ (4) Analogy-as-evidence — metronomic mapping explicitly labeled an analogy; biology stated. ✓ (5) Dose invention — no doses; explicitly refused. ✓ (6) "Natural=safe" — Sayin/ATBC/CARET/SELECT cited; thymoquinone antiplatelet flagged. ✓ (7) Chemo interactions — screening lines provided. ✓ (8) Padding — kept tight. ✓
- **Part B:** one-line summary ✓; confidence line ✓; per-entry tiers ✓; molecular mechanisms ✓; CIC-DUX4-specific = None direct ✓; "What I Could Not Establish" ✓; ≥2 Forward Hypotheses (3 given) ✓; atypical-case note ✓.
- **Citation-chain check:** every load-bearing PK number that lacks a source (thymoquinone human t½; precise CYP3A4 turnover for this patient) is explicitly marked `no direct citation`. ✓
