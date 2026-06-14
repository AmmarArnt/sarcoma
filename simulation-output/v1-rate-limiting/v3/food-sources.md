# V1 Rate Limiting — Food Sources (v3 clean-slate run)
## Sub-agent role: Food Specialist
## Output for: V1 Team Lead reconciliation (v3)

**Summary**: Food-source table for V1 rate-limiting candidate compounds (standard V1 list: quercetin,
omega-3 EPA/DHA, EGCG, curcumin, sulforaphane, fisetin, selenium, berberine, apigenin, kaempferol,
genistein, luteolin, zinc, lycopene) PLUS the bioactives present in this patient's self-administered
juice/food regimen (β-carotene from carrot, sulforaphane from broccoli, apigenin/luteolin from celery,
6-gingerol from ginger, quercetin from apple, dietary nitrate from beetroot, thymoquinone from black
cumin seed oil, curcumin from turmeric). Excludes supplement dosing (Supplement Specialist) and PK/
absorption-enhancement data (Bioavailability Specialist). Evidence tiers reflect mechanistic relevance to
V1 targets (RAS/ERK, BRD4/super-enhancer, CDK4/CCND1), not food-level efficacy claims against CIC-DUX4.

**Confidence**: Medium — the mechanisms are well-described in cell-line and dietary-epidemiology
literature, but almost every entry has a concentration-achievability gap between the studied active
concentration and what culinary/juice intake delivers; this is flagged per-entry rather than averaged away.

---

## Patient Case Anchor (clean-slate v3)

Soft-tissue CIC-rearranged sarcoma (fusion-unconfirmed, ~5% atypical subgroup), biceps femoris primary
with lung metastases at diagnosis (June 2024), VDC/IE ×14, surgery + bilateral lung/leg radiation, NED
May 2025–May 2026, oligometastatic lung relapse May 2026, **about to begin high-dose ifosfamide**.
Self-administered regimen: curcumin + piperine, liposomal vitamin C, black cumin seed oil (Nigella
sativa / thymoquinone), vitamin D, honey, and fresh juice of celery/ginger/carrot/broccoli/apple/beetroot.

Per golden rule #9 (atypical-case flag): none of the entries below depend on the CIC-DUX4 fusion junction
being present — all are fusion-agnostic pathway-level (RAS/ERK, BRD4, CDK4/CCND1) interventions, so they
remain potentially applicable to this fusion-unconfirmed case. No entry in this table should be read as
fusion-dependent.

---

## Compound-by-Compound Food Source Table

