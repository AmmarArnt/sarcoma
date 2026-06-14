# Therapeutic-Modality Layer ("How is it delivered?" — beyond systemic pharmacology)

**In response to GitHub issue #33** — *"Therapeutic Modality Expansion Beyond Systemic Pharmacology"*
(@Cerimagic), and its two follow-up comments: a **drug-repurposing scan** and an
**ethnopharmacology / phytotherapy hypothesis-space**.

> **See also (this layer cross-cuts the four vectors; it does not replace them or add a fifth):**
> the V4 expansion ([`v4-immune-watchdog/immune-watchdog-expansion.md`](v4-immune-watchdog/immune-watchdog-expansion.md),
> [ADR-0006](../docs/adr/0006-immune-watchdog-danger-signaling-expansion.md)) already covers ICD / DAMPs
> that several of these modalities exploit; the
> [feasibility + attrition layers](translational-feasibility-layer.md)
> ([ADR-0003](../docs/adr/0003-translational-feasibility-layer.md) /
> [ADR-0013](../docs/adr/0013-feasibility-attrition-reason-annotation.md)) carry the regulatory-status and
> repurposing-path machinery; the
> [evidence-transferability hierarchy](../docs/10-evidence-transferability-hierarchy.md)
> ([ADR-0014](../docs/adr/0014-evidence-transferability-hierarchy.md)) is how non-CIC-DUX4 modality
> evidence is admitted at honest confidence; the
> [host-biology layer](host-biology-modifier-layer.md) ([ADR-0005](../docs/adr/0005-host-biology-modifier-layer.md))
> already owns the host-directed end of modality class **M8**.

**Status:** framework-enhancement (a new standing cross-cutting analytical layer /
[ADR-0018](../docs/adr/0018-therapeutic-modality-layer.md)). Research-simulation output, **not medical
advice**, **not a treatment recommendation**. The goal, exactly as the issue framed it, is to make sure
biologically reasonable opportunities are **not invisible to the framework simply because they are not a
pill** — by naming a **modality axis** orthogonal to the four vectors, mapping what the existing catalog
already covers, and surfacing the under-represented formats as forward space. It does **not** assert any of
these modalities works in CIC-rearranged sarcoma.

**Confidence: medium for the taxonomy/coverage mapping; low for any specific cross-modality transfer to
CIC-DUX4.** The modality classes and the "what's already covered vs. blind-spot" map are well-grounded; the
*disease-specific* value of each under-covered modality is mostly `Theoretical`/`Mechanistic` because
CIC-rearranged sarcoma is too rare for dedicated modality trials. **Evidence tier of this layer itself:**
`Theoretical / Mechanistic` (a coverage/structuring layer — it does **not** outrank any real-data vector
finding).

---

## 1. The question, restated — and the short answer

The issue observes that the simulation evaluates hypotheses **mostly as systemic pharmacology** (a drug or
a dietary compound taken into the bloodstream) and asks whether valuable opportunities are missed by that
framing — naming cellular therapies (TIL / CAR-T / CAR-NK / TCR), viral / oncolytic-virus therapy, vaccine
approaches, local & regional therapies (intratumoral delivery, regional perfusion, hyperthermia), and
physical / energy-based interventions (hyperthermia, focused ultrasound, radiation-based immune priming),
plus combination-modality strategies. Two follow-ups extend the same idea to **sourcing**: a structured
**repurposing** scan of already-approved drugs, and **ethnopharmacology / phytotherapy** as a searchable
hypothesis space.

**Short answer, in three parts:**

1. **The diagnosis is partly correct and worth fixing.** The framework's *organizing* axis is the four
   **vectors** (what molecular goal: V1 throttle / V2 compiler-protect / V3 hot-patch / V4 immune). Vectors
   say nothing about **how an intervention is delivered**. In practice the catalog populated mostly two
   delivery formats — **systemic small molecules** and **dietary compounds** — so several formats the issue
   names were under-represented even where the *biology* was in scope.
