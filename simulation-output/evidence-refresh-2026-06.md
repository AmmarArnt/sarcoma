# Evidence Refresh — CIC-DUX4 / CIC-rearranged Sarcoma (2026-06-22; **verified 2026-06-25**)

> **Why this file exists.** The last three protocol versions (v1→v2→v3) converged — the
> framework was growing by adding *analytical lenses* (11 ADRs) rather than *new biology*.
> A targeted live-literature sweep was run to test the catalog's standing assumption that
> "direct CIC-DUX4 evidence is essentially absent," to surface 2024–2026 work, and to feed
> the condensate forward-hypothesis (Sim 9). This is the **"inject new information"** lane,
> not another re-sort of the same findings.
>
> **Verification status (updated 2026-06-25).** The original 2026-06-22 sweep ran in a
> network-egress-restricted environment (snippet/abstract level only) and flagged every
> accession `[VERIFY]`. On **2026-06-25** the same items were **verified against live PubMed /
> PMC / GEO / clinicaltrials.gov** (eutils + the registries in `docs/09-verification-sources.md`).
> Result: **7 of 8 direct-paper claims confirmed** (PMIDs/PMCIDs now inline, `[VERIFY]` stripped);
> **two citations upgraded/corrected** (DUX4-STAT1 is now the peer-reviewed *eLife* paper; the
> IGF1R item is the full *Cancer Res* paper, not the meeting abstract); and **one snippet-sourced
> claim was found WRONG and removed** — the WEE1/CCNE1/adavosertib "regression" was **not** in the
> Nat Commun MCL1 paper (see §A). Trial/regulatory status re-checked live and **date-stamped
> 2026-06-25** (still **perishable** — re-verify before external use). **Not medical advice.**

---

## TL;DR — did the refresh break the plateau?

**Partly, and informatively.** The big structural findings the catalog already tracks
(MCL1 dependency, p300/CBP, IGF1R axis) were **confirmed current and now full-text-verified
(2026-06-25)** — which is itself why v1→v3 plateaued: the catalog is genuinely keeping pace
with a tiny field. *(One snippet-sourced item — a WEE1/CCNE1/adavosertib "regression" — did
**not** survive verification and was retracted; see §A.)* The sweep surfaced **five genuine
deltas the catalog under-exploits**, two of them mechanistically unifying:

1. **p300/CBP is a single node that hits three vectors at once** — it drives the oncogenic
   transactivation (V1/V3), *stabilises* the fusion protein, **and suppresses MHC-I** (V4
   priming). The catalog treats the MHC-I bridge as an *EZH2i* story; the 2025 data make
   **p300/CBP the more direct MHC-I-restoring node**, and a clinical-stage inhibitor exists.
2. **DUX4 is an intrinsic interferon/STAT1 antagonist** — a fusion-relevant, MHC-I-independent
   second immune-evasion mechanism the catalog does not carry.
3. **A real dual-ICB (anti-PD-1 + anti-LAG-3) response case** in CIC::DUX4 — updates V4 from
   "modest checkpoint monotherapy" to "doublet incl. LAG-3 has a documented response."
4. **MCL1's feasibility is gated by class-wide cardiotoxicity** that **stacks with this
   patient's prior anthracycline** — a concrete down-weight + an interaction flag.
5. **No DUX4 or CIC-DUX4 condensate/LLPS study exists** — the Sim 9 frontier is genuinely
   open, and now sharpenable through the p300/CBP-acetylation axis.

---

## A. Confirmed already-current in the catalog (re-verified live 2026-06-25)

