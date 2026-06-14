# V3 Synthetic-Lethality Specialist — Dependency Map for CIC-Rearranged Sarcoma (Clean-Slate v3)

**Covers:** four documented or hypothesized synthetic-lethal/dependency axes relevant to "hot-patching" a
cell that already carries (or may carry) the CIC-DUX4 fusion — BRD4/BET addiction, PRC2/EZH2 dependency in
BAF-disrupted contexts, CDK4/CCND1 dependency, and the MCL1 anti-apoptotic dependency identified directly
in CIC::DUX4 patient-derived tumoroids. For each, a clinical drug + (where one exists) a dietary modulator
with an honest cell-line-vs-dietary-plasma exposure-mismatch caveat. **Deliberately excludes:** ASO/PROTAC
pipeline detail (owned by the PROTAC/ASO specialist), differentiation-therapy mechanisms (owned by the
differentiation specialist), and the p300/CBP writer-level target (owned by the epigenetic-reprogramming
specialist and the build-recipe's FH-D — referenced here only where it intersects MHC-I/V4).

**Confidence: medium.** The BRD4, CDK4/CCND1, and MCL1 entries each rest on real CIC-DUX4 or close-proxy
(Ewing) data with named cell lines and concentrations; the EZH2/PRC2 entry is the weakest — it is
well-established in *other* BAF-disrupted fusion sarcomas (epithelioid sarcoma, synovial sarcoma) but
**not** demonstrated as a viability dependency in CIC-DUX4/Ewing by CRISPR. The MCL1 entry is the strongest
single mechanistic hit in this file but is **driver-contingent for this patient** (see below).

---

## 0. Driver-uncertainty framing (read first — ADR-0008)

This patient is in the **~5% fusion-unconfirmed atypical subgroup**. Per
`simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`, the driver is
modeled as a latent variable D1–D5. The load-bearing distinction for *this* file is whether the **DUX4
C-terminal transactivation domain** is present — true only under **D1** (cryptic/true CIC-DUX4, p≈0.45,
range 0.30–0.60) and partially under a rare DUX4-family variant of **D2** (p≈0.12). The applicability
matrix in that file scores:

| Dependency in this file | Gate | D1 | D2 | D3 | D4 | D5 |
|---|---|---|---|---|---|---|
| BRD4/BETi | ETS/super-enhancer program | 1 | 1 | 1 | 0.5 | 1 |
| CDK4/CCND1 (CDK4/6i) | cell-cycle execution | 1 | 1 | 1 | 1 | 1 |
| EZH2i (→ MHC-I priming, not viability) | PRC2/MHC-I-low epigenetic state | 1 | 1 | 0.5 | 0.5 | 0.5 |
| **MCL1i / "re-arm DUX4 death program"** | **DUX4 transactivation domain** | **1** | **0 (0.5 if DUX4-family)** | **0** | **0** | **0** |

**Translation for this file:** BRD4/BETi and CDK4/CCND1 entries below are **driver-robust** — they apply
across D1–D5 and are presented as standing candidates. The **MCL1 entry is driver-contingent** — it is
presented as a high-value forward direction **conditional on driver resolution**, not a committed
recommendation, with **resolving the driver** (nuclear DUX4 IHC first, per the EVSI ranking in the
driver-uncertainty file — cheap, fast, and directly licenses or excludes this entry) flagged as the
highest-value next diagnostic action wherever this dependency appears. EZH2i is presented per its
**already-established role as an MHC-I-priming agent (V3→V4 bridge)**, not a viability dependency — see
Section 2.

---

## 1. BRD4 / BET addiction

### Clinical drug: BET inhibitors (JQ1 [preclinical tool], OTX015/birabresib, AZD5153, BMS-986158)

**Mechanism:** BRD4 reads acetylated histone marks (H3K27ac) at the super-enhancers the CIC-DUX4 fusion
builds at ETV4/ETV5 and other ETS-target loci (via p300/CBP writing — Step 5 of the build recipe).
BET-bromodomain inhibitors displace BRD4 from these marks, collapsing the super-enhancer-driven
transcriptional output. In Ewing sarcoma (EWSR1-FLI1), JQ1 silences the EWS-ETS transcriptional program
[no direct citation; mechanism inferred from Ewing BETi literature, e.g. PMC4811472, PMC5029689].

**Evidence in CIC-DUX4 specifically?** **None direct for BETi sensitivity.** No published CIC-DUX4/CIC::DUX4
cell-line BETi (JQ1/OTX015/AZD5153) dose-response study was found in this search. The closest direct
CIC-DUX4 chromatin evidence is the p300/CBP chromatin-profiling paper (Bakaric et al., *Cancers*
2024;16(2):457, PMID 38275898, DOI 10.3390/cancers16020457; GSE248040), which demonstrates **p300-dependent**
H3K27ac deposition at CIC-DUX4 sites but does **not** test BRD4/BET inhibitors — that paper's actionable
target is p300/CBP (A-485, dCBP-1), owned by the epigenetic-reprogramming specialist, not BRD4 itself.

**DepMap CRISPR cross-check (Sim 2, Ewing proxy, n=27 lines):** **BRD4 is a universal CRISPR dependency
(mean Chronos −0.96, 100% of lines dependent) but is NOT selective (selectivity vs. all-lines = +0.01)**.
This is the single most important caveat for this entry: BRD4 essentiality is **not** a CIC/Ewing-specific
vulnerability — it is essential pan-cancer (and broadly pan-cell). This is consistent with the modest
monotherapy results BET inhibitors have shown clinically (narrow therapeutic window — hits tumor and
normal proliferating tissue together).

**Tier:** Preclinical-Cell (Ewing proxy; BRD4 essentiality is real but non-selective) / **Theoretical** for
any CIC-DUX4-*selective* claim. The "BRD4 addiction" framing is more accurately "BRD4 is essential, like
almost everywhere else" — synthetic-lethal framing would require a CIC-DUX4-selective vulnerability that
the CRISPR data do not show.

**Driver-contingency:** Driver-robust (applies D1–D5 per the matrix above) — the ETS/super-enhancer program
is present whenever ETV4/5 derepression occurs, which is the shared logic across D1–D3 and D5.

**Dietary modulator: EGCG (green tea catechin)**

- **Mechanism:** EGCG has been reported to bind the BRD4 BD1 bromodomain directly in cell-free/biochemical
  assays and to reduce H3K27ac at target loci in cell-line studies [no direct citation; mechanism inferred
  from the general EGCG-BRD4 literature cited in the V1/V3 compound tables — `sarcoma-vector-context v1`
  reports this as Preclinical-Cell with poor bioavailability].
- **Exposure-mismatch caveat (HONEST):** Cell-line BRD4-binding/H3K27ac effects for EGCG are reported in
  the **low-to-mid micromolar range (typically 10–50 µM)**. Achievable human plasma EGCG concentrations
  after a cup of green tea are in the **0.1–1 µM range** (oral bioavailability of EGCG is poor — extensive
  first-pass methylation/glucuronidation). This is a **10–100× gap** between the cell-line-active
  concentration and dietary-achievable plasma levels. Given that even the *clinical* BET inhibitors show
  only modest monotherapy activity at full pharmacologic exposure, and BRD4 is a *non-selective* dependency
  (above), EGCG at dietary intake should be regarded as **mechanistically plausible at best, not a
  meaningful BRD4-blocking intervention**.
- **Chemo screening (quercetin/EGCG-class polyphenols, per `sarcoma-chemo-interactions`):** EGCG — CYP3A4:
  modulator at higher concentrations (in vitro) [no direct citation beyond general polyphenol-CYP3A4
  literature] | P-gp: reported modulator in cell-line transport assays | ROS-axis: EGCG itself is a
  pro-oxidant at high concentration in some assays — theoretical interaction with doxorubicin/ifosfamide
  ROS mechanism, clinical relevance unestablished | Other: ifosfamide is currently in active use for this
  patient (May 2026 oligometastatic relapse) — any polyphenol with CYP3A4/P-gp activity should be flagged
  for oncologist awareness even at dietary intake, though dietary-level exposure is far below the
  concentrations in the interaction studies. Citation: general class flag, not compound-specific human
  data — `not screened beyond in vitro/animal PK literature`.

---

## 2. PRC2 / EZH2 dependency in BAF-disrupted contexts

**Clinical drug: tazemetostat (EZH2 inhibitor)**

**Mechanism:** PRC2 (core catalytic subunit EZH2) deposits the repressive mark H3K27me3. In cancers where
the BAF (SWI/SNF) chromatin-remodeling complex is disrupted — classically **SMARCB1 loss** in epithelioid
sarcoma and malignant rhabdoid tumor, and **SS18-SSX-mediated SMARCB1 displacement** in synovial sarcoma —
normal BAF activity no longer evicts PRC2 from tumor-suppressor loci, creating a **synthetic-lethal
dependency on EZH2** (BAF loss ⇄ PRC2 dependency is a well-described epigenetic-antagonism relationship).
Tazemetostat (EZH2 inhibitor) was developed against exactly this dependency.

**Evidence in CIC-DUX4 specifically?**

- **There is NO documented SMARCB1 loss in CIC-DUX4.** The classical PRC2/BAF synthetic-lethality
  rationale (epithelioid sarcoma, MRT, synovial sarcoma) does **not** transfer directly via the SMARCB1
  mechanism.
- **However**, a real CIC-DUX4-specific BAF-complex lesion **was found in this session's literature
  search**: the 2025 Nat Commun CIC::DUX4 tumoroid papers report **recurrent ARID1A frameshift/truncating
  mutations** in CIC::DUX4 sarcoma models ("two of the CDS models contained frameshift mutations in ARID1A,
  as already described for individual cases, suggesting that this is indeed a common mutation in CDS" —
  Patient-derived tumoroids from CIC::DUX4 rearranged sarcoma identify MCL1 as a therapeutic target, *Nat
  Commun* 2025, PMID 40841513, DOI 10.1038/s41467-025-62629-6). ARID1A is a **cBAF-specific subunit**;
  truncating mutations cause loss of cBAF assembly. This is mechanistically the **same class** of lesion
  (cBAF disruption) that drives PRC2/EZH2 dependency elsewhere — but **the paper that reports the ARID1A
  mutations is the MCL1 paper, and it does not report EZH2/PRC2 dependency or test an EZH2 inhibitor** in
  these models. The mechanistic bridge (ARID1A loss → EZH2 dependency) is therefore **inferred by
  analogy, not demonstrated in CIC-DUX4**.
- **DepMap CRISPR cross-check (Sim 2, Ewing proxy, n=27 lines): EZH2 is NOT a viability dependency** (mean
  Chronos +0.01, 0% of lines dependent, selectivity +0.10). This directly **argues against** an EZH2
  *survival*-dependency framing in this fusion-sarcoma family, ARID1A status notwithstanding (the Ewing
  proxy lines were not selected for ARID1A status, so this does not specifically rule out an
  ARID1A-mutant-selective effect — but it removes EZH2 as a "synthetic lethal kill" candidate by default).

**Reframe — this is a V3→V4 bridge entry, not a synthetic-lethality kill.** Per the V3 vector context,
EZH2 inhibition (and HDAC inhibition) is the cleanest documented route to **MHC-I restoration** —
p300/CBP collapse (the CIC-DUX4-specific writer-level target, Bakaric 2024) "restores MHC-I" per the
build-recipe's Step 5 citation (*Mol Cancer* 2025, DOI 10.1186/s12943-025-02485-6, PMC12659477, PMID
[VERIFY]). **EZH2i's value proposition in CIC-DUX4 is therefore MHC-I priming for V4 immune visibility,
not tumor-cell killing via synthetic lethality** — the epigenetic-reprogramming specialist owns the full
MHC-I case; this file flags it because the "PRC2/EZH2 dependency" framing in the prompt could otherwise
be mis-cited as a viability claim it is not.

