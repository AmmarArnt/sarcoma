# Counterfactual Trial Forensics & Redesign — CIC-Rearranged Sarcoma

**Role:** Supplementary forward-simulation team (NOT a fifth attack vector). The four vectors in `docs/00-README.md` are fixed; this output maps each intervention class onto V1/V3/V4 and feeds the orchestrator. It does not modify the four-vector compound rankings.

**Skills loaded:** `sarcoma-contract`, `sarcoma-chemo-interactions`, `sarcoma-pre-output-check`.

**Clean-slate:** No stored memory about any individual was used. Reasoning is from the project docs (00, 02, 04, 05) and general biomedical knowledge only.

---

## CRITICAL METHOD CAVEAT — READ FIRST

**Live web access (WebSearch / WebFetch) was DENIED in this run.** I could not query PubMed, ClinicalTrials.gov, FDA/EMA labels, or any primary source to verify, freshen, or discover citations. Per the `sarcoma-contract` hard rule, **I have invented no PMIDs and no NCT numbers.** Where a trial or paper is broadly and reliably known at the level of medical-school / oncology-fellowship common knowledge (e.g., SARC028 existed; tazemetostat is FDA-approved for epithelioid sarcoma; ATBC/CARET/SELECT exist), I state it and tag it, but I append **"[exact citation not verified this run]"** so the orchestrator knows it must be re-grounded before any external use. Where I would normally cite a specific finding and cannot recall it with confidence, I write **"no direct citation."** Every numeric trial result (response rates, n, p-values) that I am not certain of is flagged as approximate or omitted. **The orchestrator must treat this entire document as citation-unverified and re-ground it against live sources before relying on any specific trial fact.**

**Confidence: medium for the mechanistic/counterfactual reasoning; low for any specific trial datum** (because verification was unavailable). The *forensic logic* — why a class underperforms, what is mechanistically different in CIC-DUX4, what to try differently — is robust to citation gaps because it rests on pathway biology described in `docs/02`. The *evidentiary scaffolding* (which exact trial, what exact ORR) is the weak part and is flagged throughout.

---

## One-line summary

For each major intervention class (BET, EZH2, CDK4/6, checkpoint blockade, the fusion itself, the antioxidant counterfactual), this document runs a five-part forensic — (a) why it underperformed, (b) what is mechanistically different about CIC-DUX4, (c) what could have been tried differently, (d) whether failure was structural/resource-limited, (e) whether the molecule hit its target — then proposes redesigned trials. It deliberately **excludes** any dosing, start/stop, or per-patient instruction, and does not credit any approach as proven in CIC-DUX4 (almost none is).

---

## Orientation: the CIC-DUX4 program in one paragraph (from docs/02)

CIC-DUX4 is a **neomorphic transcriptional activator**: the CIC HMG-box still finds the ETS-target genomic addresses (ETV1/ETV4/ETV5 loci) but the DUX4 C-terminal transactivation domain replaces CIC's repressor domain, **inverting the logic from silencing to amplification**, and the ERK-phosphorylation off-switch is physically gone, so the activator is constitutive. Output is amplified epigenetically (BRD4 at de-novo super-enhancers; BAF-maintained open chromatin) and executed by the cell-cycle machinery (CCND1/CCND2–CDK4 → Rb → E2F; MYC; CCNE1). Frequent CDKN2A co-deletion removes a brake. The tumor is immunologically "cold": MHC-I-low, low TMB, immunosuppressive microenvironment. Prognosis is worse and chemosensitivity lower than Ewing. **Every counterfactual below turns on one of these facts.**

A recurring structural truth dominates the whole field: **CIC-rearranged sarcoma is rare (a few hundred reported cases globally), has no validated predictive biomarker beyond fusion presence, has never had a dedicated powered randomized trial, and has very few public cell lines / PDX models.** Almost every "it didn't work" is therefore contaminated by underpowering and by the tumor being a tiny, unselected fraction of a basket trial. This is decisive context for the "(d) resource/structural" sub-question and is given its own cross-cutting section.

---

# CLASS 1 — BET inhibitors (BRD4) → Vectors V1 / V3

**Mapping:** V1 (rate-limit the amplification of the loop's output) and V3 (collapse the super-enhancers that make the fusion's output dominant). Tier for clinical BETi as a class: **Clinical-Trial** (in fusion-driven cancers broadly); for CIC-DUX4 specifically: **Preclinical-Cell at best; no direct CIC-DUX4 clinical data** (the disease is too rare for a dedicated BETi trial).

### (a) Why did it underperform?
Single-agent BET inhibitors (e.g., the JQ1 chemotype as a tool; clinical OTX015/birabresib, BMS-986158, molibresib, others) have generally produced **modest, non-durable monotherapy responses across the fusion-driven and hematologic cancers where they have been tested** [class-level statement; exact CIC-DUX4 trial does not exist; broad clinical-trial fact, exact citation not verified this run]. The mechanistic reasons are well characterized in BET biology:
- **Feedback reactivation / BRD4 reaccumulation.** Acute BETi displaces BRD4 from chromatin, but cells compensate — kinase rewiring (e.g., relief of negative feedback on RTK/PI3K and WNT/β-catenin signaling) and transcriptional adaptation restore super-enhancer output. The pharmacology is "displace, then the target washes back on."
- **Narrow therapeutic window / on-target toxicity.** BRD4 is required in normal tissue (thrombocytopenia, GI toxicity), capping the achievable tumor exposure. You cannot simply push the dose to overcome reaccumulation.
- **PK / reversible occupancy.** Reversible bromodomain binders require sustained trough coverage; intermittent schedules let BRD4 return.
- **Monotherapy against a multiply-buffered program.** BRD4 amplifies the loop but is not the loop's only support (BAF-maintained open chromatin, CDK7/9 elongation, MYC).

