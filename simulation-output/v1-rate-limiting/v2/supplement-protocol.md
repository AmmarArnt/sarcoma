# V1 Rate Limiting — Supplement Protocol (v2)
# Sub-agent role: Supplement Specialist
# Output for: Vector 1 Team Lead v2 reconciliation

Summary: Supplemental forms of V1 compounds — covering published clinical trial dose ranges (with citations), safety limits, and CYP3A4/P-gp interaction profiles against VDC/IE chemotherapy. Compounds without human trial data are flagged and stopped; extrapolation from cell-line concentrations to human supplement doses is not performed.

Confidence: Medium for CYP3A4/P-gp interaction flags (PK literature supports mechanisms); Low for anticancer efficacy from supplement doses (no sarcoma or CIC-DUX4 trial data exists for any dietary compound in this vector; all efficacy claims transfer from other indications with large concentration-mismatch caveats).

**PRIORITY NOTE FOR THIS PATIENT**: The patient is preparing to begin high-dose ifosfamide. Ifosfamide is a CYP3A4-activated prodrug. CYP3A4 inhibition reduces ifosfamide activation to its active alkylating metabolites (4-hydroxy-ifosfamide). Multiple compounds in the patient's current self-administered regimen inhibit CYP3A4. This is the highest-priority clinical interaction in this entire output. Every relevant compound is flagged below. Oncologist review is required before continuing any of these supplements during ifosfamide treatment.

---

## Chemo Interaction Screening Framework

Per `sarcoma-chemo-interactions` skill. Each V1 compound below is screened against:
- CYP3A4 modulation (vincristine, ifosfamide, etoposide activation/metabolism)
- P-gp modulation (vincristine, doxorubicin, etoposide efflux)
- ROS-axis interference (doxorubicin, ifosfamide mechanisms)
- CYP2B6/CYP2C9 (cyclophosphamide activation; apigenin)

---

## Per-Compound Supplement Entries

### Curcumin (Enhanced Formulation) [PATIENT TAKING — with piperine]

**Supplement forms with human PK data:**
- Conventional curcumin extract (>95% curcuminoids): very poor AUC; not preferred
- Phospholipid complex (Meriva/BCM-95): 29× higher AUC vs. unformulated in crossover PK study (Cuomo J et al., *J Nat Prod* 2011, PMID 21413822)
- Piperine co-formulation (BioPerine): see Shoba 1998 below

**Published trial dose ranges (none in CIC-DUX4 or sarcoma):**
- Safety/tolerability: Cheng AL et al., *Anticancer Res* 2001, PMID 11763884 — 4–8 g/day conventional extract; Phase I in Taiwan; no sarcoma; dose-limiting: nausea, GI at high doses
- Phase II cancer prevention (not CIC-DUX4): various doses 1–4 g/day enhanced formulations; none with sufficient tumor-tissue exposure data to confirm V1 BRD4 activity

**Concentration mismatch for V1 BRD4 mechanism**: Even with enhanced formulations, plasma free curcumin remains 0.1–1 µM; cell-line BRD4-chromatin disruption reported at 5–20 µM — 5–200× mismatch persists.

**CYP3A4**: Moderate inhibitor at supplement doses; documented in vitro and in human PK studies (Appiah-Opong R et al., *Toxicology* 2007; no PMID verified — mechanism inferred from curcumin-CYP3A4 PK literature [VERIFY]).
**P-gp**: Documented P-gp inhibitor in vitro (Anuchapreeda S et al., *Biochem Pharmacol* 2002, PMID 12363453).
**ROS-axis**: Antioxidant activity at supplement doses — theoretical interference with doxorubicin/ifosfamide ROS mechanism during active cytotoxic cycles.

**INTERACTION FLAG — HIGH PRIORITY**: Curcumin inhibits CYP3A4 and P-gp. During ifosfamide: reduces prodrug activation (reduced efficacy). During vincristine/etoposide: increases exposure and toxicity risk. The piperine co-formulation substantially amplifies both interactions (see Piperine entry).

**Consult oncologist before continuing during ifosfamide treatment — possible interactions with ifosfamide (prodrug activation), vincristine (CNS toxicity), etoposide (toxicity).**

---

### Piperine (component of curcumin+piperine supplement) [PATIENT TAKING]

**This is not a therapeutic compound for V1 purposes — it is a pharmacokinetic modifier and a CYP3A4/P-gp inhibitor. The V1 team classifies it here as a safety-priority compound, not a V1 therapeutic candidate.**