**Tier:** Established (tazemetostat, SMARCB1-deficient epithelioid sarcoma — FDA-approved 2020-01-23,
**[VERIFY live — perishable; CLAUDE.md notes tazemetostat was withdrawn from all US indications
2026-03-09]**) / Clinical-Trial (other PRC2-dependent fusion sarcomas) / **Theoretical** for CIC-DUX4
viability dependency (DepMap argues against it) / Mechanistic for the ARID1A→EZH2 bridge (inferred, not
shown).

**[VERIFY — perishable, this session]:** Per CLAUDE.md's standing note, tazemetostat's US regulatory status
changed materially (withdrawal from all US indications, dated 2026-03-09) since the original tazemetostat
approval was recorded. **This entry does not re-verify that status live** (out of scope for a
synthetic-lethality dependency map — the feasibility layer owns regulatory status) but flags it so the
orchestrator does not carry a stale "Established/FDA-approved" claim forward without checking
`simulation-output/translational-feasibility-layer.md` for the current band.

**Driver-contingency:** Driver-robust for the MHC-I-priming role (applies D1, D2, partial D3–D5 per the
matrix). The ARID1A-mutation-based mechanistic bridge is **D1/D2-leaning** (reported specifically in
CIC::DUX4 tumoroids) but ARID1A/1p-loss is also a recurrent CIC-rearranged-sarcoma-cohort finding more
broadly (Specht 2016, PMID 27664537), so it is not strictly DUX4-transactivation-domain-gated the way MCL1
is.

