# V3 Epigenetic Therapy Specialist — Epigenetic Reprogramming (Clean-Slate v3)

**One-line summary:** Covers clinical epigenetic-modifier drug classes (HDACi, EZH2i, DNMTi, BETi) and
their fusion-agnostic potential to restore MHC-I and chromatin accessibility in CIC-DUX4 sarcoma, plus
dietary epigenetic modulators (sulforaphane, butyrate, EGCG, curcumin) with honest exposure caveats.
**Deliberately excludes:** differentiation therapy (retinoids/vitamin D — covered by the
differentiation-therapy specialist), PROTAC/ASO constructs and the detailed EZH2i/BETi/CDK4-6i clinical
trial landscape (covered by the protac-aso specialist), and synthetic-lethality dependency mapping
(covered by the synthetic-lethality specialist). Overlaps with those files on EZH2i/BETi are intentional
where MHC-I/chromatin mechanism is the angle; trial-logistics detail is left to those specialists.

**Confidence: medium** — the clinical drug classes and their MHC-I mechanisms are well-documented in
cancer broadly (Established/Clinical-Trial tier in other diseases), but CIC-DUX4-specific data are sparse,
one major mechanistic assumption (PRC2/H3K27me3 dependency) is now in question for this fusion
specifically (see Red-Team Self-Challenge), and the regulatory landscape for the most-discussed agent
(tazemetostat) changed dramatically and very recently (2026-03-09).

---

## MHC-I Upregulation Candidates (V3 → V4 Bridge — TOP SECTION)

This section is the mandatory hand-off to the V4 (Immune Watchdog) lead and the orchestrator. **V4 cannot
begin until this section exists on disk.**

### Clinical-tier candidates (cleanest mechanistic cases)

| Candidate | Mechanism for MHC-I restoration | Tier | CIC-DUX4 direct evidence | Fusion-dependence |
|---|---|---|---|---|
| **HDAC inhibitors (class I, e.g., vorinostat, romidepsin, panobinostat, belinostat)** | Increased global histone acetylation (H3K27ac, H4ac) opens chromatin at antigen-presentation-machinery (APM) loci (*TAP1*, *TAP2*, *PSMB8/9*, *HLA-A/B/C*, *B2M*); HDACi-driven re-expression of endogenous retroviral elements triggers a viral-mimicry/interferon (STAT1) response that further drives APM gene transcription. Documented to upregulate MHC-I and facilitate CTL-mediated killing in glioma cell lines [Wang et al., *J Cancer* 2019, PMC6843866] and to "reshape the tumoral immune landscape towards an immune-stimulatory profile" with romidepsin in a 2025 liver-cancer study [Nature Communications 2025, doi via nature.com/articles/s41467-025-62934-0]. | Preclinical-Cell (glioma, liver, lymphoma lines) / Clinical-Trial (vorinostat/romidepsin approved for cutaneous T-cell lymphoma — different indication, same mechanism class) | None direct in CIC-DUX4 | **Fusion-agnostic** — acts on host chromatin/APM machinery, not on the fusion junction. Applies to the ~5% fusion-unconfirmed cohort. |
| **EZH2 inhibitors (tazemetostat and class)** | PRC2-mediated H3K27me3 deposition silences APM genes in PRC2-dependent tumors; EZH2i removes this repressive mark, restoring MHC-I/HLA-A,B,C and TAP1/2 transcription. This mechanism is **well-established in PRC2-dependent contexts** (SMARCB1-loss rhabdoid tumors/epithelioid sarcoma, where PRC2 is "unopposed"). | Clinical-Trial (mechanism established in PRC2-dependent tumors) / **Mechanistic-at-best for CIC-DUX4 — see caveat below** | None direct in CIC-DUX4; **and a 2024 CIC-DUX4 chromatin-profiling study suggests this fusion is NOT primarily PRC2-dependent (see "Tazemetostat" entry and Red-Team section)** | Fusion-agnostic mechanism class, but the **specific premise (PRC2 dependency) may not hold for CIC-DUX4** — see below. Do not treat as the "cleanest" example without this caveat. |
| **DNMT inhibitors (azacitidine, decitabine, guadecitabine)** | DNA hypomethylating agents reverse promoter hypermethylation of MHC-I/HLA genes and TAP genes; also reactivate endogenous retroviral elements → cGAS-STING/interferon (type I IFN) signaling → STAT1-driven APM gene transcription. Direct human evidence: a phase II study of 5-azacitidine + entinostat (HDACi) in advanced breast cancer showed "substantial upregulation in MHC-I in five patients with matched pre/post biopsies" [Li et al./related — cite the breast-cancer azacitidine+entinostat MHC-I study, PMID context via search]. Guadecitabine upregulates MHC-I in response to interferon-γ via demethylation of MHC-I genes [Luo et al., *Nat Commun* 2018, "DNA methyltransferase inhibition upregulates MHC-I to potentiate cytotoxic T lymphocyte responses in breast cancer", www.nature.com/articles/s41467-017-02630-w]. | Clinical-Trial (breast cancer; mechanism class established) | None direct in CIC-DUX4 | **Fusion-agnostic** — acts on host methylome/interferon machinery. Applies to the ~5% fusion-unconfirmed cohort. |
| **BET inhibitors (OTX015/birabresib, BMS-986158, AZD5153)** | BRD4 reads H3K27ac marks at super-enhancers; BET inhibition has been reported to modulate immune-related transcription, including interferon-stimulated genes and, in some tumor models, MHC-I/PD-L1 expression — though the direction (up vs. down) is context-dependent and less consistently "MHC-I up" than HDACi/DNMTi/EZH2i. Included here for completeness because BETi is the dominant V3 clinical-track candidate (see protac-aso-specialist file), but **flagged as the weakest of the four classes for MHC-I specifically**. | Preclinical-Cell / Clinical-Trial (general oncology) | None direct in CIC-DUX4 | Fusion-agnostic mechanism, but MHC-I direction not consistently "up" — **lower confidence than the other three**. |

### Dietary-tier candidates — UNESTABLISHED at achievable exposure

**Sulforaphane** (broccoli/broccoli-sprout glucosinolate-derived isothiocyanate) is a documented weak
class-I HDAC inhibitor in cell lines — it depletes HDAC3 (and other class I/II HDACs) in colon cancer
cells via a 14-3-3/Pin1-mediated corepressor-complex dissociation mechanism [Rajendran et al., *Mol
Cancer* 2011, molecular-cancer.biomedcentral.com/articles/10.1186/1476-4598-10-68], and shares the
"global histone acetylation / epigenetically-silenced gene reactivation" phenotype of HDACi drugs
[Myzak/Dashwood, *Cancer Res* 2004, aacrjournals.org/cancerres/article/64/16/5767]. Since clinical
HDACi upregulate MHC-I (above), and sulforaphane is mechanistically a (much weaker) HDAC inhibitor, **the
mechanistic chain to MHC-I upregulation is plausible** — but:

- **No study has measured tumor MHC-I expression in a patient after dietary sulforaphane exposure.**
- The cell-line concentrations producing measurable HDAC effects (low-to-mid µM, sustained exposure over
  days) are far above plasma sulforaphane concentrations achievable from food, which peak in the
  **sub-µM to low-µM range transiently** after a single serving of broccoli sprouts and clear within
  hours.
- **Juicing destroys the activation step.** Sulforaphane does not exist preformed in broccoli — it is
  generated from its precursor glucoraphanin by the enzyme myrosinase upon **chewing or chopping**
  (cell-wall disruption brings the enzyme into contact with substrate). Juicing in a high-speed juicer
  that separates pulp/fiber from liquid, and especially any heating/blanching step, substantially reduces
  myrosinase activity and glucoraphanin-to-sulforaphane conversion. The patient's broccoli-containing
  fresh juice is **unlikely to deliver meaningful sulforaphane** unless the broccoli is chewed/chopped
  raw separately from the juicing process.

**Honest bottom line: whether dietary sulforaphane (even via chewed broccoli/broccoli sprouts) reaches
tumor exposure sufficient to produce a measurable MHC-I upregulation in a human patient is
UNESTABLISHED.** This is a Mechanistic-tier hypothesis with a plausible chain of evidence behind each
link, not a demonstrated clinical effect. Tag: `Mechanistic`, `fusion-agnostic`, `exposure-unestablished`.

**Butyrate** (colonic SCFA from fermented fiber) is a well-characterized HDAC inhibitor — but almost
entirely **at colonic luminal concentrations (low mM)**, which are far higher than systemic/portal
butyrate levels (low µM) reached after absorption and hepatic first-pass metabolism. The mechanistic
chain (HDACi → H3K27ac → MHC-I) is the same as for sulforaphane and clinical HDACi, but **systemic tumor
exposure to butyrate at HDAC-inhibitory concentrations from dietary fiber fermentation is UNESTABLISHED**
and considered unlikely for a deep soft-tissue/lung lesion. Tag: `Mechanistic`, `fusion-agnostic`,
`exposure-unestablished`.

**Net assessment for V4:** the clinical-drug-class mechanism (HDACi/DNMTi → MHC-I up, fusion-agnostic) is
real and should inform V4's epigenetic-priming-bridge discussion. The dietary analogues
(sulforaphane/butyrate) are mechanistically aligned but **should not be presented to V4 or the
orchestrator as a "diet-based MHC-I upregulation strategy" with any expectation of clinical effect** —
they are a hypothesis, not an intervention with demonstrated immunological readout.

---

## Ranked Candidate List

| Rank | Compound/Class | Mechanism | Tier | CIC-DUX4 direct? | Cross-vector | Atypical-case (fusion-dependence) |
|---|---|---|---|---|---|---|
| 1 | HDAC inhibitors (vorinostat, romidepsin, panobinostat, belinostat) | Global histone hyperacetylation (H3K27ac↑) reopens silenced chromatin incl. APM/MHC-I loci; viral-mimicry/IFN response | Clinical-Trial (CTCL indication; sarcoma trials largely combination, modest monotherapy) | None direct | V4 (MHC-I bridge) | Fusion-agnostic |
| 2 | DNMT inhibitors (azacitidine, decitabine) | DNA demethylation reactivates silenced tumor-suppressor and APM genes; ERV reactivation → type-I IFN → STAT1 → MHC-I | Clinical-Trial (breast cancer MHC-I data; AML/MDS approved indication, different mechanism use-case) | None direct | V4 (MHC-I bridge) | Fusion-agnostic |
| 3 | EZH2 inhibitors (tazemetostat / valemetostat / class) | PRC2/H3K27me3 removal de-represses APM and differentiation genes in PRC2-dependent tumors | **Downgraded — see caveat**: was Established (epithelioid sarcoma) as of 2020; **globally withdrawn 2026-03-09 [VERIFY — confirmed live, see below]**. For CIC-DUX4, now best characterized as Theoretical given (a) no approved/marketed agent in this class currently exists at all, and (b) a 2024 CIC-DUX4 chromatin study questions the PRC2-dependency premise itself | None direct; counter-evidence exists (see Red-Team) | V4 (mechanism class only — access now nil) | Fusion-agnostic mechanism, but premise-contingent (see Red-Team) |
| 4 | BET inhibitors (OTX015, BMS-986158, AZD5153) | BRD4 reader-domain inhibition collapses super-enhancer transcription (incl. MYC-driven programs); variable effect on MHC-I/PD-L1 | Clinical-Trial (phase I/II solid tumors incl. pediatric Ewing-family, NCT02419417 / NCT03936465) | None direct | V1 (BRD4 throttling — primary BETi rationale lives there), V4 (weak MHC-I signal) | Fusion-agnostic |
| 5 | Sulforaphane (broccoli/sprouts) | Weak class-I HDAC inhibition (HDAC3 depletion via 14-3-3/Pin1) → global histone acetylation | Preclinical-Cell (colon cancer lines, low-to-mid µM sustained) | None direct | V1 (overlaps with EGCG/sulforaphane chemoprevention literature), V4 (MHC-I — exposure-unestablished) | Fusion-agnostic; exposure-unestablished |
| 6 | EGCG (green tea) | Reported DNMT inhibitor (competitive, Ki ≈ 6.9 µM) and weak EZH2 modulator in cell lines; reactivates methylation-silenced genes (RXRα, RECK, IFI16) | Preclinical-Cell (5–50 µM, days of exposure) | None direct | V1 (BRD4/bioavailability already covered there) | Fusion-agnostic; bioavailability-limited |
| 7 | Butyrate (fermented dietary fiber) | HDAC inhibition at colonic mM concentrations; H3K27ac↑ | Preclinical (colonic) | None direct | V4 (MHC-I — exposure-unestablished) | Fusion-agnostic; exposure-unestablished |
| 8 | Curcumin (turmeric, ± piperine) | Reported BRD4-chromatin disruption and broad polypharmacology incl. HAT/HDAC modulation; H3K27ac effects reported in some lines but evidence base for the BRD4/H3K27ac axis specifically is thinner than for curcumin's other reported targets (NF-κB, STAT3) | Preclinical-Cell; bioavailability is the dominant limiting factor (already detailed in V1 bioavailability file — Shoba 1998 caveat applies) | None direct | V1 (primary home for curcumin), V4 (anti-inflammatory) | Fusion-agnostic; bioavailability-limited |