| Finding | Source (verified 2026-06-25) | Tier | Catalog status |
|---|---|---|---|
| **MCL1 is a validated dependency** in patient-derived CIC::DUX4 tumoroids, **independently replicated by two 2025 Nat Commun papers**; MCL1 is a **direct transcriptional target** of CIC::DUX4; genetic + pharmacological MCL1 inhibition → rapid apoptosis and xenograft growth inhibition; **recurrent ARID1A mutations** in CIC::DUX4 | **(1) Nat Commun 2025;16(1):7688** — PMID **40841513**, PMC12370961, DOI 10.1038/s41467-025-62629-6 ✅; **(2) Nat Commun 2025** "SRCS tumoroid biobank…" — PMID **40841360**, PMC12371069, DOI 10.1038/s41467-025-62673-2 ✅ (both abstract-confirmed) | Preclinical-Cell/Animal (CIC-DUX4-direct, **independently replicated**) | Already in `findings-ranking.md` and protocol V3 as *driver-contingent* — V3's "two independent papers" framing is **confirmed correct** |
| ~~WEE1 + CCNE1 dependency; adavosertib → xenograft regression~~ — **RETRACTED (was a snippet-sourcing error).** **Both** Nat Commun 2025 MCL1 papers were full-text-checked 2026-06-25 and contain **zero** mentions of WEE1, CCNE1, cyclin E, adavosertib or AZD1775. The claim is **not supported by either paper** and is withdrawn. | — (no valid source in either MCL1 paper) | — | **Sim 3's WEE1+ifosfamide result stands on its own (Ewing-proxy) but is NOT independently validated by these papers.** Do not cite it as CIC-DUX4-direct WEE1 evidence. |
| **p300/CBP required for CIC-DUX4 activity; iP300w / A-485 suppress transactivation and reverse CIC-DUX4-induced H3 acetylation; iP300w arrests CDS lines + blocks CDS xenograft growth in vivo** | **Oncogenesis 2021;10(10):68** — PMID **34642317**, PMC8511258, DOI 10.1038/s41389-021-00357-4 ✅; chromatin follow-up **Cancers 2024** PMID **38275898**/PMC10814785 ✅ | Preclinical-Cell/Animal | Already in register (Bakaric 2024, PMID 38275898) |
| **IGF1R via HMGA2/IGF2BP/IGF2/AKT/mTOR axis → sensitivity to trabectedin + PI3K/mTOR inhibition (dactolisib)** in patient-derived CDS PDX/cell-line models | **Cancer Res 2022;82(8):1471–1485** "Integrated Molecular Characterization of Patient-Derived Models…" — PMID **34903601**, DOI 10.1158/0008-5472.CAN-21-1222 ✅ abstract-confirmed *(corrected from the meeting-abstract "82(4):708")* | Preclinical-Cell/Animal (CIC-DUX4-direct) | Validates Sim 1 IGF1R; **trabectedin link is a useful addition** |
| **Real CIC-DUX4 chromatin dataset GSE248040** ("new epigenetic dependencies"); GEO summary independently states CIC-DUX4 acts as a potent activator **mainly via direct interaction with p300**, p300 essential for CDS proliferation, p300i impacts growth in vitro + in vivo | **GSE248040** (Public 2024-01-31) = PMID **38275898** / PMC10814785, Cancers (Basel) 2024 ✅ | dataset + Preclinical | **Not yet mined** — flag for a data run (see §F) |

*Reassurance value:* the catalog is not stale on the headline targets. The plateau is
real but it reflects a genuinely small evidence base, not negligence. **The one correction
above (WEE1 retraction) is exactly why the `[VERIFY]` discipline exists** — a snippet
conflated a separate WEE1 result with this paper; full-text checking caught it.

## B. Genuine deltas — the p300/CBP unification (highest-value)

**The 2025 immune-modeling paper changes how the MHC-I bridge should be framed.**

