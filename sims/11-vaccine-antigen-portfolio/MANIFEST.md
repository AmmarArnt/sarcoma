# Manifest — Sim 11, Vaccine Antigen-Source Portfolio (INT-concept transplant test)

**Type:** Monte-Carlo decision model (antigen-supply funnel + portfolio scoring + architecture bake-off +
EVSI + ablation/flip test). **No external data download.**
**Interpreter:** repo `.venv` (`numpy` only — this session's container had no pre-existing venv, so a fresh
one was created and `numpy 2.4.6` installed from PyPI; the sim uses no other third-party package).
**Seed:** `20260819`, 40,000 draws. Deterministic.

## Provenance of the case inputs (not literature — patient record / prior sims)

| Input | Value | Source |
|---|---|---|
| Driver posterior D1–D5 | 0.264 / 0.100 / 0.095 / 0.386 / 0.156 | **Carried verbatim from `CASE-BASELINE.md` §3** (= Sim 10 output, ADR-0021/0022) |
| Post-chemo MRD window is currently open and perishable | modelled as a context multiplier | `simulation-output/chemosensitivity-ddr-cellstate-layer.md` §5 (ADR-0021) |
| NK reconstitutes before T post-chemo; NK covers MHC-I-loss escape | motivates the antigen-independent arm | Sims 4/5 + ADR-0021 §5 (in-repo results) |
| Round-cell sarcoma lesions are reachable/well-perfused; visceral (lung), not injectable skin nodules | bounds the in-situ arm | `CASE-BASELINE.md` §4 |
| Low OV susceptibility in the nearest (Ewing/round-cell) data | bounds in-situ take rate to 0.05–0.30 × access 0.35–0.70 | `simulation-output/oncolytic-virotherapy-danger-signal-layer.md` (ADR-0019) |

## Parameter provenance (literature-anchored judgements — **all `[VERIFY]`**)

| Parameter | Value | Anchor / status |
|---|---|---|
| Reference platform encodes **up to 34** patient-specific neoantigens per construct | `SLOTS = 34` | mRNA-4157 / V940 (intismeran autogene) program description — **`[VERIFY]`**, also recorded in `simulation-output/v4-immune-watchdog/v3/neoantigen-vaccine.md` |
| **CIC-rearranged sarcoma has low mutational burden** | `TMB_MED` 0.80 for D1/D2 (0.90 D3) | Italiano et al. / targeted-NGS series, **PMID 27664537** ("low mutational burden and recurrent chromosome 1p loss") — **`[VERIFY]`**, cited at this level in the existing neoantigen-specialist output |
| **Ewing/round-cell family is among the lowest-TMB malignancies** (~0.15 mut/Mb) | `TMB_MED` 0.30 for D4 | pan-cancer mutation-frequency and Ewing genome-landscape literature (Lawrence *Nature* 2013; Tirode / Brohl / Crompton *Cancer Discov* 2014) — **`[VERIFY]`**, not retrievable this session |
| Melanoma TMB ~10–30 mut/Mb (calibration arm) | median 13, GSD 3 | same pan-cancer literature — **`[VERIFY]`** |
| Exome coding footprint | 30 Mb | standard clinical WES figure |
| Clonal / expressed / binder / immunogenic attrition | 0.60 / 0.45 / 0.30 / 0.08 (each swept) | neoantigen-pipeline attrition is well documented in aggregate; the immunogenicity step (predicted binder → actually T-cell-recognised) is the notoriously lossy one — **`[VERIFY]`**, values are transparent judgements, all swept in Module E3 |
| Long-read WGS+RNA-seq junction sensitivity | 0.80 | judgement anchored on Sim 8's ranking of long-read as top-EVSI for driver resolution (in-repo) |
| CIC break-apart FISH false-negative 14–46%; short-read callers filter CIC::DUX4 on DUX4 repeats | motivates `P_JUNCTION_IDENTIFIED_TODAY = 0.0` | `CASE-BASELINE.md` §2 (already `[VERIFY]` there) |
| **DUX4 antagonises IFN-γ-induced MHC-I** → lower baseline presentation when DUX4 is expressed | `mhc1_base × (1 − 0.45·p_DUX4)` | DUX4 immune-evasion literature; the DUX4–STAT1/ISG antagonism arm already carried in `protocol-v4.md` — **`[VERIFY]`** |
| Round-cell sarcomas are characteristically MHC-I-low / immune-cold | `mhc1_base` mean 0.35 | sarcoma immunotherapy literature (SARC028 and successors) as summarised in the V4 outputs — **`[VERIFY]`** |
| Epigenetic priming (EZH2i / class-I HDACi / DNMTi) raises MHC-I | priming gain mean 0.45 | Sim 2 repositioned EZH2i as MHC-I priming on **real DepMap data** (in-repo); ADR-0021 adds the SLFN11-maintenance rationale |
| HERV / cancer-testis de-repression by DNMTi/HDACi ("viral mimicry") | class A6 | viral-mimicry literature — **`[VERIFY]`** |
| Cancer-testis antigens (NY-ESO-1/CTAG1B, PRAME, MAGE-A4) are expressed in some sarcoma subtypes and are established T-cell-therapy targets there | class A3 availability 0.35–0.45 | synovial-sarcoma / myxoid-liposarcoma CTA literature and the approved MAGE-A4 TCR-T precedent — **`[VERIFY]`**; **round-cell/CIC expression specifically is unknown** and is the model's largest unmeasured input |
| Ewing-associated lineage antigens (STEAP1, CHM1/LECT1, GPR64/ADGRG2, LIPI) | class A4 | Ewing immunotherapy target literature — **`[VERIFY]`** |
| On-target/off-tumour toxicity is a documented, sometimes fatal risk for shared/lineage-antigen T-cell therapy | `spec_risk` 0.12 (A4) / 0.15 (A6) | MAGE-A3 TCR cross-reactivity and related toxicity reports — **`[VERIFY]`**, values are judgements |
| HLA-LOH / B2M loss as an antigen-presentation escape route | mean 0.20 | immune-escape literature — **`[VERIFY]`** |
| Personalised-vaccine manufacturing turnaround ~6–9 weeks (why a wrong blind design commitment costs the window) | rebuild penalty in Module E2 | platform program descriptions, as already recorded in the neoantigen-specialist output — **`[VERIFY]`** |

