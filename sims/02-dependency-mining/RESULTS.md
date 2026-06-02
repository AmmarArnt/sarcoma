# Sim 2 — DepMap CRISPR Dependency Mining — RESULTS

**One-line:** Tested the forward-simulation's named CIC-DUX4 targets against real genome-wide CRISPR data; the result both **corroborates** (IGF1R, CDK4) and **corrects** (EZH2 is *not* a viability dependency; WEE1 is essential-everywhere not CIC-selective; CDK4 ≠ CDK6) the catalog — exactly the kind of grounding the simulation needed.

**Confidence: medium-high** for the proxy analysis (real data, validated scale, n=27 Ewing lines); **the CIC-DUX4-specific CRISPR question is unanswerable** because the registered CIC-DUX4 lines have no CRISPR screens (see below). Not a treatment claim.

## Data (real; MANIFEST.md has URLs + sha256)
- **DepMap 24Q4 Public** (figshare 27993248 v1, DOI 10.25452/figshare.plus.27993248.v1): `Model.csv` (2,105 models) + `CRISPRGeneEffect.csv` (1,178 lines, Chronos gene effect).
- Chronos scale: 0 = no dependency; ≈ −1 = median common-essential; more negative = stronger. Anchored here by controls: **EEF2 −2.42, RPL3 −2.37** (pan-essential), **OR2T4 ≈ 0** (neutral). Scale verified.

## Finding 0 — Is any CIC-DUX4 line in DepMap? (corrects our prior guess)
**Yes — 3 CIC-DUX4 models are registered**, but **none have CRISPR data**:
| ModelID | Name | OncotreeSubtype | CRISPR data? |
|---|---|---|---|
| ACH-000772 | **TE441T** (TE 441.T) | CIC-DUX4 Sarcoma | no |
| ACH-002795 | NCC-CDS1-X1-C1 | CIC-DUX4 Sarcoma | no |
| ACH-002796 | NCC-CDS1-X3-C1 | CIC-DUX4 Sarcoma | no |

So the forward-sim's "DepMap coverage may be zero" was *imprecise*: the **lines exist in the registry** (TE441T is a well-known CIC-DUX4 line; the NCC-CDS1 lines are the patient-derived ones), but they have **not been CRISPR-screened**. Genome-wide dependency inference therefore still requires the **Ewing sarcoma proxy** (EWSR1-FLI1; 27 lines with CRISPR data: A-673, SK-ES-1, RD-ES, TC-71, TC-32, SK-N-MC, MHH-ES-1, EW8, CHLA-9/10/32/99/218, CADO-ES1, EWS502, …). **Ewing is a proxy, not CIC-DUX4** — transfer is mechanistically plausible (shared fusion-driven ETS/super-enhancer biology) but unproven.

## Finding 1 — Target dependency in Ewing proxy (n=27)
| Gene | Ewing mean | Ewing-selectivity (Ewing − all) | % lines dependent (<−0.5) | Read |
|---|---|---|---|---|
| **WEE1** | **−2.58** | −0.13 | 100% | Profound dependency — but **broadly essential** (all-lines −2.46), not CIC/Ewing-selective |
| **MYC** | −2.10 | −0.35 | 100% | Strong, modestly Ewing-enriched |
| **CDK4** | **−1.53** | **−0.77** | 89% | Strong **and the most Ewing-selective** target |
| **CCND1** | −1.47 | −0.49 | 89% | Strong + selective (note: **CCND1**, not CCND2) |
| **BRD4** | −0.96 | +0.01 | 100% | Universal dependency, **not** selective |
| **IGF1R** | −0.73 | −0.42 | 70% | Moderate, **Ewing-enriched** |
| INSR | −0.20 | −0.07 | 11% | Weak |
| CDK6 | −0.05 | +0.54 | 0% | **Not a dependency** (Ewing uses CDK4, not CDK6) |
| CCND2 | −0.03 | +0.11 | 0% | Not a dependency by CRISPR |
| ETV4 | −0.03 | +0.02 | 0% | Not a single-gene dependency (redundancy) |
| IGF1 | −0.03 | −0.02 | 0% | Not a dependency |
| **EZH2** | **+0.01** | +0.10 | 0% | **NOT a viability dependency** |
| ETV1 | +0.08 | +0.01 | 0% | Not a dependency |
| ETV5 | +0.14 | +0.01 | 0% | Not a dependency |

