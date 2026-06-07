# Driver-Uncertainty Brief — Modeling the Unknown Driver in a Fusion-Unconfirmed CIC-like Sarcoma

> **Team:** Tumorigenesis / Cell-of-Origin Reverse-Engineering (supplementary). **Authored in the main
> thread** (the spawned specialist hit a session limit and returned nothing; per CLAUDE.md §3 the work was
> done directly — same grounding, same no-fabrication rule).
> **This is a research SIMULATION — hypothesis generation, NOT medical advice, NOT diagnosis.** It grounds
> the latent-variable priors and applicability matrix consumed by `sims/08-driver-uncertainty/`.

## Why this exists
The simulated patient (protocol-v1.md line ~24) is in the **~5% fusion-unconfirmed subgroup**: morphology/
clinic say CIC-rearranged sarcoma, but no CIC fusion was confirmed. The *true molecular driver is unknown*.
Rather than guess it, Sim 8 treats the driver as a **latent variable D**, marginalizes catalog
interventions over a literature-anchored prior p(D), reports what is **robust regardless of D**, and
computes the **value of resolving D** with specific tests.

## The driver hypothesis space

| ID | Hypothesis | Fusion present? | **DUX4 transactivation domain?** | CIC-class methylation? | Cryptic junction to target? |
|---|---|---|---|---|---|
| **D1** | Cryptic / false-negative **CIC-DUX4** (truly present, missed) | yes | **yes** | yes | yes (hidden) |
| **D2** | Rare non-DUX4 CIC partner (**NUTM1/FOXO4/LEUTX/NUTM2A**), off-panel | yes | **no** (rare DUX4-family variant e.g. ATXN1::DUX4 = yes) | yes | yes |
| **D3** | Non-fusion **CIC inactivation** (mutation/deletion, LOF) | no | no | usually yes | no |
| **D4** | **Phenocopy / misclassification** (BCOR-altered, EWSR1::non-ETS, undifferentiated) | (other) | no | **no** | (non-CIC) |
| **D5** | **Orphan** CIC-like, no identified driver (incl. epigenetic phenocopy) | no | no | CIC-like / unclassified | no |

**The load-bearing distinction:** the DUX4 C-terminal transactivation domain is present only under **D1**
(and a rare DUX4-family variant of D2). That domain is what creates the DUX4 totipotency death program and
the **MCL1 "apoptosis-fragility"** the build recipe flagged as the top forward hypothesis. So that
hypothesis is **driver-contingent**, not a given for this patient. Junction-specific therapy (ASO/vaccine)
needs both a real fusion (D1/D2) *and* its junction resolved.

## Literature-anchored prior p(D) — point estimates with ranges (to be SWEPT, not trusted as exact)

Conditioned on "histologically CIC-like, fusion-test-negative." These are reasoned estimates from the
evidence below; **several are `[estimate]` — the sim sweeps them, so honest ranges matter more than points.**

| ID | p(D) default | plausible range | basis |
|---|---|---|---|
| D1 cryptic CIC-DUX4 | 0.45 | 0.30–0.60 | CIC break-apart **FISH false-negative 14–46%** (one study 26%); NGS callers filter CIC::DUX4 on DUX4 repeats → a large share of "negatives" are cryptic positives. **Established** (assay limitation). |
| D2 rare partner | 0.12 | 0.05–0.22 | non-DUX4 partners ≈5% of *all* CIC-rearranged; **enriched** in the fusion-negative subset because standard panels omit them. **Clinical-genomic** `[estimate of enrichment]`. |
| D3 non-fusion CIC LOF | 0.10 | 0.03–0.20 | CIC point-mutation/deletion derepresses ETS without a fusion; poorly quantified in this morphology. **Mechanistic** `[VERIFY frequency]`. |
| D4 phenocopy / misclassified | 0.20 | 0.10–0.35 | methylation reclassifies ~13% of Ewing-like→BCOR and ~20%→CIC; a real, sizeable misclassification fraction. **Clinical-genomic.** |
| D5 orphan / epigenetic | 0.13 | 0.05–0.25 | residual; true unclassifiable CIC-like. `[estimate]`. |

Sum of defaults = 1.00. (Dirichlet sweep in the sim re-normalizes samples.)

## Diagnostic resolving power (the tests Sim 8 values)

