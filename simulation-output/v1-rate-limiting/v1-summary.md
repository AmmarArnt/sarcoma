# Vector 1 — Rate Limiting Summary

Summary: This output covers dietary and supplemental compounds that may reduce the speed of the CIC-DUX4 oncogenic loop by dampening upstream RAS/ERK amplitude (Layer A), throttling BRD4/super-enhancer amplification (Layer B), and slowing downstream CDK4/CCND1 cell-cycle execution (Layer C). It deliberately excludes: fusion-protein elimination (V3 territory), clinical BET inhibitors or CDK4/6 inhibitors (V3 clinical track), immune modulation (V4), and interventions targeting neighboring-cell translocation risk (V2). It explicitly does NOT substitute for the patient's clinical regimen.

Confidence: Low overall — no dietary compound in this vector has published evidence in CIC-rearranged sarcoma or CIC-DUX4 cell lines specifically; all evidence tiers are Preclinical-Cell, Mechanistic, or Dietary-Observational. Confidence in the interaction-screening flags (ifosfamide/piperine/curcumin) is medium-high, grounded in PK literature.

---

## PATIENT CASE CONTEXT

This run is anchored to a specific patient: CIC-rearranged sarcoma, GENOMICALLY UNCHARACTERIZED (~5% atypical subgroup — no confirmed CIC-DUX4/CIC-NUTM1/CIC-FOXO4 fusion on sequencing). Primary: biceps femoris. 14 cycles EURO EWING (VDC/IE). Surgery Jan 2025 (>95% necrotic). Whole-lung irradiation. NED May 2025 → May 2026. Now: oligometastatic relapse (one lung lesion). NOW PREPARING HIGH-DOSE IFOSFAMIDE.

**Atypical-case note (mandatory)**: Because no confirming fusion was found on genome sequencing, this patient belongs to the genomically uncharacterized ~5% subgroup. All V1 recommendations in this output operate on the BRD4/ETS/CDK4 amplification machinery downstream of the presumed fusion — these are fusion-agnostic mechanisms to the extent that ETS overactivation, BRD4 super-enhancer recruitment, and CDK4/CCND1 upregulation are features of this tumor phenotype regardless of which exact fusion (or fusion-equivalent lesion) drives them. However: any intervention that would depend on the CIC-DUX4 junction protein being present specifically (junction-specific ASOs, junction-specific epitopes) CANNOT be assumed applicable to this patient. V1 dietary interventions are all fusion-agnostic — they operate downstream of the fusion event and apply to atypical cases equally.

---

## Patient's Actual Self-Administered Regimen — V1 Assessment

The following compounds are being taken by the patient and have been evaluated explicitly for V1 relevance and, critically, for interaction with the imminent high-dose ifosfamide course.

