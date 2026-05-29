# Forward-Simulation Index & Citation Grounding

**What this is.** A synthesis layer over the two forward-simulation documents in this directory, plus a **live-verified citation/accession table** that supersedes the `[VERIFY]` flags those documents had to carry (both were run in a sandbox with network access denied, so they correctly refused to assert any accession). Every item in the "Verified" tables below was confirmed against a live primary source on 2026-05-29 from the main session.

This remains a **research-simulation output, not medical advice.** It is a supplementary forward-simulation team (like the mRNA team), not a fifth attack vector. The four vectors in `docs/00-README.md` are fixed: **V1 Rate Limiting · V2 Compiler Protection · V3 Hot Patching · V4 Immune Watchdog.**

Companion files:
- `counterfactual-trial-forensics.md` — why each intervention class underperformed in CIC-DUX4, what's mechanistically different, what to try differently.
- `in-silico-experiments.md` — computational experiments runnable by the user (structure, condensate, docking, MD, network model, signature reversal, dependency mining, PK).

---

## Headline: the grounding upgraded the simulation

The single most important result of re-grounding is that the live literature contains **validated, CIC-DUX4-specific dependencies** — not the extrapolations the catalog leaned on. Two of these change the forward picture for *this* patient (lung-relapse, imminent high-dose ifosfamide):

### 1. WEE1 is a confirmed CIC-DUX4 vulnerability — and it synergizes with DNA-damaging chemo
Lin et al., **JCI Insight 2022** (PMC8986087; bioRxiv 2021.06.21.448439). CIC-DUX4 sarcomas **depend on the G2/M checkpoint kinase WEE1** to limit DNA damage and unscheduled mitotic entry. The WEE1 inhibitor **adavosertib** decreased viability of patient-derived lines **NCC_CDS1_X1_C1** and **NCC-CDS2-C1** (↓CDK1-Y15 phosphorylation, ↑γH2AX, ↑PARP cleavage / caspase-3/7), in vitro **and in vivo**. Tier: **Preclinical-Cell + Preclinical-Animal** (patient-derived), CIC-DUX4-*specific* (not extrapolated).

> **Forward hypothesis (this patient).** WEE1 abrogates the G2/M checkpoint; ifosfamide is a DNA-damaging alkylator. WEE1 inhibition + DNA damage = forced premature mitosis → mitotic catastrophe. A **WEE1 inhibitor + ifosfamide** combination is a mechanistically grounded, CIC-DUX4-specific sensitization hypothesis directly relevant to his imminent course. This is **fusion-agnostic at the checkpoint level** (the G2/M dependency follows from replication stress, not the exact junction) — so it may apply to the ~5% fusion-unconfirmed subgroup. Caveat: adavosertib + genotoxic chemo raises **additive myelosuppression**; this is a research hypothesis for a trial/oncologist, not a co-administration suggestion. Falsifier: if his tumor lacks the replication-stress/WEE1 dependency (testable on a re-biopsy or a CIC-DUX4 line), the synergy should not appear.

### 2. IGF-1R autocrine signaling — a real dependency in a lung-metastatic CIC-DUX4 model that mirrors this patient
Nakai et al., **Sci Rep 2019** (PMID 31676869; PMC6825133). The CIC-DUX4 line **Kitra-SRS** shows **autocrine IGF-1/IGF-1R activation** and **metastasizes to the lungs** in xenografts; the IGF-1R inhibitor **linsitinib** attenuated growth and IGF-1R/AKT signaling **in vitro and in vivo**. Tier: **Preclinical-Cell + Preclinical-Animal.**

> **Counterfactual honesty.** IGF-1R inhibitors (linsitinib, others) were tested broadly in **Ewing sarcoma** with a famous arc — striking individual responses, disappointing overall trial results, no durable biomarker. So "IGF-1R is a target" must carry that scar: the redesign question is *which CIC-DUX4 subset has the autocrine loop active* (a biomarker problem), not "give everyone an IGF-1R inhibitor." The lung-metastatic phenotype of the model is a notable echo of this patient's lung-only relapse pattern.