### (b) What is mechanistically DIFFERENT about CIC-DUX4 vs where BETi "worked best"?
BETi's clearest activity is in **MYC-addicted hematologic disease (e.g., NUT carcinoma, certain lymphomas/leukemias)** where a single super-enhancer–MYC axis is rate-limiting. In CIC-DUX4 the rate-limiting node is **upstream of MYC** — the neomorphic activator itself (CIC-DUX4 → ETV1/4/5 → CCND/CDK4/MYC). BRD4 is an **amplifier of an activator that BETi does not touch.** Unlike EWSR1-FLI1, where the EWSR1 low-complexity/IDR domain is heavily implicated in condensate-mediated recruitment of BRD4 and the transcriptional apparatus, the **condensate biology of CIC-DUX4 is far less characterized** (docs/02 explicitly: "IDR/phase separation: less characterized"). So the analogy "BETi collapses the fusion's super-enhancers" is borrowed from Ewing and is **not yet confirmed in CIC-DUX4**.

### (c) What could have been tried DIFFERENTLY?
- **BET-PROTAC instead of reversible inhibitor.** Degraders (ARV-771, dBET6 class) remove BRD4 protein rather than transiently blocking the bromodomain → defeats the "wash-back" problem and can suppress the scaffolding (non-bromodomain) functions of BRD4. Tier: **Preclinical** (degraders broadly); **Theoretical for CIC-DUX4** [no direct citation].
- **Vertical combination with CDK7 or CDK9 inhibition.** BRD4 and CDK7/9 both serve Pol II pause-release/elongation at super-enhancers; co-targeting attacks the elongation machinery from two angles and is mechanistically synergistic against super-enhancer-addicted transcription. Tier: **Preclinical** (combination concept in other SE-driven cancers); **Theoretical for CIC-DUX4**.
- **Combination with CDK4/6 inhibition** to convert BETi's transcriptional throttling into durable cell-cycle exit (see Class 3 — addresses BETi's cytostatic-not-cytotoxic problem).
- **Combination with the feedback node** that drives reaccumulation (e.g., the relieved RTK/PI3K arm) — i.e., pair BETi with the V1 upstream-RAS/ERK dampening logic.
- **Schedule redesign:** continuous trough coverage vs intermittent, or degrader-enabled longer dosing intervals.

### (d) Resource / structural limitation?
**Yes, severely.** There has never been a CIC-DUX4-dedicated BETi trial; all human BETi exposure in this disease would be incidental basket-trial enrollment of one or two patients, which is uninterpretable. Preclinical BETi work in CIC-DUX4 is limited by the small number of available cell lines. So "BETi is modest" is, for CIC-DUX4 specifically, **a statement about Ewing/other tumors transferred by analogy, not a tested CIC-DUX4 result.**

### (e) Did the molecule hit its target?
At the biochemical level, yes — clinical BETi occupy BD1/BD2 and acutely displace BRD4 (target engagement is established for the class). The failure is **not "missed the target" but "the target was insufficient and reversibly engaged":** displacement is transient, reaccumulation occurs, and BRD4 is one node in a buffered network. This is the classic "right target, wrong durability/wrong dependency-share" pattern.

---

# CLASS 2 — EZH2 inhibitors (tazemetostat) → Vector V3 (bridging to V4)

**Mapping:** V3 (reopen suppressed chromatin / differentiation) and the **V3→V4 MHC-I priming bridge.** Tier: **Established** (tazemetostat, FDA accelerated approval for epithelioid sarcoma and for EZH2-mutant follicular lymphoma) [broadly known; EMA status differs and was not verifiable this run — flag]; for CIC-DUX4: **Theoretical / Mechanistic; no direct efficacy data.**

### (a) Why did it (or would it) underperform?
EZH2i's CIC-DUX4 rationale is **extrapolated**, and the extrapolation is shakier than it looks. In epithelioid sarcoma the dependency is concrete: **SMARCB1 (BAF) loss leaves PRC2/EZH2 running unopposed**, so the cell is addicted to EZH2 and EZH2i crashes that addiction (docs/04 "Bug Type 2: corrupted filesystem"). **CIC-DUX4 is not a BAF-loss tumor.** The fusion is a neomorphic *activator*; its problem is aberrant ON, not aberrant PRC2-mediated OFF. So the central question is whether a **PRC2 dependency actually exists in CIC-DUX4 at all** — and the honest answer from docs/02 is that it is unestablished. An EZH2i trial that simply assumed transfer from epithelioid sarcoma would likely underperform because **the dependency it targets may not be present.**

