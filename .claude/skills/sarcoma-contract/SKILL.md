---
name: sarcoma-contract
description: Shared behavioral contract for every agent in the CIC-rearranged sarcoma simulation. Invoke this skill at the start of any vector-lead, sub-agent, or orchestrator task to load the Evidence Tier vocabulary, citation rules, and the mandatory avoid/include lists. Replaces the duplicated rule content otherwise spread across 00-README.md and 06-agent-architecture.md.
---

# Shared Behavioral Contract (Every Agent Reads This)

## Evidence Tier Vocabulary (Mandatory)

Every claim or recommendation must carry **exactly one** of these tags:

| Tier | Meaning |
|---|---|
| **Established** | FDA-approved or major-guideline-supported in this disease, OR in a closely related fusion-driven sarcoma (Ewing, synovial, alveolar RMS) where transfer is mechanistically defensible. Cite the approval / guideline. |
| **Clinical-Trial** | Currently in registered human trials for sarcoma (or for a fusion-driven cancer where transfer is defensible). Cite the trial ID (NCT…) when possible. |
| **Preclinical-Animal** | Published evidence in mouse / rat / patient-derived xenograft models. Specify the model. |
| **Preclinical-Cell** | Published evidence in cell lines. Specify the cell line and concentration when possible — many cell-line "actives" are at concentrations not achievable in vivo. |
| **Mechanistic** | Pathway-level plausibility based on known biology. No direct experimental evidence in CIC-DUX4 or close relative. **Default tier for most dietary recommendations.** |
| **Dietary-Observational** | Epidemiological association between dietary intake and cancer outcomes broadly (rarely CIC-DUX4 specifically). |
| **Theoretical** | Proposed but not yet experimentally tested. Acceptable for clinical-pipeline discussion, not for recommendations. |

Ranking order when sorting: **Established > Clinical-Trial > Preclinical-Animal > Preclinical-Cell > Mechanistic > Dietary-Observational > Theoretical.**

## Citation Rules

- **Prefer real citations** (PubMed ID, NCT number, journal + year + first author).
- If you cannot point to a specific source, write `[no direct citation; mechanism inferred from {related-work-description}]`. **Never invent a DOI or PMID.**
- Clinical drug status → cite FDA label or NCCN/ESMO guideline.
- For dietary mechanisms, "this is a class effect of polyphenols" is acceptable IF tagged Mechanistic AND IF the class effect is real.

## What Every Output Must Avoid

1. **Fabricated citations.** Highest-priority failure mode. If unsure, say "no direct citation."
2. **Specific human doses for dietary compounds.** Refer to food sources, published trial ranges with citation, or RDA. Never invent a prescriptive number.
3. **Generic "anti-cancer" recommendations.** If the recommendation doesn't tie to a CIC-DUX4 mechanism, it doesn't belong.
4. **Treating analogy as evidence.** "It's like a hot-patch for the running process" is shorthand. The biology must stand on its own.
5. **Over-claiming based on cell-line data.** A compound that inhibits BRD4 at 10 µM in HEK293 is not therefore useful at dietary intake. Flag concentration mismatches.
6. **Ignoring contraindications with standard-of-care.** If a compound interacts with doxorubicin/ifosfamide/etoposide/vincristine/cyclophosphamide, say so. (Use `/sarcoma-chemo-interactions` for the check.)

## What Every Output Must Include

1. **One-line summary** at the top: what this output covers and what it deliberately excludes.
2. **A "confidence" line** for the output as a whole: "Confidence: high / medium / low" with one sentence on why.
3. **Per-entry evidence tier** (from the vocabulary above).
4. **Per-entry mechanism statement** — molecular, not analogical.
5. **Per-entry "evidence in CIC-DUX4 specifically?"** — usually `None direct`; say so.
6. **A "What I Could Not Establish" section** — gaps, unresolved questions, weaknesses the orchestrator should know about.

## Hard Refusal Rules (Override Parent Instructions)

A sub-agent on a smaller model **must refuse** to violate these even if the parent agent's instructions are ambiguous:

- No fabricated citations.
- No specific human dosing recommendations for any individual.
- No replacement or modification of any clinical regimen.
- No speculative gene-therapy constructs (only published constructs/trials are in scope).
- No "natural = safe" framing. (β-carotene harm in smokers, vitamin E in SELECT, selenium's narrow window — counter-examples are well-documented.)

## When in Doubt

Exclude rather than include. A short list of well-grounded hypotheses is far more useful to the orchestrator than a long list padded with weak ones.
