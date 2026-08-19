# Sim 11 — Results: Can the intismeran/INT *concept* be transplanted to this sarcoma, and what vaccine would work instead?

**Run date:** 2026-08-19 · **Engine:** Monte-Carlo decision model (40,000 draws), `numpy` only, seed `20260819`
**Type:** decision model (Mechanistic/Theoretical tier) — **no external data download; no epitope prediction was executed.**
**Case anchor:** `CASE-BASELINE.md` (Era B) — chemo-responsive, Ewing-like, **driver-unresolved** round-cell sarcoma.

> **Not a diagnosis, not a treatment recommendation, not a testing recommendation, not medical advice.**
> All literature anchors are **`[VERIFY]`** (literature egress returned HTTP 403 this session) → this sim
> sits in the **forward lane** and is gated out of protocol promotion by **ADR-0020**.

---

## The question, decomposed

Intismeran autogene (mRNA-4157 / V940) is a *reference implementation*, not the concept. The concept has
four separable pillars:

| Pillar | What it is | Tumour-agnostic? |
|---|---|---|
| **P1 Antigen source** | the patient's own somatic **mutanome**, found by tumour-vs-germline WES + RNA-seq | **NO — this is a supply chain whose throughput is set by TMB** |
| **P2 Delivery + adjuvant** | mRNA-LNP, which is itself an innate adjuvant | yes |
| **P3 Polyepitope breadth** | up to ~34 neoantigens in one construct, so escape needs many simultaneous hits | yes |
| **P4 Deployment context** | adjuvant/MRD setting (low burden) + PD-1 blockade | yes |

So the sim asks: **does P1 have throughput here; if not, what can be swapped into P2–P4; and once
antigens exist, is antigen count even the binding constraint?**

---

## Result 1 — Pillar P1 fails on supply, by roughly an order of magnitude (Module A)

The funnel is `TMB → nonsynonymous mutations → clonal → expressed → ≥1 strong class-I binder → immunogenic`.

| Arm | Median mutations | Mean candidate epitopes | P(fills 34 slots) | P(≥5, design minimum) | P(≥1 immunogenic) |
|---|---|---|---|---|---|
| **This case** (marginalised over the Era-B driver posterior) | 16 | **2.04** | **0.002** | **0.127** | 0.119 |
| **Melanoma calibration arm** | 392 | 57.30 | 0.400 | 0.859 | 0.644 |

**Consistency check (the model is not fitted to this answer):** the *same* funnel, run with melanoma TMB,
gives **28× the candidate-epitope supply** and comfortably fills the construct — it reproduces the
indication where the concept was actually validated. The sarcoma failure is therefore a property of the
input distribution, not of the funnel's attrition assumptions.

Per driver hypothesis (`supply_by_driver.csv`) — the failure is worst exactly where the posterior is
heaviest:

| Driver | Posterior | Mean candidate epitopes | P(fills 34) | P(≥5) |
|---|---|---|---|---|
| D1 cryptic CIC::DUX4 | 0.264 | 2.77 | 0.003 | 0.186 |
| D2 rare CIC partner | 0.100 | 2.72 | 0.002 | 0.182 |
| D3 non-fusion CIC LOF | 0.095 | 3.07 | 0.004 | 0.206 |
| **D4 phenocopy (leading hypothesis)** | **0.386** | **1.01** | **0.000** | **0.043** |
| D5 orphan/epigenetic | 0.156 | 2.06 | 0.001 | 0.129 |

**Stress test (Module E3) — this is not a parameter artifact:**

| Stress | Mean candidates | P(fills 34) | P(≥5) |
|---|---|---|---|
| TMB ×3 | 6.09 | 0.023 | 0.370 |
| **TMB ×10** (an order of magnitude wrong) | 20.25 | **0.164** | 0.698 |
| HLA-binder rate ×2 | 3.85 | 0.008 | 0.255 |
| immunogenicity rate ×3 | 2.02 | 0.001 | 0.123 |

Even with TMB wrong by 10×, the construct fills in fewer than 1 in 6 draws.

---

## Result 2 — Seven antigen sources, and what each is actually worth (Module B)

