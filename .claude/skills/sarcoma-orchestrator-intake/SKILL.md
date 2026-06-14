---
name: sarcoma-orchestrator-intake
description: Orchestrator-only synthesis guide for the CIC-rearranged sarcoma simulation. Provides the intake algorithm, deduplication rule, ranking order, conflict-resolution protocol, and contraindication-handling rules used to merge the four vector outputs into the final hypothesis catalog. Replaces the orchestrator's otherwise-redundant full load of 06-agent-architecture.md. Invoke at the start of any orchestrator task.
---

# Orchestrator Synthesis Guide

You coordinate four specialist Vector Team Leads:
**V1 Rate Limiting · V2 Compiler Protection · V3 Hot Patching · V4 Immune Watchdog.**

You also receive input from the **mRNA Vaccine Research Team** (supplementary), and you launch the **Metastatic Disease Specialist** as a sub-agent during your synthesis.

You receive these outputs and produce ONE final document — a hypothesis catalog, not a treatment plan. The audience is:
1. The user as a research-exercise output.
2. The user for personal exploration of the literature.
3. Possibly used as a conversation starter with a qualified oncologist **only if** a non-obvious, mechanistically grounded hypothesis emerges.

**Mandatory tone: epistemically humble.** Most claims will be Mechanistic or Preclinical-Cell tier. Say so. The value of the output is in the structure and the honest grounding — not the number of entries.

**Critical — primary purpose is forward simulation, not confirmation.** Do not produce an output that only restates what existing trials and studies have already established. That is the floor, not the ceiling. Your final catalog must identify gaps, generate mechanistically defensible hypotheses not currently in the literature, and provoke lines of inquiry that could meaningfully advance research. The Forward Hypotheses sections from each vector and the Metastatic Specialist are your raw material — curate, rank, and present the most compelling ones prominently.

---

## Intake Algorithm — Run in This Order

### 1. INTAKE
Read all four vector outputs **and the mRNA Vaccine Research Team output** end-to-end before doing anything else. Note which sub-agent outputs were consolidated into each vector summary (this matters when a claim conflicts). Confirm the V2 and V4 leads have incorporated mRNA team findings into their summaries — they are required to per the execution semantics. If a vector summary is missing required sections (Forward Hypotheses, atypical-case note), flag it and either request the missing content or note the gap in "Conflicts and Open Questions."

### 1B. INGEST STANDING ANALYTICAL LAYERS (ADR-0016)

Before deduplicating, read the **standing analytical layers** the issue thread added on top of the original
run, and reconcile the catalog against them. These are **cross-cutting layers, not a fifth vector** — they
**condition and annotate** the catalog; they **never override real-data vector evidence** (do not promote a
logic/decision-model finding above a real-data one — the `findings-ranking.md` bias note) and **never prune
the Forward-Hypotheses lane**.

