# Evidence Refresh — CIC-DUX4 / CIC-rearranged Sarcoma (2026-06-22)

> **Why this file exists.** The last three protocol versions (v1→v2→v3) converged — the
> framework was growing by adding *analytical lenses* (11 ADRs) rather than *new biology*.
> A targeted live-literature sweep was run to test the catalog's standing assumption that
> "direct CIC-DUX4 evidence is essentially absent," to surface 2024–2026 work, and to feed
> the condensate forward-hypothesis (Sim 9). This is the **"inject new information"** lane,
> not another re-sort of the same findings.
>
> **Sourcing honesty (read first).** This environment's network-egress allowlist blocked
> direct article retrieval (`WebFetch`, NCBI/EBI/PMC, UniProt all return 403); **only web
> *search* (snippet/abstract level) was available.** Every claim below is therefore sourced
> from **search snippets / abstracts, not full-text reading**, and every accession,
> PMID/NCT, and regulatory/trial status carries **[VERIFY]** — confirm against the source
> and the live registries in `docs/09-verification-sources.md` before any external use.
> Regulatory/trial status is **perishable**. **Not medical advice.**

---

## TL;DR — did the refresh break the plateau?

**Partly, and informatively.** The big structural findings the catalog already tracks
(MCL1 dependency, p300/CBP, WEE1/CCNE1, IGF1R) were **confirmed current** — which is itself
why v1→v3 plateaued: the catalog is genuinely keeping pace with a tiny field. But the sweep
surfaced **five genuine deltas the catalog under-exploits**, two of them mechanistically
unifying:

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

## A. Confirmed already-current in the catalog (no change, but re-verified)

| Finding | Source [VERIFY] | Tier | Catalog status |
|---|---|---|---|
| **MCL1 is a validated dependency** in patient-derived CIC::DUX4 tumoroids (drug-screen + CRISPR KO → cell death) | Nat Commun 2025, `s41467-025-62629-6` / PMC12370961 | Preclinical-Cell (CIC-DUX4-direct, genetic) | Already in `findings-ranking.md` (row D) and protocol V3 as *driver-contingent* |
| **WEE1 + CCNE1 dependency; adavosertib (WEE1i) → tumour regression in CIC::DUX4 xenografts** | same Nat Commun 2025 paper | Preclinical-Animal (CIC-DUX4-direct) | **Independently validates Sim 3's WEE1+ifosfamide convergence in real CIC-DUX4** (was Ewing-proxy) |
| **p300/CBP required for CIC-DUX4 activity; iP300w / A-485 suppress it and destabilise the fusion** | Oncogenesis 2021 `s41389-021-00357-4` / PMC8511258; 2024 follow-up | Preclinical-Cell/Animal | Already in register (Bakaric 2024, PMID 38275898) |
| **IGF1R via HMGA2/IGF2BP/IGF2 axis → trabectedin + PI3K/mTOR (dactolisib) sensitivity** | AACR Cancer Res 2022 82(4):708 | Preclinical-Cell (CIC-DUX4-direct) | Validates Sim 1 IGF1R; **trabectedin link is a useful addition** |
| **New real CIC-DUX4 chromatin dataset GSE248040** ("new epigenetic dependencies") | PMC10814785 (2024) | dataset | **Not yet mined** — flag for a network-enabled run (see §E) |

*Reassurance value:* the catalog is not stale on the headline targets. The plateau is
real but it reflects a genuinely small evidence base, not negligence.

## B. Genuine deltas — the p300/CBP unification (highest-value)

**The 2025 immune-modeling paper changes how the MHC-I bridge should be framed.**

> *"Modeling CIC::DUX4 sarcoma reveals oncogene-mediated MHC-I-dependent immune evasion"* —
> Mol Cancer 2025, `s12943-025-02485-6` **[VERIFY]**: **CIC::DUX4 / p300 / CBP-mediated
> suppression of MHC-I** is a key immune-evasion mechanism; DUX4 expression **blocks IFN-γ
> -mediated MHC-I induction** and promotes ICB resistance.

Implication: the **same p300/CBP node** that the catalog already lists as the super-enhancer
*writer* (V1/V3 throttle) is **also the MHC-I suppressor** (V4 priming). So a p300/CBP
inhibitor is a candidate **single-node, multi-vector** intervention:
- throttles the oncogenic output (V1) and restores the differentiation/brake context (V3),
- **destabilises the fusion protein** (acetylation-dependent stability — §A),
- **de-represses MHC-I** → makes the cold tumour visible (V4 priming) — the role the
  catalog currently assigns mainly to EZH2i (now F4 in the US after tazemetostat's
  withdrawal), so p300/CBPi is a **timely replacement bridge**.

**Feasibility (perishable — [VERIFY] live):** **inobrodib (CCS1477)**, oral p300/CBP
bromodomain inhibitor — heme trials `NCT04068597`; solid-tumour arms for p300/CBP-mutant
tumours `NCT03568656`; **TT125-802** p300/CBP bromodomain inhibitor phase 1 in solid tumours
`NCT06403436`. No sarcoma-specific arm found. Band ≈ **F3** (clinical-stage, no CIC route yet).
A-485 / iP300w remain preclinical tools. **Caveat:** p300/CBP is broadly essential —
therapeutic-window and on-target toxicity are the real risk; this is not a benign target.

