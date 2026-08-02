# CASE BASELINE — the current working snapshot (Era B, from 2026-08-02)

> **This file is the canonical description of the case this repository is about.**
> Every agent, human contributor, and new piece of research works against **this** snapshot — not
> against the older framing still embedded in `protocol-v1..v4`, `sims/01–09`, `docs/`, and
> `ADR-0001..0020`. Those artifacts are **preserved, not rewritten**; §5 tells you how to read them.
>
> **Research simulation / hypothesis generation only. NOT medical advice, NOT a diagnosis.**

---

## 1. The baseline in one paragraph

The tumour is a **small round-cell sarcoma, clinically and histologically CIC-like / Ewing-like, with NO
confirmed fusion** on genomic testing — the ~5% genomically-uncharacterized subgroup. It has now
demonstrated, twice, a **deep response to conventional chemotherapy**: >95% necrosis at first-line
resection (Jan 2025) and **complete radiographic resolution of relapsed lung nodules after 4 cycles of
ifosfamide** (2026). That chemo-responsiveness is **atypical for canonical CIC-DUX4** — which is
repair-proficient and responds well in only ~30% of patients — and is the phenotype expected of the
Ewing/round-cell family instead. The working baseline is therefore: **a chemo-responsive, Ewing-like,
driver-unresolved round-cell sarcoma**, not "CIC-DUX4 sarcoma."

## 2. What is established, what is inferred, what is still open

Keeping these three columns apart is the whole point of this file.

| | Statement | Status |
|---|---|---|
| **Established (clinical record)** | No confirming CIC-DUX4 / CIC-NUTM1 / CIC-FOXO4 fusion was found on genome sequencing | **Fact** |
| | Morphology/clinic read as CIC-rearranged / Ewing-like small round-cell sarcoma | **Fact** (pathology) |
| | Excellent response to first-line VDC/IE (>95% necrosis); complete radiographic response of relapsed lung nodules to 4× ifosfamide | **Fact** (pathology report + imaging) |
| | Metastatic from diagnosis (12 lung nodules); WLI + leg RT; NED May 2025→May 2026; oligometastatic relapse May 2026 | **Fact** |
| **Inferred (modelled, ADR-0021 / Sim 10)** | The tumour's DNA-damage-response state is **repair-limited / SLFN11-competent** | **~94% posterior**, 90% CI 0.83–0.98 |
| | Most-likely driver is a **phenocopy / non-canonical entity (D4)** rather than cryptic CIC-DUX4 (D1) | **0.386 vs 0.264** — a *lean*, not a finding |
| **Still open** | **The actual driver is UNRESOLVED.** | see §3 |
| | Whether SLFN11 is expressed in this tumour (never measured; no SLFN11 data exist in CIC-DUX4 at all) | **Unmeasured** |
| | Whether the relapse is a drug-tolerant persister population or a pre-existing metastatic clone | **Unmeasured** |

### The single most important guardrail

> **"Not CIC-DUX4" is NOT the baseline. "Driver unresolved, CIC-DUX4 less likely than before" is.**
>
> Cryptic CIC-DUX4 (D1) still holds **~26%** posterior probability. CIC break-apart FISH has a documented
> 14–46% false-negative rate and short-read callers filter CIC::DUX4 on the DUX4 repeats — a fusion-negative
> report is *weak* evidence of fusion absence. Do not let this baseline harden into "it's Ewing sarcoma."
> **"Ewing-like" is a morphological descriptor covering several entities** (BCOR-altered, EWSR1::non-ETS,
> undifferentiated round-cell, true Ewing) — it is not a molecular diagnosis, and no EWSR1 fusion has been
> reported either.

## 3. Driver posterior (the current belief, from `sims/10-chemoresponse-cellstate/`)

| Driver hypothesis | Era-A prior | **Era-B posterior** |
|---|---|---|
| D1 — cryptic / false-negative **CIC-DUX4** | 0.450 | **0.264** |
| D2 — rare non-DUX4 CIC partner (NUTM1/FOXO4/LEUTX/NUTM2A) | 0.120 | 0.100 |
| D3 — non-fusion **CIC** inactivation (LOF) | 0.100 | 0.095 |
| **D4 — phenocopy / misclassified** (BCOR-altered, EWSR1::non-ETS, undifferentiated) | 0.200 | **0.386** |
| D5 — orphan / epigenetic phenocopy | 0.130 | 0.156 |

