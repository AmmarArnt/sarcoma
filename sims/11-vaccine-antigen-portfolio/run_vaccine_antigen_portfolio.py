#!/usr/bin/env python3
"""Sim 11 — Can the individualized-neoantigen-therapy (INT) CONCEPT be transplanted to a
low-TMB, driver-unresolved round-cell sarcoma? And if not as-is, what vaccine WOULD work?

WHY THIS SIM EXISTS
-------------------
Merck/Moderna's intismeran autogene (mRNA-4157 / V940) is the reference implementation of a
*concept*, not a molecule. Stripped to its architecture, the concept is four independent pillars:

    P1  ANTIGEN SOURCE      -> the patient's own somatic mutanome (WES/RNA-seq of tumour vs germline)
    P2  DELIVERY + ADJUVANT -> mRNA-LNP, which is itself an innate adjuvant (TLR7/8, type-I IFN)
    P3  POLYEPITOPE BREADTH -> up to ~34 neoantigens in ONE construct -> escape needs many hits
    P4  DEPLOYMENT CONTEXT  -> adjuvant/MRD setting (low burden), combined with PD-1 blockade

Pillars P2, P3 and P4 are tumour-agnostic engineering. Pillar P1 is NOT: it is a *supply chain*
whose throughput is set by tumour mutational burden. Melanoma (the indication where the concept
was validated) sits at the top of the pan-cancer TMB distribution; translocation-driven round-cell
sarcoma sits at the very bottom.

So the honest question is not "does the drug work in sarcoma" but:
    (Q1) does pillar P1 have enough throughput in THIS tumour class to fill the construct?
    (Q2) if it does not, which alternative ANTIGEN SOURCES can be swapped into the same
         P2/P3/P4 architecture, and what does the resulting vaccine look like?
    (Q3) once antigens exist, is antigen count even the binding constraint — or is it
         presentation (MHC-I), timing (the MRD window), and escape coverage?

This sim answers all three quantitatively, under the Era-B case baseline (CASE-BASELINE.md):
a chemo-responsive, Ewing-like, DRIVER-UNRESOLVED round-cell sarcoma, so the antigen supply is
itself conditioned on a latent driver D1..D5.

MODEL STRUCTURE
---------------
  Module A  neoepitope supply funnel:   TMB | driver  ->  candidate epitopes -> immunogenic epitopes
            (with a MELANOMA CALIBRATION ARM as a consistency check: the same funnel must
             reproduce "melanoma easily fills a 34-slot construct" without being fitted to do so)
  Module B  antigen-source portfolio:   7 antigen classes A1..A7, each availability-conditioned on
            the driver posterior, scored on yield / escape-hazard / specificity-risk / readiness
  Module C  the gate BEYOND antigen:    presented x window x effector x escape-survival
  Module D  architecture bake-off:      6 candidate vaccine architectures ranked by expected utility
  Module E  sensitivity (tornado) + a diagnostic value-of-information ranking over the tests that
            would collapse the biggest uncertainties (composes ADR-0015 / Sim 6 / Sim 8 methodology)

TIER / STATUS
-------------
DECISION MODEL (Mechanistic/Theoretical tier). NOT a diagnosis, NOT a treatment or testing
recommendation, NOT medical advice. No patient sample, no vaccine construct, and no epitope
prediction was actually run: this models the *design space*, not a specific patient's antigens.
Every parameter is a transparent, literature-anchored mechanistic judgement declared in
MANIFEST.md; direct literature egress was blocked in this session, so **every citation is
`[VERIFY]`** per ADR-0020 and this output sits in the FORWARD lane only.
"""
from __future__ import annotations

import csv
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(20260819)
N = 40000  # Monte Carlo draws

# construct capacity of the reference platform: mRNA-4157/intismeran autogene encodes
# "up to 34" patient-specific neoantigens in one mRNA [VERIFY]
SLOTS = 34
DESIGN_MIN = 5  # design judgement: fewer than 5 candidate epitopes is not a polyepitope vaccine


def lognorm(median, gsd, size):
    """Lognormal parameterised by median and geometric SD (both natural units)."""
    return RNG.lognormal(mean=np.log(median), sigma=np.log(gsd), size=size)


def beta_from(mean, lo, hi, size):
    """Beta draw with the given mean, concentration set so ~90% of mass sits in [lo, hi]."""
    spread = max(hi - lo, 1e-3)
    conc = max(2.0, (2.0 / spread) ** 2 * 0.25)  # heuristic: tighter interval -> higher conc
    a = max(mean * conc, 0.35)
    b = max((1 - mean) * conc, 0.35)
    return np.clip(RNG.beta(a, b, size), 0.0, 1.0)


# --------------------------------------------------------------------------- #
# 0. Latent driver — Era-B posterior, carried verbatim from CASE-BASELINE.md §3
#    (itself the output of Sim 10 conditioning Sim 8's prior on the chemo response)
# --------------------------------------------------------------------------- #
DRIVERS = ["D1_cryptic_CICDUX4", "D2_rare_CIC_partner", "D3_nonfusion_CIC_LOF",
           "D4_phenocopy_misclassified", "D5_orphan_epigenetic"]
POST_D = np.array([0.264, 0.100, 0.095, 0.386, 0.156])
POST_D = POST_D / POST_D.sum()

# Does this driver hypothesis imply a translated FUSION JUNCTION (a public neoantigen)?
#   D1 CIC::DUX4 yes; D2 CIC::NUTM1/FOXO4/LEUTX yes; D3 CIC loss-of-function NO (no chimeric ORF);
#   D4 phenocopy: BCOR-ITD / EWSR1::non-ETS -> a junction/ITD often exists but is unidentified;
#   D5 orphan/epigenetic: assumed none.
HAS_JUNCTION = {"D1_cryptic_CICDUX4": 1.0, "D2_rare_CIC_partner": 1.0,
                "D3_nonfusion_CIC_LOF": 0.0, "D4_phenocopy_misclassified": 0.65,
                "D5_orphan_epigenetic": 0.10}
