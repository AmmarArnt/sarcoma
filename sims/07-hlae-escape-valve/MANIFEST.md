# Sim 07 — Data & Provenance Manifest

**Access / run date:** 2026-06-06
**Engine:** Boolean logic model (Python + pandas). No wet-lab data; no new dataset downloaded.

## Nature of inputs
This sim is a **logic extension of Sim 04** (`sims/04-immune-state-model/immune_state_model.py`),
not a new data pull. It adds cited mechanistic edges (HLA-E coupling, NKG2A brake, IFN-free Treg
depletion) and re-scans the intervention space. The **only experimental-data anchor** is inherited
transitively from Sim 04 / Sim 01:

| Upstream data anchor | Accession | Used for | Pulled by |
|---|---|---|---|
| CIC-DUX4 on/off transcriptome (IB120) | GEO **GSE60740** | baseline cell-state (MHC-I/B2M/NLRC5 low, HLA-E low, CD112 up) | Sim 01 / Sim 04 (not re-downloaded here) |

No accession, gene-effect value, expression value, drug, or trial number was invented in this sim.

## Literature sources for the added edges (URLs; verify before external use)
| Claim | Source | Tier |
|---|---|---|
| HLA-E binds CD94/NKG2A | Braud et al., *Nature* 1998 — https://www.nature.com/articles/35869 | Established |
| HLA-E surface needs VL9 leader peptide from classical HLA-A/-B/-C | review, PMC10690437; NKG2A:HLA-E review PMC11254306 | Established |
| IFN-γ upregulates HLA-E (NK-resistance, NMIBC/BCG) | PMC11398371 | Clinical-correlative |
| anti-NKG2A (monalizumab) disrupts NKG2A:HLA-E | review PMC11254306 | Clinical-Trial |
| metronomic cyclophosphamide / anti-CTLA-4 deplete Treg | Ghiringhelli metronomic-CTX; anti-CTLA-4 Treg depletion | Preclinical/Clinical `[VERIFY PMID]` |
| **EZH2i co-induces HLA-E in CIC-DUX4 (the FH-3 premise)** | **none found — INFERRED**, tagged Mechanistic/Theoretical | — |

Sim 04's own verified sources (Goel *Nature* 2017 PMID 28813415 CDK4/6i→antigen presentation+Treg↓;
senescence/NKG2D-ligand Aging 2016 PMID 26878797; NLRC5 PNAS 2016 PMID 27162338) carry over unchanged.

## Outputs (sha256, this run)
| File | sha256 |
|---|---|
| `hlae_escape_valve.py` | `200149ad05da0e477727b31d5ba0ac719abd070f9b8a4aaac41eb97ca19a1864` |
| `scan_coupling_on.csv` | `06acbf2da5c8c4b51bec15b635e3e72b3f29915423b9a079daf2ee2a46f3838a` |
| `scan_coupling_off.csv` | `571c86ae319d88332c236309c2f3d3bf6b2f74cc7a41489d9aa39f7c2b909e56` |
| `scan_b2mlost_coupling_on.csv` | `6ea2c709c45eda16ee0dc5d139ec9d9a108f13d07969d58b09adfb4eb7e06163` |
| `summary.json` | `aaecff4b12ab1f728e1cee6fb0203c1c726d7c1d4a8515dc4557a16f6d4541af` |
| `entities.txt` | `09da2c3ba440651bf00967aeea4b9c598d25bcd22adbdfdab27ee692c2bd63f8` |

## Grounding status
OpenMed NER **not run in this container** (no `.venv`; `openmed` mlx backend is Apple-Silicon-only).
`entities.txt` is prepared. To ground in a capable environment:
```
python scripts/openmed_ner.py --team v4-lead \
    --text-file sims/07-hlae-escape-valve/entities.txt --format tsv \
    > sims/07-hlae-escape-valve/grounding.tsv
```

## Reproducibility
```
python3 sims/07-hlae-escape-valve/hlae_escape_valve.py   # or .venv/bin/python
```
Deterministic (exhaustive combination scan; no randomness). Q1 parity check re-imports Sim 04 at
run time and will fail loudly if Sim 04's logic drifts.
