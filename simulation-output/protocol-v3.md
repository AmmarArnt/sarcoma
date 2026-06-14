# CIC-Rearranged Sarcoma — Multi-Vector Hypothesis Catalog (v3)

> **Clean-slate run v3.** Derived from scratch from this run's four vector summaries
> (`v1-summary-v3.md`, `v2-summary-v3.md`, `v3-summary-v3.md`, `v4-summary-v3.md`), the reused mRNA
> team summary (`mrna-vaccine-summary-v2.md`), the standing analytical layers (ADR-0016), and the
> Metastatic Disease Specialist (`metastatic-disease-considerations-v3.md`, run this session). It does
> **not** copy or anchor to `protocol-v1.md` / `protocol-v2.md` — those baselines are preserved.
> **Research simulation / hypothesis generation only. NOT medical advice. No dosing, no start/stop
> instructions for any therapy.** Regulatory/trial status is perishable — every such fact is dated or
> tagged `[VERIFY]`.

---

## KEY-MAP CALLOUT — what V1–V4 mean (read this first)

The four **attack vectors are fixed** (golden rule #8). Each names a *molecular goal*, not a delivery
format:

| Vector | Name | What it tries to do (biology) |
|---|---|---|
| **V1** | **Rate Limiting** | Slow how fast the CIC-DUX4 oncogenic loop runs and how loud its output is — dampen upstream RAS/ERK, throttle the BRD4 / super-enhancer amplifier, add friction at the CDK4/CCND1 cell-cycle gate. Does **not** fix the fusion. |
| **V2** | **Compiler Protection** | Reduce the rate at which *at-risk neighbouring* mesenchymal progenitors acquire a translocation — lower ROS/DSB burden, improve DNA-repair fidelity. Upstream **prevention** logic; least applicable to an existing tumour. |
| **V3** | **Hot Patching** | Restore the deleted "break condition" *inside* cells that already carry the fusion — epigenetic reprogramming (HDACi/DNMTi → MHC-I), differentiation, degraders/ASOs, synthetic-lethal dependencies (MCL1, CDK4). The most clinically loaded vector. |
| **V4** | **Immune Watchdog** | Make fusion-carrying cells *visible to and clearable by* the immune system — MHC-I restoration → T-cell/checkpoint, NK missing-self, the Nectin–TIGIT–DNAM-1 axis, danger-signalling/ICD. |

Two **cross-cutting axes** (NOT vectors): the **modality axis M1–M8** (*how* it is delivered — ADR-0018)
and the standing **analytical layers** (host-biology, VoI/diagnostic, feasibility/attrition,
transferability, driver-uncertainty — they condition/annotate, never override real-data vector evidence
and never prune the forward lane).

---

## Framing

This is a structured, multi-agent **research exercise** that maps the CIC-rearranged sarcoma (CIC-DUX4)
oncogenic program onto a software-engineering analogy, then explores four parallel intervention vectors —
most dietary/mechanistic, some clinical/experimental. The deliverable is a **ranked, evidence-tiered
hypothesis catalog plus forward (not-yet-tested) hypotheses** — never a treatment plan. Intended use, in
order: (1) a simulation/research output; (2) personal exploration of the literature; (3) *only if* a
non-obvious, mechanistically grounded hypothesis emerges, a conversation-starter with a qualified
oncologist. **Every dietary entry carries the standing annotation: "potential interactions with
standard-of-care chemotherapy and concurrent medications — must be reviewed by the patient's oncologist
before any change."**

**Epistemic posture.** Most entries below are **Mechanistic** or **Preclinical-Cell** tier. There is
**zero CIC-DUX4-specific clinical evidence** for any dietary compound and almost none for any drug; the
value of this catalog is its structure and honest grounding, not the number of entries.

**Atypical-case anchor (this patient).** This case is **FUSION-UNCONFIRMED** — the ~5% genomically
uncharacterized subgroup with no confirmed CIC-DUX4/CIC-NUTM1/CIC-FOXO4 fusion. Throughout, every entry
is marked **fusion-agnostic** (applies regardless of driver, incl. the atypical ~5%) or **fusion-confirmed
only** (depends on the fusion protein/junction — junction ASOs, junction-specific neoantigen vaccines/TCR-T,
and the MCL1 "re-arm" line). Fusion-confirmed-only entries are held as **driver-contingent (HOLD until the
driver is resolved)** per the driver-uncertainty model (ADR-0008).

### Patient case (anchors the whole catalog)
Soft-tissue CIC-rearranged sarcoma, dx **June 2024**, **FUSION-UNCONFIRMED**. Primary biceps femoris right
thigh; **12 lung metastases at diagnosis**. EURO EWING **VDC/IE ×14 cycles**, good response; **surgery Jan
2025 (>95% necrotic)**; radiation to leg + **whole-lung irradiation (WLI)**. **NED May 2025 → May 2026**;
**May 2026 oligometastatic relapse** (single cluster, one lung). Patient is **NOW beginning HIGH-DOSE
IFOSFAMIDE**.

---

## Top-Level Findings

The most defensible / decision-relevant reads across all four vectors, the layers, and the metastatic
specialist (each tagged with evidence tier; F-band where access matters):

1. **The single most actionable item today is a safety screen of the patient's OWN regimen, not a new
   intervention: a convergent THREE-compound CYP3A4 signal (piperine + curcumin + thymoquinone) against
   the imminent high-dose ifosfamide, a CYP3A4/CYP2B6-activated prodrug.** Because the *same* enzyme sits
   at the branch point between ifosfamide **activation** (→ ifosfamide mustard, efficacy) and
   **N-dechloroethylation** (→ chloroacetaldehyde, neuro/nephrotoxicity), the net effect of a CYP3A4
   modulator is **not predictable in direction** — flag for oncologist/pharmacist review, **not** a
   stop/start instruction. [Mechanistic / Established for the baseline ifosfamide pharmacology] **F1
   (actionable now).** *Fusion-agnostic.*

2. **The catalog's central V3→V4 bridge agent changed access status with no change in biology:
   tazemetostat (EZH2i) was voluntarily withdrawn WORLDWIDE from ALL indications on 2026-03-09** (Ipsen;
   SYMPHONY-1 secondary-malignancy signal, 5.7% vs 0% MDS/AML) — and it was **never EMA-approved**. The
   *mechanism class* survives; the named drug does not. The clean MHC-I-restoration bridge is now anchored
   on **class-I HDAC inhibitors and DNMT inhibitors** (FDA-approved for other indications, **F1
   repurposable**), not tazemetostat. [Established (withdrawal, dated 2026-03-09, `[VERIFY]`) / Clinical-Trial
   (HDACi/DNMTi mechanism class)] *Fusion-agnostic.*

3. **EZH2 is NOT a survival dependency in the fusion-round-cell proxy (DepMap), and a 2024 CIC-DUX4
   chromatin study points to p300/CBP, not PRC2, as the fusion-specific epigenetic dependency.** This
   re-positions EZH2i as (at most) an MHC-I primer, not a cytotoxic agent — and, combined with #2, takes
   EZH2i off the table as an actionable bridge for this patient. [Preclinical-Cell, real DepMap CRISPR;
   CIC-DUX4-direct chromatin profiling — Bakaric 2024, PMID 38275898] *Fusion-agnostic.*

4. **The highest-ceiling NOVEL target — MCL1 ("re-arm the DUX4 death program") — is DRIVER-CONTINGENT and
   on HOLD for this fusion-unconfirmed patient.** Two independent 2025 *Nat Commun* papers (PMID 40841513,
   PMID 40841360) show CIC::DUX4 tumoroids depend on MCL1 because the retained DUX4 transactivation domain
   forces an anti-apoptotic buffer. That domain exists only if the driver is truly CIC-DUX4 (D1). [Preclinical-Cell
   + Preclinical-Animal — highest-tier *direct* CIC-DUX4 finding in the catalog] **F2/F3.** **Fusion-confirmed
   only — HOLD until driver resolved.**

5. **CDK4 (not CDK6) is the selective, driver-ROBUST cell-cycle dependency** — applicable regardless of
   which driver (D1–D5) is present. CDK4/6 inhibitors are FDA+EMA approved (breast); sarcoma data are small
   and the one CIC-DUX4 xenograft signal for palbociclib was *limited* `[VERIFY]`. The safest clinical-track
   entry to discuss regardless of driver resolution — but cytostatic, with CCNE1 bypass. [Established (breast)
   / Clinical-Trial (sarcoma) / Preclinical-Cell (selective dependency)] **F1.** *Fusion-agnostic.*

6. **NK missing-self is the strongest single immune lever AND the relapsed clone is the setting where it
   is most relevant** — MHC-I-low cells that hide from T-cells are paradoxically NK-susceptible *if* they
   co-express stress ligands (MICA/MICB/ULBP, PVR/CD155). The VoI layer independently ranks the **nectin
   (CD155/CD112) axis #1 and HLA-E #2** as the highest-value *unmeasured* biomarkers — both NK-arm variables.
   [Mechanistic] *Fusion-agnostic.* **Genuine asymmetry (red-team):** the checkpoint arm's lead hypothesis
   has a self-falsifying biomarker gate; the NK-first arm does **not** — its load-bearing "doubly cold?"
   assumption (stress-ligands also absent) is unmeasured.

7. **The post-ifosfamide lymphodepletion/reconstitution window is the dominant near-term immune-state
   reality** and the most mechanistically plausible point for any NK- or T-cell-directed measure (IL-7/IL-15
   homeostatic proliferation). Not an agent recommendation — a **timing** observation. [Mechanistic] *Fusion-agnostic.*

8. **Checkpoint-inhibitor monotherapy carries a NEGATIVE-leaning prior here:** sarcoma CPI response (SARC028,
   Alliance A091401) concentrated in high-TMB histotypes (UPS/DDLPS) — the *opposite* of CIC-DUX4's
   genomically-simple, presumed-low-TMB profile (Italiano, PMID 27664537, CIC-DUX4-direct). One March-2025
   case report (PMID 40128305 `[VERIFY]`) shows a *fusion-confirmed* CIC::DUX4 tumour converting cold→hot
   under nivolumab+relatlimab — a disease-class precedent only. [Clinical-Trial] *Fusion-agnostic mechanism.*

9. **The antioxidant-vs-ROS-chemo AND antioxidant-vs-metastasis conflicts are genuine, unresolved, and
   sharpened by the metastatic context:** high-dose liposomal vitamin C sits closer to the Heaney-2008
   "protective/chemo-blunting" plasma range than the IV pro-oxidant range, and the Sayin-2014 antioxidant→
   metastasis signal moves from academic (in NED) to load-bearing in an *actively seeding* oligometastatic
   window. [Mechanistic / Preclinical-Animal-by-analogy] **F1 (caution item).** *Fusion-agnostic.*

10. **mRNA COVID-19 vaccination is a NULL finding for this patient's current biology** (2+ years out) —
    stated explicitly, not omitted. The one carry-forward is a *design-level* anti-PEG flag for any *future*
    LNP-mRNA cancer vaccine. [Clinical-observational] *Fusion-agnostic.*

---

## Naturally Achievable Track

> Dietary / lifestyle / well-established supplements at safe doses. **This is the only track the patient
> could act on directly — and only with oncologist review.** Every entry: *"potential interactions with
> standard-of-care chemotherapy and concurrent medications — must be reviewed by the patient's oncologist
> before any change."* Most entries are honest about a **1–3 order-of-magnitude concentration mismatch**
> between cell-line-active and dietary-achievable plasma levels, and **none has CIC-DUX4-specific evidence**.

### Diet (mechanistically grounded, food-level)

| Compound | Vector(s) | Mechanism (molecular, 1 sentence) | Tier | CIC-DUX4 direct? | Food sources | SOC contraindications |
|---|---|---|---|---|---|---|
| **Omega-3 EPA/DHA** | V1, V2, V4 | Incorporated into membrane phospholipids → alters lipid-raft composition/RAS clustering (V1); EPA/DHA → SPMs (resolvins/protectins/maresins) resolve inflammation via ChemR23/ALX-FPR2/GPR32 receptors, *not* ROS scavenging (V2/V4) | Dietary-Observational + Mechanistic (strongest cross-vector tier) | None direct | Sardines, mackerel, wild salmon, herring, oysters | Antiplatelet at high dose (surgery-relevant); does **not** carry the ROS-scavenging chemo-blunting concern (receptor-mediated mechanism). **Absent from this patient's regimen.** |
| **Sulforaphane** (glucoraphanin) | V1, V3, V4 | Weak class-I HDAC inhibition (HDAC3 depletion via 14-3-3/Pin1); Nrf2-ARE induction | Preclinical-Cell | None direct | Broccoli **sprouts** (10–100× sprout:floret glucoraphanin); needs myrosinase from chop/chew + ~40 min stand | **Juicing very likely destroys myrosinase → near-zero active delivery** (preparation finding, not an ingredient problem). No specific CYP/P-gp flag. |
| **Quercetin** | V1, V2, V3 | Multi-kinase/RTK-RAS modulation (V1); MCL1 downregulation + BH3-mimetic + weak EZH2 modulation (V3) | Preclinical-Cell | None direct | Capers, raw red-onion outer layers, apple skin | **CYP3A4 inhibitor (IC50≈1.97 µM) + P-gp modulator** — raised etoposide & doxorubicin bioavailability in rat PK (PMID 21544726, 19414395). Supplement-bolus (not apple-juice glycoside) is the concern vs ifosfamide. |
| **Curcumin (+ piperine)** | V1, V2, V3 | Reported BRD4-chromatin/H3K27ac disruption (V1); NF-κB/STAT3 modulation (V2) | Preclinical-Cell | None direct | Turmeric (fat-soluble; cook in oil) | **CYP3A4 (IC50≈2.7 µM in vitro; in-vivo direction unresolved) + P-gp inhibitor.** Piperine adds CYP3A4/P-gp. **See SOC Interaction Map — convergent ifosfamide flag.** Bioavailability: Shoba-1998 caveat (below). |
| **Apigenin / Luteolin** | V1, V2 | Reported reduction of ETS-factor expression (apigenin); cell-cycle modulation (luteolin) | Preclinical-Cell | None direct | Parsley > celery (leaves) | Plasma ~0.03–0.34 µM vs 10–50 µM cell-line → **~30–1800× mismatch**; no specific flag identified (not exhaustively screened). |
| **6-Gingerol** | V1, V2 | NF-κB/MAPK modulation at high in-vitro conc. | Preclinical-Cell | None direct | Fresh ginger | ~50–500× mismatch; non-detectable free gingerol at dietary intake (AACR 2008); benign culinary addition. |
| **EGCG** | V1, V2, V3 | Reported BRD4 BD1 binding; weak EZH2/DNMT modulation | Preclinical-Cell | None direct | Matcha, brewed green tea | CYP3A4/P-gp modulator at higher conc.; **hepatotoxicity signal ≥800 mg/day supplement `[VERIFY]`** — independent hepatic concern given VDC/IE load. |
| **β-Carotene (whole-food)** | V3 (retinoid/differentiation) | Provitamin-A → retinal/RA via BCO1 | Dietary-Observational (whole food) | None direct | Carrots, sweet potato, leafy greens | **See Conflicts — ATBC/CARET harm is for ISOLATED high-dose supplements in smokers; carrot juice ≈20.5 mg β-carotene/300 mL approaches that dose (PMC3259297). Smoking status unknown.** No isolated β-carotene supplement should be added. |
| **Dietary nitrate** | host-biology (ADR-0005), **not a V-mechanism** | NO-mediated vasodilation/bioenergetics — reaches its own target reliably, but that target is not a V1/V2/V3/V4 mechanism | Dietary-Observational + Mechanistic | None direct | Beetroot, beet greens, arugula, spinach | None found; **category error if scored as a vector** — routed to host-biology layer. |
| **Fermented foods / dietary fiber** | V4 microbiome | ↑ microbiome alpha-diversity, ↓19 inflammatory markers incl. IL-6 (Wastyk 2021, PMID 34256014); fiber → SCFA; ≈30% lower progression/death per +5 g/day fiber on ICB in melanoma (Spencer 2021, PMID 34941392) | Clinical-Trial (healthy adults / melanoma-CPI) | None direct | Yogurt, kefir, sauerkraut, kimchi; legumes, whole grains | **Live-culture infection risk in the neutropenic ifosfamide window** (timing, not PK). **Juicing strips the fiber substrate — a missed opportunity, not a harm.** |

### Supplements (only where deficiency-correction has a clear rationale; safety established)

| Compound | Vector(s) | Mechanism | Tier | CIC-DUX4 direct? | Published-dose-range note (with citation) | SOC contraindications |
|---|---|---|---|---|---|---|
| **Vitamin D3** | V3, V4 (NK) | VDR/RXR target-gene differentiation (p21/p27, SNAI2/EMT-suppression; osteosarcoma PMC10203545); NK cytotoxic-receptor support | Mechanistic / Dietary-Observational | None direct | **VITAL (PMID 30415629): primary cancer-incidence endpoint NULL** in non-deficiency-selected population. **Correct deficiency ≠ supplement-further.** Patient's 25-OH-D unknown. | VDR-mediated CYP3A4 induction is *intestinal*/low-magnitude (PMC9262690); IV ifosfamide limits relevance. Hypercalcemia + ifosfamide nephrotoxicity is a monitoring note. |
| **Magnesium (status correction)** | V2 / SOC tolerability | Cofactor for DNA pol & repair enzymes; **ifosfamide independently causes renal Mg wasting** (Fanconi-like tubulopathy) | Mechanistic / Clinical (ifosfamide hypomagnesemia) | None direct | Framed as monitoring/correction-of-measured-deficiency — the cleanest "do this" entry, **independent of any V2 efficacy claim** (PMC8971049, PMC6433442). | Direct chemo-tolerability rationale; no adverse interaction at correction doses. |
| **Folate / B12 / B6 (status correction)** | V2, V1 | One-carbon/nucleotide-pool cofactors; deficiency → uracil misincorporation → DSBs (Blount 1997, PMID 9096386) | Mechanistic (deficiency-correction) | None direct | **UNRESOLVED tension** (see Conflicts): in *active disease*, excess folate may feed proliferating tumour (colorectal "folate paradox," Directness P3–P4). Status unmeasured. | High-dose folic acid in active disease = "not a do." |
| **Liposomal Vitamin C** | V2 (primary) | Antioxidant at oral/liposomal plasma (~tens–low-hundreds µM); pro-oxidant only at IV-pharmacologic (≥1 mM) | Mechanistic (oral/liposomal); Clinical-Trial (IV route = **different intervention**) | None direct | Oral/liposomal ceiling ~0.2–0.25 mM is **~100–150× below** IV pharmacologic range (NCT03508726 STS IV-ascorbate trial). "Liposomal oral = IV" is **not supported**. | **See Conflicts + SOC map — ROS-axis chemo-blunting (Heaney 2008, PMID 18829561) + Sayin-2014-by-analogy metastasis concern. Patient's actual plasma level unknown — the single biggest uncertainty in the V2 headline.** |
| **Selenium** | V1, V2 | Selenoprotein/thioredoxin-reductase apoptosis-threshold modulation | Preclinical + Dietary-Observational | None direct | **SELECT (PMID 19066370): NULL, possible-harm.** Brazil nuts 1–2/day meet RDA; UL 400 µg/day, selenosis. | High-dose selenium **not recommended**. |
| **Zinc** | V1, V2, V4 | Ku70/Ku80 + p53 zinc-finger DNA-repair cofactor; NK maturation | Mechanistic (deficiency-correction) | None direct | UL 40 mg/day; **high-dose displaces copper** → cytopenias that confound chemo-tox monitoring. | Deficiency-correction only; not in current regimen. |

### Lifestyle (brief)
- **Physical activity / prehabilitation** (resistance exercise + protein-energy nutrition): preserve
  skeletal-muscle reserve → protect delivered ifosfamide dose-intensity (sarcopenia → ifosfamide toxicity,
  PMID 39921759). Conditions SOC tolerability, **not** tumour-directed. [Clinical-Trial, other cancers] F1.
- **Vitamin D via sun / fatty fish** — deficiency-correction framing only (see table).
- **Fiber from whole foods, not juice** — feeds SCFA-producing taxa (V4 microbiome). [Clinical-observational, melanoma]
- **Sleep/circadian, autonomic/stress (PNEI):** Mechanistic only in sarcoma; carry as host-context modifiers
  (see Host-Biology section). The patient's *perceived-control/placebo* benefit from self-administering the
  regimen is a real host-biology effect on symptom/tolerability endpoints — **not** an antitumour mechanism.

---

## Clinical / Experimental Track (For Oncologist Discussion Only)

> **Clinical / Experimental — not naturally achievable; for awareness only.** F-band + attrition-reason
> (R0–R5) annotated; **perishable — re-verify live.** Directness rung (P0–P4, ADR-0014) noted where ranking
> turns on transferred evidence. FDA *and* EMA status cited for Established-tier entries where they differ.

| Intervention | Vector(s) | Mechanism (molecular) | Tier | FDA status | EMA status | Trial IDs | F-band / R-reason / Directness | Notes |
|---|---|---|---|---|---|---|---|---|
| **CDK4/6 inhibitors** (palbociclib, ribociclib, abemaciclib) | V1, V3 | CDK4 (+cyclin D) phosphorylates Rb → E2F/S-phase; re-imposes the CDKN2A/p16 G1 brake most CIC-DUX4 tumours lost | Established (breast) / Clinical-Trial (sarcoma) / Preclinical-Cell (CDK4 selective dependency) | Approved HR+ breast (2015–2017) | Approved HR+ breast (2016–2018) | GEIS palbociclib ph2 PMC10598203 (CDK4-selected, 6-mo PFS 29%); abemaciclib DDLPS | **F1 / R-n/a / P1 (fusion round-cell)** | **Fusion-agnostic, fully driver-robust (D1–D5).** Cytostatic; CCNE1 bypass; additive myelosuppression w/ ifosfamide. Safest entry to discuss regardless of driver. |
| **Class-I HDAC inhibitors** (vorinostat, romidepsin, panobinostat, belinostat) | V3→V4 | H3K27ac/H4ac opens APM loci (TAP1/2, PSMB8/9, HLA-A/B/C, B2M); ERV reactivation → viral-mimicry/type-I-IFN/STAT1 → MHC-I↑ | Clinical-Trial (mechanism); FDA-approved class for **CTCL** (different indication) | Vorinostat **not EU-approved** (application withdrawn) `[VERIFY EU]`; romidepsin EU status differs `[VERIFY]` | PEMDAC precedent NCT02697630 (uveal melanoma, PMID 34376667) | **F1 (repurposable, US) / R-n/a / P3 (PEMDAC) → P1 mechanism** | **Fusion-agnostic.** Anchors the MHC-I bridge now that EZH2i is off-table. **No sarcoma-specific HDACi+CPI trial exists.** Toxicity overlap w/ ifosfamide. |
| **DNMT inhibitors** (azacitidine, decitabine, guadecitabine) | V3→V4 | Reverse APM/HLA/TAP promoter hypermethylation; ERV → cGAS-STING/IFN → STAT1 → MHC-I↑ | Established MDS/AML | Approved MDS/AML | Solid-tumour immune-priming trials exist | **F1 / R-n/a / P3** | **Fusion-agnostic.** Solid-tumour efficacy unproven; myelosuppression. |
| **BET inhibitors** (OTX015/birabresib, BMS-986158, AZD5153, ZEN-3694) | V1, V3, (V4 weak) | BRD4 reads H3K27ac at CIC-DUX4 super-enhancers (ETV4/5) → BETi collapses output. **DepMap: BRD4 essential pan-cancer, NOT CIC-DUX4-selective** — "addiction" overstates selectivity | Preclinical-Cell / Clinical-Trial / **Theoretical** for any CIC-DUX4-*selective* claim | **No BETi approved anywhere**; class contracted (BMS dropped ezobresib; AbbVie exited; birabresib GBM terminated; molibresib halted) | None approved; **ZEN-3694** Fast Track/Orphan (NUT carcinoma) the main survivor; BMS-986158 NCT02419417 (PMID 36077617), pediatric NCT03936465 (incl. Ewing) | **F3–F4 / R5 commercial (class contraction) — biology-silent / P1** | **Fusion-agnostic, driver-robust.** Strongest *mechanism*, among weakest *access* — pursue biology, expect a trial-stage asset or degrader concept. |
| **dCBP-1 (p300/CBP degrader)** | V3 | CIC-DUX4 needs p300/CBP for H3K27ac at target loci; degrading p300/CBP silences fusion output — **the one degrader entry with DIRECT CIC-DUX4 cell-line data** (PMC8511258) | Preclinical-Cell | n/a (preclinical) | n/a | — | **F5 / R0 never-built / P0 (direct)** | **Partially driver-contingent** (strongest D1/D2). Technology watch-item. |
| **EZH2/EZH1 inhibitors** (tazemetostat; valemetostat) | V3→V4 | PRC2/H3K27me3 removal restores APM in PRC2-dependent tumours | Doubly caveated | **Tazemetostat WITHDRAWN WORLDWIDE 2026-03-09** (epithelioid sarcoma 2020-01-23 + FL); **never EMA-approved** | Never EMA-approved | Valemetostat NCT07303387 (SWI/SNF-altered); FDA-approved 2022 ATLL (heme) | **Tazemetostat F5 / R4 regulatory-safety (NOT R1) ; valemetostat F2 / P3** | **Fusion-agnostic mechanism, but premise contested (p300/CBP, not PRC2 — Bakaric 2024) AND access closed.** Valemetostat inherits an elevated secondary-malignancy index-of-suspicion (broader PRC2 blockade) — open safety question, not reassurance. **Do NOT present as an actionable bridge.** |
| **MCL1 inhibitors / BH3-mimetics** (S63845 tool; S64315/MIK665 clinical) | V3 | DUX4 transactivation domain transactivates *MCL1* → MCL1i "re-arms" the DUX4 apoptosis program (highest-tier DIRECT CIC-DUX4 finding) | Preclinical-Cell (1–10 nM IC50) + Preclinical-Animal (S64315 → regression in CIC::DUX4 xenograft) | n/a (clinical-stage, other indications) | n/a | PMID 40841513, PMID 40841360 (2025) | **F2/F3 / R-n/a / P0 (direct) — cardiac-tox caution** | **FUSION-CONFIRMED ONLY — DRIVER-CONTINGENT, HOLD until driver resolved (D1 only; D2 0.5 if DUX4-family).** Highest ceiling, highest contingency. |
| **Pembrolizumab / nivolumab ± ipilimumab; nivolumab+relatlimab** | V4 | PD-1/PD-L1/CTLA-4/LAG-3 checkpoint relief | Established (many indications) / Clinical-Trial (sarcoma) | Approved broadly | Approved broadly | SARC028 NCT02301039 (PMID 28988646, primary endpoint NOT met overall); Alliance A091401 NCT02500797 (nivo 5% / nivo+ipi 16% ORR); CIC::DUX4 case PMID 40128305 `[VERIFY]` | **F1 / R-n/a / P3 (CPI in sarcoma)** | **Fusion-agnostic. NEGATIVE-leaning monotherapy prior** (low-TMB). Best paired with V3 MHC-I priming. |
| **IL-15 superagonist N-803 (nogapendekin alfa, Anktiva)** | V4 NK | IL-15 drives post-lymphodepletion NK/CD8 reconstitution without Treg expansion (unlike IL-2) | Established (NMIBC) / Clinical-Trial (solid tumour) | **FDA approved 2024-04-22** (NMIBC+BCG, CIS) | EMA CHMP positive opinion (conditional MA) `[VERIFY]` | QUILT-3.032; NSCLC ph3 (tislelizumab combo) `[VERIFY]` | **F1 (US, distant indication) / R-n/a / P3** | **Fusion-agnostic.** Approved route is intravesical; systemic-solid-tumour is trial-stage. Plausible timed to post-ifosfamide NK window. |
| **NTX1088 (anti-PVR/CD155)** | V4 NK + checkpoint | Removes shared TIGIT/CD96/PVRIG ligand PVR/CD155, restores surface DNAM-1 on T & NK cells — distinct from FAILED receptor-level anti-TIGIT (SKYSCRAPER-01/-02) | Clinical-Trial (ph1; MoA signal April 2026) | Investigational | Investigational | NCT05378425 (recruiting Nov 2024) `[VERIFY]` | **F3 / R-n/a / Theoretical for CIC-DUX4** | **Fusion-agnostic.** Requires the tumour to express PVR/CD155 (unmeasured). |
| **Fusion-agnostic personalized neoantigen mRNA vaccine** (intismeran autogene/mRNA-4157; autogene cevumeran/BNT122) | V4 | WES/RNA-seq-discovered somatic neoantigens, independent of fusion confirmation | Clinical-Trial (melanoma/pancreatic) / Mechanistic (this tumour) | Investigational (ph3) | Investigational | KEYNOTE-942 5-yr (Jan 2026, RFS HR 0.510); NCT05933577; BNT122 NCT04486378 (CRC futility boundary crossed Q3-2025 `[VERIFY]`) | **F2 / R-n/a / P3** | **Fusion-agnostic** (the only neoantigen-vaccine entry that is). Low-TMB tempers expectations; needs tissue; ~6–9 wk manufacturing **incompatible with the urgent ifosfamide course**; anti-PEG flag. |
| **CIC-DUX4 junction-specific neoantigen vaccine / TCR-T / junction ASO / fusion CAR** | V3/V4 | Junction peptide / junction mRNA as fusion-specific target | Theoretical | n/a | n/a | None | **F5 / R0 never-built** | **FUSION-CONFIRMED ONLY — POSSIBLY INAPPLICABLE to this patient; DRIVER-CONTINGENT, HOLD.** CIC-DUX4 protein is intracellular (no CAR target); junction nucleotide sequence varies across patients. |
| **Regorafenib** | (anti-angiogenic, off-driver) | Multikinase/VEGFR inhibition | Clinical-Trial (CIC-rearranged cohort named) | Approved (other sarcoma/GIST/CRC indications) | Approved (other indications) | **REGOBONE Cohort E / NCT02389244 — `ACTIVE_NOT_RECRUITING`, results NOT posted (verified 2026-06-13)** | **F2/F3 / results-pending (NOT R1/R2 — not negative) / P2** | **Fusion-agnostic.** One of very few trials to *name* this entity. Results-pending ≠ negative. |
| **Regional hyperthermia + chemo** (modality M7) | V2↔V4 | Heat increases chemo/RT-induced DNA damage + impairs repair (V2) AND releases HSP/HMGB1/DAMPs → immune priming (V4) | Clinical-Trial (high-risk STS, **positive ph3**) | n/a (device/modality) | n/a | EORTC 62961-ESHO 95 (Issels, *Lancet Oncol* 2010; *JAMA Oncol* 2018 OS) NCT00003052 `[PMID VERIFY]` | **F2–F3 (specialised centres) / P2 (sarcoma broadly)** | **Fusion-agnostic.** The catalog's headline **modality gap** — a modality with a positive randomised STS trial that had zero prior representation. CIC-DUX4 is often deep/visceral, bounding access. |

---

## Host-Biology & Treatment-Response Modifiers

> From `host-biology-modifier-layer.md` (ADR-0005). A **cross-cutting conditioning layer, not a fifth
> vector** — it sets the *gain* on V4 immune competence and on SOC tolerability, weighted via the three
> axes (Directness does the down-weighting; most entries are P2–P3). **All entries fusion-agnostic.**

- **Three host factors are Clinical-grade and measurable from routine labs + the staging CT** (cheap
  Tier-A data) for this patient: **systemic inflammation (NLR / mGPS)**, **sarcopenia / L3 skeletal-muscle
  index**, and **nutritional status (albumin)**. Each is prognostic in STS (NLR/mGPS PMID 34969280;
  sarcopenia → ifosfamide toxicity in an adria+ifosfamide cohort PMID 39921759, near-exact regimen → P1-in-practice).
  **Prognostic ≠ targetable** — carry as stratifiers/tolerability levers, not targets.
- **Gut microbiome / SCFA:** conditions V4 / future CPI responsiveness (Routy/Gopalakrishnan/Davar,
  melanoma/NSCLC, P3) — **directionally double-edged** (systemic butyrate → Treg can be *pro*-tolerogenic;
  broad commercial probiotics *reduced* anti-PD-1 response, Spencer 2021). "Gut health = good" is not safe to assume.
- **Autonomic/β-adrenergic, sleep/circadian, psychological stress/PNEI (CTRA):** real neuroimmune mechanisms
  (Cole PMID 31592179) but human cancer-*survival* effects weak/unproven — Mechanistic/Preclinical; forward-lane.
- **Perioperative immune conditioning** (β-blocker + COX-2 around metastasectomy): improved metastasis
  *biomarkers* in breast/CRC ph2 RCTs (PMID 28490464); **survival benefit not established, never tested in
  sarcoma; NSAID + ifosfamide raises nephrotoxicity** — clinician-run trial context only, never self-administered.
- **Placebo/nocebo:** affects symptom/tolerability/adherence endpoints **only** — honest boundary, **not**
  an antitumour mechanism. Relevant to why the patient may *feel* the self-regimen helps.

---

## mRNA COVID-19 Vaccine — Research Findings

**Net finding: NO documented relevant persistent effect of BNT162b2 on this patient's current biology (2+
years post standard primary series).** Stated explicitly — a null finding is a complete finding.

