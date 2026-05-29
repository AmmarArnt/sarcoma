# Target System States — the Two Microservices and the Selective-Clearance Contract

This is the conceptual deliverable: instead of "poison anything that divides" (cytotoxics), define
the **state the sarcoma cell must reach** and the **state the immune system must reach** so that the
immune system *selectively* removes the tumor cell — with minimal reliance on DNA-damaging chemo.
Grounded in the Boolean model (`immune_state_model.py`), the real CIC-DUX4 on/off data (Sim 1),
and verified mechanism citations.

---

## The reframing: clearance is a handshake, not a poisoning

A cytotoxic kills any cell emitting the "I am proliferating / damaged" pattern — coarse and
collateral. The immune system is a *selective* garbage collector: it removes a cell only when a
**two-sided contract** is satisfied. Both microservices must reach a compatible state at the same time:

```
   SARCOMA microservice                IMMUNE microservice
   (must become identifiable      <->  (must be armed, unbraked,
    AND stop dividing)                  and licensed to act)
                       \            /
                        SELECTIVE CLEARANCE
                     (cell removed, neighbours spared)
```

If only one side is satisfied, nothing happens:
- **Strangle only** (stop dividing, no immune engagement) → the model returns *"strangled but not
  collected"*: a non-dividing cell that just sits there.
- **Immune only** (release checkpoints, arm NK, but the cell stays invisible/braked) → *"GC active
  but nothing to grab"*.

The whole point is to drive **both** services into compatible states.

---

## A) Target state of the SARCOMA microservice: "identifiable AND out of the loop"

Two sub-states, either of which (ideally both) makes the cell a clearance target.

### A1. Identify itself to the immune system (become visible)
The fusion enforces invisibility. Real CIC-DUX4 data (GSE60740, Sim 1) shows the fusion **suppresses
the MHC-I master switch NLRC5 (−2.55)** and its targets (TAP1 −1.57, B2M −0.53, HLA-A −0.59, PSMB9,
ERAP2), while keeping **PD-L1 low** and **HLA-E low**. So the evasion is *"going dark"* (MHC-I-low),
not *"raising a shield"* (PD-L1-high).

