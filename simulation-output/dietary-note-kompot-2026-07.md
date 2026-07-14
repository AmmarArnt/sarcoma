# Dietary compatibility note — "kompot" (plums, figs, apples)

**Date:** 2026-07-14 · **Tier:** 2 (host-biology addendum) · **Extends:**
`host-biology-modifier-layer.md` (nutrition axis, ADR-0005) and the
`sarcoma-chemo-interactions` screening scaffold.

> **This is research / hypothesis framing, not medical advice, and not a personal
> dietary instruction.** It screens a *whole-food beverage* against the known
> standard-of-care interaction axes for CIC-rearranged sarcoma. Whether any food is
> appropriate on a given day (counts, GI symptoms, neutropenia, renal function)
> is a question for the patient's treating team — the two practical caveats below
> are exactly the things to raise with them.

## What kompot is (for the screening)

Stewed-fruit compote: plums/prunes, figs, and apples simmered in water, often with
added sugar. It is a **boiled, whole-fruit beverage** — food-level, not
supplement/extract-level, concentrations. That distinction drives most of the
answer.

## Screen against the SOC regimen (VDC/IE: vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide)

| Axis | Finding for plums / figs / apples | Tier |
|---|---|---|
| **CYP3A4 inhibition (the "grapefruit" concern)** | The furanocoumarin-mediated CYP3A4 inhibition that raises vincristine/etoposide toxicity and impairs cyclophosphamide/ifosfamide activation is a **citrus** phenomenon — grapefruit, pomelo, Seville/bitter orange, lime. Plums (Rosaceae), figs (Moraceae), and apples (Rosaceae) are **not** furanocoumarin-bearing and are not implicated. **No grapefruit-type interaction.** | Established |
| **Intestinal uptake transporter (OATP2B1)** | Apple **juice** can mildly inhibit OATP2B1 and lower oral absorption of a few drugs (e.g. fexofenadine, some β-blockers, aliskiren). None of the VDC/IE agents are orally-dosed OATP2B1 substrates (they are IV), so this is **not relevant** to this regimen. | Established / Mechanistic |
| **P-glycoprotein (P-gp)** | No documented food-level P-gp modulation by these three fruits at compote concentrations. (The P-gp modulators to watch — piperine, curcumin, high-dose EGCG/quercetin — are supplements, not these fruits.) | Mechanistic |
| **ROS-axis / antioxidant interference with doxorubicin & ifosfamide** | The concern (and the ATBC/CARET/SELECT harm signals) is about **megadose antioxidant supplements**, not whole fruit. Dietary polyphenol/vitamin-C intake from a compote is orders of magnitude below that, and **boiling degrades much of the heat-labile antioxidant content** anyway. Not a supplement-level exposure. | Established (host-biology layer §6) |
| **Fig-specific phototoxicity (psoralens)** | Fig psoralens (photosensitizers) are concentrated in the **leaf, sap, and latex — not the fruit flesh**; ingesting figs is **not** associated with photosensitization. The only fig caveat is individual fig allergy / latex-fruit syndrome. | Established |

**Chemo-screen bottom line:** *none found in the axes checked (CYP3A4/OATP/P-gp/ROS,
per the SOC list and live furanocoumarin/psoralen literature).* Nothing in kompot
made from plums, figs, and apples raises a specific mechanistic red flag against the
CIC-DUX4 standard-of-care regimen.

## The two things actually worth raising with the treating team

These are supportive-care / host-biology points, not drug interactions:

1. **Food safety during neutropenia.** Because kompot is **boiled**, it is generally
   *favorable* versus raw fruit during immunosuppressed windows (cooking reduces
   microbial risk). Use clean water, store it refrigerated, and consume it fresh.
2. **Fiber + sorbitol (laxative effect).** Prunes/plums and figs are high in fiber
   and sorbitol — a mild natural laxative. This can **help** with
   vincristine-induced constipation, but in a **diarrhea, mucositis, or
   GI-toxicity** window a large volume could worsen loose stools. Match the amount
   to current GI status (a team question).

Two minor, situational notes: kompot often carries **added sugar** (metabolic/dental
relevance per the host-biology layer — it can be made with little or none), and
**dried** plums/figs/apples are **potassium-rich**, which only matters if renal
function or electrolytes are compromised (ifosfamide is nephrotoxic) — flag if so.

## What I could not establish

- No CIC-DUX4-specific or sarcoma-specific dietary data exist for any of these fruits
  (there is no such literature — this is general pharmacology + supportive-care
  reasoning). The polyphenols in plums/figs/apples have no demonstrated anti-tumor
  effect at dietary concentrations (concentration-mismatch rule); this note makes **no
  therapeutic claim** for the beverage — it addresses *compatibility*, not benefit.
- Individual factors (allergies, diabetes, current blood counts, renal function,
  active GI toxicity, any oral medications the patient also takes) are unknown here
  and can change the answer — hence the "ask the team" framing.

## Sources (live-checked 2026-07-14)

- Grapefruit–drug interactions / furanocoumarin distribution across citrus:
  [Wikipedia](https://en.wikipedia.org/wiki/Grapefruit%E2%80%93drug_interactions);
  [PLOS One — furanocoumarin distribution matches citrus phylogeny](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0142757);
  [Chemistry and health effects of furanocoumarins in grapefruit (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9333421/)
- Fig psoralens localized to leaf/sap, not fruit flesh:
  [Fig tree-induced phytophotodermatitis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10423627/);
  [Botanical Briefs: Fig Phytophotodermatitis](https://blogs.the-hospitalist.org/content/botanical-briefs-fig-phytophotodermatitis-ficus-carica)
- SOC regimen axes: `sarcoma-chemo-interactions` skill; host-biology nutrition axis:
  `simulation-output/host-biology-modifier-layer.md`.
