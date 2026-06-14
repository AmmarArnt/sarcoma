---
name: sarcoma-pre-output-check
description: Pre-flight self-audit a sub-agent or vector lead runs BEFORE finalizing its output in the CIC-rearranged sarcoma simulation. Walks through 9 failure modes (citation fabrication, concentration-mismatch, dose invention, stale regulatory status, etc.), 9 mandatory-include items, and a one-pass red-team self-challenge (disconfirm / alternative / flip-test / steer-audit; ADR-0017). Catches errors before they reach the orchestrator. Invoke as the second-to-last step of any agent task, immediately before writing the output file.
---

# Pre-Output Self-Audit

Walk through every numbered check below. For each one, answer **yes/no/N-A** in your internal scratchpad. If any answer is **no**, fix the output before writing it. **Do not skip this skill** — the orchestrator depends on it.

## Part A — 9 Failure Modes to Guard Against

These are the failure modes most likely from a Sonnet-tier model. Guard your own output and flag them when reviewing others' outputs.

1. **Citation fabrication.** For every citation in my output, can I point to a real PMID, NCT ID, FDA label, or recognized guideline? If not, did I write `[no direct citation; mechanism inferred from {related work}]` instead? ("Smith et al., 2019" with no PMID is a fabrication risk.)

2. **Concentration mismatch.** For every "X inhibits Y" claim, did I state the concentration and the assay system (cell line vs. animal vs. human plasma)? Example: an EGCG → BRD4 binding claim must specify whether the cited concentration (e.g., 50 µM in HEK293) is achievable in tumor tissue from dietary intake (typically 0.1–0.5 µM at best).

3. **Cancer-class generalization.** For every compound, did I distinguish "evidence in CIC-DUX4 specifically" (almost always `None direct`) from "evidence in cancer broadly"? "Curcumin is anti-cancer" is not a valid claim — for which cancer, dose, in vivo or in vitro?

4. **Analogy-as-evidence drift.** Did I restate any engineering-analogy reasoning ("hot-patch the running cell", "throttle the loop") in biological terms? The biology must stand on its own.

5. **Dose invention.** For any "X mg/day" number in my output, can I cite the exact trial (NCT + indication) where that dose was used? If not, I must replace with food-source language or trial-range language.

6. **"Natural" treated as "safe".** Have I flagged the harm signals where applicable? β-carotene supplementation harms smokers (ATBC, CARET) · Vitamin E in SELECT · selenium's narrow window · NAC accelerated metastasis in Sayin 2014 mouse melanoma model.

7. **Chemotherapy interactions.** Did I check every dietary/supplement recommendation against the SOC chemo regimen for CIC-rearranged sarcoma (VDC/IE — vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide)? If any compound has a documented CYP3A4 / CYP2C9 / P-gp interaction or ROS-axis interference, I must flag it. (Use `/sarcoma-chemo-interactions` for the scaffolding.)

8. **Padding for length.** A shorter output that is well-grounded beats a long padded one. Did I remove entries I cannot defend? When in doubt, **exclude** rather than include.

9. **Stale regulatory / trial / feasibility status.** For every "approved / recruiting / discontinued / on-hold / withdrawn" claim, did I verify it **live this session** against the authoritative registries in `docs/09-verification-sources.md` (ClinicalTrials.gov, EU CTIS, Drugs@FDA, EMA, PMDA), record the source + access date, and check the right jurisdiction (FDA ≠ EMA ≠ PMDA)? A status carried over from an older artifact or a prior session without re-checking is a fabrication risk — approvals get withdrawn and trials close without any change in biology. If I could not confirm, did I tag `[VERIFY]` instead of asserting it?

## Part B — 9 Mandatory-Include Items

Every output must have all nine. Scan and confirm.

1. **One-line summary** at the top stating what this output covers AND what it deliberately excludes.

2. **Confidence line** — "Confidence: high / medium / low — [1 sentence why]."

3. **Per-entry evidence tier** using the vocabulary from `/sarcoma-contract` (Established · Clinical-Trial · Preclinical-Animal · Preclinical-Cell · Mechanistic · Dietary-Observational · Theoretical). For Established-tier entries, FDA and EMA status are both cited where they differ; where only one authority has acted, that fact is stated explicitly.

4. **Per-entry mechanism statement** — molecular, not analogical. ("Inhibits BRD4 BD1 binding to acetylated H3K27" — not "throttles the amplifier".)

5. **Per-entry "evidence in CIC-DUX4 specifically?"** — usually `None direct`; say so.

