---
name: sarcoma-output-schema
description: Returns the output-file schema for a specific agent role in the CIC-rearranged sarcoma simulation. Invoke with one of the role arguments (v1-lead, v2-lead, v3-lead, v4-lead, food-specialist, supplement-specialist, bioavailability-specialist, antioxidant-specialist, dna-repair-specialist, anti-inflammatory-specialist, epigenetic-therapy-specialist, differentiation-therapy-specialist, protac-aso-specialist, synthetic-lethality-specialist, checkpoint-tcell-specialist, nk-cell-specialist, microbiome-immune-specialist, neoantigen-vaccine-specialist, mrna-vaccine-lead, mrna-immune-effects, mrna-oncogenic-risk, metastatic-specialist, orchestrator). Source: docs/06-agent-architecture.md.
---

# Role-Specific Output Schemas

Pass your role as the argument. Each role gets the exact output structure expected by its parent (Vector Lead or Orchestrator).

If you cannot determine your role, write back to your invoker and ask. **Do not guess a schema.**

---

## orchestrator

Output file: `simulation-output/protocol-v1.md`

```markdown
# CIC-Rearranged Sarcoma — Multi-Vector Hypothesis Catalog (v1)

## Framing
[One paragraph: this is a research simulation output, not a treatment plan.
 Audience and intended use, per README. Include a note that ~5% of clinically
 and histologically similar cases may not have genomic fusion confirmation,
 and flag where findings in this catalog depend on fusion presence vs. apply
 more broadly.]

## Top-Level Findings
[5–10 bullets. The most defensible hypotheses across all four vectors.
 Each bullet includes evidence tier in brackets.]

## Naturally Achievable Track
### Diet (mechanistically grounded, food-level)
| Compound | Vector(s) | Mechanism (1 sentence) | Evidence tier | CIC-DUX4 specific? | Food sources | SOC contraindications |
|---|---|---|---|---|---|---|

### Supplements (only if dietary intake is insufficient AND safety profile is established)
[Same columns, plus published-dose-range column with citations.]

### Lifestyle (sleep, exercise, sun for vitamin D, fiber for microbiome)
[Free-form, brief.]

## Clinical / Experimental Track (For Oncologist Discussion Only)
| Intervention | Vector(s) | Mechanism | Evidence tier | Status FDA | Status EMA | Trial IDs | Notes |
|---|---|---|---|---|---|---|---|

For every Established-tier intervention, cite both FDA and EMA status where they differ. Where only one authority has acted, say so explicitly.

## mRNA COVID-19 Vaccine — Research Findings
[Summary of what the mRNA Vaccine Research Team found. If relevant findings
 for immune or genomic context: describe and link to the affected vector(s).
 If no relevant findings: state that explicitly rather than omitting.]

## Metastatic Disease Considerations
[Output from the Metastatic Disease Specialist sub-agent. For each major
 recommendation in the catalog, note whether it applies equally to metastatic
 disease or whether metastatic biology creates a different picture. Identify
 any vectors or interventions where metastatic-specific evidence exists or is
 notably absent.]

## Forward Hypotheses (Not Yet in the Literature)
[The most compelling mechanistically-defensible ideas curated from each
 vector's Forward Hypotheses section and the Metastatic Specialist output.
 Rank by biological plausibility and research feasibility. Each entry:
 hypothesis statement, supporting mechanism, what experiment would test it,
 and (if known) why it has not yet been tested.]

## Cross-Vector Synergies
[Compounds or intervention pairs active across multiple vectors. Rank by total
 evidence weight, not number of vectors touched.]

## Conflicts and Open Questions
[Where vectors disagree. Where the literature is silent. Where mechanism
 could not be established. Be specific.]

## Standard-of-Care Interaction Map
[Each entry flagged in the dietary track that has a documented interaction
 with sarcoma chemotherapy regimens. Cite the interaction source.]

## What This Catalog Cannot Tell You
[Limits. Scope exclusions. What would require a clinician's input.]

## Bibliography
[Every citation used. Every entry must be verifiable.]
```

---

## v1-lead, v2-lead, v3-lead, v4-lead

Output file: `simulation-output/v{N}-{vector-name}/v{N}-summary.md`
(`v1-rate-limiting`, `v2-compiler-protection`, `v3-hot-patching`, `v4-immune-watchdog`)

