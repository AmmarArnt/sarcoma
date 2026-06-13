# Biomarker Value-of-Information & Missing-Data Stratification Layer

**In response to GitHub issue #7** — *"High-impact missing biomarkers and future stratification
opportunities"* (@Cerimagic).

> **See also:** [`biomarker-voi-provenance-extension.md`](biomarker-voi-provenance-extension.md)
> ([ADR-0011](../docs/adr/0011-voi-provenance-temporal-axis.md)) extends Tier B below with two further
> axes from the issue #7 follow-up — **acquisition provenance** (archived FFPE / fresh biopsy / liquid)
> and **temporal state** (baseline / current / change-under-treatment).

**Status:** framework-enhancement proposal + applied result for the current fusion-unconfirmed case.
Research-simulation output, **not medical advice**, **not a recommendation to obtain any specific
test**. The goal, exactly as the issue framed it, is to *make uncertainty explicit* — to document
which unknown variables would most change vector prioritization, **not** to require testing.

---

## 1. The question, restated

The issue asks whether the framework should explicitly separate:

1. **currently available** patient data,
2. **missing but potentially obtainable** data, and
3. **missing data that would likely have little impact** on decision-making —

and whether it could **rank the unknown biomarkers by how much they would change vector prioritization
if they became available** (MHC-I status, NK markers, PD-L1, nectin/TIGIT axis, immune infiltration,
additional genomic/transcriptomic features).

**Short answer: yes, and it is computable, not just descriptive.** The existing immune-state model
(Sim 4) already encodes most of these markers as decision variables. We can therefore measure each
one's **value of information (VoI)** — how often learning it changes the recommended program — instead
of merely listing it. We did this in a new simulation, **Sim 6**
(`sims/06-biomarker-value-of-information/`), and propose a standing three-tier taxonomy below.

---

## 2. Proposed taxonomy (the framework layer)

For every case, classify each biomarker into one of three tiers. Tier B is ordered by **VoI** — the
fraction of plausible background states in which learning the marker changes the recommended vector or
regimen.

| Tier | Definition | How the framework should treat it |
|---|---|---|
| **A — Known** | On record for this patient | Anchors the baseline state; no action |
| **B — Missing, decision-relevant (obtainable)** | Not measured; **would change prioritization**; obtainable from archived tissue / repeat biopsy / added molecular testing | **Rank by VoI**; surface as "highest-value unknowns" with the assay and the vector each informs — *as documentation of uncertainty, not a testing mandate* |
| **C — Missing, low-impact** | Not measured; **unlikely to change the current decision** (e.g., redundant with a known marker, or only relevant in a state this case is not in) | Record once with the *reason* it is low-impact; do not propagate as a gap |