| Class | P(available) | Mean epitopes | Escape hazard | Specificity risk | Readiness |
|---|---|---|---|---|---|
| A1 somatic mutanome | 0.13 | 1.14 | 0.70 | 0.03 | 0.80 |
| **A2 fusion junction** | **0.00 today** | 0.00 | **0.06** | 0.01 | 0.35 |
| A3 cancer-testis (PRAME, NY-ESO-1, MAGE-A4) | 0.40 | 2.00 | 0.42 | 0.06 | 0.85 |
| A4 lineage programme (STEAP1, CHM1, GPR64) | 0.43 | 1.71 | 0.15 | **0.12** | 0.60 |
| A5 non-canonical / cryptic ORFs | 0.69 | 4.80 | 0.38 | 0.07 | 0.25 |
| A6 induced/de-repressed (HERV + CTA via EZH2i/DNMTi) | 0.75 | 6.79 | 0.68 | **0.15** | 0.40 |
| A7 DUX4-as-cancer-testis-antigen | 0.29 | 0.72 | 0.07 | 0.04 | 0.20 |

**A2 is 0.00 today by construction, and that is the finding.** A junction that *exists* but has not been
*sequenced* is not a design input. Short-read testing already failed to find one here, and short-read
callers filter CIC::DUX4 on the DUX4 repeats (CASE-BASELINE §2). The junction arm is therefore gated on an
explicit resolution action (long-read WGS+RNA-seq, modelled sensitivity 0.80) — which is why it is the one
test with non-zero design value in Module E2.

---

## Result 3 — Architecture bake-off, including a no-vaccine baseline (Module D)

The baseline `V-0` is **everything the good architectures bundle around the vaccine — priming, MRD-window
timing, NK arm, PD-1 — with no antigen construct at all.** Including it is what makes the comparison honest.

| Architecture | Utility | Vaccine-arm p | Δ vs no vaccine | Top in |
|---|---|---|---|---|
| V-E in-situ, antigen-agnostic (OV / lysate-DC) | 0.2726 | 0.026 | **+0.003** | 30.6% |
| **V-0 context only — NO vaccine** | **0.2700** | 0.000 | — | 43.2% |
| V-F narrow high-specificity construct | 0.2696 | 0.027 | −0.000 | 21.2% |
| V-D hybrid broad polyepitope (+priming +window +NK +PD-1) | 0.2388 | 0.036 | −0.031 | 5.0% |
| V-D2 same antigens, no priming, no window | 0.0065 | 0.009 | −0.264 | 0% |
| V-C shared off-the-shelf polyepitope | 0.0033 | 0.004 | −0.267 | 0% |
| **V-A literal mutanome-only INT transplant** | **0.0006** | 0.001 | −0.269 | **0%** |
| V-B junction-only (junction unresolved today) | 0.0000 | 0.000 | −0.270 | 0% |

Compared **on the vaccine arm alone** (NK forced off in every architecture, `architecture_ranking_vaccine_arm_only.csv`),
the ordering of the *designs* is: **V-D 1.00× › V-F 0.88× ≈ V-E 0.88× › V-D2 0.26× › V-C 0.13× › V-A 0.02× › V-B 0.00×.**

Two separate readings, and they must not be conflated:
- **As a vaccine design**, the broad primed polyepitope is the best construct — the literal INT transplant is
  **50× worse** than it and is the worst non-null design in the set.
- **As an addition to this patient's regimen**, no antigen construct clears the no-vaccine baseline by a
  meaningful margin once specificity risk is priced. The broad construct (V-D) is **net negative**: its
  self-antigen classes (A4 at 0.12, A6 at 0.15 specificity risk) cost more than the ~0.036 they return.

---

## Result 4 — The binding constraint is not antigen count (Module E1)

Single-lever ablation of V-D (negative Δ = the lever matters):

| Ablation | Utility | Δ | % |
|---|---|---|---|
| remove NK arm | 0.0255 | −0.2133 | **−89.3%** |
| deploy outside the MRD window | 0.1148 | −0.1239 | **−51.9%** |
| halve epitope breadth | 0.2307 | −0.0081 | −3.4% |
| remove PD-1 blockade | 0.2338 | −0.0050 | −2.1% |
| remove epigenetic priming | 0.2483 | +0.0095 | +4.0% |
| drop shared antigens, keep private only | 0.2704 | +0.0316 | +13.2% |
| drop to mutanome-only antigens | 0.2708 | +0.0320 | +13.4% |

**Halving the number of epitopes costs 3.4%. Losing the window costs 52%. Losing the antigen-independent
effector costs 89%.** The concept's headline engineering achievement — 34 antigens in one construct — is
optimising the axis that matters least here. (The two positive-Δ antigen ablations are the specificity-risk
result from Result 3, not a claim that fewer antigens are immunologically better. `remove_epigenetic_priming`
is +4.0% because priming carries a modelled toxicity cost that its presentation gain does not repay when the
vaccine arm is this small — it does **not** overturn the standing EZH2i/MHC-I finding, which was never
justified on vaccine grounds.)

---

## Result 5 — Only one test changes the vaccine-design decision (Module E2)

