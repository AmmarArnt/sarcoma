# Sim 4 — Immune-Clearance + Cell-State Model — RESULTS

**One-line:** Extends the network model with **nectins + immune markers** to ask not "how do we poison
the cell" but "what state must the sarcoma cell and the immune system each reach for *selective*
clearance, with minimal cytotoxics." Result: **DNA-damage-free clearance is reachable**, the minimal
route is **CDK4/6i + αTIGIT** (NK/senescence-surveillance), and "stop dividing" alone is necessary but
**not** sufficient. Full systems framing in `STATES.md`.

**Confidence: low-medium (qualitative).** Hypothesis generator, not a quantitative predictor.
Baseline cell-state anchored to real CIC-DUX4 data (GSE60740); mechanism edges cite real papers;
assumptions labelled. Not medical advice.

## Model
Boolean model coupling the oncogenic loop, a **cell-state/strangler axis** (cytostasis→senescence,
differentiation), a **visibility module** (NLRC5→MHC-I/B2M/TAP; PD-L1; HLA-E; NKG2D ligands), the
**nectin/DNAM-1–TIGIT axis** (CD155/CD112 → activating CD226 vs inhibitory TIGIT), and an **immune
effector layer** (T-cell and NK kill rules; Treg suppression). Parameters encode host/tumor context
(B2M intact?, Treg/TIGIT high, nectin ligand present, HLA-E low, effectors present). Code:
`immune_state_model.py`; full scans: `scan_b2m_intact.csv`, `scan_b2m_lost.csv`.

Baseline anchored to **real data** (Sim 1, GSE60740, fusion-ON): NLRC5/MHC-I low, PD-L1 low,
HLA-E low, CD112(nectin) up.

## Key results
- **Baseline (disease state):** `Prolif=1`, MHC-I=0, DNAM blocked, ImmuneKill=0. Dividing and invisible.
- **Non-cytotoxic clearance is achievable:** **32 of 128** non-cytotoxic intervention combinations
  reach the target state (`Cleared AND not Prolif`) — **with no DNA-damage input.**
- **Minimal solution: `CDK4/6i + αTIGIT`** (2 agents) via the **NK / senescence-surveillance** route
  (senescence→NKG2D ligands; TIGIT brake released; Treg suppressed by CDK4/6i; HLA-E low).
- **T-cell route** needs more: `CDK4/6i + αTIGIT + αPD1` (PD-L1 is IFN-induced once priming starts;
  MHC-I restored via CDK4/6i→IFN→NLRC5, optionally reinforced by EZH2i/HDACi priming).
- **"Strangle only" is not enough:** CDK4/6i, Diff, BETi (alone or combined) give `Prolif=0` but
  `Cleared=0` → **"strangled but not collected."** Stopping division must be paired with immune engagement.
- **"Immune only" is not enough:** αPD1+αTIGIT(+NKarm) without visibility/arrest → `MHC-I=0`,
  `Cleared=0` → "GC active but nothing to grab" (also: Treg stays active without CDK4/6i).
- **B2M-loss scenario:** T-cell route clears in **0** combos (antigen presentation genetically off),
  but **`CDK4/6i + αTIGIT` still clears via NK** — the NK arm is the antigen-loss fallback.

## The nectin finding (per the directive to include nectins)
**αTIGIT is required in every minimal clearance solution.** Because CD112 (and CD155) are present
(CD112 up in the data) and engage inhibitory **TIGIT**, the DNAM-1 activating signal is netted out
unless TIGIT is blocked — so the nectin/TIGIT axis is the **load-bearing gate** for both T-cell and
NK killing. Measuring tumor **CD155/CD112 and TME TIGIT** is therefore a decision variable, not a detail.

## Convergence across all four simulations
| Lever | Sim 1 (signature) | Sim 2 (dependency) | Sim 3 (loop dynamics) | Sim 4 (immune-state) |
|---|---|---|---|---|
| **CDK4/6i** | palbociclib reverser | CDK4 most Ewing-selective | cytostatic gate | **keystone: strangler + visibility + Treg-down** |
| **EZH2i** | — | not a survival dependency | — | **MHC-I priming, not cytotoxic** |
| **nectin/αTIGIT** | — | — | — | **indispensable clearance gate** |
| **WEE1+ifosfamide** | — | strong (pan-essential) | only robust *cytotoxic* collapse | (the cytotoxic alternative this sim aims to lean off) |

The picture: **WEE1+ifosfamide** is the potent *cytotoxic* route; **CDK4/6i + αTIGIT (± priming/αPD1)**
is the model's *selective, low-cytotoxic* route — strangle the loop, let senescence flag the cell,
and let NK/T cells do the selective removal.

## Caveats
See `STATES.md`. Qualitative model; transferred mechanism edges (CDK4/6i-immunity = breast; senescence-
NK = fibroblast/other; TIGIT/nectin = general, not CIC-DUX4-validated); single-cell-line baseline data;
"CDK4/6i + αTIGIT" is a hypothesis, not a regimen; combos are experimental with real toxicity.

## Grounding (OpenMed NER, team `v4-lead`)
`grounding.tsv`: nectin/immune entities recognized — CD112, CD155, CD226/DNAM-1, TIGIT, NECTIN2, PVR,
NLRC5, B2M, HLA-A, HLA-E, MICA, ULBP2, PD-L1/CD274, plus NK cell & regulatory T cell (as cells) and
senescence. No unrecognized targets.

## Reproduce
`/Users/ammararnautovic/code/sarcoma/.venv/bin/python immune_state_model.py`
