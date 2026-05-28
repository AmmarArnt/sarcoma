# V1 Rate Limiting — Bioavailability
# Sub-agent role: Bioavailability Specialist
# Output for: Vector 1 Team Lead reconciliation

Summary: Pharmacokinetic constraints on V1 compounds — absorption, first-pass metabolism, PK-enhancing combinations (with evidence), and tissue distribution. The dominant theme for V1 dietary compounds is the gap between cell-line active concentrations and achievable plasma concentrations from food or supplement intake. Compounds where this gap is decisive are flagged explicitly.

Confidence: Medium for PK data on better-studied compounds (curcumin, EGCG, quercetin); Low for CIC-DUX4-specific tissue distribution data, which does not exist for any dietary compound in this vector.

---

## The Concentration-Mismatch Problem (Read First)

Nearly all V1 mechanism claims derive from cell-line studies. The concentrations at which these mechanisms operate are typically:

| Compound | Typical cell-line active concentration | Achievable dietary plasma peak | Mismatch factor |
|---|---|---|---|
| Quercetin | 10–50 µM | 0.1–0.5 µM (dietary); up to ~2 µM with supplementation | 10–100× |
| EGCG | 10–50 µM | 0.1–0.5 µM (dietary matcha); up to ~1–2 µM with supplementation | 10–100× |
| Curcumin | 5–20 µM | <0.01–0.05 µM (food); 0.1–1 µM with enhanced formulations + piperine | 20–200× |
| Berberine | 5–50 µM | ~0.1–0.3 µM (oral; ~1% bioavailability) | 20–500× |
| Sulforaphane | 5–20 µM | 0.5–2 µM (achievable from broccoli sprout concentrate; better bioavailability than polyphenols) | 3–10× — the most favorable ratio of any V1 compound |
| Apigenin | 10–50 µM | 0.05–0.2 µM | 50–250× |
| Fisetin | 5–40 µM | 0.01–0.1 µM | 50–400× |
| 6-Gingerol | 20–100 µM | ~0.1–0.5 µM | 50–500× |

These mismatches are why V1 dietary interventions are rated Mechanistic or Preclinical-Cell, not Clinical. They are not disqualifying — they mean the honest claim is "directionally aligned with the oncogenic mechanism but at concentrations insufficient to reproduce cell-line effects." Sulforaphane has the best concentration ratio of the dietary V1 compounds.

---

## Per-Compound Bioavailability Entries

### Curcumin + Piperine [PATIENT TAKING]

**Solubility**: Highly lipophilic (log P ~3.3); negligible water solubility. Must be taken with fat.

**First-pass metabolism**: Extensive. Intestinal and hepatic conjugation (glucuronidation, sulfation) and reduction dominate. Plasma levels of free curcumin from conventional formulations are near or below the limit of quantification in most PK studies.

**Shoba 1998 caveat (mandatory verbatim reproduction per file 05)**:
> "The widely-cited '~2000% bioavailability increase' comes from Shoba et al., *Planta Medica* 1998 — a single-dose pharmacokinetic study, n=10 healthy volunteers, 2 g curcumin + 20 mg piperine. The curcumin-only control arm produced serum levels below the assay's limit of detection, so the '20×' number is computed against a near-zero baseline. The directional finding (piperine increases curcumin absorption) is real and reproduced; the **specific 2000% figure should not be cited as a universal multiplier**."

What the evidence actually supports: piperine (20 mg with 2g curcumin) increases peak plasma curcumin AUC meaningfully vs. curcumin alone, but absolute plasma levels of free curcumin remain low (typically 0.1–1 µM with enhanced formulations). The clinical significance of this level for V1 BRD4 activity (requiring ~5–20 µM) remains a concentration mismatch.