**Dietary modulator: EGCG / quercetin (weak EZH2 modulators in cell lines)**

- **Mechanism:** Both compounds have been reported as weak EZH2/H3K27me3 modulators in cell-line systems
  [Preclinical-Cell, per `sarcoma-vector-context v3`'s "EZH2 modulation (weak)" row].
- **Exposure-mismatch caveat:** As above for EGCG — dietary plasma levels are 10–100× below cell-line
  active concentrations. Given that EZH2's role here is reframed as MHC-I priming (a transcriptional,
  not viability, endpoint), and even the *clinical* EZH2 inhibitor's translation to CIC-DUX4 is unproven,
  dietary EZH2 modulation should be treated as **far below any plausible threshold for tumor-relevant
  MHC-I change** — Mechanistic at best, **unestablished** whether dietary exposure achieves any effect.
- **Chemo screening:** Quercetin — CYP3A4: documented inhibitor, IC50 ≈ 1.97 µM in vitro (concentration-
  dependent; PubMed/PMC PK studies cited below) | P-gp: documented inhibitor — increases etoposide oral
  bioavailability from ~8.9% to ~12.7–13.6% and doxorubicin bioavailability in rat PK studies (Archives of
  Pharmacal Research 2011, PMID 21544726; Anticancer Res 2009, PMID 19414395) | ROS-axis: quercetin is
  itself a redox-active polyphenol — theoretical bidirectional interaction with doxorubicin/ifosfamide ROS
  mechanism, clinical significance in humans at dietary intake **not established** | Other: **given this
  patient is currently on high-dose ifosfamide (CYP3A4-activated prodrug) and the SOC regimen includes
  etoposide and doxorubicin (both CYP3A4/P-gp substrates), any quercetin-containing supplement (as opposed
  to whole-food intake) should be flagged for oncologist awareness** — the rat PK data show real
  bioavailability shifts for structurally analogous chemo agents, even though dietary-food-level quercetin
  exposure is far below supplement-bolus levels used in those studies.

---

## 3. CDK4 / CCND1 dependency

**Clinical drug: CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib)**

**Mechanism:** CDK4 (paired with a D-type cyclin) phosphorylates and inactivates Rb, releasing E2F-driven
S-phase entry. CDK4/6 inhibitors block this phosphorylation, re-imposing a G1 arrest analogous to the
CDKN2A/p16 brake the build recipe identifies as lost in most CIC-DUX4 tumors (Step 4 of the build recipe).

**Evidence in CIC-DUX4 specifically?**

- **DepMap CRISPR cross-check (Sim 2, Ewing proxy, n=27 lines): CDK4 is the single most Ewing-selective
  CRISPR dependency in the panel** (mean Chronos −1.53, selectivity vs. all-lines −0.77, 89% of lines
  dependent). **CCND1 is also strong and selective** (mean −1.47, selectivity −0.49, 89% dependent). This
  is the **strongest, most selective dependency signal in the entire dependency-mining sim** — stronger
  and more selective than BRD4 or WEE1.
