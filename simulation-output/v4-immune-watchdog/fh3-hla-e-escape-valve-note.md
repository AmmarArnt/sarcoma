# V4 Forward Note — FH-3 (HLA-E/NKG2A escape valve) tested in-silico

**Status:** extends `v4-summary-v2.md` Forward Hypothesis 3 and `protocol-v2.md` FH-3 / Open Question #1.
**Source of result:** `sims/07-hlae-escape-valve/` (extends Sim 04). **Not medical advice.**

## What was asked
Open Question #1 of `protocol-v2.md` resolved the NK-vs-MHC-I sequencing *directionally*
(NK-first → MHC-I restoration with anti-NKG2A → checkpoint) but flagged it **"unresolved
quantitatively."** FH-3 is the crux: does epigenetic MHC-I restoration **co-induce HLA-E**, and if so
is **anti-NKG2A (monalizumab) load-bearing or optional**?

## What the sim shows (qualitative Boolean; direction, not effect size)
1. **Parity gate passed** — the model reproduces Sim 04 exactly when HLA-E coupling is off, so the
   findings below are attributable to the coupling alone.
2. **Under the FH-3 premise, anti-NKG2A is load-bearing, not optional.** Coupling collapses the
   clearance space from 176→100 routes; **88% of survivors require anti-NKG2A.** The EpiPrime+anti-PD-1
   package that worked without HLA-E now **self-blocks** (restoring MHC-I supplies HLA-E's own VL9
   stabilizing peptide) until anti-NKG2A is added.
3. **The 12 anti-NKG2A-free escape routes are exactly the "stay-cold" NK routes** — they never restore
   MHC-I and never induce IFN. Corollary: **even CDK4/6i added to an NK-first route is self-defeating**
   under coupling (its IFN induction raises HLA-E). "NK-first" must be restated as **"NK-first *before
   any IFN-inducing / MHC-I-restoring step*."**
4. **B2M-loss control:** with no classical MHC-I there is no VL9 → HLA-E cannot surface → 0 active
   brakes → anti-NKG2A irrelevant. The escape valve is a liability **specific to the MHC-I-restoration
   path**, confirming the mechanism behaves correctly.

## Catalog edits this justifies (proposed, for orchestrator)
- **Cross-Vector Synergy (V3→V4):** change the headline epigenetic-priming package from
  "EZH2-pathway-i + BETi + anti-PD-1" to **"EZH2-pathway-i + anti-NKG2A (monalizumab) ± anti-PD-1"** —
  anti-NKG2A is now first-class, not a footnote, on the restoration arm.
- **Open Question #1:** mark the *direction* confirmed and add the quantitative dependency structure
  (anti-NKG2A load-bearing for restoration; NK-first valid only while IFN-cold).
- **C8 (monalizumab)** in `v4-summary-v2.md`: promote from "pairs with MHC-I restoration" (Low) to a
  **gated-but-pivotal** partner of the restoration arm, contingent on the falsifier below.

## Honest caveat (do not overstate)
The decisive edge — **EZH2i actually co-inducing HLA-E in CIC-DUX4** — is **inferred, not measured**
(from HLA-E's leader-peptide dependence + IFN-inducibility). The sim makes the *consequence* of that
premise explicit and falsifiable; it does **not** establish the premise. Everything is D=− (no direct
CIC-DUX4 data), consistent with the rest of V4.

## Falsifier (pre-registered; also the highest-VoI measurement)
CIC-DUX4 lines ± EZH2i/HDACi, assay **surface HLA-A/B/C and HLA-E**:
- **Supports FH-3** if MHC-I↑ co-occurs with HLA-E↑ **and** anti-NKG2A increases NK/CTL killing.
- **Falsifies FH-3** if MHC-I↑ without HLA-E↑, or anti-NKG2A adds no killing → anti-PD-1 pairing
  suffices and monalizumab is not load-bearing.

This single assay (HLA-E surface response to epigenetic therapy) is the gating biomarker — recommend
adding it to the VoI layer (`biomarker-voi-stratification.md`) alongside the existing HLA-E entry.