| Compound | [PATIENT TAKING] | V1 Layer | Assessment | Chemo Interaction Priority |
|---|---|---|---|---|
| Curcumin + piperine | Yes, during rest weeks and NED year | B | V1-relevant (BRD4-chromatin disruption); bioavailability significantly below cell-line active range even with piperine | **HIGHEST PRIORITY FLAG** — piperine inhibits CYP3A4 and P-gp; ifosfamide is a CYP3A4-activated prodrug; P-gp substrates include vincristine and etoposide. MUST discuss with oncologist before ifosfamide cycle. |
| Liposomal vitamin C | Yes, during rest weeks and NED year | V2 primarily | Not a primary V1 compound | Moderate flag — high-dose antioxidant during cytotoxic chemo (doxorubicin, ifosfamide) may reduce ROS-dependent cytotoxicity. Different concern profile during NED year vs. active chemo. |
| Black cumin seed oil (Nigella sativa / thymoquinone) | Yes, during rest weeks and NED year | B/C (weak) | Thymoquinone has MAPK/NF-κB modulatory activity in cell lines; V1-B/C adjacent at best | High flag — CYP3A4 inhibition documented. Same mechanism of concern as piperine for ifosfamide prodrug activation. MUST discuss with oncologist before ifosfamide. |
| Vitamin D | Yes, during rest weeks and NED year | V3/V4 primarily | Minimal direct V1 activity | Low flag — modest CYP3A4 substrate/inducer; not a primary interaction concern at supplemental doses for ifosfamide |
| Honey | Yes | Minimal V1 specificity | Trace polyphenols at culinary intake; no V1-relevant concentrations achievable | No chemo interaction flag at culinary doses |
| Ginger juice (6-gingerol) | Yes, during chemo rest weeks | A (theoretical) | MAPK/NF-κB mechanism at concentrations 50–200× above dietary intake; concentration mismatch is decisive | Moderate flag — 6-gingerol modulates CYP2C9; some P-gp modulation in vitro |
| Celery juice (apigenin/luteolin) | Yes, during chemo rest weeks | B/C | Apigenin reduces ETS factor expression in some cell lines; luteolin is a cell-cycle modulator; both at concentrations 50–250× above achievable from juice | Moderate flag — apigenin inhibits CYP2C9 and has modest CYP3A4 activity |
| Apple juice (quercetin via skin) | Yes, during chemo rest weeks | A/B | Quercetin RTK/RAS inhibition at 10–50 µM in cell lines; dietary plasma ~0.05–0.2 µM | Moderate flag — quercetin modulates CYP3A4 and P-gp at supplement doses; juice-level intake is below the threshold for significant clinical interaction but should be noted |
| Broccoli juice (sulforaphane — ACTIVATION CONCERN) | Yes, during chemo rest weeks | B/V3 | Sulforaphane is the best-bioavailable V1 compound (3–10× mismatch vs. 10–200× for polyphenols) BUT juicing destroys myrosinase — sulforaphane will not form from juiced broccoli without the activation step | Low chemo interaction concern for sulforaphane itself; BUT preparation advice is critical |
| Carrot juice (beta-carotene) | Yes, during chemo rest weeks | V2/V3 cross-flag | Not primary V1; provitamin A → retinoid axis is V3 | Low direct V1 flag; CROSS-FLAG to V2/V3 for ATBC/CARET context (food-level carrot intake categorically different from supplementation) |

---

## Ranked Candidate List

