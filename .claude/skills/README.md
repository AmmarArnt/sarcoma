# Project-Scoped Skills

These skills are invocable by any agent operating in this repository. They exist to **reduce token usage** and **enforce simulation guardrails** without forcing every sub-agent to load the full knowledge corpus.

| Skill | Purpose | Who invokes it |
|---|---|---|
| `/sarcoma-contract` | Evidence tier vocabulary · citation rules · avoid/include lists · hard refusals | Every agent (start of task) |
| `/sarcoma-vector-context [v1\|v2\|v3\|v4]` | Returns one vector's compound list, mechanism targets, food sources, and caveats | Vector lead + that vector's sub-agents |
| `/sarcoma-pre-output-check` | 8 failure-mode checklist + 6 mandatory-include items | Every agent (before writing output) |
| `/sarcoma-chemo-interactions` | Scaffolding for screening candidates against VDC/IE chemo (does not pre-encode interactions) | Any agent recommending a dietary or supplement compound |
| `/sarcoma-output-schema [role]` | Returns the exact output schema for one role (orchestrator, v1-lead, food-specialist, …) | Every agent |
| `/sarcoma-orchestrator-intake` | Intake algorithm · deduplication rule · ranking order · conflict resolution | Orchestrator only |

## Why these exist (the token math)

The simulation runs ~15 agents (1 orchestrator + 4 leads + 10 sub-agents). Each sub-agent currently loads `00-README.md` (144 lines) and a vector slice of `05-attack-vectors.md` (often the whole 331-line file) but only needs ~70–90 lines of it. The shared behavioral rules live in `06-agent-architecture.md` (764 lines), most of which is sub-agent prompt definitions the sub-agents themselves don't need to see.

These skills surgically inject only the slice each agent needs:

- `/sarcoma-contract` replaces the ~200 lines of duplicated rule content every agent currently re-loads.
- `/sarcoma-vector-context` replaces a full 05 load (~250 unnecessary lines per sub-agent × 10 sub-agents).
- `/sarcoma-orchestrator-intake` replaces the orchestrator's full 06 load with the ~80 lines it actually uses.
- `/sarcoma-pre-output-check` and `/sarcoma-chemo-interactions` are quality skills — they catch fabrication and contraindication misses before the orchestrator has to.
- `/sarcoma-output-schema` lets each agent receive just its own schema instead of parsing all of 06.

## How agents should chain them

Typical sub-agent flow:

1. `/sarcoma-contract` (load rules)
2. `/sarcoma-vector-context v{N}` (load relevant compound context)
3. `/sarcoma-output-schema {role}` (load output schema)
4. Do the work.
5. For any dietary/supplement recommendation: `/sarcoma-chemo-interactions`.
6. `/sarcoma-pre-output-check` (self-audit).
7. Write output file.

Typical orchestrator flow:

1. `/sarcoma-contract`
2. `/sarcoma-vector-context` (no arg → cross-vector table)
3. `/sarcoma-orchestrator-intake`
4. `/sarcoma-output-schema orchestrator`
5. Synthesize.
6. `/sarcoma-pre-output-check`.
7. Write `simulation-output/protocol-v1.md`.

## Maintenance note

If `docs/05-attack-vectors.md` or `docs/06-agent-architecture.md` is updated, mirror the change into the corresponding skill. The skills are a **redundant cache** of those source-of-truth files — they trade duplication for token efficiency.
