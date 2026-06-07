# Tumorigenesis "Build Recipe" — How a Stem/Progenitor Cell Becomes a CIC-DUX4 Sarcoma Cell, and What Each Build Step Reveals as a Reverse-Engineering Target

> **Team:** Tumorigenesis / Cell-of-Origin Reverse-Engineering Team (supplementary). Lead reconciliation
> of four specialist briefs + Sim 7.
> **This is the INVERSE of the repo's normal posture.** The four attack vectors (V1–V4) ask *how do we
> break an existing CIC-DUX4 cell?* This brief asks the **forward / "steps to reproduce"** question —
> *what would you have to do to a normal stem/progenitor cell to BUILD one?* — because a construction
> recipe, read backwards, is a map of intervention points.
> **Research simulation, hypothesis generation only. Not medical advice, not a treatment plan, no dosing.**

---

## 0. TL;DR

Building a CIC-DUX4 sarcoma cell is **not** "install the fusion." The fusion's own DUX4 program is
pro-apoptotic, so in most cells the fusion alone *kills or arrests* rather than transforms. The
reconciled recipe is a **logical AND of six steps**, of which **five are non-substitutable**:

1. **Substrate** — a permissive mesenchymal/osteochondrogenic progenitor in an open-chromatin,
   high-proliferation developmental window. *(differentiation is a defense)*
2. **Driver** — install CIC-DUX4 → logic inversion at ETS loci (ETV1/4/5 flip from repressed to ON).
3. **Survive the driver** — buffer the DUX4 death program via the **MCL1/BCL2** anti-apoptotic axis.
   *(the fragility — verified dependency)*
4. **Lift the senescence brake** — **CDKN2A/2B (9p21) loss** (p16→Rb + p14ARF→p53), *or* (rarely) TP53
   loss. *(this is the one substitutable step — the gene varies, the function is required)*
5. **Amplify** — hijack **p300/CBP** to build H3K27ac super-enhancers at ETV4/5 (BRD4-read) so the ETS
   output becomes dominant. *(CIC-DUX4-specific, and reversible)*
6. **Immortalize** — maintain telomeres (TERT reactivation or ALT; mechanism in CIC-DUX4 is **unknown** —
   the single biggest evidence gap).

**Sim 7** (`sims/07-tumorigenesis-trajectory/`) enumerated this logic exhaustively: of 128 genotype
combinations only **3 fully transform, 16 die, 109 are abortive**; the apoptosis buffer (step 3) is
**non-substitutable**; and **order matters** — the death gate forces step 3 to be in place no later than
step 2 (installing the buffer first makes 120/120 build orders viable vs 60/120 if the fusion goes first).

**The reverse-engineering payoff:** four of the six build steps (substrate, MCL1 buffer, p53/TP53 brake,
immortalization) are targeted by **no current attack vector** — they are the forward-hypothesis frontier.
The single highest-value one is **re-arming the DUX4 death program the tumor had to suppress (MCL1
inhibition)**: the buffer the build was forced to install is a standing, re-armable vulnerability.

---

## 1. The engineering analogy, stated honestly

| Build concept | Software analogy | The actual biology (load-bearing) |
|---|---|---|
| Substrate cell | target hardware / OS | mesenchymal progenitor with open bivalent chromatin |
| Epigenome | firmware / build config | poised H3K4me3+H3K27me3; p300/CBP available |
| Driver insertion | merge a rogue module | t(4;19)/t(10;19) → CIC-HMG-box + DUX4-transactivation |
| "It compiles but crashes" | unhandled fatal exception | DUX4 transactivation domain triggers apoptosis |
| Exception handler | try/except around the crash | MCL1/BCL2 anti-apoptotic buffering |
| Removing the watchdog timer | disable the safety check | CDKN2A loss removes oncogene-induced senescence |
| Optimizer / JIT | make hot path dominant | p300→H3K27ac super-enhancer amplification |
| Preventing process exit | disable lifetime limit | telomere maintenance (TERT/ALT) |