---

## Detailed Entries

### 1. HDAC Inhibitors (vorinostat, romidepsin, panobinostat, belinostat)

- **Mechanism:** Class I/II HDAC inhibition prevents removal of acetyl groups from histone tails,
  increasing H3K27ac and chromatin accessibility broadly, including at antigen-presentation-machinery
  (APM) loci (*HLA-A/B/C*, *B2M*, *TAP1/2*, *PSMB8/9*). A second, increasingly emphasized mechanism is
  "viral mimicry": HDACi-induced re-expression of endogenous retroviral elements activates cytosolic
  nucleic-acid sensors (e.g., MDA5/RIG-I, cGAS-STING pathways), driving a type-I interferon response that
  upregulates APM genes via STAT1/IRF1.
- **Tier:** Clinical-Trial. Vorinostat (Zolinza) and romidepsin (Istodax) are FDA-approved for cutaneous
  T-cell lymphoma — a different indication/mechanism use-case, not sarcoma, but the drug class and the
  H3K27ac/MHC-I mechanism are clinically validated pharmacology, not purely preclinical. In sarcoma,
  HDACi "are not effective as monotherapy, but seem promising in combination treatment" [search result
  summary from sarcoma HDACi literature]; a 2025 study reports romidepsin improves efficacy of
  standard-of-care chemotherapy combinations for Ewing sarcoma [PMC12730613, *In Vitro and In Vivo
  Efficacy of Romidepsin Alone and in Addition to Standard of Care for Treatment of Ewing Sarcoma"].
- **Evidence in CIC-DUX4 specifically?** None direct. The Ewing-sarcoma romidepsin data is the closest
  P1-rung (fusion round-cell family) transfer available.
- **MHC-I evidence:** HDACi "up-regulated the expressions of MHC-I pathway molecules, and enhanced the
  recognition and killing of immune cells" in glioma cell lines [Wang et al. 2019, PMC6843866,
  jcancer.org/v10p5638.htm]; romidepsin "reshape[d] the tumoral immune landscape towards an
  immune-stimulatory profile" in a 2025 liver cancer study [Nature Communications,
  nature.com/articles/s41467-025-62934-0].
- **Atypical-case note:** Fusion-agnostic — acts on host chromatin machinery, applies to fusion-unconfirmed
  cases.
- **SOC chemo-interaction screening (sarcoma-chemo-interactions):**
  - CYP3A4: HDACi (vorinostat, romidepsin) are themselves CYP3A4 substrates; concurrent strong CYP3A4
    inducers/inhibitors would alter HDACi exposure — this is a clinician-managed drug-drug interaction in
    a hypothetical combination regimen, not a dietary concern. `not screened in depth — clinical-track
    drug, not a dietary recommendation; flag for oncologist if ever combined with ifosfamide (both CYP3A4
    substrates)`.
  - This entry is **clinical-track, not a dietary recommendation** — included here for the MHC-I
    mechanism discussion, not as something the patient is taking or could readily access outside a
    trial/oncologist-directed regimen.

### 2. EZH2 Inhibitors — Tazemetostat (and class)

**This entry requires careful handling per the assignment — full verification below.**

- **Mechanism:** EZH2 is the catalytic subunit of PRC2 (with SUZ12, EED), depositing the repressive
  H3K27me3 mark. In PRC2-dependent tumors (canonically, SMARCB1-loss rhabdoid tumors and epithelioid
  sarcoma, where loss of the BAF/SWI-SNF complex leaves PRC2 "unopposed" and hyperactive), EZH2 inhibition
  removes H3K27me3 from APM and differentiation-gene promoters, restoring their transcription —
  including MHC-I.
- **Indication basis — what tazemetostat was actually approved for:** Tazemetostat (Tazverik) received
  **FDA accelerated approval on 2020-01-23 for adults and adolescents ≥16 years with metastatic or
  locally advanced epithelioid sarcoma not eligible for complete resection** (ORR ~15% in the pivotal
  EZH-202 cohort: 1.6% CR, ~13% PR). It separately received accelerated approval for relapsed/refractory
  follicular lymphoma with an EZH2 mutation (2020) and later for relapsed/refractory follicular lymphoma
  after ≥2 prior systemic therapies regardless of EZH2 mutation status (2021).
  **Tazemetostat was NEVER approved by FDA or EMA for CIC-rearranged sarcoma, or for CIC-DUX4 of any
  kind.** Any rationale for CIC-DUX4 is an **extrapolation from PRC2 dependency in a mechanistically
  different fusion sarcoma** (epithelioid sarcoma's SMARCB1-loss-driven PRC2 dependency vs. CIC-DUX4's
  fusion biology — see Red-Team Self-Challenge below for why this extrapolation may not hold).

