# 05 — Proposed Attack Vectors

> **For sub-agents:** This file is the operational backbone of the simulation. Read carefully.
>
> Compounds listed below are **candidates** for investigation, not endorsements. Each compound name in this file is shorthand for "this molecule has been studied in some cancer context and is mechanistically plausible against this vector's target layer." Direct evidence in CIC-DUX4 sarcoma is **rare to nonexistent** for almost every dietary compound — agents must tag this honestly. Padding the lists with weakly-supported entries makes the output worse, not better.
>
> Evidence tier vocabulary (mandatory on every recommendation, defined in detail in `06-agent-architecture.md`):
> **Established · Clinical-Trial · Preclinical-Animal · Preclinical-Cell · Mechanistic · Dietary-Observational**

---

## Overview

Four parallel, complementary attack vectors. Each targets a different layer of the CIC-DUX4 oncogenic program. They are **not alternatives** — the working hypothesis is that they compose, and that no single vector is sufficient on its own.

The analogy: you don't fix a long-running production incident with a single rollback when the bug has already corrupted downstream state. You patch the running process, throttle the bad calls, harden the surrounding system, and improve monitoring — all at once.

---

## Vector 1 — Rate Limiting

**Goal: reduce how fast the oncogenic loop executes and how much oncogenic output it produces per cycle.**

This vector does NOT attempt to fix the CIC-DUX4 fusion. It targets the amplification context — the upstream signals that fuel the loop, the BRD4 machinery that amplifies the loop's output, and the cell-cycle machinery that executes its commands.

### Mechanism Targets

**A. Upstream RAS/ERK dampening** — reduce signal amplitude feeding into the broken loop. Lower ERK activity → less co-activator and BRD4 recruitment to fusion-driven super-enhancers.

| Candidate | Proposed mechanism | Evidence in CIC-DUX4 | Evidence in cancer broadly |
|---|---|---|---|
| Quercetin | RTK/RAS pathway inhibition; multiple kinase targets at high concentrations | None direct | Preclinical-Cell across many cancers; bioavailability is the limiting factor |
| Omega-3 EPA/DHA | Alters membrane lipid raft composition → impairs RAS membrane clustering | None direct | Preclinical-Animal + Dietary-Observational |
| Berberine | AMPK activation → MAPK suppression downstream | None direct | Preclinical-Cell; oral bioavailability ~1% |
| Lycopene | ERK pathway downregulation reported | None direct | Dietary-Observational (prostate cancer mostly) |

**B. BRD4 / super-enhancer throttling** — the fusion drives ETS targets via BRD4 occupancy of super-enhancers. Dietary BET-pathway modulators are weak compared to clinical BET inhibitors (JQ1, OTX015), but mechanistically aligned.

| Candidate | Proposed mechanism | Evidence in CIC-DUX4 | Notes |
|---|---|---|---|
| EGCG (green tea catechin) | Reported direct BRD4 bromodomain binding; H3K27ac modulation | None direct | Preclinical-Cell; oral bioavailability poor; matcha-level intakes are far below experimental concentrations |
| Curcumin | Reported BRD4-chromatin interaction disruption; broad polypharmacology | None direct | Preclinical-Cell; bioavailability is the dominant issue (see "Bioavailability caveats" below) |
| Apigenin | Reduces ETS factor expression in some cell lines | None direct | Preclinical-Cell |
| Kaempferol | Polyphenol; loosely BRD/MYC axis-related | None direct | Mechanistic |

**C. Downstream cell-cycle friction** — slow CDK4/CCND1 execution. Will not fix the upstream driver but reduces the rate at which the loop completes a cycle.

| Candidate | Proposed mechanism | Evidence in CIC-DUX4 | Notes |
|---|---|---|---|
| Genistein | CDK inhibition; G2/M arrest in cell lines | None direct | Preclinical-Cell; estrogenic activity is a real consideration |
| Fisetin | Reported ETS inhibition; CDK4 suppression | None direct | Preclinical-Cell + senolytic literature |
| Luteolin | Cell-cycle modulator | None direct | Preclinical-Cell |
| Selenium | Apoptosis threshold modulation; selenoprotein cofactor | None direct | Preclinical + Dietary-Observational; narrow safety window |
| Zinc | DNA repair fidelity + cell-cycle modulation | None direct | Preclinical; large supplemental doses interfere with copper |