6. **A "What I Could Not Establish" section** — gaps, unresolved questions, weaknesses the orchestrator should know about. The point of this simulation is calibrated honesty over completeness.

7. **A "Forward Hypotheses" section** — at least **two** mechanistically defensible ideas not yet in the literature. Each entry labeled `[Forward Hypothesis]` with: hypothesis statement, mechanistic basis, what experiment or study design would test it, and (if known) why it has not yet been tested. The simulation's primary purpose is to *simulate forward*, not to restate existing findings — an output without this section is incomplete.

8. **Atypical-case note where relevant.** For any recommendation that critically depends on the CIC-DUX4 (or CIC-NUTM1, CIC-FOXO4) fusion protein being present — ASO design, junction-specific neoantigen vaccines, fusion-junction CAR-T — flag that ~5% of clinically and histologically similar cases will not have a confirmed fusion on genomic testing and the recommendation will not apply to them. For fusion-agnostic recommendations (general epigenetic reprogramming, immune checkpoint approaches), note that they may apply to atypical cases as well.

9. **Scoring axes beyond tier, where they apply.** Tier alone is not sufficient (see `/sarcoma-contract` → "Three Scoring Axes"). Did I add a **confidence** read (Directness / in-vivo Achievability / Reproducibility / conflict — `docs/08-evidence-confidence-scoring.md`) where a tier could mislead, and a **feasibility band** (F1–F5; `simulation-output/translational-feasibility-layer.md`) on any **clinical/experimental** entry whose practical access matters? And did I keep the **two-lane rule** — these axes annotate the confirmatory lane but never prune the Forward-Hypotheses lane (golden rule #5)?

## Part C — Role-Specific Mandatory Sections

If you are the **V3 lead or V3 Epigenetic Therapy Specialist**: a dedicated "MHC-I upregulation candidates" section at the **top** of your output, for the V4 lead and orchestrator. This is the V3 → V4 bridge.

If you are the **V3 PROTAC/ASO Specialist** or **V4 Neoantigen Vaccine Specialist**: tag the entire output `Clinical / Experimental — not naturally achievable; for awareness only.`

If you are the **V1 Bioavailability Specialist**: the curcumin + piperine entry must reproduce the Shoba 1998 caveat (n=10, single dose, control below LOD) — the "2000% boost" figure is to be cited with that caveat, not as a universal multiplier.

If you are the **V2 Antioxidant Specialist**: include a `DO NOT RECOMMEND` section enumerating the high-dose supplement interventions the literature contraindicates.

If you are the **Orchestrator**: separate the **Naturally Achievable Track** and the **Clinical / Experimental Track**; produce the **Standard-of-Care Interaction Map**; surface conflicts explicitly rather than papering over them.

## Part D — Red-Team Self-Challenge (one pass, mandatory)

Before writing, run a single adversarial pass against your **own** leading hypothesis (the
reasoning-bias counterpart to Part A's evidence-hygiene checks). This is the standing red-team step from
`docs/11-hypothesis-steering-and-adversarial-reasoning.md` (ADR-0017) — the machine analogue of
Chain-of-Verification and Croskerry's "cognitive forcing function." Keep it to a few lines; record the
results in your "What I Could Not Establish" section.

1. **Load-bearing assumption.** Name the one input whose being-wrong would most change your conclusion.
2. **Disconfirmation.** What is the strongest *published* evidence *against* the leading hypothesis — and did
   I search for it as hard as for the supporting evidence? (counters confirmation bias)
3. **Alternative.** What is the best hypothesis that fits the same data but sits *outside* my vector/lane?
   If it names a real mechanism that fits none of V1–V4, flag it for a possible supplementary team
   (do not force it into an existing vector). (counters anchoring)
4. **Flip test.** If the load-bearing assumption (1) is wrong, does the conclusion survive? If not, tag the
   entry **assumption-/driver-contingent** (as ADR-0008 tags fusion-contingent entries).
5. **Steer audit.** If a human steer (an issue, a prompt) pointed me here, am I *confirming* it or *testing*
   it? A steer reframes the search; it does **not** supply an evidence tier. (counters sycophancy)

If any answer exposes a weakness, fix the entry (downgrade tier, add the contingency tag, add the
alternative) before writing. Do not let the red-team pass induce over-hedging — one pass, then proceed.

## Final Check Before Writing

Read back your draft. If a future researcher cited your output as the source for a claim, would the citation chain hold? If not, mark the claim weaker (lower tier) or remove it.