- **Important correction (Sim 2): CDK6 is NOT a dependency** (mean −0.05, selectivity +0.54, 0% dependent)
  and **CCND2 is NOT a CRISPR dependency** (mean −0.03, 0% dependent) **despite CCND2 being the
  CIC-DUX4-specific transcriptionally-upregulated cyclin** — in mouse CIC-DUX4-induced round-cell sarcoma
  models, **Ccnd2** (not Ccnd1) is the top upregulated D-type cyclin, directly regulated by ETV4/PEA3
  family transcription factors (Yoshimoto et al., *Cancer Res* 2017;77(11):2927-37, PMID 28404587). The
  DepMap *dependency* signal (CCND1, in Ewing) and the CIC-DUX4 *transcriptional upregulation* signal
  (CCND2, in mouse CDS) point at **different cyclin D paralogs** — CCND2 can functionally substitute for
  CCND1 in driving CDK4 activity, so a CDK4/6 inhibitor's relevant target (CDK4 itself) is likely shared
  even if the upstream cyclin differs. **Refines "CDK4/6i" to specifically "CDK4i"** — CDK6 inhibition is
  not expected to contribute.
- **Direct in vivo CIC-DUX4 data exist and show a mixed result**: palbociclib **inhibited CDS (CIC-DUX4
  small round cell sarcoma) growth in vitro, but showed only limited effect on tumor growth in vivo**
  [Preclinical-Cell positive / Preclinical-Animal negative-to-modest — search result citing CDS xenograft
  palbociclib data; exact PMID not independently re-confirmed in this session, flag **[VERIFY]**]. This is
  an **honest negative-leaning signal**: a strong, selective CRISPR dependency (CDK4, in the Ewing proxy)
  did not translate to robust in vivo monotherapy efficacy in a CIC-DUX4 model — consistent with the
  general pattern that CRISPR essentiality does not guarantee therapeutic window or monotherapy
  sufficiency.

**Tier:** Established (palbociclib/ribociclib/abemaciclib, FDA-approved HR+/HER2− breast cancer —
**[VERIFY live]**) / Clinical-Trial (sarcoma — Phase II palbociclib trial stratified by CDK4/CDKN2A mRNA
expression in advanced sarcoma, *Signal Transduct Target Ther* 2023, PMC10598203 — not CIC-DUX4-specific)
/ Preclinical-Cell (strong, selective CRISPR dependency in Ewing proxy) / Preclinical-Animal (CIC-DUX4
xenograft — **limited in vivo effect**, honest caveat above).

**Driver-contingency:** **Driver-robust** — scores `1` across **all** D1–D5 in the applicability matrix.
Cell-cycle execution via CDK4 is downstream of ETS derepression broadly, not specifically gated on the
DUX4 transactivation domain. This is one of the safer entries to carry forward regardless of driver
resolution.

**Connection to WEE1/ifosfamide convergence (flagged per prompt, not duplicated from Sim 3):** The
cooperating-lesions brief and Sim 3 identify **CCNE1-driven replication stress, buffered by an intact
WEE1/G2-M checkpoint**, as a CIC-DUX4 survival state — WEE1 inhibition (adavosertib) + ifosfamide is the
combination Sim 3 found "robustly collapses viability." **CDK4 and CCNE1-CDK2 are mechanistically distinct
nodes** (CDK4/Rb = G1/S entry brake; CCNE1/CDK2 = G1/S→S replication-stress driver), but both converge on
the same G1/S transition the fusion deregulates. A separate, real CIC-DUX4-specific finding (JCI
2019;129(10):4233-4255 — "CIC-DUX4 oncoprotein drives sarcoma metastasis and tumorigenesis via distinct
regulatory programs," PMID **[VERIFY — not independently confirmed this session]**) reports CIC-DUX4
tumors show molecular dependence on the **CCNE1-CDK2 complex**, with CDK2 inhibition (dinaciclib)
showing efficacy in CIC-DUX4 xenografts at 20 mg/kg/d (low-dose). **This means there may be two
independent, convergent G1/S-axis vulnerabilities** (CDK4/CCND-axis from this entry, and CCNE1/CDK2-axis
from the JCI paper) **plus the downstream WEE1/ifosfamide replication-stress vulnerability from Sim 3** —
all three sit on the same pathway logic (G1/S deregulation → replication stress → G2/M checkpoint
dependence) but target different nodes. **This file does not duplicate Sim 3's analysis; it flags that a
CDK4i and a CDK2i (dinaciclib) and WEE1i+ifosfamide are mechanistically related but non-identical
hypotheses worth distinguishing in any future combination-design discussion.**

**Dietary modulator: Fisetin and Genistein**

- **Mechanism:** Per the V1 vector context, fisetin is reported to suppress CDK4 in cell-line studies
  (also has independent senolytic literature); genistein has reported CDK-inhibitory and G2/M-arrest
  activity in cell lines.
- **Exposure-mismatch caveat:** Both are Preclinical-Cell findings at concentrations in the
  **low-to-mid-micromolar range**, while dietary fisetin (from strawberries, apples, persimmons) and
  genistein (soy isoflavone) achieve **plasma concentrations in the nanomolar-to-low-micromolar range at
  best**, and fisetin/genistein undergo extensive glucuronidation/sulfation — circulating "genistein"
  after soy intake is overwhelmingly conjugated metabolites, not free aglycone. **The CDK4 dependency
  signal in this file (Chronos −1.53, the strongest in the panel) is a genuine, selective finding — but
  there is no evidence that dietary fisetin/genistein intake reaches a concentration that meaningfully
  engages this target.** This is a case where the *target* is well-validated but the *dietary lever* is
  almost certainly too weak — be explicit that this gap is about achievable concentration, not about the
  target's validity.
- **Chemo screening:** Genistein — CYP3A4: weak modulator reported in vitro [no direct citation beyond
  general isoflavone-CYP literature] | P-gp: reported weak modulator | ROS-axis: genistein has both
  pro- and antioxidant reports depending on concentration; **genistein also has estrogenic activity**
  (per V1 vector context) — not a chemo-axis interaction per se, but a separate caveat for a sarcoma
  patient on no stated hormonal therapy, flagged for completeness, not urgency | Fisetin — not screened
  beyond the V1 entry; no specific CYP3A4/P-gp dietary-dose human data found in this session.

---

## 4. MCL1 anti-apoptotic dependency (driver-contingent — hold until driver resolved)

**Clinical drug class: MCL1 inhibitors / BH3 mimetics (S63845, S64315/MIK665 — clinical-stage derivative)**

**Mechanism:** The CIC::DUX4 fusion's retained DUX4 C-terminal transactivation domain drives an
embryonic/totipotency-like transcriptional program (the "FSHD death program" in DUX4 biology) that is
intrinsically pro-apoptotic. **CIC::DUX4 directly transactivates MCL1** — ChIP-seq identifies CIC::DUX4
binding peaks in/near the MCL1 locus with high H3K27ac (active-enhancer mark), and CRISPR-interference
experiments at this element reduce MCL1 expression. The tumor cell is therefore **chronically dependent on
MCL1 to buffer a death program its own driver is actively running** — removing MCL1 "re-arms" that
program. This is the build-recipe's Step 3 / FH-A: a *non-substitutable* construction debt (Sim 7: this
buffer cannot be replaced by TP53 loss, because the DUX4 death program is largely p53-independent).

