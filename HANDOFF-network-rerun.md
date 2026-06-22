# HANDOFF — Network-permissive re-run of the 2026-06 plateau-break lanes

> **For the next Claude session.** This branch (`claude/protocol-plateau-discussion-eyie6t`) started
> two "inject new information" lanes to break the v1→v3 protocol plateau, but the session ran in a
> **network-restricted** environment (egress allowlist: only GitHub + PyPI reachable from code;
> `WebFetch` and UniProt/NCBI/EBI/clinicaltrials.gov all returned 403; web *search* worked at
> snippet level only). The work was committed honestly — nothing fabricated — but two things need a
> network-permissive environment to finish: **(1) execute Sim 9 for real numbers**, and
> **(2) full-text-verify every `[VERIFY]` citation** before any of it is promoted into the catalog.
>
> **Golden rules still apply** (`CLAUDE.md` §1): no fabricated citations; verify accessions/PMIDs/NCTs
> against live sources; regulatory/trial status is perishable; tier discipline; never prune the forward
> lane. This is research/hypothesis generation only — **not medical advice.**

---

## 0. First: confirm the environment can actually reach these hosts

Before doing anything, sanity-check egress (the last session was blocked on all of these):

```bash
.venv/bin/python - <<'PY'
import requests
for u in ["https://rest.uniprot.org/uniprotkb/P35637.fasta",
          "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi",
          "https://clinicaltrials.gov/api/v2/studies?query.term=CIC-DUX4&pageSize=1",
          "https://huggingface.co/api/models?limit=1"]:
    try: print(requests.get(u,timeout=20).status_code, u)
    except Exception as e: print("ERR", u, str(e)[:60])
PY
```
Need `200`s for: **rest.uniprot.org** (Sim 9), **eutils.ncbi.nlm.nih.gov / pmc.ncbi.nlm.nih.gov**
(citation verify), **clinicaltrials.gov** (trial status), **huggingface.co** (metapredict + OpenMed
NER). If any 403s, ask the user to widen the network policy
(https://code.claude.com/docs/en/claude-code-on-the-web) before proceeding — do **not** work around it
by inventing data.

---

## 1. What is already on this branch (done, committed)

| File | What it is | State |
|---|---|---|
| `simulation-output/evidence-refresh-2026-06.md` | Dated literature refresh; 5 genuine deltas vs the catalog | **Snippet-sourced; every citation `[VERIFY]`** — needs full-text verification |
| `sims/09-condensate-llps/run_condensate_llps.py` | Runnable, CRC64-gated `localcider`(+optional `metapredict`) Track-B pipeline | **Self-test passes; biological run aborted on UniProt 403** |
| `sims/09-condensate-llps/RESULTS.md` | Honest results + Forward Hypothesis FH-9.1 | Biological numbers **pending** a network run |
| `sims/09-condensate-llps/MANIFEST.md` | Inputs/accessions/integrity gate | Done |
| `sims/09-condensate-llps/RESULTS_partial.json` | Recorded 403 failures (provenance of the block) | Done |
| `sims/00-INDEX.md`, `simulation-output/findings-ranking.md` | Registers updated (Sim 9 row; 5 finding rows; date) | Done |

The headline scientific claim to validate-then-promote: **p300/CBP is a single node hitting three
vectors** — drives transactivation (V1/V3), *stabilises* the fusion protein, **and suppresses MHC-I**
(V4 priming) — which would reframe the catalog's MHC-I bridge away from EZH2i (now F4-US) to a
clinical-stage p300/CBP inhibitor.

---

## 2. TASK A — Execute Sim 9 (condensate / LLPS) for real

```bash
cd sims/09-condensate-llps
../../.venv/bin/python -m pip install -q localcider biopython requests numpy
../../.venv/bin/python -m pip install -q metapredict        # optional, pulls torch; enables empirical IDR calling
../../.venv/bin/python run_condensate_llps.py               # should now print a descriptor table + write descriptors.json
```

The script fetches DUX4 / EWSR1 / FUS / CIC from UniProt and **verifies each sequence against its
UniProt SQ-line CRC64** before computing (it aborts on mismatch — by design). Then:

1. **Verify the `[VERIFY]` domain boundaries** hard-coded in `run_condensate_llps.py` `TARGETS`
   against UniProt feature tables before trusting the slice (these are from memory):
   - DUX4 `Q9UBX2` (424 aa) — C-term transactivation domain `345–424`
   - EWSR1 `Q01844` (656 aa) — N-term prion-like EAD `1–264`
   - FUS `P35637` (526 aa) — N-term prion-like LCD `1–214`
   - CIC `Q96RK0` (1608 aa) — HMG-box (folded control) `201–280`
   With `metapredict` installed, also call `meta.predict_disorder_domains()` and **cross-check** the
   empirical IDR boundaries against these; correct the coords if they disagree.
2. **Add the canonical LLPS web-server scores** the offline run could not reach (Track B of
   `simulation-output/forward-simulation/in-silico-experiments.md`): **FuzDrop**, **PScore**,
   **catGRANULE 2.0**, **PLAAC**. Run the DUX4 C-term + EWSR1 EAD + FUS LCD + CIC HMG-box through each;
   record raw scores + URLs + access date in `MANIFEST.md`. These are the predictors that actually
   carry the field's LLPS signal; localcider only gives charge-patterning/diagram-of-states context.
3. **Interpretation rule:** the deliverable is a *relative ranking* (does the DUX4 C-term cluster with
   the EWSR1/FUS positive controls or with the folded CIC HMG-box negative control?). Tier ceiling stays
   **Theoretical/Mechanistic** — predictors are out-of-distribution for an artificial fusion module.
   Do **not** upgrade FH-9.1 above Theoretical on predictor scores alone.
4. **Grounding:** run OpenMed NER (`scripts/openmed_ner.py --team v3-synthetic-lethality`) on the sim's
   `entities.txt` once HuggingFace is reachable; write `grounding.tsv` (convention, `CLAUDE.md` §5).
5. Fill in `RESULTS.md` §1/§3 with the real descriptor table; update the Sim 9 row in
   `sims/00-INDEX.md` and `findings-ranking.md`.

---

## 3. TASK B — Full-text-verify the evidence refresh, then decide on promotion

Open `simulation-output/evidence-refresh-2026-06.md`. **Every accession/PMID/NCT is `[VERIFY]`**
(snippet-sourced). Confirm each against the real source + the registries in
`docs/09-verification-sources.md`, fix anything that doesn't resolve, and **strip the `[VERIFY]` flag
only on items you actually read**. Checklist:

**Direct CIC-DUX4 papers (the catalog-updating ones):**
- [ ] MCL1 dependency in patient-derived tumoroids — Nat Commun 2025 `s41467-025-62629-6` / PMC12370961.
      **Reconcile the PMID** (`findings-ranking.md` row notes `40841513 / 40841360` — pick the correct one).
      Confirm: drug-screen + CRISPR KO, **CCNE1/WEE1** co-dependency, **adavosertib in-vivo regression**, **ARID1A** recurrence.
- [ ] p300/CBP → MHC-I immune evasion — Mol Cancer 2025 `s12943-025-02485-6`. Confirm the MHC-I-suppression
      + IFN-γ-block claims (this is the load-bearing one for the promotion decision).
- [ ] Dual-ICB (nivolumab + relatlimab; PD-1+LAG-3) response case — npj Precision Oncology 2025 `s41698-025-00878-w`.
- [ ] DUX4–STAT1 / ISG inhibition — bioRxiv 2022 `10.1101/2022.08.09.503314` (preprint — keep tier honest).
- [ ] p300/CBP requirement + iP300w / A-485 + fusion-stability — Oncogenesis 2021 `s41389-021-00357-4` / PMC8511258.
- [ ] IGF1R/HMGA2/IGF2BP → trabectedin + dactolisib sensitivity — AACR Cancer Res 2022 `82(4):708`.
- [ ] 2024 chromatin profiling + dataset **GSE248040** — PMC10814785.

**Perishable trial/regulatory status (re-verify live on clinicaltrials.gov):**
- [ ] p300/CBP inhibitors: inobrodib/CCS1477 `NCT04068597` (heme), `NCT03568656` (solid, p300/CBP-mut);
      TT125-802 `NCT06403436` (solid phase 1). Any sarcoma arm? Current recruitment status?
- [ ] MCL1 inhibitors + cardiotox: AZD5991 (ClinCancerRes 2024, PMC11528199); S64315/AMG176/AMG397 halts;
      ABBV-467 troponin (`s43856-023-00380-z`); BRD-810 next-gen (Nat Cancer 2024, `s43018-024-00814-0`).

**Then decide promotion (ask the user):**
- If the p300/CBP→MHC-I claim verifies → draft **`protocol-v4.md`** (next version, do **not** overwrite
  v1/v2/v3 — `CLAUDE.md` §0) whose central change is a consolidated **p300/CBP multi-vector node**
  (V1/V3 throttle + fusion destabilisation + V4 MHC-I priming), augmenting/replacing the EZH2i-centric
  MHC-I bridge, plus: DUX4-STAT1/ISG as a distinct V4 evasion arm; the PD-1+LAG-3 doublet sequencing
  read; and the MCL1 cardiotox × prior-anthracycline down-weight for this patient.
- Consider whether this warrants an **ADR** (a methodology note that "live evidence refresh" is a
  standing lane that can update the catalog between full runs) — only if the user wants it framework-level.

---

## 4. TASK C — Mine the real CIC-DUX4 datasets (replace the Ewing proxy)

Once DepMap / GEO / figshare are reachable (`depmap.org`, `ftp.ncbi.nlm.nih.gov`/GEO, `figshare.com`):
- [ ] **GSE248040** (2024 CIC-DUX4 ChIP-seq) — extend Sim 1's single-line signature; could feed a real
      CIC-DUX4 L1000 signature-reversal (Track F) instead of the GSE60740-only basis.
- [ ] **Nat Commun 2025 patient-derived tumoroid** drug-screen + CRISPR data (check the paper's data-availability
      section for the accession) — the real-CIC-DUX4 dependency resource to cross-check Sim 2's Ewing proxy and
      Sim 3's WEE1 result.
- [ ] DepMap CIC-DUX4 lines TE441T / NCC-CDS1-X1-C1 / NCC-CDS1-X3-C1 — still no CRISPR screen at last check;
      mine CCLE **expression** at minimum.
Write each as a new `sims/NN-*/` (own `data/` gitignored, `MANIFEST.md` with sha256, `RESULTS.md`,
`grounding.tsv`) per `CLAUDE.md` §4; add a `findings-ranking.md` row in the same change.

---

## 5. Definition of done
- Sim 9 prints a real descriptor table + has FuzDrop/PScore/catGRANULE/PLAAC scores; `RESULTS.md` filled; grounded.
- Every `[VERIFY]` in `evidence-refresh-2026-06.md` is either confirmed (flag removed) or corrected/removed.
- Promotion decision made *with the user*; if yes, `protocol-v4.md` written (baselines preserved) and
  `findings-ranking.md` + README "Where to start" updated accordingly.
- Nothing fabricated; perishable statuses date-stamped; forward lane (FH-9.1) never pruned.