Target visibility state — reach **either**:
- **T-cell-visible:** restore the antigen-presentation stack → **NLRC5 ↑ → MHC-I / B2M / TAP ↑**.
  Levers: epigenetic priming (EZH2i/HDACi/DNMTi — and note Sim 2 showed EZH2 is *not* a survival
  dependency, so tazemetostat's real job here is priming, not killing) and CDK4/6 inhibition
  (raises antigen presentation via DNMT1↓→ERV-dsRNA→interferon — Goel, *Nature* 2017, PMID 28813415;
  NLRC5 = CITA, PNAS 2016 PMID 27162338).
- **NK-visible (missing-self / stress):** if MHC-I *cannot* be restored (e.g., genetic **B2M loss**),
  the MHC-I-low state itself is an NK "missing-self" signal, **and** senescence raises NKG2D ligands
  (**MICA/ULBP2**; Aging 2016 PMID 26878797). The fusion already keeps **HLA-E low** (less NKG2A
  braking) — favorable. This is the fallback route when antigen presentation is irreversibly off.

### A2. Get out of the infinite loop / stop dividing (the strangler pattern)
The bug is `while True: divide()`. Two non-cytotoxic ways to exit:
- **Cytostatic arrest → senescence (the strangler):** block the execution gate so the cell stops
  adding new cycles. **CDK4/6 inhibition** clamps CDK4 → RB stays active → E2F off → cell-cycle exit;
  sustained, this becomes **senescence**. In software terms: stop writing new code around the legacy
  module; freeze it. Senescence is not inert — it **flags the cell for NK clearance** (NKG2D ligands),
  i.e., the frozen legacy module becomes safe to garbage-collect.
- **Differentiation (terminal exit):** force the cell down a differentiation path (p21/p27 ↑, permanent
  cycle exit). The APL/ATRA existence proof; thin in fusion sarcomas, but the *state* is the goal.

**Why "stop dividing" alone is not enough (key insight):** in the model, strangling (CDK4/6i, Diff,
BETi — alone or combined) reaches `Prolif=0` but `Cleared=0` — *"strangled but not collected."* The
strangler pattern only completes when the immune garbage collector removes the retired cell. So A2
must be paired with the immune microservice reaching its target state, below.

---

## B) Target state of the IMMUNE microservice: "armed, unbraked, licensed"

The collector must be (1) present, (2) un-exhausted/unbraked, and (3) licensed by the right ligand balance.

1. **Effectors present:** tumor-reactive **T cells** (need the neoantigen + MHC-I) and/or **NK cells**
   (circulating; boostable by IL-15 superagonist / adoptive NK). For this fusion-unconfirmed patient,
   the T-cell neoantigen is uncertain → the **NK arm is the more robust bet**.
2. **Brakes released — and the NECTIN axis is the load-bearing gate.** CD155/CD112 nectins (CD112 is
   *up* in the data) engage **activating DNAM-1 (CD226)** *and* **inhibitory TIGIT**. In the model,
   **αTIGIT is required in every minimal clearance solution** — without it, TIGIT engagement zeroes
   DNAM-1 activation and neither T nor NK can kill. PD-1/PD-L1 blockade is needed *only* on the T-cell
   route (PD-L1 is IFN-induced once priming starts); it does not gate NK.
3. **Suppression lifted:** the immunosuppressive TME (Treg/MDSC) must be relieved. CDK4/6 inhibition
   **suppresses Treg proliferation** (Goel 2017) — so the same drug that strangles the cell also
   de-represses the collector. HLA-E (NKG2A brake) is already low in this tumor.

---

## The minimal compatible states the model found (no DNA damage)

| Route | Sarcoma state | Immune state | Minimal levers |
|---|---|---|---|
| **NK / senescence-surveillance** | arrested→senescent; NKG2D ligands up; (MHC-I-low OR restored) | NK present; TIGIT brake off; Treg suppressed; HLA-E low | **CDK4/6i + αTIGIT** (2 agents, no chemo) |
| **T-cell** | MHC-I restored (NLRC5↑); arrested | T cells present; TIGIT + PD-1 brakes off; Treg suppressed | CDK4/6i + αTIGIT + αPD1 (+EZH2i priming) |
| **B2M-lost fallback** | MHC-I impossible; senescent → NKG2D ligands | NK; TIGIT off; Treg off | **CDK4/6i + αTIGIT** (T-cell route dead; NK still clears) |

**CDK4/6 inhibition is the keystone non-cytotoxic agent** — it appears in every solution because it
does three jobs at once: strangles the loop (cytostasis→senescence), makes the cell visible
(antigen presentation up + NKG2D ligands via senescence), and frees the collector (Treg down). It is
also independently nominated by Sim 1 (signature reverser) and Sim 2 (CDK4 = most Ewing-selective
dependency). The **nectin/TIGIT axis (αTIGIT)** is the second indispensable lever.

---

## Answers to the three questions

- **"How do I get the cell to identify itself?"** Re-express the MHC-I stack by lifting the fusion's
  NLRC5 suppression (epigenetic priming and/or CDK4/6i-driven interferon) for the T-cell route; or
  drive senescence to raise NKG2D ligands for the NK route. Keep HLA-E low (it already is).
- **"How does it get out of the infinite loop / stop dividing?"** Block the execution gate (CDK4/6i →
  RB-active → E2F-off) or force differentiation — non-cytotoxic cytostasis, not poisoning.
- **"Strangler pattern — stop dividing until the old code can be safely discarded."** Exactly the
  CDK4/6i→senescence→**NK-mediated clearance of senescent cells** path: freeze the legacy module, let
  it acquire the "remove me" tags (NKG2D ligands), and let the immune garbage collector retire it.
  The model confirms the strangle step alone leaves the cell *uncollected* — the collector
  (B-state) must be engaged for the pattern to complete.

---

## Honest caveats
- Qualitative Boolean model; binary states; shallow loops resolved by ordered evaluation. Not a
  quantitative or temporal predictor.
- Mechanism edges are real but transferred: CDK4/6i-immunity is breast-cancer data (Goel 2017);
  senescence→NK surveillance is fibroblast/other models; TIGIT/nectin biology is general, not
  CIC-DUX4-validated. CD112-up / NLRC5-low / HLA-E-low are from one CIC-DUX4 cell line (IB120,
  transcript-level).
- "CDK4/6i + αTIGIT" is a model-generated *hypothesis*, not a regimen; CDK4/6i + immunotherapy combos
  are experimental and have their own toxicity profile. Clinical decisions belong to the oncologist.
- This complements, not replaces, the cytotoxic backbone; it maps a route to lean *less* on it.
