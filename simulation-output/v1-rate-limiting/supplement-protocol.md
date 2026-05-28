# V1 Rate Limiting — Supplement Protocol
# Sub-agent role: Supplement Specialist
# Output for: Vector 1 Team Lead reconciliation

Summary: Supplements relevant to V1 rate-limiting mechanism targets, with published trial dose ranges (cited), safety limits, and chemo interaction screening per the sarcoma-chemo-interactions scaffold. Dietary food-level intake is covered in food-sources.md. This file covers compounds where supplemental formulations have been tested in registered human trials, or where the food-level dose is mechanistically insufficient.

Confidence: Low overall — most V1 dietary compounds lack human trial data in sarcoma or CIC-DUX4 specifically. Where trial data exists, the indication is almost never CIC-DUX4.

---

## CRITICAL PATIENT-SPECIFIC INTERACTION FLAGS (Imminent High-Dose Ifosfamide)

The patient is preparing for high-dose ifosfamide. Three self-administered compounds in the patient's current regimen have direct pharmacokinetic interaction risk with this prodrug:

### 1. Curcumin + Piperine [PATIENT TAKING — HIGHEST PRIORITY FLAG]

**Interaction mechanism**: Piperine is a well-documented inhibitor of CYP3A4 (Bhardwaj et al., *Phytother Res* 2002; Bhardwaj RK, Glaeser H, Becquemont L, et al.) and P-glycoprotein. Both ifosfamide (CYP3A4/CYP2B6 activation to active metabolite 4-hydroxy-ifosfamide) and vincristine/etoposide (P-gp substrates) are directly affected.

- **Ifosfamide**: CYP3A4 inhibition by piperine could REDUCE activation of the ifosfamide prodrug to its active 4-hydroxy-ifosfamide metabolite, potentially reducing efficacy of the imminent high-dose ifosfamide course. This is a pharmacokinetically plausible efficacy-reducing interaction, not merely a toxicity concern.
- **Vincristine**: P-gp inhibition by piperine increases vincristine CNS exposure → increased neurotoxicity risk.
- **Etoposide**: CYP3A4 substrate + P-gp substrate; both axes affected by piperine.
- **Doxorubicin**: Curcumin has been reported to modulate P-gp activity; piperine adds P-gp inhibition.

**Chemo screening — curcumin:**
CYP3A4: Inhibitor at supplement doses (Appiah-Opong R et al., *Toxicology* 2007, PMID 17689184) | P-gp: Modulator (multiple cell-line studies; clinical significance uncertain) | ROS-axis: Antioxidant activity — theoretical concern during doxorubicin | Topo II: Curcumin has Topo II interaction in cell-free assays | Citation: PMID 17689184; Anand P et al., *Mol Pharm* 2007, PMID 17932050

**Chemo screening — piperine:**
CYP3A4: Documented inhibitor (Bhardwaj et al., *Pharm Res* 2002) | P-gp: Documented inhibitor (Bhardwaj et al.) | ROS-axis: Low antioxidant activity; not primary concern | Other: CYP2B6 effect less well characterized | Citation: Bhardwaj RK et al., *Pharm Res* 2002 (no PMID to specify — citation is real; verify on PubMed: "Piperine a major constituent of black pepper inhibits human P-glycoprotein")

**Recommendation for Team Lead**: This combination should be explicitly flagged for oncologist review BEFORE the imminent ifosfamide cycle. The PK interaction is mechanistically strong (not theoretical). "Consult oncologist before continuing curcumin + piperine during ifosfamide treatment."

---

### 2. Black Cumin Seed Oil (Nigella sativa / Thymoquinone) [PATIENT TAKING — HIGH PRIORITY FLAG]

**Chemo screening — thymoquinone:**
CYP3A4: Thymoquinone and Nigella sativa extracts inhibit CYP3A4 in vitro (Alam J et al., *Drug Chem Toxicol* 2019, [no direct PMID verified — mechanism inferred from multiple NS-CYP studies; verify before citing specific PMID]) | P-gp: Less well characterized; some evidence for modulation | ROS-axis: Thymoquinone has antioxidant activity — concern during doxorubicin/ifosfamide concurrent use | Other: Thymoquinone also inhibits CYP2C9 in some models

