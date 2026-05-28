---
name: sarcoma-vector-context
description: Loads the compound list, mechanism targets, and caveats for one attack vector (V1 Rate Limiting, V2 Compiler Protection, V3 Hot Patching, V4 Immune Watchdog). Invoke with argument `v1`, `v2`, `v3`, or `v4`. Use instead of loading all of 05-attack-vectors.md when an agent only needs one vector's content. Source: docs/05-attack-vectors.md.
---

# Vector Context Loader

This skill returns only the vector-specific section an agent needs. Pass the vector name as an argument: `v1`, `v2`, `v3`, or `v4`.

**Default behavior if no argument:** return the cross-vector compound table and the standard-of-care chemotherapy note (the parts that every vector lead and the orchestrator need).

---

## V1 — Rate Limiting

**Goal:** reduce how fast the oncogenic loop executes and how much oncogenic output it produces per cycle. V1 does **not** attempt to fix the CIC-DUX4 fusion.

### A. Upstream RAS/ERK dampening

| Candidate | Mechanism | CIC-DUX4 evidence | Notes |
|---|---|---|---|
| Quercetin | RTK/RAS inhibition; multi-kinase at high conc | None direct | Preclinical-Cell; bioavailability is the limit |
| Omega-3 EPA/DHA | Lipid raft / RAS membrane clustering | None direct | Preclinical-Animal + Dietary-Observational |
| Berberine | AMPK → MAPK suppression | None direct | Preclinical-Cell; oral bioavailability ~1% |
| Lycopene | ERK downregulation | None direct | Dietary-Observational (prostate mostly) |

### B. BRD4 / super-enhancer throttling

| Candidate | Mechanism | Notes |
|---|---|---|
| EGCG | Reported direct BRD4 BD1 binding; H3K27ac modulation | Preclinical-Cell; bioavailability poor |
| Curcumin | BRD4-chromatin disruption; polypharmacology | Preclinical-Cell; bioavailability is dominant issue |
| Apigenin | Reduces ETS factor expression in some lines | Preclinical-Cell |
| Kaempferol | BRD/MYC axis-related | Mechanistic |

### C. Downstream cell-cycle friction (CDK4 / CCND1)

| Candidate | Mechanism | Notes |
|---|---|---|
| Genistein | CDK inhibition; G2/M arrest | Preclinical-Cell; estrogenic activity real |
| Fisetin | ETS inhibition; CDK4 suppression | Preclinical-Cell + senolytic literature |
| Luteolin | Cell-cycle modulator | Preclinical-Cell |
| Selenium | Apoptosis threshold; selenoprotein cofactor | Narrow safety window |
| Zinc | DNA repair + cell-cycle modulation | Excess interferes with copper |

### V1 Food Sources

| Compound | Sources |
|---|---|
| Quercetin | Capers, red onions (raw, outer layers), kale, elderberries, lovage |
| Omega-3 EPA/DHA | Atlantic mackerel, sardines, wild salmon, herring, oysters |
| Omega-3 ALA | Flaxseeds, chia, walnuts, hemp (ALA→EPA ~5–10%; not a substitute) |
| EGCG | Matcha, brewed green tea (3–5 min, 70–80°C preserves catechins) |
| Curcumin | Turmeric (bioavailability is the issue) |
| Sulforaphane (precursor: glucoraphanin) | Broccoli sprouts; needs myrosinase via chop/chew |
| Fisetin | Strawberries, mangoes, apples (skin), persimmons |
| Selenium | Brazil nuts (1–2/day delivers RDA; excess toxic), sardines, eggs |
| Berberine | Supplemental primarily; trace in barberries |

### V1 Bioavailability Caveats (Mandatory)

- **Curcumin + piperine "2000% boost"** is from Shoba et al., *Planta Medica* 1998 — single-dose PK, n=10, curcumin-only control below LOD. Directional finding (piperine ↑ curcumin absorption) is real and reproduced; **the specific 2000% multiplier must not be cited as universal**.
- **EGCG, quercetin, resveratrol**: oral bioavailability is poor; dietary plasma concentrations are typically 10–1000× below cell-line study concentrations. Flag when a mechanism requires unachievable concentrations.
- **Most polyphenols** are extensively metabolized by gut microbiota and phase II enzymes; metabolites — not parent compound — reach tissue.

### What V1 Cannot Do

Reverse the translocation · eliminate fusion protein · substitute for a clinical BET or CDK4/6 inhibitor · produce CR/PR as monotherapy at dietary doses.

---

## V2 — Compiler Protection

**Goal:** reduce the rate at which neighboring at-risk mesenchymal progenitor cells acquire the same translocation. Most systemic and most mechanistically generic vector. Upstream prevention, not tumor-directed therapy.

### A. Reduce DSB frequency (lower local ROS)

| Candidate | Mechanism | Tier |
|---|---|---|
| Vitamin C | Radical scavenging; cofactor for collagen and α-KG-dependent dioxygenases | Mechanistic (dietary); high-dose IV is clinical, not dietary |
| Vitamin E (mixed tocopherols) | Lipid-phase radical scavenging | Mechanistic |
| NAC | Glutathione precursor | Preclinical-Cell; **Sayin 2014: NAC accelerated metastasis in mouse melanoma — flag as ambiguous** |
| Dietary polyphenols broadly | Multi-target antioxidant + signaling | Dietary-Observational |

