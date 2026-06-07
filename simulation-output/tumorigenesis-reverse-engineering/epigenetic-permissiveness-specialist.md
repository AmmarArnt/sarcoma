# Epigenetic-Permissiveness Specialist — Forward "Steps to Reproduce"

> **Team:** Tumorigenesis / Cell-of-Origin Reverse-Engineering (supplementary).
> **Framing:** INVERSE of the repo's normal attack posture. The question is *what chromatin/firmware
> state must be set so an inserted CIC-DUX4 driver "compiles and runs" instead of crashing.*
> **This is a research SIMULATION — hypothesis generation, NOT medical advice.** No dosing, no
> start/stop instructions. Mechanisms and evidence tiers only.
> **Atypical-case flag (~5%):** steps below assume a confirmed CIC-DUX4 fusion. Where a step is
> fusion-junction-specific vs. fusion-agnostic it is noted, since ~5% of clinically CIC-rearranged
> tumors have no confirmed fusion.

---

## One-line summary + confidence

To make CIC-DUX4 productive you must put it into a cell whose chromatin is already **open and poised at
its HMG-box/ETS addresses** and whose **p300/CBP acetyltransferase machinery is available to be hijacked**
into building/amplifying H3K27ac enhancers at ETV4/ETV5 — the p300 dependency is the one CIC-DUX4-*specific*,
experimentally anchored construction step; the rest of the chromatin context (bivalency, progenitor
accessibility, DUX4 pioneer access, BAF maintenance) is mechanistically strong but partly transferred.
**Confidence: moderate** (B/C) for the overall picture; **higher** for the p300 step specifically (direct
CIC-DUX4 evidence), **lower/Theoretical** for the lock-in step.

---

## Forward build step(s) I own (firmware / chromatin states to set)

### Step E1 — Start with progenitor-grade open/poised chromatin at the target loci
**State to set:** `chromatin_open_at_ETS = TRUE` (ETV1/4/5 and CIC HMG-box target loci accessible,
bivalent H3K4me3+H3K27me3 rather than constitutively H3K9me3/H3K27me3-locked).
**Mechanism:** CIC-DUX4 keeps CIC's HMG-box and still binds the same T(G/C)AATG(A/G)A addresses, but a
TF can only *act* where its motif is accessible. Mesenchymal progenitors carry broadly open, bivalent
chromatin "poised" for activation or silencing, so a neomorphic activator landing on a poised ETS locus
flips it ON rather than hitting closed heterochromatin and doing nothing. This is the cell-of-origin /
"right cell at the right moment" requirement.
**Evidence tier:** Mechanistic (the bivalency/progenitor-permissiveness principle; docs/03). The
*specific* observation that CIC-DUX4 sarcoma shows markedly open chromatin at ETV4/ETV5 is
**Preclinical-Cell** — chromatin profiling shows CIC-DUX4 occupies its sites as an active, H3K27ac-co-localized
activator (Bakaric et al., *Cancers* 2024, **PMID 38275898**, DOI 10.3390/cancers16020457).
**CIC-DUX4-specific?** The open-state-at-ETV4/5 readout is CIC-DUX4-specific; the bivalency/poising
*rationale* is general developmental chromatin biology (transferred).

### Step E2 — Make p300/CBP available so CIC-DUX4 can convert binding into H3K27ac enhancer/super-enhancer output
**State to set:** `p300_recruited = TRUE` → drives `H3K27ac_high_at_ETS = TRUE` → enables
`super_enhancer_formed = TRUE`.
**Mechanism:** This is the load-bearing, CIC-DUX4-specific construction step. CIC-DUX4 is a **neomorphic
transcriptional activator that directly interacts with the acetyltransferase p300**; p300 deposits
H3K27ac at fusion-bound loci, and p300 is **essential for CIC-DUX4 sarcoma proliferation** in vitro and
in vivo (Bakaric et al. 2024, **PMID 38275898**). A second independent model shows CIC-DUX4 acts
*through* **p300/CBP**, and p300/CBP inhibition (or fusion inactivation) reverses the program — including
restoring MHC-I — i.e., p300/CBP is the executing enzyme of the oncogenic chromatin state (Modeling
CIC::DUX4 sarcoma, *Molecular Cancer* 2025, DOI 10.1186/s12943-025-02485-6, **PMC12659477**;
PMID [VERIFY]).
**Why this is the "compile" step:** the fusion supplies the *address book and the activation domain*, but
the **H3K27ac amplification by p300** is what turns sparse binding into a dominant, BRD4-readable
super-enhancer output. Without an acetyltransferase to hijack, the activation domain has nothing to write.
**Evidence tier:** **Preclinical-Cell / Preclinical-Animal** (direct CIC-DUX4 evidence, two independent
models).
**Super-enhancer fold-change caveat (per docs/02–03):** the *directional* claim (de novo H3K27ac/SE
gain at ETV4/5) is supported in CIC-DUX4; a *specific fold-change* and a phase-separation/condensate
mechanism are **NOT** proven for CIC-DUX4 (best-supported in EWSR1 fusions) — do not assert "10–100×" or
condensate nucleation as CIC-DUX4 fact. Tag any condensate language **Theoretical (transferred)**.

