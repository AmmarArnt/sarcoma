# Oncolytic Virotherapy as an "Artificial Danger-Signal Generator" — M4 deep-dive through the V4 lens

**Origin:** GitHub issue #11 (@Cerimagic), follow-up comment of 2026-06-13 — *"Oncolytic Viruses as
Artificial Danger-Signal Generators."*
**Status:** Incremental deepening of the **M4 (gene/viral) cell of the therapeutic-modality layer**
([ADR-0018](../docs/adr/0018-therapeutic-modality-layer.md)) viewed through the **V4 danger-signal / ICD
biology** already adopted in [ADR-0006](../docs/adr/0006-immune-watchdog-danger-signaling-expansion.md).
**Not a fifth vector; not a new scoring axis** (golden rules §8, and ADR-0018's load-bearing rule). Adopted
via [ADR-0019](../docs/adr/0019-oncolytic-virotherapy-m4-deepdive.md).
**Date written:** 2026-06-14. **Regulatory/trial status verified live this date — perishable, re-verify
before any external use.** **Research-simulation hypothesis generation only — not medical advice, not a
treatment recommendation, not a diagnosis.**

---

## One-line summary

The contributor's framing is **biologically correct and already half-built into the framework**: oncolytic
viruses (OVs) are best understood not primarily as direct cytolytic agents but as **in-situ generators of the
exact danger signals V4/ADR-0006 already names** (PAMPs + DAMPs: dsRNA→RIG-I/MDA5/TLR3, viral DNA→cGAS-STING,
plus calreticulin / HMGB1 / ATP / type-I IFN), i.e. a route to convert an **immunologically "cold,"
MHC-I-low, low-neoantigen CIC-DUX4 lesion into a visible one**. The honest counterweight — which the
optimistic literature glosses over and golden rule §5 demands I surface — is that **the sarcoma family
closest to CIC-DUX4 (the Ewing / undifferentiated round-cell group) has shown among the *lowest* OV
susceptibility in preclinical panels, and there is *zero* CIC-DUX4-specific OV data.** So OV is a
**high-conceptual-value, low-direct-evidence forward modality**: `Clinical-Trial` tier *in sarcoma broadly*
(one positive phase-2 combination), collapsing to `Theoretical` for CIC-DUX4 itself.

---

## 1. The conceptual distinction the contributor drew — and why it is the right one

The comment proposes separating two things therapies do:

> *"some therapies primarily strengthen immune **effector function**, while others primarily increase the
> probability that the immune system **notices the target** in the first place."*

This maps cleanly onto the framework and is worth adopting as standing language inside V4:

| Axis of action | What it fixes | Framework home | Example interventions |
|---|---|---|---|
| **Effector strength** ("can the immune system kill it?") | weak/exhausted/blocked effectors | V4 checkpoint, NK-rescue, IL-15 (N-803), TIGIT/PVR axis (ADR-0006 B/C) | anti-PD-1, anti-NKG2A, anti-PVR, CAR/TIL (M2/M3) |
| **Recognition / visibility** ("does it notice the target at all?") | low antigenicity **and** low adjuvanticity | V4 danger-signal/ICD module (ADR-0006 A1–A6); MHC-I restoration (V3→V4 bridge) | ICD-competent chemo scheduling, radiation/STING, **and oncolytic viruses (this file)** |

OV is unusual because it acts **predominantly on the recognition axis, and on both of its sub-parts at
once**: it raises **antigenicity** (lyses cells → releases the tumour's own antigen repertoire, including
otherwise-cryptic antigens, *without needing to know the junction sequence*) **and** **adjuvanticity**
(floods the microenvironment with PAMPs + DAMPs). That dual action is exactly the "alarm system" metaphor in
the comment, and it is the single best mechanistic argument for OV in a tumour like CIC-DUX4 whose suspected
rate-limiter is **antigen-presentation quality + low mutational load**, not effector availability
(ADR-0006 Q1). An OV that forces antigen release + a type-I-IFN/DAMP context is a way to **manufacture the
adjuvant that the checkpoint/NK levers presuppose but do not generate themselves.**

---

## 2. Where OV sits in the framework (two coordinates, no new vector)

- **Modality coordinate:** **M4** (gene/viral) on the ADR-0018 grid — the cell that layer explicitly logged
  as **"Absent"** in the catalog and named as the highest-conceptual-value M4 forward item.
- **Vector coordinate:** primarily **V4** (immune visibility/clearance); with a secondary **V2↔V4** edge
  (OV-induced lysis + dsRNA is a DNA-damage/stress-and-danger source, the same bridge hyperthermia and
  radiation occupy in ADR-0018 §M7) and a faint **V3** edge (forced differentiation/lytic exit of a stalled
  progenitor — speculative).

Per ADR-0018's load-bearing rule, **the modality moves only the feasibility axis** — being deliverable as a
virus earns OV **no** evidence-tier credit. Its tier is set by the biology/data, and its confidence by
Directness (ADR-0014): an OV result in *non-CIC* sarcoma transfers at the **P2 (sarcoma)** rung, not P0.

---

## 3. The load-bearing honesty: the Ewing/round-cell OV-susceptibility problem

Before the platform tour, the disconfirming evidence, because it should colour everything below:

- In a panel testing engineered oncolytic HSVs (NV1020, G207) across sarcoma lines, **Ewing-sarcoma lines
  were the *least* susceptible**, below rhabdomyosarcoma and osteosarcoma. `Preclinical-Cell`.
  `[PMID VERIFY — engineered-HSV sarcoma panel]`.
- Oncolytic **protoparvovirus H-1 (H-1PV)** induced apoptosis and lytic infection in Ewing cells *in vitro*
  but **failed to improve survival *in vivo*** (Geiss et al., *Viruses* 2017/2018; PMC6024310).
  `Preclinical-Animal` (negative in vivo).
- **No CIC-DUX4-specific OV datum exists** at all (cell, animal, or clinical) — confirmed absent this session.

CIC-rearranged sarcoma is biologically distinct from Ewing (different driver, *CIC-DUX4* vs *EWSR1-FLI1*),
so Ewing's poor OV susceptibility does **not** transfer as a hard prediction — but it is the **nearest
available evidence**, and it points the *wrong* way. This is why the modality is logged as forward space, not
a recommendation: the "cold-tumour-made-hot" story is mechanistically attractive but **the closest real data
are discouraging, and the disease-specific data are nil.**

---

## 4. Platform-by-platform — the named OVs, scored honestly

Tier per `sarcoma-contract`. **Sarcoma evidence** = best evidence in *any* sarcoma. **→CIC-DUX4** =
Directness/confidence of transfer (ADR-0014). **Feas.** = F1–F5 (ADR-0003), perishable. Direct CIC-DUX4
evidence is **None** for every row.

| Platform (virus class) | Best sarcoma-relevant evidence | Tier (in sarcoma) | →CIC-DUX4 | Feas. | Verified status (2026-06-14) |
|---|---|---|---|---|---|
| **T-VEC / talimogene laherparepvec** (HSV-1, GM-CSF) | **Phase-2 T-VEC + pembrolizumab, advanced sarcoma, ORR 30% (6/20 PR) at 24 wk**, responses across subtypes incl. UPS — Kelly/Antonescu, *JAMA Oncol* 2020 (DOI 10.1001/jamaoncol.2019.6152; NCT03069378; PMID `[VERIFY]`). Pediatric phase-1 in advanced non-CNS tumours (NCT02756845). | **Clinical-Trial** (sarcoma, combination) | **Low** (P2 sarcoma; small single-arm; not CIC-DUX4) | **F2** (approved agent → trial/named-patient use; deep/visceral CIC-DUX4 limits intratumoral access) | FDA-approved 2015 (melanoma, OPTiM); EMA 2015 `[VERIFY]`. The **one positive sarcoma OV signal**. |
| **RP1 / vusolimogene oderparepvec** (HSV-1 + GALV-GP-R⁻ + GM-CSF; Replimune) | No dedicated sarcoma data; melanoma program | Clinical-Trial (melanoma) | Low | **F4** | **FDA rejected twice** — CRL Jul 2025; **second rejection 2026-04-10** ("insufficient … substantial evidence of effectiveness"). Access route closed; **attrition reason ≈ R2 trial-design/efficacy, not R1 target-invalidation** (ADR-0013) — the *modality* is not refuted. |
| **RP2 / RP3** (RP1 backbone + anti-CTLA-4 / additional immunomodulators; Replimune) | Early-phase, no sarcoma readout | Preclinical/early-clinical | Low | F4/F5 (sponsor under pressure post-RP1) | Status perishable `[VERIFY]`. |
| **OH2** (oncolytic HSV-**2**, GM-CSF, ΔICP34.5/ΔICP47; Binhui) | **Two-patient advanced-sarcoma case report** with immune activation/activity (PMID 38638849, 2024); broader phase I/II in solid tumours (bladder NCT05248789, CNS NCT05235074, pancreatic NCT04637698) | **Preclinical/early-clinical** (sarcoma = 2-case report) | Low | F3 (China-centred trials; little ex-China access) | Active development in China; not approved `[VERIFY]`. |
| **VG161** (HSV-1 expressing IL-12 + IL-15 + a PD-L1-blocking peptide; Virogin) | No sarcoma data; HCC/GI program (NCT04806464; +nivolumab NCT06008925; NCT05162118; NCT06124001) | Clinical-Trial (HCC/GI) | Low | F3 | In trials, not approved `[VERIFY]`. Cytokine-armed design is conceptually attractive for a cold tumour. |
| **Reovirus / pelareorep** (wild-type dsRNA reovirus; Oncolytics) | **Phase-2 in bone & soft-tissue sarcoma metastatic to lung** (NCT00503295, completed); reovirus induces CXCL10/IP-10 and is anti-angiogenic in STS irrespective of RAS status; replication favoured in **RAS/MAPK-active** cells | **Clinical-Trial** (sarcoma, single-arm/older) | Low–Medium (mechanistic interest, see §below) | F3 (no current sarcoma trial; pelareorep focus is breast/PDAC) | Review PMID 25693885; STS mechanism Oncotarget 2017 `[PMID VERIFY]`. **Non-engineered, IV-deliverable** — relevant for visceral disease. |
| **Seneca Valley Virus (SVV-001 / NTX-010)** (picornavirus) | **COG pediatric phase-1 incl. rhabdomyosarcoma** (Burke et al., *Pediatr Blood Cancer* 2015;62:743–750, PMID 25307519); pediatric preclinical testing PMID 20582972 | Clinical-Trial (pediatric, neuroendocrine-selected) | **Very Low** | F3/F4 | **Entry requires the receptor ANTXR1/TEM8 and a neuroendocrine phenotype** — CIC-DUX4 is **not** neuroendocrine, so SVV tropism likely *does not fit*. Honest mismatch, not a candidate. |
| **Newcastle Disease Virus (NDV)** | Historical solid-tumour use; no modern sarcoma RCT; no approved Western product | Mechanistic/historical | Very Low | F4/F5 | Included for completeness; strong type-I-IFN inducer but no current regulated route `[VERIFY]`. |
| **Oncolytic measles (MeV-Edm) / H-1 parvovirus** (Ewing-context references) | H-1PV: apoptosis in Ewing in vitro, **failed in vivo** (PMC6024310); measles broadly studied, no CIC data | Preclinical (Ewing) | Very Low | F4/F5 | Cited for the §3 disconfirming signal, not as candidates. |

### The one mechanistically interesting transfer — reovirus and the MAPK output

CIC-DUX4 drives a transcriptional program with **RAS/MAPK-like (ERK) output** — the very axis V1 targets as
the upstream "rate-limiter." Reovirus replicates **preferentially in RAS/MAPK-active cells**, which is the
single most disease-relevant tropism argument among all the named platforms (it is not junction-dependent and
the virus is IV-deliverable, addressing the deep/visceral-access problem that limits intratumoral HSV
products). This is a **`Mechanistic`/`Theoretical`** hypothesis for CIC-DUX4 — attractive enough to log as a
forward experiment (§8 FH-2), **not** evidence of efficacy.

---

## 5. Translational feasibility & real-world accessibility map (the explicit ask)

The comment asks the framework to map not just plausibility but the **real-world path**. Honest map, this
date; **every status is perishable (ADR-0003) — re-verify before relying on it.**

**Regulatory status by region (modality reality check):**
- **Only one OV is approved in the US/EU at all** — **T-VEC** (FDA 2015, EMA 2015 `[VERIFY]`), for
  **melanoma**, by **intralesional** injection. Every other use, including any sarcoma use, is **off-label or
  trial-only**.
- **RP1's two FDA rejections (2025, 2026-04-10)** are the cautionary headline: the most advanced *next* OV
  did **not** clear the bar. This tempers any "OV is arriving imminently" framing.
- **China** has the most active late-stage OV pipeline of relevance here (OH2, VG161), but those are **largely
  inaccessible outside China** and not sarcoma-validated.

**Trial landscape for a sarcoma patient (the realistic routes):**
1. **T-VEC ± checkpoint, intralesional** — only realistic for **accessible (cutaneous/subcutaneous/superficial
   nodal) lesions**; most CIC-DUX4 is **deep trunk / retroperitoneal / visceral**, which is the **dominant
   feasibility limiter** (anatomy, not biology). Image-guided intratumoral injection of deep lesions exists at
   specialised centres but is procedurally demanding `[VERIFY centre-level]`.
2. **Systemically deliverable OVs (reovirus/pelareorep; some adenovirus/vaccinia platforms)** — circumvent the
   access problem but have **no current sarcoma-specific trial** open `[VERIFY clinicaltrials.gov live]`.
3. **Basket/solid-tumour OV-with-neuroendocrine or OV-pediatric trials** — SVV/NTX-010 logic is
   neuroendocrine-selected (poor CIC-DUX4 fit, §4).
4. **Compassionate-use / named-patient / expanded-access** for an unapproved OV is **rare, sponsor-dependent,
   and not a reliable route** — and the Halassy episode (§6) shows what the *unregulated* extreme looks like
   and why it is not a model. The framework does not endorse it.

**The honest accessibility verdict:** the modality's real-world feasibility for a deep/visceral CIC-DUX4
patient is **F3 for the systemic platforms (in development, no sarcoma route here today)** and **F2 only if a
lesion is physically injectable and a T-VEC-based trial/named-patient route is open** — bounded sharply by
**anatomy** and by the fact that **the field's lead next-gen asset just failed twice at FDA.**

---

## 6. The investigator / institution ecosystem — and the Halassy N-of-1 (handled honestly)

The comment asks who works in this space. Naming a *living* researcher as endorsing a specific path is exactly
where fabrication risk is highest (this is the lesson of the earlier corrected Halassy citation in this repo),
so this is deliberately **general and verifiable**, not a roster of endorsements:

- **The positive sarcoma OV trial (T-VEC + pembrolizumab) was run at Memorial Sloan Kettering** (Kelly,
  Antonescu, D'Angelo and colleagues; NCT03069378) — a real anchor for "where sarcoma + OV expertise
  co-locate." Other large sarcoma programs (MD Anderson, Mayo's virotherapy group, City of Hope) run
  OV/immunotherapy trials broadly; **specific open CIC-DUX4-relevant OV trials at any of these centres should
  be checked live on clinicaltrials.gov rather than asserted here** `[VERIFY]`.
- **Beata Halassy case (the comment names it):** a real, published **N-of-1 self-experiment** — a virologist
  treated her own **recurrent breast cancer** (not a sarcoma) with lab-grown OVs (measles virus then VSV per
  the report), intratumoral neoadjuvant, with tumour shrinkage, lymphocyte-infiltrated resection, and
  multi-year remission (*Vaccines* 2024;12(9):958; PMCID PMC11435696). **Honest read:** it is a single,
  uncontrolled, self-administered case in a *different* tumour type, published only after numerous rejections
  on **ethics (self-experimentation)** grounds — it is **anecdote/`Theoretical` for any inference about
  CIC-DUX4**, and it is included here to *answer the question accurately*, **not** as support for the modality
  and **not** as a path any patient should emulate.

---

## 7. The guiding question, answered directly

> *"If a promising virotherapy hypothesis is generated, what is the nearest real-world path through which a
> patient could potentially access, discuss, or further investigate that approach?"*

Honestly, for a deep/visceral CIC-DUX4 patient **today**:
1. **The discussion** belongs with a **sarcoma medical oncologist at a centre that runs OV/immunotherapy
   trials** (MSK ran the only positive sarcoma OV study) — framed as "is any open OV or OV+checkpoint trial
   appropriate, and is any lesion injectable?"
2. **The nearest *real* route** is **T-VEC ± checkpoint via a trial or named-patient mechanism, only if an
   anatomically injectable lesion exists** — otherwise the modality is presently **trial-gated with no open
   sarcoma-specific systemic option**.
3. **What would change this:** an open systemic-OV sarcoma/solid-tumour basket trial; or CIC-DUX4-relevant
   preclinical tropism data (does CIC-DUX4 support OV replication at all — see §3, §8). Both are checkable
   triggers, not promises.

This is **information for a clinician conversation, not a recommendation** to pursue OV.

---

## 8. Forward hypotheses (CIC-DUX4-specific, falsifiable; not in the literature)

**[FH-1] "Make the cold lesion hot" — OV as the antigen+adjuvant source feeding the V4 levers.**
*Hypothesis:* an OV that replicates in CIC-DUX4 cells converts the MHC-I-low/low-neoantigen lesion to an
IFN-high, DAMP-rich, antigen-releasing state, **and that conversion — not lysis per se — is what licenses a
subsequent checkpoint/NK step** (the ADR-0006 sequencing logic, with OV supplying the missing adjuvant).
*Falsifier:* OV infection of CIC-DUX4 models produces lysis **without** a measurable rise in type-I IFN /
calreticulin / HMGB1 / T-cell infiltration on paired biopsy → the "visibility" rationale fails and OV reduces
to a weak direct cytotoxic.

**[FH-2] Reovirus tropism tracks CIC-DUX4's MAPK output.**
*Hypothesis:* because reovirus favours RAS/MAPK-active cells and CIC-DUX4 drives an ERK-like program,
CIC-DUX4 lines support reovirus replication better than the Ewing lines that resisted engineered HSV (§3) —
giving a **systemically deliverable** (visceral-disease-compatible) option.
*Falsifier:* CIC-DUX4 lines are non-permissive to reovirus despite MAPK activity (the §3 round-cell-resistance
signal dominates) → drop the reovirus route.

**[FH-3] The threshold question: can CIC-DUX4 even be infected/lysed?**
*Hypothesis (and the gating experiment for the whole modality):* the §3 Ewing data predict **low
permissiveness**; the necessary first datum is a tropism/replication screen of a small OV panel
(HSV-1/T-VEC-class, reovirus, measles, adenovirus) across CIC-DUX4 lines/PDX.
*Falsifier:* uniformly low replication/lysis across the panel → OV is the **wrong modality** for CIC-DUX4 and
should be parked, redirecting the "danger-signal" goal to non-viral ICD sources (radiation/STING, hyperthermia
— ADR-0018 §M7; doxorubicin-ICD scheduling — ADR-0006 A2).

---

## 9. Standard-of-care interaction flags

- **OV × corticosteroids / broad immunosuppression:** steroids (common antiemetic/supportive use, and
  ifosfamide-encephalopathy management) could **blunt the very IFN/DAMP response** the OV is meant to create —
  a state-(2) suppression in the ADR-0006 inflammation-state lens. Mechanistic/theoretical; an oncologist's
  call, not a dosing instruction.
- **OV × chemotherapy timing (VDC/IE):** lymphodepleting chemo can either **aid** OV (dampening antiviral
  clearance, enabling replication) **or harm** the downstream immune-capture step — the effect is
  schedule-dependent and unmodelled here (`sarcoma-chemo-interactions`). No timing is recommended.
- **OV × doxorubicin:** doxorubicin is itself an ICD inducer (ADR-0006 A2); whether OV + anthracycline ICD is
  additive or redundant is unknown — flagged, not claimed.
- **No dietary/supplement compound is introduced here**, so the CYP/P-gp/ROS dietary screens are not triggered
  by this artifact.

---

## 10. Atypical-case flag (~5% fusion-unconfirmed)

OV is **fusion-agnostic**: its mechanism (replication in permissive tumour cells + PAMP/DAMP generation +
release of the tumour's *own* antigen repertoire) **does not depend on the CIC-DUX4 junction sequence**, so it
applies unchanged to the fusion-unconfirmed subgroup (golden rule §9; ADR-0008). This is a genuine advantage
over the junction-specific M3/M5 modalities (TCR-T, junction vaccines), which are fusion-contingent. The one
caveat is permissiveness (§3/§8 FH-3), which is a tumour-cell-biology question independent of fusion status.

---

## 11. What I could not establish

1. **Whether CIC-DUX4 cells are permissive to *any* OV** — no tropism/replication data exist; the nearest
   evidence (Ewing/round-cell) is *discouraging* (§3). This is the gating unknown (FH-3).
2. **Whether CIC-DUX4 lysis would be immunogenic** (IFN/CALR/HMGB1/ATP emission) — unmeasured, same gap as
   ADR-0006 A1–A6 for this disease.
3. **The exact PMID** for the Kelly *JAMA Oncol* 2020 sarcoma trial and for the engineered-HSV sarcoma panel
   and the reovirus-STS mechanism paper — cited by DOI/journal/NCT, PMIDs marked `[VERIFY]` rather than
   asserted.
4. **EMA approval date** for T-VEC (cited as 2015, `[VERIFY]`) and the **current** status of OH2/VG161/RP2/RP3
   and any open OV sarcoma trial — perishable; verify live on the registries (docs/09).
5. **The precise virus identities/strains** in the Halassy case beyond the published report's description.
6. **Any quantitative synergy** for OV + checkpoint / OV + NK in sarcoma beyond the single T-VEC+pembro ORR.

---

## 12. Red-team self-challenge (ADR-0017, one pass)

- **Load-bearing assumption:** that OV's "cold→hot / artificial alarm" mechanism is *applicable* to CIC-DUX4.
- **Disconfirmation (actively sought):** the closest real data — Ewing/round-cell lines showing the **lowest**
  OV susceptibility, and H-1PV **failing in vivo** in Ewing — point against applicability; and the field's
  lead next-gen asset (RP1) **failed FDA twice**. I led §3 with this rather than burying it.
- **Alternative hypothesis:** the danger-signal *goal* is right but the **vehicle** is wrong — non-viral ICD
  sources already in the framework (radiation/STING and hyperthermia, ADR-0018 §M7; doxorubicin-ICD
  scheduling, ADR-0006 A2) may achieve the same "visibility" with better feasibility and no permissiveness
  gate. This is explicitly preserved as FH-3's fallback.
- **Flip test:** if OV does **not** transfer to CIC-DUX4, the claim degrades from "promising modality" to
  "mechanistically coherent but unproven forward modality whose gating experiment is a tropism screen" — which
  is all this file asserts. No efficacy is claimed.
- **Steer audit:** the contributor steered toward "OV is a powerful answer." I **tested** rather than amplified
  it — affirming the *conceptual* fit (effector-vs-visibility, §1) while surfacing the discouraging round-cell
  data, the deep-tissue access limit, the RP1 failures, and the SVV tropism mismatch. The output is not an
  endorsement.

---

*Provenance:* deepens the **M4** cell of `therapeutic-modality-layer.md` (ADR-0018) using the danger-signal /
ICD biology of `v4-immune-watchdog/immune-watchdog-expansion.md` (ADR-0006); applies the feasibility
(ADR-0003) + attrition-reason (ADR-0013) + transferability (ADR-0014) layers. **External facts verified live
2026-06-14:** T-VEC+pembro sarcoma phase-2 (JAMA Oncol 2020, DOI 10.1001/jamaoncol.2019.6152, NCT03069378,
ORR 30% 6/20); T-VEC FDA 2015 / OPTiM; pediatric T-VEC NCT02756845; RP1 FDA CRL Jul 2025 + second rejection
2026-04-10; OH2 two-case sarcoma report PMID 38638849 + NCTs 05248789/05235074/04637698; VG161 NCTs
04806464/06008925/05162118/06124001; reovirus sarcoma NCT00503295 + review PMID 25693885; SVV/NTX-010 COG
pediatric PMID 25307519 + 20582972; H-1PV-in-Ewing PMC6024310; Halassy *Vaccines* 2024;12(9):958 / PMC11435696.
**No fabricated citations; PMIDs not pinned live are marked `[VERIFY]`; no OV asserted effective in CIC-DUX4.**

*Decision record:* [ADR-0019](../docs/adr/0019-oncolytic-virotherapy-m4-deepdive.md) (issue #11 follow-up).
**Research simulation / hypothesis generation only. Not medical advice.**
