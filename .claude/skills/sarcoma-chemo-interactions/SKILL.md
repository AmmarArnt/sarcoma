---
name: sarcoma-chemo-interactions
description: Scaffolding checklist for checking dietary or supplement candidates against the standard-of-care chemotherapy regimen for CIC-rearranged sarcoma (VDC/IE — vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide). Lists the drugs, their metabolic axes, and the well-documented interaction classes that any candidate compound must be screened against. This skill does NOT pre-encode specific compound-by-compound interactions to avoid fabrication risk — the agent looks them up in real sources. Invoke whenever a vector lead or sub-agent is about to recommend any dietary, supplement, or polyphenol intervention.
---

# Chemo-Interaction Screening Checklist

This skill is a **scaffold for the screening process**, not a claims database. The job is to look up real interactions in real sources — PubChem, DrugBank, NCCN guidelines, FDA labels — and report what you find. Do not invent interactions to look thorough; do not omit them to look conservative.

## SOC Regimen for CIC-Rearranged Sarcoma

Typical front-line regimen is **Ewing-like multi-agent chemotherapy**:

| Drug | Class | Primary metabolic / interaction axis |
|---|---|---|
| **Vincristine** | Vinca alkaloid (anti-microtubule) | CYP3A4 substrate; P-gp substrate. CYP3A4 inhibitors → increased toxicity (neuropathy) |
| **Doxorubicin** | Anthracycline (topoisomerase II inhibitor + ROS generator) | CYP3A4 / CBR1 metabolism; P-gp substrate. **ROS-mediated mechanism — high-dose antioxidants are the canonical concern** |
| **Cyclophosphamide** | Alkylating agent (prodrug) | CYP2B6, CYP3A4 activation to 4-hydroxy-CY; CYP inhibitors can reduce activation |
| **Ifosfamide** | Alkylating agent (prodrug) | CYP3A4 activation; ROS contribution to mechanism; CNS toxicity from chloroacetaldehyde metabolite |
| **Etoposide** | Topoisomerase II inhibitor | CYP3A4 substrate; P-gp substrate |

Plus surgery and radiation as indicated.

## Interaction Classes Every Candidate Must Be Screened Against

For each candidate compound your output recommends, check each of these axes and write what you find (with citation). Write `not screened — out of scope for this output` if you intentionally skipped one.

### 1. CYP3A4 modulation

Vincristine, doxorubicin, cyclophosphamide, ifosfamide, and etoposide all go through CYP3A4 to some degree. Strong CYP3A4 inhibitors raise vincristine/etoposide AUC (toxicity) and impair cyclophosphamide/ifosfamide activation (efficacy).

**Examples of dietary compounds with documented CYP3A4 activity (look up specifics yourself):** grapefruit furanocoumarins, St. John's wort (induction), curcumin, EGCG, quercetin, resveratrol, piperine, berberine, milk thistle silymarin.

### 2. CYP2B6 / CYP2C9 modulation

Cyclophosphamide activation depends partly on CYP2B6. Several polyphenols modulate CYP2C9. Check for the specific compound.

### 3. P-glycoprotein (P-gp / ABCB1) modulation

Vincristine, doxorubicin, and etoposide are P-gp substrates. P-gp inhibition increases CNS exposure and toxicity. P-gp induction reduces efficacy.

**Known modulators to look up:** piperine, curcumin, quercetin, EGCG, resveratrol, ginsenosides.

### 4. ROS-axis interference (high-dose antioxidants)

Doxorubicin and ifosfamide mechanisms include ROS generation. High-dose antioxidant supplementation (NAC, vitamin C, vitamin E) may theoretically reduce efficacy. Clinical data are mixed but medical oncology guidelines generally advise against high-dose antioxidant supplementation **during** cytotoxic chemotherapy. **Dietary intake (whole foods) is treated differently from supplement-level dosing — say which one you are recommending.**

### 5. UGT / SULT / GST conjugation pathways

Doxorubicinol formation goes through CBR1; doxorubicin glucuronidation goes through UGT2B7. Less commonly modulated by dietary compounds, but flag known interactions.

### 6. Topoisomerase II direct interactions

Some polyphenols (notably high-dose EGCG, genistein, quercetin in cell-free assays) have Topo II–poison activity. Theoretical concern for combination with etoposide/doxorubicin: additive or antagonistic? Cell-line evidence; clinical relevance unclear. Flag and stop — do not extrapolate.

### 7. Anti-platelet / bleeding risk

Garlic, ginkgo, high-dose fish oil, vitamin E, curcumin — relevant when chemo is combined with surgery (which it often is in sarcoma management).

### 8. Hepatic / renal load

Ifosfamide is nephrotoxic; doxorubicin is cardiotoxic. Concurrent supplements with renal or hepatic load (e.g., high-dose NSAID-like polyphenols) compound the burden.

## Output Format for Each Screened Compound

When a vector lead or sub-agent reports a compound in the dietary/supplement track, the screening line should read:

```
{Compound} — chemo screening:
  CYP3A4: {modulator? source} | P-gp: {modulator? source} | ROS-axis: {concern at supplement dose? source} | Other: {note} | Citation: {PMID / DrugBank / NCCN}
```

If no documented interaction was found, write `none found in {source(s) checked}`. **Never write "no interactions" without saying which sources were checked.**

## What This Skill Does Not Do

- It does not list specific interactions. The lookup must be done against real sources.
- It does not authorize claims about chemotherapy regimens.
- It does not replace the orchestrator's `Standard-of-Care Interaction Map` — that's a synthesis across all vector outputs.

## Bottom Line

Every dietary recommendation that reaches the orchestrator must arrive with an interaction-screening line. Compounds with documented interactions are not necessarily disqualified — they're flagged for oncologist review. The orchestrator decides what makes it into the final catalog.