| Compound | V1 Layer | Best food source | Realistic serving | Preparation note | Bioactive form | Evidence tier | CIC-DUX4 direct? |
|---|---|---|---|---|---|---|---|
| **Quercetin** [PATIENT TAKING — apple juice] | A (RAS/RTK) + weak EZH2 (V3 overlap) | Capers (highest density), raw red onion (outer/red layers), kale, apples with skin, elderberries | Capers 1 tbsp (~10 g) ≈ 8–23 mg quercetin; raw red onion ½ cup ≈ 20–30 mg; medium apple with skin ≈ 4–5 mg | Quercetin aglycone is heat- and light-labile in solution and oxidizes on cut-surface exposure to air; eat raw or lightly cooked, minimize standing time after cutting. Apple skin carries the great majority of the fruit's quercetin (as glycosides) — juicing with skin retains it, peeling removes it almost entirely | Quercetin-3-glucosides/rutinoside in apple/onion (require gut β-glucosidase deglycosylation before absorption); free aglycone in capers | Preclinical-Cell; **concentration mismatch**: RAS/RTK-modulatory concentrations in cell studies are typically 10–50 µM, while dietary plasma Cmax after a quercetin-rich meal is roughly 0.1–1 µM `[no direct citation; mechanism inferred from quercetin pharmacokinetic literature broadly]` | None direct |
| **Omega-3 EPA/DHA** | A (lipid-raft RAS membrane clustering) | Atlantic mackerel, sardines (canned in water), wild salmon, herring, oysters | Sardines 100 g ≈ 1.5–2 g EPA+DHA; mackerel 100 g ≈ 2–3 g; 2–3 servings/week is the typical dietary-pattern unit in cardiovascular/oncology epidemiology | Minimal heat exposure preferred — high-heat frying oxidizes long-chain PUFAs; canned-in-water retains EPA/DHA better than oil-packed (oil-packed loses some DHA into discarded packing oil). ALA from flax/chia/walnut converts to EPA/DHA at only ~5–10% efficiency and is not a substitute | EPA (eicosapentaenoic acid), DHA (docosahexaenoic acid) — long-chain n-3 PUFAs | Dietary-Observational + Mechanistic; cross-vector V1+V2+V4 (anti-inflammatory, TME) | None direct |
| **EGCG** | B (reported BRD4 BD1 binding; H3K27ac modulation) | Matcha (whole-leaf, highest catechin density), brewed green tea | Matcha 1 tsp (~2 g) whisked in hot (not boiling) water ≈ 70–140 mg EGCG; brewed green tea (3–5 min, 70–80 °C) ≈ 50–100 mg/cup | Brew at 70–80 °C — near-boiling water accelerates catechin epimerization/degradation. Avoid adding milk (casein binds catechins, reducing free EGCG). Consume freshly brewed; EGCG oxidizes on standing, especially at higher pH | EGCG (epigallocatechin-3-gallate); circulating mostly as glucuronide/sulfate/methylated metabolites | Preclinical-Cell; **concentration mismatch**: BRD4 BD1-binding and H3K27ac effects reported at 10–50 µM in cell lines vs. dietary plasma EGCG peaks around 0.1–0.5 µM `[no direct citation; mechanism inferred from EGCG pharmacokinetic literature broadly]` | None direct |
| **Curcumin** [PATIENT TAKING — turmeric + piperine] | B (BRD4-chromatin disruption; broad polypharmacology) | Fresh turmeric rhizome (modestly higher curcuminoid density than dried, plus retains volatile oils); turmeric powder in curry pastes | ~1 tsp (≈2–3 g) ground turmeric ≈ 150–250 mg total curcuminoids (curcumin + demethoxy- + bisdemethoxycurcumin) | Curcumin is fat-soluble and heat-stable to typical cooking temperatures but degrades under prolonged high heat and at alkaline pH; cooking in oil/ghee with black pepper is the traditional preparation that maximizes both solubility and absorption. **CHEMO-INTERACTION FLAG**: piperine (black pepper) is a documented CYP3A4 and P-glycoprotein inhibitor — see Chemo-Interaction Screening below; this is the single highest-priority flag in this table given the imminent high-dose ifosfamide course | Curcumin (diferuloylmethane) + demethoxycurcumin + bisdemethoxycurcumin (curcuminoid mixture) | Preclinical-Cell; **concentration mismatch**: BRD4-disruption and chromatin effects reported at 5–20 µM, while unenhanced oral curcumin yields plasma concentrations in the low-nanomolar range `[no direct citation; mechanism inferred from curcumin oral bioavailability literature broadly]` — see bioavailability.md for the Shoba 1998 piperine-enhancement caveat | None direct |
| **Sulforaphane** [PATIENT TAKING — broccoli juice; see activation analysis below] | B (weak class-I HDACi in cell lines); cross-vector V3 (MHC-I/differentiation) and V4 | Broccoli sprouts (3-day-old sprouts carry roughly 10–100× the glucoraphanin density of mature broccoli florets by fresh weight — figures vary widely by cultivar/growing conditions, treat as order-of-magnitude); mature broccoli florets as the realistic whole-food alternative | Broccoli sprouts: ~1 oz (28 g) fresh, chopped/chewed; mature broccoli: ~1 cup chopped, raw or lightly steamed (steaming <3–4 min preserves more myrosinase than boiling) | **See "Juicing and Sulforaphane Activation" section below — this is the mechanistically important question for this patient's regimen.** Bottom line: sulforaphane is not present preformed in the plant — it is generated from the inert precursor glucoraphanin by the plant enzyme myrosinase, released on cellular disruption (chopping/chewing/blending). Juicing DOES disrupt cells and release myrosinase, so a freshly made broccoli juice is not myrosinase-free at the moment of blending — but myrosinase is heat-labile (largely inactivated above ~60 °C) and the reaction needs minutes of contact time at room temperature to go to completion. The bigger loss mechanism in commercial/long-rest juicing is **epithiospecifier protein (ESP)**-driven diversion of the glucoraphanin–myrosinase reaction toward sulforaphane nitrile (an inactive byproduct) rather than sulforaphane itself — ESP is concentrated in mature broccoli more than in young sprouts | Sulforaphane (an isothiocyanate, generated enzymatically from glucoraphanin, a glucosinolate); urinary/plasma metabolites are sulforaphane–mercapturic-acid pathway conjugates (e.g., sulforaphane-N-acetylcysteine) | Preclinical-Cell (HDAC modulation); human bioavailability data exist (see below) but CIC-DUX4-specific data: none | None direct |
| **Apigenin** [PATIENT TAKING — celery juice] | B/C (reduces ETS-factor expression in some lines; cell-cycle modulation) | Parsley (much higher density than celery), celery (stalks and leaves), chamomile tea | Celery 1 cup raw, chopped ≈ 3–8 mg apigenin; fresh parsley 2 tbsp ≈ 10–15 mg; chamomile tea ≈ 1–3 mg/cup | Apigenin is relatively heat-stable compared to other flavones but is concentrated in the leaves more than the stalks — using celery leaves (often discarded) increases yield. Juicing retains apigenin reasonably well since it is not highly oxidation-sensitive | Apigenin-7-O-glucoside (predominant dietary form, requires gut/microbial deglycosylation); free aglycone present in smaller amounts | Preclinical-Cell; **concentration mismatch**: ETS-suppression and cell-cycle effects reported at 10–40 µM in vitro vs. dietary plasma levels in the low-nanomolar to sub-µM range `[no direct citation; mechanism inferred from apigenin pharmacokinetic literature broadly]` | None direct |
| **Luteolin** [PATIENT TAKING — celery juice] | C (cell-cycle modulation) | Celery leaves (higher than stalks), fresh thyme, parsley, sweet green pepper | Celery: modest amounts, concentrated in leaves; fresh thyme 1 tbsp ≈ 3–5 mg | Similar stability profile to apigenin (both flavones); using whole celery including leaves increases luteolin content. Juicing retains luteolin | Luteolin-7-O-glucoside (dietary form); aglycone after deglycosylation | Preclinical-Cell; concentration mismatch as above for flavones | None direct |
| **6-Gingerol** [PATIENT TAKING — ginger juice] | A (NF-κB/MAPK modulation reported at high in-vitro concentrations; weak RAS-adjacent context) | Fresh ginger rhizome | 1 tsp fresh grated ginger ≈ 1–4 mg 6-gingerol (highly variable by cultivar/freshness) | 6-Gingerol is the dominant pungent compound in **fresh** ginger; drying and prolonged heating convert much of it to 6-shogaol (a dehydration product with a distinct, generally more potent but differently-studied pharmacology) via retro-aldol/dehydration. Juicing fresh ginger preserves 6-gingerol; cooked/dried ginger preparations shift the profile toward 6-shogaol | 6-Gingerol (fresh); 6-shogaol (heat/dried — a different, related bioactive, not interchangeable in the cited mechanism studies) | Preclinical-Cell; **concentration mismatch**: NF-κB/MAPK-modulatory concentrations in published cell studies (often 10–100 µM) are well above what culinary-juice intake of fresh ginger plausibly delivers systemically `[no direct citation; mechanism inferred from ginger pharmacokinetic literature broadly]` | None direct |
| **β-Carotene** [PATIENT TAKING — carrot juice] | NOT primary V1 — V3 differentiation-pathway substrate (retinoic-acid signaling); flagged here because patient is actively consuming it via juice | Carrots, sweet potato, butternut squash, dark leafy greens (kale, spinach) | 1 medium carrot ≈ 5–8 mg β-carotene; carrot juice concentrates this further per serving | Fat-soluble — co-ingestion with oil (a splash of olive oil with carrot juice, or cooking carrots in fat) substantially increases carotenoid absorption vs. carrot alone. Cooking/blending disrupts the cell matrix and modestly increases bioaccessibility relative to raw whole carrots, though juicing vs. cooking differences are second-order compared to the fat-co-ingestion effect | β-carotene (provitamin A carotenoid); converted to retinol via BCMO1 in enterocytes/liver | Dietary-Observational; **CROSS-VECTOR FLAG (V2/V3) — ATBC and CARET trials**: isolated high-dose β-carotene **supplementation** (20–30 mg/day as a pharmacologic supplement) *increased* lung-cancer incidence in heavy smokers/asbestos-exposed workers in two large RCTs (ATBC 1994; CARET — Omenn et al. 1996). This is a supplement-dose finding in a specific high-risk population (active smokers), not a finding about whole-food carotenoid intake from carrots/vegetables, which is consistently associated with lower cancer risk in observational data. The mechanistic hypothesis for the harm signal involves pro-oxidant β-carotene cleavage products (e.g., apo-carotenals) accumulating in oxidatively stressed lung tissue already primed by tobacco smoke — a tissue/exposure context that does not map onto V1's RAS/ERK/BRD4/CDK4 targets in soft-tissue sarcoma. **This patient is not a smoker and is consuming carrot juice as a whole food, not an isolated β-carotene supplement** — the ATBC/CARET signal is noted for completeness and cross-vector awareness (V3 retinoid-differentiation track), not because it is judged directly applicable here. `[no direct citation beyond ATBC 1994 / CARET (Omenn et al., NEJM 1996); mechanism for the harm signal inferred from carotenoid oxidation literature broadly]` | None direct |
| **Dietary nitrate** [PATIENT TAKING — beetroot juice] | Not a classical V1-A/B/C target; included because it is a major bioactive in the patient's juice regimen and has a plausible RAS/ERK-adjacent link via nitric-oxide signaling | Beetroot, beet greens, spinach, arugula, celery (all high-nitrate vegetables) | One beetroot or ~250 mL beet juice delivers a substantial dietary nitrate dose by epidemiological-study standards | Nitrate is water-soluble and largely retained in juice. Oral bacteria (not gastric/systemic enzymes) reduce dietary nitrate to nitrite, which is further converted to nitric oxide (NO) in acidic gastric conditions and tissue; **antibacterial mouthwash use blocks this conversion** — a practical note if the patient uses one | Nitrate (NO3⁻) → nitrite (NO2⁻, via oral bacterial nitrate reductase) → nitric oxide (NO) | Dietary-Observational + Mechanistic (NO signaling is well-established in vascular biology; **direct RAS/ERK-pathway link in CIC-DUX4 or sarcoma is not established** — included here as a patient-regimen bioactive, not as a scored V1 candidate) `[no direct citation; mechanism inferred from dietary nitrate/NO physiology literature broadly]` | None direct |
| **Thymoquinone (black cumin seed oil / Nigella sativa)** [PATIENT TAKING] | B/C — NF-κB and MAPK pathway modulation reported in cell lines; weak mechanistic overlap with V1-A/B | Nigella sativa seeds (black cumin/black seed); cold-pressed black seed oil is the patient's actual intake form | Culinary use of whole/ground seeds in cooking (common in some South Asian, Middle Eastern, North African cuisines) is the food-level analogue; the patient's oil-based intake is closer to a concentrated extract than a culinary food portion — **this entry is included for V1 mechanistic completeness, but the patient's actual product is better assessed by the Supplement Specialist for dose/standardization** | **CHEMO-INTERACTION FLAG**: thymoquinone and Nigella sativa extracts inhibit hepatic CYP3A4 (and CYP2C9, CYP2D6, CYP1A2) in human liver microsome studies — see Chemo-Interaction Screening below. This is the second major CYP3A4-relevant flag in this patient's regimen alongside piperine, and both converge on the same imminent high-dose ifosfamide concern | Thymoquinone (2-isopropyl-5-methyl-1,4-benzoquinone), the principal bioactive quinone of Nigella sativa seed oil | Preclinical-Cell; **concentration mismatch**: CYP3A4 inhibition IC50 reported around 25 µM in human liver microsomes, with substantial inhibition (~79%) at 100 µM `[Badary et al. and related human-liver-microsome CYP-inhibition studies; WebSearch-verified existence of this literature, specific PMID not retrieved this session — VERIFY]`; whether the patient's oil dose reaches hepatic concentrations in this range is not established | None direct |
| **Fisetin** | C (ETS inhibition; CDK4 suppression; senolytic literature) | Strawberries (by far the highest dietary density), mangoes, apples (skin), persimmons, kiwi | Strawberries 100 g (≈ ¾ cup) ≈ 16 mg fisetin — the only food source delivering fisetin at a level discussed in the literature as nutritionally meaningful | Fisetin is relatively stable to normal food handling; freezing/thawing strawberries does not destroy it. Apple skin contributes a much smaller amount (~0.03 mg/g) — strawberries dominate | Fisetin (3,3′,4′,7-tetrahydroxyflavone) — free aglycone | Preclinical-Cell; senolytic-context literature is mostly Preclinical-Animal in aging models, not cancer-specific | None direct |
| **Selenium** | C (apoptosis threshold; selenoprotein/thioredoxin-reductase cofactor) | Brazil nuts (by far the most concentrated dietary source), sardines, eggs, tuna, sunflower seeds | **Brazil nuts: 1–2 nuts/day** is sufficient to meet/exceed the adult RDA (55 µg/day) given that a single Brazil nut can contain 50–100+ µg depending on soil selenium content | **RDA-UPPER-LIMIT FLAG**: tolerable upper intake level (UL) for adults is 400 µg/day. Because Brazil nut selenium content is highly variable and can be very high per nut, regularly eating more than a small handful (more than ~4–5/day) risks approaching or exceeding the UL — selenosis (hair/nail changes, GI symptoms, neurological symptoms at chronic excess) is a real, documented harm. "1–2 per day" is the safe framing; "more is better" is explicitly not supported | Selenomethionine (plant/nut form, the dominant dietary form); selenocysteine (animal/selenoprotein form) | Preclinical + Dietary-Observational; narrow safety window is well-established (not a CIC-DUX4-specific finding) | None direct |
| **Berberine** | A (AMPK activation → MAPK suppression) | Not meaningfully present in common foods — barberries (Berberis vulgaris) contain trace amounts; Oregon grape root and goldenseal are botanical (non-culinary) sources | No realistic food serving delivers berberine at studied concentrations — this is a supplement-route compound | N/A at food level — see supplement-protocol.md | Berberine (isoquinoline alkaloid) | Preclinical-Cell; oral bioavailability from conventional formulations is reported as very low (~1%), a major limiting factor regardless of source | None direct |
| **Lycopene** | A (ERK pathway downregulation — evidence base is overwhelmingly prostate-cancer literature) | Cooked/processed tomato products (tomato paste, sauce — higher bioavailable lycopene than raw tomato), watermelon, pink grapefruit, guava | Tomato paste 2 tbsp ≈ 10–15 mg lycopene; raw tomato ≈ 3 mg per medium fruit | Heat processing (the opposite of most polyphenols) INCREASES lycopene bioavailability — cooking disrupts the tomato cell matrix and isomerizes some all-trans-lycopene to cis-isomers, which are absorbed more efficiently. Co-ingestion with fat (olive oil in tomato sauce) is required for meaningful absorption of this fat-soluble carotenoid | Cis-lycopene isomers (more bioavailable after cooking) vs. all-trans-lycopene (predominant in raw tomato) | Dietary-Observational (predominantly prostate-cancer epidemiology); Mechanistic for the ERK-downregulation link in other tissue contexts | None direct |
| **Zinc** | C (DNA-repair + cell-cycle modulation); cross-vector V2 (Ku70/Ku80, p53 zinc finger) + V4 (NK development) | Oysters (by far the most concentrated source), beef, pumpkin seeds, hemp seeds, cashews | Oysters: 6 medium ≈ 30–32 mg zinc (well above RDA of 8–11 mg — oysters are an occasional, not daily, food); pumpkin seeds 30 g ≈ 2.5 mg | No special preparation required for animal sources. Plant zinc (pumpkin/hemp seeds, legumes) is less bioavailable due to phytate binding; soaking, sprouting, or fermenting legumes/seeds reduces phytate and improves zinc absorption | Zn²⁺ (zinc ion), bound to dietary protein/phytate depending on source | Preclinical (deficiency-correction literature is the strongest part of this evidence base); excess zinc displaces/antagonizes copper absorption — flag if considering supplementation beyond dietary intake (Supplement Specialist territory) | None direct |
| **Kaempferol** | B (BRD4/MYC-axis-related, mechanistic) | Capers, kale, spinach, leeks, broccoli, dill, chives | Capers 1 tbsp ≈ small but measurable amount alongside quercetin (the two co-occur in many of the same foods); kale/spinach 1 cup raw ≈ low-single-digit mg | Similar handling profile to quercetin — both are flavonols, both somewhat heat- and oxidation-sensitive; raw or lightly cooked leafy greens preserve more than prolonged boiling (which leaches flavonols into discarded cooking water) | Kaempferol glycosides (predominant dietary form); aglycone after deglycosylation | Mechanistic (weakest tier in this table — BRD4/MYC-axis link is plausibility-based, not demonstrated for kaempferol specifically at dietary concentrations) `[no direct citation; mechanism inferred from flavonol/BRD4 literature broadly]` | None direct |
| **Genistein** | C (CDK inhibition; G2/M arrest); estrogenic activity is real and should be named, not hidden | Soybeans and soy foods (tofu, tempeh, edamame, miso) — essentially the only meaningful dietary source | ½ cup cooked edamame or 100 g firm tofu delivers genistein in the range studied in soy-isoflavone epidemiology | Fermented soy products (tempeh, miso, natto) have isoflavones partly converted to aglycone forms by fermentation, which may alter absorption kinetics relative to unfermented soy (tofu, soy milk) where isoflavones are predominantly glycosides | Genistin (glycoside, predominant in unfermented soy); genistein aglycone (increased proportion in fermented soy) | Preclinical-Cell; genistein's estrogenic (phytoestrogen) activity via ERβ is a real, separate mechanism from its CDK-modulatory activity — both should be considered together, not just the one convenient to V1 | None direct |