The analogy is shorthand; every row is translatable to the biology in the right-hand column. (Per the
repo golden rule: mechanism before analogy.)

---

## 2. The reconciled build recipe (ordered, with evidence tiers and verified citations)

Each step lists the owning specialist brief; full mechanism + falsifiers are in those files.

### Step 1 — Start from a permissive progenitor in the developmental window
*(cell-of-origin-specialist)*
- **Action:** select an immature MSC-like mesenchymal/osteochondrogenic progenitor (limb-bud lineage),
  proliferating, with open/bivalent chromatin at ETS loci.
- **Mechanism:** the fusion's retained HMG-box can only *activate* ETV4/5 where those loci are accessible;
  differentiated cells have them closed and the fusion instead triggers the DUX4 death program — so
  **differentiation is a defense**. The same open-chromatin/high-TopoII window that lets the translocation
  *form* is what lets the fusion *reprogram* the cell → one explanation for the adolescent/young-adult peak.
- **Tier:** Preclinical-Animal (mouse mesenchymal transformation + transcriptomic concordance);
  Theoretical for the human "window" timing.
- **Citations (verified):** Yoshimoto et al., *Cancer Res* 2017;77(11):2927–37, **PMID 28404587**,
  DOI 10.1158/0008-5472.CAN-16-3351. GEMM corroboration: Hendrickson/Kirsch, *Oncogene* 2024,
  DOI 10.1038/s41388-024-02984-8, **PMID 38413794**.

### Step 2 — Install the CIC-DUX4 driver (logic inversion at ETS loci)
*(driver-engineering-specialist)*
- **Action:** express the fusion ORF (CIC N-terminus + HMG-box | DUX4 C-terminal transactivation domain).
- **Mechanism:** a repressor of ETV1/4/5 becomes a constitutive activator at the *same* addresses, and the
  ERK-phospho off-switch is deleted → signal-independent ETS derepression. ETV4 over-expression is the
  clinical IHC hallmark.
- **Tier:** Established (fusion structure + ETS up-regulation).
- **Citation (verified):** Kawamura-Saito et al., *Hum Mol Genet* 2006;15(13):2125–37, **PMID 16717057**,
  DOI 10.1093/hmg/ddl136 (original cloning; PEA3/ETS up-regulation; NIH3T3 transformation).

### Step 3 — Survive the driver: buffer the DUX4 death program (the fragility)
*(driver-engineering-specialist; cooperating-lesions-specialist)*
- **Action:** install/retain an anti-apoptotic buffer — the **MCL1/BCL2** axis.
- **Mechanism:** DUX4 is a totipotency/ZGA pioneer factor whose somatic expression drives an
  embryonic program (de-repressed transposable elements, dsRNA/innate mimicry) that **culminates in cell
  death** (the FSHD death program). The fusion carries that same transactivation domain, so the cell must
  *defeat its own driver's death program* to exist. Patient-derived CIC::DUX4 tumoroids are selectively
  **MCL1-dependent** — MCL1 inhibition triggers rapid apoptosis. Because this death program is largely
  **p53-independent**, losing p53 does **not** substitute for this buffer (this is why Sim 7 makes it a
  non-substitutable node).
- **Tier:** Preclinical-Cell/Animal (MCL1 dependency); Mechanistic (the buffering requirement).
- **Citation (verified, with a reconciliation flag):** *Nat Commun* 2025, CIC::DUX4 tumoroids → MCL1
  vulnerability. **The two specialist briefs cite adjacent accessions for this paper — PMID 40841513
  (DOI 10.1038/s41467-025-62629-6) vs PMID 40841360. VERIFY the exact PMID before external use.**
  Background DUX4 toxicity: Shadle et al., *PLoS Genet* 2017;13(3):e1006658 (FSHD; transfer-flagged).

