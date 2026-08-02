# ADR-0021: Treatment-response phenotype as evidence — the chemo-sensitivity / DDR cell-state layer

- **Status:** Accepted
- **Date:** 2026-08-02
- **Origin:** User question (2026-08-02) — the anchored patient's relapsed lung nodules resolved completely
  after 4 cycles of ifosfamide, which is atypical for canonical CIC-DUX4; asked what that implies about the
  cell's epigenetic state and which vector suits a novel immunotherapy approach.
- **Artifacts:** `simulation-output/chemosensitivity-ddr-cellstate-layer.md`,
  `sims/10-chemoresponse-cellstate/`
- **Relates to:** ADR-0008 (driver-uncertainty model — this extends it at the extension point it named),
  ADR-0001/0015 (VoI + diagnostic information-gain), ADR-0014 (transferability ladder),
  ADR-0006 (V4 expansion), ADR-0020 (`[VERIFY]` gate), ADR-0009 (findings register).

## Context

The framework's standing treatment of the fusion-unconfirmed patient (ADR-0008 / Sim 8) modelled the
**driver** as the latent variable of interest and concluded that *resolving the driver* was the
highest-value next action. Sim 8 explicitly flagged its own extension point: "if this patient already had
[testing] done, condition the prior on those results."

New information arrived that is not a molecular test but *is* evidence: a **deep, twice-repeated
chemotherapy response** (>95% necrosis at first-line resection; complete radiographic response of relapsed
lung nodules after 4 cycles of ifosfamide). The framework had **no mechanism for treating a treatment-response
phenotype as a likelihood-bearing observation** — clinical course was carried as case context, never as data
that updates beliefs.

This matters because the two leading driver hypotheses carry **opposite, molecularly named DNA-damage-response
phenotypes** (canonical CIC::DUX4 = POLE-high/repair-proficient; Ewing/EWSR1-FET = SLFN11-driven/repair-limited),
so a chemotherapy response is *diagnostic-adjacent information* the framework was discarding.

## Decision

Adopt a standing **cell-state layer** that treats **observed treatment response as evidence**, implemented as
a hierarchical latent-variable update:

```
D (driver)  ->  S (DDR / cell state)  ->  O (observed treatment response)
P(O|D) = Σ_S P(O|S) · P(S|D)
```

Three rules follow:

1. **Response phenotypes update beliefs.** A documented response or non-response to a mechanistically
   characterised agent is admissible evidence and is propagated through an explicit mechanism layer —
   never mapped driver→response directly, so that parameters stay mechanistic rather than fitted.
2. **Report the driver posterior and the cell-state posterior separately.** They can move in opposite
   directions (here: S sharpens to ~94% while entropy over D *rises*), and conflating them hides which
   question the observation actually answered.
3. **The layer conditions and re-weights; it never overrides real-data vector evidence** (ADR-0009 bias
   note) and **never prunes the forward lane** (golden rule #5). It is **not a fifth vector** (golden
   rule #8) — it re-weights V1/V3/V4.

Where a layer's mechanistic spine rests on snippet/abstract-level sources, it stays in the **forward lane**
under **ADR-0020**'s `[VERIFY]` gate and may not enter a `protocol-vN.md` until full-text-verified.

## Consequences

**What changed in the framework's standing positions:**

- "Resolve the driver first" (ADR-0008) is **qualified, not revoked**: driver-resolution remains top-EVSI
  but its purpose narrowed to re-opening the two fusion-contingent options, because the *therapeutically
  decisive* variable was already resolved by the clinical course.
- The **MCL1 "re-arm the DUX4 death program"** hypothesis is demoted on a **second, independent
  (phenotypic)** axis — intact apoptotic priming argues against a death program needing re-arming.
- The **PRC2/EZH2 node acquires a second rationale** (SLFN11 maintenance alongside MHC-I priming), unifying
  a V3 and a V4 effect at one node for a chemo-sensitive patient. Sim 2's real-data finding that EZH2 is not
  a survival dependency is **not** contradicted — neither effect is cytotoxicity.
- A **persister/reservoir distinction** enters the framework: the compartment that causes relapse is not the
  compartment chemotherapy and cell-cycle agents act on.

**Costs and risks accepted:**

- The layer's parameters (`P(S|D)`, `P(O|S)`) are mechanistic estimates, mitigated by a mandatory
  sensitivity sweep — the same discipline ADR-0008 adopted for its prior.
- Treatment response is **confounded with setting** (burden, lesion size, dose intensity). The model
  attributes all signal to cell state; some belongs to setting. This must be stated in any output using it.
- Risk of over-reading a *radiographic* response as a *biological* one. Outputs must name the distinction.

**Guardrail:** this layer produces **no diagnosis and no testing recommendation**. Its outputs are beliefs
and falsifiers.

## Alternatives considered

- **Treat the response as case context only (status quo).** Rejected: it discards the highest-information
  observation available on this tumour, and the framework already accepts decision-modelling of unknowns.
- **Map driver → response directly.** Rejected: parameters would be fitted to outcome rates with no
  external check. The mechanism layer allows the model's implied per-driver response rates (0.260 / 0.562)
  to be validated against the published rates (~0.30 / ~0.53) *without being fitted to them* — the only
  external validation the model has.
- **Make it a fifth vector.** Rejected — golden rule #8. It is a cross-cutting conditioning layer.
- **Promote the findings into `protocol-v5.md`.** Rejected for now: the mechanistic spine is
  snippet-sourced under a session-wide literature-egress block, so ADR-0020's gate applies. Promotion is a
  separate, user-gated step after full-text verification.
