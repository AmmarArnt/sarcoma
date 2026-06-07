#!/usr/bin/env python3
"""Sim 8 — Driver-uncertain ("fusion-unconfirmed") intervention-robustness + value-of-information.

The simulated patient is in the ~5% CIC-rearranged subgroup with NO confirmed fusion, so the true
molecular DRIVER is a latent variable. Rather than guess it, this model:
  (1) marginalizes every catalog intervention over a literature-anchored prior p(D) over driver
      hypotheses  -> a ROBUSTNESS ranking (what is on-target regardless of the unknown);
  (2) computes the expected value of sample information (EVSI) for three resolving tests
      (DUX4 IHC, DNA-methylation array, long-read WGS+RNA-seq) -> what it is worth to find out;
  (3) sweeps the prior (Dirichlet) so conclusions are reported as robust-to-prior, not point claims.

This is the FORWARD build recipe (Sim 7) re-expressed for the unconfirmed case, and it reuses the
value-of-information methodology from Sim 6 (ADR-0001). It is a Bayesian DECISION model
(Mechanistic/Theoretical tier), NOT a diagnosis and NOT medical advice. All parameters trace to
`simulation-output/tumorigenesis-reverse-engineering/driver-uncertainty-specialist.md`.

EVSI is the decision-theoretically correct way to value information: a test has value only when it can
flip which interventions are worth committing to. Robust interventions (low regret) are pursued anyway;
contingent high-value ones (MCL1/DUX4-fragility; junction-specific) are gated by an unknown the tests
resolve -> that gap is where the information is worth money.
"""
from __future__ import annotations
import os, csv, itertools
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(20260607)

# --------------------------------------------------------------------------- #
# Driver hypotheses (latent variable D). See driver-uncertainty-specialist.md.
# --------------------------------------------------------------------------- #
DRIVERS = ["D1_cryptic_CICDUX4", "D2_rare_partner", "D3_nonfusion_CIC_LOF",
           "D4_phenocopy_misclassified", "D5_orphan"]

# Literature-anchored default prior (conditioned on histologically CIC-like, fusion-test-negative).
PRIOR_DEFAULT = np.array([0.45, 0.12, 0.10, 0.20, 0.13])      # sums to 1.0
PRIOR_RANGE = {                                                # for the sweep
    "D1_cryptic_CICDUX4":        (0.30, 0.60),
    "D2_rare_partner":           (0.05, 0.22),
    "D3_nonfusion_CIC_LOF":      (0.03, 0.20),
    "D4_phenocopy_misclassified":(0.10, 0.35),
    "D5_orphan":                 (0.05, 0.25),
}

# Per-driver latent ATTRIBUTES used to model test outcomes (probabilities).
HAS_DUX4_TAD      = np.array([0.97, 0.05, 0.02, 0.02, 0.05])   # P(DUX4 transactivation domain present)
P_METH_CIC_CLASS  = np.array([0.97, 0.95, 0.85, 0.03, 0.60])   # P(methylation array calls "CIC class")
P_FUSION_FINDABLE = np.array([0.95, 0.92, 0.05, 0.05, 0.05])   # P(long-read finds a CIC fusion junction)

# --------------------------------------------------------------------------- #
# Interventions: on-target probability per driver (p_work), benefit value, and
# regret penalty if pursued but it cannot work. Robust items have low penalty;
# contingent items (MCL1/DUX4-fragility, junction-specific) have high penalty.
# --------------------------------------------------------------------------- #
INTERVENTIONS = {
    #                       D1    D2    D3    D4    D5     value  penalty  class
    "BRD4_BETi":         ([0.90, 0.85, 0.80, 0.60, 0.80], 2.0,  0.3, "throttle"),
    "p300_CBP_i":        ([0.90, 0.50, 0.50, 0.30, 0.50], 2.0,  0.8, "writer"),
    "CDK4_CCND1_i":      ([0.80, 0.80, 0.80, 0.75, 0.75], 2.0,  0.3, "cell-cycle"),
    "EZH2i_MHCI_prime":  ([0.80, 0.80, 0.50, 0.40, 0.50], 1.5,  0.5, "epigenetic/immune-bridge"),
    "immune_NK_checkpt": ([0.70, 0.70, 0.70, 0.70, 0.70], 1.5,  0.3, "host/driver-agnostic"),
    "MCL1i_reArm_DUX4":  ([0.85, 0.05, 0.00, 0.00, 0.00], 3.0,  2.0, "DUX4-fragility (contingent)"),
    "junction_ASO_vax":  ([0.90, 0.90, 0.00, 0.00, 0.00], 3.0,  2.5, "junction-specific (contingent)"),
}
INAMES = list(INTERVENTIONS)
PWORK = {k: np.array(v[0]) for k, v in INTERVENTIONS.items()}
VALUE = {k: v[1] for k, v in INTERVENTIONS.items()}
PEN   = {k: v[2] for k, v in INTERVENTIONS.items()}