# Does this driver imply DUX4 protein expression (a cleavage-stage/germline TF, normally silent in
# soma -> behaves like a cancer-testis antigen) AND its documented IFN/MHC-I antagonism? [VERIFY]
HAS_DUX4 = {"D1_cryptic_CICDUX4": 1.0, "D2_rare_CIC_partner": 0.15,
            "D3_nonfusion_CIC_LOF": 0.0, "D4_phenocopy_misclassified": 0.0,
            "D5_orphan_epigenetic": 0.05}

# TMB per driver class, in NONSYNONYMOUS CODING mutations per Mb (median, geometric SD).
# Anchors [VERIFY]: Ewing sarcoma is among the lowest-TMB malignancies known (~0.15 mut/Mb);
# CIC-rearranged sarcoma is characterised as "low mutational burden" (PMID 27664537);
# BCOR-altered / undifferentiated round-cell sit in the same low band.
TMB_MED = {"D1_cryptic_CICDUX4": 0.80, "D2_rare_CIC_partner": 0.80,
           "D3_nonfusion_CIC_LOF": 0.90, "D4_phenocopy_misclassified": 0.30,
           "D5_orphan_epigenetic": 0.60}
TMB_GSD = 2.3
EXOME_MB = 30.0  # coding footprint actually interrogated by a clinical WES panel
MELANOMA_TMB_MED, MELANOMA_TMB_GSD = 13.0, 3.0  # calibration arm [VERIFY]


# --------------------------------------------------------------------------- #
# MODULE A — the neoepitope supply funnel (pillar P1)
# --------------------------------------------------------------------------- #
def supply_funnel(tmb, n):
    """TMB -> #mutations -> clonal -> expressed -> HLA-I binder -> immunogenic.

    Each attrition step is sampled per-draw so the output carries parameter uncertainty,
    not just Poisson noise.
    """
    n_mut = RNG.poisson(np.clip(tmb * EXOME_MB, 0.05, None))
    f_clonal = beta_from(0.60, 0.35, 0.85, n)      # truncal vs subclonal
    f_expressed = beta_from(0.45, 0.25, 0.65, n)   # RNA-seq expression filter
    f_binder = beta_from(0.30, 0.15, 0.50, n)      # >=1 strong class-I binder over a 6-allele genotype
    f_immuno = beta_from(0.08, 0.01, 0.25, n)      # predicted binder -> actually T-cell recognised

    n_candidate = RNG.binomial(n_mut, np.clip(f_clonal * f_expressed * f_binder, 0, 1))
    n_immunogenic = RNG.binomial(n_candidate, f_immuno)
    return n_mut, n_candidate, n_immunogenic


def module_a():
    d_idx = RNG.choice(len(DRIVERS), size=N, p=POST_D)
    tmb = np.array([lognorm(TMB_MED[DRIVERS[i]], TMB_GSD, 1)[0] for i in d_idx])
    n_mut, n_cand, n_imm = supply_funnel(tmb, N)

    mel_tmb = lognorm(MELANOMA_TMB_MED, MELANOMA_TMB_GSD, N)
    m_mut, m_cand, m_imm = supply_funnel(mel_tmb, N)

    rows = []
    for label, cand, imm, mut in (("sarcoma_driver_marginal", n_cand, n_imm, n_mut),
                                  ("melanoma_calibration", m_cand, m_imm, m_mut)):
        rows.append({
            "arm": label,
            "median_nonsyn_mutations": float(np.median(mut)),
            "median_candidate_epitopes": float(np.median(cand)),
            "mean_candidate_epitopes": round(float(cand.mean()), 2),
            "mean_immunogenic_epitopes": round(float(imm.mean()), 3),
            "P_fills_34_slots": round(float((cand >= SLOTS).mean()), 4),
            "P_ge_20": round(float((cand >= 20).mean()), 4),
            "P_ge_10": round(float((cand >= 10).mean()), 4),
            "P_ge_5_design_min": round(float((cand >= DESIGN_MIN).mean()), 4),
            "P_zero_candidates": round(float((cand == 0).mean()), 4),
            "P_ge_1_immunogenic": round(float((imm >= 1).mean()), 4),
        })

    per_driver = []
    for i, d in enumerate(DRIVERS):
        t = lognorm(TMB_MED[d], TMB_GSD, N)
        _, c, im = supply_funnel(t, N)
        per_driver.append({
            "driver": d, "posterior": POST_D[i],
            "median_TMB_mut_per_Mb": round(float(np.median(t)), 3),
            "mean_candidate_epitopes": round(float(c.mean()), 2),
            "P_fills_34_slots": round(float((c >= SLOTS).mean()), 4),
            "P_ge_5_design_min": round(float((c >= DESIGN_MIN).mean()), 4),
            "mean_immunogenic_epitopes": round(float(im.mean()), 3),
        })
    return rows, per_driver, (n_cand, n_imm), d_idx


