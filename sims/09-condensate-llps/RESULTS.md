# Sim 9 — RESULTS: Condensate / LLPS propensity of the CIC-DUX4 transactivation module (Track B)

**Run dates:** pipeline authored 2026-06-22 (network-blocked); **biological run executed 2026-06-25**
(network-permissive). **Status:** ✅ executed — real descriptors from `localcider` + `metapredict`
+ `PLAAC`; canonical web servers (FuzDrop/PScore/catGRANULE) partly unobtainable (see §5).
**Research simulation / hypothesis generation only. Not medical advice.**

---

## 0. One-paragraph honest summary

This sim asks whether the **DUX4 C-terminal acidic transactivation domain** — the module CIC
retains in the CIC-DUX4 fusion — is predicted to drive **biomolecular condensates** the way the
EWSR1 and FUS prion-like low-complexity domains (LCDs) do. The pipeline (real tools: `localcider`
Das-Pappu/Uversky charge-patterning, `metapredict` per-residue disorder, `PLAAC` prion-HMM + PAPA;
CRC64 sequence-integrity verification against UniProt) **ran to completion on 2026-06-25** against
live UniProt. **Headline (honest, and partly a negative result):** the DUX4 C-term is a *bona fide*
intrinsically disordered region (metapredict mean disorder **0.65**), but it is an **acidic
activation-domain–type IDR** (strongly net-negative, charge-driven, aromatic-poor) — it does **not**
cluster with the EWSR1/FUS prion-like LCDs, and **PLAAC calls no prion domain in it (PRDscore 0.0)**
versus 77.6 (EWSR1) and 113.7 (FUS). So the **FET-fusion homotypic, prion-like self-assembly
mechanism does not transfer to CIC-DUX4.** This *sharpens* FH-9.1 rather than killing it: if CIC-DUX4
builds a transcriptional condensate it must be **heterotypic** — the acidic AD partitioning into a
**p300/CBP-coactivator/acetyl-reader condensate** — which is exactly the chemistry the known DUX4→
p300/CBP biology predicts, and gives a cleaner falsifier. Tier ceiling stays **Theoretical /
Mechanistic** (predictors are out-of-distribution for an artificial fusion module).

## 1. What executed (2026-06-25 network-permissive re-run)

| Step | Status |
|---|---|
| `localcider` import + self-test (`FCR=0.840, κ=0.626`) | ✅ passed |
| CRC64 integrity gate (`Bio.SeqUtils.CheckSum.crc64`, prefix-normalised) | ✅ all 4 sequences verified against UniProt SQ line |
| Fetch UniProt Q9UBX2 / Q01844 / P35637 / Q96RK0 | ✅ **HTTP 200** (network now open) |
| **Domain boundaries verified against live UniProt FT tables** | ✅ 3 of 4 corrected — see MANIFEST §"Boundary verification" |
| Descriptor computation (localcider) | ✅ table below |
| `metapredict` empirical disorder | ✅ installed; mean-disorder column populated |
| `PLAAC` prion-HMM + PAPA (Java CLI) | ✅ run on the 4 CRC-verified full-length proteins |
| FuzDrop / PScore / catGRANULE 2.0 / PLAAC-web | ⚠️ not obtained — see §5 (servers down / interactive-only on 2026-06-25); **not fabricated** |
| OpenMed NER grounding | ✅ `grounding.tsv` (HuggingFace reachable) |

