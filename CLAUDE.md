# CLAUDE.md — Operating Guide for Claude Code Sessions

This repository is a **multi-agent research simulation** for CIC-rearranged sarcoma (CIC-DUX4 fusion),
framed through a software/systems-engineering analogy. The deliverable is a **ranked, evidence-tiered
hypothesis catalog plus forward (not-yet-tested) hypotheses and runnable in-silico experiments** — never
a treatment plan. Read `docs/00-README.md` for full framing before substantial work.

**This is research and hypothesis generation only. No medical advice, no personal dosing, no
start/stop instructions for any therapy.** Mechanisms, food sources, evidence tiers, and published
trial dose-ranges (with citations) are in scope; prescriptive numbers are not.

---

## 1. Golden rules (non-negotiable — apply to every output, every agent)

From `docs/00-README.md`, `docs/06-agent-architecture.md`, and the `sarcoma-contract` skill.

1. **No fabricated citations. Ever.** If you can't point to a real PMID / NCT / DOI / dataset, write
   `[no direct citation; mechanism inferred from {what}]`. Plausible-looking fake references are the
   single worst failure mode. **Verify accessions/PMIDs against live sources when you can** (WebSearch/
   WebFetch); if you can't verify, label it `[VERIFY]` rather than asserting it.
2. **Evidence tier on every claim.** Use exactly one: `Established` › `Clinical-Trial` ›
   `Preclinical-Animal` › `Preclinical-Cell` › `Mechanistic` › `Dietary-Observational` › `Theoretical`.
3. **Mechanism before recommendation.** State the molecular mechanism, not an analogy and not
   "antioxidant properties." The engineering analogy (docs/04) is shorthand — always translate it back
   to biology.
4. **Cite with calibrated confidence; say what you could not establish.** A short, honest output beats
   a long padded one. Every research output needs a "what I could not establish" section.
5. **Known research is the FLOOR, not the ceiling.** Do not stop at "X was tried and didn't work."
   Ask *why* it failed, what's mechanistically different here, what could be tried differently, whether
   the molecule behaved as envisioned, whether the trial was underpowered/unselected/monotherapy.
   Generate mechanistically defensible **Forward Hypotheses** with explicit falsifiers. Be bold in
   *hypothesis* space (tag it `Theoretical`/`Mechanistic`) — but **never** dress speculation up as
   evidence.
6. **Distinguish "evidence in CIC-DUX4" from "evidence in cancer broadly."** Flag concentration
   mismatches (a 10 µM cell-line effect ≠ achievable dietary plasma level).
7. **Flag standard-of-care interactions** (VDC/IE: vincristine, doxorubicin, cyclophosphamide,
   ifosfamide, etoposide; CYP3A4/P-gp; ROS-dependent chemo). Use the `sarcoma-chemo-interactions` skill.
8. **The four attack vectors are FIXED** (V1 Rate-Limiting, V2 Compiler-Protection, V3 Hot-Patching,
   V4 Immune-Watchdog). New topics are **supplementary teams or sub-agents**, never a "fifth vector."
9. **Atypical-case flag (~5%).** Some clinically/histologically CIC-rearranged tumors have no confirmed
   fusion. Flag any fusion-dependent recommendation (junction ASOs, junction-specific vaccines/CAR-T)
   as possibly inapplicable; mark fusion-agnostic ones (EZH2i, BETi, CDK4/6i, differentiation, epigenetic
   MHC-I priming, dietary, immune) as still applicable.
10. **Clinician-facing briefs must carry honest clinical status** (what's approved vs experimental vs
    failed in trials) and a "revisit when…" trigger. Tag everything "not medical advice."

---

## 2. Gauge the effort before acting (use judgement)

| If the prompt is… | Then… |
|---|---|
| A simple factual / clarifying / "why" question | **Just answer.** No spawning, no repo-wide research. |
| "Analyze X thoroughly," "from multiple angles," "what could be tried," "run a simulation" | **Spawn the appropriate team** (below) so the topic gets multiple perspectives. |
| A research question with no fitting existing team | **Propose a new team** (lead + specialist sub-agents, same structure) and spawn **only after the user agrees.** |
| A coding/repo task (run a sim, fix a script, write a doc) | Do it directly; spawn only if it genuinely needs parallel research. |