### Step E3 — Supply DUX4's pioneer-like access without triggering the DUX4 death program
**State to set:** `dux4_pioneer_access = TRUE` AND `dux4_death_program = FALSE`.
**Mechanism:** Full-length DUX4 behaves pioneer-like — it binds MaLR/ERVL-enriched, relatively
condensed chromatin and **recruits EP300 to acetylate and open those loci**, activating cleavage-stage
genes (ZSCAN4, KDM4E, PRAMEF) and MERVL/HERVL retroelements (Hendrickson et al., *Nat Genet* 2017,
**DOI 10.1038/ng.3844**, PMID 28459457 [VERIFY]; DUX4-primes-EGA review, *iScience* 2022, PMC8990217).
But full DUX4 is **cytotoxic** — its C-terminal/p300-dependent global H3 hyperacetylation drives cell
death, reversible by p300 inhibition (Bosnakovski et al., *Sci Adv* 2019, DOI 10.1126/sciadv.aaw7781,
PMC6739093). **The fusion's escape hatch:** CIC-DUX4 keeps DUX4's transactivation domain but **replaces
DUX4's homeodomain DNA-binding with CIC's HMG-box** — so the destructive, genome-wide totipotency/MERVL
program is *not* addressed; the same p300-recruiting activation domain is instead **re-targeted to a
bounded ETS gene set**. The build trick is *retargeting a totipotency activator onto a survivable
proliferation address space.*
**Evidence tier:** Mechanistic for the "retargeting avoids the death program" inference (no direct
CIC-DUX4 toxicity-comparison study found); Preclinical-Cell for the underlying DUX4 pioneer/p300 and
DUX4-toxicity facts.
**CIC-DUX4-specific?** The retargeting logic is fusion-architecture-specific; the pioneer/death facts are
from DUX4 biology (transferred).

### Step E4 — Keep target loci open via chromatin remodeling (BAF/SWI-SNF maintenance)
**State to set:** `baf_maintained_open = TRUE` (target nucleosomes kept evicted/repositioned so
H3K27ac+BRD4 output persists across divisions).
**Mechanism:** Sustained activator output at an enhancer generally requires ATP-dependent remodeling
(BAF/SWI-SNF) to keep nucleosomes from re-closing the site. docs/02 lists "CIC-DUX4 recruits BAF
components to maintain open chromatin" as part of the amplification layer.
**Evidence tier:** **Theoretical / Mechanistic** — I found **no CIC-DUX4-specific study demonstrating BAF
recruitment by the fusion.** `[no direct citation; mechanism inferred from general BAF-at-active-enhancer
biology and the docs/02 amplification model]`. Flagged as a GAP below.

---

## The lock-in question — is there an epigenetic "point of no return"?

**Short answer: plausible but NOT demonstrated for CIC-DUX4. Treat as Theoretical, and treat the absence
of proof as good news for V3.**

- **Argument FOR lock-in:** Once p300 builds H3K27ac super-enhancers that drive ETV4/5 → CCND1/MYC, and
  BAF keeps the loci open, the state is *self-feeding* (active enhancers recruit more coactivator; MYC
  reinforces biosynthesis). Epigenetic drift toward a self-reinforcing oncogenic attractor is a general
  model (docs/03). DUX4's own ability to open and acetylate condensed chromatin (E3) could "fix" loci
  that normally re-silence. A condensate-based positive feedback would deepen lock-in — but that is
  **EWSR1-transferred and not shown for CIC-DUX4.**
