# Transplanting the Individualized-Neoantigen-Therapy (INT) Concept to Sarcoma — an M5 Deep-Dive

**Tag: Clinical / Experimental — not naturally achievable; for awareness only.**
**Backed by `sims/11-vaccine-antigen-portfolio/` (Sim 11). Era-B artifact (ADR-0022). Not a fifth vector —
this is the M5 cell of the therapeutic-modality layer (ADR-0018), worked through V4's danger-signal /
immune-visibility biology (ADR-0006) and the MRD-window finding (ADR-0021).**

**One-line summary:** This output takes the *high-level concept* behind Merck/Moderna's intismeran autogene
(mRNA-4157 / V940) — individualized mRNA-encoded polyneoantigen vaccination — decomposes it into four
separable engineering pillars, tests quantitatively which pillars survive transplant into sarcoma
(Sim 11), and specifies the vaccine architecture that the model says *would* work; it deliberately
excludes the specific drug's dosing, its trial-participation logistics, any claim about this patient's
actual antigens (none were sequenced or predicted), and CAR/TCR cell-therapy design detail (M3 — named
only where it competes with M5 for the same antigen).

**Confidence: medium for the concept-level analysis, low-medium for the case-level design.** The pillar
decomposition and the TMB-supply argument rest on well-established, reproducible tumour-genomics facts and
survive an order-of-magnitude stress test; the case-level design rests on antigen-class parameters that
have **never been measured in CIC-rearranged or round-cell sarcoma** (the model's largest unmeasured
input), and every literature anchor in this session is `[VERIFY]` because literature egress was blocked.

> **Not medical advice. Not a diagnosis. Not a treatment or testing recommendation.** Research simulation
> and hypothesis generation only. Perishable regulatory/trial facts are tagged and **must be re-verified
> live** before any external use.

---

## 1. The concept, decomposed — what is actually being transplanted

Intismeran autogene is a *reference implementation*. The transferable concept has four separable pillars:

| Pillar | What it does | Mechanism (molecular, not analogical) | Tumour-agnostic? |
|---|---|---|---|
| **P1 Antigen source** | supplies the target list | tumour-vs-germline WES + RNA-seq → somatic non-synonymous variants → HLA-binding prediction → the encoded peptide set | **NO.** Throughput is set by tumour mutational burden. |
| **P2 Delivery + adjuvant** | gets antigen into DCs *and* supplies danger signal | LNP-delivered mRNA translated in APCs; the LNP/mRNA itself triggers innate sensing (endosomal TLR7/8, cytosolic RIG-I/MDA5) → type-I IFN → DC maturation | **Yes** |
| **P3 Polyepitope breadth** | makes escape require many simultaneous losses | up to ~34 epitopes in one construct `[VERIFY]`, spanning multiple HLA restrictions | **Yes** |
| **P4 Deployment context** | picks the moment and the partner | adjuvant/MRD setting (minimal burden, less suppressive TME) + PD-1 blockade to prevent re-exhaustion of primed T cells | **Yes** |

**Three of the four pillars are tumour-agnostic engineering. Exactly one — P1 — is a biological supply
chain, and it is the one that breaks in sarcoma.** That framing is the whole answer, and everything below
is the quantification of it.

- Tier: **Mechanistic** for the decomposition itself; the platform's clinical validation is
  **Clinical-Trial** (melanoma: KEYNOTE-942 / NCT03897881, with phase-3 NCT05933577 ongoing) `[VERIFY —
  perishable; recorded at this level in `v4-immune-watchdog/v3/neoantigen-vaccine.md`, re-verify live]`.
- Evidence in CIC-DUX4 / round-cell sarcoma specifically: **None direct.** No INT platform has enrolled a
  CIC-rearranged cohort.

---

## 2. The answer at two levels (they are different answers)

### 2a. "Is it applicable to sarcoma?" — sarcoma is not one disease, and the split runs straight through this question

The decisive axis is genomic architecture, and it splits sarcoma into two halves with **opposite** vaccine
logic:

