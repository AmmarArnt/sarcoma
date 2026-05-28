# V1 Rate Limiting — Food Sources
# Sub-agent role: Food Specialist
# Output for: Vector 1 Team Lead reconciliation

Summary: Food sources for V1 rate-limiting compounds — highest-density realistic sources, preparation notes, and bioactive-form flags. Excludes supplement dosing and PK data (those are in the Supplement and Bioavailability outputs). All evidence tiers reflect the compound's mechanistic relevance to V1 targets, not food-level efficacy claims.

---

## Patient Regimen Assessment (SPECIFIC PATIENT CASE)

The patient is self-administering the following during rest weeks and the NED/surveillance period. Each item is tagged [PATIENT TAKING] and assessed for V1 relevance.

| Compound | Patient Context | V1 Layer | Assessment |
|---|---|---|---|
| Curcumin + piperine | [PATIENT TAKING] Active during chemo rest weeks and NED year | B (BRD4/super-enhancer) | V1-relevant; piperine is a strong CYP3A4/P-gp inhibitor — CRITICAL interaction flag with imminent high-dose ifosfamide (CYP3A4 prodrug activation) and vincristine/etoposide (P-gp substrates). See supplement and bioavailability outputs. |
| Liposomal vitamin C | [PATIENT TAKING] Active during chemo rest weeks and NED year | V2 primarily, minor V1 | Not a primary V1 compound. V2-relevant (ROS scavenging). High-dose antioxidant during cytotoxic chemo is a documented concern. |
| Black cumin seed oil (Nigella sativa / thymoquinone) | [PATIENT TAKING] Active during chemo rest weeks and NED year | B (mechanistic, weak) | Thymoquinone has NF-κB and MAPK-modulatory activity in cell lines; mechanistically V1-B/C adjacent. CYP3A4 inhibition documented. Flag for imminent ifosfamide. |
| Vitamin D | [PATIENT TAKING] Active during chemo rest weeks and NED year | V3/V4 primarily | Not primary V1. Cross-vector (V3 differentiation axis, V4 NK support). Deficiency correction has clearer evidence than supplementation in repleted individuals. |
| Honey | [PATIENT TAKING] Active | Minimal V1 specificity | Contains trace polyphenols (kaempferol, quercetin, caffeic acid); concentrations at culinary intake are well below any studied V1 mechanism concentration. Mechanistic tier, very weak. |
| Fresh juice: celery, ginger, carrot, broccoli, apple, beetroot | [PATIENT TAKING] Active during chemo rest weeks | Multiple V1 layers | See individual compounds below. Juicing destroys myrosinase in broccoli — glucoraphanin → sulforaphane conversion will not occur unless raw chopped broccoli florets are added after juicing. |

---

## Compound-by-Compound Food Source Table

