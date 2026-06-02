# Sim 1 — CIC-DUX4 Signature-Reversal Drug Repurposing — RESULTS

**One-line:** Built the CIC-DUX4 transcriptional signature from a real fusion-ON vs fusion-OFF contrast and asked LINCS which perturbagens reverse it; the top reversers converge on the **IGF1R → PI3K/AKT/mTOR** axis, **CDK4/6**, and **MEK** — independently corroborating the forward-simulation's named targets from an orthogonal (transcriptomic) direction.

**Confidence: medium.** Real data, coherent and target-consistent result; limited by microarray platform, small n (2 vs 4), L1000 landmark-gene coverage, and cell-context mismatch (see Limitations). Not a treatment claim.

## Data (all real; see MANIFEST.md for URLs + sha256)
- **GSE60740** series matrix (GPL17811, Brainarray Entrez CDF, gcrma log2; 18,960 probes × 31 samples). Series title: *"Expression profiles of Ewing family of tumors authenticate distinct molecular entities."*
- The CIC-DUX4 on/off contrast = patient-derived **IB120** cells:
  - **ON** (CIC-DUX4 high) = empty vector: GSM1486562, GSM1486563
  - **OFF** (CIC-DUX4 knockdown) = CIC-DUX4 shRNA_1/_2: GSM1486558–561
- Entrez→symbol: NCBI `Homo_sapiens.gene_info.gz`.
- Reversal engine: **L1000CDS2** (`aggravate=False`, geneSet). Result shareId `6a195149d52166005c9cebc2` → https://maayanlab.cloud/L1000CDS2/#/result/6a195149d52166005c9cebc2

## Method
`log2FC = mean(ON) − mean(OFF)` per probe (data already gcrma-log2). Top 150 fusion-activated (ON>OFF) = `upGenes`, top 150 fusion-repressed = `dnGenes`. L1000CDS2 with `aggravate=False` returns perturbagens that **reverse** that signature — i.e. mimic CIC-DUX4 knockdown. Simple-fold ranking is honestly weak statistics (n=2 vs 4, no replicate-level modeling); used as a hypothesis generator, not a calibrated DE analysis.

## Signature sanity check (internal validation)
Top fusion-activated genes include **POLE** (matches the independently verified npj Precis Oncol 2025 finding that CIC::DUX4 sarcomas upregulate POLE), **ETV4** (the canonical CIC-de-repression ETS target), **LINC00473, ANGPT2, IGFBP3, CCNE2, MCM10, CDC6, DTL, KIF20A** (proliferation/replication program). The signature reflects real CIC-DUX4 biology, not noise.

## Top reversers (real L1000CDS2 output; score = overlap, higher = stronger reversal)
| Score | Perturbagen | Mechanistic class | LINCS cell |
|---|---|---|---|
| 0.351 | quinacrine HCl | (p53/NF-κB modulator) | A375 |
| 0.351 | MK-2206 | **AKT inhibitor** | HT29 |
| 0.346 | mitoxantrone | TopoII / anthracycline-like | A375 |
| 0.333 | BMS-536924 | **IGF1R/IR inhibitor** | MCF7 |
| 0.333 | NVP-BEZ235 (×3) | **PI3K/mTOR inhibitor** | A549 |
| 0.329 | palbociclib (×2) | **CDK4/6 inhibitor** | HME1 |
| 0.325 | dovitinib | **multi-RTK (incl. FGFR/IGF axis) inhibitor** | A375 |
| 0.320 | BMS-754807 | **IGF1R/IR inhibitor** | A375 |
| 0.320 | torin-2 | **mTOR inhibitor** | A549 |
| 0.316 | idarubicin (4-demethoxydaunorubicin) | TopoII / anthracycline | MCF7 |
| — | trametinib | **MEK inhibitor** | (named hit) |
| — | PHA-793887 | **CDK inhibitor** | (named hit) |
| — | Nutlin-3 | MDM2–p53 | (named hit) |

Full list: `l1000_reversers.csv`. Class tally among named hits: PI3K/AKT/mTOR (5), TopoII/anthracycline (4), CDK (4), IGF1R (2 distinct drugs), MEK (1).

## Interpretation — what this independently corroborates
1. **IGF1R → PI3K/AKT/mTOR is the dominant reversible axis.** Two structurally distinct IGF1R inhibitors (BMS-754807, BMS-536924) plus the entire downstream arm (MK-2206/AKT, NVP-BEZ235/torin-2/wortmannin/mTOR) reverse the signature. This is an **orthogonal, transcriptomic** corroboration of the Kitra-SRS autocrine-IGF1R finding (Sci Rep 2019, PMID 31676869) and the RAS/ERK→CIC framing in `docs/02`. Different data type, same target.
2. **CDK4/6 (palbociclib) reverses the signature** — consistent with the CCND2/CDK4 cell-cycle execution layer (V1/V3).
3. **MEK (trametinib)** appears — consistent with the upstream RAS/ERK→CIC de-repression node.
4. **Anthracyclines/TopoII (mitoxantrone, idarubicin)** scoring as reversers is consistent with the tumor's chemo-sensitivity to the doxorubicin/etoposide backbone the patient received.

## Honest negatives (not papered over)
- **No BET/BRD4, no EZH2, no HDAC, no WEE1** among the top reversers. This does NOT contradict those hypotheses: L1000CDS2 finds *transcriptional-signature* reversers, whereas WEE1 is a kinase-*dependency* (not expected to reverse a steady-state expression signature) and BRD4/EZH2 effects may be under-captured by the L1000 landmark-gene set or this particular cell-line panel. Absence here = "this assay didn't surface it," not "it's wrong."
- The IGF1R signal must carry the **Ewing IGF1R clinical scar**: striking-but-non-durable responses, no biomarker — so the redesign is a biomarker-selected subset, not "give everyone an IGF1R inhibitor."

## Limitations
- Microarray (not RNA-seq); 1 probe/Entrez via Brainarray CDF.
- Small n (2 ON vs 4 OFF), single cell model (IB120); simple-fold ranking, no multiple-testing model.
- L1000CDS2 perturbations were profiled in non-sarcoma LINCS cell lines (A375, MCF7, A549, …) — context mismatch; signal is hypothesis-level.
- Reversing a transcriptional signature ≠ killing the cell; it nominates mechanisms, not therapies.

## Grounding (OpenMed NER, team `v1-lead`: chemical+pharma+oncology models)
`grounding.tsv`: 115 entity spans — 56 Gene_or_gene_product, 41 CHEM, 13 Simple_chemical, 3 Organism. High-confidence recognition of drugs (palbociclib 0.961, dovitinib 0.962, mitoxantrone 0.966, torin-2 0.952) and signature genes (ETV4, POLE, SERPINE1, IGFBP7, IGFBP3). Unrecognized spans were limited to synthetic catalog codes (e.g., BJM-ctd2-9, DG-041) — expected, as these are not in biomedical NER vocabularies.

## Reproduce
`.venv/bin/python sims/01-signature-reversal/run_signature_reversal.py`
Outputs: `cic_dux4_signature.csv`, `l1000_reversers.csv`, `result_meta.json`, `entities.txt`, `grounding.tsv`, `MANIFEST.md`.