| | **Complex-karyotype sarcomas** (UPS, myxofibrosarcoma, dedifferentiated liposarcoma, angiosarcoma, LMS) | **Translocation-driven sarcomas** (Ewing, synovial, CIC-rearranged, BCOR-altered, alveolar RMS) |
|---|---|---|
| Mutational burden | higher; aneuploid, chromothriptic, some UV/APOBEC signatures | **among the lowest of any human cancer** |
| Private neoantigens (P1 supply) | **present — the INT concept transfers close to as-designed** | **near-absent — P1 fails** |
| Public/shared antigens | fewer | **a defining fusion oncoprotein + frequent cancer-testis antigen expression** |
| Checkpoint-monotherapy signal | the responders in SARC028 (UPS/DDLPS) `[VERIFY]` | essentially none `[VERIFY]` |
| **Right vaccine architecture** | **individualized mutanome (the intismeran concept, transplanted directly)** | **public/shared-antigen construct — off-the-shelf, not individualized** |

> **Headline:** the intismeran *concept* is applicable to sarcoma — but to the **complex-karyotype half**.
> At the translocation-driven end, where this case sits, the concept must be **inverted**: melanoma needs
> personalization because its antigens are private; translocation sarcoma's best antigens are **public**,
> so the correct architecture is the off-the-shelf one. **Keep P2, P3, P4; replace P1.**

The existence proof that T cells *can* clear a low-TMB translocation sarcoma is already clinical:
MAGE-A4-directed TCR-T (afamitresgene autoleucel) and NY-ESO-1-directed TCR-T (letetresgene autoleucel)
in synovial sarcoma — a tumour with a translocation, low TMB, and a cold TME `[VERIFY — perishable
regulatory status; re-verify at Drugs@FDA/EMA per docs/09 before citing]`. **Low TMB is not the same as
"not immunologically attackable"; it is a statement about the *private* antigen supply only.**

- Tier: **Clinical-Trial / Established** for the synovial-sarcoma cell-therapy precedent `[VERIFY]`;
  **Mechanistic** for the transfer of that logic to CIC-rearranged/round-cell disease.
- Evidence in CIC-DUX4 specifically: **None direct.**

### 2b. "Would it work for *this* case?" — a different, harsher answer

This case is at the translocation-driven end (Era-B baseline: Ewing-like, driver-unresolved), **and** it
carries three additional constraints the general answer does not:

1. **No confirmed fusion** → the single best public antigen (the junction peptide) is **not a design input
   today** — a junction that exists but has not been sequenced cannot be encoded (golden rule #9;
   `CASE-BASELINE.md` §2).
2. **Driver unresolved** → antigen-class availability must be marginalised over the D1–D5 posterior, and
   the leading hypothesis (D4, 0.386) is the *lowest*-TMB branch of all.
3. **The chemo-responsive phenotype** means the bulk problem is being solved by chemotherapy; the unsolved
   problem is the persister reservoir, and the immunological opportunity is a **perishable post-chemo MRD
   window** (ADR-0021).

Sim 11's answer, stated plainly: **a vaccine is at best an adjunct here, not the backbone — and the literal
transplant is the worst option in the set.**

---

## 3. What Sim 11 actually computed

Full numbers, limitations and CSVs: `sims/11-vaccine-antigen-portfolio/RESULTS.md`.

**(a) Pillar P1 fails on supply by ~an order of magnitude.** Marginalised over the Era-B driver posterior,
the funnel `TMB → mutations → clonal → expressed → HLA-binder → immunogenic` yields a mean of **2.04
candidate epitopes**, with **P(filling a 34-slot construct) = 0.002** and **P(≥5) = 0.127**. The same funnel
run with melanoma TMB gives **57.3** candidates and P(fills 34) = 0.40 — a **28× supply difference**, and a
consistency check that the funnel reproduces the indication where the concept was validated without being
fitted to do so. **Stress test:** even with TMB wrong by **10×**, P(fills 34) reaches only 0.164.

**(b) The binding constraint is not antigen count.** Single-lever ablation of the best broad architecture:

| Lever removed | Utility change |
|---|---|
| the antigen-independent **NK arm** | **−89%** |
| deployment inside the **MRD window** | **−52%** |
| **halving the number of epitopes** | **−3.4%** |
| PD-1 blockade | −2.1% |

**The concept's signature engineering achievement — 34 antigens in one construct — optimises the axis that
matters least in this setting.** Timing and effector choice dominate breadth by more than an order of
magnitude.

**(c) Broad self-antigen constructs are net-negative once specificity risk is priced.** Adding the
lineage-programme and induced/de-repressed classes (modelled on-target/off-tumour risk 0.12 and 0.15,
anchored on the documented history of fatal cross-reactivity in shared-antigen T-cell therapy `[VERIFY]`)
costs more than the ~0.036 control probability they return. The **narrow, tumour-restricted** construct
(mutanome + junction + DUX4-as-CTA + cryptic ORFs, all specificity risk ≤0.07) matches the broad one at a
fraction of the risk.

**(d) Only one test changes the design decision.** Proper EVSI over five candidate tests: **long-read
WGS + RNA-seq (junction resolution) is the only one with non-zero value (+0.0035)**; the other four are
zero *for this decision* because the narrow construct wins in both branches. (They retain their value for
other questions — this does not override Sim 8 or ADR-0015.)

**(e) The flip test — what would have to be true for the vaccine to carry the response:**

| Scenario | Effective epitopes needed to match the NK arm |
|---|---|
| as modelled | **unreachable** |
| + MHC-I presentation fully restored | **unreachable** |
| + restored presentation **and** escape-proof antigens | **unreachable** |
| + all of the above **and** a mature delivery platform | **3.45** (reachable) |

**No single fix is sufficient; only the conjunction of all three makes a vaccine load-bearing.** That is the
falsifier for everything in §5.

---

## 4. The antigen-source catalog — what can be swapped into P1

Each class scored on the three axes. "Escape hazard" = probability the tumour can lose the class at no
fitness cost. Availability is conditioned on the Era-B driver posterior.

| # | Antigen class | Mechanism | Tier | Evidence in CIC-DUX4? | Escape hazard | Specificity risk | Feasibility |
|---|---|---|---|---|---|---|---|
| **A1** | Private somatic mutanome (SNV/indel) | mutated peptides presented on class I; no central tolerance | Clinical-Trial (melanoma platform) / **Theoretical here** | None direct; **low TMB in CIC is direct evidence against supply** (PMID 27664537) `[VERIFY]` | 0.70 (passengers are losable) | 0.03 | **F3** — platform exists, no route for this indication |
| **A2** | **Fusion-junction peptide (public neoantigen)** | the chimeric ORF creates a peptide absent from the normal proteome; loss is impossible without losing the driver | Preclinical-Cell / Theoretical | None direct | **0.06 — the lowest** | 0.01 | **F5 today → F3 if the junction is resolved** |
| **A3** | Cancer-testis antigens (PRAME, NY-ESO-1/CTAG1B, MAGE-A4, XAGE1) | germline-restricted genes de-repressed in tumour; testis is MHC-I-low/immune-privileged, so off-tumour presentation is limited | Clinical-Trial *in other sarcoma subtypes* / **Theoretical in round-cell** | **None — expression in CIC/round-cell is unmeasured** | 0.42 | 0.06 | **F2** — off-the-shelf antigens, established in sarcoma cell therapy `[VERIFY]` |
| **A4** | Lineage/driver-programme antigens (STEAP1, CHM1/LECT1, GPR64/ADGRG2, LIPI) | driver-transactivated surface/intracellular proteins; Ewing-associated | Preclinical-Animal / Clinical-Trial (Ewing cell therapy) `[VERIFY]` | None direct | 0.15 | **0.12 — on-target/off-tumour** | F3 |
| **A5** | Non-canonical / cryptic ORF & splice-derived antigens | fusion-driven transcriptional and splicing reprogramming generates unannotated ORFs and retained introns whose peptides reach class I | Preclinical-Cell / Mechanistic | None direct | 0.38 | 0.07 | **F4/F5** — needs immunopeptidomics |
| **A6** | Induced / de-repressed antigens (HERV, CTA) via EZH2i / DNMTi / HDACi | epigenetic de-repression of retroelements and germline genes ("viral mimicry") creates antigen *and* innate stimulus where the mutanome cannot | Preclinical-Cell / Mechanistic | None direct | 0.68 (drug-dependent) | **0.15** | F3 |
| **A7** | **DUX4 protein itself as a CT-like antigen** | DUX4 is a cleavage-stage/germline transcription factor silent in normal soma — if expressed, it is a bona fide tumour-restricted antigen | Theoretical | **Driver-contingent (D1/D2 only)** | 0.07 | 0.04 | F5 |