---

## Juicing and Sulforaphane Activation — Detailed Analysis

This is flagged as mechanistically important per the task brief, so it gets its own section rather than
being compressed into a table cell.

**The core chemistry**: Glucoraphanin (the glucosinolate precursor, present preformed in broccoli tissue)
is converted to sulforaphane (the bioactive isothiocyanate) by myrosinase (a thioglucosidase enzyme),
which is stored in separate plant cells from glucoraphanin ("mustard bomb" compartmentalization). Any
mechanical disruption of the tissue — chewing, chopping, blending, juicing — brings the two together and
initiates the reaction.

**What juicing actually does, mechanistically**:
1. **Juicing DOES disrupt the myrosinase/glucosinolate compartmentalization** — in this respect a
   high-speed blender or juicer is not fundamentally different from chewing; both are mechanical
   disruption events that can initiate the glucoraphanin → sulforaphane conversion.
2. **However, the reaction is temperature- and time-dependent.** Myrosinase is a heat-labile enzyme
   (substantially inactivated above roughly 60 °C within seconds to minutes). Centrifugal juicers can
   generate meaningful frictional heat; if the patient's juicer heats the pulp noticeably, myrosinase
   activity in that batch could be reduced before the reaction goes to completion.
3. **Epithiospecifier protein (ESP)** is a second enzyme present in mature broccoli (much less so in young
   sprouts) that diverts the myrosinase reaction away from sulforaphane and toward sulforaphane nitrile —
   an isothiocyanate-derived byproduct with little of sulforaphane's HDAC-modulatory activity. Mature
   broccoli florets (what most home juicers use) therefore yield proportionally less sulforaphane per
   unit glucoraphanin than young broccoli sprouts, independent of the juicing step itself.