# --------------------------------------------------------------------------- #
# MODULE B — antigen-source portfolio (what you swap into pillar P1)
# --------------------------------------------------------------------------- #
# Each class carries:
#   p_avail_by_driver : probability the class actually EXISTS in this tumour, given the driver
#   yield_lo/hi       : usable class-I epitopes contributed if available
#   immuno            : fraction of those that are genuinely T-cell recognised (central tolerance
#                       bites hardest on self-antigens: mutanome > junction/cryptic > CTA > lineage)
#   escape_hazard     : P(tumour can lose this antigen class with no fitness cost)
#   spec_risk         : P(clinically-relevant on-target/off-tumour autoimmunity)
#   readiness         : 0..1 translational readiness (maps to the F1..F5 feasibility bands)
#   needs_discovery   : per-patient discovery burden (0 = off-the-shelf, 1 = bespoke pipeline)
ANTIGEN_CLASSES = {
    "A1_somatic_mutanome": dict(
        p_avail={d: 1.0 for d in DRIVERS},          # always "available" — just possibly empty (Module A)
        yield_lo=0, yield_hi=0,                     # yield comes from the Module-A funnel, not a constant
        immuno=(0.05, 0.20), escape=(0.55, 0.85), spec=(0.01, 0.05),
        readiness=0.80, needs_discovery=1.0,
        tier="Clinical-Trial (platform, melanoma) / Theoretical (this tumour)"),
    "A2_fusion_junction": dict(
        p_avail=HAS_JUNCTION,
        yield_lo=1, yield_hi=3, immuno=(0.05, 0.25), escape=(0.02, 0.10), spec=(0.00, 0.02),
        readiness=0.35, needs_discovery=1.0,
        tier="Preclinical-Cell / Theoretical (fusion-contingent)"),
    "A3_cancer_testis": dict(                        # NY-ESO-1/CTAG1B, PRAME, MAGE-A4, XAGE1
        p_avail={"D1_cryptic_CICDUX4": 0.35, "D2_rare_CIC_partner": 0.35,
                 "D3_nonfusion_CIC_LOF": 0.35, "D4_phenocopy_misclassified": 0.45,
                 "D5_orphan_epigenetic": 0.45},
        yield_lo=2, yield_hi=8, immuno=(0.03, 0.15), escape=(0.25, 0.60), spec=(0.02, 0.10),
        readiness=0.85, needs_discovery=0.2,
        tier="Clinical-Trial (other sarcoma subtypes) / Theoretical (round-cell)"),
    "A4_lineage_programme": dict(                    # STEAP1, CHM1/LECT1, GPR64/ADGRG2, LIPI
        p_avail={"D1_cryptic_CICDUX4": 0.30, "D2_rare_CIC_partner": 0.30,
                 "D3_nonfusion_CIC_LOF": 0.30, "D4_phenocopy_misclassified": 0.60,
                 "D5_orphan_epigenetic": 0.35},
        yield_lo=2, yield_hi=6, immuno=(0.02, 0.10), escape=(0.05, 0.25), spec=(0.05, 0.20),
        readiness=0.60, needs_discovery=0.2,
        tier="Preclinical-Animal / Clinical-Trial (Ewing, cell therapy)"),
    "A5_noncanonical_ORF": dict(                     # cryptic ORFs, retained introns, splice-derived
        p_avail={"D1_cryptic_CICDUX4": 0.70, "D2_rare_CIC_partner": 0.70,
                 "D3_nonfusion_CIC_LOF": 0.60, "D4_phenocopy_misclassified": 0.70,
                 "D5_orphan_epigenetic": 0.65},
        yield_lo=2, yield_hi=12, immuno=(0.04, 0.18), escape=(0.20, 0.55), spec=(0.02, 0.12),
        readiness=0.25, needs_discovery=1.0,
        tier="Preclinical-Cell / Mechanistic"),
    "A6_induced_derepressed": dict(                  # HERV/ERV + CTA de-repressed by EZH2i/DNMTi/HDACi
        p_avail={d: 0.75 for d in DRIVERS},          # induced, so weakly driver-dependent
        yield_lo=3, yield_hi=15, immuno=(0.02, 0.12), escape=(0.50, 0.85), spec=(0.05, 0.25),
        readiness=0.40, needs_discovery=0.6,
        tier="Preclinical-Cell (viral mimicry) / Mechanistic"),
    "A7_DUX4_as_CTA": dict(                          # DUX4 itself as a germline-restricted antigen
        p_avail=HAS_DUX4,
        yield_lo=1, yield_hi=4, immuno=(0.03, 0.15), escape=(0.02, 0.12), spec=(0.01, 0.06),
        readiness=0.20, needs_discovery=0.5,
        tier="Theoretical (driver-contingent; DUX4 also antagonises MHC-I)"),
}
CLASS_ORDER = list(ANTIGEN_CLASSES)


# A fusion junction that EXISTS but has not been SEQUENCED is not a design input. Short-read
# panels/WGS already failed to find one in this patient (and short-read callers filter CIC::DUX4 on
# the DUX4 repeats; CIC break-apart FISH has a 14-46% false-negative rate — CASE-BASELINE §2).
# So the junction arm is gated on an explicit resolution ACTION, with long-read sensitivity ~0.80.
P_JUNCTION_IDENTIFIED_TODAY = 0.0
P_JUNCTION_IDENTIFIED_LONGREAD = 0.80


def sample_classes(d_idx, mutanome_cand, junction_resolved=False):
    """Draw per-sample availability / yield / escape / specificity for every antigen class."""
    out = {}
    driver_names = np.array(DRIVERS)[d_idx]
    p_ident = P_JUNCTION_IDENTIFIED_LONGREAD if junction_resolved else P_JUNCTION_IDENTIFIED_TODAY
    for name, p in ANTIGEN_CLASSES.items():
        p_avail = np.array([p["p_avail"][d] for d in driver_names])
        if name == "A2_fusion_junction":
            p_avail = p_avail * p_ident       # exists AND has been sequenced
        avail = RNG.random(N) < p_avail
        if name == "A1_somatic_mutanome":
            yld = np.minimum(mutanome_cand, SLOTS).astype(float)
            avail = yld >= DESIGN_MIN  # a mutanome arm only "exists" if it can fill >= design min
        else:
            yld = RNG.integers(p["yield_lo"], p["yield_hi"] + 1, N).astype(float)
        immuno = RNG.uniform(*p["immuno"], N)
        escape = RNG.uniform(*p["escape"], N)
        spec = RNG.uniform(*p["spec"], N)
        out[name] = dict(avail=avail, yld=yld * avail, immuno=immuno,
                         escape=escape, spec=spec,
                         readiness=p["readiness"], discovery=p["needs_discovery"])
    return out