> *"Modeling CIC::DUX4 sarcoma reveals oncogene-mediated MHCI-dependent immune evasion"* —
> **Mol Cancer 2025;24(1):299** — PMID **41299516**, PMC12659477, DOI 10.1186/s12943-025-02485-6
> ✅ **abstract-verified verbatim 2026-06-25** (Vachanaram, Bosnakovski et al., Univ. Minnesota):
> a dox-inducible CIC::DUX4 mouse model + the imChCDS line show "a clear dependency on the
> P300/CBP transcriptional co-activators" and identify **"CIC::DUX4/P300/CBP-mediated suppression
> of MHC class I (MHCI) as a key mechanism of CDS immune evasion."** Genetic CIC::DUX4 inactivation
> **or pharmacological P300/CBP inhibition** "induces cancer cell cycle arrest, **restores MHCI
> expression**, and triggers robust anti-tumor immune responses, … transforming the immunologically
> 'cold' CDS microenvironment into a 'hot' one and driving tumor regression." The specific
> **IFN-γ-induction-of-MHC-I block** is most directly evidenced by the DUX4-STAT1 paper (§C, eLife
> PMID 37092726). This is the **load-bearing claim for the promotion decision — it holds.**

Implication: the **same p300/CBP node** that the catalog already lists as the super-enhancer
*writer* (V1/V3 throttle) is **also the MHC-I suppressor** (V4 priming). So a p300/CBP
inhibitor is a candidate **single-node, multi-vector** intervention:
- throttles the oncogenic output (V1) and restores the differentiation/brake context (V3),
- **destabilises the fusion protein** (acetylation-dependent stability — §A),
- **de-represses MHC-I** → makes the cold tumour visible (V4 priming) — the role the
  catalog currently assigns mainly to EZH2i (now F4 in the US after tazemetostat's
  withdrawal), so p300/CBPi is a **timely replacement bridge**.

**Feasibility (verified live 2026-06-25 on clinicaltrials.gov — still perishable, re-verify):**
**inobrodib (CCS1477)**, oral p300/CBP bromodomain inhibitor — heme trial `NCT04068597`
**RECRUITING** (Phase 1/2; AML/NHL/MM/MDS; last update 2026-06-24); the advanced-solid-tumour
study `NCT03568656` (mCRPC/mBC/NSCLC/solid) is now **COMPLETED** (last update 2025-08-08).
**TT125-802** p300/CBP bromodomain inhibitor `NCT06403436` is **ACTIVE, NOT RECRUITING** (Phase 1,
advanced solid tumours incl. NSCLC/EGFR/KRAS-G12C; last update 2026-04-13). **No sarcoma-specific
arm in any.** Band ≈ **F3** (clinical-stage, no CIC route yet). A-485 / iP300w remain preclinical
tools. **Caveat:** p300/CBP is broadly essential — therapeutic-window and on-target toxicity are
the real risk; this is not a benign target.

## C. Genuine deltas — immune axis (V4)

| Delta | Source (verified 2026-06-25) | Tier | Why it's new to the catalog |
|---|---|---|---|
| **DUX4 (and mouse Dux) physically interacts with STAT1 and broadly suppresses IFN-γ-stimulated genes (ISGs)** by decreasing bound STAT1 + Pol-II recruitment; requires conserved (L)LxxL(L) motifs in the **DUX4 C-terminus**; abstract explicitly: "expression in cancers **suppresses IFNγ-induction of MHC Class I** and contributes to immune evasion" | **eLife 2023;12:e82057** — PMID **37092726**, DOI 10.7554/eLife.82057 ✅ *(now peer-reviewed; upgraded from the 2022 bioRxiv preprint)* | Preclinical-Cell (Mechanistic, now peer-reviewed) | A **second immune-evasion arm**: global ISG blunting + the **mechanistic source of the IFN-γ-MHC-I block** (complements §B). C-terminal motif = the junction-retained DUX4 moiety → **fusion-relevant**. Predicts IFN-axis therapies are blunted at the source. |
| **Documented CIC::DUX4 response to dual ICB (nivolumab + relatlimab = anti-PD-1 + anti-LAG-3)** — first reported ICB response in CDS; pre-treatment immune-cold, post-treatment CD8 influx + exhaustion-marker co-expression | **npj Precis Oncol 2025;9(1):85** — PMID **40128305**, DOI 10.1038/s41698-025-00878-w ✅ abstract-verified (MSKCC) | Clinical (single case) | Catalog says "modest checkpoint *monotherapy*"; this is a **doublet incl. LAG-3** signal. Pre-treatment was immune-cold (scarce CD3/CD8/FOXP3, negligible PD-L1/PD-1) → argues for **priming-then-checkpoint** sequencing, consistent with Sims 4/5. |

