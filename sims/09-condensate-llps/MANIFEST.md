# Sim 9 — Data MANIFEST (condensate / LLPS, Track B)

## Inputs (fetched live at run time — nothing hard-coded)
| Input | Source | Accession | Role | Integrity gate | Status 2026-06-25 |
|---|---|---|---|---|---|
| DUX4 protein | UniProt | **Q9UBX2** (424 aa) | test: C-term transactivation domain (retained in CIC-DUX4) | UniProt SQ-line **CRC64** vs `Bio.SeqUtils.CheckSum.crc64` | ✅ CRC64 `C51E9EE25C6661B8` verified |
| EWSR1 protein | UniProt | **Q01844** (656 aa) | positive control: N-term prion-like LCD (EWS-FLI1 driver) | CRC64 | ✅ `0DA02CEE146720BB` verified |
| FUS protein | UniProt | **P35637** (526 aa) | positive control: canonical LLPS LCD | CRC64 | ✅ `88C8E263B7905549` verified |
| CIC protein | UniProt | **Q96RK0** (**2517 aa**) | negative control: HMG-box (folded) | CRC64 | ✅ `5C96D30F6C7F6065` verified |

Accessions are the standard human UniProt entries named in
`simulation-output/forward-simulation/in-silico-experiments.md` (Track B).

## Boundary verification (done 2026-06-25 against live UniProt feature tables)
The original domain coordinates were literature-derived from memory and flagged `[VERIFY]`. On the
network-permissive re-run they were checked against each entry's UniProt FT (DOMAIN / REGION /
DNA_BIND) lines and **3 of 4 corrected**:

| Protein | Old (memory) | **Verified (UniProt FT)** | UniProt feature used |
|---|---|---|---|
| DUX4 Q9UBX2 | 345–424 | **327–424** | `REGION 327..424 "Required for interaction with EP300 and CREBBP, and [transactivation]"` |
| EWSR1 Q01844 | 1–264 | **1–285** | `REGION 1..285 "EAD (Gln/Pro/Thr-rich)"` |
| FUS P35637 | 1–214 | **1–214** (kept) | `REGION 1..286 "Disordered"`; 1–214 = field-standard FUS-LC construct, kept for LLPS-literature comparability |
| CIC Q96RK0 | 201–280 | **1109–1177** | `DNA_BIND 1109..1177 "HMG box"` — old length 1608 was stale; the 201–280 slice hit a **disordered/low-complexity** region (invalid negative control). Now a true folded control (metapredict 0.30). |

`metapredict` empirical disorder (mean per-residue) corroborates the slices: DUX4 0.65, EWSR1 0.94,
FUS 0.95 (all disordered), CIC HMG-box 0.30 (folded) — the negative control reads folded only after
the boundary correction.

## Tools
| Tool | Channel | What it computes | Status |
|---|---|---|---|
| `localcider` (Pappu lab) | PyPI | FCR, NCPR, κ charge-patterning, Das-Pappu region, fraction disorder-promoting | Installed, self-test passed (`FCR=0.840, κ=0.626`); ran on 4 slices |
| `biopython` | PyPI | canonical SwissProt **CRC64** (integrity gate) | Installed; comparison normalises the `"CRC-"` prefix biopython prepends |
| `metapredict` (Holehouse lab) | PyPI (pulls torch) | per-residue disorder + empirical IDR boundaries | **Installed & used** (`metapredict available: True`) |
| **`PLAAC`** (Lancaster/King; whitehead/plaac) | precompiled `plaac.jar` (Java 11) | prion-HMM **PRDscore**/COREscore/LLR + **PAPA** aggregation propensity | **Installed & used**; jar `data/plaac.jar` (41 788 B) from `raw.githubusercontent.com/whitehead/plaac/master/web/bin/plaac.jar`; run on the 4 CRC-verified full-length proteins → `data/plaac_summary.txt` (+ per-residue `data/plaac_out.txt`) |

### Web-server predictors — attempted 2026-06-25, NOT obtained (not fabricated)
| Server | URL | Status 2026-06-25 |
|---|---|---|
| FuzDrop | https://fuzdrop.bio.unipd.it/ | Reachable (HTTP 200) but a **JS single-page app**; no clean accession/REST route (`/api/predict` → 404); requires **interactive** submission. Not scripted. |
| PScore | https://abragam.med.utoronto.ca/~JFKlab/ | **Unreachable** (connection timeout) |
| catGRANULE 2.0 | https://tools.dieterichlab.org/catGRANULE2/ | **Unreachable** (connection timeout) |
| PLAAC (web) | http://plaac.wi.mit.edu/ | Reachable; **CLI used instead** (reproducible) — see Tools |

These are the heterotypic/π-aware predictors that would most directly test the *refined* heterotypic
FH-9.1. Their absence is a real limitation, stated in RESULTS §5. **No score was invented for them.**

## Outputs
| File | Content |
|---|---|
| `descriptors.json` | localcider + metapredict comparative descriptor table (date-stamped) |
| `data/plaac_summary.txt` | PLAAC per-protein summary (PRDscore/COREscore/LLR/PAPA) |
| `data/plaac_out.txt` | PLAAC per-residue track (`-p all`) |
| `data/plaac_input.fa` | the 4 CRC-verified full-length sequences submitted to PLAAC |
| `entities.txt` / `grounding.tsv` | OpenMed NER grounding (team `v3-synthetic-lethality`) |
| `RESULTS_partial.json` | historical: the 2026-06-22 network-blocked attempt (provenance) |

`data/` is gitignored (caches + jar). No new accession, gene-effect value, drug, or dataset invented.