def marginal_pwork(prior):
    """Robustness score = expected on-target probability under the prior."""
    return {k: float(prior @ PWORK[k]) for k in INAMES}


def expected_payoff_if_pursued(belief, name):
    """E_D[ p_work*value - (1-p_work)*penalty ]  for committing to one intervention."""
    pw = PWORK[name]
    return float(belief @ (pw * VALUE[name] - (1.0 - pw) * PEN[name]))


def decision_value(belief):
    """Optimal pursue-set value: pursue independent items with positive expected payoff.
    Convex in belief -> EVSI >= 0, and >0 exactly when a test flips a pursue decision."""
    return sum(max(0.0, expected_payoff_if_pursued(belief, k)) for k in INAMES)


def pursued_set(belief):
    return [k for k in INAMES if expected_payoff_if_pursued(belief, k) > 0]


def bayes_update(prior, likelihood):
    post = prior * likelihood
    s = post.sum()
    return post / s if s > 0 else prior.copy()


# --------------------------------------------------------------------------- #
# Tests: each has a set of mutually exclusive outcomes with per-driver likelihoods.
# --------------------------------------------------------------------------- #
def test_outcomes(name):
    if name == "DUX4_IHC":                       # binary: positive / negative
        return [("DUX4+", HAS_DUX4_TAD), ("DUX4-", 1 - HAS_DUX4_TAD)]
    if name == "methylation_array":              # binary: CIC class / not CIC class
        return [("CICclass", P_METH_CIC_CLASS), ("notCIC", 1 - P_METH_CIC_CLASS)]
    if name == "longread_WGS_RNAseq":            # finds CIC fusion junction / does not
        # If found, also reveals partner (D1 vs D2). Modeled as 3 outcomes.
        find = P_FUSION_FINDABLE
        # split "found" into DUX4-partner vs non-DUX4-partner using HAS_DUX4_TAD
        found_dux4 = find * HAS_DUX4_TAD
        found_other = find * (1 - HAS_DUX4_TAD)
        nofind = 1 - find
        return [("junction_DUX4", found_dux4),
                ("junction_nonDUX4", found_other),
                ("no_junction", nofind)]
    raise ValueError(name)


def evsi(prior, name):
    """Expected value of sample information for a test."""
    base = decision_value(prior)
    ev = 0.0
    for _, lik in test_outcomes(name):
        p_outcome = float(prior @ lik)
        if p_outcome <= 0:
            continue
        post = bayes_update(prior, lik)
        ev += p_outcome * decision_value(post)
    return ev - base


def entropy(p):
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def expected_posterior_entropy(prior, name):
    h = 0.0
    for _, lik in test_outcomes(name):
        p_outcome = float(prior @ lik)
        if p_outcome <= 0:
            continue
        h += p_outcome * entropy(bayes_update(prior, lik))
    return h


def write_csv(path, rows, fieldnames=None):
    fieldnames = fieldnames or list(rows[0].keys())
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def sample_prior():
    """Sample a prior from the literature ranges, renormalized (a coarse Dirichlet-like sweep)."""
    lo = np.array([PRIOR_RANGE[d][0] for d in DRIVERS])
    hi = np.array([PRIOR_RANGE[d][1] for d in DRIVERS])
    s = lo + RNG.random(len(DRIVERS)) * (hi - lo)
    return s / s.sum()