Full table: `dependency_table.csv`. Empty per-line CIC-DUX4 table: `cic_dux4_line_dependencies.csv` (confirms n=0).

## Interpretation — corroborations and corrections
**Corroborates the forward simulation:**
- **EZH2 is not a survival dependency (+0.01)** — direct, orthogonal support for the forensics claim that PRC2 *survival* dependency in CIC/Ewing is **assumed, not real**. → Strongly favors **repositioning EZH2i (tazemetostat) as an MHC-I priming agent, not a cytotoxic.** This is the single most decision-relevant result in this sim.
- **IGF1R is a real, fusion-sarcoma-enriched dependency (−0.73, selectivity −0.42)** — convergent with Sim 1 (two IGF1R inhibitors as top signature-reversers) and the Kitra-SRS autocrine-IGF1R finding. Three independent lines of evidence now point at IGF1R.
- **CDK4 axis is real and selective** — CDK4 (−1.53) + CCND1 (−1.47) are strong, Ewing-selective; supports the cell-cycle execution layer (V1/V3).

**Corrects / refines the forward simulation:**
- **CDK4 ≠ CDK6.** CDK6 is *not* a dependency (−0.05) in Ewing; the dependency is **CDK4-specific**. A CDK4/6 inhibitor's relevant target here is CDK4. Refines "CDK4/6i."
- **WEE1 is a strong dependency but essential everywhere** (selectivity −0.13). CRISPR essentiality ≠ therapeutic selectivity: the CIC-DUX4 WEE1 rationale (JCI Insight 2022, PMC8986087) rests on a *therapeutic window / replication-stress* argument in patient-derived lines, **not** on CIC-selective CRISPR essentiality. Honest framing: WEE1 inhibition is broadly cytotoxic; the case for it here is the ifosfamide-synergy/replication-stress angle, not selectivity.
- **BRD4 is a universal dependency, not selective** (selectivity +0.01) — exactly consistent with the BETi "narrow therapeutic window / hits everything" counterfactual. Explains modest monotherapy results.
- **ETV1/4/5 are not single-gene CRISPR dependencies** — the ETS output is distributed/redundant; don't expect single-ETS targeting to work.

## Limitations
- Ewing (EWSR1-FLI1) is a **proxy** for CIC-DUX4 (CIC-DUX4); shared biology is plausible, not proven.
- The 3 actual CIC-DUX4 DepMap lines lack CRISPR data — the CIC-specific dependency question stays open (TE441T may have other omics layers not analyzed here).
- CRISPR loss-of-viability ≠ druggability or therapeutic window (esp. WEE1, BRD4).
- Single data modality (Chronos CRISPR); no drug-sensitivity (PRISM) cross-check in this run.

## Grounding (OpenMed NER, team `v3-synthetic-lethality`: oncology+genome+protein)
`grounding.tsv`: all 14 target genes recognized as GENE/PROTEIN at 0.91–0.96 (ETV1/ETV4 lower at 0.57/0.67 in one model but confirmed by a second model at 0.94/0.93); **"CIC-DUX4 sarcoma" (0.91)** and **"Ewing sarcoma" (0.95)** recognized as Cancer entities. No unrecognized target entities.

## Reproduce
`.venv/bin/python sims/02-dependency-mining/run_dependency_mining.py`
Outputs: `dependency_table.csv`, `ewing_lines.csv`, `cic_dux4_line_dependencies.csv`, `entities.txt`, `grounding.tsv`, `MANIFEST.md`.