**Note the counter-intuitive part:** entropy over the driver **rose** (2.065 → 2.110 bits). The chemo
response did not identify the driver — it moved mass off a peaked D1 into a flatter D1-vs-D4 contest. The
driver question is *more* open than it was, not less. What the response *did* resolve is the cell state (§4).

## 4. The cell-state read (what actually gates therapy now)

| Property | Read | Basis |
|---|---|---|
| Proliferative fraction | **high, cycling** | alkylator CR requires cells in S-phase |
| Pharmacologic accessibility | **lesions are reachable** — small, well-perfused lung nodules | the CR itself; favours antibodies + cell therapies, which are more delivery-limited than small molecules |
| Mitochondrial apoptotic priming | **INTACT** — damage converts to death | the CR itself (a BH3 profile without the assay) |
| DNA-damage response | **sensing-competent, repair-limited** → predicted **SLFN11-positive** | Sim 10; *predicted, never measured* |
| Relapse-seeding compartment | **drug-tolerant persister reservoir** — slow-cycling, epigenetic/reversible, GPX4-dependent | relapse after deep response; class-level persister biology |

**Strategic consequence:** chemotherapy has solved the *bulk* problem twice. The unsolved problem is the
**reservoir**, and it has a different vulnerability profile than the bulk — so cell-cycle-directed agents
(CDK4/6i) and more bulk cytotoxicity are aimed at the part of the disease already being handled.

## 5. How to read Era-A artifacts (the translation table)

Era-A artifacts are **preserved, not rewritten** — ADRs are append-only, and `protocol-v1..v4` are retained
baselines. Read them through this table.

### 5a. The transferability ladder inverts (this is the big operational change)

`docs/10-evidence-transferability-hierarchy.md` (ADR-0014) scores evidence by biological proximity, with
**P0 = "in CIC-DUX4"** as the closest rung. Era-A treated CIC-DUX4-direct evidence as automatically P0 for
this case. **That assumption no longer holds.**

> **This case now has NO P0 anchor.** Neither CIC-DUX4-specific nor Ewing-specific evidence is "in this
> tumour," because we do not know what this tumour is. Directness must be **posterior-weighted across the
> driver hypotheses** rather than assumed.

| Evidence class | Era-A weighting | **Era-B weighting** |
|---|---|---|
| **CIC-DUX4-direct** (p300/CBP papers, MCL1 tumoroid papers, DUX4-STAT1/ISG antagonism, GSE60740) | P0 — closest possible | **Discounted to ~D1+D2 posterior (~0.36), not excluded.** Still the best mechanistic anchor *if* the driver is CIC-class. |
| **Ewing / fusion round-cell family** (SARC028, SLFN11/EWS-FLI1, rEECur, Ewing DepMap proxy lines) | P1 — one rung down | **Up-weighted** — D4 is now the leading hypothesis, and the chemo phenotype independently matches this family. Arguably the *closest available* anchor. |
| **Fusion-agnostic** (host biology, immune/NK, cell-cycle, danger-signalling, modality/feasibility) | full weight | **Unchanged — full weight.** These were never driver-dependent and are the most robust part of the catalog. |
| **Evidence conditioned on the chemo-RESISTANT CIC phenotype** (POLE-high/repair-proficient reasoning) | assumed to apply | **Contradicted by this patient's phenotype** — down-weight sharply. |

A useful side effect: the Ewing-proxy substitutions the sims already made out of necessity (Sim 2 used
Ewing DepMap lines because no CIC-DUX4 CRISPR screen exists) are **less of a compromise under Era B than
they were under Era A**.

### 5b. Specific Era-A positions that change

| Era-A position | Era-B status |
|---|---|
| "CIC-rearranged sarcoma, CIC-DUX4 fusion" as the case framing | **Superseded** by this file |
| **"Resolve the driver first"** is the highest-leverage next action (ADR-0008) | **Qualified.** Still top-EVSI, but its purpose narrowed: it now mainly serves to re-open the fusion-contingent options. The therapeutically decisive variable (DDR state) was already resolved by the clinical course. |
| **MCL1 "re-arm the DUX4 death program"** — most promising novel target | **Held / demoted on two independent axes** — driver-contingent (ADR-0008) *and* phenotypically argued against (intact apoptotic priming, ADR-0021). Also cardio-gated by prior anthracycline. |
| **Junction-specific ASO / vaccine / TCR-T / CAR-T** | **Held.** Requires both a real fusion *and* a resolved junction; the drivers that support it lost posterior mass. |
| **"CIC-DUX4 is chemo-resistant"** as a background assumption | **Does not describe this patient.** Any reasoning that leaned on it must be re-derived. |
| EZH2i repositioned as MHC-I priming, not cytotoxic (Sim 2, real DepMap data) | **Unchanged, and reinforced** — it gains a second rationale (SLFN11 maintenance, ADR-0021). Sim 2's real-data finding stands. |
| Throttle / cell-cycle / immune backbone (BETi, CDK4, NK/checkpoint) | **Unchanged** — driver-robust by construction (Sim 8), with one new caveat: CDK4/6i targets the cycling bulk, not the persister reservoir. |
| Golden rules #1–#10; the four fixed vectors; all layers (host-biology, feasibility, modality, VoI, steering) | **Unchanged.** Golden rule #9 (the atypical-case flag) moves from a footnote to the **centre** of the framing. |