4. **If myrosinase activity in the juice is low or absent** (heat-inactivated, or if a juicer separates
   and discards fiber-bound myrosinase-rich pulp from the liquid fraction), the glucoraphanin that
   remains in the juice is not inert forever — **gut microbiota in the colon possess myrosinase-like
   thioglucosidase activity** and can convert some glucoraphanin to sulforaphane, but this route is
   reported as substantially less efficient and more variable between individuals than plant-myrosinase
   conversion in the mouth/gut shortly after chewing.

**Net assessment**: Whether this patient's broccoli juice delivers meaningful sulforaphane depends on
juicer type (heat generation), whether pulp (myrosinase-rich) is retained or discarded, how long the juice
sits before consumption, and whether sprouts vs. mature florets are used. **None of these variables are
known from the task brief** — this is flagged in "What I Could Not Establish" below. The directionally
correct, mechanistically grounded statement is: **juicing reduces sulforaphane yield relative to chewing
fresh sprouts (due to ESP in mature broccoli, possible heat inactivation of myrosinase, and possible
pulp/myrosinase loss), but does not necessarily reduce it to zero** — this is more nuanced than a blanket
"juicing destroys sulforaphane" claim, and also more nuanced than "juicing is equivalent to chewing."
A practical mechanistic optimization (without prescribing a regimen) would be to add a small portion of
raw, finely chopped young broccoli sprouts directly to the juice immediately before drinking, maximizing
both sprout glucoraphanin density (ESP is lower in sprouts) and fresh myrosinase contact time.
`[no direct citation for the patient-specific juicer scenario; mechanism inferred from glucosinolate-myrosinase
biochemistry and human bioavailability literature broadly — WebSearch this session confirmed active myrosinase
increases sulforaphane bioavailability ~3-4 fold vs. inactive-myrosinase preparations, PMC4629881/PLOS ONE
2015, Egner et al.-adjacent broccoli bioavailability literature]`