**Shoba 1998 caveat (mandatory verbatim per framework):**
> "The widely-cited '~2000% bioavailability increase' comes from Shoba et al., *Planta Medica* 1998 — a single-dose pharmacokinetic study, n=10 healthy volunteers, 2 g curcumin + 20 mg piperine. The curcumin-only control arm produced serum levels below the assay's limit of detection, so the '20×' number is computed against a near-zero baseline. The directional finding (piperine increases curcumin absorption) is real and reproduced; the **specific 2000% figure should not be cited as a universal multiplier**."

**CYP3A4**: Well-documented inhibitor. Alkaloid mechanism (inhibits CYP3A4 competitive/non-competitive). Documented in human PK studies of co-administered CYP3A4 substrates. (Bhardwaj RK et al., *Planta Med* 2002; no PMID verified [VERIFY] — mechanism from multiple PK interaction studies.)
**P-gp**: Documented P-gp inhibitor (Bhardwaj RK et al., *Planta Med* 2002 [VERIFY]).
**For ifosfamide specifically**: Ifosfamide requires CYP3A4 activation to 4-hydroxy-ifosfamide for alkylating activity. CYP3A4 inhibition by piperine reduces this conversion → reduces ifosfamide efficacy at the tumor. The magnitude of this interaction at typical supplement doses (typically 5–20 mg piperine) is not precisely quantified in published human PK literature for the ifosfamide combination specifically [no direct citation; interaction mechanism inferred from CYP3A4 dependency of ifosfamide activation and piperine CYP3A4 inhibition literature].

**INTERACTION FLAG — HIGHEST PRIORITY**: Piperine + ifosfamide is the single most important interaction in this patient's entire regimen. The PK mechanism for interaction is well-supported. Magnitude at supplement doses requires direct oncologist assessment.

**Consult oncologist before ifosfamide cycle — possible interference with ifosfamide prodrug activation (CYP3A4), increased vincristine CNS toxicity and etoposide toxicity (P-gp).**

---

### Thymoquinone (Black Cumin Seed Oil) [PATIENT TAKING]

**Human trial data for sarcoma**: None.
**Human trial data for cancer broadly**: Small human studies exist (Dehkordi FR & Kamkhah AF, *Saudi Med J* 2008 — for hypertension, not cancer; no applicable oncology dose trial).

**V1 mechanism**: NF-κB pathway inhibition and MAPK modulation documented in cancer cell lines (Shafi G et al., *Oncol Rep* 2009, PMID 19294336); concentration mismatch is substantial (~20–100 µM cell-line vs. achievable plasma levels); evidence tier: Preclinical-Cell, None direct in CIC-DUX4.

**CYP3A4**: In vitro inhibition documented (Al-Jenoobi FI et al., *Saudi Pharm J* 2015 — rat and human liver microsome studies [VERIFY specific PMID before citing externally]).
**P-gp**: Some in vitro P-gp inhibitory activity reported [no direct citation confirmed; mechanism inferred from thymoquinone-efflux transporter cell-line literature].
**ROS-axis**: Thymoquinone has antioxidant activity; theoretical concern during doxorubicin/ifosfamide.

**INTERACTION FLAG — HIGH PRIORITY**: Same ifosfamide CYP3A4 concern as piperine and curcumin. Three CYP3A4-inhibiting compounds in the patient's regimen are additive risk.

**Consult oncologist before ifosfamide cycle — possible interference with ifosfamide prodrug activation (CYP3A4); concurrent use with piperine and curcumin compounds additive concern.**

---

### EGCG (Green Tea Extract Supplement)

**Published trial dose ranges (none in CIC-DUX4 or sarcoma):**
- Cancer prevention (prostate): Bettuzzi S et al., *Cancer Res* 2006, PMID 16397214 — 600 mg/day EGCG (200 mg × 3) for 12 months; high-grade PIN; not sarcoma
- Safety: decaffeinated green tea extract at doses above 800–1000 mg/day associated with hepatotoxicity signal (Sarma DN et al., *Drug Safety* 2008 [no direct PMID verified; hepatotoxicity signal from FDA Green Tea Dietary Supplement Advisory 2017 — VERIFY current FDA advisory status])

**CYP3A4**: Moderate inhibitor at supplement doses (not food/tea level) [mechanism from CYP3A4-polyphenol PK literature; VERIFY specific PMID before external citation].
**P-gp**: In vitro P-gp inhibition documented (Jodoin J et al., *Biochim Biophys Acta* 2002, PMID 12100161).
**Topo II**: High-dose EGCG (cell-free assay) has Topo II–poison activity — theoretical concern with concurrent etoposide/doxorubicin; clinical relevance unclear.
**ROS-axis**: Antioxidant; theoretical concern during doxorubicin.