### (b) What is mechanistically DIFFERENT?
Epithelioid sarcoma: EZH2 maintains a *corrupted-OFF* state (tumor suppressors locked by H3K27me3). CIC-DUX4: the driver lesion is *aberrant-ON* of ETS targets. EZH2i is mechanistically aimed at the wrong failure mode for the *driver.* **However**, there are two non-driver angles where EZH2i could still matter in CIC-DUX4:
1. **Tumor-suppressor / differentiation re-expression** — if PRC2 is silencing differentiation programs the fusion has shut down, EZH2i could reopen them (consistent with V3's "force differentiation" goal). This is *secondary* reprogramming, not driver inhibition.
2. **MHC-I and antigen-presentation re-expression (the V4 bridge).** PRC2/EZH2 is a documented repressor of antigen-presentation machinery (MHC-I, β2M, components of the antigen-processing pathway) in multiple cold tumors. EZH2i can **de-repress MHC-I and prime "cold" tumors for T-cell recognition.** This is the strongest CIC-DUX4-relevant rationale for EZH2i — **not as a cytotoxic single agent but as an immune primer.** Tier: **Mechanistic** for CIC-DUX4 (the MHC-I/PRC2 link is established in other tumors; direct CIC-DUX4 evidence is thin — docs/02 immune-marker note).

### (c) What could have been tried DIFFERENTLY?
- **Reposition EZH2i from "cytotoxic monotherapy" to "MHC-I priming agent"** in a deliberate V3→V4 sequence: EZH2i (or EZH2i + HDACi) to restore MHC-I/β2M, *then* checkpoint blockade or NK/T-cell therapy. This is the single most defensible EZH2i redesign for CIC-DUX4.
- **Biomarker-select before treating:** measure baseline H3K27me3 occupancy at differentiation/antigen-presentation loci and baseline MHC-I; treat the PRC2-high, MHC-I-low subset, not unselected patients. The absence of this selection is a likely reason any past basket exposure was uninformative.
- **EZH2i + HDACi combination** for additive chromatin reopening and stronger MHC-I induction (docs/05 3g).
- **Confirm the dependency first** with a CRISPR/shRNA EZH2-dropout screen in CIC-DUX4 models before any clinical move — see falsifiable experiment in Forward Hypotheses.

### (d) Resource / structural limitation?
**Yes.** Tazemetostat reached patients via an epithelioid-sarcoma indication, not a CIC-DUX4 program. CIC-DUX4 patients could only access it off-label or in baskets. No dedicated trial, no biomarker stratification, tiny n.

### (e) Did the molecule hit its target?
Tazemetostat is a **selective, on-target EZH2 catalytic inhibitor** with established target engagement (reduces global H3K27me3); it is approved. The CIC-DUX4 question is **not target engagement but target relevance** — does inhibiting EZH2 matter in a tumor that may not depend on PRC2? The MHC-I-priming angle is the route by which an on-target drug could still be useful even if the driver dependency is absent.

---

# CLASS 3 — CDK4/6 inhibitors → Vectors V1 / V3

**Mapping:** V1/V3 (downstream cell-cycle friction; the CCND2/CCND1–CDK4 → Rb axis is directly downstream of ETV4). Tier: **Established** (palbociclib/ribociclib/abemaciclib in HR+ breast cancer; jurisdictional labeling varies) [broadly known; not verified this run]; CIC-DUX4: **Mechanistic / Preclinical-Cell at best; no dedicated data.**

### (a) Why did it underperform?
The defining limitation is structural to the drug class: **CDK4/6 inhibitors are cytostatic, not cytotoxic.** They induce G1 arrest (senescence-like) but do not kill; on withdrawal, cycling resumes. As monotherapy in an aggressive, fast-proliferating sarcoma this buys time, not cures. Resistance is also well-mapped:
- **RB1 loss** — if Rb is gone, CDK4/6 inhibition is irrelevant (no substrate to keep hypophosphorylated). CIC-DUX4 frequently co-deletes CDKN2A; RB-pathway status matters and is not routinely characterized.
- **Cyclin E / CDK2 bypass (CCNE1 amplification)** — CCNE1 is a documented CIC-DUX4 downstream target (docs/02); high cyclin E–CDK2 phosphorylates Rb independently of CDK4/6, giving **intrinsic resistance baked into the CIC-DUX4 program itself.** This is a specific, mechanistic reason CDK4/6i monotherapy should be expected to underperform here.
- **p16/CDKN2A deletion** — paradoxically CDK4/6i can still work in CDKN2A-null tumors, but the loss of p16 control raises CDK4/6 activity that the drug must overcome.

### (b) What is mechanistically DIFFERENT?
In HR+ breast cancer, CDK4/6i works because ER drives cyclin D and the tumor is comparatively cyclin-E-low and Rb-intact, so the D–CDK4/6–Rb axis is genuinely rate-limiting and combining with endocrine therapy starves the upstream driver. In CIC-DUX4, the upstream driver (the fusion) **also drives CCNE1**, so the tumor has a **built-in CDK2 bypass** that breast cancer typically lacks at baseline. There is no "endocrine therapy" equivalent to starve the upstream driver — the fusion is constitutive.

### (c) What could have been tried DIFFERENTLY?
- **Pair CDK4/6i with something that supplies the missing death signal** — convert cytostasis to cytotoxicity. Candidates: (i) CDK4/6i + MEK/ERK inhibition (the V1 upstream-RAS arm) to deepen and sustain arrest; (ii) CDK4/6i + BETi (Class 1) to simultaneously throttle the transcriptional supply of cyclins and hold the cell-cycle gate shut; (iii) CDK4/6i as a **senescence inducer followed by a senolytic** (one-two punch: arrest, then clear the senescent cells). Tier: **Mechanistic/Preclinical** concepts; **Theoretical for CIC-DUX4.**
- **Co-target the CCNE1/CDK2 bypass** — emerging selective CDK2 inhibitors could close the bypass that the fusion opens. Tier: **Theoretical for CIC-DUX4** [no direct citation].
- **Biomarker-select for RB1-intact, CCNE1-low tumors** before treating — the population most likely to respond. Absence of this selection would dilute any signal to nothing in a basket.
- **Schedule:** continuous vs intermittent dosing to sustain arrest without permitting bypass re-entry.

### (d) Resource / structural limitation?
**Yes.** Sarcoma CDK4/6i trials exist but are small and mixed and not CIC-DUX4-specific; the rationale (CCND/CDK4 dependency) is sound but the disease is too rare for a powered, biomarker-stratified, combination CDK4/6i trial. The cytostatic-class problem also makes single-agent endpoints (ORR) look bad even when the drug is doing exactly what it does (arrest).

### (e) Did the molecule hit its target?
Yes — CDK4/6i reliably inhibit CDK4/6 and reduce Rb phosphorylation (established target engagement). The failure is **the wrong endpoint for a cytostatic and a built-in molecular bypass (cyclin E)**, not an off-target miss. "It hit the target and the target wasn't enough on its own" is the precise diagnosis.

---

# CLASS 4 — Checkpoint blockade → Vector V4

**Mapping:** V4. Tier: **Established** (PD-1/PD-L1 blockade in many cancers); sarcoma: **Clinical-Trial** (SARC028 and others) [SARC028 broadly known; exact ORR figures not verified this run]; CIC-DUX4: **no direct data.**

### (a) Why did it underperform?
SARC028 and the general sarcoma checkpoint experience showed **modest overall activity with subtype dependence** — better in UPS and dedifferentiated liposarcoma, poor in translocation-driven sarcomas [broadly known result; exact numbers not verified this run]. The reasons map cleanly onto CIC-DUX4 biology (docs/02, docs/05 V4):
- **Cold tumor / low TMB** — translocation-driven sarcomas have few somatic mutations, so few conventional neoantigens; checkpoint blockade releases a brake on a T-cell response that **barely exists.**
- **MHC-I-low** — even the one strong antigen (the fusion junction) is poorly presented if MHC-I/β2M are downregulated. Releasing PD-1 does nothing if the T-cell never sees a peptide.
- **Immunosuppressive microenvironment** — Tregs, MDSCs, TGF-β; few infiltrating CD8 T-cells to disinhibit.
- **Monotherapy against an unprimed system** — the canonical "checkpoint blockade works where there was a pre-existing response to unleash" logic; CIC-DUX4 has no such response to unleash.

### (b) What is mechanistically DIFFERENT vs melanoma/NSCLC?
Melanoma/NSCLC are **high-TMB, often T-cell-inflamed** tumors with pre-existing exhausted CD8 infiltrate — exactly the substrate PD-1 blockade needs. CIC-DUX4 is the opposite: **low-TMB, MHC-I-low, non-inflamed.** The single best antigen is a clonal fusion-junction neoantigen (docs/02) — but a great antigen presented poorly to absent T-cells is not actionable by checkpoint blockade alone. The failure is upstream of the checkpoint.

### (c) What could have been tried DIFFERENTLY? (priming and sequencing — the heart of the V4 redesign)
- **Epigenetic priming first (V3→V4).** EZH2i and/or HDACi to restore MHC-I/β2M and antigen-processing machinery, *then* checkpoint blockade. This is the most active idea in sarcoma immunotherapy and is the explicit V3→V4 bridge.
- **Radiation / abscopal priming.** Local radiotherapy (already part of sarcoma SOC) generates immunogenic cell death and antigen release; combining RT + checkpoint blockade aims to convert a cold tumor hot and to provoke abscopal responses at distant sites. Tier: **Clinical-Trial** (RT+IO broadly); **Theoretical for CIC-DUX4.**
- **NK-first logic.** Because CIC-DUX4 downregulates MHC-I to hide from T-cells, it becomes a **"missing-self" target for NK cells.** An NK-axis strategy (IL-15 superagonists, NK-cell engagers) attacks exactly the escape route that defeats the T-cell arm — and is *complementary* to checkpoint blockade rather than competing with it. Tier: **Mechanistic / Clinical-Trial** (NK agents broadly).
- **Active immunization to create the response checkpoint blockade can then unleash** — fusion-junction neoantigen vaccine (or mRNA neoantigen vaccine) → checkpoint blockade. Turns the junction's clonality and tumor-specificity into a usable target. Tier: **Theoretical/Preclinical for CIC-DUX4.**
- **Combination IO** (anti-PD-1 + anti-CTLA-4, or + TGF-β trap) rather than PD-1 monotherapy, to address Treg/TGF-β suppression.

### (d) Resource / structural limitation?
**Yes, and acutely.** CIC-DUX4 is too rare for a dedicated checkpoint trial; its patients were a handful of enrollees inside subtype-agnostic sarcoma baskets, where their (predictably poor) responses were averaged into a heterogeneous cohort. There has been **no biomarker-selected (MHC-I-stratified), priming-sequenced checkpoint trial in CIC-DUX4.** The "checkpoint blockade fails in sarcoma" conclusion is, for this subtype, **an artifact of basket design as much as biology.**

### (e) Did the molecule hit its target?
Yes — anti-PD-1/PD-L1 antibodies engage their targets and block the axis (established). The failure is **"unblocked a pathway that wasn't the limiting step."** The limiting steps in CIC-DUX4 are antigen presentation (MHC-I), T-cell priming, and the suppressive microenvironment — all upstream of PD-1. Right drug, wrong rate-limiting step, wrong (unprimed) context.

---

# CLASS 5 — The fusion itself as a target → Vector V3

**Mapping:** V3 (restore the break condition by acting on the compiled output / the activator itself). Tier: **Theoretical / Preclinical** throughout; **no clinical agent directly targets CIC-DUX4.**

This is the deepest counterfactual: almost nothing has been *tried* clinically against the fusion directly, so the forensic is less "why did it fail" and more "why has it not been attempted, and what is the most defensible way in." Reframed in the project's own language: **the fusion is a mis-deployed module that flipped a repressor's logic to an activator's — "fix the config / restore the original function," not just "throttle the misbehaving calls."**

### (a) Why has direct targeting underperformed / not been attempted?
- **"Undruggable" transcription factor problem.** CIC-DUX4 is an intracellular, structurally disordered-in-part transactivator with no enzymatic active site and no surface pocket — the classic hard-to-drug TF profile.
- **Delivery.** The cleanest direct approaches (ASO to the fusion junction, siRNA, CRISPR excision of the junction) all founder on **solid-tumor delivery**, which is unsolved (docs/05 3a/3b). LNP delivery is good to liver, aspirational to a soft-tissue sarcoma compartment.
- **No medicinal-chemistry campaign** has been mounted at scale against CIC-DUX4 specifically — again the rarity/resource problem.

### (b) What is mechanistically DIFFERENT (and exploitable) about CIC-DUX4?
- It is a **neomorphic ACTIVATOR built from two normal parts**: CIC's DNA-targeting HMG-box + DUX4's acidic transactivation domain. That modularity is a target surface: the **DUX4 transactivation domain** is the "gain-of-function" half and is in principle blockable (it recruits coactivators/Mediator/p300).
- It **finds the same addresses as wild-type CIC.** In principle, **restoring or supplementing wild-type CIC repressor function** at those loci could re-impose silencing in competition with the fusion — "reinstall the correct config." (Speculative; no construct exists.)
- **Condensate hypothesis (serious forward hypothesis, per mandate).** EWSR1-FLI1 in Ewing forms transcriptional condensates via the EWSR1 low-complexity/IDR domain (LLPS), concentrating BRD4/Mediator/Pol II at target super-enhancers; condensate disruption (e.g., 1,6-hexanediol in vitro, or aromatic-residue mutants) collapses the program. **CIC-DUX4's condensate behavior is uncharacterized** (docs/02). But DUX4's transactivation domain is acidic/aromatic-rich — a plausible LLPS-competent module — and BRD4-dependent super-enhancers are exactly the kind of compartment that depends on multivalent condensation. **If CIC-DUX4 operates through a transcriptional condensate, then condensate-disruption (small molecules that partition into and dissolve transcriptional condensates, or that block the specific multivalent interactions) becomes a fundamentally different mode of attack than blocking any single protein** — and it would explain why single-node inhibitors (BETi, etc.) only dent the program: you have to dissolve the compartment, not remove one component. Tier: **Theoretical**; this is a hypothesis, explicitly flagged, with a concrete falsification test below.

### (c) What could be tried DIFFERENTLY?
- **CIC-DUX4-junction ASO / siRNA** with a delivery system designed for the sarcoma compartment (the gating problem is delivery, not target validity). Junction-specific sequence gives exquisite tumor selectivity. Tier: **Preclinical/Theoretical.** (~5% atypical-case flag: fusion-negative clinically-CIC tumors would have no junction to target — ASO/siRNA are strictly fusion-confirmed-only.)
- **CIC-DUX4 PROTAC / molecular-glue degrader** — degrade the fusion protein rather than inhibit it; converts an "undruggable TF" into a degradable substrate. No published CIC-DUX4 degrader exists. Tier: **Theoretical.**
- **DUX4-transactivation-domain blocker** — disrupt the coactivator (p300/Mediator) interface used by the DUX4 half; this would neutralize the gain-of-function without needing to remove the whole protein. Tier: **Theoretical.**
- **Condensate disruption** — see (b) and Forward Hypothesis FH-4.
- **Restore-the-repressor strategies** — re-express wild-type CIC or a CIC-mimetic dominant repressor at ETS loci to out-compete the fusion. Tier: **Theoretical**; delivery-limited.

### (d) Resource / structural limitation?
**Maximal.** This is the most under-resourced class precisely because it is the hardest and the disease is the rarest. There is no large-scale screen, no degrader campaign, no delivery program targeting CIC-DUX4. The absence of attempts is itself a finding: **direct fusion targeting has not "failed" — it has barely been tried.**

### (e) Did the molecule behave as envisioned?
N/A — there is no clinical molecule against the fusion. For the *preclinical tools* (junction ASO/siRNA in cell lines), knockdown of the fusion does collapse the ETS-target program in models [directionally established that fusion knockdown reduces ETV4/5 output; exact citation not verified this run], which **validates the fusion as the on-target node** — the gap is entirely delivery, not target validity.

---

# CLASS 6 — The antioxidant counterfactual → Vector V2 (with V1 overlap)

**Mapping:** V2 (reduce DSB frequency in at-risk neighbor cells). Tier: the *population trials* are **Established (as negative/harmful results)**; the *targeted redox-context use* is **Mechanistic/Theoretical.**

### (a) Why did the population trials "fail"?
- **ATBC** (β-carotene + α-tocopherol, Finnish male smokers) and **CARET** (β-carotene + retinyl palmitate, smokers/asbestos-exposed): β-carotene supplementation **increased lung cancer incidence/mortality** in smokers [broadly established; exact citation not verified this run].
- **SELECT** (selenium + vitamin E): vitamin E supplementation was associated with **increased prostate cancer incidence** [broadly established; exact citation not verified this run].
The forensic reasons these "failed":
- **Wrong population (no deficiency to correct).** Supplementing replete people with megadose single antioxidants is not the same as correcting deficiency; benefit requires a deficit to fix.
- **Pro-oxidant/redox-context reversal.** In a pro-oxidant milieu (smoker's lung), high-dose β-carotene can become **pro-oxidant** and can blunt physiologic redox signaling (including apoptosis of damaged cells) — antioxidants can protect *pre-malignant* cells too. (Cf. Sayin et al. *Sci Transl Med* 2014, NAC/vitamin E accelerated melanoma metastasis in mice — docs/05 V2 note; exact citation not verified this run.)
- **Single-agent megadose vs whole-food matrix.** Epidemiology favoring fruit/veg intake does not transfer to isolated high-dose pills (docs/05 V2 caveat).
- **Wrong endpoint/timescale** for a prevention signal in already-high-risk people.

### (b) Does this even transfer to a targeted, biomarker-defined, redox-context-specific use?
**Largely no — and that is the key counterfactual.** The population-trial failure is a verdict on *unselected megadose single-antioxidant chemoprevention*, **not** on:
- **Correcting a documented deficiency** (zinc, selenium, vitamin D) in a deficient individual — a different intervention entirely.
- **Context-specific redox manipulation in the tumor**, where (paradoxically) **pro-oxidant** strategies, or pharmacologic IV ascorbate acting as a pro-oxidant (H₂O₂-generating, not antioxidant), are under study — the opposite of the population-trial intervention.
- **V2's actual target** (reducing DSB rate in at-risk *neighbor* cells via whole-food redox support), which is upstream prevention, not the tumor-directed megadose tested in ATBC/CARET/SELECT.
The honest synthesis: the population trials correctly killed "give everyone high-dose single antioxidants." They say **little** about deficiency correction or about biomarker-selected, redox-context-specific use — those are different hypotheses that were never the trials' subject.

### (c) What could have been tried DIFFERENTLY?
- **Deficiency-stratified design** — enroll only the deficient; measure repletion; the benefit hypothesis only applies there.
- **Redox-context measurement** — stratify by baseline oxidative-stress markers and tumor redox state instead of treating redox as uniform.
- **Whole-food / mixed-tocopherol arms** rather than single high-dose synthetic isomers (SELECT used α-tocopherol alone; mixed tocopherols/tocotrienols behave differently).
- **Direction-aware design** — recognize that the therapeutic move in established tumor may be *pro-oxidant*, not antioxidant.

### (d) Resource / structural limitation?
These were large, well-powered, expensive trials — **not** underpowered. Their limitation was **conceptual (wrong hypothesis/population/endpoint), not resource.** This is the one class where "they had the resources and the design choice was the problem" is the correct read.

### (e) Did the molecule behave as envisioned?
**No — it inverted.** β-carotene/vitamin E were envisioned as protective antioxidants; in the pro-oxidant smoker lung and in replete prostate they behaved as net-harmful (pro-oxidant / pro-survival-of-damaged-cells). The molecule reached its "target" (raised serum levels) but the *biological consequence was opposite to the design intent* — a textbook "hit the target, wrong context, wrong sign" outcome.

> **`sarcoma-chemo-interactions` screening for the redox class (V2 candidates that touch SOC):**
> **High-dose vitamin C / E / NAC (supplement-level)** — CYP3A4: not the main concern | P-gp: not main concern | **ROS-axis: YES — the canonical concern; doxorubicin and ifosfamide mechanisms include ROS generation, and high-dose antioxidant supplementation may theoretically antagonize them; oncology guidance generally advises against high-dose antioxidant supplementation DURING cytotoxic chemo** | Other: NAC accelerated metastasis in mouse melanoma (Sayin 2014, docs/05; exact citation not verified this run) | Citation: docs/05 V2/SOC sections; primary citations not re-verified this run. **Whole-food dietary intake is treated differently from supplement megadose — say which one.**

---

# CROSS-CUTTING — Why CIC-DUX4 research is structurally stuck

1. **Rarity.** A few hundred reported cases globally (docs/02). A powered randomized trial in a single rare subtype is essentially impossible; patients reach drugs only through subtype-agnostic baskets, where their results are diluted and uninterpretable.
2. **No predictive biomarker beyond fusion presence.** There is no validated marker that says "this CIC-DUX4 tumor will respond to BETi / EZH2i / CDK4/6i / checkpoint blockade." Without a biomarker you cannot enrich, so every basket signal is noise. (And ~5% of clinically/histologically CIC-like tumors are fusion-negative — docs/02 — further muddying any unselected cohort.)
3. **No dedicated trial ever run.** Every clinical inference about CIC-DUX4 is transferred from Ewing or from mixed sarcoma cohorts. "It didn't work in CIC-DUX4" almost always means "it didn't work in a basket that happened to contain one or two CIC-DUX4 patients."
4. **Cell-line / model scarcity.** Few public CIC-DUX4 cell lines and PDX models → preclinical pharmacology is thin, mechanistic claims (PRC2 dependency, condensate behavior, MHC-I dynamics) are under-tested, and combination screens are rarely run in genuine CIC-DUX4 backgrounds.
5. **Consequence:** the literature *looks* like a list of failures, but most "failures" are **underpowered, unselected, monotherapy, wrong-endpoint** exposures — i.e., the field has mostly tested the *easy, wrong* versions of each idea. The forward-simulation mandate is exactly right: **current knowledge is the floor, not the ceiling**, because the ceiling-tests have not been done.

---

# FORWARD HYPOTHESES — Redesigned trials

Each: the redesign · the mechanistic bet · the predicted outcome · the biomarker/endpoint · what would falsify it. All tiers **Theoretical/Mechanistic for CIC-DUX4** unless noted. No PMIDs/NCTs invented.

### [Forward Hypothesis FH-1] BET-PROTAC + CDK4/6 inhibitor, biomarker-selected (V1/V3)
- **Redesign:** Replace reversible BETi with a BRD4 **degrader**, combined with a CDK4/6 inhibitor, in RB1-intact / CCNE1-low CIC-DUX4 tumors.
- **Mechanistic bet:** Degradation defeats BRD4 reaccumulation (the reason monotherapy BETi is transient); CDK4/6i converts the transcriptional throttling into durable cell-cycle exit; pre-selecting RB1-intact/CCNE1-low excludes the built-in cyclin-E bypass that dooms CDK4/6i alone.
- **Predicted outcome:** Deeper, more durable suppression of the ETV4→CCND→Rb axis than either agent alone; conversion of cytostasis toward senescence/death.
- **Biomarker/endpoint:** Baseline RB1 intact + low CCNE1; pharmacodynamic readout = ETV4/ETV5 mRNA suppression and Rb-phosphorylation drop; efficacy endpoint = depth/duration of response, not just ORR.
- **Falsifies it:** ETV4/5 output rebounds despite sustained BRD4 degradation (program is BRD4-independent), OR responses are no better than BETi alone, OR CCNE1 re-amplifies and restores Rb phosphorylation under therapy.

### [Forward Hypothesis FH-2] EZH2i (±HDACi) as an MHC-I priming agent → checkpoint/NK, sequenced (V3→V4)
- **Redesign:** Use EZH2i not as cytotoxic monotherapy but as a **2–4 week immune-priming lead-in** to restore MHC-I/β2M, then add checkpoint blockade and/or an NK-axis agent; enroll MHC-I-low, PRC2-high tumors only.
- **Mechanistic bet:** CIC-DUX4 is cold because of MHC-I downregulation, not because the antigen (fusion junction) is absent. PRC2/EZH2 represses antigen-presentation machinery; relieving it makes the clonal junction-neoantigen visible, giving checkpoint blockade a response to unleash; MHC-I-low escapers are caught by NK "missing-self."
- **Predicted outcome:** MHC-I/β2M rises on tumor cells during the lead-in; T-cell infiltration increases; the EZH2i-primed cohort responds to checkpoint blockade where unprimed CIC-DUX4 did not.
- **Biomarker/endpoint:** Paired biopsy MHC-I/β2M and CD8 infiltration pre/post lead-in (pharmacodynamic primary); junction-neoantigen-specific T-cell expansion; then RECIST.
- **Falsifies it:** MHC-I fails to rise with EZH2i in CIC-DUX4 (PRC2 not the relevant repressor here), OR MHC-I rises but no T-cell response/clinical benefit follows (the antigen is not being presented or the microenvironment dominates).

### [Forward Hypothesis FH-3] NK-first immunotherapy exploiting MHC-I-low escape (V4)
- **Redesign:** Lead with an **NK-axis agent (IL-15 superagonist or NK-cell engager)** rather than a T-cell checkpoint, precisely because CIC-DUX4 downregulates MHC-I.
- **Mechanistic bet:** The same MHC-I downregulation that defeats the T-cell arm makes the tumor a **"missing-self" NK target**; attacking via NK turns the tumor's main T-cell-evasion mechanism into a liability — complementary to, not competing with, any later T-cell priming.
- **Predicted outcome:** NK-mediated cytotoxicity correlates inversely with tumor MHC-I; activity in exactly the MHC-I-low subset that checkpoint blockade cannot help.
- **Biomarker/endpoint:** Baseline MHC-I-low status; NK infiltration/activation markers; endpoint = response enriched in the MHC-I-low stratum.
- **Falsifies it:** MHC-I-low CIC-DUX4 cells upregulate NK-inhibitory ligands (e.g., HLA-E, or low NKG2D-ligand expression) and resist NK killing despite missing classical MHC-I.

### [Forward Hypothesis FH-4] Transcriptional-condensate disruption as a distinct mode of attack (V3, fusion-directed)
- **Redesign:** Test whether CIC-DUX4 organizes its super-enhancer program into a **transcriptional condensate** (as EWSR1-FLI1 does), then attack the condensate rather than any single protein — first as proof-of-mechanism in CIC-DUX4 models, only later as a therapeutic concept.
- **Mechanistic bet:** Single-node inhibitors (BETi) only dent the program because the program lives in a multivalent condensate that re-forms; the DUX4 acidic/aromatic transactivation domain is LLPS-plausible; dissolving the compartment (or blocking the specific multivalent interactions) collapses the whole ETS-target output at once.
- **Predicted outcome:** CIC-DUX4 forms nuclear puncta co-localizing with BRD4/Mediator/Pol II at ETV4/5 super-enhancers; condensate perturbation (e.g., aromatic-residue mutants, or transcriptional-condensate-partitioning small molecules) collapses ETV4/5 output more completely and durably than BETi.
- **Biomarker/endpoint:** Imaging of CIC-DUX4 puncta and their dissolution; ETV4/5 transcriptional collapse as the pharmacodynamic readout.
- **Falsifies it:** CIC-DUX4 shows **no** condensate behavior / diffuse nuclear distribution and its target output is unaffected by condensate-disrupting conditions — i.e., the Ewing analogy does not transfer and the program is not condensate-dependent.

### [Forward Hypothesis FH-5] CIC-DUX4-junction ASO/degrader with a delivery system as the primary variable (V3, fusion-directed)
- **Redesign:** Treat **delivery, not target choice, as the experiment.** Junction-specific ASO (or a fusion-degrading molecular glue) is the payload; the trial's central variable is a sarcoma-compartment delivery vehicle (intratumoral, conjugate, or next-gen LNP).
- **Mechanistic bet:** Preclinical fusion knockdown already collapses the ETS program (target validity is established in models); the entire gap is getting the agent into tumor cells. Junction specificity gives near-perfect tumor selectivity and spares normal CIC.
- **Predicted outcome:** Where delivery is achieved (e.g., accessible/intratumoral lesions), ETV4/5 output and proliferation fall sharply and selectively.
- **Biomarker/endpoint:** Intratumoral fusion-transcript knockdown (RT-qPCR on paired biopsy) as primary PD; ETV4/5 suppression; fusion-confirmed patients only (does **not** apply to the ~5% fusion-negative atypical cases — flagged per contract).
- **Falsifies it:** Adequate intratumoral knockdown is achieved yet the tumor does not regress (the fusion is no longer the sole dependency once the program is epigenetically locked in), OR delivery remains below the knockdown threshold in all accessible lesions.

---

# What I could not establish

- **Any specific trial datum with a verified citation.** Web access was denied this run; I invented no PMIDs/NCTs and flagged every broadly-known trial fact as "exact citation not verified this run." The orchestrator must re-ground SARC028 results, tazemetostat label/EMA status, ATBC/CARET/SELECT specifics, and all preclinical CIC-DUX4 BETi/EZH2i references against live sources before any external use.
- **Whether a PRC2 dependency exists in CIC-DUX4 at all.** The EZH2i rationale rests on transfer from BAF-loss epithelioid sarcoma and on the PRC2→MHC-I link; neither is confirmed in CIC-DUX4. FH-2's falsification test is the way to settle it.
- **Whether CIC-DUX4 forms a transcriptional condensate.** This is the load-bearing unknown for FH-4 and is explicitly uncharacterized in docs/02. I treated it as a hypothesis, not a fact.
- **The actual RB1/CCNE1 status distribution in CIC-DUX4 cohorts.** CCNE1 is a documented downstream target (docs/02), but the frequency of RB1 loss and the real prevalence of the cyclin-E bypass are not something I could quantify without sources — FH-1's enrichment strategy assumes a meaningful RB1-intact subset exists.
- **Real MHC-I dynamics under EZH2i/HDACi in CIC-DUX4 specifically.** docs/02 calls the direct evidence "thinner" than in other fusion sarcomas; the V3→V4 bridge is mechanistically strong but CIC-DUX4-unproven.
- **Whether any of the redesigned combinations are tolerable.** This document reasons about mechanism and design, not safety/dosing; combination toxicity (e.g., BET-PROTAC + CDK4/6i myelosuppression) is unaddressed by design and out of scope.
- **Delivery feasibility for FH-5.** The entire premise is that delivery is the unsolved variable; I could not establish that any current vehicle reaches the soft-tissue sarcoma compartment adequately.

---

## Self-audit (sarcoma-pre-output-check)

8 failure modes:
1. **Citation fabrication** — None. Web denied; all trial/paper references explicitly flagged "exact citation not verified this run" or "no direct citation." No PMIDs/NCTs invented.
2. **Concentration mismatch** — N/A (no dietary-dose mechanism claims requiring achievable concentrations are made as positives; the only dietary class, antioxidants, is discussed as a counterfactual with the whole-food-vs-megadose distinction stated).
3. **Dose invention** — None. No human doses given anywhere.
4. **Analogy-as-evidence** — Engineering analogy ("fix the config," "mis-deployed module") is used as shorthand and immediately restated in molecular terms each time (neomorphic activator; HMG-box + DUX4 transactivation domain; PRC2/MHC-I; RB/E2F/cyclin E).
5. **Over-claiming from cell-line/transfer data** — Explicitly flagged: BETi/EZH2i/CDK4/6i/checkpoint conclusions are transferred from Ewing/other tumors, not CIC-DUX4-proven; said so in every class.
6. **Contraindication / SOC interaction ignored** — Addressed: antioxidant class screened against VDC/IE ROS-axis via `sarcoma-chemo-interactions`; combination-toxicity gaps noted in "What I could not establish."
7. **Tier on every claim** — Each class carries a tier; forward hypotheses tagged Theoretical/Mechanistic.
8. **Wrong/over-broad scope** — Stayed a supplementary team; did not create a fifth vector; mapped everything to V1/V3/V4; did not produce a treatment plan or per-patient advice.

8 mandatory-include items: one-line summary ✓ · confidence line ✓ · per-class evidence tier ✓ · per-class molecular mechanism ✓ · "evidence in CIC-DUX4 specifically?" (stated per class — almost always none direct) ✓ · "What I could not establish" ✓ · "Forward Hypotheses" (5, ≥2 required) ✓ · atypical ~5% fusion-negative note (flagged on FH-5 and the fusion-directed/ASO sections) ✓.

**Hard refusal rules honored:** no fabricated citations; no per-individual dosing; no modification of any clinical regimen; no invented gene-therapy constructs (only published-class concepts — ASO, PROTAC, NK engagers — discussed at Theoretical tier); no "natural = safe" framing (antioxidant harms in ATBC/CARET/SELECT/Sayin made central).