---

## Chemo-Interaction Screening (per `sarcoma-chemo-interactions`)

Per the skill's required format. SOC = vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide
(VDC/IE); imminent treatment = high-dose ifosfamide (a CYP3A4-activated prodrug).

```
Piperine (black pepper, in patient's curcumin regimen) — chemo screening:
  CYP3A4: Documented inhibitor in human/animal studies — this is the same mechanism proposed for the
    curcumin-absorption-enhancement effect (less first-pass CYP3A4/UGT metabolism of curcumin).
    | P-gp: Documented P-glycoprotein inhibitor in preclinical studies.
    | ROS-axis: Not primarily a ROS-axis compound; no major flag here.
    | Other: CYP3A4 inhibition could theoretically REDUCE activation of ifosfamide (a CYP3A4-dependent
      prodrug requiring 4-hydroxylation for its active metabolite) — a potential EFFICACY concern,
      distinct from the more commonly discussed toxicity-increase framing for CYP3A4 substrates like
      vincristine/etoposide.
    | Citation: mechanism class is well-documented in the CYP3A4/P-gp pharmacology literature for
      piperine broadly `[no direct CIC-DUX4 or ifosfamide-specific citation; mechanism inferred from
      piperine CYP3A4/P-gp inhibition literature broadly — see bioavailability.md / supplement-protocol.md
      for the Shoba 1998 reference underlying the curcumin+piperine pairing]`. FLAG FOR ONCOLOGIST REVIEW
      given the imminent high-dose ifosfamide course.

Thymoquinone / Nigella sativa (black cumin seed oil, patient's current regimen) — chemo screening:
  CYP3A4: Documented inhibitor in human liver microsome studies (IC50 ~25 µM; ~79% inhibition at 100 µM).
    | P-gp: Not separately confirmed this session — not screened.
    | ROS-axis: Thymoquinone has both pro-oxidant and antioxidant reported activity depending on
      concentration/context — not a clean "antioxidant" flag, but worth noting given doxorubicin's
      ROS-dependent mechanism (theoretical, not screened in depth here — Supplement Specialist territory).
    | Other: Same CYP3A4-mediated ifosfamide-activation concern as piperine, additively.
    | Citation: WebSearch this session found human-liver-microsome CYP3A4-inhibition literature for
      Nigella sativa/thymoquinone (multiple secondary sources referencing Badary-group and related
      studies); specific PMID not retrieved this session — `[VERIFY]`. FLAG FOR ONCOLOGIST REVIEW —
      this compound and piperine represent TWO independent CYP3A4-inhibitory inputs in the patient's
      current regimen, converging on the same imminent high-dose ifosfamide concern.

Curcumin (turmeric) — chemo screening:
  CYP3A4: Curcumin itself has reported CYP3A4-modulatory activity in vitro, generally regarded as weaker
    and less consistent than piperine's at dietary/typical-supplement exposure.
    | P-gp: Some preclinical evidence of P-gp modulation.
    | ROS-axis: Curcumin is often framed as an antioxidant; ROS-scavenging at high supplemental doses is
      a theoretical concern alongside doxorubicin's ROS-dependent cytotoxic mechanism, but whole-food
      turmeric-level intake is far below the doses studied for this concern.
    | Other: none additional identified this session.
    | Citation: `[no direct citation; mechanism inferred from curcumin CYP3A4/antioxidant literature
      broadly]` — not screened in depth; Supplement Specialist owns the dose-dependent resolution.

EGCG / green tea — chemo screening:
  CYP3A4: EGCG has reported CYP3A4-modulatory activity in cell-free/cell-line assays at high
    concentrations.
    | P-gp: Reported P-gp modulation in preclinical studies.
    | ROS-axis: Catechins are polyphenol antioxidants — same class-level theoretical ROS-axis question
      as curcumin, at culinary-tea-level intake this is judged low-magnitude.
    | Other: high-dose green tea extract has documented hepatotoxicity signals in case reports
      (separate from chemo-interaction, but relevant to "natural ≠ safe").
    | Citation: `[no direct citation; mechanism inferred from EGCG CYP3A4/P-gp literature broadly]` — not
      screened in depth at culinary-tea exposure; flagged for completeness only.

Beetroot juice (dietary nitrate) — chemo screening:
  CYP3A4: none found in sources checked this session (WebSearch not run for this specific compound;
    not flagged in standard chemo-interaction references reviewed).
  | P-gp: none found in sources checked this session.
  | ROS-axis: nitrate/nitrite/NO chemistry is redox-active but operates through a different pathway
    (NO signaling) than the classical ROS-scavenging antioxidant framing; not screened in depth.
  | Other: none identified.
  | Citation: not screened in depth — `not screened — out of scope for this output beyond noting absence
    of an obvious flag in the sources reviewed`.

Apple, celery, ginger, carrot (juice components, fisetin/apigenin/luteolin/6-gingerol/β-carotene) —
chemo screening:
  CYP3A4 / P-gp / ROS-axis: no compound-specific high-confidence interaction flags identified this
  session at culinary-juice exposure levels for these four; this is consistent with their generally
  lower reported CYP-modulatory potency relative to piperine and thymoquinone, but was not exhaustively
  screened compound-by-compound against DrugBank/PubChem this session.
  | Citation: `not screened — out of scope for this output; defer to Supplement Specialist if any of
    these become supplement-form candidates`.

Berberine — chemo screening:
  CYP3A4: berberine is a reported CYP3A4 (and CYP2D6) inhibitor in preclinical studies — but berberine
    is not part of this patient's current regimen and has no realistic food source (see table above),
    so this is noted for V1-lead awareness only, not as an active patient-regimen flag.
  | Citation: `[no direct citation; mechanism inferred from berberine CYP literature broadly]`.
```