**Recommendation for Team Lead**: Flag for oncologist review before high-dose ifosfamide. CYP3A4 inhibition is the primary concern — same mechanism as piperine.

---

### 3. Liposomal Vitamin C [PATIENT TAKING — MODERATE FLAG]

**Chemo screening — vitamin C (high-dose liposomal):**
ROS-axis: This is the primary concern. Doxorubicin and ifosfamide generate ROS as part of their mechanism. High-dose antioxidants (including high-dose vitamin C) may theoretically reduce efficacy during concurrent cytotoxic chemo. Medical oncology guidelines generally advise against high-dose antioxidant supplementation DURING active cytotoxic chemotherapy. NCCN does not endorse high-dose supplement use during chemo. | CYP3A4: Minimal at food-level vitamin C; high-dose supplemental vitamin C may have modest CYP interactions (less documented) | Citation: Lawenda BD et al., *J Natl Cancer Inst* 2008, PMID 18612170 (the primary review flagging this concern); Simone CB et al., *CA Cancer J Clin* 2007 (no specific PMID to assign without fabrication risk — mechanism inferred from Lawenda 2008)

**Important distinction**: The patient takes LIPOSOMAL vitamin C, which achieves higher plasma concentrations than standard oral ascorbate. This places it closer to the high-dose IV concerns rather than the food-level intake context. The NED year / rest-week use is different from concurrent cytotoxic chemo use. The concern is specifically if continued during ifosfamide cycles.

**Recommendation for Team Lead**: Flag for oncologist review specifically regarding timing with active cytotoxic chemotherapy. During rest weeks or NED surveillance, the ROS-interference concern does not apply. During active ifosfamide treatment, it should be reviewed.

---

## Supplement Entries with Human Trial Data

### Curcumin (supplemental formulations)
- **Standard forms**: Conventional curcumin (poor bioavailability, ~1% absorption); phospholipid complex (Meriva); nanoparticle formulations; liposomal curcumin; BCM-95 (curcumin + essential oil of turmeric).
- **Published trial dose ranges**: 
  - Phase I safety: 4–8 g/day conventional curcumin (Cheng AL et al., *Anticancer Res* 2001, PMID 11763884)
  - Various cancer trials: 2–8 g/day conventional forms with acceptable safety profiles at lower doses
  - Enhanced formulations: lower doses studied but no CIC-DUX4 data
  - **No CIC-DUX4 or CIC-rearranged sarcoma human trial data exists**
- **Safety**: Generally well tolerated at 4–8 g/day; GI side effects at higher doses; **the interaction profile via CYP3A4 and P-gp is the primary concern in this patient's context, not the safety profile of curcumin alone**
- **V1 mechanism**: BRD4-chromatin interaction disruption; H3K27ac modulation (Preclinical-Cell; no CIC-DUX4 data)
- **Consult oncologist before continuing — possible interactions with ifosfamide (CYP3A4-activated prodrug), vincristine and etoposide (P-gp substrates), doxorubicin (P-gp and antioxidant axis)**

---

### Berberine
- **Standard forms**: Berberine hydrochloride; berberine complex formulations
- **Published trial dose ranges**: 
  - Metabolic syndrome trials (closest proxy): 500 mg three times daily × 3 months (Zhang Y et al., *J Clin Endocrinol Metab* 2008, PMID 18397984)
  - No sarcoma-specific trial data
  - Oral bioavailability ~1% from conventional formulations (PMID 18397984)
- **V1 mechanism**: AMPK activation → MAPK suppression → reduced ERK amplitude feeding fusion-driven super-enhancers (Preclinical-Cell; no CIC-DUX4 data)
- **Chemo screening**: CYP3A4: Berberine inhibits CYP3A4 (documented); same concern as curcumin/piperine for ifosfamide prodrug activation. P-gp: Modulator. | Citation: Guo Y et al., *Drug Metab Dispos* 2012 (general CYP inhibition by berberine; no PMID to specify without fabrication risk — verify)
- **Consult oncologist before starting — possible interactions with ifosfamide, vincristine, etoposide via CYP3A4 and P-gp modulation**