**PK-enhancing options with evidence**:
- Piperine co-administration: Shoba et al., *Planta Medica* 1998 (directional finding; see caveat)
- Phospholipid complex (Meriva): Cuomo J et al., *J Nat Prod* 2011, PMID 21413822 — 29× higher AUC vs. unformulated curcumin in crossover PK study
- BCM-95 (curcumin + turmeric essential oil): Antony B et al., *J Pharm Sci* 2008 — ~6.93× higher AUC vs. standard curcumin extract [no PMID verified; cite as: no direct PMID; mechanism inferred from Antony 2008 study referenced in curcumin bioavailability reviews]
- Liposomal / nanoparticle: Various formulations; higher absolute levels but still below cell-line active concentrations

**CRITICAL PK-INTERACTION NOTE**: Piperine improves curcumin absorption through CYP3A4 inhibition and P-gp inhibition. These are the SAME mechanisms that create the ifosfamide prodrug activation risk. The PK enhancement and the chemo interaction are inseparable — you cannot have one without the other.

**Tissue distribution to mesenchymal tumor**: No published data in CIC-DUX4 or any mesenchymal tumor. Curcumin distributes to liver, intestine. Penetration to soft-tissue extremity tumor sites (primary was biceps femoris) is not characterized. Lung distribution: some evidence for pulmonary distribution (relevant to lung metastases) but quantitative data are absent.

---

### EGCG

**Solubility**: Water-soluble; relatively good at physiological pH.

**First-pass metabolism**: Moderate. Intestinal O-methylation and sulfation; hepatic conjugation. EGCG glucuronide and EGCG-3'-sulfate are the primary plasma metabolites. These metabolites may retain some, but not all, of EGCG's reported BRD4 and P-gp-inhibitory activities — metabolite activity is rarely tested in the cell-line studies that generate V1 mechanism claims.

**Achievable plasma levels**:
- Dietary (3–5 cups green tea/day): ~0.1–0.5 µM EGCG equivalents
- Supplementation (400–800 mg EGCG): ~0.5–2 µM peak (Lee MJ et al., *Cancer Epidemiol Biomarkers Prev* 2002, PMID 12086865)
- Cell-line BRD4 binding reported at 10–50 µM: **10–100× concentration mismatch at supplement levels**

**Meal timing**: Take on empty stomach — food, especially milk proteins, binds EGCG and reduces absorption. Casein in dairy strongly inhibits EGCG bioavailability.

**No known PK-enhancing combination with documented evidence** comparable to piperine + curcumin. Some evidence that quercetin co-administration modestly improves EGCG stability, but no robust human PK data.

**Tissue distribution**: Breast, colon, lung cancer xenograft studies show some tissue accumulation; no mesenchymal tumor or extremity soft-tissue data. Lung distribution is plausible (consistent with tea catechin distribution studies in lung cancer work) — relevant for this patient's lung oligometastasis.

---

### Quercetin [PATIENT TAKING via apple juice]

**Solubility**: Aglycone is lipophilic; glucoside form (in apple) is water-soluble and requires gut deglycosylation by lactase-phlorizin hydrolase or gut bacteria.