| Compound | Best food source | Realistic serving | Preparation note | Bioactive form | V1 layer | Evidence tier | CIC-DUX4 direct? |
|---|---|---|---|---|---|---|---|
| **Quercetin** [PATIENT TAKING via apple juice] | Capers (highest), raw red onion (outer layers), kale, elderberries | Capers: 1 tbsp (10g) ≈ 23 mg quercetin; red onion: half cup raw ≈ 20–30 mg | Eat raw — heat destroys quercetin aglycone. Apple skin retains more than peeled. Juice significantly reduces vs. whole fruit | Quercetin aglycone (from onion); quercetin glucoside (from apple — requires gut deglycosylation) | A (RTK/RAS) + B (EZH2 modulation, weak) | Preclinical-Cell; concentration caveat: active concentrations in cell studies (10–50 µM) are 10–100× above achievable plasma | None direct |
| **EGCG** | Matcha (highest catechin density), brewed green tea | Matcha: 1 tsp (2g) in 70°C water ≈ 70–140 mg EGCG; brewed green tea (3 min, 70–80°C): ≈ 50–100 mg/cup | Brew at 70–80°C, not boiling — high temperature degrades catechins. Avoid milk (binds catechins). Freshly brewed; no long steeping | EGCG (epigallocatechin-3-gallate) — parent compound; major circulating metabolite EGC-glucuronide | B (BRD4 BD1 binding, H3K27ac modulation) | Preclinical-Cell; concentration caveat: reported BRD4 binding at 10–50 µM; dietary plasma peaks ~0.1–0.5 µM | None direct |
| **Curcumin** [PATIENT TAKING] | Turmeric root (fresh > dried); curry paste > powder | 1 tsp ground turmeric ≈ 200 mg curcumin total curcuminoids | Bioavailability is the rate-limiting issue — see bioavailability.md. Take with fat and black pepper (piperine); **piperine has documented CYP3A4 and P-gp inhibitory activity — critical interaction with ifosfamide prodrug activation and P-gp substrates vincristine/etoposide — see supplement-protocol.md** | Curcumin (diferuloylmethane); demethoxycurcumin; bisdemethoxycurcumin | B (BRD4-chromatin disruption) | Preclinical-Cell; concentration caveat: activity at 5–20 µM; food-derived plasma peaks well below this without enhancement | None direct |
| **Sulforaphane** [PATIENT TAKING via broccoli juice — ACTIVATION CONCERN] | Broccoli sprouts (50–100× higher glucoraphanin than mature broccoli) | 1 oz (28g) fresh broccoli sprouts; mature broccoli florets: 1 cup cooked | CRITICAL: sulforaphane is NOT in the food — it is formed when glucoraphanin contacts myrosinase (a plant enzyme released by chopping/chewing). Juicing destroys myrosinase. Heating above 70°C also inactivates myrosinase. For juice: chop fresh sprouts, let stand 40 min at room temperature BEFORE adding to juice or consuming | Sulforaphane (isothiocyanate); metabolized to sulforaphane-NAC mercapturic acid | B (weak class-I HDACi in cell lines) + cross-vector V3/V4 | Preclinical-Cell | None direct |
| **Apigenin** [PATIENT TAKING via celery juice] | Celery (parsley has higher density), chamomile tea | Celery: 1 cup raw ≈ 3–8 mg apigenin; parsley fresh: 2 tbsp ≈ 10–15 mg | Minimal heat effect; celery juice retains apigenin. Parsley > celery for density. Chamomile tea: ≈ 3 mg/cup | Apigenin (free aglycone); apigenin-7-glucoside (glucoside requires gut deglycosylation) | B/C (ETS factor expression reduction; cell-cycle modulation) | Preclinical-Cell | None direct |
| **Luteolin** [PATIENT TAKING via celery juice] | Celery leaves (higher than stalks), thyme, parsley, green pepper | Celery: modest amounts; fresh thyme: 1 tbsp ≈ 5 mg | Leaves contain more than stalks; juice retains meaningful luteolin | Luteolin aglycone | C (cell-cycle modulation) | Preclinical-Cell | None direct |
| **6-Gingerol** [PATIENT TAKING via ginger juice] | Fresh ginger root | 1 tsp fresh grated ginger ≈ 1–4 mg 6-gingerol | Fresh ginger contains 6-gingerol; drying/cooking converts to 6-shogaol (different but related). Juice retains gingerols | 6-Gingerol; 6-shogaol (from heat/drying) | A (NF-κB/MAPK modulation at high doses in cell studies; weak RAS context) | Preclinical-Cell; concentration caveat: mechanisms studied at concentrations not achievable from culinary intake | None direct |
| **Beta-carotene** [PATIENT TAKING via carrot juice] | Carrots, sweet potato, butternut squash, leafy greens | 1 medium carrot ≈ 5–8 mg β-carotene | Juice retains β-carotene. Fat co-ingestion (olive oil) improves carotenoid absorption significantly | β-carotene (provitamin A precursor); converted to retinol by BCMO1 | V2/V3 primarily (retinoid signaling); NOT primary V1 | Dietary-Observational; **CROSS-FLAG to V2/V3: ATBC/CARET signal — β-carotene SUPPLEMENTATION increased lung cancer in heavy smokers. Food-level intake is different from supplementation. Patient is consuming via juice (food-level), which is categorically different. Document the distinction.** | None direct |
| **Omega-3 EPA/DHA** | Atlantic mackerel, sardines (canned in water), wild salmon, herring, oysters | Sardines 100g ≈ 1.5–2g EPA+DHA; mackerel 100g ≈ 2–3g | Minimize heat; cold-water fish. Canned in water preserves EPA/DHA better than oil-packed (paradoxically, oil-packed leaches DHA into the packing oil which is then discarded) | EPA (eicosapentaenoic acid), DHA (docosahexaenoic acid) | A (lipid raft / RAS membrane clustering disruption) | Dietary-Observational + Mechanistic; cross-vector V1+V2+V4 | None direct |
| **Fisetin** | Strawberries (highest by weight), mangoes, apples (skin), persimmons | Strawberries 100g ≈ 16 mg fisetin; apple (with skin) ≈ 0.03 mg/g | Highest in strawberries; concentration in apple skin; juicing retains fisetin | Fisetin (flavonol) | C (ETS inhibition; CDK4 suppression) | Preclinical-Cell; senolytic literature in aging models | None direct |
| **Selenium** | Brazil nuts, sardines, eggs, tuna | Brazil nuts: 1 nut ≈ 70–90 µg selenium (RDA = 55 µg; upper limit = 400 µg/day) | **FLAG: upper limit for selenium is narrow. 1–2 Brazil nuts/day delivers RDA; more than 4–5/day may approach UL.** Not "more is better" | Selenocysteine (in protein), selenomethionine (in plants/nuts) | C (apoptosis threshold, selenoprotein cofactor) | Preclinical + Dietary-Observational | None direct |
| **Zinc** | Oysters (highest), beef, pumpkin seeds, hemp seeds | Oysters 6 medium ≈ 32 mg zinc; pumpkin seeds 30g ≈ 2.5 mg (RDA = 8–11 mg) | No special preparation needed. Plant zinc is less bioavailable due to phytate; soaking/sprouting seeds reduces phytate | Zinc ion (Zn²⁺) | C (DNA repair + cell-cycle modulation); cross-vector V2+V4 | Preclinical; deficiency correction well-supported; excess interferes with copper absorption | None direct |
| **Berberine** | Primarily supplemental — barberries contain trace amounts; Oregon grape root | Barberries: very low dietary density; supplemental is the realistic route | Supplemental primarily — see supplement-protocol.md | Berberine (isoquinoline alkaloid) | A (AMPK → MAPK suppression) | Preclinical-Cell; oral bioavailability ~1% from conventional formulations | None direct |
| **Lycopene** | Cooked/processed tomatoes (higher than raw), watermelon, pink grapefruit | Tomato paste 2 tbsp ≈ 10–15 mg lycopene; raw tomato ≈ 3 mg | Heat processing increases lycopene bioavailability from tomatoes (disrupts cell walls, converts all-trans to cis-lycopene which is better absorbed). Fat co-ingestion required | Cis-lycopene (higher absorption) | A (ERK pathway — mechanistic, mostly prostate literature) | Dietary-Observational (primarily prostate cancer); Mechanistic for V1-A | None direct |
| **Thymoquinone (black cumin / Nigella sativa)** [PATIENT TAKING] | Black cumin seed oil | Culinary use of seeds; oil standardized to thymoquinone content | CYP3A4 inhibition documented — **critical flag for ifosfamide prodrug activation. Do not combine with imminent high-dose ifosfamide cycle without oncologist review.** | Thymoquinone (active constituent of Nigella sativa) | B/C (NF-κB, MAPK modulation; apoptosis in cell lines) | Preclinical-Cell | None direct |