**INTERACTION FLAG — MODERATE**: P-gp inhibition affects vincristine/etoposide; CYP3A4 modulation affects ifosfamide; hepatotoxicity signal at supplement doses.

**Consult oncologist before starting EGCG supplements — possible interactions with vincristine (P-gp/CNS), etoposide (P-gp/toxicity), ifosfamide (CYP3A4 prodrug activation). Tea at food-level intake (2–3 cups/day) is a different risk profile from supplement doses.**

---

### Quercetin Supplement

**Published trial dose ranges (none in CIC-DUX4 or sarcoma):**
- Bioavailability/PK studies: Manach C et al., *AJCN* 2004, PMID 15113710 — general PK characterization
- Supplement use: various doses 500–1000 mg/day in cardiovascular and metabolic studies; no sarcoma data

**CYP3A4**: Moderate inhibitor at supplement doses; documented in vitro and in human PK studies (Okamoto T et al., *Methods Find Exp Clin Pharmacol* 2004 [VERIFY PMID]).
**P-gp**: In vitro P-gp inhibition; at supplement (not food) doses.
**Note for patient**: Apple juice (current patient intake) is at a dose well below supplement-level; quercetin interaction risk at juice-level intake is low. The concern applies if the patient were to add quercetin supplements.

**INTERACTION FLAG — LOW AT JUICE LEVEL; MODERATE IF SUPPLEMENTED**: Food/juice level below threshold for significant clinical CYP3A4/P-gp interaction; supplement doses (>500 mg/day) carry the same ifosfamide/vincristine concerns as curcumin.

**Consult oncologist before supplementing quercetin at supplement doses (>500 mg/day) during VDC/IE or ifosfamide — not currently in patient's supplement protocol based on available information.**

---

### Berberine

**Published trial dose ranges (none in CIC-DUX4 or sarcoma):**
- Metabolic syndrome: Zhang Y et al., *J Clin Endocrinol Metab* 2008, PMID 18397984 — 500 mg three times daily (1500 mg/day total); type 2 diabetes; not sarcoma
- No oncology-specific trial dose available

**Oral bioavailability**: ~1% (Tan HL et al., *Front Pharmacol* 2016, PMID 27917113). This is not a rounding error. The typical 500 mg dose produces systemic exposure equivalent to ~5 mg absorbed.

**CYP3A4**: Documented inhibitor; berberine and metabolites inhibit CYP3A4 despite poor oral bioavailability of parent compound (Guo Y et al., *Drug Metab Dispos* 2012 [VERIFY PMID]).
**P-gp**: Some modulation documented [no direct citation confirmed for specific P-gp interaction; inferred from P-gp/MDR literature on berberine-resistant cell lines].

**Note**: Despite 1% bioavailability, berberine consistently shows pharmacological effects in metabolic trials — proposed mechanisms include high local intestinal concentrations and gut microbiome conversion. Whether MAPK suppression relevant to V1 occurs at achievable systemic levels is not established.

**INTERACTION FLAG — MODERATE**: CYP3A4 inhibition despite poor bioavailability adds to the cumulative CYP3A4 inhibitor burden from curcumin+piperine and thymoquinone.

**Consult oncologist before starting berberine during ifosfamide treatment — additive CYP3A4 inhibition concern.**

---

### Omega-3 EPA/DHA Supplement

**Published dose ranges:**
- Cardiovascular: Multiple RCT — 1–4 g/day EPA+DHA (REDUCE-IT: 4 g/day icosapentaenoic acid [Bhatt DL et al., *NEJM* 2019, PMID 30415628]; VITAL: 1 g/day omega-3 [Manson JE et al., *NEJM* 2019, PMID 30415629])
- Anti-cancer adjunct: VITAL found no significant cancer incidence reduction overall; some subgroup signals not established

**Chemo interactions:**
- CYP3A4: Not a significant modulator at standard doses
- P-gp: Not a significant modulator
- ROS-axis: At 1–4 g/day doses, omega-3 has mild antioxidant activity but this is not at the level of NAC, vitamin C, or vitamin E — not the canonical antioxidant-chemo concern
- Antiplatelet: At higher doses (≥4 g/day), mild antiplatelet effect documented; relevant in surgical context (this patient had surgery in Jan 2025; active-treatment phase now)