- **Argument AGAINST a hard lock-in (and it is strong):** Both anchor papers show the oncogenic chromatin
  state is **reversible** — genetic CIC-DUX4 inactivation **or** pharmacologic p300/CBP inhibition causes
  cell-cycle arrest and *restores* MHC-I (PMID 38275898; PMC12659477). A state that collapses when its
  writer enzyme is blocked is **maintenance-dependent, not irreversibly latched.** PNAS 2020 (negative
  MAPK-ERK regulation sustains CIC-DUX4 expression, PMID 32737163 [VERIFY]) further implies the state is
  actively *sustained* rather than self-perpetuating without input.
- **Reconciliation:** the likely truth is a **deep but drainable attractor** — strongly self-reinforcing
  while the fusion + p300 keep writing, but **not past a point of no return.** This is the key
  reverse-engineering inference for V3: differentiation/epigenetic reversal is *mechanistically
  on-the-table* because lock-in appears writer-dependent, not absolute.
**Evidence tier:** reversibility = Preclinical-Cell/Animal; "no hard point of no return" = Mechanistic
inference; deep-attractor framing = Theoretical.

---

## Reverse-engineering note — which vector undoes each step, and GAPS → forward hypotheses

| Build step | State set | Undone by (existing vector) | Mechanism of reversal |
|---|---|---|---|
| E1 open/poised at ETS | `chromatin_open_at_ETS` | **V3** (EZH2i/HDACi re-balancing; differentiation) ; **V4** (epigenetic MHC-I priming) | Push poised loci toward commitment/silencing; close the address space the fusion exploits |
| E2 p300→H3K27ac→SE | `super_enhancer_formed` | **V1** (BRD4/BET inhibition collapses SE readout) ; **V3** (**p300/CBP inhibition** — the writer itself) | BETi removes the reader; p300i removes the writer → SE output + MHC-I suppression collapse (PMID 38275898; PMC12659477) |
| E3 DUX4 pioneer access, death-program off | `dux4_pioneer_access` | **V3** (re-impose the differentiation/death endpoint the fusion routed around) | Restore a survivable→committed trajectory; conceptually, re-expose the DUX4-style death program |
| E4 BAF maintenance | `baf_maintained_open` | *No mapped vector yet* | (GAP) |
| Lock-in / attractor | `epigenome_locked` | **V3** (only works *if* lock-in is writer-dependent, which evidence supports) | Drain the attractor by removing the maintenance writer |

**GAPS → Forward Hypotheses (each with falsifier):**
- **FH-EP1 (high value):** *p300/CBP is the single most reversible CIC-DUX4 chromatin dependency and should
  be elevated within V3 as a writer-level (not just reader-level/BETi) target, with the bonus of MHC-I
  restoration bridging V3→V4.* Tier: Preclinical-Cell/Animal (already supported). **Falsifier:** p300/CBP
  inhibition fails to reduce ETV4/5 H3K27ac or restore MHC-I in an independent CIC-DUX4 model.
- **FH-EP2:** *CIC-DUX4 requires BAF/SWI-SNF to keep ETS loci open; a BAF ATPase (SMARCA2/4) or
  degrader-style perturbation would collapse the same loci as BETi.* Tier: Theoretical (GAP — no
  CIC-DUX4 data). **Falsifier:** BAF perturbation does not reduce accessibility/H3K27ac at fusion target
  loci in CIC-DUX4 cells.
- **FH-EP3:** *Because lock-in appears writer-dependent, transient combined writer/reader blockade
  (p300i + BETi) could push CIC-DUX4 cells past an arrest threshold into durable differentiation rather
  than reversible cytostasis.* Tier: Theoretical. **Falsifier:** combined blockade yields only reversible
  arrest with full rebound on washout (i.e., a true hard latch exists).

---

## Model parameters for the sim (discrete state + logic rules)