**Evidence in CIC-DUX4 specifically? — Direct, and unusually strong for this catalog.** Two **separate**,
real 2025 *Nature Communications* papers (not a PMID-discrepancy — both exist independently, resolving the
`[VERIFY]` flag the build-recipe carried):

1. **PMID 40841513**, DOI 10.1038/s41467-025-62629-6, "Patient-derived tumoroids from CIC::DUX4 rearranged
   sarcoma identify MCL1 as a therapeutic target" (*Nat Commun* 2025; PMC12370961). Reports:
   - MCL1 inhibitor **S63845**: IC50 in the **1–10 nM range in the most sensitive CIC::DUX4 tumoroid
     models** — i.e., a genuinely potent, low-nanomolar effect, not a high-micromolar cell-line artifact.
   - Clinical-derivative **S64315** tested at 10–50 nM in flow-cytometry apoptosis assays.
   - **In vivo**: S64315 at **20 mg/kg twice weekly for three weeks produced significant tumor regression
     and prolonged survival in a CIC::DUX4 xenograft model.**
   - **BET inhibitors were identified as top synergy hits with S64315** in a drug-screening library —
     i.e., the BRD4 entry (Section 1) and this MCL1 entry may be **combinable**, though neither alone is
     established as CIC-DUX4-selective-and-sufficient.
   - **ARID1A frameshift mutations** were found recurrently in these CIC::DUX4 tumoroid models (flagged
     in Section 2).
2. **PMID 40841360**, DOI 10.1038/s41467-025-62673-2, "Small round cell sarcoma tumoroid biobank reveals
   CIC::DUX4 sarcoma vulnerability to MCL-1 inhibition" (*Nat Commun* 2025). A biobank-scale companion
   study (cited by the cooperating-lesions specialist) reporting **selective** MCL1 dependence in
   CIC::DUX4 tumoroids within a broader small-round-cell-sarcoma biobank (which also includes Ewing
   sarcoma models) — i.e., the dependency is reported as **CIC::DUX4-selective within the biobank**, not
   shared pan-round-cell-sarcoma. This is the strongest evidence that the dependency is **driver
   (DUX4-transactivation-domain)-specific** rather than a generic small-round-cell-sarcoma feature, though
   this file has not independently re-verified the head-to-head selectivity comparison beyond the
   abstract-level description available.

**Tier:** **Preclinical-Cell (potent, low-nanomolar) + Preclinical-Animal (xenograft regression)** — this is
the **highest-tier direct CIC-DUX4 evidence in this entire file**, well above the Mechanistic/Theoretical
tier most synthetic-lethality entries carry. No clinical-trial data in CIC-DUX4 exist; S64315/MIK665 has
been in early-phase clinical development for hematologic malignancies more broadly — **CIC-DUX4-specific
trial status [VERIFY — out of scope for this dependency map; defer to feasibility layer if/when this entry
is carried forward]**.

---

### >>> DRIVER-CONTINGENCY — READ BEFORE USING THIS ENTRY <<<

**This entry is HOLD-UNTIL-DRIVER-RESOLVED for this patient, not a committed recommendation.**

The mechanism above is **entirely dependent on the DUX4 C-terminal transactivation domain being expressed**
— that domain is what (a) drives the pro-apoptotic embryonic program and (b) directly transactivates MCL1
via the CIC::DUX4 fusion's chromatin binding. Per the driver-uncertainty applicability matrix:

- **D1 (cryptic/true CIC-DUX4, p≈0.45)**: applies (score 1).
- **D2 (rare CIC partner, p≈0.12)**: applies only if the rare partner is itself DUX4-family (e.g.
  ATXN1::DUX4, PMID 35715887) — score 0.5; **does not apply** for non-DUX4-family CIC partners (NUTM1,
  FOXO4, LEUTX, NUTM2A) — score 0.
