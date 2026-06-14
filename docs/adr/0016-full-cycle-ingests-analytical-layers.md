# ADR-0016: Full-cycle re-runs ingest the standing analytical layers

- **Status:** Accepted
- **Date:** 2026-06-14
- **Origin:** Maintainer request (planning a fresh full re-run that inherits the issue-driven layers)
- **Deciders:** maintainer

## Context

Issues #7–#11 and #31 each added a **standing analytical layer or refinement** on top of the original
multi-agent run — biomarker VoI + provenance (ADR-0001/0011), translational feasibility + attrition
(ADR-0003/0013), host-biology modifiers (ADR-0005), the V4 immune-watchdog expansion (ADR-0006), the
tumorigenesis/driver-uncertainty model (ADR-0007/0008), the evidence-transferability ladder (ADR-0014),
and the diagnostic information-gain layer (ADR-0015). Together they are the accumulated value of the issue
thread.

But these layers were wired for **main-thread reuse only** — discoverable via `CLAUDE.md §0/§2` routing and
the `findings-ranking.md` register. **None of them were referenced by the wave agents or the orchestrator**
(`docs/06-agent-architecture.md` and `.claude/agents/*.md` named only the per-vector output files). A fresh
full cycle would therefore have regenerated `protocol-v*.md` **without** any of the layers — silently
discarding the incremental insight. The maintainer is planning such a re-run and wants it to be *strictly
more informed* than the previous one.

## Decision

Make **ingestion of the standing analytical layers a required step of every full cycle**, at both the
vector and the synthesis stage (the "orchestrator + vector leads" scope).

1. **Execution order (`CLAUDE.md §3`)** gains a standing **Layer Intake** obligation: before Wave 1 each
   agent consults the layers relevant to its scope (via `§0`/`§2`); the orchestrator reconciles the catalog
   against **all** layers + `findings-ranking.md`.
2. **Orchestrator** (`.claude/agents/orchestrator.md` + `sarcoma-orchestrator-intake` skill): a new intake
   step **"1B — Ingest standing analytical layers"** lists each layer, what it contributes, and the
   reconciliation rule; RANK applies the feasibility/attrition/transferability annotations; CURATE FORWARD
   HYPOTHESES draws on the layers' forward hypotheses + the diagnostic "what to learn next" + the
   driver-uncertainty contingency.
3. **Vector leads** consume the layer(s) that specifically condition them: **V4** ← host-biology (0005),
   immune-watchdog expansion (0006), VoI immune ranking (Sim 6) + diagnostic-IG immune markers (0015);
   **V3** ← driver-uncertainty contingency (0008, hold MCL1/junction-specific lines until the driver is
   resolved) + tumorigenesis build-recipe forward hypotheses (0007); **V1/V2** ← feasibility/attrition +
   transferability annotations (light; transferability already enters via `sarcoma-contract`), and
   host-biology only for tolerability/SOC-context entries.
4. **Output schema** (`docs/06` + `sarcoma-output-schema` skill) gains two standing sections — **Host-Biology
   & Treatment-Response Modifiers** and **Missing-Data, Value-of-Information & Diagnostic Strategy (What to
   Learn Next)** — and an instruction to annotate Clinical/Experimental entries with F-band + R-reason +
   Directness rung, so the layers are *visible* in the regenerated catalog rather than only consulted.

**The load-bearing guardrail (unchanged golden rules):** layers **condition and annotate** the catalog;
they **never override real-data vector evidence** (the ADR-0009 bias note — do not promote a
logic/decision-model finding above a real-data one) and **never prune the Forward-Hypotheses lane**
(golden rule #5 / two-lane rule). The four attack vectors stay fixed (golden rule #8) — layers are
cross-cutting, **not a fifth vector**.

## Consequences

- A fresh full cycle now produces a catalog that inherits every issue-driven layer; recommend writing it to
  the **next protocol version** (e.g. `protocol-v2.md`/`-vN.md`), **not** overwriting the prior baseline
  (`CLAUDE.md §0`).
- Files changed: `CLAUDE.md` (§3), `docs/06-agent-architecture.md` (orchestrator intake + schema),
  `.claude/agents/{orchestrator,v1,v2,v3,v4}-lead.md`, `.claude/skills/sarcoma-orchestrator-intake/SKILL.md`,
  `.claude/skills/sarcoma-output-schema/SKILL.md`, `docs/adr/README.md` (index).
- **Token cost / smaller-model load:** vector leads run on `sonnet`; layer intake adds context. Mitigated by
  pointing each lead only at the layer(s) in its scope (not all of them) and keeping V1/V2 light (their
  prompts warn against over-stuffed context).
- **Does NOT:** change the four vectors, add a fifth, alter any layer's content, re-run anything now, or make
  layers outrank real data. It is a wiring/orchestration change only. Perishable feasibility/trial facts
  still must be **re-verified live** at run time (golden rule #1).

## Alternatives considered

- **Orchestrator-only ingestion.** Lighter, but the vectors would not self-condition (e.g. V3 could still
  surface the MCL1/junction line that the driver-uncertainty model says to hold for a fusion-unconfirmed
  case). Rejected in favour of full propagation, per the maintainer's "more robust / more insights" goal.
- **Leave as-is (main-thread reuse only).** Rejected: it silently drops the issue-driven layers on any
  re-run — the exact failure this ADR prevents.
- **Fold layers into the four vectors.** Rejected: violates golden rule #8 (vectors are fixed; layers are
  cross-cutting).