| Rank | Compound | Layer | Mechanism | Tier | CIC-DUX4 direct? | Cross-vector | Source/citation |
|---|---|---|---|---|---|---|---|
| 1 | Omega-3 EPA/DHA | A | Alters membrane phospholipid composition → disrupts lipid raft cholesterol-dependent RAS membrane clustering → reduces ERK activation amplitude | Dietary-Observational + Mechanistic | None direct | V1+V2+V4 | Dietary-Observational: multiple cohort studies; mechanism: Prior IA et al., *J Lipid Res* 2011 [no PMID verified — mechanism inferred from lipid raft/RAS literature; verify before citing specific PMID]; V4 dietary support: mechanistic |
| 2 | Sulforaphane (from broccoli sprouts, properly activated) | B/V3 | Inhibits class-I HDAC activity in cell lines → reduces H3K27 deacetylation at tumor-suppressor loci → weak chromatin remodeling toward BRD4 super-enhancer disruption; V3 cross-action | Preclinical-Cell | None direct | V1+V3+V4 | Myzak MC et al., *Cancer Res* 2004, PMID 15205379 (HDAC inhibition in HCT116 cells); Clarke JD et al., *Cancer Prev Res* 2011, PMID 21593198 (bioavailability) |
| 3 | Quercetin | A/B | Multi-kinase RTK/RAS pathway inhibition; weak EZH2 modulation → dual Layer A+B activity, but severe concentration mismatch (10–100× below active range at dietary intake) | Preclinical-Cell | None direct | V1+V2 | Russo M et al., *Biochem Pharmacol* 2012, PMID 22261127 (RTK inhibition in cancer cell lines; not CIC-DUX4) |
| 4 | Curcumin (enhanced formulation) | B | Disrupts BRD4-chromatin interaction; modulates H3K27ac; polypharmacology across NF-κB, MAPK | Preclinical-Cell | None direct | V1+V2+V4 | Chatterjee S et al., *Biochemistry* 2019, PMID 30865445 (curcumin-BRD4 interaction in cell lines); **INTERACTION FLAG: CYP3A4 + P-gp modulation — critical for imminent ifosfamide course** |
| 5 | EGCG (green tea) | B | Binds BRD4 BD1 bromodomain; modulates H3K27ac at super-enhancers; at 10–50 µM in cell lines (10–100× above dietary plasma) | Preclinical-Cell | None direct | V1+V2 | Berletch JB et al., *Mol Cell Biol* 2008 [no direct PMID verified — mechanism inferred from BRD4/EGCG cell-line literature; verify before citing]; concentration caveat: see bioavailability.md |
| 6 | Apigenin (from celery/parsley) | B/C | Inhibits ETS factor expression in cancer cell lines; modulates cell-cycle checkpoints; flavone with multi-target activity | Preclinical-Cell | None direct | V1 | Shukla S et al., *Mol Carcinog* 2015, PMID 24700712 (apigenin ETS targets in prostate cancer; not CIC-DUX4); concentration caveat: 50–250× mismatch at food level |
| 7 | Berberine | A | AMPK activation → mTORC1 suppression → reduced 4EBP1/S6K → lower MYC translation; secondarily MAPK suppression | Preclinical-Cell | None direct | V1 | Kim HS et al., *Biochem Pharmacol* 2012, PMID 22521726 (AMPK-MAPK in cancer cells); ~1% oral bioavailability severely limits V1 activity |
| 8 | Fisetin | C | CDK4 suppression; ETS inhibition in some cell lines; senolytic activity in aging models may reduce senescence-associated secretory phenotype (SASP) that fuels tumor microenvironment | Preclinical-Cell | None direct | V1 | Mukherjee S et al., *Eur J Pharm Biopharm* 2019 [no PMID verified — mechanism inferred from fisetin/CDK cell-line literature; verify] |
| 9 | Luteolin | C | Cell-cycle arrest (G2/M) in cell lines; CDK suppression; anti-proliferative in multiple cancer lines | Preclinical-Cell | None direct | V1 | Rani N et al., *Cell Biochem Funct* 2016, PMID 27062567; concentration caveat: 50–250× mismatch at food level |
| 10 | Lycopene | A | ERK pathway downregulation reported in prostate cancer cell lines; antioxidant activity; lipophilic carotenoid | Dietary-Observational (prostate) | None direct | V1 (weak) | Palozza P et al., *Nutrients* 2011, PMID 22254107 (prostate-focused; not CIC-DUX4 or sarcoma) |
| 11 | Thymoquinone (black cumin seed oil) | B/C | NF-κB inhibition; MAPK modulation; pro-apoptotic in cancer cell lines | Preclinical-Cell | None direct | V1 | Shafi G et al., *Oncol Rep* 2009, PMID 19294336; **INTERACTION FLAG: CYP3A4 inhibition — same concern as piperine for ifosfamide** |
| 12 | Selenium (deficiency correction) | C | Selenoprotein cofactor including thioredoxin reductase → modulates cellular redox → influences apoptosis threshold | Preclinical + Dietary-Observational | None direct | V1+V2 | Clark LC et al., *JAMA* 1996 (Nutritional Prevention of Cancer trial, PMID 8971564) — **SELECT (PMID 19066370) null result; narrow safety window applies** |

---

## Food Sources (condensed from Food Specialist output)

| Compound | Best food source | Preparation note | Concentration realism |
|---|---|---|---|
| Omega-3 EPA/DHA | Atlantic mackerel, sardines, wild salmon | Minimize heat; canned in water preferred | Food-level intake achieves the membrane-compositional mechanism (no acute threshold mismatch) |
| Sulforaphane | Broccoli sprouts (50–100× more glucoraphanin than mature broccoli) | **Chop → wait 40 min at room temperature → then consume. Do NOT juice without this activation step. Heat above 70°C destroys myrosinase.** | 3–10× mismatch — most favorable of any V1 compound |
| Quercetin | Capers (highest density), raw red onion outer layers, apple skin | Eat raw; skin-on apple retains quercetin | 10–100× mismatch at dietary plasma levels |
| EGCG | Matcha, brewed green tea (70–80°C, 3 min, no milk) | Avoid boiling water; avoid milk proteins which bind catechins | 10–100× mismatch |
| Apigenin/Luteolin | Celery leaves and parsley (higher density than stalks); chamomile tea | Juice retains apigenin; parsley > celery | 50–250× mismatch |
| Fisetin | Strawberries (highest by weight), apple skin, mango | Fresh preferred; skin-on | 50–400× mismatch |
| Selenium | Brazil nuts (1–2 per day delivers RDA — do not exceed 4–5/day; UL is 400 µg/day) | No special preparation needed | Dietary RDA delivery; supplementation not indicated beyond deficiency correction |
| Lycopene | Cooked/processed tomatoes (tomato paste), watermelon | Cooking + fat increases lycopene bioavailability from tomatoes | Dietary-observational evidence only; prostate cancer data |