```text
# State variables (booleans unless noted)
chromatin_open_at_ETS   # ETV1/4/5 + CIC HMG-box loci accessible/bivalent (cell-of-origin gate)
fusion_present          # CIC-DUX4 protein expressed and bound to its HMG-box addresses
p300_available          # p300/CBP acetyltransferase free to be hijacked
dux4_pioneer_access     # DUX4-domain pioneer-like opening of otherwise-condensed loci
dux4_death_program      # genome-wide DUX4 toxicity (hyperacetylation/MERVL) firing
baf_maintained_open     # BAF/SWI-SNF keeps target nucleosomes evicted
H3K27ac_high_at_ETS     # active enhancer mark deposited at target loci
super_enhancer_formed   # BRD4-readable SE at ETV4/ETV5
epigenome_locked        # self-reinforcing attractor engaged (NOT a hard latch by default)
productive_transformation  # output: fusion is "running"

# Logic rules
H3K27ac_high_at_ETS   = fusion_present AND chromatin_open_at_ETS AND p300_available
super_enhancer_formed = H3K27ac_high_at_ETS AND baf_maintained_open
dux4_death_program    = dux4_pioneer_access AND (NOT fusion_retargets_HMG)  # fusion sets retarget=TRUE
epigenome_locked      = super_enhancer_formed AND p300_available            # maintenance-dependent
productive_transformation = super_enhancer_formed AND (NOT dux4_death_program)

# Reversal hooks (vector perturbations)
apply_BETi  -> super_enhancer_formed = FALSE            # reader removed (V1)
apply_p300i -> H3K27ac_high_at_ETS = FALSE; MHC_I = restored  # writer removed (V3->V4)
apply_BAFi  -> baf_maintained_open = FALSE              # FH-EP2, untested
# Key sim assertion to test: epigenome_locked is reversible (drains) when p300_available=FALSE.
```

---

## What I could not establish (mandatory)

- **No CIC-DUX4-specific evidence that the fusion recruits BAF/SWI-SNF** (E4). The maintenance step is
  inferred; the docs/02 statement is not citation-backed in what I could verify.
- **No direct CIC-DUX4 measurement of a super-enhancer fold-change**, and **no CIC-DUX4 phase-separation/
  condensate demonstration** — both remain EWSR1-transferred per docs/02–03 caveats.
- **No study directly comparing CIC-DUX4 vs. full-length DUX4 toxicity** in the same cell to prove the
  "retargeting avoids the death program" model (E3) — it is a mechanistic inference from fusion
  architecture + separate DUX4-toxicity papers.
- **Could not confirm a true epigenetic point-of-no-return.** Available evidence points the other way
  (reversibility on p300i / fusion loss), but absence of a hard-latch demonstration is not proof one
  doesn't exist in some contexts.
- **PMIDs marked [VERIFY]** (PMC12659477/Mol Cancer 2025; ng.3844; PNAS 2020) — DOIs/PMC IDs confirmed via
  search, exact PubMed PMIDs not individually re-pulled from PubMed; re-verify before external use.

## Falsifiers (for the whole "permissiveness" thesis)

1. **E1 falsifier:** Introducing CIC-DUX4 into cells with *closed/heterochromatic* ETV4/5 loci still
   produces robust ETS activation and transformation → poised/open chromatin is *not* the permissiveness
   gate.
2. **E2 falsifier:** CIC-DUX4 drives its full transcriptional program with p300/CBP genetically deleted →
   p300 is not the executing writer (contradicts PMID 38275898 / PMC12659477).
3. **E3 falsifier:** CIC-DUX4 (HMG-box retargeted) is as cytotoxic as full-length DUX4 in the same cell →
   retargeting does not avoid the death program.
4. **Lock-in falsifier:** Removing CIC-DUX4 / inhibiting p300 fails to reverse the chromatin state and
   cells stay transformed → a true point-of-no-return exists, weakening V3's premise.

---

### Verified source anchors
- Bakaric et al., *Cancers* 2024 — CIC-DUX4 chromatin profiling; neomorphic activator via direct p300;
  p300 essential. **PMID 38275898**, DOI 10.3390/cancers16020457. *(CIC-DUX4-specific.)*
- Modeling CIC::DUX4 sarcoma, *Molecular Cancer* 2025 — CIC::DUX4/p300/CBP-mediated MHC-I suppression;
  p300/CBP inhibition restores MHC-I + arrests cells. DOI 10.1186/s12943-025-02485-6, **PMC12659477**
  (PMID [VERIFY]). *(CIC-DUX4-specific.)*
- Hendrickson et al., *Nat Genet* 2017 — DUX4 activates cleavage-stage genes + MERVL/HERVL via EP300.
  DOI 10.1038/ng.3844 (PMID 28459457 [VERIFY]). *(DUX4 biology; transferred.)*
- Bosnakovski et al., *Sci Adv* 2019 — DUX4 global H3 hyperacetylation/cell death reversed by p300i.
  DOI 10.1126/sciadv.aaw7781, PMC6739093. *(DUX4 toxicity; transferred.)*
- Okimoto/Sin et al., *PNAS* 2020 — negative MAPK-ERK regulation sustains CIC-DUX4. DOI
  10.1073/pnas.2009137117 (PMID 32737163 [VERIFY]). *(CIC-DUX4-specific; supports maintenance-dependence.)*