**A7 carries a mechanistic trap worth stating explicitly:** the same DUX4 protein that would supply the
antigen also **antagonises IFN-γ-induced MHC-I** `[VERIFY]` — the antigen and the block on its own
presentation arrive together. An A7-containing construct is therefore **strictly conditional on
co-administered presentation rescue**, and is doubly contingent (driver *and* priming).

**Atypical-case flag (golden rule #9):** A2 and A7 are **fusion-contingent** and do not apply to this case
as it currently stands. A1, A3, A4, A5, A6 and the entire P2/P3/P4 architecture are **fusion-agnostic** and
apply regardless of driver resolution.

---

## 5. The design the model actually endorses

If a vaccine is to be built for this disease, Sim 11 says it looks like this — and note that **three of the
five specifications are not about antigens at all**:

| # | Specification | Why (from Sim 11) |
|---|---|---|
| **S1** | **Public/shared antigen core, not an individualized mutanome** — CTA core (contingent on expression) + junction and/or DUX4 if the driver is resolved | P1 supply fails at 2.04 candidate epitopes; the public antigens are the ones this tumour class actually has |
| **S2** | **Narrow and tumour-restricted, not maximally broad** — cap specificity risk at ≤0.07/class; do not pad the construct with lineage or induced self-antigens | broad self-antigen inclusion is **net-negative**; halving breadth costs only 3.4% |
| **S3** | **Deployed inside the post-chemo MRD window** | losing the window costs **52%** — the single largest controllable lever |
| **S4** | **Paired with an antigen-independent effector arm (NK/IL-15 axis)** | the NK arm carries **89%** of modelled control and covers exactly the HLA-loss route that kills the T arm |
| **S5** | **Preceded by presentation rescue** (epigenetic MHC-I priming) **and** paired with PD-1 blockade | the flip test: a vaccine is load-bearing *only* with restored presentation **and** escape-proof antigens **and** a mature platform, together |

Keep P2 (mRNA-LNP delivery and its innate adjuvanticity) and P3's *format* (polyepitope) — **but spend the
slots on a handful of escape-resistant public antigens rather than on maximising count.** That is the
transplant that survives.

**Patient selection follows the same inversion.** In sarcoma, the reported predictor of checkpoint benefit
is the **immune microenvironment class — B-cell/tertiary-lymphoid-structure-rich tumours** — rather than
mutational burden `[VERIFY: Petitprez et al., Nature 2020, and the TLS-selected PEMBROSARC cohort; not
retrievable this session]`. A sarcoma vaccine program should select on **TLS/immune class, not TMB**.

---

## 6. The honest counterweight — when the vaccine is the wrong *format*

Two findings argue against M5 even after the redesign, and both must travel with §5:

1. **If a public antigen exists, adoptive cell therapy (M3) may beat vaccinating against the same
   antigen.** A vaccine must *prime* T cells through host APCs inside a cold, MHC-I-low TME — precisely
   the step this tumour class breaks. TCR-T delivers the effector pre-made and bypasses priming, and it is
   the approach with actual clinical validation in a low-TMB translocation sarcoma (synovial) `[VERIFY]`.
   **Same antigen, different modality, and the modality axis (ADR-0018) moves feasibility, not tier.**
2. **In this case the model's no-vaccine baseline was not beaten.** Everything bundled *around* the vaccine
   — priming, window timing, NK arm, PD-1 — scored 0.2700; the best vaccine-containing architectures scored
   0.2726 (in-situ) and 0.2696 (narrow). **The vaccine is within noise of the context that carries it.**

Stated without hedging: **Sim 11 does not find a vaccine that would work for this case as a primary
strategy.** It finds (i) that the concept transplants cleanly to a *different half of sarcoma*, (ii) the
specific architecture that would be least wrong here, and (iii) that the levers worth spending on in this
patient's situation are the window and the effector, not the antigen construct.

---

## 7. Forward Hypotheses

**[FH-11.1] The antigen-source inversion: translocation-driven sarcomas need *public*-antigen vaccines,
and personalization is actively counterproductive there.**
*Mechanistic basis:* private-mutanome supply scales with TMB and fails at ~2 candidate epitopes in this
class (Sim 11 Module A), while the same tumours carry a defining chimeric ORF and frequent germline-gene
de-repression — an antigen distribution that is the mirror image of melanoma's. Personalization also costs
6–9 weeks of manufacturing `[VERIFY]`, which in this disease consumes the MRD window that Module E1 shows
is worth 52%.
*Test:* run the real epitope pipeline both ways on a translocation-sarcoma cohort — WES/RNA-seq mutanome
prediction vs. a fixed public-antigen panel (junction + CTA + lineage) — and compare predicted-presented,
clonal, expressed epitope counts per patient, plus time-to-construct.
*Falsifier:* if the mutanome pipeline yields ≥5 high-quality clonal presented neoepitopes in a majority of
translocation-sarcoma patients, the inversion is wrong and the concept transplants directly.
*Why not yet tested:* INT programs enrol high-TMB indications by design, so the low-TMB tail has not been
run through the pipeline as a prospective comparison.

**[FH-11.2] The dual-purpose epigenetic node extends to antigen *supply*, not only antigen *presentation*.**
*Mechanistic basis:* the repo's PRC2/EZH2 node is already dual-purpose (SLFN11 maintenance → chemo-sensitivity;
MHC-I priming → visibility; ADR-0021, and Sim 2's real-data repositioning of EZH2i as priming rather than
cytotoxic). Viral-mimicry biology predicts a **third** effect on the same node: de-repression of HERV and
cancer-testis loci *creates* antigen in a tumour whose mutanome cannot. One intervention would then serve
V1/V3/V4 and the vaccine's antigen supply simultaneously.
*Test:* EZH2i / DNMTi / class-I HDACi exposure in Ewing and CIC-DUX4 lines (TE441T exists in the DepMap
registry) with paired RNA-seq (HERV + CTA loci), MHC-I flow cytometry, and — the decisive readout —
**immunopeptidomics** to confirm the induced transcripts actually reach the cell surface as presented
peptides.
*Falsifier:* transcript-level de-repression without a corresponding increase in presented peptides would
refute the antigen-supply arm while leaving the presentation arm intact.
*Caveat that must travel with it:* Sim 11 prices this class at the **highest specificity risk (0.15)** —
induced antigens are induced in normal tissue too, and the model finds the broad induced-antigen construct
net-negative. This hypothesis is about **mechanism**, and it is currently **outscored on the risk axis**.