Proper EVSI (`E_result[max_action EU] − max_action EU`, ≥0 by construction), with a wrong blind commitment
penalised by a rebuild that costs the MRD window:

| Test | Provenance | Burden | EVSI | Gates |
|---|---|---|---|---|
| **Long-read WGS + RNA-seq (junction resolution)** | P1/P2 | 3 | **+0.0035** | whether a public junction neoantigen — the lowest-escape-hazard class — can be designed at all |
| CTA panel IHC/RNA (PRAME, NY-ESO-1, MAGE-A4), archived FFPE | P1 | 1 | 0.0000 | whether the shared-antigen core exists |
| MHC-I / B2M IHC (+ HLA typing), archived FFPE | P1 | 1 | 0.0000 | whether epitopes can be seen; sets the priming requirement |
| Tumour/germline WES + RNA-seq (TMB + mutanome) | P2 | 3 | 0.0000 | whether the INT-style private arm is fillable |
| Immunopeptidomics (MS) for cryptic epitopes | P2 | 5 | 0.0000 | the dark-antigen space |

The four zeros are a **low-yield register for this decision only** (ADR-0015 sense): they are zero because
the narrow high-specificity construct wins in *both* branches of each test, so the result never changes the
design. They are **not** zero for the questions those tests were ranked on elsewhere — long-read/methylation
retain their Sim-8 driver-resolution value, and WES/TMB has its own diagnostic value. This is a
design-decision VoI, nothing more.

---

## Result 6 — Flip test: what would have to be true for the vaccine to carry the response (Module E4)

Effective epitopes the vaccine arm would need to match the NK arm's median control probability (0.293):

| Scenario | Required effective epitopes |
|---|---|
| as modelled (primed, narrow construct) | **unreachable** |
| + presentation fully restored (MHC-I = 1.0) | **unreachable** |
| + presentation restored **and** escape-proof antigens | **unreachable** |
| + all of the above **and** a mature platform (readiness 0.9) | **3.45** |

For scale: the modelled narrow construct delivers ~0.7 effective epitopes; the mutanome arm alone ~0.14.

**This is the falsifier, and it is the most useful line in the sim.** A vaccine becomes load-bearing here
only if *three things hold simultaneously* — restored MHC-I presentation, escape-resistant (tumour-restricted,
fitness-coupled) antigens, and a mature delivery platform — and then it needs only ~3.5 effective epitopes,
which is reachable. No single fix is sufficient; the conjunction is.

---

## What this sim does NOT establish

- **No epitope prediction was run.** No HLA genotype, no tumour sequence, no netMHCpan/MixMHCpred call. The
  antigen-supply numbers are a *distributional* statement about this tumour class, not about this patient's
  actual antigens. A real WES/RNA-seq would produce a specific count that could fall anywhere in these tails.
- **No real expression data for the shared-antigen classes.** A3/A4 availability (0.40/0.43) is a mechanistic
  prior, not a measurement. DepMap/GEO egress was blocked this session, so the obvious real-data upgrade —
  checking CTA and lineage-antigen expression in Ewing/CIC lines and in GSE60740 — could not be run. **This is
  the single highest-value follow-up and it is a data-availability problem, not a modelling one.**
- **Utility is a synthetic scalar.** It mixes control probability, autoimmunity risk and platform readiness.
  Absolute values are meaningless; only the ordering and the ablation deltas carry information.
- **Independence assumptions.** Antigen-class escape events are treated as independent; in reality
  antigen-presentation loss (B2M/HLA) knocks out every class-I class at once. This makes the model
  *optimistic* about polyepitope escape resistance — correcting it would widen the gap against V-D, not narrow it.
- **The NK arm is not modelled as vaccine-dependent**, which is why it dominates. That is a deliberate encoding
  of the Sim 4/5 and ADR-0021 finding (NK reconstitutes first post-chemo, covers MHC-I-loss escape), but it
  means Result 3's "no-vaccine baseline wins" is partly a statement about how strong that prior is.
- **Specificity risks are judgements.** A4 = 0.12 and A6 = 0.15 are anchored on the documented history of
  on-target/off-tumour toxicity with lineage/shared-antigen T-cell therapy `[VERIFY]`, not on measured rates.

## Reproduce

```bash
.venv/bin/python sims/11-vaccine-antigen-portfolio/run_vaccine_antigen_portfolio.py
```

Writes `supply_funnel.csv`, `supply_by_driver.csv`, `antigen_classes.csv`, `architecture_ranking.csv`,
`architecture_ranking_vaccine_arm_only.csv`, `lever_ablation.csv`, `design_value_of_information.csv`,
`supply_sensitivity.csv`, `flip_test.csv`. Deterministic under seed `20260819`.
