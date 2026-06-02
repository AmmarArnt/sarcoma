# CIC-Rearranged Sarcoma — A Research Simulation

A structured, AI-assisted thinking engine for a very rare and aggressive cancer (**CIC-rearranged
sarcoma**, driven by the CIC-DUX4 fusion). It treats the disease like a **bug in a running software
system** and asks, from many angles at once: how do we throttle it, contain it, repair it, and get the
immune system to clear it?

The output is **not a treatment plan**. It's a *ranked catalog of mechanistic hypotheses* — each one
tagged with how strong the evidence actually is — plus **forward hypotheses** the literature hasn't
tested yet, and small **computational experiments** anyone can re-run.

> ⚠️ **Research and hypothesis generation only.** Nothing here is medical advice, a dose, or a
> start/stop instruction. It's meant to inform reading and to start grounded conversations with
> qualified clinicians.

---

## The idea in 60 seconds

The fusion gene acts like a `while True: divide()` loop whose "stop" condition was deleted. We attack
it on four complementary layers (the working bet is that **no single layer is enough**):

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
- **Known research is the floor, not the ceiling.** The simulation is expected to ask *why* past
  approaches fell short and to generate testable new ideas — not just restate what's known.
- **Some hypotheses become runnable code.** See `sims/` for in-silico experiments on real public data
  (gene-signature drug repurposing, CRISPR-dependency mining, network models of the loop, immune-state
  modeling) — each reproducible, with its data sources listed.

---

## What's inside

- `simulation-output/protocol-v1.md` — the ranked, evidence-tiered hypothesis catalog.
- `simulation-output/forward-simulation/` — forward hypotheses, "why did it fail" analyses, and
  plain-language **discussion briefs** written to hand to an oncologist or molecular tumor board.
- `sims/` — five reproducible computational experiments (`sims/00-INDEX.md` summarizes them).
- `docs/` — the full framing (`00-README.md`), domain knowledge, the engineering analogy, the four
  vectors, and the agent architecture.

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
