# Manifest — Sim 10, Chemo-Response Phenotype → Driver Re-Conditioning + DDR Cell-State Resolution

**Type:** Bayesian decision model (hierarchical latent-variable update + EVSI + sensitivity sweep).
**No external data download.** Encodes published mechanism as a two-layer latent model
(`driver → DDR state → observed response`) and computes consequences. Extends **Sim 8** (ADR-0008) at the
extension point Sim 8 named itself, and reuses the value-of-information methodology of **Sim 6** (ADR-0001).

## Clinical observations used as the likelihood input
From the patient case anchored in `simulation-output/protocol-v4.md` §Patient case:
| ID | Observation | Provenance |
|---|---|---|
| O1 | Excellent histologic response to first-line VDC/IE (>95% necrosis at resection, Jan 2025) | patient case record (already in protocol-v1..v4) |
| O2 | Complete radiographic response of relapsed lung nodules after 4 cycles of ifosfamide | reported by the user, 2026-08 (this session) |

## Parameter provenance

| Parameter | Value | Source / status |
|---|---|---|
| Driver prior `p(D)` = [0.45, 0.12, 0.10, 0.20, 0.13] and its sweep ranges | unchanged | **Carried verbatim from Sim 8** / `driver-uncertainty-specialist.md` (so the update is attributable to the phenotype alone) |
| CIC-rearranged sarcoma: **~30%** of patients show a good chemotherapy response, **lower than Ewing** | anchors `P(O1\|D1)` | Connolly et al., *Cancer Medicine* 2022, "Systemic treatments and outcomes in CIC-rearranged sarcoma" (PMC9041083) — **`[VERIFY]` snippet-sourced**, full text not retrievable (egress) |
| CIC advanced disease: median OS 12.6 mo, median PFS 5.8 mo; CanSaRCC + JHU response breakdowns | context, not a fitted parameter | *J Cancer Res Clin Oncol* 2024, DOI 10.1007/s00432-024-05631-7 (PMC10912249); CanSaRCC (PMC12815609) — **`[VERIFY]`** |
| **CIC::DUX4 is repair-PROFICIENT via POLE upregulation** → `P(S_hi\|D1)=0.20` | the load-bearing mechanistic asymmetry | "Upregulation of POLE and proficient DNA repair are features of CIC::DUX4 sarcomas," *npj Precision Oncology* 2025, DOI **10.1038/s41698-025-00985-8** — **`[VERIFY]`**, abstract/snippet only (nature.com returned HTTP 403) |
| **EWS-FLI1 transactivates SLFN11** → Ewing chemo-sensitivity → `P(S_hi\|D4)=0.75` | the opposing arm | Tang et al., *Clin Cancer Res* 2015, DOI **10.1158/1078-0432.CCR-14-2112** — **`[VERIFY]`**, abstract/snippet only |
| Ewing good histologic response **~53%** | consistency check for `P(O1\|D4)` | neoadjuvant-response scoring literature (*J Bone Oncol* / retrospective series) — **`[VERIFY]`** |
| Relapsed Ewing: high-dose ifosfamide median EFS **5.7 mo**, median OS **16.8 mo**, 6-mo EFS **47%** → `P(O2\|S_hi)=0.55 < P(O1\|S_hi)` | keeps the relapse CR from being over-weighted | **rEECur** RCT, *J Clin Oncol* 2022;40(17_suppl):LBA2 — **`[VERIFY]`** |
| **EZH2/H3K27me3 silences SLFN11 → "chemosensitive relapse"; EZH2i prevents acquired resistance** | motivates the `SLFN11_maintenance` intervention | Gardner et al., *Cancer Cell* 2017, S1535-6108(17)30006-5 — **`[VERIFY]`** |
| Class-I HDACi (entinostat, romidepsin) and 5-aza **reactivate SLFN11** and re-sensitise to DNA-damaging agents | same | Murai et al., *Clin Cancer Res* 2018;24(8):1944 — **`[VERIFY]`** |
| **SLFN11-low cells are synthetic-lethal with ATR/CHK1 inhibition** | the opposing `ATR_CHK1i` branch | *PNAS* 2021, DOI 10.1073/pnas.2015654118 — **`[VERIFY]`** |
| **Drug-tolerant persisters are GPX4-dependent / ferroptosis-vulnerable**; KDM5A-associated chromatin state | motivates `GPX4_ferroptosis_persister` | Hangauer et al., *Nature* 2017, **PMID 29088702** — PMID confirmed via PubMed listing; abstract-level |
| Lymphodepletion → homeostatic proliferation, IL-7/IL-15 sink vacancy, Treg depletion | motivates `immune_MRD_window_NKfirst` | *Cancer Res* 2005;65(20):9547 (host-lymphodepletion augments adoptive T-cell therapy) — **`[VERIFY]`** |
| Intervention `value` / `penalty` and the seven Sim-8 `p_by_D` vectors | unchanged from Sim 8 | transparent mechanistic judgements, stated in code |

## `[VERIFY]` status — read this before quoting any citation above

**Direct literature egress was blocked in this session** (verified 2026-08-02): `eutils.ncbi.nlm.nih.gov`,
`pubmed.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov/pmc`, `nature.com`, `europepmc.org`,
`api.semanticscholar.org` and `api.crossref.org` all returned HTTP 403 through the agent proxy. Every
citation above was therefore obtained at **search-snippet / abstract level only** and carries `[VERIFY]`
per **ADR-0020**. Only `PMID 29088702` (Hangauer) was seen as a literal PubMed record identifier.

**Consequence under ADR-0020's mandatory gate:** none of these claims — and therefore no finding in this
sim — may be promoted into a `protocol-vN.md` until full-text/abstract-verified against a live source with
the PMID/DOI confirmed inline. This sim and its layer artifact sit in the **forward//hypothesis lane** until
that verification happens.

## Egress note (verified 2026-08-02)
`pypi.org` reachable (numpy installed into a fresh `.venv`; the repo venv is gitignored and absent in a
fresh container). HuggingFace blocked → **OpenMed NER grounding could not run**; `grounding.tsv` records
the block and no grounding scores are invented.

## Reproduce
```
.venv/bin/python sims/10-chemoresponse-cellstate/run_chemoresponse_cellstate.py
```
Deterministic (numpy seed 20260802; 20 000 sweep samples). Outputs: `driver_posterior.csv`,
`state_posterior.csv`, `intervention_reranking.csv`, `test_value_of_information.csv`,
`sensitivity_sweep.csv`, `entities.txt`.

## Honest scope
A decision model, not a diagnosis, not a testing recommendation and not medical advice. It shows what the
encoded mechanism plus a literature-anchored prior imply once this patient's observed chemotherapy response
is treated as evidence. GIGO applies — the parameters are stated explicitly so they can be challenged, and
the two weakest (`P(S_hi|D1)`, and the assumed conditional independence of O1 and O2) are named in
`RESULTS.md` §Limitations.