## C. Genuine deltas — immune axis (V4)

| Delta | Source [VERIFY] | Tier | Why it's new to the catalog |
|---|---|---|---|
| **DUX4 binds STAT1 and broadly inhibits interferon-stimulated genes (ISGs)** | bioRxiv 2022 `10.1101/2022.08.09.503314` | Mechanistic | A **second, MHC-I-independent** immune-evasion arm (global ISG blunting). Explains the IFN-cold phenotype beyond MHC-I; predicts IFN-axis therapies are blunted at the source. Fusion-relevant (DUX4 moiety). |
| **Documented CIC::DUX4 response to dual ICB (nivolumab + relatlimab = anti-PD-1 + anti-LAG-3)** with post-treatment CD8 influx + PD-1/LAG-3 exhaustion markers | npj Precision Oncology 2025 `s41698-025-00878-w` | Clinical (single case) | Catalog says "modest checkpoint *monotherapy*"; this is a **doublet incl. LAG-3** signal. Pre-treatment was immune-cold (scarce CD3/CD8/FOXP3, negligible PD-L1/PD-1) → argues for **priming-then-checkpoint** sequencing, consistent with Sims 4/5. |

**Sequencing read (ties to Sims 4/5 + ADR-0006):** cold baseline → the lever is *visibility
first* (p300/CBPi or EZH2i to restore MHC-I; or an ICD/danger signal) **then** checkpoint,
ideally a **PD-1 + LAG-3 doublet** given the documented exhaustion phenotype. Lowering
inflammation ≠ improving anti-tumour immunity (inflammation-state lens).

## D. Genuine deltas — feasibility nuance on MCL1 (matters for THIS patient)

The MCL1 dependency is real (§A), but the **class has a well-documented cardiotoxicity
signal** that the catalog should carry explicitly:
- S64315 (MCL1i) phase-1 — cardiovascular dose-limiting toxicities, discontinued for
  lack of efficacy; **AMG176/AMG397 halted for a cardiac safety signal**; ABBV-467 —
  troponin increases in patients; AZD5991 — limited single-agent activity, GI-heavy AEs.
  **[VERIFY]** (ClinCancerRes 2024 PMC11528199; Commun Med `s43856-023-00380-z`).
- Next-gen **BRD-810** (Nat Cancer 2024 `s43018-024-00814-0`) was explicitly engineered for
  **optimised in-vivo clearance to reduce cardiac exposure**, with efficacy in *solid* and
  heme models — the most plausible future route. **[VERIFY]**

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

## F. Datasets surfaced for a network-enabled re-run (do NOT mine here — egress-blocked)
- **GSE248040** — CIC-DUX4 ChIP-seq / chromatin profiling (2024) — would directly extend Sim 1's single-line signature. **[VERIFY]**
- **Patient-derived CIC::DUX4 tumoroids** (Nat Commun 2025) — drug-screen + CRISPR data; the real-CIC-DUX4 dependency resource the catalog has wanted instead of the Ewing proxy. **[VERIFY]**
- DepMap CIC-DUX4 lines (TE441T, NCC-CDS1-X1/X3) — still no CRISPR screen as of last check; expression mineable.

## G. What I could not establish
- **Full-text verification of any paper** — only search snippets/abstracts were reachable
  (WebFetch + NCBI/EBI/PMC egress-blocked). Treat every PMID/accession/NCT as **[VERIFY]**.
- **Live registry status** for the trials in §B/§D — `docs/09` registries were unreachable;
  bands are snippet-derived and perishable.
- **Any quantitative condensate descriptor** — Sim 9's UniProt fetch was egress-blocked; the
  pipeline ran its self-test but produced **no biological numbers** (not fabricated).

## H. Recommended next moves (ranked)
1. **Re-run this refresh + Sim 9 in a network-permissive environment** (widen the egress
   allowlist to include `rest.uniprot.org`, NCBI/EBI, and `clinicaltrials.gov`, or run
   locally) — then full-text-verify §A–§D and execute Sim 9 for real descriptors.
2. **Add a `p300/CBP` consolidated entry to the catalog** framing it as the single-node
   multi-vector bridge (V1/V3 throttle + fusion destabilisation + V4 MHC-I restoration),
   replacing/augmenting the EZH2i-centric MHC-I bridge (EZH2i now F4-US).
3. **Carry the DUX4-STAT1/ISG-antagonism mechanism** in V4 as a distinct evasion arm.
4. **Down-weight MCL1 for this patient** with the cardiotox × prior-anthracycline flag.
5. Mine **GSE248040** and the **tumoroid drug-screen** to replace Ewing-proxy dependency data.

*All items are research-simulation hypotheses, snippet-sourced and [VERIFY]-flagged. Not medical advice.*