### 3. CIC-DUX4 has *proficient* DNA repair / POLE upregulation
**npj Precision Oncology 2025** (s41698-025-00985-8). CIC::DUX4 sarcomas feature upregulated POLE and proficient DNA repair. Tier: **translational/Preclinical.** This reframes V2 (the tumor is not repair-deficient — don't expect a BRCA-like synthetic-lethal opening) and partially explains chemo-resistance patterns; it also strengthens the **WEE1/replication-stress** angle (force damage past a competent repair system by removing the checkpoint).

### 4. A chromatin-dependency map already exists
**CIC-DUX4 Chromatin Profiling Reveals New Epigenetic Dependencies and Actionable Therapeutic Targets** (PMC10814785; data **GSE248040**). Real ChIP-seq + dependency data underpinning the V3 epigenetic angle — i.e., the "is the epigenetic dependency real?" question the forensics doc raised is partly answerable from already-public data.

---

## Verified accession / citation tables (supersede the `[VERIFY]` flags in the companion docs)

### Docking targets (in-silico Track C) — confirmed PDB structures
| Target | PDB ID | What it is | Use |
|---|---|---|---|
| BRD4 BD1 | **3MXF** | First bromodomain of human BRD4 + JQ1 | Dock BETi / dietary BRD4 candidates; quantify concentration mismatch |
| EZH2 | **4MI0** | EZH2 + tazemetostat (EPZ-6438) | EZH2i docking; comparators 5LS6 (CPI-1205), 5HYN (UNC1999) |
| CDK6 | **5L2I** | Human CDK6 + palbociclib | CDK4/6i docking (CDK4 fold ~identical; selectivity via ATP-pocket non-conserved elements) |

### Transcriptomic data (in-silico Tracks F/G) — confirmed GEO datasets
| GEO | Content | Use |
|---|---|---|
| **GSE60740** | IB120 patient-derived CIC-DUX4 cells **± CIC-DUX4 silencing** | **Best input for LINCS/CMap signature reversal** — the fusion-on vs fusion-off contrast *is* the CIC-DUX4 signature |
| **GSE248040** | CIC-DUX4 chromatin profiling (ChIP-seq) | Super-enhancer / BRD4 occupancy map; epigenetic-dependency leads |
| GSE241369, GSE108026, GSE108027, GSE165032, GSE234092 | CIC-DUX4 / related RNA-seq | Signature construction, GSEA, cross-validation |

### Real CIC-DUX4 cell lines (for anyone validating; and a DepMap caveat)
**Kitra-SRS** (PMID 31676869), **NCC-CDS2-C1**, **NCC-CDS-X1 / -X3**, **NCC_CDS1_X1_C1**, **IB120**. These are predominantly patient-derived (largely Japanese-cohort) lines with Cellosaurus STR profiles. **Practical note:** they are likely **absent from DepMap/CCLE** — so the in-silico doc's caveat ("DepMap CIC-DUX4 coverage may be zero; use Ewing lines as proxy") stands. But published drug/RNAi screens on these lines exist (e.g., the 1,134-compound FDA screen on Kitra-SRS), so dependency data is obtainable outside DepMap.

### Clinical anchors — confirmed
| Claim | Verified |
|---|---|
| Tazemetostat FDA accelerated approval | **2020-01-23**, epithelioid sarcoma, INI1/SMARCB1-negative, ORR **15%**, study EZH-202 / NCT02601950 ✓ (matches `docs/05`) |
| SARC028 | Tawbi et al., **Lancet Oncol 2017**, **PMID 28988646**; primary endpoint **not met**; responders concentrated in UPS/DDLPS ✓ |

### Condensate precedent — confirmed (basis for the LLPS forward hypothesis)
EWS-FLI1 / fusion-TF transcriptional condensates are real and active research: **Boija et al., Cell 2018** (activation domains drive gene activation via phase separation); **Chong et al., Science 2018** + 2022 follow-up (LCD interactions tune oncogenic transcription); **PNAS 2025** (EWS::FLI1 phase separation modulated by its DNA-binding domain). CIC-DUX4 LLPS itself is **not yet demonstrated** — that is precisely the in-silico Track B forward experiment (predict before claiming). Tier for CIC-DUX4: **Theoretical/Mechanistic**; for the EWS-FLI1 precedent: **Preclinical**.

---

## Strongest redesigned trials (curated from `counterfactual-trial-forensics.md`, now grounded)

1. **WEE1 inhibitor + DNA-damaging chemo (NEW, best-grounded).** CIC-DUX4-specific dependency (PMC8986087) + the patient's imminent ifosfamide. The combination the cell-line data predicts, never trialed in CIC. *Falsifier:* no replication-stress/WEE1 dependency in the relapse clone.
2. **EZH2i repositioned as an MHC-I priming agent, not a cytotoxic.** PRC2 *survival* dependency in CIC-DUX4 is assumed, not proven; the H3K27me3→antigen-presentation de-repression mechanism holds regardless. Sequence EZH2i → checkpoint/NK (V3→V4 bridge). Test the survival dependency in DepMap-style data first.
3. **BET *degrader* (PROTAC) rather than BET inhibitor**, ± CDK7/9, to defeat the BRD4-reaccumulation/feedback escape that blunted BETi monotherapy.
4. **NK-first immunotherapy** exploiting the MHC-I-low immune-selected relapse clone, *before* epigenetic MHC-I restoration (resolves the NK-vs-MHC-I sequencing tension by temporal separation).
5. **Transcriptional-condensate disruption** as a distinct attack mode (predict LLPS in silico → if positive, target the acidic/LCD interface). Delivery, not target validity, is the real gap for fusion-directed approaches.

## First three experiments to actually run (no wet lab, no GPU, junction-independent)

1. **LINCS / CMap signature reversal** using **GSE60740** (CIC-DUX4 on vs off) → rank compounds that produce the anti-correlated signature. Drug-repurposing simulation in a browser/API.
2. **Dependency mining**: confirm whether any CIC-DUX4 line is in DepMap (likely not) → fall back to Ewing-like lines + the published Kitra-SRS / NCC-CDS screens; cross-reference WEE1, IGF-1R, BRD4, CDK4/6, EZH2.
3. **Boolean/ODE network model** of RAS/ERK → CIC-de-repression → ETV1/4/5 → BRD4/super-enhancer → CCND2/CDK4 → proliferation; simulate single + combination node knockouts; check whether the model independently predicts the BETi-feedback escape and the WEE1/replication-stress node.

---

## What grounding did NOT resolve
- **CIC-DUX4 LLPS is still unproven** — Track B is a genuine open experiment, not a confirmation.
- **No DepMap CRISPR screen of a confirmed CIC-DUX4 line** appears to exist — dependency claims rest on a small number of patient-derived lines and targeted (not genome-wide CRISPR) studies.
- **The patient's fusion is unconfirmed** — every fusion-*directed* item (junction ASO, junction vaccine, condensate-interface targeting if junction-dependent) remains POSSIBLY INAPPLICABLE until long-read re-sequencing resolves status (catalog Forward Hypothesis 5). The WEE1, IGF-1R-subset, BETi/EZH2i/CDK4-6i, and immune items are fusion-agnostic and survive that uncertainty.
- **EMA status** for tazemetostat and the other agents was not checked in this pass (FDA only).

## Citations (live-verified 2026-05-29)
- WEE1 vulnerability: JCI Insight 2022, PMC8986087 (bioRxiv 2021.06.21.448439).
- IGF-1R / Kitra-SRS: Nakai et al., Sci Rep 2019, PMID 31676869 / PMC6825133.
- POLE / proficient repair: npj Precision Oncology 2025, s41698-025-00985-8.
- Chromatin dependencies: PMC10814785, data GSE248040.
- Signature-ready dataset: GSE60740 (IB120 ± CIC-DUX4).
- PDB: 3MXF (BRD4 BD1+JQ1), 4MI0 (EZH2+tazemetostat), 5L2I (CDK6+palbociclib).
- Tazemetostat: FDA accelerated approval 2020-01-23, NCT02601950 (EZH-202).
- SARC028: Tawbi et al., Lancet Oncol 2017, PMID 28988646.
- Condensate precedent: Boija et al. Cell 2018; Chong et al. Science 2018/2022; PNAS 2025 (doi 10.1073/pnas.2221823122).
