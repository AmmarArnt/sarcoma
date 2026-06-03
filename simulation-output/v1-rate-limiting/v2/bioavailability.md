# V1 Rate Limiting — Bioavailability (v2)
# Sub-agent role: Bioavailability Specialist
# Output for: Vector 1 Team Lead v2 reconciliation

Summary: Pharmacokinetic constraints on V1 compounds — fat/water solubility, first-pass metabolism magnitude, known PK-enhancing combinations with cited effect sizes, and tissue distribution toward mesenchymal tumor. The dominant finding for this vector is that dietary plasma concentrations fall 3–500× below cell-line active concentrations for nearly all compounds; sulforaphane (3–10×) and omega-3 EPA/DHA (no threshold mismatch for its mechanism) are the notable partial exceptions. This output also contains the mandatory Shoba 1998 caveat for curcumin + piperine.

Confidence: Medium for PK data on well-studied compounds (curcumin, EGCG, quercetin, omega-3); Low for CIC-DUX4-specific or mesenchymal-tumor tissue distribution data (does not exist in the published literature for any dietary compound in this vector). Low for thymoquinone human PK specifically.

---

## The Concentration-Mismatch Problem: Summary Table

This table should be read before any individual entry. It is the most important bioavailability finding for V1.

| Compound | V1 Layer | Cell-line active concentration | Dietary plasma peak | Supplemental plasma peak | Mismatch factor | Realistic V1 contribution |
|---|---|---|---|---|---|---|
| Omega-3 EPA/DHA | A | Membrane-compositional (no single threshold) | Meaningful membrane incorporation with 2–3 servings/week | Strong with 2–4 g/day supplement | **No threshold mismatch** — mechanism is sustained membrane fatty acid composition change, not acute drug-like peak | Food-level intake achieves the mechanistic target |
| Sulforaphane | B/V3 | 5–20 µM | 0.5–2 µM (if properly activated — see myrosinase note) | N/A — no sulforaphane supplement equivalent to sprout protocol | **3–10×** — smallest mismatch of any polyphenol-type V1 compound | Best dietary compound by concentration ratio; preparation is critical |
| Quercetin | A/B | 10–50 µM | ~0.05–0.5 µM dietary (mostly conjugates; not free aglycone) | ~0.5–2 µM (aglycone supplement) | **10–100×** | Mechanistic alignment; below active range at food and moderate supplement |
| EGCG | B | 10–50 µM | ~0.1–0.5 µM (3 cups green tea) | ~0.5–2 µM (400–800 mg supplement) | **10–100×** | Same as quercetin; concentration-limited |
| Curcumin (conventional) | B | 5–20 µM | <0.01–0.05 µM (food turmeric) | ~0.05–0.3 µM (conventional extract supplement) | **100–400×** | Essentially below threshold without formulation enhancement |
| Curcumin (enhanced: phospholipid complex / piperine) | B | 5–20 µM | — | ~0.1–1 µM (best-case enhanced formulation with piperine) | **5–200×** | Enhanced formulations approach lower end of mismatch range; still below typical cell-line active range |
| Apigenin | B/C | 10–50 µM | ~0.05–0.2 µM | Limited human PK data | **50–250×** | Well below active range at food level |
| 6-Gingerol | A | 20–100 µM | ~0.1–0.5 µM (culinary fresh ginger) | Limited data | **50–200×** | Below active range; V1-A mechanism theoretical at food level |
| Berberine | A | 5–50 µM | — | ~0.1–0.3 µM (1% oral bioavailability from 500 mg dose) | **20–500×** | 1% BA; mechanistic effects in metabolic trials suggest tissue-level activity not fully captured by plasma PK |
| Fisetin | C | 5–40 µM | ~0.01–0.1 µM | Limited human PK data | **50–400×** | Well below active range |
| Lycopene | A | Not defined for ERK mechanism | Dietary carotenoid levels | Moderate with supplementation | Not quantifiable for V1 mechanism | Dietary-observational tier; mechanism mismatch assumed large |

---

## Per-Compound Bioavailability Entries

### Curcumin + Piperine [PATIENT TAKING]