**[FH-11.3] "Antigen-agnostic beats antigen-identified when the mutanome is empty."**
*Mechanistic basis:* in-situ vaccination (oncolytic virus, lysate/DC) lets the tumour supply its own
polyclonal antigen repertoire, sidestepping the identification step entirely — the only architecture in the
bake-off that beat the no-vaccine baseline (+0.003), despite being handicapped by ADR-0019's low
round-cell OV susceptibility and this patient's visceral lesions.
*Test:* the tropism/permissivity screen already named as the gating experiment in ADR-0019, extended with
an immunogenic-cell-death readout (calreticulin exposure, HMGB1/ATP release) in round-cell lines.
*Falsifier:* if round-cell lines are non-permissive across the platform panel, the arm collapses to its
adjuvant effect alone and the margin disappears.

---

## 8. What I could not establish

- **Whether this tumour expresses *any* cancer-testis or lineage antigen.** This is the model's largest
  unmeasured input and it gates the entire shared-antigen core (S1). CTA expression has never been
  characterised in CIC-rearranged or round-cell sarcoma to my knowledge, and I could not check.
- **This patient's actual antigens.** No sequencing, no HLA genotype, no epitope prediction was run.
  Sim 11's supply numbers are distributional statements about a tumour class, not about this tumour.
- **Any live regulatory or trial status.** `pubmed`, `clinicaltrials.gov`, `depmap.org`, NCBI FTP and
  `huggingface.co` all returned HTTP 403 through the proxy on 2026-08-19. Every citation here is
  **`[VERIFY]`**; the synovial-sarcoma TCR-T approvals, the KEYNOTE-942/NCT05933577 status, and the
  BNT122 colorectal futility signal recorded in the earlier neoantigen output are all **perishable** and
  were **not** re-checked this session.
