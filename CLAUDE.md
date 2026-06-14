# CLAUDE.md — Operating Guide for Claude Code Sessions

This repository is a **multi-agent research simulation** for CIC-rearranged sarcoma (CIC-DUX4 fusion),
framed through a software/systems-engineering analogy. The deliverable is a **ranked, evidence-tiered
hypothesis catalog plus forward (not-yet-tested) hypotheses and runnable in-silico experiments** — never
a treatment plan. Read `docs/00-README.md` for full framing before substantial work.

**This is research and hypothesis generation only. No medical advice, no personal dosing, no
start/stop instructions for any therapy.** Mechanisms, food sources, evidence tiers, and published
trial dose-ranges (with citations) are in scope; prescriptive numbers are not.

---

## 0. Reuse the existing run first (cost discipline)

**An initial full simulation has already been run. Its artifacts live in `simulation-output/` and
`sims/` — read and reuse them before spawning anything.** Re-running the whole multi-agent cycle every
time is slow and token-expensive, and usually unnecessary.

Already on disk:
- `simulation-output/findings-ranking.md` — **master register of every notable finding** across all sims/
  teams/analyses, scored on the three axes (evidence tier / confidence / feasibility) with "top picks by
  criterion." One place to compare results (ADR-0009). **MAINTAIN IT:** whenever a new sim, team output, or
  analysis produces a result worth comparing against the others — or a perishable feasibility band changes —
  **add/update its row in the same commit/PR** (the file's "Maintenance rule" has the steps). Do not promote
  a logic/decision-model finding above a real-data finding on evidence strength.
- `simulation-output/protocol-v1.md` — the ranked, evidence-tiered hypothesis catalog (headline output).
- `simulation-output/{v1-rate-limiting,v2-compiler-protection,v3-hot-patching,v4-immune-watchdog,mrna-vaccine-research}/`
  — each vector/team lead's summary plus its sub-agent outputs.
- `simulation-output/metastatic-disease-considerations.md` and `.../supplementary-pulsed-adjunct/`.
- `simulation-output/forward-simulation/` — counterfactual trial forensics, in-silico experiment
  designs, the grounded citation index, and the oncologist/MTB discussion briefs.
- `simulation-output/biomarker-voi-stratification.md` — three-tier missing-data taxonomy
  (Known / Missing-decision-relevant / Missing-low-impact) + value-of-information ranking of unknown
  biomarkers (from Sim 6). Reuse this for "what's unknown / what would change the recommendation" questions.
  Extended by `simulation-output/biomarker-voi-provenance-extension.md` (issue #7 follow-up / ADR-0011),
  which adds two axes inside Tier B — **acquisition provenance** (P1 archived FFPE / P2 fresh biopsy /
  P3 liquid) and **temporal state** (T0 baseline / T1 current / TΔ change-under-treatment). Reuse it for
  "where does the answer come from / archived vs fresh tissue / clonal evolution / did the marker change
  under treatment / what's the cheapest source" questions.
- `simulation-output/diagnostic-information-gain-layer.md` — **diagnostic-action (test-level)
  expected-information-gain layer** answering *"what should we **learn** next?"* (from issue #31 / ADR-0015).
  Composes the variable-level VoI (Sim 6), provenance/burden axes (ADR-0011), and driver-resolution EVSI
  (Sim 8) into a per-**test** value profile (driver EVSI + immune-route VoI, kept separate — no blended
  score), an action-level **low-yield** register, and a constraint-aware **sequencing** rule (archived P1
  bundle first → fresh P2 only for the residual delta → liquid P3 monitoring → imaging on its own staging
  cadence, re-ranked after each result). Reuse for "which test next / value of a diagnostic / information
  gain / what's low-yield / how to sequence tests under tissue/budget/time" questions. Imaging VoI is named
  as an unmodeled gap; a quantitative Sim 9 is proposed, not executed. Not a testing recommendation.
- `simulation-output/translational-feasibility-layer.md` — five-band feasibility scheme (F1 Accessible-now
  … F5 Concept-only) applied to every Clinical/Experimental entry in `protocol-v1.md`, with live-verified,
  date-stamped regulatory/trial status (from issue #9 / ADR-0003). Reuse for "is it approved / in a trial /
  discontinued / how soon could a patient reach it" questions — **re-verify before external use; bands are
  perishable** (e.g. tazemetostat was withdrawn from US indications 2026-03-09).
  Extended by `simulation-output/feasibility-attrition-reason-extension.md` (issue #9 follow-up / ADR-0013),
  which adds an **attrition-reason annotation (R0–R5)** — *why* an F3/F4 program's access closed
  (R0 never-built · R1 target-invalidated · R2 trial-fail · R3 subgroup-dilution · R4 regulatory ·
  R5 commercial) — and the rule that **only R1 (and a biomarker-enriched R2) carries negative biology**;
  R3/R4-commercial/R5 are biology-silent. Reuse for "does discontinued/withdrawn mean it failed
  biologically," "why was X deprioritized," and the regorafenib CIC-cohort (REGOBONE/NCT02389244 =
  results-pending, not negative) questions. **Not a new axis** — an annotation on the feasibility axis.
- `simulation-output/host-biology-modifier-layer.md` — cross-cutting **host-biology modifier layer**
  (gut microbiome/SCFA, systemic inflammation/NLR/mGPS, metabolic/sarcopenia, nutrition, physical
  activity, sleep/circadian, autonomic/β-adrenergic, PNEI, placebo-nocebo, perioperative conditioning).
  Not a fifth vector — it conditions V4 and SOC tolerability and is weighted via the existing three axes
  (confidence/transfer does the down-weighting). Reuse for host-level / lifestyle / "does host biology
  explain variability or tolerance" questions (from issue #10 / ADR-0005).
- `simulation-output/v4-immune-watchdog/immune-watchdog-expansion.md` — V4 conceptual expansion covering
  innate **danger recognition** (DAMPs, immunogenic cell death, HSP/HMGB1/calreticulin/ATP), the
  **Nectin–TIGIT–DNAM-1 / NKG2A-HLA-E** axis (incl. NTX1088 anti-PVR and the failed anti-TIGIT phase-3
  programs), NK exhaustion/stress-ligand evasion, and the standing **inflammation-state lens** (separating
  tumor-promoting inflammation vs. anti-tumor activation vs. treatment-related toxicity). Inside V4 — not a
  fifth vector (from issue #11 / ADR-0006). Reuse for immune-visibility / danger-signaling / ICD /
  Nectin-axis / NK-surveillance questions.
- `simulation-output/tumorigenesis-reverse-engineering/` — the **forward / "steps to reproduce" build
  recipe** (the INVERSE of the four attack vectors): how a normal mesenchymal progenitor *becomes* a
  CIC-DUX4 cell, reverse-engineered into intervention points. Lead `tumorigenesis-build-recipe.md`
  (headline) + four specialist briefs (cell-of-origin, driver-engineering, cooperating-lesions,
  epigenetic-permissiveness). A supplementary team, **not a fifth vector**. Reuse for cell-of-origin /
  pathogenesis / "how/why does the cell get into this state" / "reverse-engineer the construction" /
  minimal-transformation-set questions (from ADR-0007).
- `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md` + `sims/08-driver-uncertainty/`
  — the **fusion-unconfirmed / "unknown driver" decision model** (ADR-0008). Treats the driver of the ~5%
  fusion-unconfirmed patient as a latent variable (D1 cryptic CIC-DUX4 … D5 orphan), marginalizes the
  catalog over a literature-anchored prior (robustness), computes the **value of resolving the driver**
  (EVSI: long-read WGS+RNA-seq > DUX4 IHC > methylation array), and sweeps the prior. Reuse for
  fusion-unconfirmed / atypical-case / "unknown driver" / "what should we test first / value of resolving
  the diagnosis" questions. Key result: throttle/cell-cycle/immune vectors are driver-robust; the
  **DUX4/MCL1 "re-arm" hypothesis is driver-contingent** (hold until resolved).
- `sims/01–08/` — executed in-silico experiments with `RESULTS.md` + data `MANIFEST.md` + grounding.
  (Sim 7 = Boolean **transformation-trajectory** behind the build recipe; Sim 8 = the **driver-uncertainty**
  decision model above.)

**Default behavior:** answer from and cite these artifacts; extend incrementally. Do **not** re-run the
waves in §3 (or re-execute a sim) to reproduce something already on disk.

**Only run a fresh full cycle (§3) — or re-execute a sim — when one of these holds:**
- the user explicitly asks for a clean/fresh run or to **overwrite** existing outputs;
- the question needs **scope or parameters the existing artifacts don't cover** (a different patient
  case, a new compound/target, a different angle); or
- the findings need **expansion or updating** with newer evidence.

When extending: spawn only the **specific** specialist or supplementary team needed, and **write a new
artifact** (e.g. `protocol-v2.md`, a new `sims/NN-*/`, a dated file) rather than clobbering existing
ones — unless the user asked for an overwrite. Preserve the prior run as the baseline.

---

## 1. Golden rules (non-negotiable — apply to every output, every agent)

From `docs/00-README.md`, `docs/06-agent-architecture.md`, and the `sarcoma-contract` skill.

1. **No fabricated citations. Ever.** If you can't point to a real PMID / NCT / DOI / dataset, write
   `[no direct citation; mechanism inferred from {what}]`. Plausible-looking fake references are the
   single worst failure mode. **Verify accessions/PMIDs against live sources when you can** (WebSearch/
   WebFetch); if you can't verify, label it `[VERIFY]` rather than asserting it. Regulatory/trial/safety
   status is **perishable** — verify it live and never carry it across sessions unchecked (operative rule +
   source registry: `sarcoma-contract` and `docs/09-verification-sources.md`).
2. **Evidence tier on every claim.** Use exactly one: `Established` › `Clinical-Trial` ›
   `Preclinical-Animal` › `Preclinical-Cell` › `Mechanistic` › `Dietary-Observational` › `Theoretical`.
   Tier is the first of three orthogonal axes (tier / confidence / feasibility) — see `sarcoma-contract`
   for when to also carry confidence and translational-feasibility reads.
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
| A question the existing run already answers | **Read & cite `simulation-output/` / `sims/`.** Don't re-run the cycle (see §0). |
| A simple factual / clarifying / "why" question | **Just answer.** No spawning, no repo-wide research. |
| "Analyze X thoroughly," "from multiple angles," "what could be tried," "run a simulation" | **Spawn the appropriate team** (below) so the topic gets multiple perspectives. |
| A research question with no fitting existing team | **Propose a new team** (lead + specialist sub-agents, same structure) and spawn **only after the user agrees.** |
| A coding/repo task (run a sim, fix a script, write a doc) | Do it directly; spawn only if it genuinely needs parallel research. |
| A question about which unknown/unmeasured biomarkers matter, "what should we measure," or stratifying a new case | **Reuse the VoI layer** (`simulation-output/biomarker-voi-stratification.md` / Sim 6); extend it rather than re-deriving. |
| A question about **where** a missing biomarker's answer comes from / archived FFPE vs fresh biopsy vs liquid biopsy / clonal evolution / whether a marker **changed under treatment** / the cheapest source for a measurement | **Reuse the VoI provenance extension** (`simulation-output/biomarker-voi-provenance-extension.md` / ADR-0011): classify on **provenance** (P1 archived / P2 fresh / P3 liquid) and **temporal state** (T0 baseline / T1 current / TΔ change). Realizable VoI is bounded by recoverability from an accessible source; **not a testing recommendation**. |
| A **diagnostic-strategy** question — "what test should we do / learn next," the value/information-gain of a diagnostic, which investigations are **low-yield**, or how to **sequence** tests under tissue/budget/time constraints | **Reuse the diagnostic information-gain layer** (`simulation-output/diagnostic-information-gain-layer.md` / ADR-0015): score each **action** by its value *profile* (driver EVSI from Sim 8 + immune-route VoI from Sim 6, kept separate — no blended score) ÷ acquisition burden (ADR-0011), and apply the greedy sequencing rule (archived P1 first → fresh P2 for the residual delta → liquid P3 monitoring → imaging on its own staging axis). Imaging VoI is an unmodeled gap; **not a testing recommendation**. |
| A question about whether a candidate is approved / in a recruiting trial / discontinued / on hold, its FDA-vs-EMA status, repurposing path, or "how soon could a patient access it" | **Reuse the feasibility layer** (`simulation-output/translational-feasibility-layer.md` / ADR-0003); **re-verify the regulatory/trial facts live** before relying on them — bands are date-stamped and perishable. |
| A question about **why** a program closed / "does discontinued or withdrawn mean it failed biologically" / "was X deprioritized for negative data" / preserving subgroup signals in rare-tumor baskets | **Reuse the feasibility-attrition-reason extension** (`simulation-output/feasibility-attrition-reason-extension.md` / ADR-0013): classify the closure (R0 never-built / R1 target-invalidated / R2 trial-fail / R3 subgroup-dilution / R4 regulatory / R5 commercial); **only R1 (+ enriched R2) argues against the mechanism** — R3/R4-commercial/R5 keep it in the forward lane. **Annotation, not a new axis**; re-verify perishable statuses live. |
| A host-level / lifestyle question (microbiome, inflammation, metabolic/sarcopenia, nutrition, exercise, sleep/circadian, autonomic/stress/PNEI, placebo-nocebo, perioperative conditioning) — "does host biology explain variability / tolerance / immune competence," "should it be its own layer" | **Reuse the host-biology modifier layer** (`simulation-output/host-biology-modifier-layer.md` / ADR-0005); extend it rather than re-deriving. It is a cross-cutting modifier (conditions V4 + SOC), **not a fifth vector**, weighted via the existing three axes. |
| A question about **how transfer distance is weighted** / "is broader (sarcoma / solid-tumour / host-biology) evidence being excluded just because CIC-DUX4 is rare" / "should we admit conserved-mechanism evidence at lower confidence" | **Reuse the evidence-transferability hierarchy** (`docs/10-evidence-transferability-hierarchy.md` / ADR-0014): score the confidence **Directness** sub-axis on the graded proximity ladder (P0 CIC-DUX4 → P1 fusion round-cell family → P2 sarcoma → P3 solid-tumour-with-named-mechanism → P4 pathway-only). **Rarity lowers the rung (lower confidence), never excludes; only a missing mechanistic bridge excludes.** A refinement of the confidence axis (ADR-0004), **not a new axis**; never prunes the forward lane. |
| A V4 immune-visibility / danger-signaling / ICD / DAMP / Nectin-TIGIT / NK-surveillance question, or "should the framework distinguish tumor-promoting inflammation vs. anti-tumor activation vs. treatment toxicity" | **Reuse the V4 expansion** (`simulation-output/v4-immune-watchdog/immune-watchdog-expansion.md` / ADR-0006) and the four V4 sub-agent files; extend rather than re-deriving. It is *inside* V4 — **not a fifth vector**; apply the inflammation-state lens (lowering inflammation ≠ improving anti-tumor immunity). |
| A cell-of-origin / pathogenesis / tumorigenesis question — "how/why does the cell get *into* this state," "what would you do to a stem cell to make this tumor," "reverse-engineer the construction," minimal-transformation-set / which build steps are necessary | **Reuse the tumorigenesis reverse-engineering layer** (`simulation-output/tumorigenesis-reverse-engineering/` + `sims/07-tumorigenesis-trajectory/` / ADR-0007); extend rather than re-deriving. It is the **forward/inverse** of V1–V4 (a build recipe mapped back onto the vectors), a supplementary team, **not a fifth vector**. |
| A fusion-unconfirmed / atypical-case / "unknown driver" question — "the patient has no confirmed fusion," "which options are safe given we don't know the driver," "what should we test first / is it worth resolving the diagnosis" | **Reuse the driver-uncertainty decision model** (`simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md` + `sims/08-driver-uncertainty/` / ADR-0008). Treats the driver as a latent variable, marginalizes for robustness, and computes EVSI of resolving it; re-condition the prior on any real testing the patient already had. **Not a diagnosis.** |

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

**Supplementary teams (ad-hoc, no committed `.claude/agents/` file — reuse the written artifacts first):**
| Team | Role | Spawned specialists (parallel) | Output |
|---|---|---|---|
| Tumorigenesis / Cell-of-Origin Reverse-Engineering (ADR-0007) | **Forward/inverse** of V1–V4: the "build recipe" for how a progenitor becomes a CIC-DUX4 cell, mapped back onto the vectors | Cell-of-Origin, Driver-Engineering, Cooperating-Lesions, Epigenetic-Permissiveness | `simulation-output/tumorigenesis-reverse-engineering/` + `sims/07-tumorigenesis-trajectory/` |

### Execution order (the standard full run)
> Run this **only for a fresh full cycle** — reuse the existing outputs first (see §0). For incremental
> work, spawn just the specific specialist/team needed and write a new artifact rather than re-running.
1. `python scripts/dispatch.py` — prints the wave plan and validates prerequisites. **Run first.**
2. **Layer Intake (every full run — ADR-0016).** Before Wave 1, each agent additionally consults the
   **standing analytical layers** relevant to its scope (the §0 reuse list / §2 routing table): V4 ←
   host-biology (ADR-0005) + V4 immune-watchdog expansion (ADR-0006) + VoI immune ranking (Sim 6) +
   diagnostic-IG immune markers (ADR-0015); V3 ← driver-uncertainty contingency (ADR-0008) + tumorigenesis
   build-recipe (ADR-0007); V1/V2 ← feasibility/attrition (ADR-0003/0013) + transferability (ADR-0014, via
   `sarcoma-contract`) + host-biology for tolerability. The **orchestrator** reconciles the catalog against
   **all** layers + `findings-ranking.md`. **Layers condition/annotate — they never override real-data
   vector evidence (ADR-0009 bias note) and never prune the forward lane (golden rule #5); not a fifth
   vector (golden rule #8).** A fresh re-run writes the **next** protocol version, not over the baseline (§0).
3. **Wave 1 (parallel):** `mrna-vaccine-lead`, `v1-lead`, `v3-lead`.
4. **Gate:** mRNA output on disk + V3's `MHC-I Upregulation Candidates` section written
   (`python scripts/dispatch.py gate`).
5. **Wave 2 (parallel):** `v2-lead`, `v4-lead` (consume mRNA output; V4 also consumes V3's MHC-I section).
6. **Orchestrator** runs last (`dispatch.py ready` must pass), ingests the standing layers (ADR-0016),
   runs the Metastatic-Disease Specialist, writes the catalog (next `protocol-vN.md`, not over v1).

Each lead **reconciles** its sub-agents (merges duplicate compounds, keeps the strongest evidence tier)
— it does not just concatenate. Each agent loads the relevant skills (below), ingests its standing layers
(step 2 / ADR-0016), and runs `sarcoma-pre-output-check` before writing.

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
.venv/bin/python sims/06-biomarker-value-of-information/run_voi.py        # missing-biomarker value-of-information
```

**Simulation conventions (follow these when adding a sim):**
- Real data only. Each sim caches raw downloads under its own `data/` (gitignored) and writes a
  `MANIFEST.md` with source URLs, accession IDs, access date, and sha256. **Never invent a dataset,
  accession, gene-effect value, or compound** — if a download/API fails, report the failure.
- Each sim writes a `RESULTS.md` (real numbers + honest limitations), an `entities.txt`, and a
  `grounding.tsv` from OpenMed NER.
- See `sims/00-INDEX.md` for the current set and their convergent findings.
- **Update `simulation-output/findings-ranking.md`** in the same change when a sim produces a result worth
  comparing against the others (the file's "Maintenance rule" + ADR-0009 have the steps).
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

**Entity grounding (this) is not fact-checking.** OpenMed NER confirms a *name* is a recognized
biomedical term; it cannot tell you a drug was withdrawn or a trial closed. For verifying any
**status / approval / trial / safety / citation** *claim*, use the authoritative registries in
**`docs/09-verification-sources.md`** (the standing source list from issue #9) and date-stamp what you read.

---

## 6. Skills (`.claude/skills/`)

Invoke these instead of re-deriving the rules:
- **`sarcoma-contract`** — evidence-tier vocabulary, the three scoring axes (tier / confidence /
  feasibility), citation + live-verification rules (incl. the perishable-status rule → `docs/09`),
  avoid/include lists. Load at the start of any vector-lead / sub-agent / orchestrator task.
- **`sarcoma-vector-context`** (`v1`|`v2`|`v3`|`v4`) — one vector's compound list, targets, caveats.
- **`sarcoma-chemo-interactions`** — screen any dietary/supplement candidate against VDC/IE.
- **`sarcoma-output-schema`** `<role>` — the output-file schema for a given agent role.
- **`sarcoma-pre-output-check`** — 9-failure-mode + 9-mandatory-include self-audit; run before writing.
- **`sarcoma-orchestrator-intake`** — orchestrator-only intake/dedupe/rank/conflict protocol.

---

## 7. Repository map

The tree is organized in four audience tiers. **Convention: dot-prefixed = Tier 4 (machine/config);
plain names tiered by how human-facing. `scripts/` is the one un-dotted Tier-4 exception — it's a
documented runnable entry point.** Don't add new dirs without assigning a tier (see §9).

| Tier | Audience | Contents |
|---|---|---|
| **1 — Read first (human)** | Clinicians · patients · non-technical | `simulation-output/protocol-v2.md` (main catalog) · `simulation-output/findings-ranking.md` · `simulation-output/forward-simulation/*-brief.md` |
| **2 — Hybrid** | Researchers · motivated readers | rest of `simulation-output/` (analytical layers + per-vector summaries) · `docs/00–05` |
| **3 — Contributor / LLM** | Developers · AI agents | `docs/06–09` · `docs/adr/` · `sims/` · `CLAUDE.md` · `scripts/` |
| **4 — Machine / tooling** | Script runner · configs · caches | `.claude/` · `.prompts/` · `.venv/` · `.gitignore` · gitignored `sims/*/data/` |

```
docs/00-README.md        framing + constraints + execution semantics (read first)
docs/01–05               domain knowledge, analogy model, the four attack vectors
docs/06-agent-architecture.md   full agent prompts + output schemas
docs/07-openmed-models.md       team -> NER model map (entity grounding)
docs/08-evidence-confidence-scoring.md   confidence axis: 7-tier↔A–E crosswalk, 4-axis rubric, weak-signal register
docs/09-verification-sources.md authoritative trial/regulatory/safety registries for live fact-checking (issue #9)
docs/10-evidence-transferability-hierarchy.md   biological-proximity ladder (P0–P4) refining the confidence Directness sub-axis (issue #10 follow-up / ADR-0014)
docs/adr/                       Architecture Decision Records — framework-evolution timeline (read README first)
scripts/dispatch.py      wave plan + prerequisite/gate checker
scripts/openmed_ner.py   OpenMed NER grounding CLI (--team)
.claude/agents/          the 6 lead agents
.claude/skills/          the 6 sarcoma-* content skills + github-issue-runner (workflow; ADR-0002)
sims/00-INDEX.md         the in-silico simulations + convergent findings
sims/01–08/              reproducible simulations (script + RESULTS.md + MANIFEST.md + grounding.tsv)
simulation-output/       protocol-v2.md (main catalog), findings-ranking.md (master register),
                         forward-simulation/ (oncologist briefs), biomarker-voi-stratification.md,
                         translational-feasibility-layer.md, host-biology-modifier-layer.md,
                         tumorigenesis-reverse-engineering/, per-vector outputs
```

---

## 8. GitHub Issues (light note — a dedicated skill will own this)

The repo is hosted on GitHub and the **Issues** section is the collaboration surface: people post
grounded thoughts/questions there. The workflow is **retrieve issue → apply labels → have Claude Code
respond**, and some responses require team/sub-agent research using the same structure above.

This is owned by the **`github-issue-runner` skill** (`.claude/skills/github-issue-runner`; see
ADR-0002). Invoke it **manually** — it processes **one** issue per run, prioritizing the oldest open
issue labeled `needs attention` (an author follow-up on something already answered) and otherwise the
oldest open issue labeled neither `running`, `responded`, nor `needs attention`. It labels the issue
`running`, does the work in an isolated worktree off latest `main`, opens a PR assigned to the
maintainer, posts a findings comment, then relabels the issue `responded`. Run it again for the next
issue (sequential, user-paced). Labels are lowercase (`running` / `responded` / `needs attention`).

A nightly GitHub Action (`.github/workflows/issue-needs-attention.yml`, ADR-0010, heuristic refined in
ADR-0012) is the **one** sanctioned piece of scheduled automation: it scans issues labeled `responded`
for a newer comment **from someone other than the responder** — i.e. excluding both `github-actions[bot]`
**and** the maintainer/repo-owner account (the skill and manual follow-ups post as that account, so
counting them caused a false-positive requeue on #11) — and swaps `responded` -> `needs attention` so the
skill re-queues it. It does **not** do any analysis, commenting, or PR work itself. Don't improvise
issue handling in general sessions or build other scheduled automation — defer to the skill and this
one Action. Use `gh` for GitHub operations.

---

## 9. Conventions

- **Branches:** `sim-*` for simulation/forward work; commit experimental runs to their own branch/worktree.
  Don't merge to `main` or push outward unless asked.
- **Commits:** end messages with `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
- **Don't pollute a state the user likes** — branch/worktree first.
- **Honesty over completeness**, always. When in doubt, exclude rather than pad.

### Directory tiering — keep the tree streamlined

Every new directory or top-level file gets a tier assignment before it lands on `main`. Use this table:

| What you're adding | Tier | Where it goes | Extra step |
|---|---|---|---|
| Ranked catalog, oncologist brief, or master register (human deliverable) | **1** | `simulation-output/` (catalog/brief) or root (index) | **Link it** from the README "Where to start" block in the same PR |
| Analytical layer, per-vector summary, domain output, biomarker/VoI file | **2** | `simulation-output/` | — |
| In-silico sim, agent/architecture doc, ADR, dev doc, evidence reference | **3** | `sims/`, `docs/` | Add row to `sims/00-INDEX.md` or `docs/adr/` as appropriate |
| Machine scratch, cache, config, secret, or purely-tool dir | **4** | **Dot-prefix it** (e.g. `.scratch/`) **or** add to `.gitignore` | Never drop machine scratch into a Tier 1/2 dir |

**Rules:**
- Never mass-rename existing core dirs to add dots — it breaks 130+ path references and
  `scripts/dispatch.py`. The README is the navigation layer; the filesystem is secondary.
- `scripts/` stays un-dotted — it's a documented, externally runnable entry point.
- When in doubt, ask: "would a clinician or patient be confused to see this in the GitHub tree?"
  If yes → Tier 3/4; hide it behind the README nav layer.

---

## 10. Architecture Decision Records (`docs/adr/`)

The framework evolves — new analytical layers, new teams, contract changes, conventions. Each such
**framework-level decision is recorded as a dated, numbered ADR** in `docs/adr/`, so the project carries
an honest historical timeline rather than silently mutating. CLAUDE.md holds the *current* rules; the
ADR log holds *why and when* they changed. Keep the log in `docs/adr/`, **not** inline here.

- **Read** `docs/adr/README.md` (the index) when you need the rationale or history behind a rule, or
  before proposing a change that may contradict a past decision.
- **Append** a new ADR (copy the template in the README, next number, status `Accepted`) when a change
  is **framework-level**: a new standing deliverable/sim *type*, a new team or agent, a change to the
  golden rules / contract / conventions, or a notable methodology choice. Link the originating issue/PR.
  Then update CLAUDE.md's current-state rules to match and cross-reference the ADR number.
- **Don't** write an ADR for routine work (answering a question, running an existing sim, a bug fix) —
  only for decisions that change how the framework itself operates.