2. **But several named modalities already live inside the framework** — they were just never made explicit
   as a modality. V4 already houses checkpoint antibodies, NK approaches, neoantigen/mRNA vaccines, and the
   ICD/DAMP biology that oncolytic viruses and hyperthermia exploit (ADR-0006). The fix is **not new biology
   for those** — it is a *checklist axis* so coverage gaps are visible.
3. **The genuine blind spots are the non-systemic, non-cellular formats** — **regional/local delivery** and
   **physical/energy-based** therapy (especially **regional hyperthermia**, which has a *positive phase-3
   RCT in high-risk soft-tissue sarcoma* — see §4 M7). These had **no** representation in the catalog despite
   real sarcoma evidence. That is the highest-value correction this layer makes.

**This is a cross-cutting axis, not a fifth vector** (golden rule #8). A modality is the *form factor*; the
vector is the *target*. Every entry has both coordinates (a 2-D grid, §2).

---

## 2. Two orthogonal axes: vector (what) × modality (how)

| | **What molecular goal?** → the four fixed **vectors** (V1–V4) |
|---|---|
| **How is it delivered?** ↓ the **modality** classes (M1–M8) | every intervention is one cell in this grid |

**Modality classes (M1–M8):**

| Class | Modality | Examples | Primary vector(s) it serves |
|---|---|---|---|
| **M1** | Systemic small-molecule pharmacology *(framework default)* | EZH2i, BETi, CDK4/6i, kinase inhibitors, most repurposed drugs | V1, V3 (and V2) |
| **M2** | Systemic biologics / antibodies | checkpoint mAbs, antibody-drug conjugates, anti-PVR (NTX1088) | V4 (V3 for ADCs) |
| **M3** | Cellular therapy | TIL, CAR-T, **CAR-NK**, TCR-engineered T cells | V4 |
| **M4** | Gene / viral therapy | oncolytic viruses, virus-mediated immune activation | V4 (ICD → V3 differentiation crosstalk) |
| **M5** | Active immunization / vaccines | tumor / personalized-neoantigen / mRNA vaccines | V4 |
| **M6** | Local / regional delivery | intratumoral injection, intratumoral cytokine, **isolated limb/regional perfusion**, intra-arterial | route-agnostic (amplifies V4 or local control) |
| **M7** | Physical / energy-based | **regional hyperthermia**, focused ultrasound (HIFU), radiation & **radiation-immune priming / abscopal**, cryoablation | V2 (DSB/sensitization) + V4 (DAMP/ICD) |
| **M8** | Dietary / natural-product / host-directed | the V1 dietary track; host-biology layer (microbiome, metabolic, exercise) | V1; conditions V4 + SOC (ADR-0005) |

**Repurposing and ethnopharmacology are not modalities — they are *sourcing strategies*** that feed
candidates **into** the grid (mostly M1/M2 for repurposing; M8/M1 for phytotherapy). They are handled as
two **hypothesis-sourcing sub-scans** (§5–§6), deliberately kept distinct from the modality axis so the
framework does not inflate into "more vectors."

---

## 3. The load-bearing rule: modality changes **feasibility**, not **evidence tier** or **mechanism**

A modality is a *delivery decision*. Within the three scoring axes (`sarcoma-contract`):

- **Evidence tier** is set by the **biology/data**, not the form factor. "Deliverable as a slick cell
  therapy" earns **no** tier credit. A `Theoretical` CAR target stays `Theoretical`.
- **Confidence (incl. Directness, ADR-0014)** is unchanged by modality — a hyperthermia result in
  *non-CIC* STS transfers to CIC-DUX4 at the same proximity discount (P2 sarcoma) as a drug would.
- **Feasibility (F1–F5, ADR-0003)** is where modality *does* move the needle, often **downward**: cellular
  and viral therapies for an ultra-rare fusion sarcoma are typically **F4–F5** (concept/early-trial),
  capacity-limited, and centre-restricted; regional hyperthermia is **F2–F3** but only at specialised
  centres; local perfusion is anatomy-restricted (§4 M6).

So this layer **expands the search space** (the forward lane, golden rule #5) and **annotates feasibility**;
it never promotes a finding's evidence strength because it is delivered in a fashionable format.

---

## 4. Modality coverage map — what the catalog already has vs. the blind spots

Honest audit of `protocol-v2.md` + the V4 outputs against the modality grid. Feasibility bands are
**perishable — re-verify before external use** (ADR-0003).

| Class | Coverage now | Verdict | Highest-value action |
|---|---|---|---|
| **M1** systemic small-molecule | **Strong** — the bulk of V1/V3 (EZH2i, BETi, CDK4/6i, PROTAC/ASO) | covered | — |
| **M2** biologics/antibodies | **Moderate** — V4 checkpoint mAbs, anti-PVR (ADR-0006) | covered | watch ADC payloads vs. CIC-DUX4 surface markers (forward) |
| **M3** cellular (TIL/CAR-T/CAR-NK/TCR) | **Thin / conceptual** — V4 NK + neoantigen arms gesture at it; no executed CAR/TCR analysis | **gap** | scope a fusion-neoantigen **TCR** (intracellular junction ⇒ not CAR) + **CAR-NK** against a CIC-DUX4 surface ligand — **fusion-contingent** (§7) |
| **M4** viral / oncolytic | **Deep-dived** — [`oncolytic-virotherapy-danger-signal-layer.md`](oncolytic-virotherapy-danger-signal-layer.md) (ADR-0019) | gap **worked through** | oncolytic virus as an **ICD/DAMP "artificial danger-signal generator"** (links ADR-0006); one positive sarcoma signal (T-VEC+pembro phase-2), but Ewing/round-cell lines resist OV and CIC-DUX4 data are nil → `Theoretical` in CIC-DUX4 |
| **M5** vaccines | **Moderate** — neoantigen-vaccine + mRNA team exist | covered (fusion-contingent for junction vaccines) | — |
| **M6** local / regional delivery | **Absent** | **gap (bounded)** | isolated limb/regional perfusion is **anatomy-limited** (most CIC-DUX4 is deep trunk/retroperitoneal/visceral, not extremity) — note as bounded, not headline |
| **M7** physical / energy-based | **Absent** | **gap — highest value** | **regional hyperthermia + chemo** has a positive phase-3 STS RCT (below); radiation-immune priming / abscopal as a V2↔V4 bridge |
| **M8** dietary / host-directed | **Strong** — V1 dietary + host-biology layer (ADR-0005) | covered | the ethnopharmacology sub-scan (§6) feeds here |

### The headline correction — M7 regional hyperthermia (a real, missed sarcoma signal)

The **EORTC 62961-ESHO 95** randomised phase-3 trial (Issels et al., *Lancet Oncol* 2010;11:561–570;
NCT00003052; `[PMID VERIFY]`) added **regional hyperthermia** to neoadjuvant chemotherapy in localised
**high-risk soft-tissue sarcoma** and reported improved local progression-free and (on long-term follow-up,
*JAMA Oncol* 2018) overall survival. `Clinical-Trial` tier **in soft-tissue sarcoma broadly** (transfer to
CIC-DUX4 specifically: **P2 sarcoma** proximity, ADR-0014 — not CIC-DUX4-validated). Mechanistically it is a
**V2↔V4 dual hit**: hyperthermia increases chemo/radiation-induced DNA damage and impairs repair (V2) **and**
releases HSPs/HMGB1/DAMPs that can prime immune recognition (V4 / ADR-0006). That the catalog had **zero**
representation of a modality with a *positive randomised sarcoma trial* is exactly the systemic-pharmacology
blind spot the issue predicted. **F2–F3** (specialised centres only); **not a recommendation** — flagged for
the catalog and for clinician awareness.

Other M7: **radiation-immune priming / abscopal** effect (radiation as an *in situ* ICD source feeding V4) —
`Mechanistic`/`Preclinical`; **focused ultrasound (HIFU)** and **cryoablation** as local ICD sources —
`Theoretical` in CIC-DUX4. None fabricated into trial claims.

### Other established cross-modality anchors (real, but transfer-limited)

- **M4 oncolytic virus:** talimogene laherparepvec (T-VEC) is the first **FDA-approved** oncolytic virus
  (Oct 2015, melanoma, OPTiM phase 3) — proof the *modality* is real and approvable; **no CIC-DUX4 data**
  (transfer `Theoretical`).
- **M6 isolated limb perfusion** with **TNF-α + melphalan** is **approved in Europe (1998)** for unresectable
  extremity soft-tissue sarcoma (review: PMID 18066703) — proof the *modality* works in STS, but
  **anatomy-restricted** and largely inapplicable to deep/visceral CIC-DUX4 presentations.

---

## 5. Sub-scan A — structured drug-repurposing (issue comment 1)

The follow-up asks for a structured scan of **already-approved drugs** that hit disease-relevant pathways
(angiogenesis, immune activation, differentiation, apoptosis, DNA-damage response, tumour metabolism), and
of drugs "abandoned for one indication that may matter in another." **This machinery largely already exists**
— the feasibility layer (ADR-0003) carries a *repurposing path*, and the attrition-reason annotation
(ADR-0013) already encodes the comment's core insight that **"abandoned ≠ biologically invalidated"**
(only **R1 target-invalidated** / enriched-**R2 trial-fail** carry negative biology; R3/R4-commercial/R5 are
biology-silent). This sub-scan **names the discipline** so repurposed candidates are not waved in on their
familiarity.

**The discipline (same gauntlet as any candidate):** every repurposed drug gets (a) an **evidence tier on
the CIC-DUX4-relevant mechanism**, (b) a **Directness rung** for the transfer (ADR-0014), (c) a
**concentration-mismatch** check (achievable plasma vs. effective dose), and (d) a **chemo-interaction
screen** (`sarcoma-chemo-interactions`). The issue's own examples, scored honestly:

| Repurposing example | Established where | Mechanism of interest | Transfer to CIC-DUX4 | Honest read |
|---|---|---|---|---|
| **Arsenic trioxide** | APL (FDA 2000) — `Established` | **degrades the PML-RARA *fusion* oncoprotein** (proteasome/SUMO) | `Theoretical` | **Mechanistically the most apt** — a *fusion-degrader* precedent that conceptually echoes V3 PROTAC/ASO degradation of CIC-DUX4. **But** the arsenic mechanism is **PML-specific chemistry, not a general fusion-degrader** — this is a *conceptual analogy*, not a drug to try. |
| **Thalidomide / lenalidomide** | multiple myeloma — `Established` | cereblon/IMiD neosubstrate degradation; anti-angiogenic/immunomodulatory | `Theoretical` | No known CRBN-neosubstrate link in CIC-DUX4; the *molecular-glue degrader* concept is the transferable idea (→ V3), not the drug. |
| **Colchicine** | gout; CV inflammation (COLCOT/LoDoCo2) — `Established` (CV) | microtubule + NLRP3-inflammasome inhibition | `Theoretical` | Vinca alkaloids (microtubule) are **already SOC**; "anti-inflammatory" ≠ "anti-tumour" (inflammation-state lens, ADR-0006). Low priority. |
| **Ivermectin** | antiparasitic — `Established` (parasites) | varied oncology claims (WNT, PAK1, mitochondria) | `Preclinical-Cell` at best | **The cautionary example.** Reported anti-tumour effects occur at **µM concentrations far above achievable human plasma** — textbook **concentration mismatch**. Included to show the scan *filters*, not just collects. |

**Output of the sub-scan:** a small, mechanism-anchored repurposing shortlist routed to the relevant vector
(degrader concepts → V3; metabolic/angiogenic → V1; immune → V4), each carrying tier + Directness +
concentration + chemo-interaction flags. It is **not** a "scan PubMed for any approved drug" exercise —
breadth without the gauntlet is how fabrication and concentration-mismatch errors enter.

---

## 6. Sub-scan B — ethnopharmacology / phytotherapy as a searchable hypothesis space (issue comment 2)

The second follow-up asks the framework to treat **traditional-medicine and phytotherapy literature** (TCM,
Kampo, Ayurveda, ethnobotany, medicinal mushrooms, plant-derived compounds) as a **hypothesis source**, not
to dismiss it as "alternative medicine," noting that artemisinin, paclitaxel, aspirin, and morphine all came
from this space. **This is reasonable and largely already how V1 was populated** — curcumin, sulforaphane,
EGCG, and quercetin are phytochemicals that entered via the V1 Food/Supplement specialists.

**Admitting the space without lowering standards (the explicit ask):**

1. **It is a *source of mechanisms*, scored like any other.** Natural-product → drug success stories
   (artemisinin; paclitaxel from *Taxus*; aspirin from salicin; morphine) became medicines through
   **compound isolation, dose standardisation, and controlled trials** — not as crude preparations. A
   candidate from this space therefore enters at its **real evidence tier** (usually `Mechanistic`,
   `Preclinical-Cell`, or `Dietary-Observational`) and its **Directness rung** for any non-CIC evidence.
2. **Concentration-mismatch is the dominant failure mode here** — most positive in-vitro phytochemical
   results occur at concentrations **unachievable from oral intake** (the standing V1 caveat). This filter
   does most of the work.
3. **Chemo-interaction screen is mandatory** — botanicals are common CYP3A4/P-gp perpetrators (e.g.
   St John's wort) and can collide with VDC/IE (`sarcoma-chemo-interactions`).
4. **Medicinal mushrooms:** β-glucan immunomodulators are the most translationally advanced corner —
   **PSK (polysaccharide-K / krestin)** from *Trametes versicolor* and lentinan are used as adjuvants in
   **Japan** `[VERIFY jurisdiction/status — perishable]`; mechanism is innate immune (macrophage/NK)
   modulation → routes to **V4 / M8** and conditions host biology (ADR-0005). Tier in CIC-DUX4:
   `Theoretical`.

**Output:** ethnopharmacology candidates are **welcomed as forward hypotheses**, routed to V1 (M8) or V4,
and run the same gauntlet as §5. The space is **searchable, not privileged** — exactly the issue's stated
intent ("not to lower evidence standards").

---

## 7. Atypical-case flag (fusion-unconfirmed ~5%)

Modality interacts sharply with the fusion-confirmation question (golden rule #9; driver-uncertainty model,
ADR-0008):

- **Fusion-CONTINGENT modalities (hold/flag if the fusion is unconfirmed):** junction-specific **TCR-T**,
  **CAR** against a fusion-defined surface ligand, and **junction/neoantigen vaccines** (M3/M5) — their
  target *is* the fusion sequence, which varies across patients and is absent in ~5%.
- **Fusion-AGNOSTIC modalities (apply regardless of fusion status):** **regional hyperthermia** (M7),
  **radiation-immune priming** (M7), **local/regional control** (M6), **checkpoint / NK** approaches (M2/M3),
  and the host-directed/dietary end (M8). These do not depend on resolving the driver.

---

## 8. Honest limitations — what this does and does NOT claim

- **No modality is asserted to work in CIC-rearranged sarcoma.** CIC-rearranged sarcoma is too rare for
  dedicated modality trials; nearly every cross-modality claim is `Theoretical`/`Mechanistic` in *this*
  disease, transferred at a P2 (sarcoma) rung or worse (ADR-0014).
- **This is a structuring/coverage layer, not new biology.** It adds an axis and an audit; the mechanisms it
  points to live in the vectors and the V4 expansion (ADR-0006).
- **Feasibility bands are perishable** — every F-band and regulatory status here must be re-verified live
  before external use (ADR-0003).
- **Combination-modality strategies are not modelled quantitatively.** The issue lists "combination modality
  strategies"; this layer only notes the obvious mechanistic pairings (hyperthermia + chemo/RT; oncolytic
  virus / radiation + checkpoint). No synergy magnitude is claimed.
- **Not a recommendation, not medical advice, not a diagnosis.**

**What I could not establish:**
- The exact **PMID** for Issels et al. 2010 (PubMed fetch blocked in-session) — cited by journal/volume/pages
  + NCT00003052, marked `[PMID VERIFY]`.
- Any **CIC-DUX4-specific** efficacy datum for cellular (M3), viral (M4), local/regional (M6), or
  physical/energy (M7) modalities — none found; treated as forward space, not asserted.
- Current **jurisdictional status** of PSK/lentinan as oncology adjuvants `[VERIFY]`.
- A quantitative value for any combination-modality strategy.

**Red-team self-challenge (ADR-0017, one pass):** *Load-bearing assumption* — that the M7 hyperthermia
signal transfers from high-risk STS broadly to CIC-rearranged sarcoma. *Disconfirmation* — EORTC 62961 did
**not** enrich for CIC-rearranged tumours (they are far too rare), and CIC-DUX4 is frequently deep/visceral
rather than the extremity/trunk disease most amenable to regional hyperthermia or limb perfusion; the
transfer is **P2 (sarcoma), not P0**. *Flip test* — if hyperthermia does **not** transfer, the claim
degrades from "highest-value modality" to "highest-value *coverage gap to consider*," which is all this layer
asserts (it makes no efficacy claim). *Steer audit* — the issue steered toward "modalities are missing"; I
**tested** rather than confirmed it by showing M1/M2/M5/M8 are already covered and by bounding M6 as
anatomy-limited, so the layer is not a blanket endorsement of every named format.

---

## 9. Forward work (mechanistically defensible, not executed here)

- **[Forward] Modality-coverage audit as a standing orchestrator check.** At synthesis, tag every catalog
  entry with its M-class and flag any vector whose hypotheses collapse into one or two modalities — a
  cheap guard against the systemic-pharmacology default re-asserting itself on each re-run (wired per §
  ADR-0016; see PR).
- **[Forward / V2↔V4] Hyperthermia-as-ICD sub-hypothesis.** Does regional hyperthermia convert the cold
  CIC-DUX4 microenvironment toward immune visibility (HSP/HMGB1/DAMP release; ADR-0006)? *Falsifier:* if
  hyperthermia's STS benefit is purely chemo-sensitisation with no measurable DAMP/immune shift, the V4 arm
  of the hypothesis is wrong and it reduces to a V2 sensitiser.
- **[Forward / V4] Oncolytic virus or in-situ ICD (radiation/HIFU) + checkpoint** as a route to prime the
  cold microenvironment — `Theoretical` in CIC-DUX4; *falsifier:* no T-cell infiltration shift on paired
  biopsy. **Worked through in the M4 deep-dive** ([`oncolytic-virotherapy-danger-signal-layer.md`](oncolytic-virotherapy-danger-signal-layer.md),
  ADR-0019): gating experiment = a CIC-DUX4 tropism/permissiveness screen, since the nearest data
  (Ewing/round-cell) show *low* OV susceptibility.
- **[Forward / V3] Fusion-degrader repurposing concept.** The arsenic→PML-RARA precedent (§5) motivates a
  *molecular-glue / PROTAC* search for CIC-DUX4 degradation — already V3 territory; this sub-scan supplies
  the conceptual precedent, not a drug.

---

*Provenance:* structures `simulation-output/protocol-v2.md` + the V4 outputs against a modality grid; reuses
the feasibility (ADR-0003), attrition (ADR-0013), transferability (ADR-0014), V4-expansion (ADR-0006),
host-biology (ADR-0005), and driver-uncertainty (ADR-0008) layers. External anchors verified live (SARC028
PMID 28988646; T-VEC FDA Oct 2015 / OPTiM; ILP TNF-α+melphalan EU 1998, PMID 18066703; arsenic trioxide FDA
2000 / APL; Issels et al. *Lancet Oncol* 2010;11:561–570 / NCT00003052 `[PMID VERIFY]`). **No fabricated
citations; no modality asserted effective in CIC-DUX4.**

*Decision record:* adopted via [ADR-0018](../docs/adr/0018-therapeutic-modality-layer.md) (issue #33).
Not medical advice. Research simulation / hypothesis generation only.