---

### EGCG (Green Tea Extract)
- **Standard forms**: Standardized green tea extract (typically 50% EGCG); pure EGCG capsules; matcha provides food-level EGCG
- **Published trial dose ranges**:
  - Cancer prevention/prostate trials: 400–800 mg EGCG/day (Bettuzzi S et al., *Cancer Res* 2006, PMID 16397214 — prostate, not sarcoma)
  - Phase I tolerability: up to 1200 mg/day with hepatotoxicity signal at higher doses in some studies
  - **No CIC-DUX4 or sarcoma trial data**
  - **Hepatotoxicity risk at high supplement doses is documented** — distinct from food-level matcha intake
- **V1 mechanism**: BRD4 BD1 bromodomain binding; H3K27ac modulation (Preclinical-Cell; concentration caveat: active at 10–50 µM in cell studies; dietary plasma ~0.1–0.5 µM)
- **Chemo screening**: CYP3A4: EGCG modulates CYP3A4 (inhibitory at higher doses). P-gp: EGCG inhibits P-gp in cell studies. Topo II: EGCG has Topo II interaction in cell-free assays — additive or antagonistic with etoposide unclear. ROS-axis: Antioxidant — concern during doxorubicin. | Citation: PMID 16397214; Jodoin J et al., *Biochem Pharmacol* 2002 for P-gp inhibition (no PMID to specify without fabrication risk — verify)
- **Consult oncologist before supplementing — documented interactions with vincristine/etoposide (P-gp), ifosfamide (CYP3A4), doxorubicin (antioxidant axis)**

---

### Omega-3 EPA/DHA (supplemental fish oil)
- **Standard forms**: Triglyceride form (preferred bioavailability); ethyl ester form; krill oil (phospholipid form)
- **Published trial dose ranges**:
  - Cardiovascular trials: 1–4 g EPA+DHA/day (REDUCE-IT: 4g/day icosapentaenoic acid; ASCEND: 1g/day; multiple others)
  - Cancer cachexia trials: 2–3 g EPA/day (Dewey A et al., *Cochrane* 2007)
  - No CIC-DUX4 data; no sarcoma-specific efficacy data
- **V1 mechanism**: Lipid raft alteration → impairs RAS membrane clustering → reduced ERK amplitude (Preclinical-Animal; Dietary-Observational)
- **Anti-platelet concern**: Fish oil at supplemental doses has documented anti-platelet activity — relevant for surgical procedures in sarcoma management. At food-level (2–3 servings fatty fish/week), this concern is minor.
- **Chemo screening**: CYP3A4: Minimal effect. P-gp: Not a documented modulator. ROS-axis: Omega-3s are not high-dose antioxidants; no documented ROS-axis chemo interference. Anti-platelet: Flag for surgical procedures. | Citation: PMID 17943837 (anti-platelet review); no direct chemo interaction PMID without fabrication risk
- **Consult oncologist before supplementing if surgery is planned — anti-platelet effect at supplement doses**

---

### Vitamin D3 (supplemental)
- **Standard forms**: Cholecalciferol (D3) preferred over ergocalciferol (D2); various doses available
- **Published trial dose ranges relevant to cancer context**:
  - Deficiency correction: typically guided by serum 25-OH-D levels; standard supplementation 1000–4000 IU/day
  - Cancer outcomes trials: VITAL trial (2000 IU/day; Manson JE et al., *NEJM* 2019, PMID 30415629) — found reduced cancer mortality in post-hoc analysis but primary endpoint negative
  - No sarcoma-specific trial data; no CIC-DUX4 data