---

## Supplementation Notes (condensed from Supplement Specialist output)

The following notes apply to compounds where supplemental forms have been tested in registered human trials. For each, the trial indication is NOT CIC-DUX4 unless explicitly stated (it never is).

**Curcumin**: Phase I safety data exists (Cheng AL et al., *Anticancer Res* 2001, PMID 11763884: 4–8 g/day conventional form). Enhanced formulations (phospholipid complex Meriva, BCM-95) improve AUC without solving the fundamental concentration mismatch for V1 BRD4 activity. **The most important note for this patient is the interaction profile, not the dose. Consult oncologist before continuing during ifosfamide treatment — piperine is the CYP3A4/P-gp concern, not curcumin alone.**

**EGCG supplementation**: 400–800 mg/day tested in cancer prevention (Bettuzzi S et al., *Cancer Res* 2006, PMID 16397214 — prostate, not sarcoma). Hepatotoxicity signal at high doses. Consult oncologist before supplementing — P-gp inhibition affects vincristine/etoposide.

**Berberine**: 500 mg three times daily from metabolic trials (Zhang Y et al., *JCEM* 2008, PMID 18397984). No sarcoma data. CYP3A4 inhibition — same ifosfamide concern. Consult oncologist before starting.

**Selenium**: SELECT (PMID 19066370) was null for cancer prevention; narrow safety window (UL 400 µg/day); 1–2 Brazil nuts/day preferred over supplementation.

**Vitamin D3**: VITAL trial (Manson JE et al., *NEJM* 2019, PMID 30415629) — 2000 IU/day; deficiency correction is the clearest indication. Cross-vector (V3/V4).

**Black cumin seed oil / thymoquinone**: No human sarcoma trial data; no dose to report. CYP3A4 inhibition is the clinical flag. Consult oncologist before ifosfamide cycle.

---

## Bioavailability Notes (condensed from Bioavailability Specialist output)

**Shoba 1998 caveat (mandatory verbatim per file 05)**:
> "The widely-cited '~2000% bioavailability increase' comes from Shoba et al., *Planta Medica* 1998 — a single-dose pharmacokinetic study, n=10 healthy volunteers, 2 g curcumin + 20 mg piperine. The curcumin-only control arm produced serum levels below the assay's limit of detection, so the '20×' number is computed against a near-zero baseline. The directional finding (piperine increases curcumin absorption) is real and reproduced; the **specific 2000% figure should not be cited as a universal multiplier**."

**Critical bioavailability note for this patient**: Piperine's CYP3A4 and P-gp inhibitory effects are the SAME mechanism that improves curcumin absorption. The PK enhancement and the chemo interaction cannot be separated. Taking curcumin with piperine during ifosfamide treatment enhances curcumin absorption AND reduces ifosfamide prodrug activation AND increases vincristine/etoposide CNS exposure.

**Concentration mismatch summary (most important entries)**:
- Sulforaphane: 3–10× mismatch — most bioavailable V1 compound; BUT current preparation (broccoli juicing) likely yields near-zero sulforaphane due to myrosinase destruction
- Omega-3 EPA/DHA: No threshold mismatch — membrane compositional change is the mechanism; food-level sustained intake achieves this
- Polyphenols broadly: 10–500× mismatch depending on compound; dietary intake is below cell-line active concentrations for all Layer A/B mechanisms involving kinase inhibition or BRD4 binding

**Fat-soluble compounds** (curcumin, thymoquinone, beta-carotene, lycopene, vitamin D): require dietary fat for absorption. For the patient's fresh juices, adding a small amount of olive oil to carrot/broccoli juice meaningfully increases carotenoid and fat-soluble compound absorption.