**INTERACTION FLAG — LOW**: Omega-3 at food-to-supplement doses (1–4 g/day) does not carry the CYP3A4/P-gp concerns of curcumin, piperine, or thymoquinone. Mild antiplatelet effect at higher doses is worth noting in surgical planning context.

**Generally the safest V1 cross-vector supplement; consult oncologist for dose confirmation.**

---

### Vitamin D3 Supplement (Cross-vector V3/V4; listed here for completeness)

**Published dose ranges:**
- VITAL: 2000 IU/day (Manson JE et al., *NEJM* 2019, PMID 30415629)
- Correction of deficiency: dose varies by baseline 25-OH-D level; standard practice

**Chemo interactions:**
- CYP3A4: Vitamin D3 is metabolized by CYP3A4 (CYP27B1 primarily, but CYP3A4 involvement documented); not a strong inhibitor of CYP3A4 for other substrates
- P-gp: Not a significant modulator
- ROS-axis: Not applicable

**INTERACTION FLAG — LOW at supplemental doses**: Not a primary ifosfamide interaction concern. Deficiency correction is the clearest indication.

**Consult oncologist for current 25-OH-D level and appropriate dose if supplementation is indicated.**

---

### Selenium (Deficiency Correction Only)

**Published dose range:**
- Nutritional Prevention of Cancer trial: 200 µg/day selenized yeast (Clark LC et al., *JAMA* 1996, PMID 8971564) — SELECT was null (Lippman SM et al., *JAMA* 2009, PMID 19066370)
- Adult dietary reference intake: ~55 µg/day; Tolerable Upper Limit: 400 µg/day

**Safety window**: Narrow. Selenosis symptoms begin above 400 µg/day; frank toxicity at higher doses. Food sources (1–2 Brazil nuts/day) are the safer delivery route than supplements for most individuals.

**Chemo interactions:**
- CYP3A4/P-gp: Not a clinically significant modulator
- ROS-axis: Selenoproteins (glutathione peroxidase, thioredoxin reductase) are antioxidant — theoretical concern during ROS-dependent chemo at high supplemental doses; food-level is not the concern
- SELECT null trial: Selenium supplementation did not reduce cancer incidence; potential harm signal in men with high baseline selenium (Kristal AR et al., *J Natl Cancer Inst* 2014, PMID 24563519)

**INTERACTION FLAG — LOW AT FOOD LEVEL; NARROW WINDOW IF SUPPLEMENTED**: Brazil nuts (1–2/day) are the preferred delivery route; selenium supplementation above the RDA requires oncologist discussion.

---

## Compounds Without Sufficient Human Trial Data to Supplement

The following compounds have V1 mechanistic plausibility but lack human trial data at any defined dose for any indication. Per the schema requirement: state this and stop — do not extrapolate cell-line concentrations.

| Compound | Status |
|---|---|
| Fisetin | No human cancer trial data for supplemental fisetin at any defined dose; only Phase I in elderly humans (senolytic context — NCT02848131 [VERIFY]; not oncology); cannot report a dose for oncology context |
| Apigenin | No human trial data for supplemental apigenin at defined doses; cannot report a dose |
| Luteolin | No human trial data for supplemental luteolin at defined doses; cannot report a dose |
| 6-Gingerol (isolated) | No human trial data for isolated 6-gingerol supplementation; ginger extract trials are not equivalent; cannot report a dose |
| Lycopene | Some small RCT data (prostate context; not sarcoma); not sufficient to carry into a V1 sarcoma supplement protocol |

---

## What I Could Not Establish

1. The actual piperine dose in the patient's specific curcumin+piperine supplement product — product formulations vary widely; the 20 mg piperine dose used in Shoba 1998 may or may not match the patient's product.

2. Human PK quantification of the piperine–ifosfamide interaction magnitude at typical supplement doses — the mechanism is supported; the clinical magnitude in a human cancer patient is not robustly published.

3. Whether additive CYP3A4 inhibition from three concurrent compounds (piperine + curcumin + thymoquinone) produces clinically meaningful reduction in ifosfamide activation beyond any single compound — no published data on this specific combination in cancer patients.

4. Regulatory approval status for any supplement compound in any country — no supplement in this list is approved as a cancer therapeutic anywhere; this is a research output, not a product endorsement.

5. Whether current (2026) bioavailability-enhanced curcumin formulations (SLCP, micellar, nanoparticle) achieve plasma levels closer to V1-relevant concentrations — newer formulations may have higher AUC but published clinical data with these newer forms remain limited.