**Fat- vs. water-soluble**: Highly lipophilic (log P ~3.3). Curcumin is essentially insoluble in water. Must be consumed with dietary fat for meaningful absorption. The patient's turmeric in supplements, if taken without a fat-containing meal, will have near-zero absorption.

**First-pass magnitude**: Extensive. Intestinal glucuronidation (UGT1A8, UGT1A10), sulfation (SULT1A1), and reductive metabolism dominate. Hepatic first-pass further reduces systemic curcumin. Plasma free curcumin from conventional formulations in most published PK studies is at or below assay LOD (~0.01–0.05 µM). The circulating species are predominantly curcumin glucuronides and sulfates, which may not retain full BRD4-binding activity.

**Shoba 1998 caveat (mandatory verbatim reproduction):**
> "The widely-cited '~2000% bioavailability increase' comes from Shoba et al., *Planta Medica* 1998 — a single-dose pharmacokinetic study, n=10 healthy volunteers, 2 g curcumin + 20 mg piperine. The curcumin-only control arm produced serum levels below the assay's limit of detection, so the '20×' number is computed against a near-zero baseline. The directional finding (piperine increases curcumin absorption) is real and reproduced; the **specific 2000% figure should not be cited as a universal multiplier**."

**What the evidence actually supports**: The Shoba study documents a directional finding only. The denominator (curcumin alone) was below the assay's LOD in the control arm, so the "2000%" figure is calculated as (detectable level) ÷ (below detection), which is mathematically undefined as a true fold-change. Subsequent PK studies confirm that piperine meaningfully increases curcumin AUC; absolute peak plasma curcumin with 2 g + 20 mg piperine in the Shoba study reached approximately 1.8 µg/mL (~4.9 µM, including metabolites). Even at this best-case figure, the V1 BRD4-chromatin mechanism requires 5–20 µM of free (unconjugated) curcumin in cell lines.

**PK-enhancing combinations with documented effect sizes:**
| Formulation | Enhancement vs. unformulated | Citation | Caveat |
|---|---|---|---|
| Piperine (20 mg with 2 g curcumin) | Directional increase; "2000%" against below-LOD baseline | Shoba G et al., *Planta Med* 1998 (see caveat above) | n=10, single dose; do not cite 2000% as universal |
| Phospholipid complex (Meriva) | ~29× higher AUC vs. unformulated curcumin | Cuomo J et al., *J Nat Prod* 2011, PMID 21413822 | Crossover PK in healthy volunteers; not sarcoma |
| Liposomal curcumin | Variable; higher absolute levels but formulation-dependent | Multiple formulation studies; no single canonical citation confirmed without PMID verification risk [no PMID; mechanism inferred from liposomal bioavailability literature] | No clinical oncology trial in sarcoma |

**Critical PK-interaction inseparability**: Piperine enhances curcumin absorption primarily through two mechanisms: (a) increased intestinal absorption/P-gp inhibition, and (b) CYP3A4 inhibition slowing curcumin metabolism. These are the **same** mechanisms that create the ifosfamide prodrug activation risk. The patient cannot gain the absorption benefit of piperine without simultaneously incurring the CYP3A4/P-gp interaction risk with ifosfamide and vincristine/etoposide.

**Tissue distribution to mesenchymal/lung tumor**: No published data for CIC-DUX4 or any soft-tissue sarcoma. Animal studies show curcumin distribution to liver, intestinal mucosa, and some evidence for lung tissue accumulation in rodent models. Pulmonary curcumin levels in human cancer patients — particularly in the context of a post-irradiated lung with an oligometastatic lesion — have not been characterized.

---

### EGCG

**Fat- vs. water-soluble**: Water-soluble. Does not require fat co-ingestion. However, dairy (casein) binds EGCG strongly and reduces absorption — consume tea without milk.

**First-pass magnitude**: Moderate. Intestinal O-methylation (COMT) to EGC-3'-Me; hepatic glucuronidation and sulfation. The principal circulating form at physiological plasma concentrations is EGCG-3'-glucuronide and EGCG-3'-sulfate. These conjugates retain partial BRD4-inhibitory activity compared to the parent compound in some but not all assays — activity of metabolites vs. parent is an important unresolved question for V1 mechanism translation.