### Food Sources (for the V1 Food Specialist)

| Compound | Richer dietary sources |
|---|---|
| Quercetin | Capers, red onions (raw, outer layers), kale, elderberries, lovage |
| Omega-3 EPA/DHA | Atlantic mackerel, sardines, wild salmon, herring, oysters |
| Omega-3 ALA (plant) | Flaxseeds, chia seeds, walnuts, hemp seeds — note: ALA→EPA conversion in humans is ~5–10%; ALA is not a substitute for marine EPA/DHA |
| EGCG | Matcha, brewed green tea (3–5 min, 70–80°C preserves catechins) |
| Curcumin | Turmeric; bioavailability is the issue (see below) |
| Sulforaphane precursor (glucoraphanin) | Broccoli sprouts (much higher than mature broccoli); needs myrosinase activation by chopping or chewing |
| Fisetin | Strawberries, mangoes, apples (skin), persimmons |
| Selenium | Brazil nuts (a small number provide a typical daily requirement; excess is toxic — agents must not recommend "more is better"), sardines, eggs |
| Berberine | Primarily supplemental; trace amounts in barberries |

### Bioavailability Caveats (Mandatory Reading)

- **Curcumin + piperine**: The widely-cited "~2000% bioavailability increase" comes from Shoba et al., *Planta Medica* 1998 — a single-dose pharmacokinetic study, n=10 healthy volunteers, 2 g curcumin + 20 mg piperine. The curcumin-only control arm produced serum levels below the assay's limit of detection, so the "20×" number is computed against a near-zero baseline. The directional finding (piperine increases curcumin absorption) is real and reproduced; the **specific 2000% figure should not be cited as a universal multiplier**.
- **EGCG, quercetin, resveratrol**: Oral bioavailability is poor and highly variable. Plasma concentrations achievable from diet are typically 10–1000× below concentrations used in cell-line studies. Agents must flag when a recommended mechanism requires concentrations not achievable from food.
- **Most polyphenols are extensively metabolized** by gut microbiota and phase II enzymes. The metabolites — not the parent compound — are what reach tissue. This is rarely accounted for in mechanism-from-cell-line claims.

### What Vector 1 Cannot Do

- Reverse the CIC-DUX4 translocation
- Eliminate fusion protein from cells that already carry it
- Substitute for a clinical BET inhibitor or CDK4/6 inhibitor at the concentrations tested in trials
- Produce CR/PR responses as monotherapy at dietary doses (no published evidence supports this)

---

## Vector 2 — Compiler Protection

**Goal: reduce the rate at which neighboring at-risk cells acquire the same translocation event.**

The translocation has already happened in the index tumor. The microenvironment around the tumor — flooded with ROS, hypoxia, inflammatory cytokines — actively elevates DSB rates in surrounding cells. Mesenchymal progenitor cells in that microenvironment are the cell-of-origin population for sarcoma. Vector 2 attempts to reduce that local risk.

This vector is the most **systemic** and the most **mechanistically generic** — it overlaps heavily with general "reduce oxidative stress / support DNA repair" cancer prevention literature. Agents should be honest that this is upstream prevention, not tumor-directed therapy.

### Mechanism Targets

**A. Reduce DSB frequency** — primarily by reducing the local ROS burden.

| Candidate | Proposed mechanism | Tier |
|---|---|---|
| Vitamin C | Direct radical scavenging; cofactor for collagen and α-KG-dependent dioxygenases | Mechanistic (dietary doses); some clinical interest in high-dose IV (not dietary) |
| Vitamin E (mixed tocopherols) | Lipid-phase radical scavenging | Mechanistic |
| NAC | Glutathione precursor | Preclinical-Cell; note: in mouse melanoma models, NAC accelerated metastasis (Sayin et al., *Sci Transl Med* 2014) — flag as ambiguous |
| Dietary polyphenols broadly | Multi-target antioxidant + signaling | Dietary-Observational |