```markdown
# Vector {N} — {Vector Name} Summary

Summary: [1-sentence what this covers]
Confidence: [high/medium/low] — [1-sentence why]

## Ranked Candidate List
| Rank | Compound | Layer | Mechanism | Tier | CIC-DUX4 direct? | Cross-vector | Source/citation |
|---|---|---|---|---|---|---|---|

## [Vector-specific sub-sections from sub-agents — condensed, not concatenated]
   V1: Food Sources · Supplementation Notes · Bioavailability Notes
   V2: Antioxidant Protocol · DNA Repair Support · Anti-Inflammatory Protocol · "Harms / Null Trials"
   V3: Dietary Track · Clinical Track (clearly separated) · MHC-I Upregulation (top section)
   V4: Dietary Track · Clinical Track (clearly separated)

## Cross-Vector Flags
[Compounds the other vector leads should also see]

## Forward Hypotheses
[At least **two** mechanistically defensible ideas not yet in the literature.
 Each entry labeled `[Forward Hypothesis]` with: hypothesis statement,
 mechanistic basis, what study design would test it. The orchestrator carries
 the strongest of these into the final catalog. An output without this
 section is incomplete.]

## Atypical-Case Notes
[Where any candidate in the Ranked Candidate List depends critically on the
 CIC-DUX4 fusion being present (ASO/junction-specific approaches), flag the
 ~5% of clinically and histologically similar cases without a confirmed
 fusion to whom that candidate will not apply. Where a candidate is
 fusion-agnostic, note that it may apply to atypical cases as well.]

## What I Could Not Establish
[Gaps]
```

V3-lead additional requirement: `MHC-I Upregulation Candidates` section at the **top** for V4 lead and orchestrator.

V2-lead additional requirement: `Harms / Null Trials` section addressing ATBC, CARET, SELECT, NAC/Sayin 2014 head-on. The V2 lead must also incorporate the mRNA Vaccine Research Team's findings on inflammatory context before finalizing.

V4-lead additional requirement: must incorporate (a) the V3 MHC-I Upregulation Candidates section before finalizing, and (b) the mRNA Vaccine Research Team's findings on immune modulation before finalizing.

---

## food-specialist (V1)

Output: `simulation-output/v1-rate-limiting/food-sources.md`

```markdown
| Compound | Best food source | Realistic serving | Preparation note | Bioactive form |
|---|---|---|---|---|
```

Hard constraints: no mg/day prescriptions; "Brazil nuts: 1–2 per day" OK (RDA-relevant), "EGCG 500mg/day" NOT OK; flag foods where intake recommendation would exceed RDA upper limits.

---

## supplement-specialist (V1)

Output: `simulation-output/v1-rate-limiting/supplement-protocol.md`

Required fields per compound: standard supplement forms · dose ranges **from published clinical trials** (cite NCT or PubMed) · safety / upper limits · CYP3A4 / CYP2C9 / P-gp interactions · documented interactions with doxorubicin, vincristine, etoposide, ifosfamide, cyclophosphamide.

Every supplement entry ends: "consult oncologist before starting — possible interactions with [specific drugs]."

If no human trial data exists for a compound: say so and stop. Do not extrapolate from cell-line concentrations.

---

## bioavailability-specialist (V1)

Output: `simulation-output/v1-rate-limiting/bioavailability.md`

Fields per compound: fat- vs water-soluble + meal-timing · first-pass magnitude · known PK-enhancing combinations (cite the actual PK study + real effect size) · tissue distribution to mesenchymal tumor.

**Curcumin + piperine entry must reproduce the Shoba 1998 caveat** (n=10, single dose, control below LOD; "2000% boost" cited with caveat, not as universal multiplier).

---

## antioxidant-specialist (V2)

Output: `simulation-output/v2-compiler-protection/antioxidant-protocol.md`

Must address: ROS sources in TME · endogenous antioxidant system (SOD, catalase, GPx) · dietary polyphenols vs isolated high-dose · ATBC / CARET / SELECT trials and proposed mechanisms for harm · NAC/metastasis (Sayin 2014 and follow-up) · antioxidant+chemo concerns.

**Must include a `DO NOT RECOMMEND` section** enumerating high-dose supplement interventions the literature contraindicates.

---

## dna-repair-specialist (V2)

Output: `simulation-output/v2-compiler-protection/dna-repair-support.md`

Cofactors: zinc (Ku70/Ku80, p53 zinc finger) · magnesium (DNA pol cofactor) · folate / B12 / B6 (nucleotide pools; folate-excess literature) · selenium (narrow window) · NAD+ precursors (thin clinical evidence — be honest).

For every cofactor, distinguish: correcting documented deficiency (clearer) · supplementation in repleted individuals (thin) · high-dose supplementation (often no benefit, sometimes harm).

---

## anti-inflammatory-specialist (V2)

Output: `simulation-output/v2-compiler-protection/anti-inflammatory-protocol.md`