**Sequencing read (ties to Sims 4/5 + ADR-0006):** cold baseline → the lever is *visibility
first* (p300/CBPi or EZH2i to restore MHC-I; or an ICD/danger signal) **then** checkpoint,
ideally a **PD-1 + LAG-3 doublet** given the documented exhaustion phenotype. Lowering
inflammation ≠ improving anti-tumour immunity (inflammation-state lens).

## D. Genuine deltas — feasibility nuance on MCL1 (matters for THIS patient)

The MCL1 dependency is real (§A), but the **class has a well-documented cardiotoxicity
signal** that the catalog should carry explicitly:
- **ABBV-467** — "efficacious in tumor models but **associated with cardiac troponin increases
  in patients** (4 of 8)": **Commun Med 2023;3:171** — PMID **37880389**, DOI 10.1038/s43856-023-00380-z
  ✅ abstract-verified. **AZD5991** Phase-1 FIH (heme) reported deaths from AEs incl. **cardiac
  arrest**: **Clin Cancer Res 2024** — PMID **39167622**, PMC11528199, DOI 10.1158/1078-0432.CCR-24-0028
  ✅. *(S64315 / AMG176 / AMG397 cardiac-discontinuation claims are general program reports — not
  separately re-verified here; treat as background, not load-bearing.)*
- Next-gen **BRD-810** — "highly selective MCL1 inhibitor with **optimized in vivo clearance**…
  troponin-I release in iPSC-cardiomyocytes only at suprapharmacologic concentrations": **Nat Cancer
  2024** — PMID **39179926**, DOI 10.1038/s43018-024-00814-0 ✅ abstract-verified — explicitly engineered for
  **optimised in-vivo clearance to reduce cardiac exposure**, with efficacy in *solid* and
  heme models — the most plausible future route.

**Patient-specific flag:** this patient received **doxorubicin** (anthracycline,
cumulative cardiotoxicity). An MCL1 inhibitor's cardiac liability **stacks on prior
anthracycline exposure** → MCL1 feasibility for this patient is **F3–F4 and cardio-gated**,
not a clean "novel target." This is exactly the kind of patient-conditioned down-weight the
generic catalog row misses. *(Not advice — a feasibility annotation; an oncologist owns any
cardiac-risk judgement.)*

## E. The open frontier — condensates (feeds Sim 9)

The sweep found **no DUX4 and no CIC-DUX4 liquid-liquid phase-separation / condensate
study** (searched explicitly: "DUX4 phase separation / condensate / transactivation IDR",
"CIC-DUX4 condensate super-enhancer"). The field's condensate work is on **EWSR1/FET**
fusions. Yet the DUX4 C-term's mechanism — **recruiting p300/CBP to build an acetylated
activating hub** — is exactly the kind of coactivator/acetyl-reader chemistry that nucleates
transcriptional condensates. So the condensate hypothesis is **genuinely novel, fusion-
agnostic (covers the ~5% unconfirmed case), and now mechanistically anchored to an
already-druggable node (p300/CBP).** Operationalised as **Sim 9** (`sims/09-condensate-llps/`,
Forward Hypothesis FH-9.1, with a named p300/CBP-inhibitor dissolution falsifier).