def main():
    print("=" * 78)
    print("Sim 8 — Driver-uncertain (fusion-unconfirmed) robustness + value-of-information")
    print("=" * 78)
    prior = PRIOR_DEFAULT
    print("\nDriver prior (default):")
    for d, p in zip(DRIVERS, prior):
        print(f"   {d:30s} {p:.2f}   P(DUX4-TAD)={HAS_DUX4_TAD[DRIVERS.index(d)]:.2f}")
    print(f"   prior entropy H(D) = {entropy(prior):.3f} bits")

    # (1) ROBUSTNESS ----------------------------------------------------------
    mw = marginal_pwork(prior)
    rob_rows = []
    for k in sorted(INAMES, key=lambda x: -mw[x]):
        contingent = INTERVENTIONS[k][3].endswith("(contingent)")
        rob_rows.append({"intervention": k,
                         "expected_on_target_prob": round(mw[k], 3),
                         "value": VALUE[k], "regret_penalty": PEN[k],
                         "class": INTERVENTIONS[k][3],
                         "robust_or_contingent": "CONTINGENT" if contingent else "robust"})
    write_csv(os.path.join(HERE, "robustness_ranking.csv"), rob_rows)
    print("\n[1] ROBUSTNESS — expected on-target probability, marginalized over the unknown driver:")
    for r in rob_rows:
        print(f"    {r['intervention']:20s} {r['expected_on_target_prob']:.3f}  "
              f"[{r['robust_or_contingent']}]")
    print(f"    Pursued without any test: {pursued_set(prior)}")

    # (2) VALUE OF INFORMATION ------------------------------------------------
    voi_rows = []
    for t in ["DUX4_IHC", "methylation_array", "longread_WGS_RNAseq"]:
        v = evsi(prior, t)
        h_post = expected_posterior_entropy(prior, t)
        voi_rows.append({"test": t,
                         "EVSI_decision_value": round(v, 4),
                         "expected_posterior_entropy_bits": round(h_post, 3),
                         "entropy_reduction_bits": round(entropy(prior) - h_post, 3)})
    voi_rows.sort(key=lambda r: -r["EVSI_decision_value"])
    write_csv(os.path.join(HERE, "test_value_of_information.csv"), voi_rows)
    print("\n[2] VALUE OF INFORMATION (EVSI = expected gain in decision value from each test):")
    for r in voi_rows:
        print(f"    {r['test']:22s} EVSI={r['EVSI_decision_value']:+.4f}  "
              f"ΔH={r['entropy_reduction_bits']:+.3f} bits")

    # show what each test unlocks (posterior pursue-set per outcome)
    print("\n    What each test can unlock (pursue-set under each outcome):")
    unlock_rows = []
    for t in ["DUX4_IHC", "methylation_array", "longread_WGS_RNAseq"]:
        for label, lik in test_outcomes(t):
            post = bayes_update(prior, lik)
            ps = pursued_set(post)
            newly = [x for x in ps if x not in pursued_set(prior)]
            unlock_rows.append({"test": t, "outcome": label,
                                "p_outcome": round(float(prior @ lik), 3),
                                "pursue_set": "; ".join(ps),
                                "newly_unlocked": "; ".join(newly) or "(none)"})
            if newly:
                print(f"      {t} = {label:16s} (p={float(prior@lik):.2f}) "
                      f"-> unlocks: {', '.join(newly)}")
    write_csv(os.path.join(HERE, "test_unlock_map.csv"), unlock_rows)

    # (3) PRIOR SENSITIVITY SWEEP --------------------------------------------
    N = 5000
    top_robust, top_voi, mcl1_unlocked_noinfo = {}, {}, 0
    rob_first_counts, voi_first_counts = {}, {}
    for _ in range(N):
        pr = sample_prior()
        mwn = marginal_pwork(pr)
        rb = max(mwn, key=lambda x: mwn[x])
        rob_first_counts[rb] = rob_first_counts.get(rb, 0) + 1
        vois = {t: evsi(pr, t) for t in ["DUX4_IHC", "methylation_array", "longread_WGS_RNAseq"]}
        vb = max(vois, key=lambda x: vois[x])
        voi_first_counts[vb] = voi_first_counts.get(vb, 0) + 1
        if "MCL1i_reArm_DUX4" in pursued_set(pr):
            mcl1_unlocked_noinfo += 1
    sweep_rows = []
    print(f"\n[3] PRIOR SWEEP ({N} samples drawn from the literature ranges):")
    print("    Top-robustness intervention across prior samples:")
    for k, c in sorted(rob_first_counts.items(), key=lambda x: -x[1]):
        print(f"      {k:20s} {100*c/N:5.1f}%")
        sweep_rows.append({"metric": "top_robust", "item": k, "pct_of_prior_samples": round(100*c/N, 1)})
    print("    Highest-VoI test across prior samples:")
    for k, c in sorted(voi_first_counts.items(), key=lambda x: -x[1]):
        print(f"      {k:22s} {100*c/N:5.1f}%")
        sweep_rows.append({"metric": "top_voi_test", "item": k, "pct_of_prior_samples": round(100*c/N, 1)})
    print(f"    MCL1/DUX4-fragility pursued WITHOUT a test: "
          f"{100*mcl1_unlocked_noinfo/N:.1f}% of prior samples "
          f"(low => it stays contingent on resolving the driver).")
    sweep_rows.append({"metric": "MCL1_pursued_without_test",
                       "item": "MCL1i_reArm_DUX4", "pct_of_prior_samples": round(100*mcl1_unlocked_noinfo/N, 1)})
    write_csv(os.path.join(HERE, "prior_sweep.csv"), sweep_rows)

    # drivers table + entities
    write_csv(os.path.join(HERE, "drivers.csv"),
              [{"driver": d, "prior_default": prior[i], "P_DUX4_TAD": HAS_DUX4_TAD[i],
                "P_methylation_CICclass": P_METH_CIC_CLASS[i], "P_fusion_findable": P_FUSION_FINDABLE[i]}
               for i, d in enumerate(DRIVERS)])
    with open(os.path.join(HERE, "entities.txt"), "w") as fh:
        fh.write(". ".join(["CIC-DUX4", "CIC", "DUX4", "CIC-NUTM1", "CIC-FOXO4", "CIC-LEUTX",
                            "BCOR", "EWSR1", "ETV4", "MCL1", "EZH2", "BRD4", "CDK4",
                            "DNA methylation", "CIC-rearranged sarcoma"]) + ".\n")

    print("\n[done] wrote robustness_ranking.csv, test_value_of_information.csv, test_unlock_map.csv,")
    print("       prior_sweep.csv, drivers.csv, entities.txt")


if __name__ == "__main__":
    main()