- **Immune modulation:** acute innate (TLR4/NLRP3 → IL-6/TNF-α/IL-1β + type-I IFN) resolves ~72 h; T-cell
  memory waned and spike-specific (not tumour-specific); NK activation (NKG2D↑) resolved ~30 days (Kared,
  PMID 35087044 `[VERIFY]`). [Established acute / Low at 2+ years]
- **Inflammatory context:** no persistent cytokine/NF-κB elevation. The patient's *dominant* inflammatory
  contexts are **post-WLI fibrotic/TGF-β, imminent ifosfamide (acrolein), and the relapse niche** — the
  vaccine contributes to none.
- **Genomic stability / oncogenesis:** no peer-reviewed evidence of integration, chromosomal instability,
  or a sarcoma incidence signal (Barda PMID 34432976). For CIC-rearranged sarcoma specifically (~1–2/million/yr),
  pharmacovigilance is **statistically underpowered** — absence of signal reflects the detection floor.
- **Affected vectors:** **V2** — translocation-risk framework unchanged. **V4** — checkpoint/NK/Nectin logic
  unconfounded; **one actionable carry-forward: the anti-PEG IgG/IgM flag** (Kozma PMID 35853896 `[VERIFY]`)
  — if a *future* LNP-mRNA neoantigen vaccine (fusion-agnostic track) is ever considered, pre-treatment
  anti-PEG titre is a reasonable PK-stratification covariate (ABC phenomenon, Ishida PMID 16797763). Design-level only.