- **REGULATORY STATUS — VERIFIED LIVE 2026-06-14 [VERIFY — current as of this date, re-check before any
  future use]:**
  - **On 2026-03-09, Ipsen (the current sponsor) voluntarily and immediately withdrew Tazverik
    (tazemetostat) from the market and from all clinical trials, across ALL indications** — follicular
    lymphoma AND epithelioid sarcoma — **worldwide**. [Sources: FDA Drug Safety Alert
    (fda.gov/drugs/drug-alerts-and-statements/fda-alerts-health-care-providers-and-patients-about-increased-risk-new-blood-cancers-tazverik);
    Ipsen press releases (ipsen.com/press-release/ipsen-voluntarily-withdraws-tazverik-tazemetostat-in-follicular-lymphoma-and-epithelioid-sarcoma-3251503/
    and the "Update" follow-on press release 3252192); OncLive
    (onclive.com/view/fda-indications-for-tazemetostat-in-r-r-follicular-lymphoma-and-epithelioid-sarcoma-are-voluntarily-withdrawn);
    CancerNetwork, Targeted Oncology, Oncology Nurse Advisor — concordant reporting, accessed
    2026-06-14.]
  - **Reason:** an Independent Data Monitoring Committee for the ongoing phase Ib/III SYMPHONY-1 trial
    (tazemetostat + lenalidomide + rituximab vs. rituximab alone in follicular lymphoma) found that, as of
    2026-03-06, **18/318 (5.7%) of tazemetostat-treated patients developed secondary hematologic
    malignancies** (including MDS and acute leukemias, with associated mortality and limited resolution),
    **vs. 0 events in the control arm**. The IDMC recommended halting enrollment and discontinuing
    tazemetostat in all treated patients across all clinical programs, transitioning patients to
    standard-of-care.
  - **Practical consequence for this patient/catalog:** As of 2026-06-14, **there is no approved,
    marketed, or (per these sources) actively-enrolling tazemetostat program anywhere** — not for
    epithelioid sarcoma (its only prior approved sarcoma indication), not for follicular lymphoma, and a
    fortiori not as an extrapolated CIC-DUX4 option. The EZH2i drug-class mechanism remains scientifically
    relevant to the MHC-I discussion below, but **tazemetostat itself is not currently a real-world
    access pathway for any patient, for any indication** — a substantially stronger statement than "not
    approved for CIC-DUX4," and a change from the framework's prior characterization of this agent.
  - **EMA status (independent of the withdrawal):** Even before the March 2026 withdrawal, tazemetostat
    had **never received EMA approval** — as of a March 2025 source, "Tazverik seems a long way away from
    EMA approval" [everyone.org/blog/tazemetostats-ema-approval, accessed via search 2026-06-14]. So EMA
    status was already "not approved" independent of the subsequent global withdrawal; FDA and EMA status
    were **not divergent in the direction of "EMA lags FDA approval"** in any way that would have given a
    European patient access tazemetostat that a US patient lacked.
  - **Other EZH1/2 inhibitors (class context):** Valemetostat (DS-3201b, a dual EZH1/2 inhibitor) is
    approved in **Japan** for relapsed/refractory adult T-cell leukemia/lymphoma and peripheral T-cell
    lymphoma (different indication, different jurisdiction), and has been studied in a pediatric phase I
    trial (NCCH1904) in SMARCB1/INI1-deficient solid tumors (malignant rhabdoid tumor, epithelioid
    sarcoma) with an objective response in 2/14 evaluable patients, both AT/RT
    [ascopubs.org/doi/abs/10.1200/JCO.2025.43.16_suppl.10003]. **No published valemetostat data in
    CIC-DUX4.** Valemetostat is not FDA- or EMA-approved for any solid-tumor or sarcoma indication
    [VERIFY — checked 2026-06-14].

- **Tier:** Given the above, I am scoring this entry as follows — **tier differs by what is being
  claimed**:
  - "EZH2i mechanism (PRC2/H3K27me3 → MHC-I de-repression) is real pharmacology" → Clinical-Trial (in
    PRC2-dependent tumors generally).
  - "Tazemetostat is an accessible option for this patient, via any regulatory pathway, for any
    indication" → **false as of 2026-06-14** — no tier applies; access is nil.
  - "EZH2i is mechanistically rationalized for CIC-DUX4 specifically" → **Theoretical**, and per the
    Red-Team section below, the rationale itself is now in question.
- **Evidence in CIC-DUX4 specifically?** None direct, and see Red-Team section for counter-evidence.
- **Atypical-case note:** The PRC2/H3K27me3 mechanism, where it applies, is fusion-agnostic (acts on host
  chromatin, not the fusion junction sequence) — but per the Red-Team section, whether it applies to
  CIC-DUX4 **at all** is now uncertain, independent of fusion-confirmation status.

### 3. DNMT Inhibitors (azacitidine, decitabine, guadecitabine)

- **Mechanism:** Hypomethylating agents are incorporated into DNA in place of cytosine, trapping and
  depleting DNMT1/3A/3B and causing passive demethylation over successive cell divisions. This reverses
  promoter hypermethylation of silenced tumor-suppressor and APM genes, and separately reactivates
  endogenous retroviral elements ("viral mimicry") to trigger a type-I interferon response.
- **Tier:** Clinical-Trial for the MHC-I mechanism in solid tumors. Azacitidine and decitabine are
  FDA-approved for myelodysplastic syndrome/AML (a different indication/mechanism-use-case — cytotoxic
  hypomethylation in a hematologic malignancy, not immune-priming in a solid tumor). The MHC-I-restoration
  use-case is supported by:
  - Luo et al., *Nature Communications* 2018, "DNA methyltransferase inhibition upregulates MHC-I to
    potentiate cytotoxic T lymphocyte responses in breast cancer"
    [nature.com/articles/s41467-017-02630-w] — guadecitabine demethylates MHC-I gene promoters and
    upregulates MHC-I in response to IFN-γ.
  - A phase II trial of 5-azacitidine + entinostat (an HDACi) in advanced breast cancer reported
    "substantial upregulation in MHC-I in five patients with matched pre- and post-treatment biopsies"
    [search-result summary; **[no direct PMID located in this session — flag for follow-up
    verification]**].
  - A clinical trial of decitabine evaluated "changes in HLA class I as indicators of interferon
    response" [search-result summary referencing a decitabine + interferon trial,
    clinicaltrials.gov/study/NCT00701298 covers decitabine ± interferon alfa-2b in unresectable/metastatic
    solid tumors — **[VERIFY: this NCT is for a different, older decitabine+IFN study; cited here only as
    an example of the decitabine+interferon clinical-trial space, not as direct MHC-I evidence — do not
    over-cite]**].
- **Evidence in CIC-DUX4 specifically?** None direct. One search result noted "azacitidine chemosensitizes
  sarcoma cells through PTEN activation" — a different (non-MHC-I) mechanism, in sarcoma broadly, not
  CIC-DUX4-specific [no direct citation located; mechanism inferred from search-result summary].
- **Atypical-case note:** Fusion-agnostic — acts on host methylome and interferon-signaling machinery.
  Applies to fusion-unconfirmed cases.
- **SOC chemo-interaction screening:** Clinical-track drug, not a dietary recommendation —
  `not screened in depth; flag for oncologist if ever considered in combination with ifosfamide given
  shared myelosuppression risk with cyclophosphamide/ifosfamide`.

### 4. BET Inhibitors (OTX015/birabresib, BMS-986158, AZD5153) — MHC-I angle only

- **Mechanism:** BRD4 (and other BET family bromodomain proteins) read H3K27ac marks at active enhancers
  and super-enhancers, recruiting transcriptional machinery. BET inhibition (e.g., JQ1, OTX015,
  BMS-986158, AZD5153) competitively displaces BRD4 from acetylated chromatin, collapsing super-enhancer-
  driven transcriptional programs — the primary rationale for BETi in CIC-DUX4 lives in **V1 (BRD4 /
  super-enhancer throttling)** and the protac-aso-specialist file (clinical trial landscape). For this
  V3/MHC-I-focused entry: BET inhibition has variable, context-dependent effects on immune-related gene
  expression, including some reports of altered MHC-I/PD-L1; the direction is not as consistently
  "MHC-I up" as for HDACi/DNMTi/EZH2i.