### B. Improve DNA repair fidelity

| Compound | Role | Notes |
|---|---|---|
| Zinc | Ku70/Ku80, p53 zinc finger | Deficiency impairs repair; supplementation in repleted = no additional benefit |
| Folate + B12 | Nucleotide pool; deficiency → uracil misincorporation | Both deficiency *and excess folate* associated with cancer outcomes |
| Selenium | Thioredoxin reductase cofactor | Narrow safety window |
| Magnesium | DNA polymerase / repair enzyme cofactor | Deficiency relevant; replete-supplementation evidence thin |

### C. Reduce replication stress

| Compound | Mechanism |
|---|---|
| Folate, B12, B6 | Nucleotide synthesis cofactors |
| Omega-3 EPA/DHA | Anti-inflammatory → fewer aberrant proliferation signals |

### D. Reduce Topoisomerase II stress

High transcriptional load creates mechanical DSBs. Reducing transcriptional load on at-risk loci (which V1 partly does) reduces Topo II throughput there. Mostly a V1↔V2 synergy, not a standalone V2 intervention.

### V2 Critical Caveat — Antioxidants Have a Mixed Trial Record

- **β-carotene supplementation** *increased* lung-cancer incidence in heavy smokers (ATBC, CARET).
- **Vitamin E supplementation** *increased* prostate-cancer incidence (SELECT).
- Whole-food antioxidant intake shows protective epidemiology; isolated high-dose supplements do not.

Generic "take antioxidants" is the exact output V2 must NOT produce.

### What V2 Cannot Do

Affect tumor cells already carrying the fusion · quantify individual risk reduction · replace standard prevention guidance.

---

## V3 — Hot Patching

**Goal:** restore the break condition inside cells that already carry the fusion. **Most clinically-loaded vector. Dietary contribution is the weakest. Be honest in the split.**

### Clinical / Experimental Track — flag separately

| # | Approach | CIC-DUX4 status | Tier |
|---|---|---|---|
| 3a | CRISPR (excise junction) | Not clinically feasible for solid tumors (delivery problem) | Theoretical |
| 3b | ASOs targeting CIC-DUX4 mRNA junction | No clinical-stage CIC-DUX4 ASO published; ASOs established for SMA/DMD | Theoretical / Preclinical |
| 3c | EZH2i (tazemetostat) | FDA approved 2020-01-23 for **epithelioid sarcoma**, NOT CIC-rearranged. CIC rationale extrapolates from PRC2 dependency in BAF-disrupted fusion sarcomas. | Established (epithelioid) / Clinical-Trial (other) |
| 3d | BETi (JQ1 preclinical; OTX015, BMS-986158, AZD5153 clinical) | Strong preclinical; modest monotherapy results so far | Clinical-Trial |
| 3e | CDK4/6i (palbociclib, ribociclib, abemaciclib) | FDA-approved HR+ breast; sarcoma trials smaller and mixed | Established (breast) / Clinical-Trial (sarcoma) |
| 3f | PROTACs (BET-PROTACs ARV-771, dBET6) | No published CIC-DUX4-specific PROTAC | Preclinical / Theoretical |
| 3g | Differentiation therapy (ATRA model from APL) | Generalization to fusion sarcomas poorly established | Established (APL) / Theoretical (CIC-DUX4) |

### Naturally Achievable Track (adjunctive at best)

| Goal | Compound | Sources | Mechanism | Tier |
|---|---|---|---|---|
| HDAC modulation | Sulforaphane | Broccoli sprouts (chop/chew → myrosinase) | Weak class-I HDACi in cell lines; far weaker than clinical HDACi | Preclinical-Cell |
| HDAC modulation | Butyrate (SCFA) | Colonic fermentation of resistant starch, inulin; dairy butter | HDACi at mM colonic; systemic conc much lower | Preclinical |
| Retinoic acid signaling | Vitamin A / β-carotene | Liver, egg yolk; carrots, sweet potato, leafy greens | Substrate for endogenous RA synthesis | Dietary-Observational; **β-carotene supplementation harms smokers** |
| Vitamin D axis | Vitamin D3 | Sunlight, fatty fish | Modulates VDR-target gene expression including differentiation | Mechanistic; correct deficiency first |
| EZH2 modulation (weak) | EGCG, Quercetin | Green tea, capers, red onions | Weak EZH2 modulators in cell lines | Preclinical-Cell |

### V3 → V4 Bridge — MANDATORY OUTPUT SECTION

Several V3 interventions upregulate MHC-I on tumor cells, a prerequisite for V4 immune clearance. **Every V3 intervention with documented MHC-I upregulation must be flagged at the top of the V3 output for orchestrator and V4 lead.** Cleanest examples: EZH2i and clinical HDACi. Whether sulforaphane / dietary butyrate achieve sufficient tumor exposure to upregulate MHC-I clinically is **unestablished** — say so.

