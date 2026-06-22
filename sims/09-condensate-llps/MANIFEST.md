# Sim 9 — Data MANIFEST (condensate / LLPS, Track B)

## Intended inputs (fetched live at run time — nothing hard-coded)
| Input | Source | Accession | Role | Integrity gate |
|---|---|---|---|---|
| DUX4 protein | UniProt | **Q9UBX2** | test: C-term transactivation domain (retained in CIC-DUX4) | UniProt SQ-line **CRC64** vs `Bio.SeqUtils.CheckSum.crc64` |
| EWSR1 protein | UniProt | **Q01844** | positive control: N-term prion-like LCD (EWS-FLI1 driver) | CRC64 |
| FUS protein | UniProt | **P35637** | positive control: canonical LLPS LCD | CRC64 |
| CIC protein | UniProt | **Q96RK0** | negative control: HMG-box (folded) | CRC64 |

Accessions are the standard human UniProt entries named in
`simulation-output/forward-simulation/in-silico-experiments.md` (Track B). **[VERIFY]**
the accessions and the domain-boundary coordinates in `run_condensate_llps.py` before
relying on them — boundaries are literature-derived from memory and flagged `[VERIFY]`;
where `metapredict` is installed the script also derives IDR boundaries empirically.

## Tools
| Tool | Version channel | What it computes | Real / honest status |
|---|---|---|---|
| `localcider` (Pappu lab) | PyPI | FCR, NCPR, κ charge-patterning, Das-Pappu diagram-of-states region, fraction disorder-promoting | Installed & **self-test passed** (`FCR=0.840, κ=0.626` on the built-in test peptide) |
| `biopython` | PyPI | canonical SwissProt **CRC64** (sequence-integrity gate) | Installed |
| `metapredict` (Holehouse lab) | PyPI (optional; pulls torch) | per-residue disorder + empirical IDR boundaries | **Not installed** in this run (`metapredict available: False`) |

NOT used (web servers unreachable in this environment): FuzDrop, PScore, catGRANULE,
PLAAC. These are the canonical LLPS predictors named in Track B; their absence is a
real limitation, stated in RESULTS.

## Execution status in THIS environment — HONEST
**The biological run did not produce numbers.** This managed environment enforces a
network-egress **allowlist** (only GitHub + PyPI reachable; `rest.uniprot.org`,
`ebi.ac.uk`, NCBI e-utils, RCSB all return `403 Host not in allowlist`). All four
UniProt fetches returned HTTP 403, so the script **aborted by design (exit code 2)
rather than fabricate sequences** (golden rule #1). See `RESULTS_partial.json` for the
recorded failures. The toolchain (localcider self-test) is validated; only the network
input is blocked. Re-run where UniProt is reachable to obtain the descriptors.

## Outputs
| File | When produced |
|---|---|
| `descriptors.json` | on a successful (network-enabled) run — the comparative descriptor table |
| `RESULTS_partial.json` | this run — the recorded fetch failures (provenance of the block) |

No new accession, gene-effect value, drug, or dataset is invented. OpenMed NER
grounding pulls models from HuggingFace, which is **also** egress-blocked here, so
grounding is deferred to a network-enabled run (noted in RESULTS).