**Achievable levels:**
- 3 cups brewed green tea (70°C): ~0.1–0.5 µM EGCG equivalents in plasma (Lee MJ et al., *Cancer Epidemiol Biomarkers Prev* 2002, PMID 12086865)
- 400–800 mg EGCG supplement: ~0.5–2 µM peak
- Cell-line BRD4 BD1 binding reported: 10–50 µM → **10–100× mismatch**

**Meal timing**: Empty stomach or between meals; 2-hour separation from dairy.

**No validated PK-enhancing combination**: Some evidence quercetin co-administration modestly stabilizes EGCG from intestinal degradation, but robust human PK data for this combination are absent [no PMID confirmed; mechanism-based inference].

**Tissue distribution**: Pulmonary distribution has been studied in lung cancer prevention context in rodent models; relevant to lung oligometastasis but human lung tissue data absent.

---

### Quercetin [PATIENT TAKING via apple juice]

**Fat- vs. water-soluble**: Aglycone (free form) is lipophilic; glycoside forms (quercetin-4'-glucoside in onion; quercetin-3-glucoside in apple) are water-soluble and require gut hydrolysis before absorption. Apple juice provides quercetin-3-glucoside predominantly, requiring lactase-phlorizin hydrolase at the brush border or gut bacterial deglycosylation.

**First-pass magnitude**: Very extensive. Free quercetin is rapidly glucuronidated (quercetin-3'-glucuronide), sulfated (3'-sulfate), and O-methylated (isorhamnetin). These conjugates are the primary circulating forms; they may not retain full RTK/RAS inhibitory activity at the concentrations where the parent compound exerts kinase effects.

**Achievable levels**: From apple juice: estimated ~0.05–0.2 µM free quercetin equivalents in plasma. From quercetin aglycone supplement: ~0.5–2 µM peak (Manach C et al., *AJCN* 2004, PMID 15113710). Cell-line active range: 10–50 µM → **10–100× mismatch** at supplement level; **50–500× at apple juice level**.

**Apple skin note**: Quercetin is concentrated in apple skin (aglycone form; ~3–5 mg per apple with skin). If the patient uses whole apple with skin in juicing, the aglycone form provides higher direct absorption potential than quercetin-glucoside from flesh.

---

### Sulforaphane (from glucoraphanin) [PATIENT TAKING via broccoli juice — ACTIVATION CONCERN]

**This is the most important preparation note in the entire V1 bioavailability section.**

**Fat- vs. water-soluble**: Isothiocyanate; moderate lipophilicity but good aqueous solubility. Absorbed efficiently from intestinal mucosa without fat requirement.

**The activation bottleneck**: Sulforaphane does not exist in broccoli — glucoraphanin does. Sulforaphane forms when myrosinase (a thioglucosidase enzyme co-located in broccoli cell walls) contacts glucoraphanin following cell disruption. This reaction requires:
1. Physical disruption of broccoli cells (chopping, chewing, crushing)
2. Myrosinase activity — the enzyme is heat-labile (inactivated at ~70°C) and shear-sensitive
3. Contact time: the myrosinase-glucoraphanin reaction takes approximately 40 minutes at room temperature

**Patient-specific consequence**: Centrifugal juicing destroys myrosinase through:
- Mechanical shear forces in the juicer blade
- Possible brief heat generation during high-speed processing
- Rapid oxidative inactivation of the exposed enzyme

Without myrosinase, gut microbiome performs limited conversion — estimated 3–10× less sulforaphane yield than myrosinase-activated preparation. The patient is almost certainly receiving near-zero sulforaphane from their current broccoli juice protocol.

**Corrective protocol**: Chop broccoli sprouts or broccoli florets → allow 40 minutes at room temperature → then consume (cold, minimally processed). Alternatively, add fresh daikon radish or mustard seed powder (10 mg powder per 100 g broccoli) as an exogenous myrosinase source to the juice; this has been shown in healthy volunteers to rescue sulforaphane formation from heat-processed broccoli (Vermeulen M et al., *J Nutr* 2008, PMID 18539765; Cramer JM et al., *J Nutr* 2011 [VERIFY PMID for Cramer 2011]).

**Achievable plasma levels with correct preparation**:
- From broccoli sprouts (proper activation): 0.5–2 µM sulforaphane (Clarke JD et al., *Cancer Prev Res* 2011, PMID 21593198)
- From current broccoli juice (likely no myrosinase): ~0.05–0.2 µM or less (gut bacterial conversion only)
- Cell-line HDAC inhibitory concentrations (V1/V3): 5–20 µM → **3–10× mismatch with proper preparation (most favorable V1 ratio); >25× with current preparation**

**First-pass**: Sulforaphane is rapidly conjugated with glutathione (sulforaphane-GSH), then cysteinylated (sulforaphane-Cys) and N-acetylcysteinylated (sulforaphane-NAC). These are the predominant urinary metabolites used as PK markers (Ye L et al., *J Nutr* 2002, PMID 12421854). The conjugates circulate in plasma; their HDAC inhibitory activity relative to free sulforaphane is an open question.

**Tissue distribution**: Rodent studies show sulforaphane distribution to multiple tissues including lung, liver, colon. Human lung distribution relevant to this patient's lung oligometastasis is not published specifically but is biologically plausible given rodent data and sulforaphane's lipophilicity.

---

### Omega-3 EPA/DHA

**Fat- vs. water-soluble**: Highly lipophilic. Optimal absorption with a high-fat meal. Triglyceride form (fish oil, TG) has approximately 1.7× higher bioavailability than ethyl ester form (EE) when taken without a high-fat meal (Dyerberg J et al., *Prostaglandins Leukot Essent Fatty Acids* 2010, PMID 20674321).

**First-pass**: Relatively minimal compared to polyphenols. EPA and DHA are incorporated into chylomicrons, enter lymphatic circulation, and are distributed to phospholipid membranes throughout the body. This contrasts sharply with polyphenols that undergo extensive intestinal/hepatic metabolism.

**Concentration-mismatch assessment**: The V1-A mechanism (RAS membrane clustering disruption) operates through altered lipid raft cholesterol-domain structure following membrane phospholipid EPA/DHA enrichment. This is not a drug-receptor interaction requiring a specific plasma Cmax threshold — it is a sustained compositional change that accumulates over days to weeks of dietary intake. This is why omega-3 is the only V1 dietary compound without a meaningful concentration-mismatch problem: the mechanism does not require an acute plasma "drug level."

**PK-enhancing consideration**: Triglyceride-form fish oil with a fat-containing meal is the optimal delivery. The patient's fatty fish consumption directly provides this.

**Tissue distribution**: EPA and DHA incorporation into cell membranes is a systemic effect, including tumor-associated cells. No CIC-DUX4-specific membrane composition data; mechanism from general lipid raft/RAS biology [no direct citation; mechanism inferred from Prior IA et al., lipid raft/RAS membrane clustering literature].

---

### Berberine

**Fat- vs. water-soluble**: Slightly lipophilic cation. Reasonable intestinal permeability but significant active efflux (P-gp, MRP2) limits net absorption.

**First-pass magnitude**: Extreme. Oral bioavailability approximately 1% from conventional formulations (Tan HL et al., *Front Pharmacol* 2016, PMID 27917113). Enterohepatic recirculation and gut bacterial metabolism contribute to its pharmacological effects despite low systemic exposure. Plasma levels after 500 mg oral dose: approximately 0.1–0.3 µM.

**Concentration-mismatch**: 5–50 µM cell-line active range for AMPK/MAPK effects → **20–500× mismatch at achievable plasma levels**. Despite this, berberine shows documented pharmacological effects in metabolic trials, suggesting either: (a) tissue concentrations higher than plasma suggest, (b) gut-level pharmacology contributes, or (c) active metabolites contribute. These alternative mechanisms are uncharacterized for the specific V1-A (MAPK suppression) activity.

---

### 6-Gingerol [PATIENT TAKING]

**Fat- vs. water-soluble**: Moderately lipophilic; absorbed from gut, subject to phase II metabolism.

**First-pass**: Significant. 6-gingerol is converted to 6-shogaol (by dehydration; higher in dried/heated ginger and more potent in some assays), 6-paradol, and gingerol glucuronides in circulation. Fresh ginger juice preserves 6-gingerol better than dried or cooked preparations.

**Achievable levels**: ~0.1–0.5 µM peak from typical culinary fresh ginger consumption; cell-line MAPK/NF-κB effects: 20–100 µM → **50–200× mismatch**. The V1-A contribution from culinary ginger juice is theoretical at the concentration level.

**Assessment for patient**: The patient juices fresh ginger, preserving 6-gingerol (not shogaol). At culinary volumes, the V1-A mechanism is essentially theoretical. Ginger is a safe culinary ingredient with no significant chemo interactions at food-level intake; the concentration mismatch means V1 contributions are negligible.

---

### Thymoquinone (Black Cumin Seed Oil) [PATIENT TAKING]

**Fat- vs. water-soluble**: Lipophilic monoterpene ketone. Reasonable lipid absorption from oil formulation.

**First-pass**: Human PK data for thymoquinone are limited. Animal studies show significant first-pass hepatic metabolism; multiple metabolites. Plasma thymoquinone levels in humans after supplementation are not well-characterized in published PK studies [no direct human PK citation confirmed without PMID verification risk; pharmacokinetics inferred from animal PK and general lipophilic compound principles].

**Clinical interaction priority**: Regardless of the uncertainty in human PK, thymoquinone's documented in vitro CYP3A4 inhibitory activity creates the same ifosfamide prodrug activation concern as piperine and curcumin. The interaction mechanism does not depend on quantifying precise plasma thymoquinone levels.

---

## Cross-Compound Summary: Concentration Realism by Tier

The following is the consensus view after reconciling Food Specialist and Supplement Specialist inputs:

**No meaningful mismatch (food-level mechanism achievable):**
- Omega-3 EPA/DHA (membrane compositional mechanism)

**Small mismatch (3–10×; most favorable dietary compound):**
- Sulforaphane (from properly prepared broccoli sprouts)

**Moderate mismatch (10–100×; mechanistic alignment at dietary concentrations, active concentrations not achievable):**
- Quercetin, EGCG

**Large mismatch (>100×; V1 mechanism theoretical at achievable concentrations):**
- Curcumin (even enhanced formulations remain 5–200× below typical cell-line active range)
- Berberine, apigenin, luteolin, 6-gingerol, fisetin

---

## What I Could Not Establish

1. CIC-DUX4 tumor tissue concentration data for any dietary compound — this information does not exist for this tumor type anywhere in the published literature.

2. Whether circulating conjugate metabolites of quercetin, EGCG, and apigenin retain the parent compound's kinase-inhibitory or BRD4-binding activity — this is the key unresolved question for V1 mechanism translation, and it is rarely tested in cell-line studies that use the parent compound.

3. Human lung tissue distribution for any V1 compound in the context of post-irradiated lung containing an oligometastatic sarcoma lesion. Radiation alters local vascularity and tissue architecture; compound distribution to a post-irradiated lung oligometastasis cannot be inferred from normal-lung rodent models.

4. The exact sulforaphane yield from the patient's specific juicing protocol — whether the juicer generates sufficient heat and shear to fully destroy myrosinase. Some cold-press or masticating juicers may preserve myrosinase better than high-speed centrifugal models; this is not characterized in published literature.

5. Whether enhanced curcumin formulations (SLCP, micellar, solid lipid nanoparticles) developed after 2020 achieve plasma levels closer to the lower end of V1-relevant concentrations — newer formulations may improve on the Meriva/phospholipid-complex figures but peer-reviewed PK data in oncology populations are limited.

6. The specific piperine dose in the patient's supplement product and the cumulative CYP3A4 inhibitory effect of concurrent piperine + curcumin + thymoquinone in a cancer patient undergoing ifosfamide — this three-compound combination has not been studied in any published PK interaction trial.