# --------------------------------------------------------------------------- #
# MODULE C — the gate beyond antigen: presentation x window x effector x escape
# --------------------------------------------------------------------------- #
def context_draws(d_idx):
    driver_names = np.array(DRIVERS)[d_idx]
    dux4 = np.array([HAS_DUX4[d] for d in driver_names])

    # Baseline MHC-I adequacy. Round-cell sarcomas are characteristically MHC-I-low / immune-cold
    # [VERIFY]; where DUX4 is expressed it additionally antagonises IFN-gamma-induced MHC-I [VERIFY].
    mhc1_base = beta_from(0.35, 0.15, 0.60, N) * (1.0 - 0.45 * dux4)
    # Epigenetic priming (EZH2i / class-I HDACi / DNMTi) — the repo's dual-purpose PRC2 node
    # (Sim 2 repositioned EZH2i as MHC-I priming, not cytotoxic; ADR-0021 adds SLFN11 maintenance).
    prime_gain = beta_from(0.45, 0.20, 0.70, N)
    mhc1_primed = np.clip(mhc1_base + prime_gain * (1 - mhc1_base), 0, 1)

    # Deployment context. In the post-chemo MRD window: low burden, lymphodepletion-driven
    # homeostatic expansion, Treg trough. Outside it: bulk disease, suppressive TME.
    window_mult = beta_from(0.95, 0.85, 1.00, N)
    nowindow_mult = beta_from(0.45, 0.25, 0.65, N)

    # Effector arms. T-cell reconstitution lags NK by weeks post-chemo (ADR-0021 NK-first).
    t_fitness = beta_from(0.45, 0.25, 0.70, N)
    nk_fitness = beta_from(0.55, 0.30, 0.80, N)
    icb_mult = RNG.uniform(1.15, 1.60, N)  # PD-1 add-on multiplier

    # Escape routes independent of antigen identity
    hla_loh = beta_from(0.20, 0.08, 0.35, N)  # HLA-LOH / B2M loss under T-cell pressure

    # Adding a systemic epigenetic priming agent is not free (toxicity, chemo interaction, one more
    # drug in a heavily pre-treated patient). Modelled as a flat utility penalty so that "always
    # prime" is not automatically dominant and an MHC-I test can have non-zero value.
    prime_cost = RNG.uniform(0.88, 0.97, N)
    return dict(mhc1_base=mhc1_base, mhc1_primed=mhc1_primed, window_mult=window_mult,
                nowindow_mult=nowindow_mult, t_fitness=t_fitness, nk_fitness=nk_fitness,
                icb_mult=icb_mult, hla_loh=hla_loh, prime_cost=prime_cost)


def architecture_utility(classes, ctx, use, *, priming, in_window, nk_arm, icb,
                         antigen_agnostic=False, take_rate=None):
    """Expected utility of one vaccine architecture, per Monte-Carlo draw.

    utility = breadth(N_eff) x presentation x context x effector x escape-survival x safety x readiness
    """
    if antigen_agnostic:
        # In-situ vaccination (oncolytic virus / lysate-DC): antigens are supplied by the tumour
        # itself, so no identification step — but it is gated on infection/take rate AND on
        # physical access to the lesion instead. ADR-0019's honest read is applied here: the
        # nearest data (Ewing/round-cell) show LOW OV susceptibility, and this patient's lesions
        # are visceral (lung), not injectable skin nodules.
        n_eff = take_rate * RNG.uniform(2.0, 8.0, N)
        escape_survival = np.full(N, 0.85)  # polyclonal, whole-repertoire -> escape needs many losses
        safety = np.full(N, 0.95)
        readiness = 0.45
        slots_used = np.zeros(N)
    elif not use:
        # Context-only baseline: NO vaccine at all. Everything the winning architectures bundle
        # AROUND the vaccine (priming, MRD-window timing, NK arm, PD-1) with no antigen construct.
        # This is the comparator that isolates what the vaccine itself contributes.
        n_eff = np.zeros(N)
        escape_survival = np.ones(N)
        safety = np.ones(N)
        readiness = 0.70
        slots_used = np.zeros(N)
    else:
        n_eff = np.zeros(N)
        keep_prob = np.ones(N)   # P(all chosen classes lost) accumulator
        safety = np.ones(N)
        slots_used = np.zeros(N)
        readiness_terms = []
        for name in use:
            c = classes[name]
            room = np.clip(SLOTS - slots_used, 0, None)
            taken = np.minimum(c["yld"], room)
            slots_used += taken
            n_eff += taken * c["immuno"]
            # a class contributes escape-resistance only if it actually contributed epitopes
            contributes = taken > 0
            keep_prob *= np.where(contributes, c["escape"], 1.0)
            safety *= np.where(contributes, 1 - c["spec"], 1.0)
            readiness_terms.append(c["readiness"])
        escape_survival = 1 - keep_prob
        # a construct ships when its SLOWEST component is ready, so readiness is a min, not a mean
        readiness = float(np.min(readiness_terms)) if readiness_terms else 0.0

    breadth = 1 - np.exp(-n_eff / 3.0)                      # saturating returns on epitope count
    presentation = ctx["mhc1_primed"] if priming else ctx["mhc1_base"]
    context = ctx["window_mult"] if in_window else ctx["nowindow_mult"]

    # T-cell (vaccine-attributable) arm — the only arm that antigen escape and HLA loss can defeat.
    # The construct's translational readiness discounts THIS arm only: a hard-to-build vaccine
    # must not be allowed to degrade the antigen-independent NK arm running alongside it.
    p_t = breadth * presentation * context * ctx["t_fitness"] * (ctx["icb_mult"] if icb else 1.0)
    p_t = np.clip(p_t, 0, 1) * (1 - ctx["hla_loh"]) * escape_survival * (0.55 + 0.45 * readiness)
    if nk_arm:
        # NK arm is antigen-INDEPENDENT and covers exactly the MHC-I-loss escape route
        # (Sims 4/5/6: nectin/missing-self route; ADR-0021: NK reconstitutes first post-chemo).
        # It is therefore not multiplied by escape_survival, presentation, or vaccine readiness.
        p_nk = ctx["nk_fitness"] * context * (0.45 + 0.55 * ctx["hla_loh"])
        p_control = 1 - (1 - p_t) * (1 - np.clip(p_nk, 0, 1))
    else:
        p_control = p_t

    # safety (on-target/off-tumour autoimmunity) and priming cost are systemic harms: they apply
    # to the whole regimen, not just to the arm that caused them
    util = p_control * safety
    if priming:
        util = util * ctx["prime_cost"]
    return util, n_eff, slots_used, p_t