**Bottom-line interaction flag for V1 lead and orchestrator**: the patient's current regimen contains
**two independent, CYP3A4-inhibitory compounds (piperine and thymoquinone/black cumin seed oil)**, both
converging on the same concern — CYP3A4 is required to activate the ifosfamide prodrug to its
cytotoxic metabolite, and CYP3A4 inhibition could theoretically blunt that activation just as high-dose
ifosfamide begins. This is **not** a "high-dose antioxidant blunts ROS-dependent chemo" framing (the more
commonly discussed V2-territory concern) — it is a **prodrug-activation** concern, mechanistically
distinct and arguably higher-priority given the timing. This is squarely **for oncologist discussion**,
not a recommendation to stop anything (golden rule: no start/stop instructions).

---

## Cross-Vector Flags (for V1 lead → other vector leads)

- **Sulforaphane** — flag to V3 (HDAC/MHC-I axis) and V4 (immune visibility): if the broccoli-juice
  preparation question can be resolved toward meaningful sulforaphane delivery, this is the cleanest
  single dietary bridge across V1/V3/V4.
- **β-Carotene** — flag to V3 (retinoic-acid/differentiation track): the ATBC/CARET harm signal belongs
  in V3's differentiation-therapy discussion, with the smoker/supplement-dose caveat carried forward
  (do not let it become a generalized "carotenoids are dangerous" statement).
