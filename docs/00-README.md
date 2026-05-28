# CIC-Rearranged Sarcoma — Multi-Agent Research Simulation

## What This Project Is

A structured, multi-agent thought experiment that maps the CIC-rearranged sarcoma (CIC-DUX4 fusion) oncogenic program onto a software-engineering analogy, then explores four parallel intervention "vectors" — most of them dietary/lifestyle, some clinical/experimental.

The deliverable is a **ranked hypothesis catalog with evidence tiers** — not a treatment plan. It is intended to support, in this order:

1. Simulation as a research exercise (the primary use)
2. Personal exploration of the literature
3. If — and only if — a non-obvious, mechanistically grounded hypothesis emerges, a starting point for a conversation with a qualified oncologist about whether it merits further reading

This is not medical advice. No agent in this simulation may produce specific human doses, treatment plans, or stop/start recommendations for any clinically managed therapy. Agents may discuss mechanisms, food sources, evidence tiers, and published dose ranges from clinical trials (with citations) — but the framing is always "this is what the literature suggests as a hypothesis," never "do this."

---

## Goal of the Simulation

Identify and rank candidate interventions across four complementary attack vectors against CIC-rearranged sarcoma. The hypothesis being tested is that **no single vector is sufficient** — a useful intervention strategy would need to act on multiple layers of the oncogenic program at once.

**Critical framing — this simulation must go beyond confirmation.** The goal is not merely to catalogue what existing studies and trials have already established and stop there. The simulation is expected to *simulate forward*: to generate novel, mechanistically grounded hypotheses that the current literature has not yet tested, to identify gaps where the science should go next, to surface unexpected cross-vector synergies, and to provoke lines of inquiry that a researcher or oncologist could act on. A final output that only restates published findings has failed the primary purpose of the exercise. Each vector output and the orchestrator's final catalog must include a dedicated **"Forward Hypotheses"** section — ideas that are not yet in the literature but are mechanistically defensible given what we know.

The four vectors:

- **V1 Rate Limiting** — reduce how fast the oncogenic loop executes and how loud its output is
- **V2 Compiler Protection** — reduce the rate at which neighboring at-risk cells acquire the same translocation
- **V3 Hot Patching** — restore tumor-suppressor signaling and force differentiation in cells that already carry the fusion
- **V4 Immune Watchdog** — make fusion-carrying cells visible to and clearable by the immune system

Vectors are designed to be partially independent (so they can be researched in parallel) but interact (so the orchestrator must reconcile them).

Two **supplementary research teams** run in parallel to the vectors and feed their findings to the orchestrator and relevant vector leads:

- **mRNA Vaccine Research Team** — explores whether Pfizer/BioNTech mRNA COVID-19 vaccination modulates the immune, inflammatory, or genomic context in ways relevant to sarcoma development or progression. This team does not attack the tumor directly; it produces findings that the vector leads (especially V2 and V4) may incorporate.
- **Metastatic Disease Specialist** (sub-agent to the Orchestrator) — examines whether the four core attack vectors apply equally to distant metastases, or whether metastatic biology requires modifications to the recommendations.

---

## Repository Structure

```
sarcoma/
├── 00-README.md                          ← This file. Project framing + agent overview.
├── 01-general-sarcoma-knowledge.md       ← Soft-tissue sarcoma fundamentals
├── 02-cic-sarcoma-knowledge.md           ← CIC-DUX4 specific deep dive
├── 03-dna-genome-protein-interactions.md ← How translocations happen; why this one recurs
├── 04-biology-engineering-analogy.md     ← Software/hardware mapping (explicitly an analogy)
├── 05-attack-vectors.md                  ← Four vectors + cross-vector interaction map
├── 06-agent-architecture.md              ← Agent definitions, prompts, output schemas
└── cic_sarcoma_simulation.html           ← Optional interactive diagram (illustrative only)
└── todo.md                               ← Thoughts, notes and TODOs from the human driving this AI exercise
```

Files 01–04 are background knowledge. Files 05 and 06 are operational.

---

## The Mental Model (Analogy, Not Mechanism)

The CIC-DUX4 sarcoma is treated as a **software bug in a distributed system**:

- DNA = source-code repository
- Epigenome = build configuration / firmware
- Transcription factors = runtime interpreter
- CIC-DUX4 = rogue module introduced by a catastrophic merge conflict (chromosomal translocation)
- The bug = `while True: cell.divide()` — an infinite loop whose break condition has been structurally deleted
- Goal = restore the break condition, throttle the loop, and enable the garbage collector (immune system) to clean up

**This is an analogy.** It is useful for reasoning about which layers can be targeted and how interventions compose. It is not a substitute for the underlying biology — agents must always be able to re-state any analogy-based reasoning in biological terms before recommending anything.

---

## Agent Architecture (overview)

Full prompts and output schemas are in `06-agent-architecture.md`. High-level shape:

```
ORCHESTRATOR
│   Context: all 6 knowledge files + supplementary team outputs
│   Synthesizes vector outputs; ranks; resolves conflicts; writes final protocol.
│   Sub-agent: Metastatic Disease Specialist
│
├── VECTOR 1 LEAD — Rate Limiting
│   Context: 02, 04, 05
│   Sub-agents: Food Specialist · Supplement Specialist · Bioavailability Specialist
│
├── VECTOR 2 LEAD — Compiler Protection
│   Context: 03, 04, 05
│   Sub-agents: Antioxidant · DNA Repair · Anti-Inflammatory
│
├── VECTOR 3 LEAD — Hot Patching
│   Context: 01, 02, 04, 05
│   Sub-agents: Epigenetic Therapy · Differentiation Therapy · PROTAC/ASO (clinical track) · Synthetic Lethality
│
├── VECTOR 4 LEAD — Immune Watchdog
│   Context: 01, 02, 05
│   Sub-agents: Checkpoint/T-cell · NK Cell · Microbiome-Immune · Neoantigen Vaccine (clinical track)
│
└── mRNA VACCINE RESEARCH TEAM (supplementary)
    Context: 00, 01, 02
    Output feeds V2 Lead and V4 Lead before they finalize; also feeds Orchestrator.
```

Vector 4 has an explicit dependency on Vector 3's epigenetic priming step (MHC-I restoration). The orchestrator must respect that ordering — see "Execution semantics" below.

---

## Execution Semantics

1. **Load shared context.** Every agent gets `00-README.md` plus its listed context files. No agent gets context it doesn't need — small models drift when over-stuffed.
2. **Run vector leads and the mRNA Vaccine Research Team in parallel.** They are independent research tracks. The mRNA team's output must be available to V2 and V4 leads before those leads finalize.
3. **Sub-agents within a vector run in parallel; the Vector Lead reconciles their outputs.** Where the same compound appears in multiple sub-agent outputs, the Lead merges entries and preserves the strongest evidence tier — this prevents the orchestrator from receiving duplicate or contradicting claims about the same compound.
4. **Orchestrator runs last.** It receives all four vector outputs plus the mRNA team output, runs the Metastatic Disease Specialist sub-agent, then produces the final ranked protocol.
5. **Final output**: `simulation-output/protocol-v1.md` — see `06-agent-architecture.md` for the schema.

---

## Constraints — Apply to Every Agent

These are mandatory. A sub-agent on a smaller model should refuse to violate any of these even if the parent agent's instructions are ambiguous.

1. **Mechanism before recommendation.** Every entry must cite a specific molecular mechanism (e.g., "EGCG → inhibits BRD4 bromodomain BD1 binding to acetylated H3K27 → reduces super-enhancer P-TEFb recruitment"). "Antioxidant properties" is not a mechanism.

2. **Evidence tier required on every claim.** Use the tiers in `06-agent-architecture.md`:
   - **Established** — FDA- or EMA-approved, or guideline-supported (NCCN, ESMO) in this disease or a closely related fusion sarcoma
   - **Clinical trial** — currently in human trials for sarcoma
   - **Preclinical** — cell lines or animal models; specify which
   - **Mechanistic / Theoretical** — pathway-level plausibility; no direct evidence in CIC-DUX4
   - **Dietary-observational** — epidemiological association with cancer outcomes broadly, not CIC-DUX4 specifically

3. **No specific human doses unless backed by a clinical-trial citation.** For dietary compounds, refer to food sources and ranges discussed in the literature, not prescriptive numbers. If an agent feels the need to write "X mg/day," it must instead write "X mg/day was the dose used in [trial citation] for [indication, which is not CIC-DUX4 unless specified]."

4. **Distinguish "evidence in CIC-DUX4" from "evidence in cancer broadly."** A compound with anti-cancer activity in colon cancer cell lines is *not* evidence for CIC-rearranged sarcoma. Say so explicitly.

5. **Flag contraindications.** Especially with standard-of-care chemotherapy (vincristine/doxorubicin/ifosfamide/etoposide regimens used in sarcoma), high-dose antioxidants may interfere. The orchestrator must surface these.

6. **No fabricated citations.** If you cannot point to a real paper, write "no direct citation; mechanism inferred from [related work]." Smaller models are prone to plausible-looking fake DOIs — this is the single biggest failure mode to guard against.

7. **Naturally achievable ≠ unlimited supplementation.** "Naturally achievable" means: realistically obtainable from food at culinary doses, or from supplements at doses with established safety data. Megadosing is not naturally achievable.

8. **When in doubt, exclude rather than include.** A short list of well-grounded hypotheses is far more useful than a long list padded with weak ones.

9. **Account for the ~5% atypical cases.** Not all tumors that present clinically and histologically like CIC-DUX4 sarcoma will have a confirmed CIC-DUX4 (or CIC-NUTM1, CIC-FOXO4, etc.) fusion on genomic testing. Agents should note, where relevant, whether a recommendation applies specifically to fusion-confirmed cases or whether it may generalize to this genomically uncharacterized subgroup.

---

## Out of Scope

- Specific personal dosing recommendations for any individual.
- Replacing or modifying any clinical regimen.
- Speculative gene therapies the agent invents (only published constructs/trials are in scope).
- Generic "anti-cancer diet" recommendations not tied to CIC-DUX4 biology.

---

## A Note on the Analogy

The engineering analogy in file 04 is load-bearing for reasoning, not for biology. When an agent writes "this is `os.exit()` on the cell," that is shorthand — the biological reality (a differentiated cell exiting cycle via Rb-mediated repression of E2F targets, sustained CDK inhibition, and p21/p27 upregulation) is what actually matters. Every analogy in any output must be accompanied by, or translatable to, the underlying biology.