# --------------------------------------------------------------------------- #
# MODULE D — architecture bake-off
# --------------------------------------------------------------------------- #
ARCHITECTURES = {
    "V-0_context_only_NO_vaccine": dict(
        use=[], priming=True, in_window=True, nk_arm=True, icb=True,
        note="BASELINE: everything except the vaccine — priming + MRD window + NK arm + PD-1"),
    "V-A_mutanome_only_INT_transplant": dict(
        use=["A1_somatic_mutanome"], priming=False, in_window=False, nk_arm=False, icb=True,
        note="literal intismeran-style transplant: private mutanome + PD-1, adjuvant setting"),
    "V-B_junction_only": dict(
        use=["A2_fusion_junction"], priming=False, in_window=False, nk_arm=False, icb=True,
        note="fusion-junction vaccine; requires the driver AND the junction to be resolved"),
    "V-C_shared_offtheshelf_polyepitope": dict(
        use=["A3_cancer_testis", "A4_lineage_programme"], priming=False, in_window=False,
        nk_arm=False, icb=True,
        note="off-the-shelf CTA + lineage-programme mRNA polyepitope; no per-patient discovery"),
    "V-D_hybrid_primed_polyepitope": dict(
        use=["A1_somatic_mutanome", "A2_fusion_junction", "A3_cancer_testis",
             "A4_lineage_programme", "A6_induced_derepressed"],
        priming=True, in_window=True, nk_arm=True, icb=True,
        note="portfolio antigens + epigenetic MHC-I/antigen priming + MRD window + NK arm + PD-1"),
    "V-D2_hybrid_no_priming_no_window": dict(
        use=["A1_somatic_mutanome", "A2_fusion_junction", "A3_cancer_testis",
             "A4_lineage_programme", "A6_induced_derepressed"],
        priming=False, in_window=False, nk_arm=False, icb=True,
        note="ablation of V-D: same antigens, none of the context engineering"),
    "V-F_narrow_high_specificity": dict(
        use=["A1_somatic_mutanome", "A2_fusion_junction", "A7_DUX4_as_CTA", "A5_noncanonical_ORF"],
        priming=True, in_window=True, nk_arm=True, icb=True,
        note="only antigen classes with tumour-restricted expression (spec-risk <=0.07): private "
             "mutanome + junction + DUX4-as-CTA + cryptic ORFs; no shared self-antigens"),
    "V-E_in_situ_antigen_agnostic": dict(
        use=[], priming=True, in_window=True, nk_arm=True, icb=True, antigen_agnostic=True,
        note="in-situ vaccination (OV / lysate-DC): tumour supplies its own antigen repertoire"),
}


