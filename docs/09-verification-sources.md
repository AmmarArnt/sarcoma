# 09 — Authoritative Verification & Cross-Referencing Sources

**Status:** standing reference (framework layer). **Origin:** GitHub issue #9 (@Cerimagic) named a set of
authoritative online sources for clinical-trial and regulatory awareness; this file makes them a
**reusable grounding / fact-checking registry for every future session, simulation, and research task** —
not a one-off used only for the translational-feasibility layer.

> **Not medical advice.** This registry says *where to verify a fact*, not what anyone should do. A
> source confirming that a drug is "approved" or a trial is "recruiting" is a statement about
> *status*, never about benefit for this patient.

---

## 1. What this is (and how it differs from OpenMed NER)

The framework now has **two distinct grounding mechanisms — do not confuse them:**

| Mechanism | Job | Where |
|---|---|---|
| **OpenMed NER** (`docs/07`, `scripts/openmed_ner.py`) | **Entity grounding** — "is *EZH2* / *tazemetostat* a recognized biomedical term?" Confirms the *name*, not the *claim*. | `docs/07-openmed-models.md` |
| **This registry** (`docs/09`) | **Fact verification** — "is tazemetostat *actually still FDA-approved*? Is NCT02389244 *actually recruiting*?" Confirms the *claim/status* against a primary authority. | this file |

NER cannot tell you a drug was withdrawn; only the registries below can. Both run before finalizing —
NER for entity grounding (golden rule via `docs/05`/`docs/07`), these for any **status, approval, trial,
or safety** claim (golden rule #1; `sarcoma-contract` citation rules).

---

## 2. The registry (verify against these; cite source + access date)

All are **canonical, free, primary-or-official** portals as of June 2026. Query them with `WebSearch` /
`WebFetch` (or their public APIs). **Always date-stamp what you read** — status is perishable (§4).

### Clinical-trial status & availability
| Source | Authoritative for | Entry point |
|---|---|---|
| **ClinicalTrials.gov** | US + many international trials: phase, recruitment status, NCT IDs, sites, results | https://clinicaltrials.gov · API v2: https://clinicaltrials.gov/data-api/api |
| **EU CTIS** (Clinical Trials Information System) | EU/EEA trials authorised under the Clinical Trials Regulation (the system that replaced EudraCT for new trials since Jan 2023) | https://euclinicaltrials.eu/ |
| **EU Clinical Trials Register** (legacy EudraCT) | Older EU trials predating CTIS | https://www.clinicaltrialsregister.eu/ |
| **WHO ICTRP** | Global meta-search across national registries (ISRCTN, ANZCTR, jRCT, ChiCTR, etc.) | https://trialsearch.who.int/ |

### Regulatory status, approvals, labels & safety notices
| Source | Authoritative for | Entry point |
|---|---|---|
| **FDA — Drugs@FDA** | US approvals, approval dates, labels | https://www.accessdata.fda.gov/scripts/cder/daf/ |
| **FDA — news / safety / withdrawals** | Approvals, accelerated-approval status, safety communications, market withdrawals | https://www.fda.gov/drugs |
| **EMA** | EU centralised approvals, EPARs, CHMP opinions, referrals & safety | https://www.ema.europa.eu/en/medicines |
| **PMDA (Japan)** | Japanese approvals (relevant where a drug is approved only in Japan, e.g. valemetostat) | https://www.pmda.go.jp/english/ |

### Pharmacovigilance / post-market safety signals
| Source | Authoritative for | Entry point |
|---|---|---|
| **FDA FAERS / MedWatch** | US adverse-event reporting | https://www.fda.gov/safety/medwatch |
| **EU EudraVigilance (adrreports.eu)** | EU adverse-event reporting | https://www.adrreports.eu/ |
| **MHRA Yellow Card** | UK adverse-event reporting | https://yellowcard.mhra.gov.uk/ |

### Literature & accessions
| Source | Authoritative for | Entry point |
|---|---|---|
| **PubMed / PMC** | Peer-reviewed literature; PMID/PMCID verification | https://pubmed.ncbi.nlm.nih.gov/ · https://www.ncbi.nlm.nih.gov/pmc/ |
| **Gene-expression / dependency data** (already used by sims) | GEO, DepMap — see each sim's `MANIFEST.md` | https://www.ncbi.nlm.nih.gov/geo/ · https://depmap.org/ |

---

## 3. How to use it (the standing workflow)

1. **Any claim about approval / trial / safety / withdrawal status → verify against the matching source
   above before asserting it.** This is the operational form of golden rule #1 ("verify accessions
   against live sources").
2. **Record source + access date** (e.g. *"FDA Drugs@FDA, accessed 2026-06-03"*). For trials, record the
   **NCT/EudraCT/CTIS number** and the **recruitment status as of that date**.
3. **If a source is unreachable or ambiguous, tag `[VERIFY]`** — never assert an unconfirmed status.
4. **FDA ≠ EMA ≠ PMDA.** Check the jurisdiction(s) relevant to the question; report divergence (a drug
   approved by only one authority has a different access profile — see the feasibility layer).
5. **Status confirms a *band/tier*, not benefit.** A registry hit supports the `Established` /
   `Clinical-Trial` evidence tier and the feasibility band (`simulation-output/translational-feasibility-layer.md`);
   it is **not** efficacy evidence for CIC-DUX4.

---

## 4. Perishability (why this is a standing, repeated check)

Regulatory and trial status change without any change in biology — the translational-feasibility layer
(ADR-0003) was triggered exactly by one: **tazemetostat was voluntarily withdrawn from all US indications
on 2026-03-09**, three months before that layer was written. Therefore:

- **Do not trust a previously-recorded status across sessions.** Re-verify against these sources each time
  a status claim is load-bearing.
- A status fact in any existing artifact (incl. `protocol-v1.md`, the feasibility layer) carries its
  access date; if the date is old and the fact matters, re-check before relying on it.

---

## 5. Provenance

The trial/regulatory sources here are those **named by @Cerimagic in issue #9** (ClinicalTrials.gov, EU
CTIS, FDA communications, EMA communications, regulatory approvals & safety notices, recruiting status)
plus the registries actually used to build the translational-feasibility layer (PubMed/PMC, PMDA for
Japan-only approvals, the pharmacovigilance portals used by the mRNA team). Literature/data sources
(PubMed, GEO, DepMap) were already in use across the sims and are consolidated here for one canonical
list.

*Decision record:* adopted via [ADR-0004](adr/0004-scoring-axes-and-verification-sources-wiring.md). Not
medical advice; sources are canonical entry points as of June 2026 — if a portal URL changes, update this
file.