Cover: IL-6 / TNF-α / IL-1β axes · M1/M2 polarization and what diet can/cannot shift · omega-3 → SPMs (resolvins, protectins, maresins) · polyphenols with NF-κB activity at achievable concentrations · Mediterranean pattern vs isolated compounds.

Every "anti-inflammatory diet reduces cancer risk" claim must distinguish epidemiology from mechanism and acknowledge that effect sizes on existing-tumor outcomes are small.

---

## epigenetic-therapy-specialist (V3)

Output: `simulation-output/v3-hot-patching/epigenetic-reprogramming.md`

Cover: HDACi, EZH2i, DNMTi, BETi clinical agents (FDA status + NCT) · dietary modulators with mechanism (even if weak) · mechanisms via H3K27me3, H3K27ac, DNA methylation · documented MHC-I upregulation flagged for V4.

**MHC-I upregulation section is mandatory and goes at the top of the output.**

---

## differentiation-therapy-specialist (V3)

Output: `simulation-output/v3-hot-patching/differentiation-therapy.md`

Cover: retinoic acid pathway (ATRA in APL as existence proof; retinoid pathways in fusion sarcomas mostly thin) · vitamin A from animal sources + β-carotene from plants (with explicit ATBC/CARET caveat) · vitamin D3 / VDR-target genes (deficiency vs supplement) · butyrate via dietary fiber (high colonic, low systemic) · combinations of differentiation + epigenetic strategies.

---

## protac-aso-specialist (V3)

Output: `simulation-output/v3-hot-patching/clinical-experimental.md`

Cover: published or in-development ASOs targeting CIC-DUX4 junction (if none, say so) · PROTAC technology for BET / EZH2 / fusion proteins · clinical trial landscape for EZH2i (tazemetostat and successors), BETi (OTX015, BMS-986158, AZD5153), CDK4/6i in sarcoma · NCT IDs / phase / indication.

**Tag the entire output: `Clinical / Experimental — not naturally achievable; for awareness only.`**

---

## synthetic-lethality-specialist (V3)

Output: `simulation-output/v3-hot-patching/synthetic-lethality.md`

Cover: BRD4 addiction (BETi sensitivity in fusion sarcomas) · PRC2/EZH2 dependency (BAF-disrupted) · CDK4 / CCND1 dependency · documented synthetic-lethal CRISPR hits in CIC-DUX4 cell lines (search Cellosaurus / DepMap; if not, say so).

For each dependency: list clinical drug + dietary modulator (with honest exposure-mismatch caveat).

---

## checkpoint-tcell-specialist (V4)

Output: `simulation-output/v4-immune-watchdog/tcell-surveillance.md`

Cover: PD-1 / PD-L1 / CTLA-4 biology · clinical CPI trials in sarcoma (SARC028 etc.) · combination strategies (CPI + epigenetic priming) · dietary modulation of PD-L1 (flag honestly: mostly cell-line, patient evidence essentially zero) · V3 → V4 bridge (epigenetic priming, MHC-I restoration).

---

## nk-cell-specialist (V4)

Output: `simulation-output/v4-immune-watchdog/nk-cell-activation.md`

Cover: NK missing-self detection, KIR, NKG2D ligands · vitamin D3 + NK function (correct deficiency vs replete-supplementation) · zinc status and NK development · IL-15 / IL-15-superagonist pipeline · NK engager bispecifics in trials · adoptive NK transfer.

Key framing concept: NK cells target MHC-I-LOW cells, which is the same evasion CIC-DUX4 cells use against T-cells — a real, well-grounded basis for NK-directed approaches.

---

## microbiome-immune-specialist (V4)

Output: `simulation-output/v4-immune-watchdog/microbiome-immune.md`

Cover: SCFA (butyrate, propionate, acetate) from fiber fermentation · microbiome diversity ↔ CPI response (cite Routy 2018, Gopalakrishnan 2018, Davar 2021 FMT trial — these are canonical) · prebiotic fiber types (inulin, resistant starch, beta-glucan) · fermented foods (Sonnenburg lab) · probiotic use during cancer therapy (mixed/controversial; some trials showed reduced CPI response with broad probiotics).

Evidence base is overwhelmingly melanoma/NSCLC, not sarcoma. Say so.

---

## neoantigen-vaccine-specialist (V4)

Output: `simulation-output/v4-immune-watchdog/neoantigen-vaccine.md`

Cover: personalized neoantigen platforms (BNT122, mRNA-4157, NEO-PV-01) · whether any pipeline targets CIC-DUX4 specifically (verify; likely no) · CAR-T toward solid tumors; CIC-DUX4-targeted constructs (likely preclinical only) · per-patient vs pan-CIC-DUX4 vaccine design and junction sequence variability (see file 02).

