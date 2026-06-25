# ADR-0020: Live evidence-refresh + verification lane (catalog updates between full runs)

- **Status:** Accepted
- **Date:** 2026-06-25
- **Origin:** Maintainer request (network-permissive re-run of `HANDOFF-network-rerun.md`); notified on issue #33 thread
- **Deciders:** Maintainer (Ammar) + Claude Code

## Context

Protocol versions v1→v2→v3 had **plateaued**: the framework kept growing by adding *analytical lenses*
(ADR-0001…0019) rather than *new biology*. The open question was whether the catalog's standing
assumption — "direct CIC-DUX4 evidence is essentially absent" — was still true, or whether 2024–2026
work had moved.

A targeted **live-literature sweep** (`evidence-refresh-2026-06.md`) was run to *inject new information*
rather than re-sort existing findings. It was first executed in a network-restricted environment, so
every accession was snippet-sourced and flagged `[VERIFY]`. A second, **network-permissive** pass
(2026-06-25) then verified each claim against live PubMed / PMC / GEO / clinicaltrials.gov and executed
the previously network-blocked **Sim 9**. This produced two things the framework had no standing process
for: (1) a set of **verified new biology** that materially updates the catalog (the p300/CBP→MHC-I node),
and (2) a **retraction** — one snippet-sourced claim (a WEE1/CCNE1/adavosertib "xenograft regression"
attributed to the *Nat Commun* 2025 MCL1 papers) was found in **neither** of the two papers on full-text
check and was withdrawn. There was no recorded decision on whether such a between-runs refresh may
update the headline catalog, or how its provenance/verification discipline should work.

## Decision

Adopt the **live evidence-refresh + verification lane** as a standing, sanctioned way to update the
catalog **between** full multi-agent runs (distinct from a §3 full cycle and from a routine question):

1. **A refresh is a dated artifact** (`evidence-refresh-YYYY-MM.md`) that injects new/updated literature,
   not a re-sort of existing findings. Every claim carries an evidence tier and a citation.
2. **Two-stage verification is mandatory before promotion.** Snippet/abstract-sourced claims are tagged
   `[VERIFY]`; **no `[VERIFY]` item may enter a protocol version until it is full-text/abstract-verified
   against a live source** (PubMed/PMC/GEO/registry per `docs/09-verification-sources.md`), with PMID/PMCID/
   accession inline and perishable trial/regulatory status **date-stamped**. Items that fail verification
   are **corrected or retracted in place** (the WEE1 retraction is the worked example).
3. **A verified refresh may produce the next protocol version** (here `protocol-v4.md`) — an *incremental,
   evidence-verified* update that **preserves all prior baselines** (CLAUDE.md §0) and states, up front,
   exactly what changed vs the prior version (including anything that got *weaker* or was retracted).
   Promotion into the headline catalog is a **user-gated** decision.
4. **The lane is symmetric — it can refute as well as confirm.** Sim 9's executed result is an
   *informative partial-negative* (the DUX4 C-term is an acidic activation domain, **not** a FET-type
   prion-like LCD), and the WEE1 claim was retracted. The lane is not a confirmation pipeline; the forward
   lane (golden rule #5) is never pruned, but the *confirmatory* lane can lose entries on verification.
5. **The register is maintained in the same change** (`findings-ranking.md`, ADR-0009): rows updated with
   verified PMIDs and date-stamps; the README "Where to start" points at the new headline version.

## Consequences

- **CLAUDE.md** §0 reuse-list + §2 routing gain the live-evidence-refresh lane as a recognised,
  non-full-cycle way to update the catalog; the `[VERIFY]`→full-text-verify discipline is reinforced as
  the gate between a refresh and a protocol version.
- **Headline catalog is now `protocol-v4.md`** (v1–v3 preserved); README + tier table updated.
- **New obligation:** a refresh's `[VERIFY]` flags are a *blocking* gate, not decoration — promotion
  requires live verification and date-stamping. This is what caught the WEE1 retraction; it is the point.
- **Honest trade-off / what it does NOT do:** a refresh is **not** a full multi-agent cycle — it does not
  re-spawn the four vector leads or re-reconcile every layer; it injects and verifies specific new
  evidence. It does not upgrade tiers on predictor scores or single-model findings (the p300/CBP→MHC-I
  node is Medium-High, **not** Established — one group/one mouse model). It is not medical advice.

## Alternatives considered

- **Fold refreshes into the next full §3 cycle only** — rejected: full cycles are slow/token-expensive
  (CLAUDE.md §0), and a tiny field's occasional new paper does not warrant re-running the whole simulation;
  it does warrant a verified, incremental catalog update.
- **Let snippet-sourced refreshes update the catalog directly** — rejected outright: the WEE1 retraction
  shows snippets conflate claims; promotion without full-text verification would have published a
  fabricated-by-conflation result, the single worst failure mode (golden rule #1).
- **Treat the refresh as a one-off, no ADR** — rejected: it changes *how the framework updates itself*
  between runs (a methodology choice per CLAUDE.md §10), so it is framework-level and recorded here.