## 6. Epistemic eras — the demarcation

| Era | Dates | Working assumption | Artifacts authored under it |
|---|---|---|---|
| **Era A** | 2026-06-02 → 2026-08-01 | **Canonical CIC-DUX4** sarcoma; fusion-unconfirmed treated as an *edge case* flagged per-entry | `protocol-v1..v4`, `sims/01–09`, `ADR-0001..0020`, all vector outputs, all analytical layers, `docs/00–11` |
| **Era B** | 2026-08-02 → | **Chemo-responsive, Ewing-like, driver-unresolved** round-cell sarcoma; the atypical case *is* the case | `CASE-BASELINE.md` (this file), `ADR-0021`, `ADR-0022`, `sims/10-chemoresponse-cellstate/`, `simulation-output/chemosensitivity-ddr-cellstate-layer.md` |

**Rule:** Era-A artifacts are never retro-edited to match Era B. They are historical records of what was
concluded under what assumption. When an Era-A conclusion conflicts with this baseline, **this baseline
wins for new work**, and §5b records the delta.

## 7. Verification status — read before quoting anything from Era B

The Era-B evidence spine is **snippet/abstract-level only**. PubMed, PMC, nature.com, EuropePMC, Crossref
and the NCBI E-utilities all returned **HTTP 403** through this environment's proxy on 2026-08-02; only
`PMID 29088702` was seen as a literal PubMed record identifier. Every Era-B citation therefore carries
**`[VERIFY]`**, and under **ADR-0020**'s mandatory gate:

> **No Era-B finding may be promoted into a `protocol-vN.md` until it is full-text-verified against a live
> source with the PMID/DOI confirmed inline.** Era B is currently a **forward-lane** baseline.

This does **not** weaken the *case facts* in §2 (those come from the patient record, not the literature) —
it constrains the *mechanistic interpretation* in §4 and §5a.

## 8. What would change this baseline again

| If… | Then… |
|---|---|
| Long-read WGS+RNA-seq finds a **canonical CIC::DUX4 junction** | Era B is largely reverted — D1 confirmed, this becomes a chemo-sensitive CIC-DUX4 outlier, and the full Era-A catalog re-applies (with the chemo phenotype as an outlier annotation) |
| **Methylation array returns CIC class** | D4 collapses; the CIC-directed catalog re-strengthens; the cell-state read (§4) survives independently |
| **Methylation array returns a non-CIC class** (e.g. BCOR, Ewing) | Era B hardens into a *specific* entity, and that entity's own literature becomes the P0 anchor |
| **SLFN11 IHC is negative** | The §4 DDR read fails; chemo-sensitivity runs through another route (e.g. HR/ARID1A) and the ATR/CHK1i branch opens |
| Disease **stops responding** to DNA-damaging chemotherapy | The core Era-B premise is gone; re-derive from the resistant phenotype |

## 9. Where to go next

| Question | Read |
|---|---|
| What does the chemo response imply, and which immunotherapy vector/timing? | `simulation-output/chemosensitivity-ddr-cellstate-layer.md` (+ `sims/10-chemoresponse-cellstate/`) |
| The full ranked hypothesis catalog (Era A — read via §5) | `simulation-output/protocol-v4.md` |
| Every finding scored on the three axes | `simulation-output/findings-ranking.md` |
| Why the framework operates the way it does | `docs/adr/README.md` (ADR-0021, ADR-0022 are the Era-B records) |
| How sessions and agent teams work | `CLAUDE.md` |

---

*Baseline established 2026-08-02 (ADR-0022). Research simulation / hypothesis generation only —
not medical advice, not a diagnosis, and not a testing or treatment recommendation.*
