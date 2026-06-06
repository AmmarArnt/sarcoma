# Sim 07 — HLA-E / NKG2A Escape Valve of Epigenetic MHC-I Restoration

**Tests V4 Forward Hypothesis 3** (`simulation-output/protocol-v2.md` FH-3; `v4-summary-v2.md`):

> *EZH2i/HDACi restore classical MHC-I but may **co-induce HLA-E**, re-suppressing both the NK arm
> relied on earlier AND the new CD8 arm (via CD94/NKG2A) — so pair MHC-I restoration with anti-NKG2A
> (monalizumab), not anti-PD-1 alone.*

**Engine.** Boolean hypothesis generator that **extends Sim 04** (`sims/04-immune-state-model/`).
Sim 04 treats HLA-E as a static favorable parameter (`HLA_E=0`), so it structurally cannot represent
FH-3. Sim 07 makes HLA-E a **dynamic node coupled to MHC-I restoration**, adds two candidates
(`aNKG2A` = monalizumab-class; `Tdeplete` = an IFN-free Treg-depletion lever), and applies the
HLA-E/NKG2A brake to **both** the NK and the CD8 effector arms. Qualitative, not quantitative; no
fabrication. Baseline CIC-DUX4 cell-state inherited unchanged from Sim 04 (anchored to GSE60740 /
Sim 01: fusion ON ⇒ MHC-I/B2M/NLRC5 low, HLA-E low, CD112/nectin up).

Reproduce: `python3 sims/07-hlae-escape-valve/hlae_escape_valve.py`
(needs `pandas`; in the project venv use `.venv/bin/python`).

---

## The new coupling edge (and its honest evidence tier)

| Edge added vs Sim 04 | Statement | Tier | Source |
|---|---|---|---|
| classical-MHC-I → HLA-E surface | HLA-E reaches the surface only as an MHC-I molecule (needs B2M) **and** needs a VL9 leader peptide derived from classical HLA-A/-B/-C signal sequences. Restoring classical MHC-I therefore *supplies HLA-E's own stabilizing ligand*. | **Established** (general immunology) | Braud *Nature* 1998 (HLA-E↔CD94/NKG2A) https://www.nature.com/articles/35869 ; VL9 leader dependence PMC10690437 ; review PMC11254306 |
| IFN → HLA-E | IFN-γ transcriptionally upregulates HLA-E (documented NK-resistance route, e.g. HLA-E/NKG2A resistance to BCG in NMIBC). | **Clinical-correlative** | PMC11398371 |
| anti-NKG2A lifts the brake | monalizumab-class blockade disrupts NKG2A:HLA-E. | **Clinical-Trial** | review PMC11254306 |
| **EZH2i specifically co-induces HLA-E in CIC-DUX4** | the load-bearing premise of FH-3 | **Mechanistic / Theoretical — INFERRED, not established** | inferred from the two edges above; *no* direct CIC-DUX4 (or EZH2i-specific HLA-E) data found this session |
| Treg depletion independent of CDK4/6i (`Tdeplete`) | metronomic low-dose cyclophosphamide / anti-CTLA-4 deplete Treg without inducing tumor IFN | Preclinical-Animal / Clinical | Ghiringhelli metronomic-CTX Treg depletion; anti-CTLA-4 intratumoral Treg depletion [VERIFY PMIDs before external use] |

`[VERIFY]` items are perishable / not live-verified to PMID this session — re-check before external use.

---

## Results

### Q1 — Parity with Sim 04 — **PASS**
With the coupling OFF and the two new drugs removed from the pool, Sim 07 reproduces Sim 04's
`Prolif / MHCI / Tcell_kill / NK_kill / Cleared / TargetState` **identically across all 128 combos**.
The extension is faithful; every divergence below is attributable to the HLA-E coupling, nothing else.

### Q2 — The escape valve is real and anti-NKG2A is load-bearing
| Metric | Coupling OFF | Coupling ON |
|---|---|---|
| Combos reaching TargetState (arrested **and** immune-cleared) | **176 / 512** | **100 / 512** |
| Routes lost to the HLA-E/NKG2A brake | — | **76** |
| Surviving routes that contain **anti-NKG2A** | — | **88 / 100 (88%)** |
| Surviving routes **without** anti-NKG2A | — | **12** |

The 12 anti-NKG2A-free survivors **never restore MHC-I and never induce IFN** (verified
programmatically: `restore MHC-I / induce IFN? = False`). They are exactly the *stay-cold* NK
missing-self routes — the only way to clear under coupling without monalizumab is to **not** trip
HLA-E in the first place.

The EpiPrime (MHC-I-restoration) route dissected (Treg handled by the IFN-free `Tdeplete`, so HLA-E
is the only moving part):

