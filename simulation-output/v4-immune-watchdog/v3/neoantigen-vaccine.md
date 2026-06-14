# V4 Neoantigen Vaccine Specialist — Clean-Slate Run (v3)

**TAG: Clinical / Experimental — not naturally achievable; for awareness only.**

**One-line summary:** This output covers personalized neoantigen vaccine platforms (BNT122/autogene
cevumeran, mRNA-4157/intismeran autogene, NEO-PV-01), CAR-T/TCR-T for solid tumors and any
CIC-DUX4-specific construct, and the per-patient-vs-pan-CIC-DUX4 vaccine design question driven by
junction-sequence variability — re-verified live for this clean-slate run; it deliberately excludes
IL-15-superagonist mechanism detail (NK specialist's domain, cross-referenced only) and any dietary
intervention (clinical/experimental track only, per scope).

**Confidence: medium-low.** The personalized-neoantigen platform mechanism and its general clinical
validation (melanoma) are now better-supported than at the v1 run (5-year KEYNOTE-942 follow-up,
January 2026), but CIC-rearranged sarcoma remains absent from every platform's enrolled-cohort list,
and — the dominant fact for this output — **this patient's fusion-unconfirmed status makes the single
most tumor-specific candidate neoantigen (the CIC-DUX4 junction peptide) unavailable as a design
input.** Confidence is further lowered by the unresolved BNT122 colorectal futility signal, which
shows personalized-neoantigen efficacy is not a settled question even in better-characterized
indications.

---

## HEADLINE FINDING — FUSION-UNCONFIRMED STATUS IS THE DOMINANT FACT FOR THIS REPORT

**This patient is in the ~5% CIC-rearranged-sarcoma cohort with NO confirmed CIC-DUX4, CIC-NUTM1,
CIC-FOXO4, or other CIC-fusion junction on genomic testing** (per the mRNA Vaccine Team's Section 5c,
`simulation-output/mrna-vaccine-research/mrna-vaccine-summary-v2.md`, which is the single most
important input for this entire output).

Consequence, stated directly: **A CIC-DUX4-junction-specific neoantigen vaccine (whether delivered
as a BNT122-style or mRNA-4157-style individualized mRNA construct, a long-peptide vaccine, or a
junction-peptide TCR-T) is POSSIBLY INAPPLICABLE to this patient**, because the junction nucleotide
sequence — the design input for any of these — has not been identified. Every entry below tagged
**FUSION-CONFIRMED ONLY** inherits this caveat without restatement.

A **fusion-agnostic personalized neoantigen approach** — whole-exome/transcriptome-based somatic
neoantigen discovery directly from this patient's tumor tissue, as used by the mRNA-4157/intismeran-
autogene and BNT122/autogene-cevumeran platforms — **does NOT require a confirmed CIC-DUX4 junction**
and is the only neoantigen-vaccine-class approach that could remain on the table for this patient.
This is discussed as its own track below, separate from (and not contingent on) junction resolution.
- Tier: **Mechanistic** (the platform mechanism is Clinical-Trial-tier in melanoma; its application to
  *this tumor* is Mechanistic until tissue-based neoantigen discovery is actually performed)
- Evidence in CIC-DUX4 specifically: **None direct**

---

## PERSONALIZED NEOANTIGEN VACCINE PLATFORMS — LIVE-VERIFIED STATUS (accessed 2026-06-14)

### mRNA-4157 / V940, now branded **intismeran autogene** — Moderna/Merck

- **Mechanism:** Individualized mRNA-LNP vaccine encoding up to 34 patient-specific tumor neoantigens,
  selected by whole-exome sequencing (WES) + RNA-seq of tumor vs. germline, followed by in-silico
  HLA-binding prediction. Manufactured per-patient (turnaround on the order of weeks).
- **Lead trial / status [VERIFY — perishable]:** KEYNOTE-942 (NCT03897881), randomized phase 2b,
  intismeran autogene + pembrolizumab vs. pembrolizumab alone in resected high-risk (stage IIIB–IV)
  cutaneous melanoma. **A 5-year follow-up was announced January 2026** (Moderna/Merck press release):
  sustained improvement in recurrence-free survival, **49% reduction in risk of recurrence or death**
  vs. pembrolizumab alone — the strongest durability data this platform has produced to date. A
  **Phase 3 confirmatory trial (NCT05933577)** is now ongoing in resected high-risk melanoma, with
  primary completion estimated ~2029.
- **Evidence tier: Clinical-Trial** (melanoma, phase 2b with phase-3 confirmation in progress) —
  **Theoretical** for any CIC-rearranged-sarcoma application (no sarcoma cohort enrolled in either
  trial as of this access date).
- **CIC-DUX4 specifically:** No published trial, case report, or registered protocol targets
  CIC-DUX4. CIC-rearranged sarcoma is not listed as an indication/cohort in NCT03897881 or
  NCT05933577.
- **Applicability to this patient:** The **fusion-agnostic somatic-neoantigen-discovery design** is
  the only conceivably relevant pathway (see "Fusion-Agnostic Track" below). A junction-specific
  payload component is **FUSION-CONFIRMED ONLY**.

### BNT122 (RO7198457), now branded **autogene cevumeran** — BioNTech/Genentech (Roche)

- **Mechanism:** Individualized uridine mRNA-LNP vaccine encoding up to ~20 patient-specific
  neoantigens, same general WES/RNA-seq → HLA-prediction → per-patient manufacture pipeline as
  intismeran autogene, different LNP/mRNA chemistry specifics.
- **Status [VERIFY — perishable, mixed picture]:**
  - **Pancreatic cancer (adjuvant, post-resection):** Phase 1 long-term follow-up (Rojas et al.,
    *Nature* 2023, and a 3-year update reported by BioNTech) showed durable T-cell responses in
    "responder" patients (vaccine-induced T-cells detectable up to 3 years) associated with longer
    recurrence-free survival in a small cohort (8/16 patients showed immune response). A **phase 2
    trial (IMCODE-003)** in adjuvant pancreatic ductal adenocarcinoma is ongoing.
  - **Colorectal cancer (adjuvant, ctDNA-positive stage II/III):** The phase 2 trial **BNT122-01
    (NCT04486378)** crossed a **futility boundary at first interim analysis** per BioNTech's
    Q3-2025 disclosure; the trial remains blinded and continues to final analysis (data delayed from
    2026 to 2027). This is **not** a confirmed negative result, but it is a documented setback —
    "Bad omens for BioNTech & Roche's neoantigen project" (ApexOnco/Oncology Pipeline, 2025–2026
    coverage).
  - **Bladder cancer (IMCODE-004, muscle-invasive):** reported on clinical hold for a safety event
    per the same coverage — **[VERIFY directly at clinicaltrials.gov before relying on this]**.
- **Evidence tier: Clinical-Trial** (pancreatic, phase 1/2 with positive durability signal in a small
  responder subset; colorectal, phase 2 with an unresolved futility signal) — **Theoretical** for any
  sarcoma application.
- **CIC-DUX4 specifically:** No published trial, case report, or registered protocol. CIC-rearranged
  sarcoma is not an enrolled cohort in any BNT122/autogene-cevumeran trial as of this access date.
- **Net read for this output:** the mixed BNT122 picture (one program durable, one program facing
  futility, one apparently on hold) is a useful honesty check — **personalized-neoantigen efficacy is
  not yet a settled question even in indications with established neoantigen landscapes**. This
  should temper expectations for a much-lower-TMB tumor like CIC-rearranged sarcoma, fusion status
  aside.
- **Applicability to this patient:** Same fusion-agnostic-only pathway as intismeran autogene.

### NEO-PV-01 — originally Neon Therapeutics, platform absorbed into BioNTech

- **Mechanism:** Long-peptide (not mRNA) personalized neoantigen vaccine + poly-ICLC adjuvant,
  combined with anti-PD-1.
- **Status [VERIFY]:** Published phase 1b data in melanoma, NSCLC, and bladder cancer (Annals of
  Oncology 2019; *Cancer Cell* 2022 for the NSCLC + chemo + anti-PD-1 combination) showed induction of
  broad de novo neoantigen-specific CD4+/CD8+ T-cell responses. Clinical development under the
  NEO-PV-01 name appears to have been folded into BioNTech's broader mRNA-based personalized-vaccine
  programs (BNT122/autogene cevumeran) following the Neon acquisition; **no active NEO-PV-01-branded
  trial was identified** as of this access date — **[VERIFY]** before citing as an active program.
- **Evidence tier: Clinical-Trial** (melanoma/NSCLC/bladder, phase 1b) — **Theoretical** for sarcoma.
- **CIC-DUX4 specifically: None.**
- **Relevance:** Mainly historical/conceptual — establishes that the personalized-neoantigen + anti-PD-1
  combination principle (relevant to Forward Hypothesis 1 below and to the checkpoint-tcell
  specialist's domain) predates the mRNA-LNP platforms and was demonstrated with a different delivery
  technology (synthetic long peptide).

---

## FUSION-AGNOSTIC TRACK — THE ONLY POTENTIALLY APPLICABLE NEOANTIGEN-VACCINE PATHWAY FOR THIS PATIENT

### Design concept

Both mRNA-4157/intismeran-autogene and BNT122/autogene-cevumeran are, at their core, **platforms for
discovering and encoding patient-specific somatic neoantigens from tumor sequencing** — the
CIC-DUX4 junction peptide (when present and confirmed) is simply *one candidate neoantigen* among the
set the pipeline would identify, not a structural requirement of the platform. This means:

1. WES + RNA-seq of this patient's tumor (vs. matched germline) could identify somatic SNV/indel/
   frameshift-derived neoantigens **independent of fusion status**.
2. If the pipeline identifies a sufficient number (the field's working threshold is roughly 5–20
   high-quality predicted-binder neoantigens; Rizvi et al., *Science* 2015, for the general
   TMB-neoantigen relationship — **not CIC-DUX4-specific**, cited for the concept only) of
   expressed, HLA-binding, non-germline peptides, a personalized vaccine could in principle be
   designed regardless of whether the CIC fusion junction itself is one of them.
3. **CIC-rearranged sarcomas are characterized as low-mutational-burden** (Italiano et al. /
   targeted-NGS series, PMID 27664537 — "low mutational burden and recurrent chromosome 1p loss" in
   CIC-DUX4 soft-tissue sarcomas). This is a material headwind: low TMB means fewer candidate somatic
   neoantigens overall, independent of the fusion-junction question. **This caveat applies to V4's
   fusion-agnostic neoantigen track generally, not only to this patient.**

- **Tier: Mechanistic** (platform mechanism is Clinical-Trial-tier in melanoma/pancreatic; the
  low-TMB headwind is Clinical-Trial-tier evidence — PMID 27664537 — applied by extrapolation to this
  patient's tumor biology)
- **Evidence in CIC-DUX4 specifically:** the low-TMB finding (PMID 27664537) IS in CIC-DUX4 sarcoma
  directly; the platform-application is None direct.

### Tissue-source consideration (theoretical, not a procedure recommendation)

Two tumor specimens exist in this patient's history as theoretical sources of sequencing material:

- **January 2025 resection specimen:** described as >95% necrotic post-VDC/IE. WES/RNA-seq from
  largely-necrotic FFPE tissue has well-documented quality limitations — DNA fragmentation, RNA
  degradation, and low tumor-cell purity in the viable rim reduce sensitivity for neoantigen calling.
  The surviving ≤5% represents the chemo-resistant subclone, which is arguably the most clinically
  relevant target — but is also the smallest fraction of the specimen.
- **Current (May 2026) oligometastatic relapse, single lung cluster:** if a biopsy were obtained for
  other clinical reasons, fresh/frozen tissue from an actively growing lesion would in principle
  yield substantially higher-quality nucleic acid for WES/RNA-seq than the largely-necrotic resection
  specimen, and would reflect the *current* clonal state (relevant given 12+ months of clonal
  evolution since the January 2025 resection). This is noted as a **theoretical tissue-quality
  consideration only** — it is not a recommendation to obtain a biopsy, and any biopsy decision is a
  clinical one made for other reasons (e.g., diagnostic confirmation, the driver-uncertainty
  resolution discussed in `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`).
- **Tier: Mechanistic** (general FFPE/necrotic-tissue NGS-quality literature; not CIC-DUX4-specific)

### Timing reality — manufacturing vs. imminent high-dose ifosfamide

Personalized neoantigen vaccine manufacturing (WES/RNA-seq → neoantigen prediction → per-patient mRNA
synthesis/GMP release) has a **published turnaround on the order of 6–9 weeks** for the mRNA-LNP
platforms (consistent across BNT122 and mRNA-4157 program descriptions). This patient is **now
beginning high-dose ifosfamide** for an oligometastatic relapse — a clinically urgent treatment that
cannot wait for vaccine manufacturing, and which itself induces a lymphodepleting immunosuppression
that would be a poor immunological backdrop for vaccine priming even if a construct existed. **This
is a feasibility/timing reality, not a statement about biology** — it does not mean the fusion-agnostic
approach is mechanistically inapplicable, only that it is not actionable on the current treatment
timeline.
- **Tier: Mechanistic** (manufacturing-timeline facts from platform program descriptions;
  immunosuppression-from-ifosfamide is Established pharmacology, not CIC-DUX4-specific)

---

## CAR-T AND TCR-T FOR SOLID TUMORS / CIC-DUX4

### General solid-tumor CAR-T status

CAR-T is **Established** for hematologic malignancies (CD19-directed: tisagenlecleucel,
axicabtagene ciloleucel, lisocabtagene maraleucel, brexucabtagene autoleucel; BCMA-directed:
idecabtagene vicleucel, ciltacabtagene autoleucel — FDA-approved, multiple). Solid-tumor CAR-T remains
**Clinical-Trial/Preclinical** and unresolved as a class, limited by: (1) poor T-cell trafficking/
infiltration into solid TME, (2) antigen heterogeneity and escape, (3) an immunosuppressive TME
(TGF-β, Tregs, MDSCs) that neutralizes CAR-T function even when cells reach the tumor, and (4)
on-target/off-tumor toxicity risk for shared antigens.

### CIC-DUX4-specific CAR-T or TCR-T

- **No published CAR-T or TCR-T construct specifically targeting CIC-DUX4** (the fusion protein
  itself, a junction-derived peptide, or a CIC-DUX4-associated surface antigen) was identified in this
  search — consistent with the v1 finding and re-confirmed for this run.
- The CIC-DUX4 fusion protein is **intracellular** (a transcription factor), so it is not itself a
  direct CAR target (CAR constructs require a cell-surface antigen). A junction-peptide-MHC complex
  could in principle be a **TCR-T** target if (a) the junction is confirmed, (b) the patient's HLA
  type is known, and (c) the junction peptide is shown to be presented on MHC-I (which requires the
  MHC-I-restoration discussed in the V3→V4 bridge, below, since CIC-DUX4 tumors are reported MHC-I-low
  at baseline).
- **Evidence tier: Theoretical** for any CIC-DUX4-directed CAR-T/TCR-T.
- **Fusion tag: FUSION-CONFIRMED ONLY** for any junction-peptide-derived TCR-T; **N/A** for CAR-T
  generally (no surface target identified regardless of fusion status).

---

## PER-PATIENT vs. PAN-CIC-DUX4 VACCINE DESIGN — JUNCTION SEQUENCE VARIABILITY

Per `docs/02-cic-sarcoma-knowledge.md`: the CIC-DUX4 fusion junction (CIC exon ~20 fused to DUX4 exon
1) creates a peptide sequence absent from the normal proteome — a textbook neoantigen — **but the
junction breakpoint varies at the nucleotide level across patients**, both within CIC (literature
describes variability roughly in the CIC exon ~15–20 region) and at the DUX4 side. Consequences:

- **A pan-CIC-DUX4 vaccine is not a single product.** It would need to be a multi-variant cocktail
  covering the major recurrent breakpoint classes — the v1 output estimated "3–8 major variants" but
  flagged this as **[VERIFY] — no large published series establishes a definitive variant count**;
  this remains true for this run. **Tier: Theoretical.**
- **Per-patient junction sequencing is the safer design assumption** — this is the design logic
  underlying the personalized-neoantigen platforms generally (they sequence each patient's tumor
  rather than assuming a shared antigen), and it applies with extra force to CIC-DUX4 given the
  documented breakpoint heterogeneity.
- **For THIS patient, the question is moot at the current information state** — no junction has been
  confirmed at all, so neither a per-patient nor a pan-variant junction-specific vaccine has a design
  input. Resolving this is the domain of the driver-uncertainty model (Sim 8 /
  `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`), which
  ranks long-read WGS + RNA-seq splice-junction re-analysis as the highest-value test for converting
  this patient from fusion-unconfirmed to fusion-confirmed.

---

## V3 → V4 BRIDGE — MHC-I RESTORATION AS A PREREQUISITE FOR ANY PEPTIDE-VACCINE APPROACH

Per `simulation-output/v3-hot-patching/v3-summary-v3.md` (MHC-I Upregulation Candidates, top
section), **HDAC inhibitors (rank 1) and DNMT inhibitors (rank 2)** are V3's leading fusion-agnostic
candidates for restoring tumor-cell MHC-I (HLA-A/B/C, TAP1/2, B2M) via chromatin-opening and
viral-mimicry/type-I-IFN mechanisms; EZH2i was **downgraded** this run (premise-contested for
CIC-DUX4 per the p300/CBP chromatin-profiling data, and tazemetostat is now globally withdrawn
2026-03-09 — F5/concept-only).

**Relevance to this output:** MHC-I density is the rate-limiting variable for **any** peptide-based
vaccine approach — a personalized neoantigen vaccine (junction-specific or fusion-agnostic) primes
circulating T-cells against predicted peptides, but those T-cells can only recognize tumor cells that
**display** those peptides on MHC-I. If CIC-DUX4 tumor cells are MHC-I-low at baseline (as
mechanistically expected per `docs/02-cic-sarcoma-knowledge.md`'s biomarker notes), a neoantigen
vaccine could generate a robust circulating T-cell response that **cannot find its target in the
tumor**. This is the same dependency the V1-output Forward Hypothesis 1 (carried over and updated
below) builds on.

- **Tier: Theoretical/Mechanistic** — the MHC-I-restoration mechanism is Clinical-Trial-tier in other
  contexts (V3 bridge ranks 1–2); the "neoantigen vaccine + MHC-I restoration as required tandem"
  combination has **not been studied in any tumor type** as a designed sequence.
- **Evidence in CIC-DUX4 specifically: None direct** for either the MHC-I-low baseline or the
  combination hypothesis.

---

## CROSS-VECTOR / CROSS-TEAM FLAGS

### Anti-PEG antibody flag (from mRNA Vaccine Team, Section 5a — carried forward)

BNT162b2 (this patient's prior COVID-19 vaccination) is documented to induce anti-PEG IgG/IgM
antibodies in a subset of recipients (Kozma et al., *NPJ Vaccines* 2022, PMID 35853896 — **[VERIFY]**,
tagged by the mRNA team as consistent-with-but-not-independently-reconfirmed). Both intismeran
autogene (mRNA-4157/V940) and autogene cevumeran (BNT122) use **PEGylated LNP-mRNA delivery** — the
same general chemistry class as BNT162b2.

- **Theoretical mechanism:** pre-existing anti-PEG IgG/IgM could opsonize PEG-LNP particles and
  trigger accelerated blood clearance (ABC phenomenon; Ishida et al., *J Controlled Release* 2006,
  PMID 16797763), reducing lymph-node delivery of the vaccine payload and attenuating the T-cell
  priming response.
- **Tier:** anti-PEG antibody induction — **Clinical-observational** (Kozma 2022, [VERIFY]); ABC
  phenomenon applied to LNP-mRNA cancer vaccines — **Mechanistic/Theoretical** (extrapolated from
  liposomal-drug ABC literature, not measured for cancer-vaccine LNPs specifically).
- **Confidence: Low**, per the mRNA team's own confidence scoring (D=0, A=0, R=0, X=0 — single
  primary study, no direct PK measurement in this context).
- **Design-level flag for the orchestrator:** **IF** this patient were ever considered for an
  intismeran-autogene- or autogene-cevumeran-style trial (most plausibly via the fusion-agnostic
  track above, on a longer time horizon after the current ifosfamide course), **pre-treatment
  anti-PEG IgG/IgM titer (ELISA)** would be a reasonable PK-stratification covariate to flag for
  trial design — not a contraindication, and not actionable today.

### MHC-I-priming synergy note (from V3, this output)

See "V3 → V4 Bridge" section above. Flagged for the orchestrator as a **Theoretical/Mechanistic**
cross-vector synergy (V3 epigenetic priming + V4 neoantigen vaccine) — not demonstrated in any tumor
type, but mechanistically coherent and not yet contradicted.

### Immune-cold-to-hot precedent (cross-reference, not this specialist's primary domain)

A March 2025 case report (Immunologic correlates in a CIC::DUX4 fusion-positive sarcoma responsive to
dual immune checkpoint blockade, *npj Precision Oncology*, PMID 40128305, PMC11933392 — **new since
the v1 run, [VERIFY] for the checkpoint-tcell specialist to incorporate directly**) describes a
CIC::DUX4-confirmed sarcoma that was immunologically cold at baseline (scarce CD3+/CD8+/FOXP3+
infiltrate, negligible PD-L1/PD-1) and converted to an actively-infiltrated, PD-1/LAG-3-coexpressing
("exhausted-but-present") phenotype after nivolumab + relatlimab. This is the **first documented
immunotherapy response signal in CIC::DUX4 sarcoma specifically**. It is primarily relevant to the
checkpoint-tcell specialist's domain (dual ICB), but it is relevant here as a precedent that
**CIC::DUX4 tumors are not immunologically inert** — a cold-to-hot transition is achievable by some
route, which is a precondition for any vaccine-primed T-cell to eventually matter. **Tier:
Clinical-Trial (single case report)**. **Evidence in CIC-DUX4 specifically: Direct** (this is the one
CIC::DUX4-direct immunotherapy data point identified in either run of this simulation).

---

## FORWARD HYPOTHESES

**[Forward Hypothesis 1] — Neoantigen vaccine + MHC-I-restoring epigenetic priming as a required
tandem, re-sequenced in light of the EZH2i downgrade**

**Hypothesis:** A personalized neoantigen vaccine (fusion-agnostic, mRNA-4157/intismeran-autogene- or
BNT122/autogene-cevumeran-style, targeting somatic neoantigens discovered from this patient's tumor
sequencing) cannot produce tumor-cell killing if the tumor is MHC-I-low — primed circulating T-cells
have no presented target to recognize. The V1 output proposed EZH2i (tazemetostat) as the priming
agent; **this run's V3 output downgrades EZH2i to F5/concept-only (global withdrawal 2026-03-09) and
re-ranks HDAC inhibitors (class I — vorinostat, romidepsin, panobinostat, belinostat) and DNMT
inhibitors (azacitidine, decitabine, guadecitabine) as the top two fusion-agnostic MHC-I-restoration
candidates instead.** The updated hypothesis: a brief course of a class-I HDACi or DNMTi, timed to
precede personalized-neoantigen-vaccine dosing, could increase tumor MHC-I/HLA-A,B,C/TAP1/TAP2/B2M
density before vaccine-primed T-cells arrive, converting a vaccine-generated circulating response into
a tumor-recognizing one.

**Mechanistic basis:** HDACi-driven H3K27ac opening at antigen-presentation-machinery loci, and
DNMTi-driven demethylation of MHC-I/HLA and TAP promoters with downstream cGAS-STING/type-I-IFN/STAT1
signaling, both documented to increase MHC-I surface density in other tumor contexts (V3 bridge,
ranks 1–2; Wang et al. 2019 PMC6843866; Luo et al. 2018 DOI 10.1038/s41467-017-02630-w — none
CIC-DUX4-direct). Personalized neoantigen vaccines (intismeran autogene, autogene cevumeran) are
documented to generate neoantigen-specific circulating CD8+ T-cells (KEYNOTE-942, BNT122 pancreatic
follow-up). The combination has not been tested in any tumor type.

**What experiment would test it:** A two-arm design (could be modeled in-silico first using the
existing Sim 4 immune-state model, `sims/04-immune-state-model/`, by simulating MHC-I density as a
function of HDACi/DNMTi exposure and its effect on modeled CD8+ T-cell-tumor recognition probability):
Arm A — fusion-agnostic personalized neoantigen vaccine + anti-PD-1 (current field standard, per
KEYNOTE-942 design); Arm B — short HDACi or DNMTi course timed to precede vaccine dosing, with serial
tumor MHC-I IHC and neoantigen-specific pMHC-multimer T-cell tracking as co-primary correlates.

**Why not yet tested:** HDACi/DNMTi + personalized-neoantigen-vaccine sequencing is an under-explored
combination generally (most MHC-I-priming-bridge literature pairs epigenetic agents with checkpoint
inhibitors, not vaccines); CIC-rearranged sarcoma's rarity means no dedicated trial exists for any
component; and the EZH2i-based version of this hypothesis (V1 output) is now additionally blocked by
tazemetostat's 2026-03-09 withdrawal, requiring this re-derivation.

---

**[Forward Hypothesis 2] — In-silico junction-variant landscape mapping as a pre-emptive design step
for the ~5% fusion-unconfirmed cohort, independent of this patient's own resolution**

**Hypothesis:** Rather than treating "pan-CIC-DUX4 junction vaccine feasibility" as unknowable until a
large clinical series exists, the **published CIC-DUX4 junction sequences from molecularly confirmed
cases** (the Macedo et al. 2025 series of 48 molecularly confirmed cases, DOI 10.1111/his.15341, and
any other public CIC-DUX4 fusion-junction sequence depositions) could be computationally aggregated
and clustered to produce a **provisional junction-variant landscape** — an estimate of how many
distinct breakpoint clusters exist and what fraction of confirmed cases each covers — *before* any
individual patient is sequenced. This would convert the current "[VERIFY] — no large published series
establishes a definitive variant count" gap (carried unresolved from the v1 output) into an actual
number, informing whether a multi-variant pan-CIC-DUX4 vaccine cocktail is a realistic future product
for the ~95% who ARE fusion-confirmed, and by extension what "per-patient sequencing" buys beyond
matching to a known cluster.

**Mechanistic basis:** Fusion breakpoints in other fusion-driven sarcomas (e.g., EWSR1-FLI1 in Ewing
sarcoma) cluster into a tractable number of recurrent breakpoint classes despite nucleotide-level
variability — this is why Ewing-sarcoma fusion-transcript RT-PCR diagnostics can use a limited primer
panel rather than per-patient sequencing for *detection*. Whether CIC-DUX4 junctions show similar
clustering (favoring a feasible multi-variant vaccine cocktail) or are more uniformly distributed
(favoring per-patient design as the only option) is an empirical question answerable from existing
published sequence data without any new patient.

**What experiment would test it:** A bioinformatic study (not requiring new patient samples):
aggregate published CIC-DUX4 breakpoint coordinates (from case reports, the Macedo et al. 2025 cohort,
and any COSMIC/ICGC fusion-breakpoint depositions for CIC-DUX4), align/cluster the resulting junction
peptide sequences, and report (a) the number of distinct clusters needed to cover a given percentage
(e.g., 80%, 95%) of cases, and (b) the predicted HLA-binding promiscuity of the peptides in each
cluster across common HLA alleles. Output: a quantitative answer to "is a pan-CIC-DUX4 junction
vaccine a 3-variant product or a 30-variant product?" — directly informing whether per-patient
sequencing is a *necessity* or merely a *convenience* for the 95% fusion-confirmed cohort.

**Why not yet tested:** CIC-DUX4 sarcoma's rarity (fewer than 200 reported cases worldwide per recent
literature) means breakpoint-sequence depositions are scattered across individual case reports and
small series rather than a centralized database; no group appears to have undertaken this aggregation
specifically for vaccine-design purposes (as opposed to diagnostic-assay design, where Macedo et al.
2025 instead pursued an IHC-based detection shortcut that sidesteps the sequence-variability problem
entirely).

---

## ATYPICAL-CASE NOTES

**This patient's fusion-unconfirmed status is the central organizing fact of this entire output —
restated here for completeness per the contract requirement.**

**FUSION-CONFIRMED ONLY (possibly inapplicable to this patient without confirmatory fusion
identification):**
- CIC-DUX4 junction-specific neoantigen vaccine (any platform: BNT122/autogene-cevumeran-style,
  mRNA-4157/intismeran-autogene-style, long-peptide, or pan-variant cocktail).
- CIC-DUX4 junction-peptide-specific TCR-T.
- Any "pan-CIC-DUX4" vaccine product, regardless of how many junction-variant clusters Forward
  Hypothesis 2 ultimately identifies.

**FUSION-AGNOSTIC (may apply to this patient and to the ~5% atypical subgroup generally):**
- Fusion-agnostic personalized neoantigen vaccine via somatic WES/RNA-seq discovery (intismeran
  autogene / autogene cevumeran platform mechanism) — subject to the low-TMB headwind
  (PMID 27664537) and the manufacturing-timeline-vs-ifosfamide feasibility constraint, both of which
  apply to fusion-confirmed CIC-DUX4 patients equally.
- General CAR-T toward any non-junction-derived surface target (none currently identified for
  CIC-DUX4 — applies equally to fusion-confirmed and fusion-unconfirmed cases, i.e., this is a gap
  for the whole disease, not specific to this patient).
- The MHC-I-restoration bridge (V3 ranks 1–2, HDACi/DNMTi) — fusion-agnostic, acts on host
  chromatin/APM machinery.
- The anti-PEG antibody flag — applies regardless of fusion status (it is about the LNP delivery
  vehicle, not the payload).
- The npj Precision Oncology dual-ICB case report (PMID 40128305) was in a **fusion-CONFIRMED**
  CIC::DUX4 patient — its direct relevance to this fusion-unconfirmed patient is as a **precedent for
  the disease class**, not a directly transferable data point. Flagged for the checkpoint-tcell
  specialist.

---

## WHAT I COULD NOT ESTABLISH

1. **NEO-PV-01's current independent development status** — could not confirm whether any
   NEO-PV-01-branded trial remains active versus having been fully absorbed into BNT122/autogene-
   cevumeran programs. Tagged [VERIFY].

2. **A definitive CIC-DUX4 junction-variant count** — the v1 output's "3–8 major variants" estimate
   remains unverified; Forward Hypothesis 2 proposes how to resolve this, but it has not been done.

3. **This patient's HLA type** — required for any neoantigen-binding prediction (fusion-agnostic
   track) and for any TCR-T approach (junction-specific track, if ever unlocked). Not addressed by
   this output; would need confirmation from clinical records.

4. **Quality/yield of WES/RNA-seq from the January 2025 (>95% necrotic) resection specimen** —
   flagged as a theoretical limitation; actual sequencing-quality metrics for this specific specimen
   are unknown to this output.

5. **Whether autogene cevumeran's BNT122-01 colorectal futility signal reflects a platform-level
   ceiling on personalized-neoantigen efficacy or an indication-specific issue (colorectal TME,
   ctDNA-based patient selection, etc.)** — the distinction matters for how much the fusion-agnostic
   track's prospects should be discounted for CIC-rearranged sarcoma, and is not resolved in the
   sources reviewed.

6. **Current enrolled-cohort lists for NCT05933577 (intismeran autogene phase 3), IMCODE-003
   (autogene cevumeran pancreatic phase 2), and any other active personalized-neoantigen trial** —
   confirmed absent for CIC-rearranged sarcoma as of this access date (2026-06-14), but trial
   cohorts can be amended; re-verify before relying on this absence.

7. **The DUX4 IHC test (Macedo et al. 2025, used as the cheapest driver-resolution test in
   `simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`) was not
   independently re-evaluated here for its junction-*sequence* informativeness** — IHC confirms DUX4
   transactivation-domain presence/expression but does not yield the breakpoint sequence needed for
   vaccine design; long-read WGS + RNA-seq remains the design-relevant test, per Sim 8.