| Layer (read end-to-end) | ADR | What it contributes to the final catalog |
|---|---|---|
| `simulation-output/biomarker-voi-stratification.md` + `biomarker-voi-provenance-extension.md` | 0001 / 0011 | Missing-data taxonomy (Known / obtainable-decision-relevant / low-impact) + VoI ranking of unknown biomarkers + where each answer lives (provenance P1/P2/P3, timepoint T0/T1/TΔ). → feeds the **Missing-Data / VoI / Diagnostic Strategy** section. |
| `simulation-output/diagnostic-information-gain-layer.md` | 0015 | Test-level "**what to learn next**": rank each diagnostic *action* by value-profile ÷ acquisition burden, the constraint-aware sequencing rule, and the action-level **low-yield** register. → same section. |
| `simulation-output/translational-feasibility-layer.md` + `feasibility-attrition-reason-extension.md` | 0003 / 0013 | F-band (F1–F5) + attrition-reason (R0–R5) annotations on **every Clinical/Experimental entry**; "discontinued ≠ biologically invalidated" (only R1/enriched-R2 carries negative biology). **Re-verify perishable status live.** |
| `simulation-output/host-biology-modifier-layer.md` | 0005 | Host-biology / treatment-response modifiers (microbiome/SCFA, inflammation/NLR, metabolic/sarcopenia, nutrition, activity, sleep/circadian, autonomic/PNEI, perioperative). → the **Host-Biology Modifiers** section; conditions V4 + SOC tolerability. |
| `simulation-output/v4-immune-watchdog/immune-watchdog-expansion.md` | 0006 | Danger-signaling / ICD / DAMPs, Nectin–TIGIT–DNAM-1 / NKG2A-HLA-E axis, NK surveillance, and the inflammation-state lens (tumor-promoting vs anti-tumor vs toxicity). Verify V4 already consumed it; integrate at catalog level if not. |
| `docs/10-evidence-transferability-hierarchy.md` | 0014 | Confidence **Directness** rung (P0 CIC-DUX4 → P4 pathway-only) on transferred evidence — already enters via `sarcoma-contract`; surface the rung where a ranking turns on transfer distance. |
| `simulation-output/tumorigenesis-reverse-engineering/` + `driver-uncertainty-specialist.md` | 0007 / 0008 | Build-recipe forward hypotheses, and the **driver-uncertainty contingency** for the fusion-unconfirmed case: throttle/cell-cycle/immune vectors are driver-robust; the **MCL1 "re-arm" + junction-specific lines are driver-contingent — hold until the driver is resolved**, and flag resolving the driver as the highest-value next action (EVSI). |
| `simulation-output/therapeutic-modality-layer.md` | 0018 | The **modality axis (M1–M8)** — delivery format, orthogonal to the four vectors (not a fifth vector). Run a **modality-coverage audit**: tag each catalog entry with its M-class and flag any vector whose hypotheses collapse into one or two formats (the systemic-pharmacology default). Modality moves the **feasibility** annotation, never the evidence tier. Surface the M3/M4/M6/M7 gaps (esp. **M7 regional hyperthermia**, positive phase-3 STS RCT) in the forward lane. Apply the repurposing & ethnopharmacology sub-scans' gauntlet (tier + Directness + concentration-mismatch + chemo-interaction) to any candidate sourced that way. |
| `simulation-output/findings-ranking.md` | 0009 | The master register — reconcile every catalog finding against it and **add/update rows** in the same change (its Maintenance rule). |

**On a fresh re-run, write the catalog to the next version (`protocol-v2.md`/`-vN.md`), not over the prior
baseline (`CLAUDE.md §0`).**

### 2. DEDUPLICATE
Many compounds appear in multiple vectors (Quercetin in V1+V2; sulforaphane in V1/V3/V4; omega-3 across V1/V2/V4). For each duplicate:

- Merge into a single entry.
- **Preserve the strongest evidence tier** seen across vectors (Established > Clinical-Trial > Preclinical-Animal > Preclinical-Cell > Mechanistic > Dietary-Observational > Theoretical).
- Preserve all distinct mechanisms (one compound may have a different mechanism in V1 vs V4 — list both).
- Track all vectors the compound is active in (this feeds the Cross-Vector Synergies section).
- Inherit the strongest contraindication flag.

### 3. RANK

Apply these criteria, in this order:

a) **Evidence tier** (highest first).
b) **Mechanistic alignment with CIC-DUX4 biology specifically** — not generic cancer biology. A compound with strong evidence in colon cancer and a weak transfer to CIC-DUX4 ranks lower than one with weaker evidence but more direct mechanistic alignment.
c) **Cross-vector synergy** — among entries at the same tier, compounds active across multiple vectors rank higher.
d) **Safety / feasibility** — dietary > supplement > clinical, within the same tier and CIC-DUX4 alignment band.

Annotate each Clinical/Experimental entry with its **feasibility F-band + attrition R-reason** (ADR-0003/0013,
**re-verify live**) and, where a ranking turns on transferred evidence, its **Directness rung** (ADR-0014).
For the fusion-unconfirmed case, mark the **MCL1 "re-arm" and junction-specific entries as driver-contingent
(hold until the driver is resolved)** per the driver-uncertainty model (ADR-0008) — do not rank them as if
the driver were known.

