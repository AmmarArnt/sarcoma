# Cooperating-Lesions Specialist — Second Hits Required to Complete CIC-DUX4 Transformation

> **Team:** Tumorigenesis / Cell-of-Origin Reverse-Engineering Team (supplementary). This is a research
> SIMULATION — hypothesis generation, **not medical advice**, **not a treatment plan**. The "forward /
> build" framing is an *inverse* reverse-engineering device: each construction step is read backwards as
> an intervention point. Nothing here is an instruction to do anything to any cell or person.

**One-line summary:** The CIC-DUX4 fusion is a necessary but insufficient driver; the lesions that most
plausibly *complete* transformation are (1) loss of the **CDKN2A/2B (p16/p14ARF)** senescence brake,
(2) a permissive **G1/S–replication-stress + apoptosis-bypass** configuration (CCNE1/MYC-driven stress
buffered by an intact G2/M checkpoint and by MCL-1 anti-apoptotic dependence; TP53-pathway dampening),
and (3) **replicative immortalization** (telomere maintenance) — with the caveat that, unlike Ewing,
CIC-DUX4 cohorts show a **quiet point-mutation landscape dominated by broad copy-number events**, so most
"second hits" here are copy-number/expression states rather than recurrent SNVs. **Confidence: medium** —
the *categories* of required cooperating events are well-grounded in cancer biology and partially
evidenced in CIC-DUX4 cohorts, but exact CIC-DUX4-specific frequencies for several hits (notably TERT/
telomere status) are not established in the literature I could verify.

This output covers cooperating genomic/state lesions. It deliberately **excludes** the fusion-creation
step itself (DSB topology, cell-of-origin) — owned by sibling specialists.

---

## Forward build step(s) I own — install these "second hits"

### Step C1 — Delete the CDKN2A/CDKN2B (p16/p14ARF) senescence brake
- **Build action (forward):** homozygously delete the 9p21 *CDKN2A/CDKN2B* locus (or epigenetically
  silence it).
- **Mechanism:** *p16^INK4a* inhibits CDK4/6, keeping Rb hypophosphorylated → G1 arrest; *p14^ARF*
  sequesters MDM2, stabilizing p53. The fusion already forces the CCND1–CDK4–Rb gate open (docs/02–03);
  removing p16 *removes the only endogenous counter-throttle* on CDK4/6, and removing p14ARF blunts the
  p53 arm of **oncogene-induced senescence (OIS)** — the default fate of a strong oncogene in a primary
  cell. Without this hit the fusion tends to drive cells into senescence/crisis rather than immortal
  proliferation. *Mechanistic / Established (general OIS biology).*
- **CIC-DUX4-specific frequency:** docs/02 calls it "frequent co-occurrence." I could **not** verify a
  clean CIC-DUX4-specific homozygous-deletion percentage. What is verifiable: (a) CIC-rearranged sarcoma
  cohorts show recurrent **broad copy-number loss** but a quiet SNV landscape (Specht 2016, below);
  (b) *CDKN2A* homozygous loss is documented in **individual CIC-rearranged cases** with NGS (e.g. case
  reports describing CDKN2A/B loss alongside the CIC rearrangement); (c) in soft-tissue sarcoma broadly,
  CDKN2A copy-number loss runs ~14–22% and marks poor prognosis (Bui/Charville-type clinico-genomic
  cohort, PMID 31528332). So the *directional* claim ("loss occurs and removes the senescence brake") is
  sound; the **exact CIC-DUX4 rate is [VERIFY] — do not cite a specific %.**
- **Evidence tier:** Mechanistic (role) / Preclinical-Cell+Clinical-genomic (occurrence in sarcoma);
  CIC-DUX4-specific frequency = **inferred, not established**.
- **Citation:** Specht K et al., *Hum Pathol* 2016;58:161-170, PMID **27664537** (low TMB, recurrent
  broad CNAs in CIC-DUX4). Bui N et al., *Clin Sarcoma Res* 2019;9:12, PMID **31528332** (CDKN2A loss
  frequency + prognosis in STS, not CIC-DUX4-specific). `[no direct citation for an exact CIC-DUX4
  CDKN2A-deletion frequency; inferred from per-case NGS reports + pan-STS rates]`.

### Step C2 — Configure G1/S override + replication-stress tolerance (CCNE1 / MYC) AND buffer apoptosis
- **Build action (forward):** drive **CCNE1** (Cyclin E1) and **MYC** high (the fusion does this via
  ETS derepression and via MYC-locus amplification), and ensure the resulting replication/oncogenic
  stress is *survivable* — i.e. an intact **G2/M (WEE1) checkpoint** to avoid mitotic catastrophe, plus
  **anti-apoptotic (MCL-1) buffering**.