Default to teams for analysis/research/simulation; default to a direct answer for everything else.
A "thorough"-sounding multi-part question is not automatically a spawn — judge whether real
multi-angle research adds value.

---

## 3. Teams, agents, and sub-agents

The model: **a team of humans, each with strengths/weaknesses, attacking a topic from several angles;
a lead reconciles and writes the report.** Prefer this over a single context window — parallel
specialists catch what one pass misses. Always try an **existing team** first.

### Existing project agents (`.claude/agents/`)
| Agent | Role | Spawns these sub-agents (parallel) |
|---|---|---|
| `v1-lead` | V1 Rate Limiting (throttle the oncogenic loop) | Food, Supplement, Bioavailability specialists |
| `v2-lead` | V2 Compiler Protection (reduce new-translocation risk) | Antioxidant, DNA-Repair, Anti-Inflammatory |
| `v3-lead` | V3 Hot Patching (restore suppressor/differentiation) | Epigenetic, Differentiation, PROTAC/ASO, Synthetic-Lethality |
| `v4-lead` | V4 Immune Watchdog (visibility + clearance) | Checkpoint/T-cell, NK, Microbiome-Immune, Neoantigen-Vaccine |
| `mrna-vaccine-lead` | Supplementary: BNT162b2 immune/inflammatory/genomic relevance | mrna-immune-effects, mrna-oncogenic-risk (optional) |
| `orchestrator` | Synthesis: dedupe, rank, resolve conflicts, write final catalog | Metastatic-Disease Specialist |

### Execution order (the standard full run)
1. `python scripts/dispatch.py` — prints the wave plan and validates prerequisites. **Run first.**
2. **Wave 1 (parallel):** `mrna-vaccine-lead`, `v1-lead`, `v3-lead`.
3. **Gate:** mRNA output on disk + V3's `MHC-I Upregulation Candidates` section written
   (`python scripts/dispatch.py gate`).
