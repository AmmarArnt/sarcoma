# Cell-of-Origin Specialist — "The Target Hardware"

**Team:** Tumorigenesis / Cell-of-Origin Reverse-Engineering Team
**Angle:** Which cell is the permissive substrate for a CIC-DUX4 build, and why.
**Framing:** This is the *forward* (construction) question — "steps to reproduce a CIC-DUX4 sarcoma cell from a normal cell" — used to reverse-engineer each build step into an intervention point. **Hypothesis-generation research only. Not medical advice, not a treatment plan.**

---

## One-line summary + confidence

The load-bearing substrate is most plausibly an **immature mesenchymal / osteochondrogenic progenitor (an MSC-like cell) caught in an early, undifferentiated, highly proliferative, broadly-open-chromatin state** — *not* a terminally differentiated cell, which the same fusion tends to **kill rather than transform**; the human cell of origin remains formally unproven. **Confidence: moderate** (multiple concordant mouse models + transcriptomic concordance, but no direct human lineage-tracing; the embryonic/totipotency window is inference from DUX4 biology, tier-mixed).

---

## Forward build step(s) I own — "steps to reproduce"

These are the steps applied to the **substrate cell** (the hardware), upstream of the fusion's transcriptional rewiring that other specialists own.

### Build Step CoO-1 — Start from a mesenchymal / osteochondrogenic progenitor, not a differentiated cell
- **Action:** Select an immature MSC-like mesenchymal progenitor (limb-bud / osteochondrogenic lineage) as the chassis.
- **Mechanism:** Ectopic CIC-DUX4 in murine embryonic mesenchymal cells (eMC, MSC-marker-overlapping) produces aggressive undifferentiated small-round-cell sarcoma whose transcriptome (PEA3/ETS family, Ccnd2, Etv4/5) is concordant with human CDS. Osteochondrogenic progenitors transform with high efficiency. The fusion's HMG-box still binds normal CIC/ETS addresses; only a chromatin context where those addresses are *poised* lets the inverted (activating) output take hold.
- **Evidence tier:** **Preclinical-Animal** (mouse mesenchymal transformation + transcriptomic concordance with human tumors).
- **Citation:** Yoshimoto, Tanaka, Homme, … Antonescu, Nakamura. *CIC-DUX4 Induces Small Round Cell Sarcomas Distinct from Ewing Sarcoma.* Cancer Res 2017;77(11):2927–2937. DOI 10.1158/0008-5472.CAN-16-3351; PMC5488331. (PMID likely 28404587 [VERIFY] — two candidate numbers surfaced.)
- **Corroboration (GEMM):** Hendrickson, Oristian, … Linardic, Kirsch. *Spontaneous expression of the CIC::DUX4 fusion oncoprotein from a conditional allele potently drives sarcoma formation in genetically engineered mice.* Oncogene 2024;43(16):1223–1230. DOI 10.1038/s41388-024-02984-8; PMID 38413794. (Three conditional models develop sarcoma + metastasis; relevant because tumors arose readily from the engineered mesenchymal compartment.) **Preclinical-Animal.**

### Build Step CoO-2 — Hit the developmental window: high-proliferation, open/bivalent chromatin
- **Action:** Express the fusion while the progenitor is in an actively proliferating, bivalent-chromatin (H3K4me3 + H3K27me3) state — i.e., during the adolescent growth surge.
- **Mechanism:** CIC-DUX4 is a potent transcriptional activator that works **through p300/CBP** to deposit H3K27ac and build de novo super-enhancers at ETV4/ETV5; this requires chromatin that is permissive (poised/open) for the activator to convert. Rapidly dividing growth-plate/periosteal mesenchyme has the proliferation, the open chromatin, and high TopoII activity (the same activity that creates the transient DSBs enabling the t(4;19)/t(10;19) translocation in the first place). This couples *when the fusion can form* to *when the cell can be reprogrammed by it* — a single window explanation for the AYA age peak.
- **Evidence tier:** **Preclinical-Cell / Mechanistic** for the chromatin/p300 requirement; **Theoretical** for the specific "adolescent window" timing claim in humans.
- **Citation (p300/CBP-dependent activation & super-enhancers):** Bakaric, Cironi, … Rivera, Riggi. *CIC-DUX4 Chromatin Profiling Reveals New Epigenetic Dependencies and Actionable Therapeutic Targets in CIC-Rearranged Sarcomas.* Cancers 2024;16(2):457. DOI 10.3390/cancers16020457; PMC10814785. **Preclinical-Cell.**
- **Window/3D-proximity timing:** `[no direct citation; mechanism inferred from {general recurrent-translocation 3D-proximity biology (docs/03), TopoII-DSB biology, and the AYA epidemiology of CDS}]`. **Theoretical.**