### 4. RESOLVE CONFLICTS

Where two vectors recommend opposing things, surface the conflict explicitly. Do not paper over it. This
is the orchestrator-level **red-team** pass (`docs/11-hypothesis-steering-and-adversarial-reasoning.md`,
ADR-0017): challenge each high-leverage finding (would it change a top-tier ranking or a clinician-facing
brief?) — run the flip-test on its load-bearing assumption and tag it **assumption-/driver-contingent** if
it does not survive (the fusion-contingent MCL1/junction entries are the worked example, ADR-0008). The
canonical conflicts you should expect to see:

- **Antioxidants vs. ROS-dependent chemo.** V2 recommends antioxidant support; SOC chemo (doxorubicin, ifosfamide) uses ROS. State both, name the regimen, defer the decision to clinical judgment.
- **β-carotene supplementation.** V3 may surface it for retinoid signaling; V2 must flag ATBC/CARET harm in smokers. Carry both flags.
- **NAC.** V2 may surface as glutathione precursor; Sayin 2014 mouse melanoma metastasis signal counter-flags. Carry both.
- **High-dose vitamin E / selenium.** SELECT trial and selenium's narrow window. Carry the harm signal.
- **Probiotics during cancer therapy.** V4 may surface for microbiome modulation; some CPI-response trials show reduced response with broad probiotics. Carry the caveat.

### 5. FLAG CONTRAINDICATIONS WITH STANDARD-OF-CARE — non-negotiable

SOC for CIC-rearranged sarcoma is typically Ewing-like multi-agent chemo (vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide) plus surgery and radiation. Every dietary recommendation that reaches the final catalog must carry the orchestrator-level annotation:

> "Potential interactions with standard-of-care chemotherapy and concurrent medications — must be reviewed by the patient's oncologist before any change."

Compounds with documented CYP3A4 / CYP2C9 / P-gp / ROS-axis interactions get an additional specific flag in the Standard-of-Care Interaction Map. (Use `/sarcoma-chemo-interactions` for the screening framework.)

### 6. SEPARATE TRACKS — keep these clean

a) **Naturally Achievable Track** — dietary, lifestyle, well-established supplements at safe doses. This is what the user can act on directly (with oncologist review).

b) **Clinical / Experimental Track** — for awareness only. This includes EZH2i, BETi, CDK4/6i, PROTACs, ASOs, neoantigen vaccines, CAR-T, checkpoint inhibitors. Requires oncologist.

Do not blur the two. A dietary "weak HDAC modulator" (sulforaphane) does not equal a clinical HDAC inhibitor — same target, different track.

### 7. INCORPORATE mRNA VACCINE TEAM FINDINGS

The mRNA team output has its own dedicated section in the final catalog. If the team surfaced any immune, inflammatory, or genomic modulation potentially relevant to sarcoma biology, also integrate those findings into the appropriate vector sections (typically V2 and V4) and cross-reference them. If the team found no relevant effect, **state that explicitly** rather than omitting the section — a null finding is a complete finding.

### 8. RUN THE METASTATIC DISEASE SPECIALIST SUB-AGENT

After steps 1–7 produce a stable view of the catalog, launch the Metastatic Disease Specialist as a sub-agent (see `06-agent-architecture.md` § "ORCHESTRATOR SUB-AGENT: Metastatic Disease Specialist", or `/sarcoma-output-schema metastatic-specialist` for the schema). Pass it the four Vector Lead summaries and the mRNA team output as input — **not** the full sub-agent outputs. Incorporate its `simulation-output/metastatic-disease-considerations.md` as the "Metastatic Disease Considerations" section of the final protocol.

### 9. REGULATORY COVERAGE — FDA + EMA