---

## Cross-Vector Flags

| Compound | V1 | V2 | V3 | V4 | Notes |
|---|---|---|---|---|---|
| Sulforaphane | B | — | HDAC modulation | Possible MHC-I upregulation | **Cross-vector priority compound**; HDAC modulation is shared V1/V3; MHC-I upregulation in V4 (unestablished at dietary doses); best bioavailability ratio of V1 dietary compounds |
| Omega-3 EPA/DHA | A | Anti-inflammatory | — | NK cell support | Membrane mechanism (V1), SPM production (V2/anti-inflammatory), NK function support (V4); recommend to orchestrator for cross-vector weighting |
| Quercetin | A/B | ROS scavenging | EZH2 modulation (weak) | — | V1+V2 priority; concentration-limited at food level |
| EGCG | B | ROS scavenging | EZH2 modulation (weak) | — | V1+V2; hepatotoxicity signal at high supplement doses |
| Curcumin | B | NF-κB/inflammatory | — | Anti-inflammatory TME | V1+V2+V4; **interaction flag with imminent ifosfamide dominates all other considerations for this patient** |
| Vitamin D3 | — | — | Differentiation axis | NK cell function | Primarily V3+V4; deficiency correction first |
| Selenium | C | DNA repair cofactor | — | — | V1+V2; SELECT null; narrow window |
| Zinc | C | DNA repair cofactor | — | NK development | V1+V2+V4; correct deficiency; excess displaces copper |
| Beta-carotene (from carrot juice) | — | Cross-flag | Retinoid axis | — | **V2/V3 cross-flag — ATBC/CARET harm signal for supplementation; food-level intake from carrot juice is NOT the same as supplement; document distinction explicitly for orchestrator** |

---

## Forward Hypotheses

**[Forward Hypothesis 1]: Sulforaphane + BET inhibitor priming — testing dietary HDAC modulation as a combinatorial sensitizer to clinical BRD4 inhibition in CIC-DUX4**

Hypothesis: Sulforaphane, at the concentrations achievable from properly activated broccoli sprout concentrate (0.5–2 µM), may not reach the threshold for standalone HDAC inhibitory activity in CIC-DUX4 tumor cells, but may lower the threshold for clinical BET inhibitor (e.g., OTX015 or BMS-986158) activity by partially redistributing H3K27ac at super-enhancer loci — creating a combinatorial sensitization effect at clinically achievable BETi doses.

Mechanistic basis: Class-I HDAC inhibition reduces histone deacetylation at target loci → increases H3K27ac occupancy → makes BRD4-occupied super-enhancers more dependent on BRD4 for maintenance → increases sensitivity to BET bromodomain displacement. At standalone sulforaphane concentrations achievable in vivo, the effect is too weak; in combination with a BETi that is already occupying the therapeutic range, the additive chromatin effect may lower the effective BETi dose required. This has mechanistic precedent from HDACi + BETi combination studies in other cancers (e.g., Gao et al., *Cancer Lett* 2020 describing synergy in solid tumors; no CIC-DUX4-specific data).

Study design to test: In vitro: test sulforaphane (0.5–2 µM, matching achievable plasma concentrations) + OTX015 (at sub-IC50 concentrations) in CIC-DUX4 cell lines (if publicly available — Cellosaurus has limited CIC-DUX4 lines). Readout: ETV4/ETV5 mRNA, BRD4 super-enhancer occupancy by ChIP-qPCR, viability. In vivo: patient-derived xenograft (PDX) fed sulforaphane-producing diet (broccoli sprout diet in mice is established) + low-dose OTX015. Why not yet tested: CIC-DUX4 cell-line models are scarce; sulforaphane is rarely used as a pre-conditioning agent in BETi combination studies (usually HDACi drugs are used); no commercial interest in sulforaphane-BETi combination.

---

**[Forward Hypothesis 2]: Piperine-timed pharmacological window — exploiting CYP3A4 inhibition therapeutically rather than toxicologically in ifosfamide scheduling**