### Build Step CoO-3 — Keep the cell in a "reprogrammable, not apoptotic" state (the kill-switch must be disarmed)
- **Action:** Ensure the substrate tolerates a DUX4-driven embryonic-like program instead of dying from it — i.e., an immature cell whose apoptotic response to the DUX4 transactivation domain is blunted/compatible.
- **Mechanism:** DUX4 is a cleavage-stage embryonic-genome-activation factor, normally silenced in soma; when forced into **differentiated** cells (FSHD muscle, nasal precursors) its transactivation domain drives an embryonic/stem-like program **incompatible with the differentiated identity → MYC-stabilization, dsRNA accumulation, apoptosis**. The CIC-DUX4 fusion carries that same potent DUX4 C-terminal transactivation domain. So the substrate must be a cell whose state is *closer to* the embryonic program DUX4 evokes (less identity conflict, intact proliferative/survival wiring), letting the output **reprogram rather than kill**. Frequent co-deletion of CDKN2A in human CDS plausibly further lowers the apoptotic/senescence barrier.
- **Evidence tier:** **Preclinical-Cell / Mechanistic** (DUX4 lethality in differentiated cells is well-shown; the "permissive immature state survives it" is inference, not a direct CIC-DUX4 survival assay across lineages).
- **Citation (DUX4 apoptosis in somatic/differentiated cells):** Shadle et al. *DUX4-induced dsRNA and MYC mRNA stabilization activate apoptotic pathways in human cell models of FSHD.* PLoS Genet 2017;13(3):e1006658. DOI 10.1371/journal.pgen.1006658. **Preclinical-Cell** (FSHD context — **transfer flag:** evidence is DUX4-alone in muscle, not the CIC-DUX4 fusion in mesenchyme).

---

## Reverse-engineering note — which attack vector "undoes" each build step

| Build step (forward) | The "undo" | Covered by | Gap / forward hypothesis |
|---|---|---|---|
| CoO-1: progenitor chassis | Force lineage commitment so the chassis no longer reads as permissive | **V3 (Hot-Patching / differentiation)** — differentiation therapy is conceptually the direct inverse | Partial. V3 targets the *established* tumor's stuck state, not "harden the at-risk progenitor." No vector pushes pre-malignant progenitor differentiation as prophylaxis (**inherently not a treatment** — flag as concept-only). |
| CoO-2: open/bivalent chromatin + p300/super-enhancers | Collapse the activating chromatin (p300/CBP, BRD4/BET, EZH2 rebalancing) | **V1 (Rate-Limiting)** + **V3 (epigenetic)** — BETi/p300i/EZH2i all live here | Well-covered for the tumor. **Gap:** the *3D-proximity / TopoII window* that lets the translocation form at all is targeted by **no vector** (you cannot ethically intervene there) → record as mechanistic insight only. |
| CoO-3: apoptosis disarmed / reprogrammable state | Re-arm the kill-switch — restore the DUX4-incompatibility lethality or CDKN2A axis | **V3 (synthetic-lethality)**; partially **V1** | **Gap (forward hypothesis):** deliberately *re-imposing* the differentiated-cell context that makes DUX4 lethal (push the tumor toward an identity its own fusion cannot tolerate) — a "force the conflict" differentiation/ICD angle. **Theoretical.** Note V4 relevance: DUX4-driven dsRNA → potential immunogenic-cell-death / danger signal (links to V4 expansion). |