**Tag the entire output: `Clinical / Experimental — not naturally achievable; for awareness only.`**

---

## mrna-vaccine-lead

Output: `simulation-output/mrna-vaccine-research/mrna-vaccine-summary.md`

```markdown
# mRNA Vaccine Research Team — Summary

Summary: [1-sentence what this covers; "no relevant effect found" is a valid and complete output]
Confidence: [high/medium/low] — [1-sentence why]

## Immune Modulation
[T-cell, NK, checkpoint pathway, cytokine milieu — what is documented vs. speculative vs. contradicted. Include LNP / TLR / mRNA platform immunological duration of effect.]

## Inflammatory Context
[Persistent low-grade inflammation, NF-κB modulation, cytokine profile changes — relevant to V2 microenvironment logic.]

## Genomic Stability
[Survey peer-reviewed literature. If no effect on genomic stability, say so clearly; non-peer-reviewed claims cited only as "exists but unconfirmed."]

## Oncogenesis Signal in Surveillance Data
[Pharmacovigilance / epidemiology signal linking BNT162b2 to sarcoma incidence or progression. State signal or absence of signal explicitly.]

## Relevance to mRNA Cancer Vaccines
[LNP immunogenicity, pre-existing mRNA platform immunity — implications for future BNT122 / mRNA-4157-style CIC-DUX4 neoantigen vaccine design.]

## Relevance to V2 (Compiler Protection)
[Even if "no documented relevant effect" — state explicitly.]

## Relevance to V4 (Immune Watchdog)
[Even if "no documented relevant effect" — state explicitly.]

## Forward Hypotheses
[At least two mechanistically defensible ideas not yet in the literature. Label each `[Forward Hypothesis]`.]

## What I Could Not Establish
[Gaps, study-population limits, detection floors.]
```

Apply the same evidence tier vocabulary as all other agents. Non-peer-reviewed sources may be cited only to note their existence and the absence of peer-reviewed confirmation — not as evidence.

---

## mrna-immune-effects

Output: `simulation-output/mrna-vaccine-research/immune-effects.md`

Focus: peer-reviewed literature on persistent immune effects of BNT162b2. Apply the contract evidence tiers. Do not speculate beyond the literature. Required sections: One-line summary · Confidence · Per-claim tier and mechanism · Duration-of-effect evidence · Relevance flags for V4 · What I Could Not Establish · Forward Hypotheses (≥2).

---

## mrna-oncogenic-risk

Output: `simulation-output/mrna-vaccine-research/oncogenic-risk.md`

Focus: pharmacovigilance data and peer-reviewed oncogenesis literature. Specifically: is there a signal, and if not, how large is the studied population and what is the detection limit? Required sections: One-line summary · Confidence · Signal or absence-of-signal with population size and detection limit · Per-claim tier · Relevance flags for V2 · What I Could Not Establish · Forward Hypotheses (≥2).

---

## metastatic-specialist

Output: `simulation-output/metastatic-disease-considerations.md`

```markdown
# Metastatic Disease Considerations — CIC-Rearranged Sarcoma

## Summary
[1–2 sentences: overall assessment of whether the four vectors apply to
 metastatic disease, and where the key gaps are.]

## Per-Vector Applicability in Metastatic Disease
For each V1–V4 (2–5 sentences each): applies / applies with caveats / does
not clearly apply. Say why. Consider:
  - Immune evasion pressure (metastatic cells have already survived surveillance)
  - Microenvironment differences (bone, lung, CNS vs. soft tissue primary)
  - Treatment context (prior VDC/IE exposure changes dietary applicability —
    e.g., antioxidants after prior doxorubicin)
  - Fusion heterogeneity (clonal evolution may have altered the target for
    fusion-dependent approaches)

## mRNA Team Findings — Metastatic Relevance
[If the mRNA team found anything relevant to systemic immune or inflammatory
 context, note its specific implication for metastatic biology.]

## Metastatic-Specific Forward Hypotheses
[At least **two** mechanistically defensible ideas specific to metastatic
 setting that are not already covered in the primary-tumor vectors.]

## What I Could Not Establish
[Be specific about what is unknown about CIC-DUX4 metastatic biology.]
```

You are given the four Vector Lead summaries and the mRNA team output as input. **Do not repeat them** — for each major finding, ask whether metastatic biology changes the picture.

---

## Final Note

Before writing your output, invoke `/sarcoma-pre-output-check` and `/sarcoma-chemo-interactions` for any dietary/supplement entries. The rules in `/sarcoma-contract` apply to everything written.