---

## Key Preparation Alerts

1. **Broccoli juicing destroys sulforaphane activation**: The patient's broccoli juice will not yield meaningful sulforaphane unless raw, freshly chopped broccoli (with intact myrosinase) is used. Chop → wait 40 min → then consume. Heat (even gentle) inactivates myrosinase.

2. **Apple in juice**: Quercetin is concentrated in the skin. If juiced with skin, quercetin is retained. Without skin, minimal quercetin.

3. **Curcumin + piperine during ifosfamide**: Piperine is a documented CYP3A4 and P-gp inhibitor. Ifosfamide is a CYP3A4-activated prodrug. Inhibiting CYP3A4 could reduce ifosfamide activation to its active metabolite, potentially reducing efficacy. This is the highest-priority interaction flag for this patient's imminent high-dose ifosfamide course. Vincristine and etoposide (P-gp substrates) would also be affected.

4. **Carrot juice / beta-carotene**: Food-level beta-carotene from carrot juice is categorically different from the supplementation doses used in ATBC/CARET (20–25 mg/day as isolated supplement). The harm signal applies to supplementation, not food intake. Cross-flag to V2/V3 for completeness, but do not apply the ATBC/CARET harm signal to dietary carrot consumption.

---

## What This Output Could Not Establish

- Realistic sulforaphane delivery from the patient's current broccoli juice preparation (likely near-zero from juiced broccoli without the myrosinase activation step)
- Whether the quercetin from apple juice (primarily quercetin glucoside, requiring gut deglycosylation) reaches plasma levels comparable to the quercetin aglycone studied in V1-A cell-line work
- Ginger (6-gingerol) concentrations at culinary intake — mechanism is clear; whether plasma levels from juice approach V1-A active concentrations is not established
- Specific PK data for thymoquinone from black cumin seed oil at the patient's dose — see supplement-protocol.md