**B. Improve DNA repair fidelity** — cofactors for NHEJ and HR machinery.

| Compound | Proposed role | Notes |
|---|---|---|
| Zinc | Structural cofactor for many DNA repair proteins (Ku, p53 zinc finger) | Deficiency clearly impairs repair; supplementation beyond RDA in repleted individuals has no documented additional benefit |
| Folate + B12 | Nucleotide-pool maintenance; deficiency causes uracil misincorporation → DSBs | Both deficiency and *excess folate* have been associated with cancer outcomes — supplementation is not unambiguously protective |
| Selenium | Thioredoxin reductase cofactor → redox environment for repair enzymes | Narrow safety window |
| Magnesium | DNA polymerase / repair enzyme cofactor | Deficiency relevant; supplementation in repleted individuals has thin evidence |

**C. Reduce replication stress** — adequate nucleotide pools, fewer aberrant proliferation cycles.

| Compound | Proposed mechanism |
|---|---|
| Folate, B12, B6 | Nucleotide synthesis substrates / cofactors |
| Omega-3 EPA/DHA | Anti-inflammatory → fewer aberrant proliferation signals in microenvironment |

**D. Reduce Topoisomerase II stress** — high transcriptional activity creates mechanical DSBs. Reducing transcriptional load on at-risk loci (which Vector 1 partly does upstream) reduces Topo II throughput at those loci. This is mostly a Vector 1↔V2 synergy, not a standalone V2 intervention.

### Key Caveat for Sub-Agents

The "antioxidants prevent cancer" hypothesis has a famously mixed clinical record:
- **β-carotene supplementation** *increased* lung-cancer incidence in heavy smokers (ATBC, CARET trials).
- **Vitamin E supplementation** *increased* prostate-cancer incidence in SELECT.
- Whole-food antioxidant intake (fruits, vegetables) shows protective associations in epidemiology; isolated high-dose supplement intake does not.

The Anti-Inflammatory Specialist must address this explicitly in their output — recommending "high-dose antioxidants" generically is exactly the kind of output that this simulation should *not* produce.

### What Vector 2 Cannot Do

