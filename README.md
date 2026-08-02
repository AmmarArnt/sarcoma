# Ewing-like / CIC-like Round-Cell Sarcoma — A Research Simulation

A structured, AI-assisted thinking engine for a very rare and aggressive cancer — a **small round-cell
sarcoma, clinically and histologically CIC-like / Ewing-like, with no confirmed fusion**. It treats the
disease like a **bug in a running software system** and asks, from many angles at once: how do we throttle
it, contain it, repair it, and get the immune system to clear it?

> 📌 **Read [`CASE-BASELINE.md`](CASE-BASELINE.md) first.** As of **2026-08-02** the case framing was
> refreshed: the tumour is **driver-unresolved** (no confirmed CIC-DUX4) and has now shown a **deep,
> twice-repeated chemotherapy response**, which is atypical for canonical CIC-DUX4. Most of this
> repository (`protocol-v1..v4`, `sims/01–09`, `docs/`, `ADR-0001..0020`) was written **before** that
> refresh, under a canonical-CIC-DUX4 working assumption. Those files are **preserved, not rewritten** —
> `CASE-BASELINE.md` §5 is the translation table for reading them. New work goes against the baseline.

The output is **not a treatment plan**. It's a *ranked catalog of mechanistic hypotheses* — each one
tagged with how strong the evidence actually is — plus **forward hypotheses** the literature hasn't
tested yet, and small **computational experiments** anyone can re-run.

> ⚠️ **Research and hypothesis generation only.** Nothing here is medical advice, a dose, or a
> start/stop instruction. It's meant to inform reading and to start grounded conversations with
> qualified clinicians.

---

## Where to start (pick your path)

**I'm a clinician, patient, or non-technical reader — show me the findings:**

| Document | What it is |
|---|---|
| [`CASE-BASELINE.md`](CASE-BASELINE.md) | **Read this first — the current working snapshot of the case** (Era B, from 2026-08-02): what's established vs inferred vs still open, the driver posterior, the cell-state read, and how to read the older artifacts. |
| [`simulation-output/chemosensitivity-ddr-cellstate-layer.md`](simulation-output/chemosensitivity-ddr-cellstate-layer.md) | What the chemotherapy response reveals about the cell's DNA-damage-response state, the relapse reservoir, and **when** in the treatment course immunotherapy has its best window. |
| [`simulation-output/protocol-v4.md`](simulation-output/protocol-v4.md) | **The main hypothesis catalog — ranked and evidence-tiered.** (v4, 2026-06-25: an evidence-verified update of v3 — adds the p300/CBP multi-vector MHC-I-restoring node + DUX4-STAT1 immune-evasion arm; `protocol-v1/v2/v3.md` retained as prior baselines.) **Era-A document** — read alongside `CASE-BASELINE.md` §5. |
| [`simulation-output/findings-ranking.md`](simulation-output/findings-ranking.md) | One-page master register: every notable finding scored on three axes (evidence strength · confidence · real-world access). The honest summary and quick-scan table. |
| [`simulation-output/forward-simulation/WEE1-ifosfamide-oncologist-brief.md`](simulation-output/forward-simulation/WEE1-ifosfamide-oncologist-brief.md) | Plain-language brief on the WEE1 + ifosfamide hypothesis — written to hand to an oncologist or molecular tumor board. |
| [`simulation-output/forward-simulation/selective-clearance-oncologist-brief.md`](simulation-output/forward-simulation/selective-clearance-oncologist-brief.md) | Brief on selective immune clearance strategies — same format, same audience. |
| [`simulation-output/forward-simulation/00-INDEX.md`](simulation-output/forward-simulation/00-INDEX.md) | Index of all forward hypotheses and discussion briefs. |

**I'm a researcher or want to challenge the findings:**

Start with [`docs/00-README.md`](docs/00-README.md) (full framing), then
[`docs/02-cic-sarcoma-knowledge.md`](docs/02-cic-sarcoma-knowledge.md) and
[`docs/05-attack-vectors.md`](docs/05-attack-vectors.md). The
[Issues tab](../../issues) is the front door for grounded contributions.

**I'm here to run the code or extend the simulation:**

Read [`CLAUDE.md`](CLAUDE.md) first (how sessions and agent teams operate), then
`scripts/dispatch.py` (wave plan) and `sims/00-INDEX.md` (what each experiment does).

---

## The idea in 60 seconds