- **Mechanism:** CIC::DUX4-driven CCNE1 upregulation compromises the G1/S transition and raises DNA
  replication stress; the cell becomes **dependent on the WEE1-controlled G2/M checkpoint** to finish
  division — a synthetic-lethal vulnerability, but in the *build* direction it is a required survival
  buffer. MYC amplification (trisomy 8) supplies biosynthetic throughput. Independently, CIC::DUX4
  tumoroids show selective dependence on **MCL-1**, indicating the transformed state leans on
  anti-apoptotic buffering to tolerate oncogenic stress. *Preclinical-Cell / Mechanistic.*
- **CIC-DUX4-specific frequency:** **MYC amplification / chr8 (trisomy 8): MYC-locus amplification in
  6/7 testable cases, trisomy 8 in 5/7, MYC IHC+ in 10/10** (Yoshimoto/Specht-type Modern Pathology
  series). **Chromosome 8 gain + 1p loss** are the recurrent broad CNAs (Specht 2016). CCNE1 upregulation
  is a published CIC::DUX4 hallmark (WEE1 dependency work). MCL-1 dependence shown in patient-derived
  CIC::DUX4 tumoroids.
- **Evidence tier:** Preclinical-Cell (CCNE1/WEE1, MCL-1); Clinical-genomic (MYC/trisomy 8 in cohorts).
- **Citation:** "CIC-DUX sarcomas demonstrate frequent MYC amplification and ETS-family transcription
  factor expression," *Mod Pathol* 2015;28(1):57-68, PMID **24947144** (MYC 6/7, trisomy 8 5/7, IHC
  10/10). Specht 2016, PMID **27664537** (chr8 gain, 1p loss). WEE1 vulnerability via CCNE1/replication
  stress: bioRxiv 2021.06.21.448439 (preprint — `[VERIFY peer-reviewed version]`). MCL-1 dependence:
  "Small round cell sarcoma tumoroid biobank reveals CIC::DUX4 sarcoma vulnerability to MCL-1
  inhibition," *Nat Commun* 2025, PMID **40841360**.

### Step C3 — Dampen the TP53 stress-response arm
- **Build action (forward):** reduce p53 pathway output (TP53 mutation/loss, or functionally via p14ARF
  loss in C1 / MDM2 pressure).
- **Mechanism:** DUX4's transactivation domain is intrinsically **cytotoxic** when ectopically expressed
  (docs/02; FSHD biology) and a strong oncogene triggers p53-mediated apoptosis/senescence. Lowering p53
  output lets the cell *tolerate* both the DUX4 toxicity and the C2 replication stress. *Mechanistic /
  Established (p53 as OIS/apoptosis gatekeeper).*
- **CIC-DUX4-specific frequency:** **Low / not a recurrent driver in CIC-DUX4.** Unlike most STS
  (TP53 mutated ~20–47%), CIC-rearranged cohorts are notable for a **quiet mutational landscape** with
  *recurrent somatic SNVs not identified* (Specht 2016); recurrent CNAs seen in Ewing — including TP53
  deletion — were **not** recurrent in the limited CIC-DUX4 cohort. This argues TP53 is **often bypassed
  indirectly** (via p14ARF loss / MDM2 axis) rather than mutated. **Treat direct TP53 mutation as an
  optional, low-frequency hit in CIC-DUX4 specifically — the *function* (senescence/apoptosis bypass) is
  required; the *gene-level mechanism* is usually not TP53 SNV.**
- **Evidence tier:** Mechanistic (requirement); Clinical-genomic (low CIC-DUX4 frequency).
- **Citation:** Specht 2016, PMID **27664537** (recurrent SNVs incl. TP53 not identified; Ewing-type CNAs
  not recurrent). Pan-sarcoma TP53 frequency for contrast: Lesluyes/Italiano MOSCATO-ProfiLER pooled
  analysis, *Cancers* 2021;13(13):3362, PMID **34209222** (~20%). `[no direct CIC-DUX4 TP53-mutation
  frequency that I could verify beyond "not recurrent"]`.

### Step C4 — Install replicative immortality (telomere maintenance: TERT or ALT)
- **Build action (forward):** stably maintain telomeres — reactivate telomerase (TERT) or engage ALT.
- **Mechanism:** replicative immortality is a required hallmark; without telomere maintenance, even a
  fully driver-loaded cell hits crisis. *Established (hallmark biology).*
