# CLAUDE.md — Operating Guide for Claude Code Sessions

This repository is a **multi-agent research simulation** for a **small round-cell sarcoma that is
clinically/histologically CIC-like and Ewing-like but has NO confirmed fusion**, framed through a
software/systems-engineering analogy. The deliverable is a **ranked, evidence-tiered hypothesis catalog
plus forward (not-yet-tested) hypotheses and runnable in-silico experiments** — never a treatment plan.
Readers are clinicians and an informed patient.

**Read `CASE-BASELINE.md` before anything else.** It is the canonical, current case (Era B, from
2026-08-02) and supersedes the case framing embedded in `protocol-v1..v4`, `sims/01–09`, `docs/`, and
`ADR-0001..0020`. Those Era-A artifacts assumed canonical CIC-DUX4 biology; they are **preserved, not
rewritten**, and `CASE-BASELINE.md` §5 is the translation table for reading them. The driver is genuinely
*unresolved* (D4 phenocopy 0.386 > D1 cryptic CIC-DUX4 0.264; ADR-0021/0022): do not default to CIC-DUX4
biology, and do not overclaim the reverse — "not CIC-DUX4" is not established.

**This is research and hypothesis generation only. No medical advice, no personal dosing, no
start/stop instructions for any therapy.** Mechanisms, food sources, evidence tiers, and published
trial dose-ranges (with citations) are in scope; prescriptive numbers are not.

---

## 0. Reuse the existing run first

A full simulation and many analytical layers already exist in `simulation-output/` and `sims/`.
**Answer from them and extend incrementally** — re-running the multi-agent cycle is slow and expensive and
usually unnecessary. Reuse *through* the baseline: per `CASE-BASELINE.md` §5a this case has **no P0
anchor**, so CIC-DUX4-direct evidence is discounted to the D1+D2 posterior (~0.36), Ewing/round-cell-family
evidence is up-weighted, and fusion-agnostic evidence keeps full weight.

**Era tags (ADR-0022).** Artifacts authored 2026-06-02 → 2026-08-01 are **Era A** (canonical-CIC-DUX4
working assumption): their *mechanism* content holds, their *case framing* and *Directness weighting* do
not. Artifacts from 2026-08-02 on are **Era B**.

Run a fresh full cycle (§3) or re-execute a sim **only** when the user asks for a clean/fresh run or an
overwrite; when the question needs scope or parameters the artifacts don't cover (a new case, compound,
target or angle); or when findings need updating with newer evidence. Otherwise spawn only the specific
specialist or team needed and **write a new artifact** (`protocol-vN.md`, a new `sims/NN-*/`, a dated
file) rather than clobbering — the prior run stays as the baseline.

### Where each kind of question is already answered

None of these is a fifth vector (golden rule 8); layers condition and annotate, they never override
real-data vector evidence (ADR-0009) and never prune the forward lane (golden rule 5). Every layer says
"not a testing / treatment recommendation" where relevant. Perishable regulatory/trial facts must be
**re-verified live** before reuse.