- **D3 (non-fusion CIC LOF, p≈0.10), D4 (phenocopy, p≈0.20), D5 (orphan, p≈0.13)**: score **0** — no DUX4
  transactivation domain, no mechanistic basis for MCL1 transactivation by this route, no basis for "re-arm
  the DUX4 death program."

**For this fusion-unconfirmed patient, the prior-weighted probability this entry applies is roughly the
D1 + (0.5 × DUX4-family-D2) mass — i.e., on the order of ~45-50% under the default prior**, not a
near-certainty. **This is presented as the single highest-value forward direction *if* the driver resolves
to D1 (or DUX4-family D2)** — not as a current recommendation.

**Highest-value next action:** Per the driver-uncertainty file's EVSI ranking, **nuclear DUX4 IHC** is the
cheapest, fastest test that **directly resolves the gating question for this entry** — a positive result
strongly implicates D1 and **directly licenses** this MCL1 line of inquiry (and the broader DUX4/junction-
dependent lines); a negative result takes this entry **off the table** for this patient. Long-read
WGS+RNA-seq (resolves D1 vs D2 vs D3, recovers cryptic junctions) and genome-wide methylation array
(collapses D4) are the next-tier tests if DUX4 IHC is ambiguous or positive and partner identity matters.
**This file does not re-derive the EVSI ranking** — see
`simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md` and
`simulation-output/diagnostic-information-gain-layer.md` for the full sequencing logic.

---

**Dietary modulator: Quercetin (reported Mcl-1-downregulating / BH3-mimetic flavonoid)**

- **Mechanism:** Quercetin has been reported (a) to **downregulate Mcl-1 via effects on mRNA stability and
  protein degradation** in tumor-cell studies (Clin Cancer Res 2010;16(23):5679, PMC3142809/PMC3069720 —
  "Quercetin Induces Tumor-Selective Apoptosis through Downregulation of Mcl-1 and Activation of Bax"), and
  (b) to exhibit **direct BH3-mimetic activity**, binding the BH3-domain groove of anti-apoptotic BCL2-family
  proteins in biophysical (NMR/docking) studies in leukemic (Jurkat/CLL) cells (ASH/Blood abstract,
  "Decoding the BH3-Mimetic Pro-Apoptotic Activity of Quercetin in Jurkat Cells"). Mechanistically, this is
  the **same node** (MCL1/BCL2-family anti-apoptotic buffering) as the clinical MCL1 inhibitors above —
  quercetin is, at least directionally, a much weaker, less selective, orally-available analog of the same
  idea.
- **Evidence in CIC-DUX4 specifically?** None direct — the quercetin-Mcl-1 literature is in other tumor
  types (the cited studies are not sarcoma).
- **Exposure-mismatch caveat (HONEST, this is the most important caveat in this file):** The clinical MCL1
  inhibitor S63845 achieves its CIC::DUX4-tumoroid effect at **1–10 nM**. Quercetin's Mcl-1-downregulation
  and BH3-mimetic effects in the cited cell studies are reported at concentrations in the
  **low-to-mid-micromolar range (typically 10–50 µM)** — i.e., **roughly 1,000-to-10,000-fold higher** than
  the clinical inhibitor's effective concentration, while achievable dietary quercetin plasma levels are
  in the **sub-micromolar-to-low-micromolar range** (and quercetin is extensively glucuronidated/sulfated
  — circulating quercetin aglycone is a small fraction of total). **This is the largest potency gap of any
  comparison in this file.** Quercetin's BH3-mimetic/MCL1-modulating activity should be regarded as
  **mechanistically interesting and directionally consistent with the same vulnerability the clinical
  MCL1 inhibitors exploit, but many orders of magnitude too weak at dietary exposure to be expected to
  "re-arm the DUX4 death program" in any meaningful sense.** If the driver resolves favorably (D1/DUX4-
  family-D2) and this dependency is pursued, **it is a clinical-pharmacology question (MCL1i/BH3-mimetic
  drug development), not a dietary one** — this file's job is to be honest that the dietary lever here is
  essentially negligible relative to the clinical one, even though the underlying biological node
  (MCL1/BCL2-family buffering) is shared.
- **Chemo screening:** Quercetin's CYP3A4/P-gp interaction profile is detailed in Section 2 above (IC50
  ≈1.97 µM for CYP3A4 inhibition; documented etoposide/doxorubicin bioavailability effects in rat PK
  studies). The same flag applies here: **if this dependency is ever pursued pharmacologically, it would
  be via a clinical BH3-mimetic, not quercetin supplementation** — so the chemo-interaction question is
  largely moot for this specific dietary entry, but is recorded for completeness since quercetin appears
  in multiple entries in this file.

---

## What I Could Not Establish

1. **BETi sensitivity has no direct CIC-DUX4 dose-response data.** The closest CIC-DUX4 chromatin paper
   (Bakaric 2024) targets p300/CBP, not BRD4 directly. The "BRD4 addiction" framing from the prompt is
   better supported as "BRD4 is essential like almost everywhere" (DepMap: non-selective) than as a
   CIC-DUX4-*selective* synthetic lethality. I could not find a published CIC-DUX4 JQ1/OTX015/AZD5153
   IC50.
2. **The EZH2/PRC2-BAF "dependency" framing from the prompt does not hold as a viability claim in
   CIC-DUX4** — DepMap shows EZH2 is not a CRISPR dependency in the Ewing proxy (+0.01, 0% dependent). I
   reframed this entry around the ARID1A-mutation finding (real, CIC::DUX4-specific, from the 2025 Nat
   Commun MCL1 paper) and the established MHC-I-priming role, but the **ARID1A→EZH2-dependency mechanistic
   bridge is inferred by analogy to SMARCB1-deficient sarcomas, not demonstrated in CIC-DUX4.** This is a
   gap a future specialist could test directly (EZH2i dose-response in ARID1A-mutant CIC::DUX4 tumoroids,
   if/when such lines become available with CRISPR or drug-screen data).