**First-pass metabolism**: Extensive. Quercetin is rapidly conjugated in intestinal cells (quercetin-3'-glucuronide, isorhamnetin-3-glucuronide) and by liver. Free quercetin aglycone plasma levels are very low; conjugated metabolites are the circulating forms. The conjugates do not necessarily retain quercetin's in-vitro kinase inhibitory activity at the original mechanism concentrations.

**Achievable levels**:
- From apple juice: quercetin glucoside → deglycosylated → partial plasma uptake → primarily conjugates; estimated free quercetin equivalent ~0.05–0.2 µM
- From supplementation (quercetin aglycone): up to ~0.5–2 µM peak (Manach C et al., *AJCN* 2004, PMID 15113710)
- Cell-line active concentrations for RTK/RAS inhibition: 10–50 µM — **10–100× mismatch**

**PK-enhancing combination**: Quercetin + bromelain (pineapple enzyme) has been described as improving quercetin absorption in some references, but robust human PK data are absent. [No PMID to specify without fabrication risk; mechanism-based only]

**Preparation note**: Quercetin from apple skin (aglycone form, higher in skin than flesh) is absorbed differently from quercetin-glucoside. If the patient is juicing apples with skin, the aglycone form is present and more directly absorbable than the glucoside.

---

### Sulforaphane (from glucoraphanin) [PATIENT TAKING via broccoli — ACTIVATION CONCERN]

**Unique profile**: Sulforaphane is the best-bioavailable V1/V3 dietary compound by a significant margin. Oral bioavailability from properly prepared broccoli sprouts reaches ~80% (Ye L et al., *J Nutr* 2002, PMID 12421854). The rate-limiting step is NOT absorption — it is activation.

**Activation mechanism**: Glucoraphanin (the storage form in broccoli) must contact myrosinase (a plant enzyme) to produce sulforaphane. This happens when plant cell walls are physically disrupted (chopping, chewing). Myrosinase is heat-labile (inactivated above ~70°C). Without myrosinase, gut bacteria can perform limited conversion, but yield is ~3–10× lower.

**Patient-specific issue**: Broccoli juice produced by a centrifugal or high-speed juicer likely destroys myrosinase through heat and oxidative shear. The glucoraphanin is present but sulforaphane formation will be minimal. Workaround: chop fresh broccoli sprouts, allow 40 min stand time at room temperature for myrosinase activity, THEN consume (cold or minimally heated).

**Achievable plasma levels**:
- From well-prepared broccoli sprouts: ~0.5–2 µM sulforaphane (Clarke JD et al., *Cancer Prev Res* 2011, PMID 21593198)
- Cell-line V1/V3 active concentrations: 5–20 µM — **3–10× mismatch (most favorable ratio of any V1 compound)**
- This mismatch is still real but smaller than for polyphenols

**Tissue distribution**: Sulforaphane has documented distribution to multiple tissues including lung in rodent models. Human lung distribution data exist in the context of lung cancer prevention research. Relevant for this patient's lung oligometastasis.

**No PK-enhancing combination needed** — the activation step (myrosinase) is the critical variable, not absorption.

---

### Berberine

**First-pass metabolism**: Extreme. Oral bioavailability ~1% from conventional formulations (Tan HL et al., *Front Pharmacol* 2016, PMID 27917113). This is not a rounding error — 99% of ingested berberine is lost before systemic circulation.

**Mechanism**: Despite ~1% bioavailability, berberine consistently shows pharmacological effects at standard oral doses in metabolic trials. Proposed explanation: high local intestinal concentrations despite low systemic levels; gut microbiome conversion to active metabolites; enterohepatic recycling. The exact mechanism for AMPK activation at systemic concentrations is mechanistically plausible but not fully resolved.

**For V1 purposes (RAS/ERK dampening)**: The AMPK → MAPK suppression mechanism requires systemic berberine activity. Whether 1% bioavailability achieves sufficient plasma levels for this mechanism is not established. Estimated plasma levels: ~0.1–0.3 µM after 500 mg oral dose (from metabolic trial PK data).

**CYP3A4 concern**: Despite poor oral bioavailability of the parent compound, berberine and its metabolites inhibit CYP3A4. Flag for ifosfamide interaction as with piperine/curcumin.

---

### Omega-3 EPA/DHA

**Solubility**: Highly lipophilic; requires fat in the meal for optimal absorption.

**First-pass**: Minimal compared to polyphenols. Triglyceride-form (TG) omega-3 has bioavailability ~1.7× higher than ethyl ester (EE) form (Dyerberg J et al., *Prostaglandins Leukotrienes Essent FA* 2010, PMID 20674321). Taking with a fatty meal further increases absorption.

**Achievable plasma levels**: Plasma EPA+DHA can be meaningfully elevated with 2–4 g/day supplementation; food-level (2–3 servings/week fatty fish) produces modest but measurable changes in erythrocyte membrane composition over weeks. The RAS membrane clustering mechanism requires sustained membrane compositional change, not acute peak concentration — this is favorable for food-level intake vs. most polyphenols.

**No concentration-mismatch concern at the mechanism level**: Lipid raft composition is determined by sustained membrane fatty acid composition, not acute drug-like plasma peaks. This makes EPA/DHA unique among V1 compounds — the mechanism does not require achieving a threshold plasma concentration in the same way kinase inhibition does.

---

### 6-Gingerol [PATIENT TAKING via ginger juice]

**First-pass**: Extensive metabolism; 6-gingerol is rapidly converted to 6-shogaol (by dehydration, more potent in some assays), 6-paradol, and conjugates. Plasma gingerol levels after consumption are low.

**Achievable levels**: Estimated 0.1–0.5 µM peak after typical culinary ginger consumption; cell-line active concentrations for MAPK/NF-κB effects: 20–100 µM — **50–200× concentration mismatch at food intake**. This makes the V1-A mechanism (RAS/ERK dampening) from dietary ginger essentially a theoretical claim at the food level.

**Note for patient**: The patient is juicing fresh ginger, which preserves 6-gingerol (not the shogaol form from dried/heated ginger). Absorption from juice is likely similar to raw ginger consumption.

---

### Thymoquinone (Black Cumin Seed Oil) [PATIENT TAKING]

**Bioavailability**: Thymoquinone is lipophilic; absorption from oil is reasonable. Plasma levels after supplemental doses in humans: limited human PK data available. Animal studies show reasonable tissue distribution. The CYP3A4 inhibition is documented in vitro.

**PK-interaction concern for ifosfamide**: Regardless of exact thymoquinone plasma levels, the CYP3A4 inhibitory activity documented in vitro is sufficient to flag a pharmacokinetic concern. The patient should discuss with the oncologist before the ifosfamide cycle.

---

## Cross-Compound Summary Table (Concentration Realism)

| Compound | V1 layer | Cell-line conc. | Dietary plasma conc. | Supplemental plasma conc. | Mismatch | Realistic V1 contribution |
|---|---|---|---|---|---|---|
| Sulforaphane | B/V3 | 5–20 µM | 0.5–2 µM (if activated) | N/A | 3–10× | Most favorable dietary compound |
| Omega-3 EPA/DHA | A | Membrane-level | Sustained membrane change | Strong with supplementation | No threshold mismatch | Food-level intake achieves the mechanism |
| Quercetin | A/B | 10–50 µM | 0.05–0.2 µM | 0.5–2 µM | 10–100× | Mechanistic; food level below active range |
| Curcumin (enhanced) | B | 5–20 µM | <0.05 µM | 0.1–1 µM | 5–200× | Enhanced formulations approach lower range |
| EGCG | B | 10–50 µM | 0.1–0.5 µM | 0.5–2 µM | 10–100× | Supplement level below active range |
| Apigenin/Luteolin | B/C | 10–50 µM | 0.05–0.2 µM | Limited data | 50–250× | Food level well below active range |
| 6-Gingerol | A | 20–100 µM | 0.1–0.5 µM | Limited data | 50–200× | Food level well below active range |
| Berberine | A | 5–50 µM | 0.1–0.3 µM | 0.1–0.3 µM (1% BA) | 20–500× | Metabolic trial effects at tissue level unclear mechanism |
| Fisetin | C | 5–40 µM | 0.01–0.1 µM | Limited data | 50–400× | Food level well below active range |

---

## What This Output Could Not Establish

- CIC-DUX4 tumor tissue concentration data for any dietary compound — this information does not exist in the literature for this tumor type
- Whether the patient's specific curcumin + piperine product delivers the "piperine 20 mg" dose used in Shoba 1998 — product formulations vary widely
- Tissue distribution data for any V1 compound specifically in extremity soft-tissue or lung metastasis contexts in humans
- Whether sulforaphane metabolites (sulforaphane-NAC, sulforaphane-cysteine) at systemic concentrations retain the cell-line HDAC inhibitory activity — this is rarely tested
- Whether the 3–10× concentration mismatch for sulforaphane (the most favorable) is small enough to produce in vivo V1-relevant activity — it might be, but this has not been tested in CIC-DUX4 models