> A note on the original block: the 2026-06-22 run aborted on what looked like a CRC64 mismatch.
> The 2026-06-25 re-run found this was a **format bug** (biopython's `crc64()` returns a `"CRC-…"`
> prefix the comparison didn't strip), *not* a sequence problem — the checksums matched once
> normalised. Fix is in `run_condensate_llps.py`. `RESULTS_partial.json` is retained as historical
> provenance of the original network-blocked attempt.

## 2. The biology this is testing (why the DUX4 C-term is the right substrate)

- CIC-DUX4 = repressor CIC (incl. its **HMG-box** DNA-binding domain) fused to the **DUX4
  C-terminal transactivation domain**; the fusion converts CIC from repressor to strong activator.
  *(Established.)*
- UniProt annotates that very C-terminal module (Q9UBX2 **REGION 327–424**) as *"Required for
  interaction with EP300 and CREBBP"* — i.e. the domain's defined job is **recruiting the histone
  acetyltransferases p300/CBP** to CIC target sites → H3 acetylation → target activation; p300/CBP
  is *required* for CIC-DUX4 activity and stabilises the fusion protein. *(Preclinical-Cell/Animal —
  see evidence-refresh artifact for citations.)*
- **p300/CBP and histone-acetylation are established nucleators of transcriptional condensates**
  (acetyl-reader/BRD4 + coactivator phase behaviour). So a domain whose whole job is to *recruit
  p300/CBP and build an acetylated activating hub* is a mechanistically reasonable **heterotypic**
  condensate-partitioning element — yet **no DUX4 or CIC-DUX4 LLPS study exists** (2026-06 sweep
  found none; the field's condensate work is on EWSR1/FET fusions). That gap is the opportunity.

## 3. Results — comparative descriptor table (REAL, 2026-06-25)

Domain slices are the **UniProt-feature-verified** boundaries (MANIFEST §boundary-verification).
Source: `descriptors.json` (localcider + metapredict) and `data/plaac_summary.txt` (PLAAC).

| Protein | Role | Region (verified) | n | FCR | NCPR | κ | %acidic | %basic | %aromatic | Das-Pappu | metapredict mean-disorder | **PLAAC PRDscore** | PLAAC PAPAprop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|:--:|---:|---:|---:|
| **DUX4** | **test** | C-term transactiv./EP300-CREBBP (327–424) | 98 | 0.194 | **−0.153** | 0.199 | **0.173** | 0.020 | **0.031** | 1 | **0.649** | **0.00** | −0.078 |
| EWSR1 | pos. control | N-term prion-like EAD (1–285) | 285 | 0.039 | −0.018 | 0.158 | 0.028 | 0.011 | 0.140 | 1 | 0.943 | **77.58** | +0.057 |
| FUS | pos. control | N-term prion-like FUS-LC (1–214) | 214 | 0.028 | −0.019 | 0.208 | 0.023 | 0.005 | 0.126 | 1 | 0.946 | **113.68** | +0.101 |
| CIC | neg. control | HMG-box, folded (1109–1177) | 69 | 0.290 | +0.116 | 0.130 | 0.087 | 0.203 | 0.130 | 2 | **0.297** | **0.00** | −0.112 |

*(PLAAC PRDscore = prion-domain score from the prion-HMM; PRDstart/end for EWSR1=1–328, FUS=1–257;
DUX4 & CIC: no prion domain identified. Full PLAAC summary in `data/plaac_summary.txt`.)*

**What the numbers say (three independent algorithm families converge):**

1. **DUX4 C-term IS disordered** (metapredict 0.65) — so it *can* in principle participate in
   condensates; it is not a folded domain.
2. **But it is the wrong *flavour* of IDR to self-assemble like FET LCDs.** It is **strongly acidic
   and charge-driven** (NCPR −0.15, 17% acidic, FCR 0.19) and **aromatic-poor** (3%), the signature
   of a classical **acidic activation domain** — the opposite of the **low-charge, aromatic-rich**
   (~13% aromatic, FCR ~0.03) prion-like LCDs of EWSR1/FUS that drive homotypic π-mediated phase
   separation.
3. **PLAAC makes this decisive:** **no prion domain is called in the DUX4 C-term (PRDscore 0.0)**,
   while EWSR1 (77.6) and FUS (113.7) score as strongly prion-like; PAPA agrees (DUX4 negative,
   controls positive). DUX4 clusters with the **folded CIC negative control** on prion-likeness.
4. **The negative control behaves correctly now** (metapredict 0.30, folded) — validating the
   boundary correction from the broken 201–280 slice to the real HMG box 1109–1177.

## 4. Forward Hypothesis (the deliverable — *refined* by the real numbers)

**[FH-9.1, refined] CIC-DUX4 organises a p300/CBP-dependent, acetylation-driven transcriptional
condensate by *heterotypic* partitioning of its acidic DUX4 C-terminal activation domain into a
coactivator/acetyl-reader hub — NOT by FET-type homotypic prion-like self-assembly — and this
property is invariant across fusion-junction variants.**
- *Mechanistic basis (now data-anchored):* the DUX4 C-term is a verified IDR (metapredict 0.65) but
  is an **acidic AD, not a prion-like LCD** (this sim: PLAAC PRDscore 0 vs 77.6/113.7; aromatic-poor,
  net-negative). Acidic ADs drive **heterotypic** condensation by partitioning into coactivator
  (p300/CBP/Mediator) condensates rather than self-associating. The DUX4 C-term's defined function —
  UniProt "Required for interaction with EP300 and CREBBP" — is exactly that partitioning chemistry.
- *Why the refinement matters:* it **kills the naive EWSR1-analogy transfer** (don't expect CIC-DUX4
  to phase-separate via a prion-like module) and **redirects the hypothesis onto the p300/CBP node**
  — which is *independently* the catalog's emerging multi-vector target (evidence-refresh §B). The
  in-silico result and the druggable-node story now point at the *same* place.
- *In-silico test (done here):* score DUX4 C-term vs EWSR1 EAD / FUS-LC (pos.) and CIC HMG-box (neg.)
  on charge-patterning + disorder + prion-HMM. **Result: DUX4 is a disordered acidic AD, not
  prion-like** → supports the *heterotypic* model, refutes the *homotypic* one. (Adding
  FuzDrop/PScore/catGRANULE — heterotypic-aware predictors — would test the heterotypic-droplet
  propensity directly; see §5, deferred.)
- *Wet-lab falsifier (names the disconfirming experiment, per golden rule #5):* 1,6-hexanediol
  sensitivity / optoDroplet / live-imaging of CIC-DUX4 puncta; and a **p300/CBP-inhibitor (A-485,
  inobrodib) condensate-dissolution test**. The refined model predicts CIC-DUX4 hubs are **p300/CBP-
  inhibitor-sensitive** (heterotypic, coactivator-dependent) — if they dissolve on p300/CBP
  inhibition but are *insensitive* to mutating any DUX4-intrinsic aromatic/prion residues, the
  heterotypic model is supported; if they self-assemble independent of coactivators, it is wrong.
- *Fusion-agnostic:* every CIC-DUX4 junction retains this C-terminus → the condensate-partitioning
  element is junction-robust → **applies to the ~5% fusion-unconfirmed patient.**
- *Strategic value:* links an under-explored mechanism (condensates) to an **already-druggable node**
  (p300/CBP; inobrodib in solid-tumour trials) — testable *and* actionable.

## 5. What I could not establish / limitations
- **FuzDrop, PScore, catGRANULE 2.0 scores — NOT obtained on 2026-06-25 (not fabricated).** PScore
  (JFKlab, abragam.med.utoronto.ca) and catGRANULE 2.0 (tools.dieterichlab.org) servers were
  **unreachable** (connection timeouts); FuzDrop (fuzdrop.bio.unipd.it) responds but is a JS
  single-page app requiring **interactive submission** with no clean accession/REST route (its
  `/api/predict` 404s). These are the heterotypic/π-aware predictors that would most directly test
  the *refined* (heterotypic) hypothesis — they remain a genuine, named gap. Retry when the servers
  are up or submit interactively; record raw scores + URLs + access date in MANIFEST.
- **Predictors are out-of-distribution** for an artificial fusion module and trained on biased LLPS
  sets; localcider/PLAAC give composition/charge/prion context, not proof of phase separation, no
  saturation concentration. Tier ceiling: **Theoretical / Mechanistic.**
- **Whether CIC-DUX4 forms condensates *in cellulo*** — no such study exists (confirmed 2026-06
  sweep); FH-9.1 stays a forward hypothesis with a named falsifier.
- **FUS-LC boundary** kept at the field-standard 1–214 (UniProt marks disorder to 1–286); this is a
  construct-definition choice, documented in MANIFEST, and does not change the qualitative ranking.