Hypothesis: Piperine's CYP3A4 inhibitory effect (which creates the interaction flag for ifosfamide in V1) could, paradoxically, be therapeutically useful in the context of other CYP3A4-cleared drugs — specifically in a future context where a CYP3A4-cleared targeted agent (BETi, CDK4/6i, or EZH2i) is co-administered with ifosfamide in a sarcoma combination trial. Intentional CYP3A4 inhibition with a defined piperine dose could modulate the targeted agent's PK in a controlled, predictable way, similar to the ritonavir "boosting" principle used in HIV pharmacology.

Mechanistic basis: Ritonavir-boosted protease inhibitors are the precedent — a strong CYP3A4 inhibitor extends the PK profile of a CYP3A4-cleared co-drug. Piperine is a weaker CYP3A4 inhibitor than ritonavir but could provide partial boosting of a BETi's exposure. The hypothesis requires separating the ifosfamide prodrug phase (where CYP3A4 inhibition is harmful) from the targeted-agent phase (where it could be beneficial). In a combination scheduling trial where ifosfamide is given on days 1–5 and a BETi is given continuously, timed piperine on BETi-only days (not ifosfamide days) could increase BETi exposure without affecting ifosfamide activation.

Study design to test: PK study: enroll patients on BETi + ifosfamide combination (if/when such a trial exists in sarcoma) and evaluate piperine co-administration on non-ifosfamide days for BETi AUC modulation. Requires: robust CYP3A4-phenotyping; tight scheduling protocol. Pre-clinical validation: rat model with piperine + OTX015 PK study first. Why not yet tested: The combination BETi + ifosfamide trial in sarcoma does not yet exist at scale; the piperine "booster" concept has not been proposed for oncology drug scheduling to my knowledge.

---

**[Forward Hypothesis 3]: Myrosinase-engineered broccoli sprout juice protocol for achieving sulforaphane concentrations relevant to V1/V3 in sarcoma patients undergoing chemotherapy rest weeks**

Hypothesis: The patient's current broccoli juice preparation almost certainly delivers near-zero sulforaphane due to myrosinase inactivation by juicing. A standardized protocol (chop → 40-min room-temperature stand → cold consumption, with co-administration of daikon radish as an exogenous myrosinase source) could increase plasma sulforaphane from effectively zero to the 0.5–2 µM range that has the most favorable V1/V3 concentration ratio of any dietary compound. A feasibility PK study in sarcoma patients during chemo rest weeks would be straightforward to conduct.

Mechanistic basis: Myrosinase is the enzymatic bottleneck for sulforaphane formation; exogenous myrosinase sources (daikon radish, mustard seed powder) have been shown in healthy volunteer studies to rescue sulforaphane formation from heat-processed broccoli (Cramer JM et al., *J Nutr* 2011; Vermeulen M et al., *J Nutr* 2008, PMID 18539765). The V1/V3 mechanism relevance (class-I HDAC modulation at 5–20 µM in cell lines; 0.5–2 µM achievable with proper preparation) creates a 3–10× gap that is smaller than for any other dietary V1 compound.

Study design to test: Phase 0 PK feasibility study: 10–15 sarcoma patients during chemo rest weeks; standardized broccoli sprout + daikon powder protocol vs. current broccoli juice practice; measure plasma isothiocyanate levels (including sulforaphane-GSH, sulforaphane-NAC) and urinary excretion as PK endpoints. No therapeutic claim required for this study — it is a PK feasibility study. This could be conducted as a correlative study within an existing sarcoma trial.

---

## Atypical-Case Notes

This patient has NO confirmed fusion on genomic sequencing — the ~5% genomically uncharacterized subgroup. The following applies to the V1 recommendations:

- ALL dietary V1 interventions in this summary operate downstream of the fusion event (at BRD4 super-enhancer level, ETS factor output level, CDK4/CCND1 level). These are fusion-agnostic.
- None of the V1 dietary interventions require knowledge of which specific fusion is present.
- The mechanistic rationale for V1 (ETS overactivation → BRD4 super-enhancer formation → CDK4-driven proliferation) is consistent with CIC-rearranged sarcoma phenotype regardless of the specific fusion partner.
- The patient's treatment response (>95% necrosis, NED for one year) is consistent with a functional CIC-rearranged sarcoma diagnosis even without fusion confirmation.
- You CANNOT fix the fusion — and for this patient specifically, you cannot even sequence-target the fusion. V1 is the most applicable vector because it operates entirely downstream of and independently from the specific fusion identity.
- For the orchestrator: the atypical-case qualifier specifically matters for V3 ASO/junction approaches and V4 junction-neoantigen vaccine approaches — both inapplicable to this patient. V1 is unaffected by the fusion-unconfirmed status.