### Step 4 — Lift the senescence brake (the one substitutable step)
*(cooperating-lesions-specialist)*
- **Action:** delete/silence **CDKN2A/2B (9p21)** — *or*, rarely, lose TP53.
- **Mechanism:** the fusion forces the CCND1–CDK4–Rb gate open; a strong oncogene's default fate in a
  primary cell is oncogene-induced senescence. CDKN2A loss removes **both** brakes at once — p16 (→CDK4/6→Rb,
  senescence) and p14ARF (→MDM2→p53). In CIC-DUX4, TP53 point mutation is **rare** and the SNV landscape is
  quiet, so CDKN2A/ARF loss is the empirically favored route.
- **Tier:** Mechanistic (role)/Clinical-genomic (occurrence); **the exact CIC-DUX4 CDKN2A-deletion % is
  `[VERIFY]` — do not cite a number** (docs/02's "frequent" is directionally right; no clean cohort rate
  was verifiable).
- **Citations (verified):** Specht et al., *Hum Pathol* 2016;58:161–70, **PMID 27664537** (quiet SNVs;
  recurrent 1p loss + chr8 gain; Ewing-type CNAs incl. TP53 del **not** recurrent). Pan-STS CDKN2A context:
  Bui et al., *Clin Sarcoma Res* 2019;9:12, **PMID 31528332**.

### Step 5 — Amplify the output: hijack p300/CBP → super-enhancers
*(epigenetic-permissiveness-specialist)*
- **Action:** recruit **p300/CBP** to deposit H3K27ac at ETV4/5, building BRD4-readable super-enhancers so
  the ETS output is *dominant* rather than a transient burst.