- **Zinc** — flag to V2 (DNA-repair cofactor, Ku70/Ku80) and V4 (NK-cell development) — this patient's
  zinc status is unknown; correcting a deficiency (if present) has much stronger evidence than
  supplementing a repleted individual (Bioavailability/Supplement Specialist territory).
- **Piperine + thymoquinone CYP3A4 convergence** — flag to V2 and the orchestrator's Standard-of-Care
  Interaction Map as the highest-priority interaction item from this V1 sub-agent given the imminent
  high-dose ifosfamide.
- **Dietary nitrate (beetroot)** — flag to V4: NO signaling has documented roles in immune-cell function
  and tumor vasculature in broader oncology literature; whether this is relevant to V4's immune-visibility
  framing for CIC-DUX4 is unestablished and would need a V4 sub-agent to assess.

---

## Forward Hypotheses

**[Forward Hypothesis 1] — Sequencing broccoli-sprout sulforaphane delivery away from the CYP3A4-inhibitor
window.** If piperine and thymoquinone meaningfully inhibit CYP3A4 (as the literature suggests at
sufficient exposure), and if sulforaphane itself is partly metabolized via glutathione-conjugation
pathways that interact with phase-I/II enzyme induction (sulforaphane is a well-documented Nrf2/phase-II
inducer), there may be a **time-of-day or treatment-cycle sequencing interaction** between (a) the
patient's curcumin+piperine/black-cumin intake (CYP3A4-inhibitory) and (b) any future attempt to use
broccoli-sprout sulforaphane for its MHC-I/HDAC-modulatory potential (V3/V4 territory) — sulforaphane's
Nrf2-mediated phase-II induction could partially offset or interact with piperine/thymoquinone's CYP3A4
inhibition in ways not characterized in any single-compound PK study. **Mechanistic basis**: Nrf2 target
genes include several phase-II conjugation enzymes (GSTs, UGTs) and some phase-I cross-talk has been
reported in rodent models. **Test**: a small PK sub-study (even N-of-1, with appropriate biomarker
monitoring, in a research context — not a treatment recommendation) measuring a CYP3A4 probe-drug
metabolite ratio with and without concurrent sulforaphane-rich broccoli-sprout intake, alongside the
patient's existing piperine/thymoquinone intake. **Why untested**: this is a three-way interaction
(piperine × thymoquinone × sulforaphane) on a single CYP enzyme relevant to a specific prodrug
(ifosfamide) in a specific rare-tumor context — far too narrow a combination for any funded PK study to
have addressed.