- **Tier:** Preclinical-Cell / Clinical-Trial (general oncology). BMS-986158 has been studied in a phase
  I/IIa trial of advanced solid tumors (NCT02419417) and in a pediatric phase I trial of relapsed/
  refractory solid tumors including Ewing sarcoma patients (NCT03936465)
  [PMC9454848; clinicaltrials.gov/study/NCT02419417; hra.nhs.uk study summary].
- **Evidence in CIC-DUX4 specifically?** None direct.
- **MHC-I evidence:** Weak/inconsistent — **flagged as the weakest of the four classes for the V3→V4
  bridge**. Not recommending this as a primary MHC-I-priming candidate; full BETi discussion belongs to V1
  and the protac-aso-specialist.
- **Atypical-case note:** Fusion-agnostic (BRD4/super-enhancer mechanism doesn't depend on the specific
  junction sequence).

### 5. Sulforaphane (broccoli, broccoli sprouts)

- **Mechanism:** Isothiocyanate derived from glucosinolate precursor glucoraphanin via myrosinase-mediated
  hydrolysis upon chewing/chopping. In colon cancer cell lines, sulforaphane causes time-dependent loss of
  class I (and some class II) HDAC proteins, with HDAC3 depletion preceding other HDACs, via a
  14-3-3/Pin1-mediated mechanism that dissociates the HDAC3/SMRT corepressor complex [Rajendran et al.,
  *Mol Cancer* 2011, molecular-cancer.biomedcentral.com/articles/10.1186/1476-4598-10-68]. This produces
  global histone hyperacetylation and reactivation of epigenetically silenced genes, the same general
  phenotype as clinical HDACi [Myzak & Dashwood, *Cancer Res* 2004,
  aacrjournals.org/cancerres/article/64/16/5767/511641].
- **Tier:** Preclinical-Cell. Concentrations used in the cited mechanistic studies are low-to-mid µM
  sustained over days — see exposure caveat in the MHC-I section above.
- **Evidence in CIC-DUX4 specifically?** None direct.
- **MHC-I relevance:** Mechanistically plausible chain (weak HDACi → H3K27ac↑ → MHC-I↑, by analogy to
  clinical HDACi above) but **no direct measurement of MHC-I after dietary sulforaphane exposure in any
  tumor type was found**. Tag: `Mechanistic`, `exposure-unestablished`.
- **Juicing note (patient-specific):** The patient's fresh juice includes broccoli. As stated in the
  MHC-I section, **juicing (especially with pulp/fiber separation, and any heat) substantially reduces
  myrosinase-mediated sulforaphane generation** relative to chewing raw broccoli or broccoli sprouts.
  If sulforaphane exposure is a goal (even acknowledging it is `exposure-unestablished` for MHC-I), raw
  chewed broccoli/sprouts (not juiced) is the mechanistically more defensible preparation —
  **this is a mechanism note, not a dosing recommendation.**
- **Atypical-case note:** Fusion-agnostic.
- **SOC chemo-interaction screening:**
  - CYP3A4: Sulforaphane has been reported to modulate CYP isoforms in some preclinical studies, but
    dietary-level (food-derived) exposure effects on CYP3A4 activity relevant to ifosfamide activation are
    not well characterized in humans. `not screened beyond this — no strong documented dietary-dose CYP3A4
    interaction found in the sources checked (PubChem/general search this session)`.
  - P-gp: no documented dietary-dose interaction found in sources checked this session.
  - ROS-axis: sulforaphane is generally pro-oxidant/Nrf2-activating at the cellular level rather than a
    direct antioxidant scavenger in the vitamin-C/NAC sense; no documented ifosfamide-efficacy concern
    found in sources checked this session.
  - **Citation for "none found": general web search this session (2026-06-14); not a substitute for a
    DrugBank/NCCN-level pharmacist review.**

### 6. EGCG (green tea catechin)

- **Mechanism:** EGCG is a reported competitive DNMT inhibitor (Ki ≈ 6.89 µM) that reactivates
  methylation-silenced genes — demonstrated for RXRα in colon cancer cells [Oncotarget,
  oncotarget.com/article/9204/text/], RECK in oral squamous cell carcinoma [Nature, *Br J Cancer*,
  nature.com/articles/6604521], and IFI16 (an innate-immune gene) in a 2022 screen of DNA-methylation-
  modifying natural compounds [PMID 35707762]. Original DNMT-inhibition characterization: Fang et al.,
  *Cancer Res* 2003, "Tea Polyphenol (-)-Epigallocatechin-3-Gallate Inhibits DNA Methyltransferase and
  Reactivates Methylation-Silenced Genes in Cancer Cell Lines" [PMID 14633667]. Also reported as a weak
  EZH2 modulator in cell lines (carried in the V1 cross-vector table from `sarcoma-vector-context`).
- **Tier:** Preclinical-Cell. Concentrations in the cited studies range 5–50 µM over 6 days to 144 hours —
  **substantially above achievable dietary plasma EGCG concentrations**, which are typically in the
  0.1–1 µM range after brewed green tea, per the V1 bioavailability caveats already documented for this
  compound.
- **Evidence in CIC-DUX4 specifically?** None direct.
- **IFI16 relevance note:** IFI16 is a cytosolic DNA sensor in the innate-immune/interferon pathway —
  mechanistically adjacent to the "viral mimicry → interferon → MHC-I" axis discussed above for HDACi/
  DNMTi, but **this is a second-order inference, not a demonstrated EGCG → MHC-I link**. Flagging as a
  potential mechanistic bridge for a forward hypothesis (see below), not as an established pathway.