The driver acts like a `while True: divide()` loop whose "stop" condition was deleted. (*Which* driver
deleted it is genuinely unresolved in this case — see `CASE-BASELINE.md`; the loop behaves the same way
either way, which is why the four layers below are mostly driver-agnostic.) We attack it on four
complementary layers (the working bet is that **no single layer is enough**):

| Vector | Plain meaning |
|---|---|
| **V1 — Rate Limiting** | Slow the loop down; reduce how much it produces per cycle. |
| **V2 — Compiler Protection** | Lower the chance neighbouring cells acquire the same fault. |
| **V3 — Hot Patching** | Restore the missing "stop" signal / push the cell to grow up (differentiate). |
| **V4 — Immune Watchdog** | Make the cell visible to the immune system so it gets cleared. |

---

## How it works

- **A team of AI specialists, not one voice.** Each vector has a *lead* that spawns specialist
  *sub-agents* (food, supplements, epigenetics, immunology, …), who research in parallel; the lead
  reconciles them, and an *orchestrator* merges everything into one ranked catalog. Disagreements are
  surfaced, not smoothed over.
- **Every claim carries an evidence tier** — from `Established` (approved/guideline) down to
  `Theoretical` — so a reader instantly sees what's solid and what's a stretch.
- **No invented references.** If there's no real source, it says so. Findings are grounded against a
  biomedical entity recognizer (OpenMed NER) and, where possible, verified against live literature.
- **Known research is the floor, not the ceiling.** The simulation asks *why* past approaches fell
  short and generates testable new ideas — not just restatements of what's known.
- **Some hypotheses become runnable code.** See `sims/` for in-silico experiments on real public data
  (gene-signature drug repurposing, CRISPR-dependency mining, network models of the loop, immune-state
  modeling) — each reproducible, with its data sources listed.

---

## Repository map (organized by audience)

The tree is arranged in four tiers. If you're not here to run code, you can ignore Tiers 3 and 4
entirely.

| Tier | Audience | Directories / files |
|---|---|---|
| **1 — Read first** | Clinicians · patients · non-technical readers | `simulation-output/protocol-v4.md` (main catalog; v1–v3 retained as baselines) · `simulation-output/findings-ranking.md` · `simulation-output/forward-simulation/*-brief.md` (plain-language discussion briefs) · this `README.md` |
| **2 — Hybrid** | Researchers · motivated readers | rest of `simulation-output/` (analytical layers: biomarker VoI, feasibility, host-biology, metastatic, per-vector summaries, tumorigenesis reverse-engineering) · `docs/00–05` (framing + domain knowledge) |
| **3 — Contributor / LLM** | Developers · AI agents | `docs/06–09` + `docs/adr/` (agent architecture, evidence-scoring, verification sources, ADRs) · `sims/` (reproducible in-silico experiments) · `CLAUDE.md` (session operating guide) · `scripts/` (orchestration + NER) |
| **4 — Machine / tooling** | Script runner · configs · caches | `.claude/` · `.prompts/` · `.venv/` · `.gitignore` · gitignored `sims/*/data/` |

> **Convention:** dot-prefixed directories are Tier 4 (machine/config). Everything else is plain-named
> and tiered by how human-facing it is. `scripts/` is the one un-dotted Tier-4 exception because it's a
> documented runnable entry point referenced throughout the docs.

---

## Contribute — the Issues tab is the front door

This is an evolving, collaborative thesis, and **you don't need to be an oncologist *or* an engineer to
help.** If you have a grounded thought, a paper we should read, a flaw to poke, or a hypothesis worth
testing — **open a GitHub Issue.** Mechanistic reasoning and real citations are welcome; hand-waving and
miracle cures are not. Issues are triaged, labelled, and may trigger a full multi-agent research pass to
answer them.

The one house rule mirrors the whole project: **be specific, cite what's real, and say when you're
unsure.**

---

## Run it (for the technically inclined)

```bash
python scripts/dispatch.py                 # see the multi-agent wave plan
.venv/bin/python sims/01-signature-reversal/run_signature_reversal.py   # example experiment
```

New to the codebase? Read **`CLAUDE.md`** (how sessions and the agent teams operate) and
**`docs/00-README.md`** (framing and constraints) first.

---

## Where this is headed

Built in the open as a living thesis. The intent is to keep tightening the evidence, invite medical
researchers and clinicians to challenge and refine it, and align anything that matures toward real
clinical and regulatory review. Grounded skepticism is the most useful contribution you can make.