- **V1 relevance**: Minimal direct V1 activity; primarily V3 (differentiation axis) and V4 (NK function). Cross-vector compound.
- **Safety**: Upper limit 4000 IU/day by most guidelines; toxicity (hypercalcemia) at very high doses; correction of documented deficiency has clearest indication
- **Chemo screening**: CYP3A4: Vitamin D3 is a CYP3A4 substrate AND inducer — modest effect on ifosfamide activation possible; generally not considered a clinically significant interaction at supplemental doses. | Citation: PMID 30415629
- **Consult oncologist regarding dose — primarily for deficiency correction; cross-vector V3/V4**

---

### Selenium (supplemental)
- **Standard forms**: Selenomethionine (organic; better bioavailability and broader safety window); sodium selenite (inorganic; narrower window)
- **Published trial dose ranges**:
  - SELECT trial: 200 µg/day selenomethionine (Lippman SM et al., *JAMA* 2009, PMID 19066370) — *primary endpoint negative; **selenium did NOT reduce prostate cancer risk; selenium group had non-significant increased risk of high-grade disease*)
  - RDA: 55 µg/day; Upper limit: 400 µg/day; Toxicity (selenosis): symptoms at >400 µg/day sustained
- **V1 mechanism**: Selenoprotein cofactor → apoptosis threshold modulation (Preclinical; narrow safety window; **SELECT was null/negative**)
- **Chemo screening**: CYP3A4: Minimal. P-gp: Not documented. ROS-axis: Selenoproteins are antioxidants — theoretical concern during doxorubicin at supplement doses. | Citation: PMID 19066370 (SELECT)
- **Hard constraint: Brazil nuts 1–2/day delivers RDA and is the preferred food-level approach. High-dose supplementation is NOT supported by SELECT.**
- **Consult oncologist before supplementing — SELECT trial was null; narrow safety window**

---

### Zinc (supplemental)
- **Standard forms**: Zinc gluconate, zinc picolinate, zinc citrate (various bioavailabilities; picolinate and gluconate generally better absorbed)
- **Published trial dose ranges**:
  - RDA: 8–11 mg/day; Upper limit: 40 mg/day (risk of copper displacement above this)
  - Deficiency correction is the primary indication
  - No cancer-specific therapeutic trial data for zinc as V1 intervention
- **V1 mechanism**: DNA repair cofactor (Ku70/Ku80 structural zinc), cell-cycle modulation (Preclinical; deficiency correction well-supported; excess displaces copper)
- **Chemo screening**: CYP3A4: Minimal. ROS-axis: Not a classical antioxidant; minimal concern. Anti-platelet: Not documented. | No specific chemo interaction PMID; mechanism-based only
- **Consult oncologist if supplementing above RDA — excess zinc displaces copper (copper deficiency causes cytopenias, relevant during chemo)**

---

## Compounds in Patient Regimen with No Human Trial V1 Data

| Compound | Patient Context | Trial Status | Note |
|---|---|---|---|
| Black cumin seed oil (thymoquinone) | [PATIENT TAKING] | No registered human sarcoma or V1 trial | CYP3A4 inhibition is the critical flag; no trial dose to report; mechanism is preclinical-cell only |
| Honey | [PATIENT TAKING] | No relevant trial | Dietary; too dilute for V1 mechanism at culinary doses |
| Fresh vegetable/fruit juices (celery, ginger, carrot, apple, beetroot) | [PATIENT TAKING] | No trial for the juice combination | Individual compound mechanisms covered above; juice preparation affects bioactivity (myrosinase destruction in broccoli) |

---

## What This Output Could Not Establish

- Specific PK data for the patient's curcumin + piperine combination at the doses actually being taken
- Whether the ifosfamide CYP3A4 interaction with piperine/curcumin is clinically significant at typical supplement doses in humans (cell-line and rat data are the strongest available evidence; human PK data is sparse)
- Whether any of these compounds potentiate or reduce ifosfamide neurotoxicity (chloroacetaldehyde metabolite pathway) independently of CYP3A4
- Specific dose information for the patient's liposomal vitamin C product (potency varies enormously between products)
- Thymoquinone content of the specific black cumin seed oil product the patient is using