For every Established-tier intervention in the Clinical / Experimental Track, cite both **FDA** and **EMA** status. Where they differ (e.g., tazemetostat for epithelioid sarcoma — FDA accelerated approval 2020-01-23, EMA status separate and must be verified), surface both. Where only one authority has acted, say so explicitly — a compound FDA-approved but not EMA-approved (or vice versa) has a different practical access profile for patients in different jurisdictions.

### 10. CURATE FORWARD HYPOTHESES

Each vector lead and the Metastatic Specialist were required to produce ≥2 Forward Hypotheses. Curate across all of them: deduplicate near-duplicates, rank by biological plausibility and research feasibility, and surface the strongest in the catalog's "Forward Hypotheses" section. **An orchestrator output without curated forward hypotheses has failed the simulation's primary purpose** — restating existing findings is the floor, not the ceiling. **Also draw on the standing layers (step 1B):** the tumorigenesis build-recipe forward hypotheses (ADR-0007), the diagnostic "what to learn next" / VoI next-actions (ADR-0015/0001 — including resolving the driver, ADR-0008), and any host-biology forward hypotheses (ADR-0005). Layers expand the forward lane; they never prune it.

### 11. CITATION DOUBLE-CHECK

Before writing the final document, scan every citation for fabrication risk. The most common Sonnet-tier failure mode is a plausible-looking "Smith et al., 2019" with no real PMID. If you cannot verify a citation, demote it to `[no direct citation; mechanism inferred from {description}]` or remove the claim entirely. This check is **mandatory** for the orchestrator — sub-agents may have missed it.

### 12. WRITE FINAL PROTOCOL

Use the orchestrator output schema. Invoke `/sarcoma-output-schema` with argument `orchestrator` for the exact structure.

---

## Cross-Vector Synergy Notes (Pre-known Patterns)

These are documented synergies in the source material that the orchestrator should expect to see and amplify in the catalog:

- **V1 ↔ V2:** Many compounds (Quercetin, Omega-3, Selenium, Zinc) hit both. Reducing transcriptional load (V1) reduces Topo II DSBs at active loci (V2).
- **V3 → V4 bridge (mandatory section):** EZH2i and clinical HDACi restore MHC-I → enables V4 immune clearance. Dietary analogues (sulforaphane, butyrate) are weaker; flag the exposure-mismatch honestly.
- **V1 ↔ V3 (downstream):** CDK4/6 axis (V1.C) overlaps with V3 clinical CDK4/6 inhibitors — same target, different track.
- **V4 NK arm:** NK cells target MHC-I-LOW cells, which is the same evasion mechanism CIC-DUX4 cells use against T-cells. This is a non-obvious therapeutic angle and belongs in the Top-Level Findings if it survives the evidence-tier check.

## Sub-Agent Failure Modes the Orchestrator Must Catch

Sub-agents on Sonnet-tier models often produce these failures. Scan for them:

1. **Fabricated citations** (highest priority).
2. **Concentration mismatch** — cell-line concentrations presented without noting they're unachievable from diet.
3. **Cancer-class generalization** — "anti-cancer" claims without specifying cancer or context.
4. **Analogy-as-evidence drift** — "hot-patches the cell", "throttles the loop" without biology.
5. **Dose invention** — "X mg/day" without trial citation.
6. **"Natural" = "safe"** — missing ATBC/CARET, SELECT, NAC/Sayin flags.
7. **Ignored chemo interactions.**
8. **Padding for length** — long lists of weakly-supported entries.

When you catch one, fix the entry (downgrade tier, add caveat, remove) and note in the orchestrator's "Conflicts and Open Questions" section that the sub-agent's claim was adjusted.

## Bibliography Discipline

Every citation in the final catalog must be verifiable. Build the Bibliography section as you write, not at the end. Re-verify each one before publishing.

## Final Reminder

A short, well-grounded catalog is the win condition. Padding lowers the orchestrator's credibility and makes the output less useful to its intended audience. When in doubt, **exclude**.
