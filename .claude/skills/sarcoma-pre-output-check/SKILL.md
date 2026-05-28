---
name: sarcoma-pre-output-check
description: Pre-flight self-audit a sub-agent or vector lead runs BEFORE finalizing its output in the CIC-rearranged sarcoma simulation. Walks through 8 failure modes (citation fabrication, concentration-mismatch, dose invention, etc.) and 8 mandatory-include items. Catches errors before they reach the orchestrator. Invoke as the second-to-last step of any agent task, immediately before writing the output file.
---

# Pre-Output Self-Audit

Walk through every numbered check below. For each one, answer **yes/no/N-A** in your internal scratchpad. If any answer is **no**, fix the output before writing it. **Do not skip this skill** — the orchestrator depends on it.

## Part A — 8 Failure Modes to Guard Against

These are the failure modes most likely from a Sonnet-tier model. Guard your own output and flag them when reviewing others' outputs.

1. **Citation fabrication.** For every citation in my output, can I point to a real PMID, NCT ID, FDA label, or recognized guideline? If not, did I write `[no direct citation; mechanism inferred from {related work}]` instead? ("Smith et al., 2019" with no PMID is a fabrication risk.)

2. **Concentration mismatch.** For every "X inhibits Y" claim, did I state the concentration and the assay system (cell line vs. animal vs. human plasma)? Example: an EGCG → BRD4 binding claim must specify whether the cited concentration (e.g., 50 µM in HEK293) is achievable in tumor tissue from dietary intake (typically 0.1–0.5 µM at best).

3. **Cancer-class generalization.** For every compound, did I distinguish "evidence in CIC-DUX4 specifically" (almost always `None direct`) from "evidence in cancer broadly"? "Curcumin is anti-cancer" is not a valid claim — for which cancer, dose, in vivo or in vitro?

4. **Analogy-as-evidence drift.** Did I restate any engineering-analogy reasoning ("hot-patch the running cell", "throttle the loop") in biological terms? The biology must stand on its own.

5. **Dose invention.** For any "X mg/day" number in my output, can I cite the exact trial (NCT + indication) where that dose was used? If not, I must replace with food-source language or trial-range language.

6. **"Natural" treated as "safe".** Have I flagged the harm signals where applicable? β-carotene supplementation harms smokers (ATBC, CARET) · Vitamin E in SELECT · selenium's narrow window · NAC accelerated metastasis in Sayin 2014 mouse melanoma model.

7. **Chemotherapy interactions.** Did I check every dietary/supplement recommendation against the SOC chemo regimen for CIC-rearranged sarcoma (VDC/IE — vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide)? If any compound has a documented CYP3A4 / CYP2C9 / P-gp interaction or ROS-axis interference, I must flag it. (Use `/sarcoma-chemo-interactions` for the scaffolding.)

8. **Padding for length.** A shorter output that is well-grounded beats a long padded one. Did I remove entries I cannot defend? When in doubt, **exclude** rather than include.

## Part B — 8 Mandatory-Include Items

Every output must have all eight. Scan and confirm.

1. **One-line summary** at the top stating what this output covers AND what it deliberately excludes.

2. **Confidence line** — "Confidence: high / medium / low — [1 sentence why]."

3. **Per-entry evidence tier** using the vocabulary from `/sarcoma-contract` (Established · Clinical-Trial · Preclinical-Animal · Preclinical-Cell · Mechanistic · Dietary-Observational · Theoretical). For Established-tier entries, FDA and EMA status are both cited where they differ; where only one authority has acted, that fact is stated explicitly.

4. **Per-entry mechanism statement** — molecular, not analogical. ("Inhibits BRD4 BD1 binding to acetylated H3K27" — not "throttles the amplifier".)

5. **Per-entry "evidence in CIC-DUX4 specifically?"** — usually `None direct`; say so.

6. **A "What I Could Not Establish" section** — gaps, unresolved questions, weaknesses the orchestrator should know about. The point of this simulation is calibrated honesty over completeness.

7. **A "Forward Hypotheses" section** — at least **two** mechanistically defensible ideas not yet in the literature. Each entry labeled `[Forward Hypothesis]` with: hypothesis statement, mechanistic basis, what experiment or study design would test it, and (if known) why it has not yet been tested. The simulation's primary purpose is to *simulate forward*, not to restate existing findings — an output without this section is incomplete.

8. **Atypical-case note where relevant.** For any recommendation that critically depends on the CIC-DUX4 (or CIC-NUTM1, CIC-FOXO4) fusion protein being present — ASO design, junction-specific neoantigen vaccines, fusion-junction CAR-T — flag that ~5% of clinically and histologically similar cases will not have a confirmed fusion on genomic testing and the recommendation will not apply to them. For fusion-agnostic recommendations (general epigenetic reprogramming, immune checkpoint approaches), note that they may apply to atypical cases as well.

## Part C — Role-Specific Mandatory Sections

If you are the **V3 lead or V3 Epigenetic Therapy Specialist**: a dedicated "MHC-I upregulation candidates" section at the **top** of your output, for the V4 lead and orchestrator. This is the V3 → V4 bridge.

If you are the **V3 PROTAC/ASO Specialist** or **V4 Neoantigen Vaccine Specialist**: tag the entire output `Clinical / Experimental — not naturally achievable; for awareness only.`

If you are the **V1 Bioavailability Specialist**: the curcumin + piperine entry must reproduce the Shoba 1998 caveat (n=10, single dose, control below LOD) — the "2000% boost" figure is to be cited with that caveat, not as a universal multiplier.

If you are the **V2 Antioxidant Specialist**: include a `DO NOT RECOMMEND` section enumerating the high-dose supplement interventions the literature contraindicates.

If you are the **Orchestrator**: separate the **Naturally Achievable Track** and the **Clinical / Experimental Track**; produce the **Standard-of-Care Interaction Map**; surface conflicts explicitly rather than papering over them.

## Final Check Before Writing

Read back your draft. If a future researcher cited your output as the source for a claim, would the citation chain hold? If not, mark the claim weaker (lower tier) or remove it.