3. **The palbociclib CIC-DUX4 in vivo "limited effect" claim** — found via web search summary, not
   independently read in the primary source this session. **[VERIFY]** before citing further; flagged
   honestly as a negative-leaning signal rather than omitted.
4. **The CCNE1-CDK2/dinaciclib JCI paper's exact PMID** was not independently confirmed this session
   (search results described the finding and cited "JCI 2019;129(10):4233-4255" framing but I did not
   open the primary record to extract/verify the PMID). **[VERIFY]** before external use.
5. **No CIC-DUX4-specific CRISPR screen data exists** (confirmed via Sim 2: TE441T, NCC-CDS1-X1-C1,
   NCC-CDS1-X3-C1, NCC-CDS2-C1 are registered patient-derived/Cellosaurus lines but **none have DepMap
   CRISPR data**). All CRISPR-based dependency claims in this file are via the **Ewing sarcoma proxy
   (n=27 lines)** — mechanistically plausible (shared fusion-driven ETS/super-enhancer biology) but
   **unproven for CIC-DUX4**. This is the single biggest structural limitation of the dependency-based
   entries (BRD4, CDK4/CCND1, EZH2); the **MCL1 entry is the exception** — it has direct CIC::DUX4
   tumoroid + xenograft data, not proxy data.
6. **Whether the MCL1 dependency reported in PMID 40841360's biobank is truly CIC::DUX4-*selective* vs.
   shared with the biobank's Ewing models** was not independently verified beyond the title/abstract-level
   framing ("CIC::DUX4 sarcoma vulnerability") — if MCL1 dependence turned out to be pan-small-round-cell-
   sarcoma rather than DUX4-transactivation-domain-specific, the driver-contingency argument in Section 4
   would need softening (the dependency might be present even without the DUX4 domain, via a different
   route). The ChIP-seq direct-transactivation evidence in PMID 40841513 is the stronger argument for
   driver-specificity and is what this file leans on.
7. **No dietary modulator was identified for the BRD4/CDK4 dependency that has any plausible chance of
   reaching an active concentration** — EGCG/fisetin/genistein are all flagged with order-of-magnitude
   exposure gaps. This file does not pretend otherwise.

---

## Forward Hypotheses

- **[Forward Hypothesis] FH-SL1 — BET inhibitor + MCL1 inhibitor combination as a driver-contingent,
  two-hit "construction debt" attack.** *Statement:* In driver-confirmed (D1/DUX4-family-D2) CIC::DUX4
  cells, combining a BET inhibitor (collapsing the p300/BRD4-built super-enhancer state that sustains ETS
  output and proliferative drive) with an MCL1 inhibitor (removing the anti-apoptotic buffer the same
  fusion's DUX4 domain forced the cell to install) would act on **two independent, non-redundant
  "construction debts"** (Step 5 amplification + Step 3 apoptosis buffer from the build recipe)
  simultaneously — potentially achieving durable response where either alone gives only transient
  arrest or apoptosis-with-resistance. *Mechanistic basis:* the 2025 Nat Commun MCL1 paper (PMID 40841513)
  already identified **BET inhibitors as the top synergy hits with the MCL1 inhibitor S64315** in its
  drug-screening library — this hypothesis extends that finding into an explicit "two construction debts"
  framing and proposes testing whether the combination produces **durable** (not just additive-acute)
  responses, and whether resistance that emerges to either single agent remains sensitive to the
  combination. *Experiment:* in CIC::DUX4 tumoroids/xenografts (the same models used in PMID 40841513),
  compare (a) BETi monotherapy, (b) MCL1i monotherapy, (c) combination, at matched sub-maximal doses, with
  long-term (weeks, not days) regrowth/resistance readouts and RNA-seq to check whether BETi-driven
  super-enhancer collapse *reduces* MCL1 transactivation (testing whether the two debts are themselves
  coupled). *Falsifier:* if BETi treatment does not reduce MCL1 expression/dependency, and the combination
  shows no benefit over the better single agent in durable-response assays, the "two independent debts"
  framing is wrong and the synergy is acute/additive only (still useful, but a weaker claim). *Why not yet
  tested:* the acute synergy screen exists (2025), but durable-response/resistance data and the
  mechanistic-coupling question (does BETi reduce MCL1 transactivation?) were not reported in the sources
  reviewed this session.

- **[Forward Hypothesis] FH-SL2 — ARID1A-mutant status as a patient-selectable biomarker for an
  EZH2i-as-MHC-I-primer strategy, independent of the MCL1/driver question.** *Statement:* If this
  patient's tumor is found to carry an **ARID1A loss-of-function mutation** (frameshift/truncating, as
  recurrently reported in CIC::DUX4 tumoroids, PMID 40841513) — a finding that, unlike the MCL1/DUX4-domain
  question, is **not strictly gated on D1 vs D2 vs D3-D5** (ARID1A/1p-loss is a recurrent finding across
  CIC-rearranged cohorts more broadly per Specht 2016, PMID 27664537) — this could serve as an independent,
  **driver-uncertainty-robust** biomarker supporting the EZH2i-for-MHC-I-priming rationale (Section 2),
  via the cBAF-disruption → PRC2-dominance mechanism documented in SMARCB1-deficient sarcomas, applied
  here via ARID1A instead of SMARCB1. *Mechanistic basis:* cBAF and PRC2 are in epigenetic antagonism at
  shared loci (BAF evicts PRC2; BAF loss → PRC2 dominance); ARID1A truncation causes cBAF-assembly failure,
  mechanistically analogous (though not identical in subunit) to SMARCB1 loss. *Experiment:* (1) test
  whether ARID1A-mutant CIC::DUX4 tumoroids show **greater EZH2i-induced MHC-I/H3K27me3 change** than
  ARID1A-WT tumoroids (if any ARID1A-WT CIC::DUX4 models exist for comparison); (2) if this patient's
  archived tissue (P1, per ADR-0011 provenance framing) already has NGS data, check ARID1A status as a
  near-zero-additional-cost readout. *Falsifier:* if EZH2i-induced MHC-I/H3K27me3 changes are equivalent
  in ARID1A-mutant vs. ARID1A-WT CIC::DUX4 models, ARID1A status is not a useful stratifier for this
  mechanism and the SMARCB1-analogy does not transfer via ARID1A. *Why not yet tested:* the ARID1A finding
  in CIC::DUX4 tumoroids is from a 2025 paper whose primary focus was MCL1, not EZH2/MHC-I — the
  cross-connection to the V3→V4 MHC-I bridge has not, to this file's knowledge, been explicitly drawn or
  tested before.