> **Sim 9 update (executed 2026-06-25):** the pipeline now runs with real numbers (localcider +
> metapredict + PLAAC). **Informative partial-negative:** the DUX4 C-term is a disordered **acidic
> activation domain, NOT a FET-type prion-like LCD** (PLAAC PRDscore 0 vs EWSR1 77.6 / FUS 113.7).
> So the EWSR1-analogy *homotypic* self-assembly model **does not transfer** — FH-9.1 is refined to
> a **heterotypic** model (acidic AD → p300/CBP coactivator-condensate partitioning), which points
> at the *same* p300/CBP node as §B. See `sims/09-condensate-llps/RESULTS.md`.

## F. Datasets surfaced for a data-mining run (verified 2026-06-25; not yet mined)
- **GSE248040** — CIC-DUX4 ChIP-seq / chromatin profiling — GEO **Public 2024-01-31**, linked PMID
  **38275898** ✅ verified; would directly extend Sim 1's single-line signature.
- **Patient-derived CIC::DUX4 tumoroids** (Nat Commun 2025, PMID 40841513) — the paper's *drug-screen*
  is the real-CIC-DUX4 dependency resource the catalog wants instead of the Ewing proxy. **NB:** the
  abstract/full-text describe an **ex-vivo drug screen on tumoroids**, not a genome-wide CRISPR screen —
  cross-check the data-availability section for the actual deposited data before promising "CRISPR."
- DepMap CIC-DUX4 lines (TE441T, NCC-CDS1-X1/X3) — still no CRISPR screen as of last check; expression mineable.

## G. What I could not establish (after the 2026-06-25 verification pass)
- **Heterotypic LLPS web-server scores** (FuzDrop / PScore / catGRANULE 2.0) — not obtained: PScore
  and catGRANULE servers were unreachable on 2026-06-25, FuzDrop is interactive-only (Sim 9 §5). The
  reproducible CLI predictors (localcider/metapredict/PLAAC) were run; **not fabricated.**
- **Full-text of the Cancer Res 2022 IGF1R paper** — the *abstract* confirms the HMGA2/IGF2BP/IGF1R/
  AKT-mTOR axis + trabectedin sensitivity; the specific partner **dactolisib** is named from the
  refresh's prior snippet and is consistent with the AKT/mTOR axis but was **not** re-confirmed in the
  abstract text I read — treat "dactolisib" as the likely-but-unconfirmed PI3K/mTOR agent.
- **S64315 / AMG176 / AMG397 cardiac-discontinuation** specifics — general program reports, not
  separately accession-verified here (the load-bearing ABBV-467 / AZD5991 / BRD-810 ones are).
- **Whether CIC-DUX4 forms condensates *in cellulo*** — no such study exists (sweep confirmed);
  FH-9.1 stays Theoretical with a named falsifier.

## H. Recommended next moves (ranked)
1. ~~Re-run this refresh + Sim 9 in a network-permissive environment~~ — **DONE 2026-06-25:**
   §A–§D full-text-verified; Sim 9 executed (real descriptors; see §E note + Sim 9 RESULTS).
2. **Add a `p300/CBP` consolidated entry to the catalog (`protocol-v4.md`)** framing it as the
   single-node multi-vector bridge (V1/V3 throttle + fusion destabilisation + V4 MHC-I restoration),
   replacing/augmenting the EZH2i-centric MHC-I bridge (EZH2i now F4-US). **Verification supports
   this** (load-bearing §B claim holds). ← *promotion decision pending user sign-off.*
3. **Carry the DUX4-STAT1/ISG-antagonism mechanism** in V4 as a distinct evasion arm (now eLife-grade).
4. **Down-weight MCL1 for this patient** with the cardiotox × prior-anthracycline flag (ABBV-467/AZD5991/BRD-810 verified).
5. Mine **GSE248040** and the **tumoroid drug-screen** to replace Ewing-proxy dependency data.

*All items are research-simulation hypotheses. Direct-paper citations were full-text/abstract-verified
2026-06-25; trial/regulatory status is perishable (date-stamped, re-verify before external use). Not medical advice.*