- **The real-data upgrade that egress would have allowed:** DepMap/GEO expression of the A3/A4 antigen
  classes across Ewing/CIC lines, and GSE60740's antigen-presentation response to driver induction. Both
  are runnable the moment egress returns, and both would convert the weakest parameters in the model from
  judgement into measurement.
- **OpenMed NER grounding could not be run** (HuggingFace blocked). `entities.txt` is written;
  `grounding.tsv` is absent rather than fabricated.

### Red-team pass (ADR-0017)

1. **Load-bearing assumption:** that this tumour's TMB sits in the translocation-sarcoma low band
   (0.3–0.9 mut/Mb).
2. **Disconfirmation:** the strongest evidence *against* my pessimism is the synovial-sarcoma TCR-T
   precedent — a low-TMB translocation sarcoma where antigen-directed T cells produce real responses
   `[VERIFY]`. It does not rescue the mutanome pillar, but it does refute "low TMB ⇒ not immunologically
   attackable," and I have given it §2a rather than burying it. A second disconfirming point: TMB is a poor
   *within*-tumour-type predictor, so a class-level supply argument does not settle any individual case.
3. **Alternative outside this lane:** the binding constraint may be the TME/stroma rather than antigen at
   all — in which case neither M5 nor M3 is the answer and the target is the suppressive compartment. This
   fits the same data and is **not** what a vaccine-framed question surfaces. Flagged, not forced into M5.
4. **Flip test:** at TMB ×10 the conclusion survives (P(fills 34) = 0.164); at ×100 it would not. The
   conclusion is robust to an order-of-magnitude error, not to two. Entries A2/A7 are additionally tagged
   **driver-contingent**.
5. **Steer audit:** the question asked me to "find a vaccine that could work." The model's answer is that
   the best available vaccine architecture is *within noise of no vaccine* for this case, and §6 says so
   rather than delivering the requested artefact as though it had cleared the bar. The design in §5 is
   offered as the least-wrong construction, explicitly conditioned on the flip test in §3(e).

---

## 9. Standard-of-care interaction note

No dietary or supplement candidate is proposed here, so the `sarcoma-chemo-interactions` compound screen
does not apply. Two regimen-level interactions do:

- **Ifosfamide/VDC-IE cytotoxic chemotherapy is lymphodepleting.** That is simultaneously the *reason* the
  MRD window exists (homeostatic expansion, Treg trough, NK-first reconstitution — ADR-0021 §5) and a
  constraint on priming during active cycles. The window is a **transition**, not the cycles themselves.
- **Corticosteroids and other supportive-care immunosuppressants** blunt vaccine priming and checkpoint
  activity — a scheduling interaction, stated as a mechanism, with **no timing or dosing guidance given
  here**; that is a clinical decision outside this repository's scope.

---

*Sim 11 · Era-B artifact (ADR-0022) · forward lane only, gated out of protocol promotion by ADR-0020
(all citations `[VERIFY]`). Not a fifth vector — the M5 cell of ADR-0018. Research simulation and
hypothesis generation only: not medical advice, not a diagnosis, not a treatment or testing recommendation.*
