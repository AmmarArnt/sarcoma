# Discussion Brief — Non-Cytotoxic Selective Immune Clearance ("NK-first") in CIC-DUX4 Sarcoma

**Prepared:** 2026-05-29 · **For:** discussion with treating oncologist / molecular tumor board
**Status:** Research-simulation hypothesis. **Not medical advice.** No recommendation to start, stop, or
combine any drug. Companion to the WEE1+ifosfamide brief (the *cytotoxic* route); this is the
*low-cytotoxic, immune-selective* route. Citations are real and verifiable.

---

## Patient context (1 line)
Soft-tissue CIC-rearranged sarcoma (fusion **not** confirmed — atypical ~5% subgroup), oligometastatic
lung relapse after VDC/IE + surgery + whole-lung irradiation, now on high-dose ifosfamide.

## The idea (1 line)
Rather than only poisoning dividing cells, drive the tumor cell into a state where the immune system
**selectively** removes it: **stop it dividing (strangler), make it visible, release the nectin/TIGIT
brake, and arm NK cells — NK-first.** A forward hypothesis for *if/when* cytotoxic options are limited.

## Why this tumor is a candidate (real data)
From the CIC-DUX4 expression contrast (GEO GSE60740, fusion on vs knockdown), the fusion enforces
**immune invisibility**: it suppresses the MHC-I master switch **NLRC5 (−2.55)** and its targets
(TAP1 −1.57, B2M −0.53, HLA-A −0.59), keeps **PD-L1 low**, **HLA-E low** (less NK braking), and
**CD112/Nectin-2 up**. So evasion is "going dark," not "raising a shield" — which means (a) checkpoint
blockade alone is unlikely to help, and (b) the **MHC-I-low state is itself an NK target** (missing-self).

## The mechanism / state to reach (the "handshake")
Selective clearance needs the tumor cell **and** the immune system in compatible states at once:
- **Tumor:** proliferation OFF (cytostasis → senescence) **and** visible — MHC-I restored (NLRC5↑) for
  T cells, or NKG2D ligands (MICA/ULBP2) via senescence for NK.
- **Immune:** NK/T effectors present, Tregs suppressed, and the **nectin/TIGIT brake released** so
  CD155/CD112 → activating DNAM-1 (CD226) dominates.

## Candidate components (and their mechanistic jobs)
- **CDK4/6 inhibitor (palbociclib/ribociclib/abemaciclib)** — the keystone: stops the cycle (RB-active
  → senescence = the "strangler"), **raises antigen presentation and suppresses Tregs** (Goel, *Nature*
  2017, PMID 28813415), and senescence flags the cell for NK clearance (NKG2D ligands; Aging 2016,
  PMID 26878797). FDA/EMA-approved in HR+ breast; **experimental in sarcoma**.
- **IL-15 superagonist (N-803 / Anktiva)** — arms NK (and CD8) cells. **FDA-approved 2024** for
  BCG-unresponsive NMIBC (intravesical); systemic/solid-tumor use is **experimental**.
- **Nectin/TIGIT-axis modulation** — the model's indispensable gate. **Honest caveat:** the lead
  anti-TIGIT (tiragolumab) **failed multiple Phase 3 trials** (SKYSCRAPER-01/03; programs scrapped) —
  so TIGIT blockade is biologically motivated but **clinically unproven**; alternative axis modulation
  (other anti-TIGIT, anti-CD96, DNAM-1-sparing) is earlier still.
- **EZH2 inhibitor (tazemetostat)** — optional MHC-I *priming* (not as a cytotoxic; CRISPR shows EZH2
  is not a survival dependency). FDA-approved for epithelioid sarcoma; off-label here.
- **Anti-PD-1 (pembrolizumab/nivolumab)** — only needed to open the T-cell arm once priming induces
  PD-L1; sarcoma monotherapy responses are modest (SARC028).

## What the in-silico work showed (5 simulations, this repo)
- **Selective, DNA-damage-free clearance is reachable** in the model (32/128 non-cytotoxic combos).
- **Minimal route: CDK4/6i + nectin/TIGIT-release**, via NK/senescence — robust even under **B2M loss**
  (when T-cell recognition is impossible, NK still clears).
- **Order matters — NK-first** clears fastest by using the existing MHC-I-low window; **checkpoint-first
  never works**; **"strangle only" stops division but does not clear** (the immune collector must be engaged).
- CDK4/6i is independently nominated by the drug-signature and CRISPR-dependency simulations too.

## Suggested sequence (hypothesis, not a regimen)
**NK-first:** cytostasis/senescence + NK arming + nectin-gate release → exploit missing-self early →
**then** open the T-cell arm (priming ± anti-PD-1) as the second wave. Repair the **host** NK
compartment (fitness/IL-15) — clearance is a property of the whole system, not one drug.

## Questions for the oncologist / molecular tumor board
1. Can the **relapse lesion be profiled** for MHC-I/B2M (intact vs genetically lost), HLA-E, PD-L1,
   TILs, and the **nectin/TIGIT axis (CD155, CD112)** — to choose the T-cell vs NK route?
2. Is **B2M intact**? If lost, prioritize the **NK route** (T-cell approaches won't work).
3. Are there **trials** combining a CDK4/6 inhibitor with immunotherapy, or **IL-15 / NK-directed**
   trials (NK engagers, adoptive NK), open to sarcoma / AYA / tumor-agnostic baskets?
4. Given the **anti-TIGIT Phase 3 failures**, is any nectin-axis modulation worth pursuing only in a trial?
5. Does the **prior whole-lung irradiation** (radiation-primed/STING context) make the lung lesion a
   better immune-priming site?

## When this becomes most relevant
**If response to ifosfamide alone is limited** — as a non-cytotoxic, selective strategy to take to a
molecular tumor board and to match against open immunotherapy/CDK4/6i/NK trials.

## Honest limitations
The *state/sequence* logic is well-grounded; the *drugs* are a mixed bag — CDK4/6i and IL-15-SA and
EZH2i are approved in other indications, anti-PD-1 is modest in sarcoma, and **anti-TIGIT has largely
failed clinically.** All components are experimental in CIC-DUX4, carry real toxicity, and combinations
are unproven. Mechanism edges are transferred from other tumor types and a single CIC-DUX4 cell line.
This complements — does not replace — the standard backbone. Clinical decisions belong to the oncologist.

## Provenance
Multi-agent CIC-DUX4 research simulation; in-silico analyses in `sims/` of this repository.
Verified citations: GSE60740 (real expression data); Goel *Nature* 2017 (PMID 28813415); senescence→NK
(PMID 26878797); HLA-E escape (Nat Commun 2019); NLRC5/CITA (PMID 27162338); N-803 FDA approval 2024;
SKYSCRAPER anti-TIGIT Phase 3 failures (2024–2025). Verify all before clinical use.