**Net:** the chromatin step (CoO-2) is the most thoroughly mirrored by existing vectors; the **chassis/identity step (CoO-1) and the disarmed-kill-switch step (CoO-3) are the least covered** — the strongest forward-hypothesis territory from this angle.

---

## Model parameters for the Boolean transformation sim

Discrete state variables this step contributes:

```
progenitor_state    ∈ {differentiated, committed_progenitor, permissive_MSC}
developmental_window: bool        # high-proliferation, open/bivalent-chromatin growth surge
chromatin_poised:    bool         # bivalent/open at ETV4/ETV5 + p300/CBP available
apoptosis_disarmed:  bool         # DUX4-program tolerated (e.g., immature state and/or CDKN2A-low)
```

**Pass rule for "substrate is permissive" (`substrate_ok`):**
```
substrate_ok = (progenitor_state == permissive_MSC)
               AND developmental_window
               AND chromatin_poised
               AND apoptosis_disarmed
```
**Transformation gate (combine with fusion-expression node owned by other specialists):**
```
transform = substrate_ok AND fusion_active
# if progenitor_state == differentiated AND fusion_active  -> outcome = cell_death (not transform)
```
Intended use: a differentiated substrate or a closed-chromatin/armed-apoptosis state should route to **death/no-transform**, reproducing the load-bearing asymmetry. (Sets up cleanly against sims/03 Boolean/ODE model.)

---

## What I could not establish (honest)

- **The human cell of origin is not proven.** All direct transformation evidence is **mouse mesenchymal/osteochondrogenic**; no human lineage-tracing exists. "MSC-like" is an inference from transcriptomic concordance, not identity.
- **Neural-crest origin:** I found **no verified primary evidence** supporting a neural-crest cell of origin for CIC-DUX4 sarcoma; the literature I could verify points to mesenchymal/osteochondrogenic progenitors. I am not asserting neural crest is excluded — only that I could not substantiate it.
- **The "adolescent developmental window" timing** is epidemiology + mechanism, not a demonstrated cell-state measurement in human at-risk tissue (**Theoretical**).
- **CoO-3 (reprogram-vs-kill threshold)** is inferred by transferring DUX4-alone FSHD/nasal-precursor apoptosis data onto the CIC-DUX4 fusion in mesenchyme — **not** a direct cross-lineage survival assay of the fusion. Concentration/context mismatch flag applies.
- **Exact Yoshimoto 2017 PMID** carries a `[VERIFY]` (two candidate numbers); DOI/PMC are verified.
- **Atypical-case flag (~5%):** ~5% of clinically/histologically CIC-rearranged tumors lack a confirmed fusion. Build steps CoO-2/CoO-3 (chromatin state, apoptosis threshold) are **fusion-agnostic and still plausibly relevant**; CoO-1 framed around the *CIC-DUX4* fusion specifically may not apply to fusion-unconfirmed cases.

---

## Falsifiers — what would prove this wrong

1. **Lineage tracing / single-cell** of human CDS that maps origin to a **differentiated or non-mesenchymal** lineage (e.g., neural crest) would falsify the MSC-progenitor chassis claim (CoO-1).
2. A controlled experiment showing CIC-DUX4 transforms **terminally differentiated** cells **as efficiently as** progenitors (no death asymmetry) would falsify the "differentiation is a defense" thesis (CoO-3) and break the model's death-routing rule.
3. Demonstrating CDS arises with equal efficiency **outside** the proliferative/open-chromatin window (e.g., quiescent, closed-chromatin cells transform readily) would falsify the developmental-window requirement (CoO-2).
4. Showing CIC-DUX4 activation is **p300/CBP- and super-enhancer-independent** (transforms with closed chromatin) would falsify the chromatin-poised requirement.
5. Forcing a permissive progenitor to **differentiate before** fusion expression and still getting efficient transformation would falsify the "harden-the-chassis" reverse-engineering claim.
