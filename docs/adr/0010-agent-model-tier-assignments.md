# ADR-0010: Agent model-tier assignments (Orchestrator → Fable)

- **Status:** Accepted
- **Date:** 2026-06-10
- **Origin:** Maintainer request (agent/sub-agent model review)
- **Deciders:** Maintainer + Claude Code

## Context

The committed agents in `.claude/agents/` carried model-tier assignments chosen before **Fable 5**
existed: the Orchestrator on `opus`, every Vector Lead and the mRNA Vaccine Research Team Lead on
`sonnet`, and the fan-out sub-agents inheriting Sonnet-tier by convention. `docs/06-agent-architecture.md`
specified the Orchestrator should run on "the highest-tier model available."

Fable 5 is now the most capable model — a tier above Opus 4.8 — at roughly 2× Opus's per-token price
($10/$50 vs $5/$25 per MTok). That changes what "highest-tier available" resolves to, and prompted a
review of whether any agent would benefit from Fable instead of its current model, and whether the
tiering as a whole is still appropriate.

## Decision

Assign model tiers by **synthesis depth × error blast-radius**, discounted by **parallel fan-out**:

- **Orchestrator → `fable`** (was `opus`). It is the single capstone synthesis pass — it dedupes and
  ranks across all four vectors plus the mRNA team, resolves cross-team conflicts, ranks by evidence tier
  *and* biological plausibility, surfaces cross-vector synergies, flags chemo contraindications, and is
  the citation backstop for the headline deliverable (`protocol-v1.md`). It runs **once per cycle** with
  no fan-out, so the higher Fable cost is bounded, and a fabrication or mis-ranking here is the most
  consequential failure in the whole run. This is the "correctness matters more than cost" case. Opus
  remains an acceptable fallback if Fable is unavailable.
- **Vector Leads, mRNA Lead, sub-agents, Metastatic Disease Specialist → `sonnet`** (unchanged). These
  are coordinators and focused researchers that run **in parallel** (up to three leads per wave, 3–4
  sub-agents under each lead). Reconciliation and single-domain research sit well within Sonnet 4.6's
  range, and the Orchestrator re-checks their output. Promoting them to a higher tier would inflate cost
  across the widest fan-out point of the pipeline without a correctness justification.

`docs/06-agent-architecture.md` § *Recommended Models* was rewritten to match the committed frontmatter
and to record this principle.

## Consequences

- `.claude/agents/orchestrator.md` frontmatter is now `model: fable`; all other lead frontmatter is
  unchanged (`model: sonnet`).
- `docs/06-agent-architecture.md` § *Recommended Models* now names Fable as the Orchestrator tier, states
  the synthesis-depth × blast-radius × fan-out principle, and warns against blanket-promoting the leads
  or sub-agents to Fable.
- A fresh full run (`§3` of `CLAUDE.md`) now spends more on the single Orchestrator pass and the same as
  before on every other agent. Net cost impact is small because the Orchestrator is one serial call, not
  a fan-out.
- This does **not** change any golden rule, the scoring axes, the wave structure, or any agent's prompt
  content — only which model executes the Orchestrator. The no-fabrication and "say what you could not
  establish" guardrails are unchanged and remain the substantive backstop regardless of tier.

## Alternatives considered

- **Promote the Vector Leads to Opus/Fable too.** Rejected: they run in parallel fan-out where Sonnet is
  the right speed/intelligence/cost balance, and the Orchestrator already re-checks their work. A
  three-tier ladder (Sonnet leads → Opus orchestrator → Fable) was considered and set aside as
  over-engineering for no measured quality gain.
- **Leave the Orchestrator on Opus.** Rejected: the architecture doc already calls for the
  highest-tier model, and the Orchestrator's role is the textbook case for maximum capability — single
  serial pass, highest stakes, correctness-critical, cost bounded.
- **Pin sub-agents to an explicit model in the lead prompts.** Deferred: sub-agents are dispatched via
  `subagent_type: general-purpose` and inherit Sonnet-tier by convention; pinning them in-prompt adds
  maintenance surface without changing behavior. Revisit only if inheritance stops resolving to a
  Sonnet-class model.