---

## Metastatic Disease Considerations

> From the Metastatic Disease Specialist (`metastatic-disease-considerations-v3.md`, run this session).
> The May-2026 clone is a **selected survivor** of VDC/IE + WLI + 1 year of surveillance.

**Per-vector applicability in metastatic disease:**
- **V1 (Rate Limiting) — APPLIES, not strengthened.** Targets are metastasis- and fusion-agnostic; a
  sub-threshold dietary throttle is *even less* likely to bite a treatment-hardened survivor clone. Its
  decision-relevant content (the ifosfamide CYP3A4 screen) is metastasis-agnostic host pharmacology.
- **V2 (Compiler Protection) — DOES NOT APPLY as prevention; INVERTS into an active-disease harm-direction
  flag.** This is the vector metastasis changes most: the Sayin-2014 antioxidant→metastasis signal goes from
  academic (in NED) to **load-bearing in an actively-seeding oligometastatic window**. Doxorubicin's ROS/ICD
  is now retrospective; the *active* ROS-relevant agent (ifosfamide) is less clearly ROS-dependent (its
  dominant mechanism is DNA alkylation) — so the *active* antioxidant concern is **metastatic seeding**, not
  chemo-blunting.
- **V3 (Hot Patching) — APPLIES (fusion-agnostic entries).** Clonal selection adds a *second* contingency on
  top of the already-on-HOLD MCL1/dCBP-1 lines: the survivor clone may have altered that dependency. Re-weights
  diagnostic sequencing to "resolve driver on archived P1 → only then fresh P2 *relapse* tissue for contingent lines."
