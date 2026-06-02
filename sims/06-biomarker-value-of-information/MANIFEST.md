# Sim 6 — Data MANIFEST

This simulation downloads **no new data**. It is a decision-sensitivity (value-of-information) layer
computed entirely from a model already in this repository.

## Inputs (all already in-repo, previously grounded)

| Input | Source | Role here |
|---|---|---|
| `../04-immune-state-model/immune_state_model.py` | Sim 4 (this repo) | The validated Boolean immune-clearance model — imported unchanged (`evaluate`, `DEFAULT_PARAMS`, `NONCYTO`). Every edge cites a real mechanism (see Sim 4 SOURCES). |
| Baseline cell-state | Sim 1, GEO **GSE60740** (CIC-DUX4 on/off, IB120) | Anchors the disease-state parameters inherited via Sim 4 (NLRC5/MHC-I low, PD-L1 low, HLA-E low, CD112 up). |
| Mechanism citations | Goel *Nature* 2017 (PMID 28813415); Aging 2016 (PMID 26878797); Nat Commun 2019 (s41467-019-10335-5); PNAS 2016 (PMID 27162338) | Inherited from Sim 4; not re-derived here. |

No new accession, gene-effect value, drug, or dataset is introduced. No network access is required to
reproduce the VoI computation. OpenMed NER grounding **was run** on the project venv (team `v4-lead`,
matching Sim 4) — see `grounding.tsv` and RESULTS "Grounding"; the model download from HuggingFace is
the only step that touches the network.

## Outputs (written by `run_voi.py`)

| File | Contents |
|---|---|
| `voi_ranking.csv` | Per-biomarker total-effect decision/route/reachability flip frequencies (the ranking). |
| `oat_detail.csv` | One-at-a-time effect at the case baseline (regimen + route under assumed vs alternative value). |
| `voi_summary.json` | Case baseline regimen + full ranking + OAT, machine-readable. |
| `entities.txt` | Entity list (subset of Sim 4's grounded set; see RESULTS "Grounding"). |
| `grounding.tsv` | OpenMed NER output (team `v4-lead`); all 24 entities recognized, incl. FOXP3 + CD8-positive T cell. |

## Provenance / integrity

- Engine: deterministic Boolean evaluation; no randomness, no sampling — results are exact and
  reproducible bit-for-bit given the same Sim-4 model file.
- Access date: 2026-06-02.
- Dependency: `pandas` (only because the imported Sim-4 module imports it). The Sim-6 script itself
  uses stdlib only (`itertools`, `json`, `csv`, `os`, `sys`).