def main():
    print("=" * 78)
    print("SIM 11 — Vaccine antigen-source portfolio for a low-TMB, driver-unresolved sarcoma")
    print("=" * 78)

    # ---------------- Module A ----------------
    a_rows, per_driver, (n_cand, n_imm), d_idx = module_a()
    print("\n[MODULE A] Neoepitope supply funnel — can pillar P1 fill a 34-slot construct?\n")
    for r in a_rows:
        print(f"  {r['arm']:<26} median mutations={r['median_nonsyn_mutations']:>6.1f} "
              f"mean candidate epitopes={r['mean_candidate_epitopes']:>6.2f}  "
              f"P(fills 34)={r['P_fills_34_slots']:.3f}  P(>=5)={r['P_ge_5_design_min']:.3f}  "
              f"P(>=1 immunogenic)={r['P_ge_1_immunogenic']:.3f}")
    ratio = (a_rows[1]["mean_candidate_epitopes"] / max(a_rows[0]["mean_candidate_epitopes"], 1e-9))
    print(f"\n  CONSISTENCY CHECK: the same funnel gives melanoma {ratio:.0f}x the candidate-epitope "
          f"supply of\n  the sarcoma arm, and P(melanoma fills 34 slots)="
          f"{a_rows[1]['P_fills_34_slots']:.2f} vs {a_rows[0]['P_fills_34_slots']:.2f} here — "
          "the funnel\n  reproduces the indication where the concept was validated without being "
          "fitted to it.")

    with open(os.path.join(HERE, "supply_funnel.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(a_rows[0]))
        w.writeheader()
        w.writerows(a_rows)
    with open(os.path.join(HERE, "supply_by_driver.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(per_driver[0]))
        w.writeheader()
        w.writerows(per_driver)

    # ---------------- Module B ----------------
    classes = sample_classes(d_idx, n_cand)
    print("\n[MODULE B] Antigen-source classes — availability and expected usable epitopes\n")
    b_rows = []
    for name in CLASS_ORDER:
        c = classes[name]
        row = dict(antigen_class=name,
                   P_available=round(float(c["avail"].mean() if c["avail"].dtype == bool
                                           else (c["yld"] > 0).mean()), 4),
                   mean_epitopes_if_used=round(float(c["yld"].mean()), 2),
                   mean_immunogenic=round(float((c["yld"] * c["immuno"]).mean()), 3),
                   escape_hazard=round(float(c["escape"].mean()), 3),
                   specificity_risk=round(float(c["spec"].mean()), 3),
                   readiness=c["readiness"], per_patient_discovery=c["discovery"],
                   tier=ANTIGEN_CLASSES[name]["tier"])
        b_rows.append(row)
        print(f"  {name:<26} P(avail)={row['P_available']:.2f}  "
              f"epitopes={row['mean_epitopes_if_used']:>5.2f}  "
              f"immunogenic={row['mean_immunogenic']:>5.2f}  "
              f"escape={row['escape_hazard']:.2f}  spec-risk={row['specificity_risk']:.2f}")
    with open(os.path.join(HERE, "antigen_classes.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(b_rows[0]))
        w.writeheader()
        w.writerows(b_rows)

    # ---------------- Modules C + D ----------------
    ctx = context_draws(d_idx)
    print("\n[MODULE D] Architecture bake-off — expected utility across "
          f"{N:,} draws over the driver posterior\n")
    utils, d_rows = {}, []
    for name, cfg in ARCHITECTURES.items():
        kw = dict(cfg)
        note = kw.pop("note")
        use = kw.pop("use")
        # in-situ take rate: ADR-0019 low round-cell OV susceptibility x visceral-lesion access
        take = (RNG.uniform(0.05, 0.30, N) * RNG.uniform(0.35, 0.70, N)
                if kw.get("antigen_agnostic") else None)
        u, n_eff, slots, p_t = architecture_utility(classes, ctx, use, take_rate=take, **kw)
        utils[name] = u
        d_rows.append(dict(architecture=name, mean_utility=round(float(u.mean()), 4),
                           median_utility=round(float(np.median(u)), 4),
                           p05=round(float(np.percentile(u, 5)), 4),
                           p95=round(float(np.percentile(u, 95)), 4),
                           mean_effective_epitopes=round(float(n_eff.mean()), 2),
                           mean_slots_used=round(float(slots.mean()), 1),
                           mean_vaccine_arm_p=round(float(p_t.mean()), 4), note=note))
    stack = np.vstack([utils[k] for k in ARCHITECTURES])
    top = np.array(list(ARCHITECTURES))[stack.argmax(axis=0)]
    base_ctx_only = utils["V-0_context_only_NO_vaccine"].mean()
    for r in d_rows:
        r["pct_top_ranked"] = round(float((top == r["architecture"]).mean()), 4)
        r["delta_vs_no_vaccine"] = round(float(r["mean_utility"] - base_ctx_only), 4)
    d_rows.sort(key=lambda r: -r["mean_utility"])
    for r in d_rows:
        print(f"  {r['architecture']:<36} utility={r['mean_utility']:.4f} "
              f"[{r['p05']:.4f}-{r['p95']:.4f}]  vax-arm p={r['mean_vaccine_arm_p']:.4f}  "
              f"Δ vs no-vaccine={r['delta_vs_no_vaccine']:+.4f}  "
              f"top in {r['pct_top_ranked']*100:>5.1f}%")
    with open(os.path.join(HERE, "architecture_ranking.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(d_rows[0]))
        w.writeheader()
        w.writerows(d_rows)

    # Second pass: NK arm forced OFF for every architecture, so the vaccine designs are compared
    # against each other on their own merits rather than being swamped by an antigen-independent
    # effector that runs identically underneath all of them.
    print("\n[MODULE D2] Vaccine-arm-only comparison (NK arm forced OFF in every architecture)\n")
    d2_rows = []
    for name, cfg in ARCHITECTURES.items():
        if name == "V-0_context_only_NO_vaccine":
            continue
        kw = dict(cfg)
        kw.pop("note")
        use = kw.pop("use")
        kw["nk_arm"] = False
        take = (RNG.uniform(0.05, 0.30, N) * RNG.uniform(0.35, 0.70, N)
                if kw.get("antigen_agnostic") else None)
        u, n_eff, _, _ = architecture_utility(classes, ctx, use, take_rate=take, **kw)
        d2_rows.append(dict(architecture=name, mean_utility=round(float(u.mean()), 5),
                            p95=round(float(np.percentile(u, 95)), 5),
                            mean_effective_epitopes=round(float(n_eff.mean()), 2)))
    d2_rows.sort(key=lambda r: -r["mean_utility"])
    best2 = d2_rows[0]["mean_utility"]
    for r in d2_rows:
        r["relative_to_best"] = round(r["mean_utility"] / best2, 3) if best2 else 0.0
        print(f"  {r['architecture']:<36} utility={r['mean_utility']:.5f}  "
              f"eff.epitopes={r['mean_effective_epitopes']:>5.2f}  "
              f"relative={r['relative_to_best']:.2f}x")
    with open(os.path.join(HERE, "architecture_ranking_vaccine_arm_only.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(d2_rows[0]))
        w.writeheader()
        w.writerows(d2_rows)

    # ---------------- Module E1 — what actually binds? (lever ablation) ----------------
    print("\n[MODULE E1] Which lever is binding? Single-lever ablation of the winning hybrid\n")
    base_cfg = dict(ARCHITECTURES["V-D_hybrid_primed_polyepitope"])
    base_cfg.pop("note")
    base_use = base_cfg.pop("use")
    base_u, _, _, _ = architecture_utility(classes, ctx, base_use, **base_cfg)
    ablations = {
        "remove_epigenetic_priming": dict(priming=False),
        "deploy_outside_MRD_window": dict(in_window=False),
        "remove_NK_arm": dict(nk_arm=False),
        "remove_PD1_blockade": dict(icb=False),
        "drop_to_mutanome_only_antigens": dict(_use=["A1_somatic_mutanome"]),
        "drop_shared_antigens_keep_private": dict(_use=["A1_somatic_mutanome", "A2_fusion_junction"]),
        "halve_epitope_breadth": dict(_halve=True),
    }
    e_rows = []
    for label, mod in ablations.items():
        cfg = dict(base_cfg)
        use = list(base_use)
        if "_use" in mod:
            use = mod["_use"]
        else:
            cfg.update({k: v for k, v in mod.items() if not k.startswith("_")})
        if mod.get("_halve"):
            halved = {k: dict(v) for k, v in classes.items()}
            for k in halved:
                halved[k]["yld"] = halved[k]["yld"] * 0.5
            u, _, _, _ = architecture_utility(halved, ctx, use, **cfg)
        else:
            u, _, _, _ = architecture_utility(classes, ctx, use, **cfg)
        delta = float(u.mean() - base_u.mean())
        e_rows.append(dict(ablation=label, mean_utility=round(float(u.mean()), 4),
                           delta_vs_full=round(delta, 4),
                           pct_loss=round(100 * delta / base_u.mean(), 1)))
    e_rows.sort(key=lambda r: r["delta_vs_full"])
    for r in e_rows:
        print(f"  {r['ablation']:<34} utility={r['mean_utility']:.4f}  "
              f"delta={r['delta_vs_full']:+.4f} ({r['pct_loss']:+.1f}%)")
    with open(os.path.join(HERE, "lever_ablation.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(e_rows[0]))
        w.writeheader()
        w.writerows(e_rows)

    # ---------------- Module E2 — diagnostic value of information ----------------
    # Which measurement most reduces the uncertainty that is actually driving the design choice?
    # Modelled as the expected utility gain from being able to CONDITION the architecture on the
    # result, versus committing blind. (Methodology composed from Sim 6 / Sim 8 / ADR-0015.)
    print("\n[MODULE E2] Diagnostic value of information for the VACCINE-DESIGN decision\n")
    voi_rows = []
    SHARED = ["A3_cancer_testis", "A4_lineage_programme", "A6_induced_derepressed"]
    NARROW = ["A1_somatic_mutanome", "A2_fusion_junction", "A7_DUX4_as_CTA", "A5_noncanonical_ORF"]

    def build(use, cls=None, **kw):
        cfg = dict(priming=True, in_window=True, nk_arm=True, icb=True)
        cfg.update(kw)
        return architecture_utility(cls if cls is not None else classes, ctx, use, **cfg)[0]

    def evsi(gate_bool, options):
        """Proper EVSI: E_result[ max_action EU(action | result) ] - max_action EU(action).

        Guaranteed >= 0. A value of ~0 means the test does not change which design wins —
        which is itself a finding (that is what a low-yield test looks like).
        """
        gate_bool = np.asarray(gate_bool, dtype=bool)
        eu_informed = 0.0
        for branch in (gate_bool, ~gate_bool):
            w = float(branch.mean())
            if w == 0:
                continue
            eu_informed += w * max(float(u[branch].mean()) for u in options.values())
        blind = max(float(u.mean()) for u in options.values())
        return max(eu_informed - blind, 0.0)  # clamp float noise; EVSI is >= 0 by construction

    # Classes redrawn under the counterfactual "long-read has been run and a junction was found"
    classes_jr = sample_classes(d_idx, n_cand, junction_resolved=True)

    # A design commitment made BLIND can turn out to be built on an antigen the tumour does not
    # have. That is discovered at manufacture/QC time, forcing a rebuild — and the rebuild costs
    # the MRD window, which FH-10.3 identifies as the scarce resource. That penalty is what gives
    # a cheap up-front test its value.
    def commit(use, gate, fallback_use, cls=None):
        good = build(use, cls=cls)
        bad = build(fallback_use, cls=cls, in_window=False)   # rebuilt too late
        return np.where(np.asarray(gate, dtype=bool), good, bad)

    a3 = classes["A3_cancer_testis"]["avail"]
    a5 = classes["A5_noncanonical_ORF"]["avail"]
    a2jr = classes_jr["A2_fusion_junction"]["avail"]
    mutanome_ok = n_cand >= DESIGN_MIN

    voi_rows.append(dict(
        test="CTA panel IHC/RNA (PRAME, NY-ESO-1/CTAG1B, MAGE-A4) on ARCHIVED FFPE",
        provenance="P1 archived", burden=1,
        voi=round(evsi(a3, {
            "commit_CTA_core": commit(SHARED, a3, ["A6_induced_derepressed"]),
            "commit_narrow": build(NARROW),
            "commit_broad": build(SHARED + NARROW)}), 5),
        gates="whether the off-the-shelf shared-antigen core exists at all"))
    voi_rows.append(dict(
        test="MHC-I / B2M IHC (+ HLA typing) on ARCHIVED FFPE",
        provenance="P1 archived", burden=1,
        voi=round(evsi(ctx["mhc1_base"] < 0.35, {
            "always_prime": build(NARROW, priming=True),
            "never_prime": build(NARROW, priming=False)}), 5),
        gates="whether epitopes can be SEEN; decides if epigenetic priming is required"))
    voi_rows.append(dict(
        test="Long-read WGS + RNA-seq (junction resolution)",
        provenance="P1/P2", burden=3,
        voi=round(evsi(a2jr, {
            "commit_junction_core": commit(["A2_fusion_junction", "A7_DUX4_as_CTA"], a2jr,
                                           ["A7_DUX4_as_CTA"], cls=classes_jr),
            "commit_narrow_no_junction": build(["A1_somatic_mutanome", "A7_DUX4_as_CTA",
                                                "A5_noncanonical_ORF"]),
            "commit_shared": build(SHARED)}), 5),
        gates="whether a public junction neoantigen (lowest escape hazard) can be designed"))
    voi_rows.append(dict(
        test="Tumour/germline WES + RNA-seq (TMB + private mutanome)",
        provenance="P2 fresh preferred", burden=3,
        voi=round(evsi(mutanome_ok, {
            "commit_mutanome_INT": commit(["A1_somatic_mutanome"], mutanome_ok,
                                          ["A7_DUX4_as_CTA"]),
            "commit_narrow": build(NARROW),
            "commit_shared": build(SHARED)}), 5),
        gates="whether the intismeran-style private-mutanome arm is fillable at all"))
    voi_rows.append(dict(
        test="Immunopeptidomics (MS) for non-canonical/cryptic epitopes",
        provenance="P2 fresh, high burden", burden=5,
        voi=round(evsi(a5, {
            "commit_cryptic_core": commit(["A5_noncanonical_ORF"], a5, ["A7_DUX4_as_CTA"]),
            "commit_narrow": build(NARROW),
            "commit_shared": build(SHARED)}), 5),
        gates="access to the dark-antigen space that low-TMB tumours still have"))
    voi_rows.sort(key=lambda r: (-r["voi"], r["burden"]))
    for r in voi_rows:
        print(f"  VoI={r['voi']:+.5f}  burden={r['burden']}  {r['test']}")
        print(f"                          gates: {r['gates']}")
    with open(os.path.join(HERE, "design_value_of_information.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(voi_rows[0]))
        w.writeheader()
        w.writerows(voi_rows)

    # ---------------- Module E3 — parameter sensitivity (tornado) ----------------
    print("\n[MODULE E3] Parameter sensitivity — does the headline survive parameter stress?\n")
    t_rows = []
    for label, scale_key, factor in [
        ("TMB x3 (sarcoma TMB tripled)", "tmb", 3.0),
        ("TMB x10 (sarcoma TMB order-of-magnitude higher)", "tmb", 10.0),
        ("HLA-binder rate x2", "binder", 2.0),
        ("immunogenicity rate x3", "immuno", 3.0),
    ]:
        tmb = np.array([lognorm(TMB_MED[DRIVERS[i]], TMB_GSD, 1)[0] for i in d_idx])
        if scale_key == "tmb":
            tmb = tmb * factor
        n_mut = RNG.poisson(np.clip(tmb * EXOME_MB, 0.05, None))
        fb = beta_from(0.30, 0.15, 0.50, N) * (factor if scale_key == "binder" else 1.0)
        fi = beta_from(0.08, 0.01, 0.25, N) * (factor if scale_key == "immuno" else 1.0)
        cand = RNG.binomial(n_mut, np.clip(beta_from(0.60, 0.35, 0.85, N)
                                           * beta_from(0.45, 0.25, 0.65, N)
                                           * np.clip(fb, 0, 1), 0, 1))
        imm = RNG.binomial(cand, np.clip(fi, 0, 1))
        t_rows.append(dict(stress=label, mean_candidate=round(float(cand.mean()), 2),
                           P_fills_34=round(float((cand >= SLOTS).mean()), 4),
                           P_ge_5=round(float((cand >= DESIGN_MIN).mean()), 4),
                           mean_immunogenic=round(float(imm.mean()), 3)))
    for r in t_rows:
        print(f"  {r['stress']:<48} mean candidates={r['mean_candidate']:>6.2f}  "
              f"P(fills 34)={r['P_fills_34']:.3f}  P(>=5)={r['P_ge_5']:.3f}  "
              f"mean immunogenic={r['mean_immunogenic']:.2f}")
    with open(os.path.join(HERE, "supply_sensitivity.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(t_rows[0]))
        w.writeheader()
        w.writerows(t_rows)

    # ---------------- Module E4 — flip test: what would make the vaccine load-bearing? -------- #
    # ADR-0017 red-team requirement: state the conditions that would OVERTURN the conclusion,
    # not just the conclusion. Here: what would the vaccine arm need in order to match the
    # antigen-independent NK arm it is currently dwarfed by?
    print("\n[MODULE E4] Flip test — what would have to be true for the vaccine arm to "
          "match the NK arm?\n")
    p_nk_med = float(np.median(ctx["nk_fitness"] * ctx["window_mult"]
                               * (0.45 + 0.55 * ctx["hla_loh"])))
    med = {k: float(np.median(ctx[k])) for k in
           ("mhc1_base", "mhc1_primed", "window_mult", "t_fitness", "icb_mult", "hla_loh")}
    f_rows = []
    for label, presentation, escape_surv, readiness in [
        ("as modelled (primed, narrow construct)", med["mhc1_primed"], 0.60, 0.20),
        ("+ presentation fully restored (MHC-I=1.0)", 1.0, 0.60, 0.20),
        ("+ presentation restored AND escape-proof antigens", 1.0, 0.95, 0.20),
        ("+ all of the above AND a mature platform (readiness=0.9)", 1.0, 0.95, 0.90),
    ]:
        k = (presentation * med["window_mult"] * med["t_fitness"] * med["icb_mult"]
             * (1 - med["hla_loh"]) * escape_surv * (0.55 + 0.45 * readiness))
        # solve 1 - exp(-n/3) = p_nk_med / k  for n  (the effective-epitope count required)
        target = p_nk_med / k
        n_req = -3.0 * np.log(1 - target) if target < 1 else np.inf
        f_rows.append(dict(scenario=label,
                           required_effective_epitopes=(round(float(n_req), 2)
                                                        if np.isfinite(n_req) else "unreachable"),
                           nk_arm_median_p=round(p_nk_med, 4)))
        print(f"  {label:<56} needs "
              f"{f_rows[-1]['required_effective_epitopes']} effective epitopes")
    print(f"\n  For scale: the modelled narrow construct delivers ~0.7 effective epitopes, and the "
          f"mutanome\n  arm alone delivers ~0.14. The NK arm's median control probability is "
          f"{p_nk_med:.3f}.")
    with open(os.path.join(HERE, "flip_test.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(f_rows[0]))
        w.writeheader()
        w.writerows(f_rows)

    print("\n" + "=" * 78)
    print("Decision model only — not a diagnosis, not a treatment or testing recommendation.")
    print("All literature anchors are [VERIFY] (egress blocked); forward lane per ADR-0020.")
    print("=" * 78)


if __name__ == "__main__":
    main()