- **V4 (Immune Watchdog) — APPLIES; rationale most strengthened, but selected-survivor logic cuts hardest
  here.** The oligometastatic, single-cluster setting is surveillance-favourable, and the post-ifosfamide
  NK-reconstitution window is an active opportunity. Immunoediting predicts the relapse clone is MHC-I-low —
  which could make it a *better* NK missing-self target **or** "doubly cold." The relapse-tissue immune
  phenotype is the decisive unknown, answerable **only on fresh P2 relapse tissue** (the archived primary
  predates the selection event).

**mRNA findings — metastatic relevance:** the only systemic carry-forward is the post-WLI cGAS-STING
priming question (whether the irradiated lung niche retains an immunogenic-priming advantage at the relapse
site) — unestablished at this timepoint.

**Single most important metastatic-specific insight:** **fresh relapse tissue is where P2-provenance
decisively beats P1-archived** — the archived 2025 primary cannot report the relapse clone's escape
phenotype, and the **MHC-I-low-but-NK-ligand-retained vs. doubly-cold fork is the highest-value unmeasured
question.**

**Honest counterweight (carried from the specialist's red-team):** this tumour was **metastatic from
diagnosis** (12 lung mets at dx), so the relapse may be **outgrowth of a pre-existing disseminated clone**
rather than fresh immune-editing — which genuinely weakens the immunoediting premise. The burden/timing-based
V4 framings survive that flip; the "better-NK-substrate" claim is tagged **clone-divergence-contingent.**

---

## Forward Hypotheses (Not Yet in the Literature)

> Curated and ranked across all four vectors, the metastatic specialist, and the standing layers
> (tumorigenesis build-recipe ADR-0007; VoI/diagnostic "what to learn next" ADR-0015/0001/0008; host-biology
> ADR-0005). Ranked by **biological plausibility × research feasibility**. The two-lane rule applies —
> a Concept-only/F5 idea can still rank at the top here. **None of these is a recommendation.**

**FH-1 (highest practical leverage). Resolve the driver first — nuclear DUX4 IHC on archived P1 tissue —
to license-or-exclude the entire contingent option set.** *Statement:* a single cheap archived-tissue stain
(DUX4 IHC; Macedo 2025, DOI 10.1111/his.15341) resolves the DUX4-transactivation-domain question that gates
the MCL1 "re-arm" line and all junction-specific approaches. *Mechanistic basis:* the MCL1 dependency and
the junction targets exist only under D1 (and a rare DUX4-family D2); two independent decision models (Sim 8
EVSI; protocol driver-uncertainty) agree this is the highest-value next action. *Test:* DUX4 IHC on the
Jan-2025 resection block (P1, near-zero risk); long-read WGS+RNA-seq next if ambiguous/positive and partner
identity matters; methylation array collapses the phenocopy (D4) question. *Why not done:* an n-of-1
diagnostic-stewardship question, not a registered trial — addressable now. **Fusion-resolving; the gate for
the fusion-confirmed-only lines.**

**FH-2 (highest immune leverage). Paired archived-primary-vs-fresh-relapse immune phenotyping to resolve
the "MHC-I-low-NK-exposed vs. doubly-cold" fork.** *Statement:* the selected relapse clone is plausibly
MHC-I-low-but-NK-stress-ligand-retained → the post-ifosfamide NK-reconstitution window is the best-timed
NK-surveillance opportunity. *Mechanistic basis:* immunoediting under VDC/IE+WLI+1-yr surveillance selects
for MHC-I-low escape; NK missing-self exploits exactly that — *if* MICA/MICB/ULBP/PVR are co-expressed.
VoI ranks nectin CD155/CD112 (#1) and HLA-E (#2) as the top unmeasured biomarkers. *Test:* paired HLA-A/B/C
+ B2M + TAP1/2 + MICA/MICB/ULBP + PVR/CD155 + HLA-E + CD8/FoxP3 phenotyping on archived primary (T0/P1) vs
fresh relapse (T1/P2). *Why not done:* the panel exists; no one has framed primary-vs-relapse CIC-DUX4 immune
divergence as the decision. **Fusion-agnostic.** *Caveat:* tagged **clone-divergence-contingent** (the
metastatic-from-dx counterweight) and **lacks a self-falsifying gate** (asymmetry vs FH-3).

**FH-3 (self-falsifying by design). Post-ifosfamide, biomarker-GATED HDACi/DNMTi → checkpoint sequence in
the lymphocyte-reconstitution window.** *Statement:* a short class-I HDACi or DNMTi course (F1 repurposable)
timed to the post-ifosfamide reconstitution window (IL-7/IL-15 homeostatic proliferation), with an
**on-treatment biopsy/ctDNA gate for MHC-I/APM transcript induction (TAP1/2, HLA-A/B/C, B2M) BEFORE
proceeding to anti-PD-1.** *Mechanistic basis:* HDACi/DNMTi restore APM via viral-mimicry/IFN (V3 ranks 1–2);
timing — not a novel agent — is the lever to improve an otherwise-modest CPI prior. *Test:* window-of-opportunity
ph1b; the MHC-I/APM gate is the falsifier — **no induction ⇒ do not proceed to CPI, and the result strengthens
FH-2's NK-first framing.** *Why not done:* the HDACi/DNMTi-anchored version is new (prior runs anchored to
now-withdrawn tazemetostat); most combination trials co-administer rather than sequence-and-confirm.
**Fusion-agnostic.**

**FH-4. BET inhibitor + MCL1 inhibitor as a two-"construction-debt" attack (DRIVER-CONTINGENT).** *Statement:*
in driver-confirmed CIC::DUX4 cells, BETi (collapse the p300/BRD4 super-enhancer state) + MCL1i (remove the
DUX4-forced anti-apoptotic buffer) hit two non-redundant build-recipe debts (Steps 5 and 3) at once. *Mechanistic
basis:* PMID 40841513 already found BET inhibitors as top synergy hits with S64315. *Test:* CIC::DUX4
tumoroids/xenografts, BETi vs MCL1i vs combination at sub-maximal doses, long-term regrowth + RNA-seq to test
whether BETi *reduces* MCL1 transactivation (coupling). *Falsifier:* no MCL1 reduction and no durable benefit
over the better single agent ⇒ acute/additive only. **Fusion-confirmed only — HOLD; gated by FH-1.**

**FH-5. Composite host-inflammatory/reserve index (mGPS + NLR + L3-SMI) as a pre-treatment stratifier for
whether full-dose ifosfamide and any V4 immune approach are worth attempting.** *Mechanistic basis:* high
systemic inflammation + sarcopenia both predict immunosuppression and poor chemo tolerance; in an already-cold
tumour, the high-inflammation/low-reserve host is where checkpoint approaches are least likely to yield and
dose reductions most likely. *Test:* retrospective→prospective correlation of baseline mGPS/NLR/SMI with
delivered ifosfamide dose-intensity, toxicity, and any CPI response, pooled across sarcoma histotypes (CIC too
rare alone). **All inputs are routine bloods + staging CT — zero new assays.** [Clinical (prognostic), F1]
**Fusion-agnostic.**

**FH-6 (modality forward space). Regional hyperthermia as an ICD/DAMP "make-the-cold-tumour-hot" V2↔V4 bridge.**
*Statement:* does regional hyperthermia (positive ph3 in high-risk STS) convert the cold CIC-DUX4 microenvironment
toward immune visibility via HSP/HMGB1/DAMP release, beyond pure chemo-sensitisation? *Falsifier:* if the STS
benefit is purely chemo-sensitisation with no measurable DAMP/immune shift, the V4 arm is wrong and it reduces
to a V2 sensitiser. *Why surfaced:* M7 was the catalog's headline modality gap — a modality with a positive
randomised sarcoma trial and zero prior representation. [Clinical-Trial in STS broadly / P2] **Fusion-agnostic.**
*(Companion forward space, lower priority: oncolytic virus / in-situ ICD as an "artificial danger-signal
generator" — `Theoretical` for CIC-DUX4 since the nearest Ewing/round-cell data show LOW OV susceptibility and
no CIC-DUX4 OV data exist; gating experiment = a CIC-DUX4 tropism screen, ADR-0019.)*

**FH-7 (technology watch). Repurpose the EWSR1::FLI1 "transcriptional rewiring" (EB-TCIP, 2025) chemical-biology
template to CIC::DUX4.** Both are "undruggable" TF fusions whose oncogenicity is transcriptional output, not an
enzymatic site; a chemically-induced-proximity bivalent could recruit the fusion to a pro-apoptotic locus.
[Preclinical concept / F5] **Fusion-confirmed only — HOLD; technology watch-item, not a near-term candidate.**

---

## Cross-Vector Synergies

Ranked by total evidence weight (not number of vectors touched):

1. **V3 → V4 MHC-I bridge (the catalog's central cross-vector dependency).** HDACi/DNMTi restore MHC-I/APM →
   enables the V4 T-cell/checkpoint arm. Now anchored on **HDACi/DNMTi (F1 repurposable)** after the tazemetostat
   withdrawal removed EZH2i. [Clinical-Trial component mechanisms] **Verified consumed by V4 this run.**
2. **The NK-vs-MHC-I-priming SEQUENCING tension (the most important cross-vector finding this run).** Restoring
   MHC-I helps T-cells but *removes* the NK missing-self signal (re-arms KIR/NKG2A) — and HLA-E may co-induce,
   *closing* the NK window rather than just shifting it. Resolution: **NK-directed measures earlier (native
   MHC-I-low state) → epigenetic MHC-I restoration later (switch the dominant effector arm).** [Mechanistic;
   Sim 6 VoI supports NK-axis primacy]
3. **V1 ↔ V3 downstream CDK4/CCND1 overlap.** V1's dietary cell-cycle friction (fisetin/genistein, weak) and
   V3's clinical CDK4/6i hit the *same* target — same axis, different track, different magnitude.
4. **V1 ↔ V2 shared antioxidant/cofactor compounds** (quercetin, omega-3, selenium, zinc): reducing
   transcriptional load (V1) reduces Topo II DSBs at active loci (V2). **But** for *this* patient the V1↔V2
   overlap is dominated by the antioxidant-vs-chemo conflict, not a benefit.
5. **BETi + MCL1i synergy** (FH-4) and **dCBP-1 (p300) × BETi** (same super-enhancer axis: p300 writes
   H3K27ac, BRD4 reads it) — both **driver-contingent** via the MCL1/dCBP-1 entries.

---

## Conflicts and Open Questions

Surfaced explicitly — not papered over (orchestrator red-team pass, ADR-0017):

- **Antioxidants vs. ROS-dependent chemo (genuine, unresolved).** V2 surfaces liposomal vitamin C; SOC
  doxorubicin (given) and etoposide use ROS, and the patient is starting ifosfamide. Oral/liposomal vitamin C
  plausibly sits in the Heaney-2008 chemo-*blunting* plasma range, **not** the IV pro-oxidant range — but the
  patient's actual plasma level is **unmeasured** (assumption-contingent; if ≥1 mM the directionality flips to
  potentiation). **Flagged for oncology discussion; not a contraindication this catalog can declare.**
- **Antioxidants vs. metastasis (sharpened by the metastatic context).** Sayin-2014 (NAC/vitamin E →
  accelerated metastasis in mouse melanoma/Kras-lung; Le Gal 2015 follow-up) is **Mechanistic-by-analogy** to
  liposomal vitamin C (different compound/route) — but the patient has *active oligometastatic disease*, so the
  concern is load-bearing, not academic. Carry the flag.
- **β-carotene.** V3 surfaces retinoid/differentiation signalling; V2 flags ATBC/CARET harm. Whole-food carrot
  juice is **not** the isolated-supplement harm signal — but a dose-equivalence analysis (≈20.5 mg/300 mL ≈ the
  20 mg ATBC dose) means the "whole food is automatically safe" framing is **not** fully supported, and
  **smoking status is unknown** (decision-relevant). No isolated β-carotene supplement should be added.
- **NAC.** Not in the regimen; common OTC "antioxidant" — should **not** be added during active malignancy
  (Sayin 2014). Carry the flag.
- **High-dose vitamin E / selenium.** SELECT harm signal; selenium's narrow window. Carry.
- **Probiotics during therapy.** V4 microbiome surfaces fiber benefit, but **broad commercial probiotics
  *reduced* anti-PD-1 response** (Spencer 2021) + infection risk in the neutropenic ifosfamide window — argues
  against "more probiotics = better."
- **Folate-excess-in-active-disease (unresolved by design).** Deficiency-correction prevents uracil-misincorporation
  DSBs in healthy progenitors (V2); excess folate may feed proliferating tumour (colorectal paradox, P3–P4).
  Resolving it needs measured folate status or tumour MTHFD2 expression (V2 FH-1). Left open.
- **The MHC-I-bridge ceiling-effect risk (red-team, load-bearing).** The whole V3→V4 bridge assumes APM loci are
  baseline-*repressed* in CIC-DUX4 (something to restore). The same p300/CBP-activator finding that downgraded
  EZH2i could mean APM loci are **not** repressed (nothing to restore). No study addresses this. If true, the
  vector's centre of gravity shifts to the NK/Nectin arm. **Assumption-contingent.**
- **NK-first lacks a self-falsifying gate.** FH-3 (checkpoint arm) has a built-in MHC-I/APM biomarker gate;
  FH-2 (NK arm) does not yet — its "doubly cold?" assumption is unmeasured. A genuine asymmetry the orchestrator
  flags.
- **Adjustments made to sub-agent claims:** none required removal; tier/contingency tags were applied (MCL1,
  dCBP-1, junction lines marked driver-contingent; tazemetostat moved to F5/R4; BETi "addiction" reframed as
  pan-essential not CIC-DUX4-selective per DepMap). All `[VERIFY]` tags carried from the vector leads' live
  2026-06-14 verification are preserved.

---

## Standard-of-Care Interaction Map

> SOC = VDC/IE (vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide) + surgery + radiation.
> **Imminent: high-dose ifosfamide.** Every entry: *must be reviewed by the patient's oncologist/pharmacist
> before any change.* Screened against CYP3A4 / CYP2B6 / CYP2C9 / P-gp / ROS-axis per `sarcoma-chemo-interactions`.

**THE CONVERGENT SIGNAL (highest priority, surfaced for oncologist/pharmacist review — research/awareness,
NOT a stop/start instruction):** the patient's regimen contains **THREE independent CYP3A4-modulating
compounds — piperine, curcumin, thymoquinone — converging on the bioactivation of ifosfamide, a CYP3A4/CYP2B6
prodrug.** Because CYP3A4 sits at the **branch point** between activation (→ ifosfamide mustard, efficacy) and
N-dechloroethylation (→ chloroacetaldehyde, neuro/nephrotoxicity), the **net direction is not predictable from
first principles**, and the burden of three concurrent modulators is additive in principle even if each is
individually weak. A **second, independent** axis: piperine + curcumin are **P-gp inhibitors**, and vincristine
is a P-gp substrate with a narrow therapeutic index (severe-neurotoxicity case reports exist for vincristine +
strong CYP3A4/P-gp inhibitors — itraconazole PMID 16012330, posaconazole PMC6213623 — far more potent than
these dietary compounds; equivalence is **not** claimed, direction is the same: toward *more* exposure).

| Compound | CYP3A4 | CYP2C9 | P-gp | ROS-axis | Net flag | Source |
|---|---|---|---|---|---|---|
| **Piperine** | Inhibitor in vitro (Ki≈36–77 µM); 1 human P-gp datapoint (+68% fexofenadine AUC, 20 mg/day `[VERIFY]`) | — | Inhibitor (IC50 15.5 µM) | — | **Concerning — flag for pharmacist review vs ifosfamide branch-point + vincristine** | Bhardwaj 2002 PMID 12130727 |
| **Curcumin** | In-vitro inhibitor (IC50≈2.7 µM `[VERIFY]`); a reported in-vivo *activation* finding points opposite — **net direction unresolved** | — | Inhibitor (PMID 12363453); alters etoposide/tamoxifen PK in rat (PMID 21506134, 22512082) | NF-κB only (not redox-scavenging) | **Concerning — direction unresolved; flag** | as cited |
| **Thymoquinone (black cumin seed oil)** | In-vitro inhibitor (IC50≈25 µM); whole *Nigella* extract shows time-dependent CYP3A4/2C19/2C9 inhibition `[VERIFY]` | Most sensitive (IC50≈0.5 µM) | Conflicting in literature — unresolved | Nrf2/antioxidant | **Concerning — third independent CYP input; gut-wall/first-pass effect possible even at near-zero serum (PMC10671713)** | as cited |
| **Liposomal Vitamin C** | — | — | — | **Antioxidant range (oral/liposomal ~0.2–0.25 mM) → potential ROS-dependent chemo-blunting (doxorubicin/etoposide; ifosfamide less ROS-dependent) + Sayin-by-analogy metastasis concern** | **Caution; flag — magnitude depends on unmeasured plasma level** | Heaney 2008 PMID 18829561; Sayin 2014 PMID 25214635; Lawenda 2008 PMID 18612170 |
| **Quercetin (supplement bolus)** | Inhibitor (IC50≈1.97 µM) | — | Modulator (↑etoposide/doxorubicin bioavailability, rat PK PMID 21544726, 19414395) | — | **Flag for supplement-bolus form** (apple-juice glycoside far weaker) | as cited |
| **Vitamin D3** | Intestinal CYP3A4 induction, low-magnitude (PMC9262690) | — | — | — | **Low concern** (IV ifosfamide limits intestinal first-pass relevance); hypercalcemia + nephrotoxicity is a *monitoring* note | PMC9262690 |
| **Honey** | Source-dependent, "cannot be generalized" (Igbinoba 2016) | — | — | — | **Low concern; additive consideration only** | Igbinoba 2016 |
| **EGCG** | Modulator at higher conc. | — | Modulator | — | **Independent hepatotoxicity signal ≥800 mg/day `[VERIFY]`** given VDC/IE hepatic load | as cited |
| **Magnesium** | — | — | — | — | **Beneficial/neutral** — ifosfamide causes Mg wasting; correction has a tolerability rationale | PMC8971049, PMC6433442 |
| **NAD+ precursors** (not in regimen) | — | — | — | PARP1-mediated repair ↑ → **reduces chemosensitivity** in osteosarcoma cells (PMC7281559) | **DO NOT add during active chemo** | PMC7281559 |
| Apple/celery/ginger/carrot/beetroot juice constituents | class-effect, modest at dietary intake | — | class-effect | — | **Likely neutral at culinary intake** — not exhaustively screened (flagged "not screened," not "no interaction") | V1/V2 sub-agents |

---

## Patient's Actual Self-Administered Regimen — Assessment

> **helping / neutral / potentially concerning** — addressing interactions head-on. **Research/awareness
> framing, NOT a stop/start instruction.** Regimen: curcumin+piperine, liposomal vitamin C, black cumin
> seed oil/thymoquinone, vitamin D3, honey, and fresh juice of celery/ginger/carrot/broccoli/apple/beetroot.

| Component | Verdict | Reasoning (head-on) |
|---|---|---|
| **Curcumin + piperine** | **Potentially concerning (flag for pharmacist review)** | CYP3A4/P-gp modulation real but likely modest at OTC doses; converges with thymoquinone on the **ifosfamide branch-point** concern + a P-gp input on the **vincristine** axis. V1 BRD4 benefit almost certainly **below cell-line-active concentration**. **Shoba 1998 caveat:** the "~2000%/20× curcumin-bioavailability boost from piperine" comes from n=10, single-dose, with the curcumin-only control **below the assay LOD** — the *direction* is real and reproduced; the **specific multiplier is NOT a universal factor** and must not be cited as one. |
| **Black cumin seed oil / thymoquinone** | **Potentially concerning (flag for pharmacist review)** | Third independent CYP3A4 (+ CYP2C9, IC50≈0.5 µM) input; **gut-wall/first-pass effect possible even though free thymoquinone is non-detectable in serum** (PMC10671713) — so the concern does *not* depend on resolving its near-zero systemic PK. Whole-extract-vs-isolated CYP discrepancy unresolved `[VERIFY]`. **Most actionable epigenetic-claim overreach** — its better-supported activity is antioxidant/Nrf2, not "epidrug." |
| **Liposomal vitamin C** | **Neutral-to-potentially-concerning, low-to-moderate magnitude** | Antioxidant-range exposure (not IV pro-oxidant) → potential **ROS-dependent chemo-blunting** (doxorubicin/etoposide; ifosfamide less ROS-dependent) **+ Sayin-by-analogy metastatic-seeding** concern in this active oligometastatic window. **Magnitude hinges on the patient's unmeasured plasma ascorbate level** — the single biggest uncertainty in the V2 headline. |
| **Vitamin D3** | **Low concern; neutral-to-possibly-helpful IF correcting a deficiency** | Primarily a deficiency-correction question (25-OH-D unknown). VDR CYP3A4 induction is intestinal/low-magnitude; IV ifosfamide limits relevance. "Correct deficiency" ≠ "supplement further." |
| **Honey** | **Low concern** | No anticancer V-mechanism identified; CYP3A4 effect source-dependent and not generalizable. Simple-sugar load dominates (glycemic consideration during chemo). |
| **Carrot juice (β-carotene)** | **Likely neutral as whole food; flagged for V3 cross-ref** | Best-absorbed compound in the regimen, but mechanism is **V3 (retinoid), not V1**. ATBC/CARET harm is for **isolated supplements in smokers** — does not directly transfer to whole-food juice; **dose-equivalence caveat + unknown smoking status** noted. No isolated β-carotene supplement should be added. |
| **Beetroot juice (nitrate)** | **Neutral** | Reliably reaches its own NO target, but that is **not a V-mechanism** — routed to host-biology (vascular/oxygenation). |
| **Broccoli juice (sulforaphane)** | **Neutral — likely near-zero active delivery** | **Juicing very likely destroys myrosinase** (shear/heat; no ~40-min stand) and mature florets start from a lower glucoraphanin pool than sprouts → a **preparation finding, not an ingredient problem**. |
| **Apple (quercetin), celery (apigenin/luteolin), ginger (6-gingerol) juice** | **Likely neutral** | Mechanisms real in cell lines but **~30–1800× concentration mismatch** from juice forms; no acute chemo flag at culinary intake (apple/celery not exhaustively screened — flagged "not screened"). |

**Headline regimen verdict:** the regimen is **mostly neutral-to-benign at culinary doses with no proven
antitumour benefit at achievable exposures**, and its **single most important feature is a convergent,
multi-compound CYP3A4 signal (piperine + curcumin + thymoquinone) against an imminent CYP3A4-activated
ifosfamide prodrug whose net direction cannot be predicted** — plus a liposomal-vitamin-C ROS/metastasis
question. **Both belong in front of the oncologist/pharmacist before the ifosfamide course, framed as
awareness, not as an instruction to stop or continue anything.**

---

## Missing-Data, Value-of-Information & Diagnostic Strategy (What to Learn Next)

> From the VoI layer (ADR-0001/0011), the diagnostic information-gain layer (ADR-0015), and the
> driver-uncertainty model (ADR-0008). **Documentation of uncertainty — NOT a testing recommendation,
> NOT a diagnosis.**

**(1) Missing-data taxonomy + VoI ranking of unknown biomarkers.** The tumour's immune profile was **never
measured** — every immune marker in this catalog is currently an *assumption*. Ranked by decision-flip VoI
(Sim 6):

| Rank | Biomarker (assay) | VoI | What it changes | Provenance / timepoint |
|---|---|---|---|---|
| 1 | Nectin CD155/CD112 (IHC) | 0.625 | Loss makes non-cytotoxic selective clearance unreachable (gates BOTH T-cell & NK) | P1 archived *or* **P2 fresh (current dominates)** |
| 2 | HLA-E expression | 0.500 | HLA-E⁺ closes the NK route → forces T-cell/MHC-I-priming route | P1/P2, T1 |
| 3 | Treg/FoxP3; TIGIT axis | 0.312 | Regimen composition | P1/P2 |
| 5 | NK functional reserve (post-WLI/chemo) | 0.250 | Unfit NK → T-cell route or IL-15 host repair | **P2/P3 only — unrecoverable from archive**, T1 |
| 6 | MHC-I/B2M/TAP1 integrity; CD8 TIL | 0.188 | V3-prime→T-cell vs NK-first (NK fallback limits marginal value) | P1/P2 |

*Tier-C low-impact (with reason):* static baseline PD-L1 (modelled as IFN-induced/adaptive); mRNA-vaccine
immune status (null at 2+ yr). *Also unknown and decision-relevant for THIS patient:* 25-OH-vitamin-D status,
serum zinc, baseline folate/Mg, smoking status, actual liposomal-vitamin-C plasma level, juicing method.

**(2) Test-level "what to learn next" (diagnostic-action register + sequencing rule).** Rank each *action*
by dominant value ÷ acquisition burden; **archived P1 bundle first → fresh P2 only for the residual delta →
liquid P3 monitoring → imaging on its own staging cadence; re-rank after each result.**
1. **Archived bundle first (P1, F1, one block):** DUX4 IHC (driver EVSI) + methylation array (collapses D4
   phenocopy) + baseline multiplex immune IHC (the 6-variable bundle). Highest realizable VoI-per-burden, no
   new procedural risk.
2. **Fresh increment only for the residual delta (P2, F2):** long-read WGS+RNA-seq (the one test needing
   high-MW DNA), the **current (T1)** immune read on **relapse tissue** (the markers most subject to immune
   editing — see Metastatic section, FH-2), and live NK reserve — **only if** a contingent program is actually
   on the table.
3. **Liquid (P3):** ctDNA only **after** a junction is resolved (then a low-burden serial MRD tool).
4. **Imaging:** restaging CT ± FDG-PET on its own *staging* axis (oligometastatic mapping / metastasectomy-SBRT
   eligibility) — a real, often management-changing value that the framework does **not** quantify (named gap,
   not fabricated).
*Low-yield register:* repeat short-read FISH after a prior negative (cryptic-junction problem — info lives in
long-read, not a re-run); ctDNA before a junction is resolved; generic serum tumour markers with no CIC linkage.

**(3) Resolving the driver is the single highest-value next action for this fusion-unconfirmed case** (ADR-0008,
FH-1): nuclear DUX4 IHC (cheap, P1) → licenses/excludes the MCL1 + junction-targeted lines; long-read WGS+RNA-seq
next; methylation array collapses phenocopy. **The throttle/cell-cycle/immune vectors are driver-ROBUST** (safe
to reason about before resolution); **the MCL1 "re-arm" and junction-specific lines are driver-CONTINGENT — HOLD.**

---

## What This Catalog Cannot Tell You

- **Whether any entry works in CIC-DUX4, or in this patient.** There is **zero CIC-DUX4-specific clinical
  evidence** for any dietary compound and almost none for any drug; most entries are Mechanistic/Preclinical-Cell
  and carry 1–3 order-of-magnitude concentration mismatches.
- **The direction or magnitude of the piperine/curcumin/thymoquinone × ifosfamide interaction** — no human PK
  study of that combination exists; the branch-point mechanism is Established only for ifosfamide's general
  pharmacology.
- **This patient's actual immune phenotype, driver, micronutrient status, smoking status, liposomal-vitamin-C
  plasma level, or whether the relapse clone diverges from the primary** — all unmeasured; the highest-VoI gaps
  are flagged above.
- **Anything requiring a clinician's judgement:** any testing decision, any change to the regimen, any
  start/stop of any therapy, the timing of a fresh biopsy relative to imminent ifosfamide, and oligometastatic
  local-control eligibility (metastasectomy/SBRT — named for MTB discussion, not evaluated here).
- **Perishable facts** (tazemetostat withdrawal, NTX1088/N-803/valemetostat status, trial recruitment, the
  CIC::DUX4 case report PMID 40128305) — dated 2026-06-14 or tagged `[VERIFY]`; re-verify live before any use.

---

## Bibliography

Every citation reproduced from the vector summaries / mRNA team / metastatic specialist / standing layers,
each previously verified or explicitly tagged. **No fabricated citations.** Access date for live-verified
regulatory/trial facts: **2026-06-14** unless noted.

**CIC-DUX4 biology / targets:**
- Bakaric et al., *Cancers* 2024;16(2):457, PMID 38275898, DOI 10.3390/cancers16020457 — CIC-DUX4 p300/CBP activator.
- PMC8511258 — CIC-DUX4 inactivation via p300/CBP inhibition (dCBP-1).
- PMID 40841513, DOI 10.1038/s41467-025-62629-6 — CIC::DUX4 tumoroids: MCL1 target (*Nat Commun* 2025).
- PMID 40841360, DOI 10.1038/s41467-025-62673-2 — small-round-cell tumoroid biobank: CIC::DUX4 MCL-1 vulnerability.
- Italiano et al., PMID 27664537 — CIC-DUX4 low-TMB (CIC-DUX4-direct); ARID1A/1p loss (Specht, *Hum Pathol* 2016).
- Yoshimoto et al., *Cancer Res* 2017;77(11):2927-37, PMID 28404587 — Ccnd2 via ETV4/PEA3 in mouse CIC-DUX4.
- Kawamura-Saito et al., *Hum Mol Genet* 2006, PMID 16717057 — original CIC-DUX4 cloning.
- Macedo et al., *Histopathology* 2025, DOI 10.1111/his.15341 — DUX4 IHC (48 confirmed cases).

**Epigenetic / MHC-I / clinical:**
- Wang et al. 2019, PMC6843866 (HDACi MHC-I, glioma); *Nat Commun* 2025 DOI 10.1038/s41467-025-62934-0 (romidepsin); Luo et al. *Nat Commun* 2018 DOI 10.1038/s41467-017-02630-w (guadecitabine MHC-I).
- Tazemetostat worldwide withdrawal 2026-03-09 (Ipsen press releases; OncLive; CancerNetwork) `[VERIFY]`; NCT02601950, NCT04917042. Valemetostat NCT07303387.
- BMS-986158 NCT02419417 / PMID 36077617; pediatric NCT03936465; OTX015 NCT02296476; AZD5153 (AACR/MCT 2023); ZEN-3694 NCT06161493.
- Palbociclib GEIS ph2 PMC10598203; abemaciclib DDLPS (JCO PO.21.00211). CDK4/6i FDA 2015–2017 / EMA 2016–2018.
- EORTC 62961-ESHO 95 (Issels, *Lancet Oncol* 2010;11:561-570; *JAMA Oncol* 2018) NCT00003052 `[PMID VERIFY]` — regional hyperthermia STS.

**Immune / V4:**
- Tawbi et al. *Lancet Oncol* 2017, PMID 28988646 (SARC028); D'Angelo et al. *Lancet Oncol* 2018 (Alliance A091401; 2024 expansion PMID 39343511).
- Johnson et al. *Nat Commun* 2021, PMID 34376667 (PEMDAC). CIC::DUX4 dual-ICB case *npj Precis Oncol* PMID 40128305 / PMC11933392 `[VERIFY]`.
- SKYSCRAPER-01 / -02 (anti-TIGIT ph3 failures). NTX1088 NCT05378425 `[VERIFY]`. N-803/Anktiva FDA 2024-04-22 (QUILT-3.032) `[VERIFY]`.
- Intismeran autogene KEYNOTE-942 5-yr (Jan 2026), NCT05933577; autogene cevumeran BNT122 NCT04486378 `[VERIFY]`.
- Casares 2005 PMID 16365148; Obeid 2007 PMID 17187072 (doxorubicin ICD). Routy 2018 PMID 29209380; Gopalakrishnan 2018 PMID 29097493; Davar 2021 PMID 33542131; Spencer 2021 PMID 34941392; Wastyk 2021 PMID 34256014. VITAL PMID 30415629.

**V1 / V2 / regimen / harms:**
- Shoba 1998 (*Planta Medica*; curcumin+piperine, n=10 — caveat). Bhardwaj 2002 PMID 12130727 (piperine CYP3A4/P-gp). Curcumin P-gp PMID 12363453; rat PK 21506134/22512082. Quercetin PK PMID 21544726, 19414395. PMC10671713 (thymoquinone serum non-detect).
- Heaney 2008 PMID 18829561; Sayin 2014 PMID 25214635; Le Gal 2015; Lawenda 2008 PMID 18612170. ATBC PMID 8127329; CARET PMID 8602180; SELECT PMID 19066370. Blount 1997 PMID 9096386. Yatomi 2015 PMID 26660549 (RvD1). PMC8971049/PMC6433442 (ifosfamide hypomagnesemia). PMC7281559 (NAD+/PARP1 chemoresistance). PMC3259297 (carrot-juice β-carotene). NCT03508726 (IV-ascorbate STS).

**mRNA team:**
- Barda 2021 PMID 34432976; Kared 2022 PMID 35087044 `[VERIFY]`; Kozma 2022 PMID 35853896 `[VERIFY]`; Ishida 2006 PMID 16797763; Netea 2016 PMID 27102489; Ndeupen 2021 PMID 34825150; Arunachalam 2021 PMID 33951659.

**Host-biology / layers:**
- NLR/mGPS PMID 34969280; sarcopenia/ifosfamide PMID 39921759; ACSM exercise PMC6814265; perioperative β-blockade/COX-2 PMID 28490464; CTRA Cole PMID 31592179.
- Internal: `biomarker-voi-stratification.md` (+ provenance ext.), `diagnostic-information-gain-layer.md`, `translational-feasibility-layer.md` (+ attrition ext.), `host-biology-modifier-layer.md`, `v4-immune-watchdog/immune-watchdog-expansion.md`, `tumorigenesis-reverse-engineering/` (+ driver-uncertainty), `therapeutic-modality-layer.md`, `oncolytic-virotherapy-danger-signal-layer.md`, `docs/10-evidence-transferability-hierarchy.md`, `findings-ranking.md`; `sims/02,04,06,07,08`.

*Research simulation / hypothesis generation only. Not medical advice. No dosing, start/stop, or treatment
recommendations are made or implied. Regulatory/trial status dated 2026-06-14 or tagged `[VERIFY]` and is
perishable — re-verify before any external use.*