| Question | Artifact (ADR) | What to carry over |
|---|---|---|
| What is the case now / is it still "CIC-DUX4" / what changed / which old findings hold | `CASE-BASELINE.md` (0022) | §2 established-vs-inferred-vs-open, §3 driver posterior, §5 Era-A translation table, §8 what would change it. Never state "it is not CIC-DUX4" — cryptic CIC-DUX4 still holds ~26%. |
| Compare findings across sims/teams; which result is strongest | `simulation-output/findings-ranking.md` (0009) | Master register scored on tier / confidence / feasibility. **Maintain it**: add/update a row in the same change whenever a new result or a perishable feasibility band changes (its "Maintenance rule"). Never rank a logic/decision-model finding above a real-data one on evidence strength. |
| The catalog itself | `protocol-v4.md` (v1–v3 retained as baselines); per-vector folders; `metastatic-disease-considerations.md`; `supplementary-pulsed-adjunct/`; `forward-simulation/` (trial forensics, in-silico designs, citation index, oncologist/MTB briefs) | Era-A framing — re-weight per §5a. |
| What's unknown / which unmeasured biomarker would change the recommendation | `biomarker-voi-stratification.md` (Sim 6, 0001) + `biomarker-voi-provenance-extension.md` (0011) | Known / missing-decision-relevant / low-impact taxonomy + VoI ranking. Provenance P1 archived FFPE / P2 fresh biopsy / P3 liquid; temporal T0 baseline / T1 current / TΔ change-under-treatment. Realizable VoI is bounded by recoverability from an accessible source. |
| Which test next / value of a diagnostic / low-yield tests / sequencing under tissue-budget-time limits | `diagnostic-information-gain-layer.md` (0015) | Per-test value *profile* — driver EVSI (Sim 8) and immune-route VoI (Sim 6) kept separate, no blended score — ÷ acquisition burden. Sequence: archived P1 bundle → fresh P2 for the residual delta → liquid P3 monitoring → imaging on its own staging cadence; re-rank after each result. Imaging VoI is an unmodeled gap. |
| Is X approved / in a trial / discontinued; FDA vs EMA; how soon could a patient reach it | `translational-feasibility-layer.md` (0003) | F1 accessible-now … F5 concept-only, date-stamped. Bands are perishable (tazemetostat's US indications were withdrawn 2026-03-09). |
| Why did a program close / does "withdrawn" mean it failed biologically | `feasibility-attrition-reason-extension.md` (0013) | R0 never-built · R1 target-invalidated · R2 trial-fail · R3 subgroup-dilution · R4 regulatory · R5 commercial. Only R1 (and biomarker-enriched R2) carries negative biology. REGOBONE/NCT02389244 CIC cohort = results pending, not negative. An annotation on feasibility, not a new axis. |
| Host-level / lifestyle: microbiome, inflammation (NLR/mGPS), metabolic/sarcopenia, nutrition, exercise, sleep/circadian, autonomic/PNEI, placebo-nocebo, perioperative | `host-biology-modifier-layer.md` (0005) | Conditions V4 and SOC tolerability; weighted through the existing three axes. |
| How transfer distance is weighted / is broader evidence excluded because the tumour is rare | `docs/10-evidence-transferability-hierarchy.md` (0014) | Directness ladder P0 CIC-DUX4 → P1 fusion round-cell family → P2 sarcoma → P3 solid tumour with named mechanism → P4 pathway-only. Rarity lowers the rung, never excludes; only a missing mechanistic bridge excludes. Era B: no P0 anchor (§5a). |
| Immune visibility, danger signalling, ICD/DAMPs, Nectin–TIGIT–DNAM-1 / NKG2A–HLA-E, NK surveillance | `v4-immune-watchdog/immune-watchdog-expansion.md` (0006) | Includes NTX1088 anti-PVR and the failed anti-TIGIT phase-3 programs. Apply the inflammation-state lens: tumour-promoting inflammation vs anti-tumour activation vs treatment toxicity — lowering inflammation ≠ improving anti-tumour immunity. |
| Cell of origin / pathogenesis / "how does a cell get into this state" / minimal transformation set | `tumorigenesis-reverse-engineering/` + `sims/07-tumorigenesis-trajectory/` (0007) | The forward "build recipe" (inverse of V1–V4) mapped back onto intervention points. |
| No confirmed fusion / unknown driver / which options are safe without the driver / is resolving it worth it | `tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md` + `sims/08-driver-uncertainty/` (0008) | Driver as latent variable (D1 cryptic CIC-DUX4 … D5 orphan); EVSI: long-read WGS+RNA-seq > DUX4 IHC > methylation array. Throttle / cell-cycle / immune vectors are driver-robust; the DUX4/MCL1 "re-arm" line is driver-contingent (hold). Re-condition the prior on any testing the patient already had. Not a diagnosis. |
| What does the chemo response tell us; chemo-sensitivity/resistance; SLFN11; persister reservoir; when to deploy immunotherapy | `chemosensitivity-ddr-cellstate-layer.md` + `sims/10-chemoresponse-cellstate/` (0021) | Response as evidence via `driver → DDR state → response`; report driver and cell-state posteriors **separately**. Cell state resolves to ~94% while driver entropy *rises*; most-likely driver flips D1→D4 in 75.2% of sweeps; MCL1 "re-arm" drops out in 99.1%; SLFN11 IHC / BH3 profiling ≈ 0 EVSI (the clinical course already bought that information). PRC2/EZH2→SLFN11 makes one node serve V3+V4; persister reservoir ≠ chemo-sensitive bulk (GPX4/ferroptosis; CDK4/6i hits the bulk); the post-chemo MRD window is the best immunological moment and it closes (NK first). Response is confounded with setting — say so. **All citations `[VERIFY]`** → forward lane only (ADR-0020). |
| Reasoning process: clinician steering, red-team / "try to disprove X", debiasing, premature convergence, expanding or contracting the search | `docs/11-hypothesis-steering-and-adversarial-reasoning.md` (0017) | Red-team self-challenge (disconfirm / alternative / flip-test / steer-audit — also in `sarcoma-pre-output-check`). Steering reframes the search but never supplies an evidence tier; contraction never prunes the forward lane. |
| Beyond systemic drugs: cellular (TIL/CAR-T/CAR-NK/TCR), gene/viral, vaccines, local-regional, physical (hyperthermia, HIFU, radiation priming), dietary; drug repurposing; ethnopharmacology / phytotherapy | `therapeutic-modality-layer.md` (0018) | Modality axis M1–M8, orthogonal to the vectors: it moves **feasibility**, never tier or mechanism. Thin spots M3/M4/M6/M7 — **M7 regional hyperthermia** has a positive phase-3 STS RCT. Repurposing and phytotherapy candidates go through tier + Directness + concentration-mismatch + `sarcoma-chemo-interactions`. Junction-specific cellular/vaccine modalities are fusion-contingent. |
| Oncolytic viruses / "make the cold tumour hot with a virus" / a named platform (T-VEC, RP1/2/3, OH2, VG161, pelareorep, NDV, Seneca Valley) | `oncolytic-virotherapy-danger-signal-layer.md` (0019) | OV as an artificial danger-signal generator (visibility axis). One positive sarcoma signal (T-VEC + pembrolizumab ORR 30%, NCT03069378); Ewing/round-cell data show *low* susceptibility and no CIC-DUX4 OV data exist → `Theoretical`; fusion-agnostic; RP1's twice-rejected FDA path and visceral anatomy bound feasibility. Gating experiment: a tropism screen. |
| Refresh the evidence / does a new paper change anything / is finding X still current | Live evidence-refresh lane (0020): dated `evidence-refresh-YYYY-MM.md` | Tier and cite each claim. Snippet/abstract-sourced claims are `[VERIFY]` and may not enter a protocol version until verified against a live source (PubMed/PMC/GEO/registry per `docs/09`), PMID/accession inline, perishable status date-stamped; failures are corrected or **retracted in place** (this caught the 2026-06 WEE1 retraction). A verified refresh may produce the next `protocol-vN.md` on a **user-gated** promotion (update `findings-ranking.md` + README "Where to start"). Symmetric: it can refute as well as confirm. |
| Executed in-silico experiments | `sims/01–10/` (see `sims/00-INDEX.md`) | Each has `RESULTS.md`, a data `MANIFEST.md`, and grounding. |

---

## 1. Golden rules (apply to every output, every agent)

Canonical wording lives in the `sarcoma-contract` skill; this is the summary.

1. **No fabricated citations.** If you can't point to a real PMID / NCT / DOI / dataset, write
   `[no direct citation; mechanism inferred from {what}]`. Plausible-looking fake references are the
   worst failure mode this project has. Verify accessions/PMIDs against live sources when you can; if you
   can't, label the claim `[VERIFY]`. Regulatory/trial/safety status is **perishable** — verify it live and
   never carry it across sessions unchecked (`sarcoma-contract`, `docs/09-verification-sources.md`).
2. **Evidence tier on every claim**, exactly one of: `Established` › `Clinical-Trial` ›
   `Preclinical-Animal` › `Preclinical-Cell` › `Mechanistic` › `Dietary-Observational` › `Theoretical`.
   Tier is the first of three orthogonal axes (tier / confidence / feasibility) — see `sarcoma-contract`.
3. **Mechanism before recommendation.** State the molecular mechanism, not an analogy and not
   "antioxidant properties." The engineering analogy (docs/04) is shorthand — translate it back to biology.
4. **Calibrated confidence; say what you could not establish.** A short, honest output beats a long
   padded one. Every research output has a "what I could not establish" section.
5. **Known research is the floor, not the ceiling.** Don't stop at "X was tried and didn't work" — ask
   why it failed, what is mechanistically different here, whether the trial was underpowered, unselected
   or monotherapy. Generate mechanistically defensible **Forward Hypotheses** with explicit falsifiers,
   tagged `Theoretical`/`Mechanistic` — bold in hypothesis space, never dressed up as evidence. The
   adversarial counterpart (red-team, premature-closure guard) is in `docs/11` (ADR-0017); contraction may
   prune the confirmatory lane but never this one.
6. **Distinguish evidence in this tumour from evidence in cancer broadly.** Flag concentration mismatches
   (a 10 µM cell-line effect ≠ an achievable dietary plasma level).
7. **Flag standard-of-care interactions** (VDC/IE: vincristine, doxorubicin, cyclophosphamide,
   ifosfamide, etoposide; CYP3A4/P-gp; ROS-dependent chemo) with the `sarcoma-chemo-interactions` skill.
8. **The four attack vectors are fixed** (V1 Rate-Limiting, V2 Compiler-Protection, V3 Hot-Patching,
   V4 Immune-Watchdog). New topics are supplementary teams or sub-agents, never a fifth vector.
9. **Driver applicability.** This patient has no confirmed fusion. Flag every fusion-dependent idea
   (junction ASOs, junction-specific vaccines / CAR-T, the MCL1 "re-arm" line) as possibly inapplicable and
   driver-contingent; mark fusion-agnostic ones (epigenetic, BETi, CDK4/6i, differentiation, epigenetic
   MHC-I priming, dietary, immune) as still applicable.
10. **Clinician-facing briefs carry honest clinical status** (approved vs experimental vs failed in trials),
    a "revisit when…" trigger, and "not medical advice."

---

## 2. Gauge the effort before acting

| If the prompt is… | Then… |
|---|---|
| Anything | Read `CASE-BASELINE.md` first. |
| A question an artifact in §0 already answers | Read and cite it (re-weighted per §5a). Don't re-run the cycle. |
| A simple factual / clarifying / "why" question | Just answer. |
| "Analyze X thoroughly," "from multiple angles," "what could be tried," "run a simulation" | Spawn the appropriate existing team (§3) so the topic gets several perspectives. A thorough-sounding question is not automatically a spawn — judge whether multi-angle research adds value. |
| A research question no team fits | Propose a new supplementary team (lead + 2–4 specialists) and spawn only after the user agrees. |
| A coding / repo task (run a sim, fix a script, write a doc) | Do it directly. |

---

## 3. Teams, agents, and sub-agents

The model: a team of specialists attacks a topic from several angles; a lead reconciles (merges
duplicates, keeps the strongest evidence tier — not concatenation) and writes the report. Try an existing
team first.

### Project agents (`.claude/agents/`)

Model and effort are set in each agent's frontmatter; leads pass `model` when they spawn specialists
(ADR-0023).

| Agent | Model | Role | Spawns (parallel) |
|---|---|---|---|
| `v1-lead` | Opus | V1 Rate Limiting | Food, Supplement, Bioavailability (Sonnet) |
| `v2-lead` | Opus | V2 Compiler Protection | Antioxidant, DNA-Repair, Anti-Inflammatory (Sonnet) |
| `v3-lead` | Opus | V3 Hot Patching | Epigenetic, Differentiation, PROTAC/ASO, Synthetic-Lethality (Sonnet) |
| `v4-lead` | Opus | V4 Immune Watchdog | Checkpoint/T-cell, NK, Microbiome-Immune, Neoantigen-Vaccine (Sonnet) |
| `mrna-vaccine-lead` | Sonnet | Supplementary: BNT162b2 immune/inflammatory/genomic relevance | mrna-immune-effects, mrna-oncogenic-risk (optional, Sonnet) |
| `orchestrator` | Fable | Synthesis: dedupe, rank, resolve conflicts, write the catalog | Metastatic-Disease Specialist (Opus) |

Supplementary team without a committed agent file — reuse its artifacts first: **Tumorigenesis /
Cell-of-Origin Reverse-Engineering** (ADR-0007; Cell-of-Origin, Driver-Engineering, Cooperating-Lesions,
Epigenetic-Permissiveness specialists) → `simulation-output/tumorigenesis-reverse-engineering/` +
`sims/07-tumorigenesis-trajectory/`.

### Full-run sequence (fresh cycle only — see §0)

Runs are versioned so nothing is overwritten: run N writes `<vector-dir>/<lead>-summary-vN.md`,
specialist files under `<vector-dir>/vN/`, and `simulation-output/protocol-vN.md`. `scripts/dispatch.py`
derives N (next protocol version; override with `SARCOMA_RUN`) and gates on run-scoped files.
`.prompts/run-sim.prompt` is the patient-anchored launch prompt.

1. `python scripts/dispatch.py` (plan + output paths) and `python scripts/dispatch.py check`.
2. **Layer intake (ADR-0016).** Each lead reads the standing layers in its scope (named in its agent
   file); the orchestrator reconciles against all of them plus `findings-ranking.md` and runs the
   ADR-0018 modality-coverage audit.
3. **Wave 1 (parallel):** `mrna-vaccine-lead`, `v1-lead`, `v3-lead`.
4. **Gate:** `python scripts/dispatch.py gate` — this run's mRNA summary exists and V3's summary has its
   `MHC-I Upregulation Candidates` section.
5. **Wave 2 (parallel):** `v2-lead`, `v4-lead`.
6. **Orchestrator** after `python scripts/dispatch.py ready`; it runs the Metastatic-Disease Specialist and
   writes `protocol-vN.md`.

Each agent loads its skills (§6) and runs `sarcoma-pre-output-check` before writing.

If background sub-agents keep returning with 0 tool uses (transient API overload), run the work directly in
the main thread — same scripts, data, grounding and no-fabrication rule.

When asked for a clean-slate exercise, don't use stored personal memory.

---

## 4. Running the Python simulations

Interpreter: the repo venv at `.venv/bin/python` (from a git worktree, the main checkout's venv). It has
pandas, numpy, scipy, networkx, requests, GEOparse, and `openmed`. `scripts/openmed_ner.py` and
`scripts/dispatch.py` find the venv themselves.

Each sim is run as `.venv/bin/python sims/NN-*/<script>.py`; `sims/00-INDEX.md` lists them with their
convergent findings.

Conventions for a new sim:
- **Real data only.** Cache raw downloads under the sim's own `data/` (gitignored) and write a
  `MANIFEST.md` with source URLs, accession IDs, access date, and sha256. Never invent a dataset, accession,
  gene-effect value, or compound — if a download or API fails, report the failure.
- Write `RESULTS.md` (real numbers + honest limitations), `entities.txt`, and `grounding.tsv` (§5).
- Add a row to `sims/00-INDEX.md` and update `findings-ranking.md` in the same change when the result is
  worth comparing (ADR-0009).
- Isolate experimental runs in a worktree: `git worktree add -b sim-<topic> ../sarcoma-<topic> <base>`.

---

## 5. Grounding with OpenMed NER

Every agent and sim grounds the biomedical entities it names (genes, drugs, diseases) with OpenMed NER
before finalizing — confirming the names are recognized biomedical terms. Grounding is **not**
fact-checking: it cannot tell you a drug was withdrawn or a trial closed (use `docs/09` for that), and it is
not evidence tiering.

```bash
python scripts/openmed_ner.py --list-teams                 # team -> model map (also docs/07)
python scripts/openmed_ner.py --check                      # can grounding run here?
python scripts/openmed_ner.py --team v3-synthetic-lethality \
    --text-file sims/02-dependency-mining/entities.txt --format tsv > grounding.tsv
```

Pick the `--team` whose models fit the entity types (genes/proteins → `v3-synthetic-lethality`;
drugs+genes → `v1-lead`; immune → `v4-lead`) and note any entity NER did not recognize. The CLI is
offline-first (cached weights never touch the Hub) and auto-selects MLX or PyTorch. **Exit code 3** means
the weights aren't cached and huggingface.co is unreachable (typical in network-restricted cloud
sessions): record grounding as `NOT RUN` with the reason, as in
`sims/10-chemoresponse-cellstate/grounding.tsv`, and never invent scores. Fixes are in `docs/07`.

---

## 6. Skills (`.claude/skills/`)

- **`sarcoma-contract`** — tier vocabulary, the three scoring axes, citation + live-verification rules,
  avoid/include lists. Load at the start of any lead / sub-agent / orchestrator task.
- **`sarcoma-vector-context`** (`v1`|`v2`|`v3`|`v4`) — one vector's compounds, targets, caveats.
- **`sarcoma-chemo-interactions`** — screen dietary/supplement candidates against VDC/IE.
- **`sarcoma-output-schema`** `<role>` — the output schema for an agent role.
- **`sarcoma-pre-output-check`** — failure-mode + mandatory-include self-audit and red-team pass; run
  before writing.
- **`sarcoma-orchestrator-intake`** — orchestrator intake / dedupe / rank / conflict protocol.
- **`github-issue-runner`** — the issue workflow (§8).

---

## 7. Repository map

Four audience tiers. Dot-prefixed = Tier 4 (machine/config); plain names are tiered by how human-facing.
`scripts/` is the one un-dotted Tier-4 exception (a documented entry point).

| Tier | Audience | Contents |
|---|---|---|
| **1 — Read first** | Clinicians · patients | `CASE-BASELINE.md` · `simulation-output/protocol-v4.md` (v1–v3 baselines) · `findings-ranking.md` · `chemosensitivity-ddr-cellstate-layer.md` · `forward-simulation/*-brief.md` |
| **2 — Hybrid** | Researchers | rest of `simulation-output/` (layers + per-vector outputs) · `docs/00–05` |
| **3 — Contributor / LLM** | Developers · agents | `docs/06–11` · `docs/adr/` · `sims/` · `CLAUDE.md` · `scripts/` |
| **4 — Machine** | Tooling | `.claude/` · `.prompts/` · `.venv/` · `.gitignore` · gitignored `sims/*/data/` |

Key paths: `docs/06-agent-architecture.md` (full agent prompts + schemas) · `docs/07-openmed-models.md`
(NER map + install/offline) · `docs/08` (confidence axis) · `docs/09` (verification registries) ·
`docs/10` (transferability ladder) · `docs/11` (steering + adversarial reasoning) · `docs/adr/` (decision
log) · `scripts/dispatch.py` (wave plan + gates) · `scripts/openmed_ner.py` (grounding CLI).

---

## 8. GitHub Issues

Issues are the collaboration surface. The **`github-issue-runner` skill** (ADR-0002) owns them: invoked
manually, it processes **one** issue per run — the oldest open issue labeled `needs attention`, else the
oldest labeled none of `running` / `responded` / `needs attention`. It labels it `running`, works in an
isolated worktree off latest `main`, opens a PR assigned to the maintainer, posts a findings comment, then
relabels `responded`.

A nightly Action (`.github/workflows/issue-needs-attention.yml`, ADR-0010/0012) is the one sanctioned piece
of scheduled automation: it moves `responded` → `needs attention` when someone other than
`github-actions[bot]` and the maintainer account comments. It does no analysis itself. Don't improvise
issue handling in general sessions or build other scheduled automation. Use `gh` for GitHub operations.

---

## 9. Conventions

- **Branches:** `sim-*` for simulation/forward work; experimental runs go on their own branch/worktree.
  Don't merge to `main` or push unless asked; don't pollute a state the user likes.
- **Commits:** end messages with the `Co-Authored-By` trailer for the model you are running as.
- **Honesty over completeness.** When in doubt, exclude rather than pad.

### Directory tiering

Every new directory or top-level file gets a tier before it lands on `main`:

| Adding | Tier | Where | Extra step |
|---|---|---|---|
| Catalog, oncologist brief, master register | 1 | `simulation-output/` (or root for an index) | Link it from the README "Where to start" block in the same PR |
| Analytical layer, per-vector summary, VoI file | 2 | `simulation-output/` | — |
| Sim, agent/architecture doc, ADR, evidence reference | 3 | `sims/`, `docs/` | Row in `sims/00-INDEX.md` or `docs/adr/` |
| Scratch, cache, config, secret | 4 | Dot-prefix it or `.gitignore` it | Never in a Tier 1/2 dir |

Don't mass-rename core dirs to add dots — it breaks 130+ path references and `scripts/dispatch.py`; the
README is the navigation layer. Test: would a clinician be confused to see this in the GitHub tree? If yes,
Tier 3/4.

---

## 10. Architecture Decision Records (`docs/adr/`)

CLAUDE.md holds the current rules; the ADR log holds why and when they changed. Read `docs/adr/README.md`
for the rationale behind a rule or before proposing a change that may contradict a past decision. Append a
new ADR (next number, template in the README) for **framework-level** changes — a new standing
deliverable or sim type, a new team or agent, a change to the golden rules / contract / conventions /
agent models, or a notable methodology choice — and update this file to match. Routine work gets no ADR.