- **Mechanism:** the fusion supplies the address book + activation domain, but p300 is the **writer** that
  turns sparse binding into a dominant program; p300 is **essential** for CIC-DUX4 proliferation, and
  p300/CBP inhibition (or fusion loss) collapses the state **and restores MHC-I** — a direct V3→V4 bridge.
  Crucially the state is **reversible** on writer removal → a *deep but drainable attractor*, **no hard
  epigenetic point-of-no-return demonstrated** (this supports V3's differentiation premise).
- **Tier:** Preclinical-Cell/Animal (CIC-DUX4-specific). Do **not** assert a super-enhancer fold-change or
  a phase-separation/condensate mechanism — those remain EWSR1-transferred (per docs/02–03 caveats).
- **Citations (verified):** Bakaric et al., *Cancers* 2024;16(2):457, **PMID 38275898**,
  DOI 10.3390/cancers16020457 (p300 dependency). MHC-I link: *Mol Cancer* 2025,
  DOI 10.1186/s12943-025-02485-6, PMC12659477 (PMID [VERIFY]).

### Step 6 — Immortalize (telomere maintenance) — the biggest unknown
*(cooperating-lesions-specialist)*
- **Action:** maintain telomeres via TERT reactivation or ALT.
- **Mechanism:** replicative immortality is a required hallmark; without it even a fully driver-loaded cell
  hits crisis. In CIC-DUX4 the **mechanism is genuinely unestablished** — TERT-promoter hotspot mutations
  are rare in non-myxoid STS, so a promoter-mutation route is unlikely; whether it is non-mutational TERT
  reactivation (plausibly DUX4-driven, since DUX4 evokes an embryonic program where telomerase is active)
  or ALT is **not reported**.
- **Tier:** Established (the requirement); Theoretical (the CIC-DUX4-specific mechanism).
- **Citation (verified):** Koelsche et al., *J Exp Clin Cancer Res* 2014;33:33, **PMID 24726063**
  (TERT-promoter mutations rare outside myxoid liposarcoma). `[no direct citation for the CIC-DUX4
  telomere-maintenance mechanism — UNKNOWN]`.

**Near-obligate accelerant (not a separate gate):** MYC amplification / trisomy 8 (MYC-locus amp 6/7,
trisomy 8 5/7, MYC IHC 10/10 — *Mod Pathol* 2015, **PMID 24947144**) supplies biosynthetic throughput;
CCNE1-driven replication stress buffered by an intact WEE1 G2/M checkpoint is a required *survival state*.

---

## 3. The minimal transformation set (Sim 7)

Exhaustive enumeration (`sims/07-tumorigenesis-trajectory/`) of the encoded logic:

- **Necessary (in every sufficient recipe):** permissive progenitor, fusion, **MCL1/BCL2 apoptosis
  buffer**, telomere immortalization, p300/super-enhancer amplification.
- **Substitutable:** the senescence-bypass *gene* — **CDKN2A loss OR TP53 loss** (function required, gene
  varies; CDKN2A is the empirical route).
- **Minimal recipe (empirical):** `progenitor + fusion + MCL1-buffer + CDKN2A-loss + immortalize + p300/SE`.
- **Order constraint:** the DUX4 death gate means the apoptosis buffer must be installed **no later than**
  the fusion becomes active in a permissive cell — buffer-first → 120/120 build orders viable; fusion-first
  → only 60/120 (240/720 orders abort overall, almost all by death).

**This is a logic-model claim** (Mechanistic/Theoretical), not measured transformation data — its job is to
make the dependency structure explicit and falsifiable.

---

## 4. Reverse-engineering map — every build step → its "undo," and the gaps

| Build step | The "undo" | Covered by | Gap / forward hypothesis |
|---|---|---|---|
| 1 Permissive progenitor | force differentiation / harden the chassis | **V3** (after the fact only) | **GAP** — no vector pre-empts the permissive window (prophylaxis is not a treatment; concept-only) |
| 2 Fusion present | prevent translocation / degrade fusion | **V2** (prophylactic) + **V3** (ASO/PROTAC) | direct degradation experimental; fusion-dependent → atypical ~5% caveat |
| 3 **MCL1/BCL2 buffer** | re-arm the DUX4 death program | **none** | **GAP → TOP FH: MCL1 inhibition** (+ raise the resident DUX4/ETS death-program load) — synthetic-lethal, not monotherapy |
| 4 Senescence brake (CDKN2A) | re-impose p16 / p14ARF arms | **V1/V3** (CDK4/6i substitutes for lost p16; convergent w/ Sims 1–3) | partial — p53 arm (MDM2i) is unaddressed by current vectors |
| 5 p300/SE amplification | remove writer (p300i) / reader (BETi) | **V3** (p300i, +MHC-I→V4) + **V1** (BETi) | well covered; elevate **p300/CBP as a writer-level V3 target** (FH-EP1) |
| 6 Telomere maintenance | telomerase/ALT targeting | **none** | **GAP** — target unspecified until mechanism known (FH-2: DUX4-driven non-mutational TERT) |
| (survivors) | immune visibility + clearance | **V4** (orthogonal; needs MHC-I via V3) | end-stage net |

**Four steps with no current vector → the forward-hypothesis frontier:** permissive substrate, MCL1
buffer, p53/TP53 brake, telomere maintenance.

---

## 5. Forward hypotheses (mechanistically defensible, not yet tested in CIC-DUX4)

Consolidated from the four briefs; each has a falsifier in its source file. All tagged Theoretical/
Mechanistic — bold in *hypothesis* space, never dressed up as evidence.

- **FH-A (highest value) — Re-arm the fragility the build had to suppress.** The tumor must hold the MCL1
  buffer ON for life. Combine **MCL1 (BCL2-family) inhibition** with anything that *raises* the resident
  DUX4/ETS death-program load (e.g. forcing the totipotency/dsRNA program), so the driver executes the
  death it was built to suppress. Bonus: DUX4-driven dsRNA/TE de-repression is a **danger signal feeding
  V4** (viral mimicry → innate sensing / immunogenic cell death). *Falsifier:* removing the buffer in an
  established line does not increase death.
- **FH-B — Reconstitute the deleted 9p21 brakes.** In CDKN2A-deleted, TP53-WT cells, **CDK4/6i (replaces
  p16) + MDM2i (replaces p14ARF)** re-imposes oncogene-induced senescence — the matched reversal of the
  locus's two arms. *Falsifier:* no senescence in TP53-WT models.
- **FH-C — Telomere maintenance is the unmeasured load-bearing hit.** Test whether CIC-DUX4 maintains
  telomeres by **DUX4-driven non-mutational TERT reactivation** (predicting telomerase-inhibitor
  sensitivity) vs ALT. *Falsifier:* ALT-positive (C-circle+) or TERT-promoter-mutant.
- **FH-D — p300/CBP as a writer-level V3 target.** p300/CBP is the most reversible CIC-DUX4 chromatin
  dependency and restores MHC-I (bridging V3→V4); combined writer+reader blockade (p300i + BETi) might
  push cells past arrest into durable differentiation. *Falsifier:* p300i fails to reduce ETV4/5 H3K27ac
  or restore MHC-I; or combined blockade gives only reversible arrest (a true latch).
- **FH-E (diagnostic only) — "Force the identity conflict."** Drive the tumor toward a differentiated
  identity its own DUX4 program cannot tolerate (re-expose the death program of Step 1's defense).

---

## 6. Cross-cutting insight: the tumor's construction debts are its vulnerabilities

Three of the build steps create **standing debts** the tumor must service for life, and each is a
re-armable kill switch in an *existing* tumor:
1. **MCL1 buffer** (Step 3) — must stay ON or the DUX4 program kills the cell.
2. **p300/CBP writing** (Step 5) — must keep writing or the super-enhancer state drains (reversible).
3. **WEE1/G2-M checkpoint** (accelerant) — must stay intact or CCNE1/MYC replication stress → mitotic
   catastrophe. (Convergent with Sim 3's "only WEE1 + ifosfamide robustly collapses viability.")

This reframes the catalog's strongest hits not as arbitrary targets but as **the exact buffers the
construction was forced to install** — which is the entire point of reverse-engineering the build.

---

## 7. What we could not establish (honest)

- **Human cell of origin is unproven** — all direct transformation evidence is mouse mesenchymal; no human
  lineage tracing. No verifiable evidence for a neural-crest origin (not excluded, just unsubstantiated).
- **No clean CIC-DUX4-specific frequencies** for CDKN2A deletion or TP53 status (small, mutationally quiet
  cohorts; several figures `[VERIFY]`). No real co-occurrence pull was possible — DepMap/cBioPortal egress
  blocked in this environment (see Sim 7 MANIFEST).
- **Telomere-maintenance mechanism in CIC-DUX4 is unknown** — the single biggest gap.
- **MCL1 paper PMID** differs between two briefs (40841513 vs 40841360) — reconcile before external use.
- **Several mechanistic steps are inferences/transfers** (DUX4-toxicity → fusion; super-enhancer/condensate
  language is EWSR1-transferred; BAF maintenance has no direct CIC-DUX4 citation).
- **Sim 7 is a logic model**, not transformation data — GIGO; the wiring is the hypothesis.

## 8. Atypical-case flag (~5%)

For clinically/histologically CIC-rearranged tumors **without** a confirmed fusion, the fusion-specific
steps (2, and fusion-dependent undos like junction ASOs) may not apply; the **cooperating-state logic
(steps 3, 4, 6) is fusion-agnostic** and still relevant.

---

## Sources
- Specialist briefs (this directory): `cell-of-origin-specialist.md`, `driver-engineering-specialist.md`,
  `cooperating-lesions-specialist.md`, `epigenetic-permissiveness-specialist.md`.
- In-silico model: `sims/07-tumorigenesis-trajectory/` (`RESULTS.md`, `transformation_model.py`, CSVs).
- Background: `docs/02-cic-sarcoma-knowledge.md`, `docs/03-dna-genome-protein-interactions.md`.

*Not medical advice. Research simulation and hypothesis generation only.*