```
EpiPrime+aPD1+aTIGIT+Tdeplete            MHCI=1 HLA_E=1 brake=1  -> BLOCKED by HLA-E/NKG2A (no kill)
EpiPrime+aPD1+aTIGIT+Tdeplete+aNKG2A     MHCI=1 HLA_E=1 brake=0  -> killed (T-cell) but still cycling
EpiPrime+aPD1+aTIGIT+CDK46i+aNKG2A       MHCI=1 HLA_E=1 brake=0  -> TARGET-STATE (arrested + cleared)
```
Restoring MHC-I to "make the tumor visible" simultaneously raises its own NKG2A brake; **the
checkpoint package that worked under Sim 04 (no HLA-E) fails here until anti-NKG2A is added.**

### Q3 — Sequencing: NK-first-while-cold beats restoration-first
```
NK-first, stay HLA-E-low (aTIGIT+NKarm+Tdeplete)   HLA_E=0 brake=0 ImmuneKill=1 via NK
NK-first + CDK4/6i (senescence, but IFN->HLA-E)     HLA_E=1 brake=1 ImmuneKill=0 via none
Restoration-first (EpiPrime, no anti-NKG2A)         HLA_E=1 brake=1 ImmuneKill=0 via none
Restoration-first + anti-NKG2A (FH-3 fix)           HLA_E=1 brake=0 ImmuneKill=1 via T-cell
```
Two non-obvious points:
1. **Even CDK4/6i added to a pure NK route is self-defeating under coupling** — its IFN induction
   raises HLA-E and trips the brake. Any IFN/MHC-I-inducing move forfeits the MHC-I-low advantage.
2. This refines the catalog's "NK-first" ordering: NK-first only stays clean if it stays *IFN-cold*;
   the moment you restore visibility you **must** carry anti-NKG2A.

### B2M-loss contrast — mechanistic validation
Under B2M loss, **0** combos have an active NKG2A brake — because with no surface classical MHC-I
there is no VL9 leader peptide to stabilize HLA-E. Clearance proceeds via the NK missing-self route
(minimal `CDK46i+aTIGIT`), and **anti-NKG2A is irrelevant**. The escape valve is specifically a
liability of the *MHC-I-restoration* path, not of the NK/antigen-loss path — a clean internal check
that the coupling logic behaves mechanistically.

---

## What this changes for the catalog

- **FH-3 is supported in-silico under its own stated premise.** If epigenetic MHC-I restoration
  co-induces HLA-E, then anti-NKG2A is **load-bearing, not optional**, for the V3→V4 MHC-I-restoration
  arm (88% of surviving routes). Pairing EZH2i/HDACi with anti-PD-1 **alone** is predicted to
  under-perform; the pairing should be EZH2i/HDACi **+ anti-NKG2A** (± anti-PD-1).
- **Refines the NK-first ordering** (Sim 05 / FH-1): NK-first wins *only while IFN-cold*; CDK4/6i and
  EpiPrime both forfeit the advantage. "NK-first" should be stated as "NK-first **before any
  IFN-inducing / MHC-I-restoring step**."
- **Gives a falsifiable, measurable signature** (below) and identifies the gating biomarker
  (HLA-E surface response to EZH2i/HDACi) — feeds the VoI layer.

## Falsifier (pre-registered)
CIC-DUX4 lines ± EZH2i/HDACi assayed for surface HLA-A/B/C **and** HLA-E:
- **Hypothesis survives** if classical MHC-I↑ is accompanied by HLA-E↑ **and** adding anti-NKG2A
  increases NK/CTL killing of the restored cells.
- **Hypothesis falsified** if MHC-I↑ occurs **without** HLA-E co-induction, or if anti-NKG2A adds no
  killing — in which case anti-NKG2A is *not* load-bearing and anti-PD-1 pairing suffices.

## Limitations (honest)
- **Boolean, qualitative.** Counts of "routes" are combinatorial bookkeeping, not probabilities or
  effect sizes. The headline is the *direction and dependency structure*, not "88%" as a clinical number.
- **The decisive edge (EZH2i→HLA-E in CIC-DUX4) is inferred, not measured.** Everything rests on
  HLA-E's leader-peptide dependence + IFN-inducibility. Sim 07 makes the *consequence* of that premise
  explicit and testable; it does not establish the premise.
- **No new wet/▢omics data.** This is a logic extension of Sim 04 over cited biology; the only
  experimental data anchor is GSE60740 (via Sim 01/04). No dataset, accession, or value was invented.
- **`Tdeplete` and `aNKG2A` are abstractions** of drug classes, not specific-agent models.
- **HLA-E on CD8:** the brake on the T-cell arm assumes NKG2A⁺ CD8 T cells; NKG2A induction on CD8
  varies with activation state — modeled as present-when-relevant, a simplification.
- **OpenMed NER grounding could not be run in this container** (no `.venv`; `openmed` uses an
  mlx/Apple-Silicon backend). `entities.txt` is prepared; run grounding in a capable environment:
  `python scripts/openmed_ner.py --team v4-lead --text-file entities.txt --format tsv > grounding.tsv`.

*Research-simulation hypothesis only. Not medical advice. No start/stop/dosing guidance.*
