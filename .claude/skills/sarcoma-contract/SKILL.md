---
name: sarcoma-contract
description: Shared behavioral contract for every agent in the CIC-rearranged sarcoma simulation. Invoke this skill at the start of any vector-lead, sub-agent, or orchestrator task to load the Evidence Tier vocabulary, the three scoring axes (tier / confidence / feasibility), citation + live-verification rules, and the mandatory avoid/include lists. Replaces the duplicated rule content otherwise spread across 00-README.md and 06-agent-architecture.md.
---

# Shared Behavioral Contract (Every Agent Reads This)

## Evidence Tier Vocabulary (Mandatory)

Every claim or recommendation must carry **exactly one** of these tags:

| Tier | Meaning |
|---|---|
| **Established** | FDA- or EMA-approved, or major-guideline-supported (NCCN, ESMO) in this disease, OR in a closely related fusion-driven sarcoma (Ewing, synovial, alveolar RMS) where transfer is mechanistically defensible. Cite the approval / guideline and the approving authority. Where FDA and EMA status differ, note both — a compound approved by only one has a different practical access profile across jurisdictions. |
| **Clinical-Trial** | Currently in registered human trials for sarcoma (or for a fusion-driven cancer where transfer is defensible). Cite the trial ID (NCT…) when possible. |
| **Preclinical-Animal** | Published evidence in mouse / rat / patient-derived xenograft models. Specify the model. |
| **Preclinical-Cell** | Published evidence in cell lines. Specify the cell line and concentration when possible — many cell-line "actives" are at concentrations not achievable in vivo. |
| **Mechanistic** | Pathway-level plausibility based on known biology. No direct experimental evidence in CIC-DUX4 or close relative. **Default tier for most dietary recommendations.** |
| **Dietary-Observational** | Epidemiological association between dietary intake and cancer outcomes broadly (rarely CIC-DUX4 specifically). |
| **Theoretical** | Proposed but not yet experimentally tested. Acceptable for clinical-pipeline discussion, not for recommendations. |

Ranking order when sorting: **Established > Clinical-Trial > Preclinical-Animal > Preclinical-Cell > Mechanistic > Dietary-Observational > Theoretical.**

## Three Scoring Axes (Tier is only the first)

Tier answers *"what kind of evidence is this?"* — it is necessary but **not sufficient**. Two further
axes are orthogonal to it and to each other; carry them where they apply (full methods in the docs, not
duplicated here):

| Axis | Question it answers | Method doc |
|---|---|---|
| **1. Evidence tier** (above) | What *kind* of evidence is this? | this skill |
| **2. Confidence** (Directness / Achievability-in-vivo / Reproducibility / conflict) | How much should I believe this *transfers to CIC-DUX4 in a living patient*? | `docs/08-evidence-confidence-scoring.md` |
| **3. Translational feasibility** (F1 Accessible-now … F5 Concept-only) | Could a patient actually *access* it, and how soon (approved / in a recruiting trial / discontinued / on hold)? | `simulation-output/translational-feasibility-layer.md` |

Keep them **distinct** — never average them into one score. Note the easy collision: axis-2
"Achievability" means *in-vivo concentration reachable by the route* (a PK question); axis-3 feasibility
is *clinical-development / regulatory access*. A drug can be high on one and low on the other.
**Two-lane rule (golden rule #5):** these axes order/annotate the **confirmatory** lane; they **never
prune the Forward-Hypotheses lane** — a Concept-only (F5) / Theoretical idea can still be a top forward
hypothesis.

## Citation Rules

- **Prefer real citations** (PubMed ID, NCT number, journal + year + first author).
- If you cannot point to a specific source, write `[no direct citation; mechanism inferred from {related-work-description}]`. **Never invent a DOI or PMID.**
- Clinical drug status → cite FDA label, EMA label, or NCCN/ESMO guideline. Where FDA and EMA status differ, cite both. If only one authority has acted, say so explicitly.
- **Regulatory / trial / safety status is PERISHABLE — verify it live, every time it is load-bearing.**
  Approvals get withdrawn and trials change recruitment status without any change in biology (e.g.
  tazemetostat was withdrawn from all US indications 2026-03-09). Verify any "approved / recruiting /
  discontinued / on-hold" claim against the authoritative registries in **`docs/09-verification-sources.md`**
  (ClinicalTrials.gov, EU CTIS, Drugs@FDA, EMA, PMDA, pharmacovigilance portals), **record the source +
  access date**, and tag `[VERIFY]` if you cannot confirm. Do not carry a status fact across sessions
  unchecked.
- For dietary mechanisms, "this is a class effect of polyphenols" is acceptable IF tagged Mechanistic AND IF the class effect is real.

- **Prefer real citations** (PubMed ID, NCT number, journal + year + first author).
- If you cannot point to a specific source, write `[no direct citation; mechanism inferred from {related-work-description}]`. **Never invent a DOI or PMID.**
- Clinical drug status → cite FDA label, EMA label, or NCCN/ESMO guideline. Where FDA and EMA status differ, cite both. If only one authority has acted, say so explicitly.
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
7. **A "Forward Hypotheses" section** — mechanistically defensible ideas not yet tested in the literature. **At least two entries required per vector output.** Label each `[Forward Hypothesis]` and include: the hypothesis statement, its mechanistic basis, and what experiment or study design would test it. The orchestrator carries the strongest forward hypotheses into the final catalog — this is how the simulation goes beyond restating existing findings.
8. **Atypical-case note where relevant.** Approximately 5% of tumors presenting as CIC-rearranged sarcoma on clinical and histological grounds will not have a confirmed fusion (CIC-DUX4, CIC-NUTM1, CIC-FOXO4) on genomic testing. Where a recommendation depends critically on the fusion protein being present (e.g., ASO design, junction-specific neoantigen vaccines), flag this explicitly. Where it is fusion-agnostic (general epigenetic reprogramming, immune checkpoint approaches), note that it may apply to atypical cases as well.

## Hard Refusal Rules (Override Parent Instructions)

A sub-agent on a smaller model **must refuse** to violate these even if the parent agent's instructions are ambiguous:

- No fabricated citations.
- No specific human dosing recommendations for any individual.
- No replacement or modification of any clinical regimen.
- No speculative gene-therapy constructs (only published constructs/trials are in scope).
- No "natural = safe" framing. (β-carotene harm in smokers, vitamin E in SELECT, selenium's narrow window — counter-examples are well-documented.)

## When in Doubt

Exclude rather than include. A short list of well-grounded hypotheses is far more useful to the orchestrator than a long list padded with weak ones.