- **CIC-DUX4-specific frequency:** **Genuinely unestablished.** **TERT promoter hotspot mutations are
  *rare* in soft-tissue sarcomas outside myxoid liposarcoma** (Koelsche et al.: 7/302 non-MLS sarcomas;
  confined to SFT, MPNST, SS — UPS/round-cell categories wild-type), so a *TERT-promoter-mutation* route
  is unlikely to be the CIC-DUX4 mechanism. Whether CIC-DUX4 cells maintain telomeres by **non-mutational
  TERT reactivation** (plausible — DUX4 is an embryonic/totipotency factor and could derepress telomerase
  programs) **or by ALT is not, to my verification, directly reported for CIC-DUX4.** This is the single
  biggest evidence gap among the required hits.
- **Evidence tier:** Established (the requirement); **Theoretical** (the specific CIC-DUX4 mechanism).
- **Citation:** Koelsche C et al., "TERT promoter hotspot mutations are recurrent in myxoid liposarcomas
  but rare in other soft tissue sarcoma entities," *J Exp Clin Cancer Res* 2014;33:33, PMID **24726063**.
  `[no direct citation for CIC-DUX4 telomere-maintenance mechanism — TERT-reactivation-vs-ALT is unknown]`.

### Step C5 — (Minor) recurrent broad copy-number context + ARID1A
- **1p loss** and **chr8 gain** are the recurrent broad CNAs (Specht 2016); a somatic **ARID1A R963X**
  nonsense mutation appeared **only in a local recurrence** in one case pair (Specht 2016) — i.e. a
  *progression*-associated, not initiating, event. Tier: Clinical-genomic (1p/8); Preclinical/anecdotal
  (ARID1A). Citation: PMID **27664537**. The 1p-loss target gene(s) are not resolved — candidate
  tumor-suppressor content on 1p is **inferred, not pinned**.

---

## Minimal cooperating genotype (synthesis)

Smallest set that, with CIC-DUX4 in a permissive mesenchymal progenitor, plausibly completes
transformation:

```
CIC-DUX4 fusion                       [given — driver]
  + SENESCENCE/APOPTOSIS BYPASS        ← CDKN2A/2B loss (primary, evidenced route)
                                          and/or p53-arm dampening (often via p14ARF loss, not TP53 SNV)
  + REPLICATION-STRESS SURVIVAL        ← intact WEE1/G2-M checkpoint + MCL-1 anti-apoptotic buffer
                                          (state, not a lesion) tolerating CCNE1/MYC stress
  + TELOMERE MAINTENANCE               ← TERT reactivation OR ALT  [mechanism UNKNOWN in CIC-DUX4]
  (+ MYC amplification / trisomy 8     ← strongly recurrent; accelerant, may be near-obligate)
```

**Most defensible minimal set:** `CIC-DUX4 + CDKN2A loss + telomere maintenance`, with MYC amplification
as a near-obligate accelerant and MCL-1/WEE1 dependence as required *survival states* rather than
discrete mutations. **Honest uncertainty:** (1) whether CDKN2A loss is *obligatory* vs *highly enriched*
in CIC-DUX4 is unverified (no clean frequency); (2) the telomere-maintenance mechanism is unknown;
(3) because CIC-DUX4 is mutationally quiet, several "hits" are **copy-number/expression states**, so the
genotype is better modeled as a *state vector* than a SNV checklist. **Atypical-case flag (~5%):** in
fusion-unconfirmed CIC-rearranged tumors the *driver* premise is uncertain, but the cooperating-state
logic (senescence bypass + immortalization + stress survival) is **fusion-agnostic** and still applies.

---

## Reverse-engineering note — which vector undoes each hit, and the gaps → forward hypotheses

