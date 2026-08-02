# ADR-0022: Case-baseline refresh — Era B (chemo-responsive, Ewing-like, driver-unresolved)

- **Status:** Accepted
- **Date:** 2026-08-02
- **Origin:** Maintainer instruction (2026-08-02) — "set this as the baseline now… all follow-up agents,
  humans and research goes against this refreshed snapshot of findings, rather than reusing the old
  findings. However, for the sake of previous files like ADRs, sims and protocols, take note that research
  to a certain date has been done against one set of data, and that this one and from now on another set
  of knowledge is used."
- **Artifacts:** `CASE-BASELINE.md` (new, root, Tier 1)
- **Relates to:** ADR-0021 (the evidence that motivated it), ADR-0008 (driver-uncertainty),
  ADR-0014 (transferability ladder — materially affected), ADR-0020 (`[VERIFY]` gate), ADR-0009.

## Context

The repository was framed throughout as a simulation about **"CIC-rearranged sarcoma (CIC-DUX4 fusion)"** —
in `README.md`, `docs/00-README.md`, `CLAUDE.md`, `.prompts/run-sim.prompt`, and every protocol version.
The fusion-unconfirmed status of the actual case was handled as an **edge case**: golden rule #9 required
per-entry flagging of fusion-dependent recommendations, but the *default* framing still assumed canonical
CIC-DUX4 biology.

Two things made that framing wrong rather than merely imprecise:

1. **The fusion was never confirmed.** A negative CIC break-apart FISH / short-read panel is weak evidence
   of absence (14–46% false-negative rate; DUX4-repeat mappability), but it is also not confirmation. The
   case has always been driver-unresolved; the framing did not reflect that.
2. **The tumour responded deeply to chemotherapy — twice.** Canonical CIC-DUX4 is repair-proficient
   (POLE-high) with ~30% good response. ADR-0021 / Sim 10 showed this observation moves the driver
   posterior from D1-led (0.450) to D4-led (0.386 vs 0.264) and resolves the DDR cell state to ~94%.

Continuing to default to CIC-DUX4 biology would systematically mis-weight new work: it would over-credit
CIC-DUX4-specific evidence, under-credit Ewing/round-cell-family evidence, and keep importing the
"chemo-resistant" background assumption that this patient's course directly contradicts.

## Decision

**Establish `CASE-BASELINE.md` as the canonical case description, and route all new work through it.**

1. **New work reads the baseline first.** Every agent, contributor, and research task works against
   `CASE-BASELINE.md`, not against the case framing embedded in Era-A artifacts.
2. **Declare two epistemic eras**, so the historical record stays legible:
   - **Era A (2026-06-02 → 2026-08-01)** — canonical CIC-DUX4 working assumption. `protocol-v1..v4`,
     `sims/01–09`, `ADR-0001..0020`, all vector outputs, all analytical layers, `docs/00–11`.
   - **Era B (2026-08-02 → )** — chemo-responsive, Ewing-like, driver-unresolved. `CASE-BASELINE.md`,
     `ADR-0021`, this ADR, `sims/10-chemoresponse-cellstate/`, the chemo-sensitivity/DDR layer.
3. **Era-A artifacts are preserved, never retro-edited.** ADRs are append-only by policy and protocol
   versions are retained baselines by policy (CLAUDE.md §0). They are historical records of what was
   concluded under which assumption. A **short pointer banner** is added to the *live navigational*
   documents only (README, `docs/00-README.md`, `protocol-v4.md`, `findings-ranking.md`,
   `.prompts/run-sim.prompt`); the rest of the tree is left alone and read through
   `CASE-BASELINE.md` §5.
4. **Directness becomes posterior-weighted (amends ADR-0014 in application, not in structure).** This case
   has **no P0 anchor**: neither CIC-DUX4-specific nor Ewing-specific evidence is "in this tumour." The
   Directness sub-axis is weighted across the driver posterior instead of assuming P0 = CIC-DUX4.
   The ladder itself (P0–P4) is unchanged; what changed is which rung this case sits on.

## Consequences

**Operational:**
- CIC-DUX4-direct evidence is **discounted (~0.36 posterior mass), not excluded** — it remains the best
  mechanistic anchor *if* the driver is CIC-class.
- Ewing / fusion-round-cell-family evidence is **up-weighted** and is arguably now the closest available
  anchor. Side effect: the Ewing-proxy substitutions the sims already made out of necessity (Sim 2's
  DepMap lines) are **less of a compromise under Era B than under Era A**.
- Fusion-agnostic evidence (host biology, immune/NK, cell-cycle, danger-signalling, modality, feasibility)
  is **unchanged at full weight** — it was never driver-dependent, and is now the most robust part of the
  catalog.
- Golden rule #9's atypical-case flag moves from a **footnote to the centre** of the framing.

**Explicitly NOT decided:**
- **This is not a re-diagnosis.** "Not CIC-DUX4" is *not* the baseline; "driver unresolved, CIC-DUX4 less
  likely than before" is. Cryptic CIC-DUX4 retains ~26% posterior. The baseline carries an explicit
  guardrail against hardening into "it's Ewing sarcoma," since "Ewing-like" is a morphological descriptor
  covering several entities and no EWSR1 fusion has been reported either.
- **No `protocol-v5`.** The Era-B evidence spine is snippet/abstract-level under a session-wide literature
  egress block (HTTP 403 across PubMed/PMC/nature.com/EuropePMC/Crossref), so ADR-0020's `[VERIFY]` gate
  keeps Era B in the **forward lane**. Promotion to a protocol version is a separate, user-gated step after
  full-text verification. Note this constrains the *mechanistic interpretation* only — the **case facts**
  come from the patient record, not the literature, and are unaffected.
- **No vector changes.** The four attack vectors remain fixed (golden rule #8); no layer is retired.

**Risks accepted:**
- A baseline stated this confidently can itself become an anchor. Mitigated by `CASE-BASELINE.md` §8
  ("what would change this baseline again"), which names the specific results that revert or harden it —
  in particular, a canonical junction on long-read WGS would largely revert Era B.

## Alternatives considered

- **Retro-edit the old artifacts to the new framing.** Rejected: it destroys the honest historical record,
  violates the append-only ADR policy and the preserved-baseline protocol policy, and would silently
  rewrite conclusions whose *reasoning* was valid under what was known at the time.
- **Leave the framing alone and rely on golden rule #9's per-entry flagging.** Rejected: that is exactly
  what produced the mis-weighting. The default framing is what agents actually absorb.
- **Declare the case "Ewing-like sarcoma" outright.** Rejected as overclaiming — it is a morphological
  descriptor, not a molecular diagnosis, and the driver posterior is a 0.39/0.26 lean, not a finding.
- **Fold the baseline into `protocol-v5`.** Rejected: blocked by ADR-0020's verification gate, and a case
  *definition* is a different kind of object from a *hypothesis catalog* — it should not be versioned on
  the catalog's cadence.