### What V3 Cannot Do via Diet Alone

Eliminate the fusion protein · reproduce clinical EZH2i / BETi effect · force differentiation at meaningful tumor scale.

---

## V4 — Immune Watchdog / Garbage Collector

**Goal:** enable immune surveillance and clearance of cells weakened by V1 and made visible by V3.

### Why Surveillance Should Work — and Why It Fails

The CIC-DUX4 junction IS a neoantigen. Documented evasion mechanisms (most evidence from melanoma / NSCLC, less from sarcoma):

1. MHC-I downregulation (cell goes quiet)
2. PD-L1 upregulation ("do not kill")
3. Immunosuppressive TME (Tregs, MDSCs, TGF-β)
4. Antigen-escape variants under immune pressure

CIC-DUX4-specific data on each is limited. Do not transfer melanoma findings without flagging.

### Interventions

| # | Approach | Notes | Tier |
|---|---|---|---|
| 4a | Checkpoint inhibitors (pembrolizumab, nivolumab) | Modest sarcoma response (SARC028 etc.); better in UPS/DDLPS; CIC too rare for dedicated trials | Established (multi) / Clinical-Trial (sarcoma) / no direct CIC-DUX4 data |
| 4b | Epigenetic priming bridge (V3 → V4) | EZH2i/HDACi restore MHC-I; most active area in sarcoma immuno-trials. Dietary analogues (sulforaphane, butyrate) mechanistically aligned but much weaker exposure | Clinical-Trial |
| 4c | NK cell activation | **NK targets MHC-I-LOW cells — the same evasion CIC uses against T-cells, paradoxically increases NK visibility.** Clinical IL-15 agonists, NK engagers. Diet: correct vit D / zinc deficiency; microbiome diversity | Mechanistic / Clinical-Trial |
| 4d | CAR-T | Solid-tumor penetration unsolved; no CIC-DUX4-specific CAR-T published | Theoretical |
| 4e | Neoantigen vaccine | Junction sequence **varies across patients** (see file 02) — pan-CIC-DUX4 vaccine needs multiple variants | Theoretical / Preclinical |

### Dietary Support

| Goal | Compounds | Sources | Tier |
|---|---|---|---|
| NK activity | Vit D3 (correct deficiency), Zinc (correct deficiency) | Sunlight, fatty fish; oysters, pumpkin seeds | Mechanistic; replete-supplementation thin |
| Gut microbiome → systemic immune | Diverse fiber, fermented foods | Vegetables, legumes, whole grains; yogurt, kefir, sauerkraut, kimchi | Dietary-Observational (Akkermansia/Bifidobacterium ↔ CPI response in **melanoma**, not CIC-DUX4) |
| Anti-inflammatory TME | Omega-3, curcumin, polyphenols | Fatty fish, turmeric, berries, green tea | Mechanistic + Dietary-Observational |
| Possible MHC-I upregulation | Sulforaphane, butyrate | Broccoli sprouts, high-fiber diet | Preclinical |

### Canonical CPI-microbiome citations

Routy 2018 · Gopalakrishnan 2018 · Davar 2021 (FMT in melanoma).

### What V4 Cannot Do via Diet Alone

Substitute for checkpoint inhibitors · generate tumor-specific immune response (needs V3 priming or active immunization) · overcome deeply immunosuppressed TME.

---

## Cross-Vector Compound Table (default load — for orchestrator and any lead)

| Compound | V1 | V2 | V3 | V4 | Strongest claim |
|---|---|---|---|---|---|
| Sulforaphane | ✓ | — | ✓ | ✓ | Preclinical-Cell HDAC modulation |
| Quercetin | ✓ | ✓ | — | — | Preclinical-Cell, bioavailability-limited |
| EGCG | ✓ | ✓ | ✓ | — | Preclinical-Cell, bioavailability-limited |
| Omega-3 EPA/DHA | ✓ | ✓ | — | ✓ | Dietary-Observational + Mechanistic |
| Curcumin | ✓ | ✓ | — | ✓ | Preclinical-Cell, bioavailability-limited |
| Butyrate (fermented fiber) | — | — | ✓ | ✓ | Preclinical colonic; systemic exposure questionable |
| Vitamin D3 | — | — | ✓ | ✓ | Mechanistic + Dietary-Observational; correct deficiency first |
| Selenium | ✓ | ✓ | — | — | Narrow safety window |
| Zinc | ✓ | ✓ | — | ✓ | Correct deficiency; excess displaces copper |
| Fisetin | ✓ | — | — | — | Preclinical-Cell |
| β-carotene / Vit A | — | — | ✓ | — | Dietary-Observational; **harmful in smokers when supplemented** |

## Standard-of-Care Note (always include downstream)

CIC-rearranged sarcoma SOC is typically Ewing-like multi-agent chemo: VDC/IE — vincristine, doxorubicin, cyclophosphamide, alternating with ifosfamide and etoposide — plus surgery and radiation where applicable. Response rates lower than Ewing.

For chemo-interaction checking, invoke `/sarcoma-chemo-interactions`.