| Cooperating hit | Undoing vector | How |
|---|---|---|
| CDKN2A/2B loss (no p16 → CDK4/6 unrestrained) | **V1 (rate-limiting)**, **V3 (hot-patching)** | Pharmacologic CDK4/6 inhibition *substitutes* for the deleted p16 brake — restoring the throttle the deletion removed. |
| p53-arm dampening (often via p14ARF loss) | **V3** | MDM2 inhibition (nutlin-class) reactivates residual wild-type p53 — directly counters p14ARF loss. |
| CCNE1/replication stress (buffered by WEE1) | **V1**, synthetic-lethality (V3) | WEE1 inhibition removes the G2/M buffer the cell built → mitotic catastrophe (the build's survival crutch becomes the kill switch). |
| MCL-1 anti-apoptotic buffer | **V3** (synthetic-lethality) | MCL-1 inhibition removes apoptosis buffering (Nat Commun 2025). |
| Telomere maintenance | **V1/V3** | Telomerase/ALT-pathway targeting — but mechanism unknown, so target is unspecified (see gap). |
| MHC-I-low immune evasion (separate, V4-owned) | **V4** | Epigenetic MHC-I re-priming. |

**GAPS → Forward Hypotheses (mechanistically defensible, not yet tested in CIC-DUX4):**

- **[Forward Hypothesis] FH-1 — Restore the senescence brake CDKN2A loss removed (MDM2/CDK4 axis).**
  Statement: in CDKN2A-deleted CIC-DUX4 cells, combined CDK4/6 inhibition (replaces p16) + MDM2 inhibition
  (replaces p14ARF, if TP53 WT) reconstitutes both arms of the deleted locus and re-imposes oncogene-
  induced senescence. Basis: the 9p21 locus encodes *both* p16 (CDK4/6→Rb) and p14ARF (MDM2→p53);
  deleting it removes both arms, so re-imposing both pharmacologically is the matched reversal. Test:
  CDK4/6i ± MDM2i in CDKN2A-deleted, TP53-WT CIC-DUX4 cell/tumoroid models; readout = SA-β-gal,
  p21/p16 axis, proliferation; falsified if no senescence induction in TP53-WT lines.

- **[Forward Hypothesis] FH-2 — Telomere-maintenance mechanism is the unmeasured load-bearing hit.**
  Statement: CIC-DUX4 tumors maintain telomeres by **non-mutational TERT reactivation driven by the
  DUX4 (embryonic/totipotency) transactivation program** rather than by TERT-promoter mutation or ALT.
  Basis: DUX4 normally activates an early-embryonic/cleavage-stage program (where telomerase is active);
  TERT-promoter hotspots are rare in non-MLS STS (Koelsche, PMID 24726063). Test: telomere-length +
  C-circle (ALT) assays + TERT expression/promoter genotyping across CIC-DUX4 lines/tumoroids; if
  TERT-high without promoter mutation and ALT-negative → supports DUX4-driven reactivation, predicting
  telomerase-inhibitor sensitivity. Falsified if ALT-positive or TERT-promoter-mutant.

- **[Forward Hypothesis] FH-3 — CDKN2A loss is an enabler of, not just a passenger with, the fusion.**
  Statement: introducing CIC-DUX4 into a CDKN2A-intact primary mesenchymal progenitor drives senescence,
  whereas CDKN2A co-deletion permits proliferation/immortalization — i.e. CDKN2A loss is the rate-limiting
  cooperating step. Test: ordered introduction (fusion ± CDKN2A knockout) in human mesenchymal stem cells;
  readout = senescence vs proliferation, colony formation; falsified if fusion alone immortalizes.

---

## Model parameters for the sim (discrete state variables + logic)

```python
# State variables (booleans unless noted)
fusion_present        : bool   # CIC-DUX4 (or rare variant) — the driver
cdkn2a_loss           : bool   # 9p21 p16/p14ARF homozygous loss/silencing
tp53_functional       : bool   # True = intact p53 stress arm
p14arf_loss           : bool   # usually == cdkn2a_loss (same locus); can dampen p53 indirectly
telomere_maintained   : bool   # TERT reactivation OR ALT  (mechanism unknown -> flag)
myc_amplified         : bool   # trisomy8 / MYC-locus amp (recurrent accelerant)
ccne1_high            : bool   # fusion-driven; raises replication stress
wee1_checkpoint_intact: bool   # G2/M buffer that lets cell survive ccne1 stress
mcl1_dependence       : bool   # anti-apoptotic buffer (emergent survival state)

# Derived logic
senescence_bypassed = cdkn2a_loss or (not tp53_functional) or p14arf_loss
replication_stress_survived = (not ccne1_high) or wee1_checkpoint_intact
apoptosis_buffered = mcl1_dependence or (not tp53_functional)

fully_transformed = (
    fusion_present
    and senescence_bypassed
    and telomere_maintained
    and replication_stress_survived
    and apoptosis_buffered
)
# myc_amplified: accelerant -> multiply proliferation_rate, not a hard gate (set as soft weight)

# Reverse-engineering (kill) rules — removing a built buffer:
#   CDK4/6i        -> emulates p16  -> if cdkn2a_loss: re-impose G1 brake
#   MDM2i          -> emulates p14ARF-> if tp53_functional: re-impose p53 arm
#   WEE1i          -> wee1_checkpoint_intact = False -> if ccne1_high: mitotic catastrophe
#   MCL1i          -> mcl1_dependence buffer removed -> apoptosis
#   telomerase/ALT -> telomere_maintained = False -> crisis  (target depends on FH-2 outcome)
```

Suggested defaults from evidence: `myc_amplified` true in the majority (≈6/7 cohort), `ccne1_high` true
(fusion-intrinsic), `tp53_functional` **usually true** (TP53 SNV not recurrent), `cdkn2a_loss` enriched
but frequency `[VERIFY]`, `telomere_maintained` true-by-requirement with **mechanism = UNKNOWN flag**.

---

## What I could not establish (mandatory)

1. **A clean CIC-DUX4-specific CDKN2A/2B homozygous-deletion frequency.** docs/02 says "frequent"; I found
   per-case NGS reports and pan-STS rates (~14–22%) but **no verifiable CIC-DUX4 cohort percentage.** Do
   not cite a number.
2. **Telomere-maintenance mechanism in CIC-DUX4 (TERT reactivation vs ALT).** Not reported in sources I
   could verify; TERT-promoter mutation is unlikely (rare in non-MLS STS). Largest gap.
3. **Whether any single cooperating hit is strictly obligatory vs strongly enriched.** No knockout/
   reconstitution ordering data in human mesenchymal cells that I could verify (FH-3 is untested).
4. **The 1p-loss target gene(s).** Recurrent event (Specht 2016) but the load-bearing tumor suppressor on
   1p is not pinned.
5. **TP53 exact frequency in CIC-DUX4** beyond "recurrent SNVs not identified / Ewing-type CNAs not
   recurrent" (Specht 2016, small cohort). PMC/Nature/Frontiers full texts were 403-blocked to WebFetch;
   numbers here come from verifiable search-indexed abstracts/snippets — treat full-text-only figures as
   `[VERIFY]` before external use.

## Falsifiers

- **If** CIC-DUX4 cohorts are shown to be **CDKN2A-intact at high frequency**, the "CDKN2A loss is the
  primary senescence-bypass route" claim (C1, FH-3) is wrong.
- **If** CIC-DUX4 lines are **ALT-positive (C-circle+) or TERT-promoter-mutant**, FH-2 (DUX4-driven
  non-mutational TERT reactivation) is falsified.
- **If** introducing CIC-DUX4 alone immortalizes primary human mesenchymal progenitors **without** any
  second hit, the entire "necessary-but-insufficient / minimal cooperating genotype" premise collapses.
- **If** TP53 mutation turns out **recurrent** (>30%) in larger CIC-DUX4 cohorts, C3's "function-required-
  but-gene-rarely-mutated" framing is wrong.
- **If** CDK4/6i + MDM2i fails to induce senescence in CDKN2A-deleted/TP53-WT CIC-DUX4 models, FH-1 is
  falsified.

---

### Verified citations used
- Specht K et al. *Hum Pathol* 2016;58:161-170. **PMID 27664537** (low TMB; recurrent 1p loss + chr8 gain;
  ARID1A R963X in recurrence; Ewing-type CNAs incl. TP53 del not recurrent).
- Yoshimoto M / Specht K et al. "CIC-DUX sarcomas demonstrate frequent MYC amplification and ETS-family
  transcription factor expression." *Mod Pathol* 2015;28(1):57-68. **PMID 24947144** (MYC amp 6/7,
  trisomy 8 5/7, MYC IHC 10/10).
- Antonescu CR et al. "Sarcomas With CIC-rearrangements... 115 Cases." *Am J Surg Pathol* 2017;41(7):
  941-949. **PMID 28346326** (entity definition, aggressive/chemoresistant — molecular % not extracted
  from full text here).
- "Small round cell sarcoma tumoroid biobank reveals CIC::DUX4 sarcoma vulnerability to MCL-1 inhibition."
  *Nat Commun* 2025. **PMID 40841360** (MCL-1 dependence).
- Koelsche C et al. *J Exp Clin Cancer Res* 2014;33:33. **PMID 24726063** (TERT-promoter mutations rare
  in non-MLS STS).
- Bui N et al. *Clin Sarcoma Res* 2019;9:12. **PMID 31528332** (CDKN2A loss frequency + prognosis, pan-STS).
- Lesluyes/Italiano et al. *Cancers* 2021;13(13):3362. **PMID 34209222** (TP53 ~20% pan-sarcoma; contrast).
- WEE1/CCNE1 replication-stress dependency: bioRxiv 2021.06.21.448439 **[VERIFY peer-reviewed version]**.

*Not medical advice. Research simulation, hypothesis generation only.*