**[Forward Hypothesis 2] — Apple-skin quercetin + onion-derived quercetin as a "whole-food cocktail"
may achieve additive RAS/ERK pathway coverage that single-compound cell-line studies miss.** Most V1-A
quercetin evidence comes from isolated-compound cell-line studies at single concentrations. The patient's
regimen (apple-with-skin juice plus, hypothetically, onion-containing cooked foods) delivers quercetin
alongside a cocktail of co-occurring flavonoids (kaempferol, in the same foods) and apple-specific
procyanidins/chlorogenic acid, which have been reported in some non-CIC-DUX4 contexts to have synergistic
(more-than-additive) effects on RTK/RAS pathway nodes relative to quercetin alone. **Mechanistic basis**:
polyphenol "matrix effects" — co-occurring compounds can alter gut absorption, competitive
glucuronidation (sparing more parent quercetin), and have overlapping-but-non-identical kinase-inhibition
profiles that could produce broader RAS/ERK pathway coverage than any single compound. **Test**: compare
RAS/ERK pathway-node phosphorylation (e.g., pERK1/2 by Western blot or phospho-flow) in a CIC-DUX4 cell
line treated with isolated quercetin vs. a matched whole-apple-skin polyphenol extract at equivalent
quercetin-equivalent concentrations, looking for non-additive effects. **Why untested**: whole-food
extracts are harder to standardize than single compounds, and CIC-DUX4 cell-line work is itself scarce —
this combination has likely never been tested in any fusion-sarcoma line.

---

## Atypical-Case Notes

All compounds in this table act on pathway-level targets (RAS/ERK, BRD4/super-enhancer chromatin state,
CDK4/CCND1 cell-cycle machinery) that are not contingent on the CIC-DUX4 fusion junction sequence itself.
**None of these recommendations require fusion confirmation to be mechanistically plausible** — they
remain in-scope for this patient's fusion-unconfirmed (~5% atypical) status. This contrasts with V3
junction-specific ASOs or V4 junction-specific neoantigen vaccines, which would need to be flagged as
possibly inapplicable to this patient (those flags belong in the V3/V4 outputs, not here).

---

## What I Could Not Establish

1. **The patient's actual broccoli-juicing method** (juicer type/heat generation, pulp retention vs.
   discard, rest time before consumption, sprouts vs. mature florets) — this single unknown determines
   whether the sulforaphane-delivery question resolves toward "meaningful" or "near-zero." This is the
   load-bearing assumption identified in the pre-output red-team pass: if the patient is in fact adding
   raw chopped sprouts to the juice and consuming it promptly, the "juicing destroys sulforaphane"
   framing would be largely wrong for this patient specifically.
2. **Quantitative human PK data for thymoquinone from black cumin seed oil at the patient's actual
   product/dose** — the CYP3A4-inhibition IC50 (~25 µM) is from human liver microsomes, not whole-body PK;
   whether oral black-cumin-oil intake achieves hepatic concentrations anywhere near this range is not
   established and was not resolved this session (`[VERIFY]`).
3. **Whether the apple-juice quercetin (predominantly glycosides) reaches plasma concentrations
   comparable to the aglycone forms studied in the V1-A cell-line literature** — the deglycosylation step
   adds a layer of inter-individual variability (gut microbiome-dependent) not characterized here.
4. **6-Gingerol concentrations from this patient's specific ginger-juice preparation** — mechanism is
   clear (fresh ginger = 6-gingerol-dominant), but whether culinary-juice intake reaches even the lower
   end of studied cell-line concentrations is not established.
5. **Any direct CIC-DUX4 (or even broader sarcoma) data for any compound in this table** — every entry is
   `None direct`; the entire table rests on pathway-level (RAS/ERK, BRD4, CDK4/CCND1) mechanistic
   plausibility plus, in most cases, evidence from other cancer types or non-cancer contexts. This is the
   expected and stated limitation of the V1 dietary track as a whole (per `sarcoma-vector-context v1`:
   "What V1 Cannot Do").
6. **Compound-by-compound CYP/P-gp screening for apple, celery, ginger, carrot, and beetroot
   constituents** was not exhaustively performed against DrugBank/PubChem this session — flagged as
   "not screened" rather than asserting "no interaction."
7. **Red-team disconfirmation note**: the strongest evidence *against* the "juicing destroys sulforaphane"
   framing is the existence of gut-microbial thioglucosidase activity, which provides a (less efficient)
   conversion route even when plant myrosinase is fully inactivated — meaning "destroyed" is too strong a
   word regardless of preparation method; "substantially reduced, with high preparation-dependent
   variance" is the defensible claim.

---

## Grounding (OpenMed NER)

Run from repo root: `python scripts/openmed_ner.py --team v1-lead --text-file <entity list> --format tsv`.
All entities in this output (compound names: Quercetin, Omega-3 EPA/DHA, EGCG, Curcumin, Sulforaphane,
Fisetin, Selenium, Berberine, Apigenin, Kaempferol, Genistein, Luteolin, Zinc, Lycopene, Beta-carotene,
6-Gingerol, 6-Shogaol, Dietary nitrate, Thymoquinone, Glucoraphanin, Myrosinase, Piperine, Nitric oxide;
gene/pathway names: RAS, ERK, BRD4, CDK4, CCND1, CYP3A4, P-glycoprotein, EZH2, HDAC; chemo agents:
Vincristine, Doxorubicin, Cyclophosphamide, Ifosfamide, Etoposide; organisms: Nigella sativa, Broccoli,
Turmeric, Curcuma longa) were recognized by at least one OpenMed model
(`chemical_detection_pubmed`, `pharma_detection_superclinical`, `oncology_detection_superclinical`) —
no unresolved entities.