4. **Wave 2 (parallel):** `v2-lead`, `v4-lead` (consume mRNA output; V4 also consumes V3's MHC-I section).
5. **Orchestrator** runs last (`dispatch.py ready` must pass), runs the Metastatic-Disease Specialist,
   writes `simulation-output/protocol-v1.md`.

Each lead **reconciles** its sub-agents (merges duplicate compounds, keeps the strongest evidence tier)
— it does not just concatenate. Each agent loads the relevant skills (below) and runs
`sarcoma-pre-output-check` before writing.

### Recommending a NEW team
If no existing team fits (e.g., "forward trial forensics," "in-silico experiment design," "regimen
timing," "immune-state modeling" — all done previously), describe a lead + 2–4 specialists with distinct
angles, get the user's OK, then spawn. New work is a **supplementary team**, not a new vector.

### Practical caveat (learned)
Background sub-agent dispatch can hit transient API-overload windows (agents return with 0 tool-uses).
If retries keep failing, **run the work directly in the main thread** — same scripts, same data, same
grounding, same no-fabrication rule. The substance matters more than the delivery vehicle.

### Anchoring to a patient case
Runs can be anchored to a specific case (see `.prompts/run-sim.prompt`). When asked for a "clean-slate"
exercise, do **not** use stored personal memory. Always honor the atypical fusion-unconfirmed flag.

---

## 4. Running the Python simulations

Interpreter: the repo venv at `.venv/bin/python` (relative to the repo root). It has pandas, numpy,
scipy, networkx, requests, GEOparse, and `openmed` (mlx backend). `scripts/openmed_ner.py`
self-bootstraps into the venv.

```bash
# Orchestration helper — prints wave plan; subcommands validate state
python scripts/dispatch.py            # wave plan
python scripts/dispatch.py check      # prerequisite checks
python scripts/dispatch.py gate       # Wave-1 gate (mRNA + V3 MHC-I section)
python scripts/dispatch.py ready      # orchestrator preconditions

# In-silico simulations (real public data; reproducible):
.venv/bin/python sims/01-signature-reversal/run_signature_reversal.py   # GSE60740 -> L1000CDS2
.venv/bin/python sims/02-dependency-mining/run_dependency_mining.py     # DepMap 24Q4 CRISPR
.venv/bin/python sims/03-network-model/boolean_model.py                 # + ode_model.py
.venv/bin/python sims/04-immune-state-model/immune_state_model.py       # nectins + immune markers
.venv/bin/python sims/05-systemstate-sequencing/system_state_sequencing.py
```

**Simulation conventions (follow these when adding a sim):**
- Real data only. Each sim caches raw downloads under its own `data/` (gitignored) and writes a
  `MANIFEST.md` with source URLs, accession IDs, access date, and sha256. **Never invent a dataset,
  accession, gene-effect value, or compound** — if a download/API fails, report the failure.
- Each sim writes a `RESULTS.md` (real numbers + honest limitations), an `entities.txt`, and a
  `grounding.tsv` from OpenMed NER.
- See `sims/00-INDEX.md` for the current set and their convergent findings.
- **Isolate experimental runs in a git worktree** off the current good branch so the baseline state is
  not polluted (`git worktree add -b sim-<topic> ../sarcoma-<topic> <base>`). Branch names: `sim-*`.

---

## 5. Grounding with OpenMed NER

Every agent/sim **grounds** the biomedical entities it names (genes, drugs, diseases) with the OpenMed
NER ensemble before finalizing — confirming the named entities are recognized biomedical terms. It is
**for grounding only** — not for evidence tiering, mechanism, or citation discipline (those stay the
agent's responsibility).

```bash
python scripts/openmed_ner.py --list-teams                 # team -> model map (also in docs/07)
python scripts/openmed_ner.py --team v3-synthetic-lethality \
    --text-file sims/02-dependency-mining/entities.txt --format tsv > grounding.tsv
echo "WEE1 and EZH2 in CIC-DUX4." | python scripts/openmed_ner.py --team v1-lead
```

Pick the `--team` whose model set fits the entity types (genes/proteins → `v3-synthetic-lethality`;
drugs+genes → `v1-lead`; immune → `v4-lead`). Note any entity NER did **not** recognize. Models
download from HuggingFace on first use. See `docs/07-openmed-models.md`.

---

## 6. Skills (`.claude/skills/`)

Invoke these instead of re-deriving the rules:
- **`sarcoma-contract`** — evidence-tier vocabulary, citation rules, avoid/include lists. Load at the
  start of any vector-lead / sub-agent / orchestrator task.
- **`sarcoma-vector-context`** (`v1`|`v2`|`v3`|`v4`) — one vector's compound list, targets, caveats.
- **`sarcoma-chemo-interactions`** — screen any dietary/supplement candidate against VDC/IE.
- **`sarcoma-output-schema`** `<role>` — the output-file schema for a given agent role.
- **`sarcoma-pre-output-check`** — 8-failure-mode + 8-mandatory-include self-audit; run before writing.
- **`sarcoma-orchestrator-intake`** — orchestrator-only intake/dedupe/rank/conflict protocol.

---

## 7. Repository map

```
docs/00-README.md        framing + constraints + execution semantics (read first)
docs/01–05               domain knowledge, analogy model, the four attack vectors
docs/06-agent-architecture.md   full agent prompts + output schemas
docs/07-openmed-models.md       team -> NER model map
scripts/dispatch.py      wave plan + prerequisite/gate checker
scripts/openmed_ner.py   OpenMed NER grounding CLI (--team)
.claude/agents/          the 6 lead agents
.claude/skills/          the 6 sarcoma-* skills
sims/00-INDEX.md         the in-silico simulations + convergent findings
sims/01–05/              reproducible simulations (script + RESULTS.md + MANIFEST.md + grounding.tsv)
simulation-output/       protocol-v1.md (catalog), forward-simulation/, per-vector outputs,
                         and oncologist/MTB discussion briefs
```

---

## 8. GitHub Issues (light note — a dedicated skill will own this)

The repo is hosted on GitHub and the **Issues** section is the collaboration surface: people post
grounded thoughts/questions there. The intended workflow is **retrieve issues → apply labels → have
Claude Code respond**, and some responses require team/sub-agent research using the same structure
above. A dedicated **GitHub-issues skill** (in progress) will handle this; it may later run on a
schedule. For now it's invoked manually — don't build issue automation into general sessions; defer to
that skill. Use `gh` for GitHub operations.

---

## 9. Conventions

- **Branches:** `sim-*` for simulation/forward work; commit experimental runs to their own branch/worktree.
  Don't merge to `main` or push outward unless asked.
- **Commits:** end messages with `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
- **Don't pollute a state the user likes** — branch/worktree first.
- **Honesty over completeness**, always. When in doubt, exclude rather than pad.