---

## Atypical-Case / Driver-Uncertainty Summary

| Entry | Driver-contingent? | Applies to ~5% fusion-unconfirmed (D3-D5)? |
|---|---|---|
| BRD4/BETi (Section 1) | No — driver-robust (D1-D5: 1,1,1,0.5,1) | Yes (partial under D4) |
| EZH2i / MHC-I priming (Section 2) | No — driver-robust for MHC-I role (D1-D5: 1,1,0.5,0.5,0.5) | Yes (partial under D3-D5) |
| ARID1A-bridge (FH-SL2) | Largely no — ARID1A/1p-loss reported across CIC cohorts broadly | Likely yes, but unconfirmed-driver tumors' ARID1A status is itself unknown without sequencing |
| CDK4/CCND1 (Section 3) | **No — fully driver-robust** (D1-D5: 1,1,1,1,1) | **Yes, fully** |
| **MCL1 (Section 4)** | **YES — gated on DUX4 transactivation domain** (D1-D5: 1, 0/0.5, 0, 0, 0) | **NO for D3-D5; HOLD pending DUX4 IHC** |

**Bottom line for this patient:** of the four dependencies in this file, **CDK4/CCND1 is the only one that
is fully driver-agnostic and well-supported by selective CRISPR data** — it is the safest entry to discuss
regardless of driver-resolution outcome (though its in vivo CIC-DUX4 translation is itself only modest per
the palbociclib caveat). **MCL1 is the highest-ceiling but most driver-contingent entry** — it should be
framed to any clinical audience as "pending nuclear DUX4 IHC," not as a current option.

---

## Bibliography (this file)

- DepMap 24Q4 CRISPR proxy analysis: `sims/02-dependency-mining/RESULTS.md` and `dependency_table.csv`
  (this repo).
- Bakaric et al., *Cancers* 2024;16(2):457, PMID 38275898, DOI 10.3390/cancers16020457 (p300/CBP dependency,
  GSE248040 ChIP-seq).
- "Patient-derived tumoroids from CIC::DUX4 rearranged sarcoma identify MCL1 as a therapeutic target,"
  *Nat Commun* 2025, PMID 40841513, DOI 10.1038/s41467-025-62629-6, PMC12370961.
- "Small round cell sarcoma tumoroid biobank reveals CIC::DUX4 sarcoma vulnerability to MCL-1 inhibition,"
  *Nat Commun* 2025, PMID 40841360, DOI 10.1038/s41467-025-62673-2.
- Yoshimoto et al., *Cancer Res* 2017;77(11):2927-37, PMID 28404587 (Ccnd2 upregulation via ETV4/PEA3 in
  mouse CIC-DUX4 models).
- Specht K et al., *Hum Pathol* 2016;58:161-170, PMID 27664537 (1p loss, recurrent CNAs, ARID1A in
  recurrence).
- Quercetin-Mcl1: Clin Cancer Res 2010;16(23):5679, PMC3142809 / PMC3069720.
- Quercetin-doxorubicin PK (rat): PMID 21544726. Quercetin-etoposide PK (rat): PMID 19414395.
- Quercetin CYP3A4 IC50 ≈1.97 µM: cited via PK-interaction literature search this session.
- "CIC-DUX4 oncoprotein drives sarcoma metastasis and tumorigenesis via distinct regulatory programs," JCI
  2019 (CCNE1-CDK2/dinaciclib) — **PMID [VERIFY]**.
- Palbociclib in vivo CIC-DUX4 ("limited effect"): **[VERIFY — source not independently re-opened this
  session]**.
- Driver-uncertainty applicability matrix and EVSI ranking:
  `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`.
- Tumorigenesis build recipe (Steps 3, 5; FH-A, FH-D):
  `simulation-output/tumorigenesis-reverse-engineering/tumorigenesis-build-recipe.md`.
- ARID1A as cBAF subunit / BAF-PRC2 antagonism: general molecular biology, search-result-level summary
  this session — `[no single direct citation extracted; mechanism inferred from BAF-PRC2 antagonism
  literature, e.g. PMC7060479, and ARID1A structural role]`.

*Research simulation; hypothesis generation only. Not medical advice, not a treatment plan, no dosing.*
