# ADR-0014: Evidence-transferability hierarchy (biological-proximity ladder) — refines the confidence axis (ADR-0004)

- **Status:** Accepted
- **Date:** 2026-06-13
- **Origin:** Issue #10 follow-up comment (@Cerimagic, 2026-06-12) / PR (this change)
- **Deciders:** Maintainer (AmmarArnt), Claude Code session

## Context

Issue #10 (host-biology modifier layer, ADR-0005) was answered, then the author raised a
**methodological concern** in a follow-up: keeping CIC-DUX4-specific evidence at the top is correct,
but narrowing the search space *aggressively* risks **artificially excluding** mechanistically conserved
host-biology / immune-context evidence — pathways (exercise, systemic inflammation, autonomic
signalling, perioperative biology, NK fitness, COX-2, sleep/circadian, nutrition) that are not
inherently CIC-DUX4-specific but conserved across sarcomas and solid tumours. With the patient's fusion
status unresolved and CIC-specific datasets extremely limited, the author proposed an **explicit
hierarchy rather than a hard restriction**: (1) CIC-rearranged/CIC-DUX4 → (2) fusion-driven round-cell
sarcomas → (3) sarcomas generally → (4) solid tumours with strong mechanistic transferability, with
broader evidence *admitted at lower confidence* rather than discarded.

The gap was real but narrow: the framework's **Directness (D)** sub-axis of the confidence score
(`docs/08` §3) had only three coarse levels (`+` CIC-DUX4/close fusion / `0` generic cancer / `−`
pathway-inferred). That collapsed middle lumped "another fusion-driven round-cell sarcoma (Ewing)" with
"a generic carcinoma" — exactly the over-narrowing the comment warned against, in the opposite
direction (loss of resolution, not loss of breadth). Golden rules #5 (known research is the floor) and
#6 (distinguish CIC-DUX4 evidence from cancer-broadly) already *intend* admission-with-downgrade; what
was missing was a **graded, auditable** version of the down-weighting.

## Decision

Adopt the proposed hierarchy as a **refinement of the existing Directness sub-axis — not a new axis and
not a new score.** Recorded in **`docs/10-evidence-transferability-hierarchy.md`**:

- Replace the 3-level D with a **graded proximity ladder**: **P0** index disease (CIC-DUX4) → **P1**
  same molecular family (WHO undifferentiated round-cell sarcomas: Ewing / BCOR / DSRCT / EWSR1-non-ETS)
  → **P2** sarcoma broadly → **P3** solid tumour *with an explicitly named conserved mechanism* → **P4**
  pathway-inferred only → **floor** (no mechanistic bridge → not admitted as evidence; may route to the
  Weak-Signal Register).
- **Operating rule:** rarity is *never* grounds for exclusion. Disease-distance moves a candidate **down
  the ladder (lower confidence), never out of the search space.** The only bright line is **mechanistic,
  not taxonomic**: a candidate is excluded from the evidence tracks only when no conserved, *named*
  mechanistic bridge exists.
- **Two-lane guarantee:** the proximity discount feeds the **confidence label / confirmatory-lane
  ordering only**; it **never prunes the Forward-Hypotheses lane** (`docs/08` §4). Disease-distant
  conserved-mechanism ideas stay alive as forward hypotheses — the outcome the comment asked for.
- **Fusion-uncertainty coupling (ADR-0008):** when the driver is a latent variable, P0 is discounted by
  the cryptic-fusion posterior and **P1 is the robust anchor** — so the *effective* P0→P1 gap narrows,
  making broader fusion-family evidence relatively more valuable, not less.
- **Scorer step added:** name the *mechanism being transferred* before assigning a rung, and record the
  rung explicitly (e.g. `D = P2 (sarcoma; mGPS prognostic)`). Proximity is scored on the mechanism, not
  the disease label of the source paper (worked: EZH2i→MHC-I sits high because the *mechanism* is the
  candidate).

## Consequences

- **CLAUDE.md updated:** §2 routing table gets a row for "is broader/host evidence being excluded on
  rarity grounds / how is transfer distance weighted" → reuse the transferability ladder; the docs map
  (§7) gains `docs/10`.
- **`docs/08` §3** gets an additive cross-reference: the D sub-axis now points to `docs/10` for the
  graded ladder. **`sarcoma-contract`** axis-2 row points to `docs/10`. **`host-biology-modifier-layer.md`
  §5** gets a one-line pointer (it is the layer the comment was raised against).
- **Future sessions:** "is this being excluded just because CIC-DUX4 is rare?" now has a principled
  answer — assign a proximity rung and attenuate confidence; only the mechanistic-bridge floor excludes.
- **Explicitly does NOT:** invent a new axis or numeric weight; re-score `protocol-v1.md` (a
  `protocol-v2.md` regeneration is deferred, same staging as `docs/08` §7); change the evidence-tier
  vocabulary; or create CIC-DUX4-specific evidence where none exists. A proposed `sarcoma-pre-output-check`
  failure mode ("P3 admitted without a named conserved mechanism") is **deferred to maintainer sign-off**,
  not applied in this change.
- **Trade-off:** the rungs are ordinal, not metric; discount magnitudes are deliberately bands, and P3's
  integrity depends on the "name the bridge" discipline being enforced.

## Alternatives considered

- **Leave the 3-level D as is.** Rejected — it is the over-narrowing the comment correctly flagged; it
  hides the Ewing-vs-carcinoma gradient.
- **Make transferability a fourth standalone scoring axis.** Rejected — it *is* the Directness question
  the confidence axis already asks; a separate axis would duplicate it and invite double-counting. A
  refinement of the existing sub-axis is the minimal, non-redundant change.
- **Hard taxonomic restriction (CIC-only, then sarcoma-only).** Rejected — this is exactly the
  artificial exclusion the comment warns against and the two-lane rule forbids.
- **Numeric transfer-distance weights (e.g. ×1.0 / ×0.7 / ×0.4).** Rejected — false precision; the
  framework's standing choice (`docs/08` §3) is auditable bands over magic numbers.