## `[VERIFY]` status — read before quoting any citation above

**Direct literature and data egress was blocked in this session (2026-08-19).** `pubmed.ncbi.nlm.nih.gov`,
`ftp.ncbi.nlm.nih.gov`, `depmap.org`, `clinicaltrials.gov` and `huggingface.co` all returned **HTTP 403** at
the agent proxy (`CONNECT tunnel failed, response 403`; confirmed against
`$HTTPS_PROXY/__agentproxy/status`). No PMID, NCT, accession or regulatory status in this sim was verified
live. Every anchor above therefore carries **`[VERIFY]`** per **ADR-0020**, and nothing here may be promoted
into a `protocol-vN.md` until full-text verified.

**Nothing was fabricated to fill the gap:** no dataset was invented, no epitope prediction was simulated as
if it had been run, and the two real-data upgrades that egress would have enabled (DepMap/GEO expression of
the A3/A4 antigen classes in Ewing/CIC lines; GSE60740 antigen-presentation response to driver induction)
are named as *not done* in RESULTS.md rather than approximated.

## Entity grounding

`entities.txt` lists the named biomedical entities. **OpenMed NER grounding could not be executed** —
`scripts/openmed_ner.py` downloads models from HuggingFace on first use, and `huggingface.co` returned
HTTP 403 through the proxy this session. No `grounding.tsv` is present, and none was fabricated. Re-run
`python scripts/openmed_ner.py --team v4-lead --text-file sims/11-vaccine-antigen-portfolio/entities.txt
--format tsv > sims/11-vaccine-antigen-portfolio/grounding.tsv` when model egress is available.

## Outputs

| File | Contents |
|---|---|
| `supply_funnel.csv` | sarcoma vs melanoma antigen-supply funnel |
| `supply_by_driver.csv` | supply per driver hypothesis D1–D5 |
| `antigen_classes.csv` | the seven antigen classes with availability/yield/escape/specificity/readiness |
| `architecture_ranking.csv` | full-context bake-off incl. the no-vaccine baseline |
| `architecture_ranking_vaccine_arm_only.csv` | designs compared on the vaccine arm alone (NK forced off) |
| `lever_ablation.csv` | which lever is binding |
| `design_value_of_information.csv` | EVSI of five tests **for the design decision only** |
| `supply_sensitivity.csv` | TMB/binder/immunogenicity stress tests |
| `flip_test.csv` | what would have to be true for the vaccine arm to be load-bearing |