- **Atypical-case note:** Fusion-agnostic; bioavailability-limited (already detailed in V1).
- **SOC chemo-interaction screening:** EGCG/green tea catechins have documented CYP3A4 and P-gp modulatory
  activity reported in the pharmacology literature broadly (consistent with the `sarcoma-chemo-
  interactions` skill's list of compounds to check); the V1 bioavailability file is the primary location
  for this compound's full interaction screening. `cross-reference V1 — not re-screened in full here to
  avoid duplication`.

### 7. Butyrate (dietary fiber fermentation)

- **Mechanism:** Short-chain fatty acid produced by colonic bacterial fermentation of resistant starch and
  inulin-type fibers. Classic HDAC inhibitor at colonic luminal concentrations (low millimolar).
- **Tier:** Preclinical (colonic-concentration cell/tissue studies).
- **Evidence in CIC-DUX4 specifically?** None direct.
- **MHC-I relevance:** Same mechanistic chain as sulforaphane (HDACi → H3K27ac↑ → MHC-I↑ by analogy to
  clinical HDACi), but **systemic/portal butyrate concentrations after absorption are roughly 2–3 orders
  of magnitude below colonic luminal concentrations**, making meaningful HDAC inhibition in a deep
  soft-tissue/lung tumor far less plausible than a local colonic effect. Tag: `Mechanistic`,
  `exposure-unestablished`, lower confidence than sulforaphane for systemic reach.
- **Atypical-case note:** Fusion-agnostic.

### 8. Curcumin (turmeric ± piperine)

- **Mechanism:** Broad polypharmacology; reported effects include modulation of histone
  acetyltransferase/HDAC balance and BRD4-chromatin interactions in some cell-line studies, alongside its
  better-characterized NF-κB and STAT3 modulation (more relevant to V1/V4 anti-inflammatory framing than
  to this epigenetic file specifically).
- **Tier:** Preclinical-Cell; the BRD4/H3K27ac-specific literature is thinner than curcumin's broader
  anticancer literature — **I could not locate a curcumin → H3K27ac/BRD4 study with a clear concentration
  and cell-line citation in this session's searches** (general 2024–2025 curcumin-bioavailability searches
  returned reviews on nanoformulations and general anticancer mechanisms, not the specific
  BRD4/H3K27ac axis). This entry is therefore **weaker than the V1 cross-vector table implies** — flagging
  for the orchestrator that the curcumin/BRD4/H3K27ac mechanistic claim in the V1 vector-context document
  should be treated as `[no direct citation located this session; mechanism as stated in
  sarcoma-vector-context skill, inferred from curcumin's general polypharmacology]`.
- **Evidence in CIC-DUX4 specifically?** None direct.
- **Atypical-case note:** Fusion-agnostic; bioavailability-limited (Shoba 1998 caveat — full discussion in
  V1 bioavailability file, not reproduced here).
- **SOC chemo-interaction screening:** Curcumin has documented CYP3A4 and P-gp modulatory activity and
  anti-platelet effects relevant to a patient on active chemotherapy and potential surgery — full
  screening is the V1/V2 specialists' domain; **cross-reference, not re-screened here**. The patient is
  already taking curcumin+piperine — this is noted for cross-vector awareness, not as a new recommendation.

---

## CIC-DUX4-Specific Chromatin Biology — Important Context for This Whole File

A 2024 paper, "CIC-DUX4 Chromatin Profiling Reveals New Epigenetic Dependencies and Actionable
Therapeutic Targets in CIC-Rearranged Sarcomas" [*Cancers* (Basel) 2024, 16(2):457, DOI:
10.3390/cancers16020457; PMC10814785; associated dataset GSE248040], found that **CIC-DUX4 functions as a
potent transcriptional *activator* at its binding sites, via direct interaction with the histone
acetyltransferase p300/CBP** — in contrast to wild-type CIC, which is a transcriptional *repressor*. The
paper proposes **p300 inhibition** (not EZH2/PRC2 inhibition) as the actionable epigenetic dependency for
CIC-DUX4, based on this chromatin profiling.

This is directly relevant to two things in this file:
1. It is the strongest piece of **CIC-DUX4-specific** epigenetic-dependency evidence I found in this
   session — stronger than anything supporting the EZH2/PRC2 axis for this fusion.
2. p300/CBP is itself an H3K27ac "writer" — so **p300 inhibition would be expected to *decrease* H3K27ac**
   at CIC-DUX4 target genes, which is a different direction of chromatin change than the HDACi/DNMTi/EZH2i
   "open up silenced chromatin" mechanisms discussed above for MHC-I restoration. Whether p300 inhibition
   in CIC-DUX4 cells would help or hurt MHC-I expression specifically is **not addressed by the cited
   paper and is not established** — flagging as an open question, not asserting either direction.

**p300/CBP inhibitor detail (specific compounds, clinical-trial landscape, and PROTAC angle) is the
protac-aso-specialist's or synthetic-lethality-specialist's domain** — I am flagging the existence and
relevance of this CIC-DUX4-specific finding here because it directly bears on how much weight the
PRC2/EZH2 entries above should carry, but am not duplicating the full compound-level writeup.

---

## What I Could Not Establish

1. **Whether EZH2/PRC2 dependency is mechanistically relevant to CIC-DUX4 at all.** The epithelioid-
   sarcoma extrapolation rests on PRC2 being "unopposed" after SMARCB1/BAF-complex loss. CIC-DUX4 does not
   have documented SMARCB1 loss, and the one CIC-DUX4-specific chromatin-profiling study I found
   (PMC10814785, 2024) characterizes CIC-DUX4 as a p300/CBP-driven transcriptional *activator*, not a
   PRC2-silencing-dependent tumor. I could not find any study directly measuring H3K27me3/PRC2 occupancy
   or EZH2 dependency (e.g., CRISPR dropout) specifically in CIC-DUX4 cell lines or patient samples.
2. **Whether dietary sulforaphane or butyrate produce any measurable MHC-I change in any human tumor.**
   The mechanistic chain (weak HDACi → H3K27ac → MHC-I) is plausible by analogy to clinical HDACi, but I
   found no study measuring tumor MHC-I after dietary-level sulforaphane or butyrate exposure in any
   cancer type, let alone CIC-DUX4.
3. **The exact citation for the azacitidine+entinostat breast-cancer MHC-I study** (referenced in search
   results as showing "substantial upregulation in MHC-I in five patients") — I could not locate a PMID
   for this specific finding in this session and have flagged it as needing follow-up verification rather
   than asserting it with a fabricated citation.
4. **Curcumin's BRD4/H3K27ac mechanism with a specific concentration/cell-line citation** — the V1
   cross-vector context document carries this claim, but my searches this session did not surface a
   primary source for it. I have flagged this for the orchestrator rather than re-asserting it without a
   citation.
5. **Whether p300/CBP inhibition (the CIC-DUX4-specific actionable target per PMC10814785) would help or
   hurt MHC-I expression** — direction not established in the cited paper or elsewhere I could find.
6. **The full clinical-trial status of valemetostat and any other EZH1/2 inhibitors as a "successor" class
   to tazemetostat** — I found Japan-approval and pediatric-trial data but did not do an exhaustive
   ClinicalTrials.gov sweep; the protac-aso-specialist's file is the more appropriate place for a
   complete EZH2i-class trial landscape.

---

## Forward Hypotheses

**[Forward Hypothesis 1] — IFI16/cGAS-STING as the convergent node for epigenetic MHC-I priming in
CIC-DUX4, testable independent of the EZH2/PRC2 question.**

*Hypothesis statement:* If CIC-DUX4 tumors have a baseline-silenced innate-immune/viral-mimicry gene set
(IFI16, cGAS, STING, MDA5, and downstream type-I IFN response genes) — independent of whether the
silencing mechanism is PRC2/H3K27me3, DNA methylation, or simple heterochromatin compaction — then
**any epigenetic agent that de-represses this gene set (HDACi, DNMTi, or even EGCG's reported DNMT/IFI16
effect) should produce a measurable MHC-I increase via the interferon/STAT1 axis**, regardless of whether
CIC-DUX4's "native" dependency is PRC2 (epithelioid-sarcoma-style) or p300/CBP (per PMC10814785).

*Mechanistic basis:* HDACi and DNMTi both converge on "viral mimicry → type-I IFN → STAT1/IRF1 → MHC-I/
TAP/B2M transcription" as a shared downstream mechanism (documented in the MHC-I section above), even
though their direct chromatin targets (acetylation vs. methylation) differ. This convergent node may be
**more robust to the CIC-DUX4-specific-dependency uncertainty** than betting on the EZH2/PRC2 axis
specifically.

*What experiment would test it:* Treat CIC-DUX4 patient-derived cell lines (e.g., the lines used in
PMC10814785/GSE248040, if available, or other published CIC-DUX4 lines) with a panel of low-dose HDACi
(e.g., entinostat or panobinostat at clinically achievable concentrations) and a DNMTi (decitabine), then
measure: (a) IFI16/cGAS/STING/MDA5 baseline expression and methylation/acetylation status by ChIP-seq and
RNA-seq (extending the GSE248040 dataset's approach), (b) MHC-I surface expression by flow cytometry
before/after treatment, and (c) whether the MHC-I change correlates with H3K27me3 loss (PRC2 axis),
H3K27ac gain (HDACi axis), or DNA demethylation (DNMTi axis) at the relevant promoters — distinguishing
which mechanism, if any, actually drives the MHC-I change in this specific fusion.

*Why it hasn't been tested:* CIC-DUX4 is extremely rare, and most epigenetic-immune-priming work has been
done in melanoma, NSCLC, breast cancer, and the PRC2-canonical fusion sarcomas (epithelioid sarcoma,
rhabdoid tumor) — not in CIC-DUX4, which only recently (2024) got its first dedicated chromatin-profiling
study.

---

**[Forward Hypothesis 2] — p300/CBP inhibition and HDACi may have opposing or context-dependent effects on
MHC-I in CIC-DUX4, making the choice between them a testable branch point rather than an assumption.**

*Hypothesis statement:* Given that PMC10814785 identifies p300/CBP as the CIC-DUX4-specific
transcriptional-activation dependency (CIC-DUX4 recruits p300 to drive its oncogenic transcriptional
program), and p300 is an H3K27ac "writer" while HDACs are H3K27ac "erasers," **p300 inhibition and HDAC
inhibition push H3K27ac in opposite directions globally** — yet both could plausibly affect MHC-I, just
via different routes (p300i: shuts down the CIC-DUX4 oncogenic program, potentially relieving an
indirect repression of APM genes by the fusion's activity elsewhere in the genome; HDACi: directly opens
chromatin at APM loci). **If both independently increase MHC-I, that would suggest MHC-I restoration in
CIC-DUX4 is overdetermined and robust to which epigenetic axis is targeted — a favorable result for
translational robustness.** If they have opposing effects, that would argue for sequencing (e.g., p300i
to first shut down the oncogenic program, then HDACi to prime immune visibility) rather than combination.

*Mechanistic basis:* CIC-DUX4's p300-dependent activator function (PMC10814785) operating on a different
gene set than the APM/MHC-I locus set targeted by HDACi's global H3K27ac increase — two largely
non-overlapping gene programs that could be independently modulated.

*What experiment would test it:* In CIC-DUX4 cell lines, perform a 2x2 design (vehicle / p300 inhibitor
(e.g., A-485, a published p300/CBP inhibitor used in the PMC10814785-adjacent literature — **[VERIFY
A-485's exact use in CIC-DUX4 specifically before citing; I have not confirmed this compound was used in
PMC10814785 itself]**) / HDACi / combination), measuring MHC-I surface expression, H3K27ac ChIP-seq at
both the CIC-DUX4 binding sites identified in GSE248040 and at canonical APM loci (HLA-A/B/C, B2M,
TAP1/2), and tumor cell viability. The key readout is whether MHC-I change at APM loci is independent of
(or coupled to) the H3K27ac change at CIC-DUX4's own oncogenic binding sites.

*Why it hasn't been tested:* The CIC-DUX4-specific p300 dependency was only published in January 2024;
no follow-up combination study with HDACi/MHC-I readout has had time to be conducted and published as of
this session (2026-06-14), as far as I could determine.

---

## Red-Team Self-Challenge (ADR-0017)

1. **Load-bearing assumption:** The assignment's framing treats "EZH2i and clinical HDACi" as "the
   cleanest examples" of MHC-I-restoring V3 candidates for CIC-DUX4. The load-bearing assumption is that
   **EZH2/PRC2 dependency is mechanistically relevant to CIC-DUX4** (by extrapolation from epithelioid
   sarcoma's SMARCB1-loss biology).
2. **Disconfirmation:** I searched specifically for "CIC-DUX4 EZH2 PRC2 H3K27me3 dependency" and found
   PMC10814785 (2024, *Cancers*), which characterizes CIC-DUX4 as a **p300/CBP-driven transcriptional
   activator**, explicitly contrasting this with the repressive function of wild-type CIC, and proposes
   **p300 inhibition**, not EZH2 inhibition, as the CIC-DUX4-specific actionable target. This is the
   strongest disconfirming evidence available, and I gave it equal search effort to the confirming
   direction (I searched for CIC-DUX4 + EZH2 evidence both supporting and questioning the link).
3. **Alternative:** The best-fitting alternative hypothesis outside this file's lane is **p300/CBP
   inhibition** itself — a real, CIC-DUX4-specific mechanism (PMC10814785) that doesn't map cleanly onto
   "epigenetic reprogramming for MHC-I" (my assigned lane) but does map onto "synthetic lethality /
   dependency" (the synthetic-lethality-specialist's lane) or "PROTAC target" (the protac-aso-specialist's
   lane). I am flagging it here (see the dedicated section above) rather than forcing it into my MHC-I
   framing, and noting it for those specialists/the v3-lead to pick up if they have not already.
4. **Flip test:** If the PRC2/EZH2-dependency assumption is wrong for CIC-DUX4 (which the 2024 paper
   suggests it likely is), **does the MHC-I Upregulation Candidates section still hold?** Yes — HDACi and
   DNMTi MHC-I-restoration mechanisms (viral mimicry → IFN → STAT1 → APM transcription) do not depend on
   PRC2/EZH2 status; they are independently grounded. Only the **EZH2i-specific entry** is
   assumption-contingent, and I have tagged it as such (downgraded from "cleanest example" to
   "premise-contingent, and the premise itself is now in question — separate from and in addition to the
   global regulatory withdrawal"). The HDACi and DNMTi entries remain the cleanest examples for the V4
   bridge.
5. **Steer audit:** The assignment steered me toward tazemetostat as "the cleanest example" and primarily
   toward verifying its *regulatory* status. I did that verification (and found a dramatic result — global
   withdrawal from all indications, not just a CIC-specific non-approval). But I also tested the
   *mechanistic* premise underlying the steer (PRC2 dependency in CIC-DUX4), which the steer did not
   explicitly ask me to question, and found independent grounds (PMC10814785) to downgrade tazemetostat/
   EZH2i further than the regulatory finding alone would imply. I am reporting both findings rather than
   only the one the steer anticipated.

---

## Atypical-Case Summary

All entries in this file (HDACi, EZH2i-class, DNMTi, BETi, sulforaphane, EGCG, butyrate, curcumin) act on
**host chromatin machinery, the host methylome, or host innate-immune signaling** — none depend on the
specific CIC-DUX4 junction sequence. **All entries in this file are fusion-agnostic and apply to the ~5%
fusion-unconfirmed atypical cohort**, including this patient if their fusion status remains unconfirmed.
The one caveat is the EZH2i/PRC2 entry, where the *open question* is not fusion-confirmation status but
whether the PRC2-dependency mechanism applies to CIC-DUX4 biology at all (a different axis of uncertainty,
orthogonal to the atypical-case flag).

---

## Bibliography (this file)

- FDA Drug Safety Alert, "FDA Alerts Health Care Providers and Patients about Increased Risk of New Blood
  Cancers with Tazverik (tazemetostat) Use; Sponsor to Voluntarily Withdraw Product from Market" —
  fda.gov/drugs/drug-alerts-and-statements/fda-alerts-health-care-providers-and-patients-about-increased-risk-new-blood-cancers-tazverik
  [accessed 2026-06-14]
- Ipsen press releases re: voluntary withdrawal of Tazverik (tazemetostat), 2026-03-09 and follow-up —
  ipsen.com/press-release/ipsen-voluntarily-withdraws-tazverik-tazemetostat-in-follicular-lymphoma-and-epithelioid-sarcoma-3251503/
  and ipsen.com/press-release/update-ipsen-voluntarily-withdraws-tazverik-tazemetostat-in-follicular-lymphoma-and-epithelioid-sarcoma-3252192/
  [accessed 2026-06-14]
- OncLive, "FDA Indications for Tazemetostat in R/R Follicular Lymphoma and Epithelioid Sarcoma Are
  Voluntarily Withdrawn" — onclive.com/view/fda-indications-for-tazemetostat-in-r-r-follicular-lymphoma-and-epithelioid-sarcoma-are-voluntarily-withdrawn
  [accessed 2026-06-14]
- everyone.org, "Tazemetostat's EMA approval: What if waiting is no option?" —
  everyone.org/blog/tazemetostats-ema-approval [accessed 2026-06-14, dated ~March 2025; EMA non-approval
  status independently corroborated by the global-withdrawal sources above]
- Valemetostat pediatric phase I trial (NCCH1904) —
  ascopubs.org/doi/abs/10.1200/JCO.2025.43.16_suppl.10003 [accessed 2026-06-14]
- PMC10814785 / *Cancers* 2024, 16(2):457, DOI 10.3390/cancers16020457, "CIC-DUX4 Chromatin Profiling
  Reveals New Epigenetic Dependencies and Actionable Therapeutic Targets in CIC-Rearranged Sarcomas";
  dataset GSE248040 — pmc.ncbi.nlm.nih.gov/articles/PMC10814785/ [accessed 2026-06-14]
- Wang et al. 2019, "Histone deacetylase inhibition up-regulates MHC class I to facilitate cytotoxic T
  lymphocyte-mediated tumor cell killing in glioma cells", *J Cancer* — PMC6843866,
  jcancer.org/v10p5638.htm [accessed 2026-06-14]
- Nature Communications 2025, "The HDAC inhibitor romidepsin renders liver cancer vulnerable to RTK
  targeting and immunologically active" — nature.com/articles/s41467-025-62934-0 [accessed 2026-06-14]
- PMC12730613, "In Vitro and In Vivo Efficacy of Romidepsin Alone and in Addition to Standard of Care for
  Treatment of Ewing Sarcoma" [accessed 2026-06-14]
- Luo et al. 2018, "DNA methyltransferase inhibition upregulates MHC-I to potentiate cytotoxic T
  lymphocyte responses in breast cancer", *Nat Commun* — nature.com/articles/s41467-017-02630-w [accessed
  2026-06-14]
- Fang et al. 2003, "Tea Polyphenol (-)-Epigallocatechin-3-Gallate Inhibits DNA Methyltransferase and
  Reactivates Methylation-Silenced Genes in Cancer Cell Lines", *Cancer Res* — PMID 14633667 [accessed
  2026-06-14]
- Rajendran et al. 2011, "Histone deacetylase turnover and recovery in sulforaphane-treated colon cancer
  cells...", *Mol Cancer* — molecular-cancer.biomedcentral.com/articles/10.1186/1476-4598-10-68 [accessed
  2026-06-14]
- Myzak & Dashwood 2004, "A Novel Mechanism of Chemoprotection by Sulforaphane: Inhibition of Histone
  Deacetylase", *Cancer Res* — aacrjournals.org/cancerres/article/64/16/5767/511641 [accessed 2026-06-14]
- NCT02419417, NCT03936465 — BMS-986158 BET inhibitor trials, clinicaltrials.gov [accessed 2026-06-14]
- Oncotarget, EGCG/RXRα demethylation in colon cancer — oncotarget.com/article/9204/text/ [accessed
  2026-06-14]
- PMID 35707762 — EGCG and IFI16 gene expression / DNA methylation natural-compound screen [accessed
  2026-06-14]