- Affect tumor cells that already carry the fusion (that's V1/V3/V4)
- Quantify the actual risk reduction in any individual (the absolute risk of *a second CIC-DUX4 translocation* in someone with an existing tumor is unknown)
- Replace standard prevention guidance from oncology

---

## Vector 3 — Hot Patching

**Goal: restore the break condition inside cells that already carry the fusion, by targeting the compiled output (fusion protein), the amplification machinery, the downstream chromatin state, and the differentiation programs the loop has silenced.**

Vector 3 is where the highest-impact interventions live, but also where the dietary contribution is the weakest and the clinical/experimental contribution is the strongest. Be honest in the split.

### Approaches — Clinical/Experimental (flag separately in V3 output)

**3a. CRISPR — Edit the Source Code**
- Conceptual ideal: excise the CIC-DUX4 junction. **Not clinically feasible** for solid tumors today — delivery efficiency to the tumor compartment remains the unsolved problem.
- Tier: Theoretical. LNP delivery is improving (now standard for liver-targeted therapies); solid-tumor targeting remains aspirational.

**3b. Antisense Oligonucleotides (ASOs)**
- Target: CIC-DUX4 mRNA at the fusion junction (sequence unique to the fusion).
- Mechanism: ASO binds → RNaseH-mediated transcript degradation.
- Status: No clinical-stage ASO specific to CIC-DUX4 that I can find. ASOs are clinically established for other indications (SMA, DMD); fusion-junction ASOs are an active research area.
- Tier: Theoretical / Preclinical at best for CIC-DUX4 specifically.

**3c. EZH2 inhibitors (clinical)**
- Tazemetostat: FDA accelerated approval (2020-01-23) for epithelioid sarcoma; EMA approval status should be verified as it may differ. Not approved for CIC-rearranged sarcoma by either authority.
- Mechanistic rationale extrapolates from PRC2 dependency in BAF-disrupted sarcomas; direct CIC-DUX4 efficacy data is limited.
- Tier: Established (epithelioid sarcoma) / Clinical-Trial (other sarcomas).

**3d. BET inhibitors (clinical)**
- JQ1 (preclinical tool), OTX015, BMS-986158, etc.
- Strong preclinical rationale in fusion-driven sarcomas; Phase I/II results so far have been modest as monotherapy.
- Tier: Clinical-Trial.

**3e. CDK4/6 inhibitors (clinical)**
- Palbociclib, ribociclib, abemaciclib — FDA- and EMA-approved for HR+ breast cancer (specific approved indications and labeling vary by jurisdiction; verify current status).
- Sarcoma trials are smaller and more mixed; rationale (CCND1/CDK4 dependency in CIC-DUX4) is solid.
- Tier: Established (breast) / Clinical-Trial (sarcoma).

**3f. PROTAC degraders**
- Bifunctional molecules that recruit a target protein to the proteasome.
- BET-PROTACs (ARV-771, dBET6) and others are in preclinical/early-clinical development.
- A CIC-DUX4-specific PROTAC would be ideal but is not currently published as far as I can tell.
- Tier: Preclinical / Theoretical (for CIC-DUX4).

**3g. Differentiation therapy (clinical)**
- ATRA (all-trans retinoic acid) is the canonical example — transformative in APL (PML-RARα). Whether it generalizes to other fusion-driven sarcomas is poorly established.
- Combinations of EZH2i + HDACi are mechanistically attractive but in early study.
- Tier: Established (APL) / Theoretical (CIC-DUX4).

### Approaches — Naturally Achievable (Vector 3's dietary track)

Dietary support for Vector 3 is **adjunctive at best**. Do not present these as standalone interventions.

| Goal | Compound | Sources | Mechanistic basis | Tier |
|---|---|---|---|---|
| HDAC modulation | Sulforaphane | Broccoli sprouts (chopped/chewed to activate myrosinase) | Weak class-I HDAC inhibitor in cell lines; far weaker than clinical HDACi | Preclinical-Cell |
| HDAC modulation | Butyrate (SCFA) | Colonic fermentation of dietary fiber (resistant starch, inulin); also dairy butter at modest levels | HDAC inhibitor at millimolar colonic concentrations; systemic concentrations far lower | Preclinical |
| Retinoic acid signaling | Vitamin A / β-carotene | Liver, egg yolk; carrots, sweet potato, leafy greens | Substrate for endogenous retinoic acid synthesis | Dietary-Observational; β-carotene supplementation has documented harms in smokers (see V2 caveat) |
| Vitamin D axis | Vitamin D3 | Sunlight, fatty fish, supplementation in deficient individuals | Modulates VDR-target gene expression including some differentiation programs | Mechanistic; deficiency correction has clearer evidence than supplementation in replete individuals |
| EZH2 modulation | EGCG, Quercetin | Green tea, capers, red onions | Weak EZH2 modulators in cell lines | Preclinical-Cell |
| Anti-fusion-condensate (speculative) | — | — | No dietary compound has known anti-condensate activity for CIC-DUX4 | Out of scope |

### Critical V3 → V4 Bridge

Several V3 interventions upregulate MHC-I expression on tumor cells, which is the prerequisite for V4 immune clearance. **Every V3 intervention with documented MHC-I upregulation must be flagged in the V3 output for the orchestrator and V4 lead.** The cleanest examples are EZH2 inhibitors and (clinical) HDAC inhibitors. Whether sulforaphane / dietary butyrate achieve sufficient systemic exposure to upregulate MHC-I in tumor tissue is unestablished — flag honestly.

### What Vector 3 Cannot Do via Diet Alone

- Eliminate the CIC-DUX4 fusion protein
- Reproduce the effect of a clinical EZH2 or BET inhibitor
- Force differentiation at meaningful tumor scale (this is the role of clinical agents)

---

## Vector 4 — Immune Watchdog / Garbage Collector

**Goal: enable immune surveillance and clearance of cells weakened by V1 and made visible by V3.**

### Why Immune Surveillance Should Work — And Why It Fails

The CIC-DUX4 junction is a neoantigen (a peptide sequence not in any normal proteome). The immune system *should* see it. Multiple evasion mechanisms have been documented in fusion-driven sarcomas:

1. **MHC-I downregulation** — fewer peptides displayed; the cell "goes quiet on the network"
2. **PD-L1 upregulation** — "do not kill" signal raised
3. **Immunosuppressive microenvironment** — Tregs, MDSCs, TGF-β
4. **Antigen escape variants** — under immune pressure, junction-loss variants get selected

Direct evidence for each mechanism in CIC-DUX4 specifically is more limited than in melanoma or NSCLC. Agents should not assume mechanisms documented in immunogenic tumors automatically apply.

### Interventions

**4a. Checkpoint Inhibitors (clinical)**
- PD-1/PD-L1 blockade — pembrolizumab, nivolumab.
- Sarcoma response rates to checkpoint inhibitor monotherapy have been modest in trials (SARC028, etc.), better in selected subtypes (UPS, DDLPS); CIC-rearranged is too rare for dedicated trials.
- Tier: Established (multiple cancers) / Clinical-Trial (sarcoma generally) / no direct CIC-DUX4 data.

**4b. Epigenetic Priming Bridge (V3 → V4)**
- EZH2i and HDACi upregulate MHC-I on tumor cells, restoring visibility.
- The combination strategy (epigenetic priming → checkpoint inhibitor) is the most active area in sarcoma immunotherapy trials.
- Tier: Clinical-Trial.
- Dietary contribution (sulforaphane, butyrate) is **mechanistically aligned but at much weaker exposure**.

**4c. NK Cell Activation**
- NK cells use "missing-self" logic: they attack cells with low MHC-I.
- CIC-DUX4 cells that downregulate MHC-I to hide from T-cells become paradoxically more visible to NK cells.
- Clinical NK activators: IL-15 agonists, NK engagers (in trials).
- Dietary support: vitamin D status (correction of deficiency has clearer evidence than supplementation in replete individuals); zinc status; gut-microbiome diversity has documented systemic effects on NK function.
- Tier: Mechanistic / Clinical-Trial.

**4d. CAR-T (clinical, experimental in solid tumors)**
- Engineered T-cells targeting CIC-DUX4 junction peptide.
- Solid-tumor CAR-T penetration remains the unsolved problem; no published CIC-DUX4-specific CAR-T to my knowledge.
- Tier: Theoretical.

**4e. Neoantigen Vaccine (clinical, experimental)**
- Patient-specific peptide vaccine targeting the patient's exact junction sequence.
- Junction sequence varies across patients (see file 02) — pan-CIC-DUX4 vaccines would need to cover multiple variants.
- Tier: Theoretical / Preclinical.

### Dietary Support

| Goal | Compounds | Sources | Tier |
|---|---|---|---|
| NK cell activity | Vitamin D3 (correct deficiency), zinc (correct deficiency) | Sunlight, fatty fish; oysters, pumpkin seeds | Mechanistic; replete-individual supplementation has thin evidence |
| Gut microbiome (systemic immune modulation) | Diverse fiber, fermented foods | Vegetables, legumes, whole grains, yogurt, kefir, sauerkraut, kimchi | Dietary-Observational (Akkermansia and Bifidobacterium abundance associated with checkpoint inhibitor response in melanoma — *not* CIC-DUX4) |
| Anti-inflammatory microenvironment | Omega-3, curcumin, polyphenols | Fatty fish, turmeric, berries, green tea | Mechanistic + Dietary-Observational |
| Possible MHC-I upregulation | Sulforaphane, butyrate (from fermented fiber) | Broccoli sprouts, high-fiber diet | Preclinical |

### What Vector 4 Cannot Do via Diet Alone

- Substitute for checkpoint inhibitors
- Generate a tumor-specific immune response (that requires either priming via V3 or active immunization)
- Overcome a deeply immunosuppressed tumor microenvironment

---

## Vector Interaction Map

```
V2 (Compiler Protection)
   └─ Reduces new translocation events in at-risk neighbor cells
   └─ Shares antioxidant / cofactor compounds with V1

V1 (Rate Limiting) ⇄ V2 (Compiler Protection)
   └─ Many compounds serve both (Quercetin, Omega-3, Selenium, Zinc)
   └─ Reducing transcriptional load (V1) reduces Topo II DSBs at active loci (V2)

V3 (Hot Patching)
   └─ EZH2i / HDACi (clinical) restore MHC-I → ENABLES V4
   └─ Sulforaphane / butyrate are weak dietary analogues — flag, don't oversell
   └─ Differentiation therapy slows the loop → cells become more clearable by V4

V4 (Immune Watchdog)
   └─ Most effective after V3 epigenetic priming has restored MHC-I visibility
   └─ NK cells catch the MHC-I-low cells that escaped T-cell arm
```

### Optimal Sequencing Hypothesis

This is a hypothesis about ordering, not a clinical protocol:

1. **V2 — continuously** (upstream prevention; lowest risk profile)
2. **V1 — continuously** (loop throttling; mostly dietary; supplements with care)
3. **V3 — clinical/experimental track, when indicated** (this is where standard-of-care lives; dietary track is adjunctive)
4. **V4 — clinical, after V3 priming**

---

## Cross-Vector Compound Table (for the Orchestrator)

The ✓ marks indicate "this compound has been discussed as relevant to this vector in this file." It is not a claim of established efficacy. Each entry must still carry an evidence tier in the orchestrator's final output.

| Compound | V1 | V2 | V3 | V4 | Strongest evidence claim |
|---|---|---|---|---|---|
| Sulforaphane | ✓ | — | ✓ | ✓ | Preclinical-Cell HDAC modulation |
| Quercetin | ✓ | ✓ | — | — | Preclinical-Cell, bioavailability-limited |
| EGCG | ✓ | ✓ | ✓ | — | Preclinical-Cell, bioavailability-limited |
| Omega-3 EPA/DHA | ✓ | ✓ | — | ✓ | Dietary-Observational + Mechanistic |
| Curcumin | ✓ | ✓ | — | ✓ | Preclinical-Cell, bioavailability-limited |
| Butyrate (via fermented fiber) | — | — | ✓ | ✓ | Preclinical (colonic); systemic exposure questionable |
| Vitamin D3 | — | — | ✓ | ✓ | Mechanistic + Dietary-Observational; correct deficiency first |
| Selenium | ✓ | ✓ | — | — | Narrow safety window |
| Zinc | ✓ | ✓ | — | ✓ | Correct deficiency; excess interferes with copper |
| Fisetin | ✓ | — | — | — | Preclinical-Cell |
| β-carotene / Vit A | — | — | ✓ | — | Dietary-Observational; **caution: supplementation harmful in smokers** |

---

## Standard-of-Care Awareness for All Vectors

CIC-rearranged sarcoma standard of care today typically involves multi-agent chemotherapy (often Ewing-like regimens: VDC/IE — vincristine, doxorubicin, cyclophosphamide, alternating with ifosfamide and etoposide), plus surgery and radiation where applicable. Response rates are lower than in Ewing sarcoma.

**Interactions agents must flag:**
- High-dose antioxidants (NAC, vitamin C, vitamin E) may theoretically interfere with chemotherapy mechanisms that rely on ROS (doxorubicin, ifosfamide). Clinical data are mixed but the concern is real enough that medical oncology guidelines generally advise against high-dose antioxidant supplementation during cytotoxic chemotherapy.
- Curcumin, EGCG, quercetin, and others have documented cytochrome P450 interactions that could alter drug metabolism — relevant for any concurrent medication.
- Grapefruit-like CYP3A4 interactions are *not* the only concern; dietary compounds at supplement-level doses are pharmacologically active.

Any dietary recommendation surfaced by this simulation must carry the orchestrator-level annotation: "potential interactions with standard-of-care chemotherapy and concurrent medications — must be reviewed by the patient's oncologist before any change."