---

## What I Could Not Establish

1. Direct evidence in CIC-DUX4 cell lines or animal models for ANY dietary compound in this vector. All V1 dietary mechanism claims transfer from other cancer cell-line models.

2. CIC-DUX4-specific published cell lines where any of these compounds have been tested — the cell-line literature for this rare tumor is extremely thin. DepMap/Cellosaurus has very limited CIC-DUX4 entries as of the knowledge cutoff.

3. Achievable tumor tissue concentrations (in biceps femoris primary or in lung metastasis) for any dietary compound. Plasma PK data exist for several compounds but tissue PK in extremity soft tissue is not characterized for dietary polyphenols.

4. The clinical significance of the piperine–ifosfamide CYP3A4 interaction at the doses the patient is actually taking (supplement product dose unknown). The cell-line and animal PK data support the interaction mechanism; human PK quantification of the interaction magnitude at typical supplement doses is not robustly established.

5. Whether the patient's current sulforaphane delivery from broccoli juice is effectively zero (probable, based on myrosinase inactivation during juicing) or whether gut bacterial conversion provides meaningful systemic exposure (possible but at 3–10× lower yield than myrosinase-activated preparation).

6. Whether the oligometastatic relapse (one lung lesion, May 2026) represents a clonally evolved tumor that may have acquired additional mutations affecting the V1 targets (BRD4 dependency, CDK4/CCND1 amplification). Clonal evolution through VDC/IE and radiotherapy cannot be assumed to have preserved the exact same molecular profile as the primary.

7. Whether whole-lung irradiation (completed) affects the bioavailability or efficacy of orally consumed compounds in the lung microenvironment — radiation alters local vascularity and stromal architecture in ways that could affect drug/nutrient distribution to the remaining lung metastasis.

---

## Standard-of-Care Interaction Summary (for orchestrator)

Priority interactions for THIS PATIENT with IMMINENT HIGH-DOSE IFOSFAMIDE:

| Compound | Interaction type | Mechanism | Priority | Action |
|---|---|---|---|---|
| Piperine (in curcumin+piperine supplement) | CYP3A4 + P-gp inhibition | Reduces ifosfamide prodrug activation (CYP3A4); increases vincristine/etoposide CNS exposure (P-gp) | HIGHEST — discuss before ifosfamide cycle | Oncologist review required |
| Curcumin | CYP3A4 + P-gp modulation; antioxidant during doxorubicin | Overlapping mechanism with piperine; alone less potent than piperine | HIGH | Oncologist review required |
| Thymoquinone (black cumin seed oil) | CYP3A4 inhibition | Same ifosfamide prodrug activation concern as piperine | HIGH | Oncologist review required |
| Liposomal vitamin C (high-dose) | ROS-axis interference | Reduces ROS-mediated cytotoxicity of doxorubicin and ifosfamide during active cytotoxic cycles | MODERATE — concern during active chemo; different profile during NED surveillance | Oncologist review for active chemo timing |
| Quercetin (at supplement doses; juice level lower) | CYP3A4 + P-gp modulation | Juice-level intake likely below threshold for significant clinical interaction; supplement doses would be relevant | LOW at juice level | Note for oncologist |
| Apigenin | CYP2C9 + modest CYP3A4 | Celery juice level likely below threshold | LOW at juice level | Note for oncologist |

Note: The patient is described as taking these in REST WEEKS between cycles. The interaction concern is highest during active chemotherapy cycles. During rest weeks and the NED year, the ROS-axis interaction with doxorubicin/ifosfamide does not apply; CYP3A4 interactions with any concurrent medications still apply. For the imminent high-dose ifosfamide course specifically: the question is whether the patient plans to continue curcumin+piperine and black cumin seed oil DURING or shortly before that treatment. This requires direct oncologist communication.