1. **Nuclear DUX4 IHC** — cheap, fast. Highly sensitive/specific for CIC::DUX4 (Macedo et al., *Histopathology* 2025, 48 molecularly confirmed cases). **Resolves the DUX4-transactivation-domain question** → a positive strongly implicates D1 and *directly licenses the MCL1/DUX4-fragility and junction-DUX4 lines*. The single cheapest high-leverage test for *our* contingent hypothesis. **Established.**
2. **Genome-wide DNA-methylation array** — high sensitivity/specificity for the CIC sarcoma methylation class vs BCOR/Ewing; reclassifies morphologic mimics. **Collapses D4 (and helps triage D5).** **Established/Clinical-grade.**
3. **Long-read WGS + RNA-seq** (Nanopore/PacBio) — recovers cryptic CIC-DUX4 junctions and rare partners that short-read/FISH miss (the DUX4 D4Z4 repeat problem). **Separates D1/D2/D3 and unlocks junction-specific options.** Matches protocol-v1's V3-FH3 "highest immediate clinical leverage" claim. **Mechanistic/Clinical-emerging.**

## Intervention applicability matrix (the key sim input)

`1` = applies, `0.5` = partial/uncertain, `0` = does not apply.

| Intervention | gate | D1 | D2 | D3 | D4 | D5 |
|---|---|---|---|---|---|---|
| BRD4 / BETi | ETS/super-enhancer program | 1 | 1 | 1 | 0.5 | 1 |
| p300/CBP inhibition | CIC-activator p300 dependence | 1 | 0.5 | 0.5 | 0.5 | 0.5 |
| CDK4 / CCND1 (CDK4/6i) | cell-cycle execution | 1 | 1 | 1 | 1 | 1 |
| EZH2i → MHC-I priming | PRC2/MHC-I-low epigenetic state | 1 | 1 | 0.5 | 0.5 | 0.5 |
| immune / NK / checkpoint | host-side, driver-agnostic | 1 | 1 | 1 | 1 | 1 |
| **MCL1i / re-arm DUX4 death program** | **DUX4 transactivation domain** | 1 | 0 (0.5 if DUX4-family) | 0 | 0 | 0 |
| **junction-specific ASO / vaccine** | **fusion + resolved junction** | 1 | 1 | 0 | 0 | 0 |

(BCOR phenocopy D4 is itself super-enhancer/CCND-driven, so the generic throttle vectors keep partial-to-
full applicability even under misclassification — which is *why* they are robust.)

## What I could not establish (honest)
- **No clean frequency** for D3 (non-fusion CIC LOF) or D5 in this exact morphology — `[VERIFY]`/`[estimate]`.
- The **enrichment** of rare partners (D2) specifically within the fusion-*negative* subset is inferred,
  not directly measured.
- Whether *this* patient's prior testing already included methylation/DUX4 IHC is unknown — the model
  assumes the generic fusion-unconfirmed state; if those tests were done, condition the prior on them.
- Applicability scores are mechanistic judgments, not per-driver trial data.

## Falsifiers
- If a DNA-methylation array returns **non-CIC class**, D4 dominates and most CIC-directed entries drop.
- If **DUX4 IHC is negative**, the MCL1/DUX4-fragility hypothesis is effectively off the table for this patient.
- If long-read WGS finds a **canonical CIC-DUX4 junction**, the latent-variable problem collapses to D1 and
  Sim 7's full recipe applies directly.

### Verified source anchors
- CIC FISH false-negative 14–46% / pitfalls: *Pathol Res Pract* 2022 (CIC FISH interpretation pitfalls);
  RNA-seq recovers FISH-negative CIC-DUX4. **[VERIFY exact PMIDs]**
- Partner frequency (DUX4 ≈95%; FOXO4/LEUTX/NUTM1/NUTM2A ≈5%; NUTM1 2nd): Frontiers *Cell Dev Biol* 2024
  review (PMC11176417); *Mod Pathol* 2023 "Expanding the Molecular Diversity of CIC-Rearranged Sarcomas."
- DUX4 IHC sensitivity/specificity: Macedo et al., *Histopathology* 2025 (DOI 10.1111/his.15341).
- Methylation reclassification (47% Ewing / 20% CIC / 13% BCOR among Ewing-like): array-based methylation
  profiling studies (*Mod Pathol* 2022; PMC7084764; PMC7819999). **[VERIFY exact split per source]**
- ATXN1::DUX4 expands the CIC-rearranged concept (DUX4-family, non-CIC): PMID 35715887.

*Not medical advice. Research simulation / hypothesis generation only.*
