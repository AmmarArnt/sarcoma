# Sim 9 — RESULTS: Condensate / LLPS propensity of the CIC-DUX4 transactivation module (Track B)

**Run date:** 2026-06-22 · **Status:** toolchain validated; **biological run network-blocked** (see below).
**Research simulation / hypothesis generation only. Not medical advice.**

---

## 0. One-paragraph honest summary

This sim asks whether the **DUX4 C-terminal acidic transactivation domain** — the
module CIC retains in the CIC-DUX4 fusion — is predicted to drive **biomolecular
condensates** the way the EWSR1 and FUS prion-like low-complexity domains (LCDs) do.
The pipeline (real tools: `localcider` for Das-Pappu/Uversky charge-patterning
descriptors + canonical CRC64 sequence-integrity verification; optional `metapredict`
for disorder) **ran and self-validated**, but this environment's network-egress
allowlist blocked every UniProt fetch (HTTP 403), so it **aborted rather than invent
sequences** (golden rule #1). The script is committed and runs to completion wherever
`rest.uniprot.org` is reachable. The scientific contribution delivered here is
therefore (a) a runnable, integrity-checked pipeline, and (b) a **literature-grounded
condensate forward-hypothesis, newly sharpened by the 2026-06 evidence refresh** —
not fabricated descriptor numbers.

## 1. What executed, what did not

| Step | Status |
|---|---|
| `localcider` import + self-test (`FCR=0.840, κ=0.626`) | ✅ passed |
| CRC64 integrity gate wired (`Bio.SeqUtils.CheckSum.crc64`) | ✅ in place |
| Fetch UniProt Q9UBX2 / Q01844 / P35637 / Q96RK0 | ❌ **HTTP 403 — egress allowlist** |
| Descriptor computation on the four sequences | ⏸ pending a network-enabled run |
| `metapredict` empirical IDR boundaries | ⏸ not installed (optional; pulls torch) |
| OpenMed NER grounding | ⏸ HuggingFace also egress-blocked here |

Recorded failures: `RESULTS_partial.json`. This is the convention-mandated "report the
failure, don't fake the data" outcome (CLAUDE.md §4).

## 2. The biology this is testing (why the DUX4 C-term is the right substrate)

- CIC-DUX4 = repressor CIC (incl. its **HMG-box** DNA-binding domain) fused to the
  **DUX4 C-terminal transactivation domain**; the fusion converts CIC from repressor
  to strong activator. *(Established — multiple sources, confirmed in 2026-06 refresh.)*
- That C-terminal domain works by **recruiting the histone acetyltransferases
  p300/CBP** to CIC target sites → H3 acetylation → target activation; p300/CBP is
  *required* for CIC-DUX4 activity and even stabilises the fusion protein.
  *(Preclinical-Cell/Animal; Okimoto/Bosnakovski lines of work — see evidence-refresh
  artifact for citations.)*
- **p300/CBP and histone-acetylation are established nucleators of transcriptional
  condensates** (acetyl-reader/BRD4 + coactivator phase behaviour). So a domain whose
  whole job is to *recruit p300/CBP and build an acetylated activating hub* is a
  mechanistically reasonable condensate-seeding element — yet **no DUX4 or CIC-DUX4
  LLPS study exists** (2026-06 literature sweep found none; the field's condensate work
  is on EWSR1/FET fusions). That gap is the opportunity.

## 3. What a successful run would (and would NOT) tell you

**Would:** a *relative ranking* — e.g. "the DUX4 C-term IDR sits in the Das-Pappu
strong-polyampholyte / acidic-IDR region with charge-patterning comparable to the
EWSR1 EAD and FUS LCD" vs "it looks more like a folded domain (clusters with the CIC
HMG-box control)." Invariance of that read across the (junction-retained) DUX4 C-term
is the point — it is **fusion-agnostic** and so **applies to the ~5% fusion-unconfirmed
patient**, because every CIC-DUX4 junction keeps the DUX4 C-terminus.

**Would NOT:** prove a condensate forms in a cell; give a saturation concentration;
substitute for FuzDrop/PScore/catGRANULE (unreachable here); or overcome the fact that
these predictors are trained on a small, biased LLPS set (out-of-distribution risk is
high for an artificial fusion module). Tier ceiling for any output: **Theoretical /
Mechanistic.**

## 4. Forward Hypothesis (the deliverable)

**[FH-9.1] CIC-DUX4 organises a p300/CBP-dependent, acetylation-driven transcriptional
condensate nucleated by the DUX4 C-terminal acidic transactivation IDR, and this
property is invariant across fusion-junction variants.**
- *Mechanistic basis:* the DUX4 C-term recruits p300/CBP (required for fusion activity
  and stability); acetyl-coactivator hubs phase-separate; the DUX4 C-term is acidic and
  predicted-disordered. Because every CIC-DUX4 junction retains this C-terminus, the
  condensate-seeding element is junction-robust → a target that does **not** need the
  patient's exact junction.
- *In-silico test (this sim, network-enabled):* score the DUX4 C-term IDR with
  localcider + metapredict (and, ideally, FuzDrop/PScore/catGRANULE) head-to-head
  against the EWSR1 EAD and FUS LCD positive controls and the CIC HMG-box negative
  control; invariance + EWSR1/FUS-comparable charge-patterning supports the hypothesis.
- *Wet-lab falsifier (names the disconfirming experiment, per golden rule #5):*
  1,6-hexanediol sensitivity / optoDroplet / live-imaging of CIC-DUX4 puncta; and a
  **p300/CBP-inhibitor (A-485, inobrodib) condensate-dissolution test** — if CIC-DUX4
  transcriptional hubs are *not* hexanediol-sensitive and do *not* dissolve on p300/CBP
  inhibition, the condensate model is wrong even though p300/CBP is still a target.
- *Why this matters strategically:* it links a **novel, under-explored mechanism**
  (condensates) to an **already-druggable node** (p300/CBP; inobrodib is in solid-tumour
  trials) — i.e. the hypothesis is testable *and* actionable, not just speculative.

## 5. What I could not establish
- Any descriptor value for DUX4/EWSR1/FUS/CIC here — UniProt was egress-blocked; not
  fabricated.
- FuzDrop/PScore/catGRANULE scores — web servers unreachable.
- Whether CIC-DUX4 forms condensates *in cellulo* — no such study exists (confirmed by
  the 2026-06 sweep); this remains a Theoretical forward hypothesis with a named falsifier.