**Design principle (ties to issue #8):** a hypothesis that depends on a Tier-B unknown should be
**flagged as conditional** ("contingent on X") rather than propagated at full confidence. Uncertainty
in an input should attenuate the strength of any downstream recommendation that hinges on it.

---

## 3. Applied to the current case (fusion-unconfirmed, post-VDC/IE, lung-relapse)

### Tier A — Known
Histology (CIC-rearranged sarcoma), **fusion status = UNCONFIRMED (atypical ~5% subgroup)**, lung-only
metastatic pattern, full treatment history (VDC/IE ×14, >95% necrosis at resection, leg RT + whole-lung
irradiation, oligometastatic lung relapse, imminent high-dose ifosfamide).

### Tier B — Missing, decision-relevant, ranked by VoI
Critically, **the tumor's immune profile was never measured** for this case — so every marker the issue
lists is currently an *assumption* in the catalog. Sim 6 ranks them (total-effect decision-flip
frequency across all background uncertainty; see `sims/06-.../RESULTS.md`):

| Rank | Biomarker (assay) | VoI (decision-flip) | What it changes | Vector |
|---|---|---|---|---|
| **1** | **Nectin CD155 / CD112** (DNAM-1 ligand) IHC | **0.625** | Its loss makes non-cytotoxic selective clearance **unreachable** (gates *both* T-cell and NK kill) — no fallback | V4 nectin/TIGIT gate |
| **2** | **HLA-E** expression | **0.500** | HLA-E⁺ closes the NK route → forces the T-cell / MHC-I-priming route | V4 NK |
| 3 | **Treg / FoxP3** TME burden | 0.312 | Changes *which* agents are needed (regimen composition) | V4 T-cell + NK |
| 3 | **TIGIT** axis expression | 0.312 | Same — composition of the brake-release regimen | V4 nectin/TIGIT |
| 5 | **NK functional reserve** (post-WLI/chemo) | 0.250 | Unfit NK forces T-cell route or host repair (IL-15) | V4 NK |
| 6 | **MHC-I / B2M / TAP1** integrity | 0.188 | Decides V3-prime→T-cell vs NK-first — but NK fallback limits its marginal value | V3→V4 T-cell |
| 6 | **CD8+ TIL** density | 0.188 | T-cell-arm input; NK route is robust to it at baseline | V4 T-cell |

### Tier C — Missing, low-impact (with the reason)
- **Baseline PD-L1 IHC** — low VoI **in this model**, because PD-L1 is encoded as *IFN-induced /
  adaptive* (it switches on once priming begins), so a static pre-treatment value rarely enters the
  decision. *Caveat: this low rank is a property of the adaptive-PD-L1 modeling assumption and is
  stated, not hidden — if the model treated PD-L1 as a fixed input it would rank higher.*
- **mRNA-COVID-vaccine immune status** — already established as a null at >2 years (see
  `mrna-vaccine-research/`); not a current decision variable.

---

## 4. The non-obvious finding (why this is worth more than a checklist)

The issue listed **MHC-I expression status first** — the natural intuition. The model says the
**nectin (CD155/CD112) axis outranks it**, and explains why: in the kill-rule logic the DNAM-1
activating signal gates **both** effector arms, so losing the nectin ligand collapses the entire
non-cytotoxic program with **no fallback** — whereas MHC-I/B2M loss merely *reroutes* T-cell→NK (the
documented antigen-loss fallback). The three NK-arm variables — **nectin, HLA-E, NK fitness** —
collectively dominate the case's decision uncertainty, which is consistent with the catalog's
**NK-first** hypothesis and Sim 5's finding that host NK state must be repaired (IL-15) in unfit hosts.

This is precisely the value the issue anticipated: making explicit *which* unanswered biological
questions would most move therapeutic prioritization — and occasionally **correcting** an intuitive
ranking.

---

## 5. Honest limitations (what this does and does not claim)

- **Ranks what to measure, not the measurement.** High VoI ≠ "this marker is abnormal in this patient."
- **Model-relative magnitudes.** The ordering is driven by the Boolean kill-rule structure (DNAM_active
  is a shared AND-gate); a different encoding would shift magnitudes. The robust takeaway is the
  *ordering logic* (NK-axis markers > T-cell-axis markers, given the antigen-loss fallback), not the
  decimal values.
- **Inherits Sim 4 limitations** — qualitative Boolean logic; transferred (non-CIC-DUX4-validated)
  mechanism edges; single-cell-line baseline (GSE60740).
- **Fusion-junction status is out of scope here** — it governs a separate decision (junction ASO /
  vaccine / CAR-T), and the atypical fusion-unconfirmed flag is unchanged.
- **Not a testing recommendation.** This documents uncertainty for future contributors; any actual
  testing decision belongs to the patient's oncologist.

**Evidence tier of this layer:** `Theoretical / Mechanistic` (a decision-sensitivity analysis over a
qualitative model anchored to one real dataset). It is a *prioritization* tool, not evidence about the
patient.

---

*Provenance:* `sims/06-biomarker-value-of-information/` (script `run_voi.py`, `RESULTS.md`,
`voi_ranking.csv`, `oat_detail.csv`, `voi_summary.json`, `MANIFEST.md`). Built on the validated Sim 4
immune-clearance model and the Sim 1 GSE60740 real-data baseline. No new biology, no fabricated
citations. Not medical advice.

*Decision record:* this layer was adopted via [ADR-0001](../docs/adr/0001-missing-data-taxonomy-and-voi-layer.md)
(issue #7 / PR #15).
