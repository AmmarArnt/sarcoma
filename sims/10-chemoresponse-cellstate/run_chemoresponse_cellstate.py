#!/usr/bin/env python3
"""Sim 10 — Chemo-response phenotype as evidence: re-conditioning the latent driver AND
resolving the therapeutically-decisive DNA-damage-response (DDR) cell state.

WHY THIS SIM EXISTS
-------------------
Sim 8 modelled the fusion-unconfirmed patient's DRIVER as a latent variable D (D1..D5) under a
literature prior, and concluded "resolve the driver first" (long-read WGS+RNA-seq top EVSI).
Sim 8 explicitly flagged its own extension point:

    "Assumes the generic fusion-unconfirmed state. If this patient already had DUX4 IHC /
     methylation / long-read done, condition the prior on those results."

This patient has since produced something Sim 8 did not model: a **deep, twice-repeated
chemotherapy response** —
    O1 = excellent histologic response to first-line VDC/IE (>95% necrosis at resection, Jan 2025)
    O2 = complete radiographic response of relapsed lung nodules after 4 cycles of ifosfamide (2026)

That is not a molecular test, but it IS a likelihood-bearing observation, because the two leading
driver hypotheses have OPPOSITE, molecularly-named DDR phenotypes:
  * canonical CIC::DUX4 is chemo-RESISTANT, and the named mechanism is POLE upregulation +
    proficient DNA repair (npj Precis Oncol 2025) -> only ~30% of CIC patients respond well;
  * Ewing/EWSR1-FET is chemo-SENSITIVE, and the named mechanism is EWS-FLI1 transactivation of
    SLFN11, which converts replication stress into irreversible fork arrest (Clin Cancer Res 2015)
    -> ~53% good histologic response.

MODEL STRUCTURE (the key design choice)
---------------------------------------
We do NOT map driver -> response directly. We insert the mechanism as an explicit latent layer:

        D (driver)  ->  S (DDR / SLFN11 cell state)  ->  O (observed chemo response)

    S in {S_hi = SLFN11-high / "sensing-competent, repair-limited",
          S_lo = SLFN11-low  / "repair-proficient" (the POLE-high CIC phenotype)}

so that  P(O|D) = sum_S P(O|S) P(S|D).

This matters for three reasons:
  (1) it forces the parameters to be MECHANISTIC rather than fitted-to-outcome;
  (2) it lets the model be validated against BOTH published response rates simultaneously
      (see the CONSISTENCY CHECK printed at run time: the D1 and D4 marginals reproduce the
      published ~30% CIC and ~53% Ewing good-response rates without being fitted to them);
  (3) it separates the two questions that actually matter clinically and answers them separately:
      "which driver?" (D) versus "which DDR state, i.e. what do we DO?" (S).

The headline result falls out of (3) and is not obvious in advance.

TIER / STATUS
-------------
Bayesian DECISION model (Mechanistic/Theoretical tier). NOT a diagnosis, NOT medical advice, NOT a
treatment recommendation. Parameters are transparent mechanistic judgements anchored to the
literature listed in MANIFEST.md; every conclusion is reported with a sensitivity sweep because the
likelihood parameters are estimates, not measurements.
"""
from __future__ import annotations
import os
import csv
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(20260802)
N_SWEEP = 20000

# --------------------------------------------------------------------------- #
# 1. Latent driver D — identical hypothesis space and prior as Sim 8 (ADR-0008)
# --------------------------------------------------------------------------- #
DRIVERS = ["D1_cryptic_CICDUX4", "D2_rare_partner", "D3_nonfusion_CIC_LOF",
           "D4_phenocopy_misclassified", "D5_orphan"]
PRIOR_D = np.array([0.45, 0.12, 0.10, 0.20, 0.13])
PRIOR_D_RANGE = {                      # Sim 8's literature ranges, swept here too
    "D1_cryptic_CICDUX4":         (0.30, 0.60),
    "D2_rare_partner":            (0.05, 0.22),
    "D3_nonfusion_CIC_LOF":       (0.03, 0.20),
    "D4_phenocopy_misclassified": (0.10, 0.35),
    "D5_orphan":                  (0.05, 0.25),
}

# --------------------------------------------------------------------------- #
# 2. Latent DDR / SLFN11 cell state S, conditioned on the driver: P(S_hi | D)
#    S_hi = SLFN11-high, "sensing-competent but repair-limited" (Ewing-like DDR)
#    S_lo = SLFN11-low,  "repair-proficient"  (the POLE-high canonical CIC::DUX4 DDR)
# --------------------------------------------------------------------------- #
P_SHI_GIVEN_D = np.array([
    0.20,   # D1 canonical CIC::DUX4 — POLE-high / repair-proficient is its named phenotype
    0.30,   # D2 rare non-DUX4 partner — CIC-class output, but partner-dependent; little data
    0.35,   # D3 non-fusion CIC LOF — CIC transcriptional output without the fusion protein
    0.75,   # D4 phenocopy / Ewing-like — EWS-FLI1 directly transactivates SLFN11
    0.45,   # D5 orphan — deliberately uninformative, near the midpoint
])
P_SHI_GIVEN_D_RANGE = np.array([
    (0.08, 0.35),
    (0.15, 0.50),
    (0.15, 0.55),
    (0.55, 0.90),
    (0.25, 0.65),
])

# --------------------------------------------------------------------------- #
# 3. Observation likelihoods P(O | S). Two response events, taken as conditionally
#    independent GIVEN S — the tumour's DDR state is their common cause, which is
#    exactly the conditional-independence structure the mechanism implies.
#      O1 = excellent histologic response (>95% necrosis) to first-line VDC/IE
#      O2 = complete radiographic response of relapsed lung nodules to 4x ifosfamide
#    O2 is deliberately given a LOWER likelihood even under S_hi: rEECur showed high-dose
#    ifosfamide gives only ~5.7 months median EFS in relapsed Ewing, so a relapse-setting CR
#    is a favourable-but-not-routine event even in genuinely chemo-sensitive disease.
# --------------------------------------------------------------------------- #
P_O1_GIVEN_S = np.array([0.70, 0.15])       # [S_hi, S_lo]
P_O2_GIVEN_S = np.array([0.55, 0.10])
P_O1_RANGE = np.array([(0.55, 0.85), (0.05, 0.28)])
P_O2_RANGE = np.array([(0.40, 0.72), (0.03, 0.20)])

STATES = ["S_hi_SLFN11high_repairLimited", "S_lo_SLFN11low_repairProficient"]


def joint_posterior(prior_d, p_shi_given_d, p_o1_given_s, p_o2_given_s):
    """Return (posterior joint over (D,S), posterior over D, posterior over S,
    marginal P(O|D), evidence P(O)).

    Joint model:  P(D,S,O) = P(D) * P(S|D) * P(O1|S) * P(O2|S)

    The full JOINT is returned, not just the two marginals: after observing O the joint no
    longer factorises as P(D|O) * P(S|D), so any downstream update (the EVSI branches) must
    start from the joint or it will silently use an inconsistent belief.
    """
    p_s_given_d = np.stack([p_shi_given_d, 1.0 - p_shi_given_d], axis=1)   # (5,2)
    lik_s = p_o1_given_s * p_o2_given_s                                    # (2,)
    joint = prior_d[:, None] * p_s_given_d * lik_s[None, :]                # (5,2)
    evidence = joint.sum()
    joint = joint / evidence
    post_d = joint.sum(axis=1)
    post_s = joint.sum(axis=0)
    p_o_given_d = (p_s_given_d * lik_s[None, :]).sum(axis=1)
    return joint, post_d, post_s, p_o_given_d, evidence


def entropy(p):
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


# --------------------------------------------------------------------------- #
# 4. Interventions. Sim 8's seven originals (driver-conditioned only) plus four new
#    entries that this patient's phenotype puts on the table. New entries are scored
#    on the DDR state S as well as the driver D, because that is what gates them.
#
#    p_by_D   : on-target probability per driver (Sim 8 values, unchanged, for comparability)
#    p_by_S   : on-target probability per DDR state, or None if S-independent
#    value    : benefit if it works;  penalty : regret if committed to and it cannot work
# --------------------------------------------------------------------------- #
INTERVENTIONS = {
    # ---- Sim 8 originals (unchanged parameters — so any movement is due to the update alone)
    "BRD4_BETi":                    dict(p_by_D=[0.90, 0.85, 0.80, 0.60, 0.80], p_by_S=None,
                                         value=2.0, penalty=0.3, cls="throttle (V1)"),
    "p300_CBP_i":                   dict(p_by_D=[0.90, 0.50, 0.50, 0.30, 0.50], p_by_S=None,
                                         value=2.0, penalty=0.8, cls="writer (V1/V3/V4)"),
    "CDK4_CCND1_i":                 dict(p_by_D=[0.80, 0.80, 0.80, 0.75, 0.75], p_by_S=None,
                                         value=2.0, penalty=0.3, cls="cell-cycle (V1)"),
    "EZH2i_MHCI_prime":             dict(p_by_D=[0.80, 0.80, 0.50, 0.40, 0.50], p_by_S=None,
                                         value=1.5, penalty=0.5, cls="epigenetic bridge (V3->V4)"),
    "immune_NK_checkpt":            dict(p_by_D=[0.70, 0.70, 0.70, 0.70, 0.70], p_by_S=None,
                                         value=1.5, penalty=0.3, cls="host/driver-agnostic (V4)"),
    "MCL1i_reArm_DUX4":             dict(p_by_D=[0.85, 0.05, 0.00, 0.00, 0.00], p_by_S=None,
                                         value=3.0, penalty=2.0, cls="DUX4-fragility (contingent)"),
    "junction_ASO_vax":             dict(p_by_D=[0.90, 0.90, 0.00, 0.00, 0.00], p_by_S=None,
                                         value=3.0, penalty=2.5, cls="junction-specific (contingent)"),

    # ---- New entries put on the table by the chemo-response phenotype
    # Preserve the demonstrated chemo-sensitivity by blocking EZH2/H3K27me3-mediated SLFN11
    # silencing — the documented route to "chemosensitive relapse" (Cancer Cell 2017).
    # Needs SLFN11 to still be there, i.e. it is gated on S_hi, not on the driver.
    "SLFN11_maintenance_EZH2i_HDACi": dict(p_by_D=None, p_by_S=[0.75, 0.10],
                                           value=2.5, penalty=0.6,
                                           cls="DDR-state maintenance (V3, doubles as V4 priming)"),
    # The opposite branch: SLFN11-LOW cells are synthetic-lethal with ATR/CHK1 inhibition.
    "ATR_CHK1i_synthlethal":         dict(p_by_D=None, p_by_S=[0.20, 0.65],
                                          value=2.0, penalty=0.8,
                                          cls="DDR synthetic-lethal (V3)"),
    # The reservoir that survived a regimen the bulk was exquisitely sensitive to: drug-tolerant
    # persisters. Their state is epigenetic/reversible and GPX4-dependent -> ferroptosis-vulnerable.
    "GPX4_ferroptosis_persister":    dict(p_by_D=None, p_by_S=[0.55, 0.55],
                                          value=2.5, penalty=0.7,
                                          cls="persister-directed (V3, driver-agnostic)"),
    # V4 deployed in the window the chemotherapy itself created: lowest tumour burden + chemo
    # lymphodepletion -> homeostatic-proliferation rebound. Host-side, so driver-agnostic.
    "immune_MRD_window_NKfirst":     dict(p_by_D=None, p_by_S=[0.72, 0.72],
                                          value=2.5, penalty=0.4,
                                          cls="immune in MRD window (V4)"),
}
INAMES = list(INTERVENTIONS)


def expected_payoff(post_d, post_s, name):
    """E[ p_work*value - (1-p_work)*penalty ] under the current belief."""
    spec = INTERVENTIONS[name]
    if spec["p_by_D"] is not None:
        pw = float(np.asarray(spec["p_by_D"]) @ post_d)
    else:
        pw = float(np.asarray(spec["p_by_S"]) @ post_s)
    return pw * spec["value"] - (1.0 - pw) * spec["penalty"], pw


def decision_value(post_d, post_s):
    return sum(max(0.0, expected_payoff(post_d, post_s, k)[0]) for k in INAMES)


def pursued_set(post_d, post_s):
    return [k for k in INAMES if expected_payoff(post_d, post_s, k)[0] > 0]


# --------------------------------------------------------------------------- #
# 5. Tests — EVSI recomputed AFTER the phenotype update, including two tests the
#    phenotype itself makes relevant (SLFN11 IHC; BH3 profiling).
# --------------------------------------------------------------------------- #
HAS_DUX4_TAD     = np.array([0.97, 0.05, 0.02, 0.02, 0.05])
P_METH_CIC_CLASS = np.array([0.97, 0.95, 0.85, 0.03, 0.60])
P_FUSION_FINDABLE= np.array([0.95, 0.92, 0.05, 0.05, 0.05])
# SLFN11 IHC reads the S layer directly (imperfectly: sens ~0.85, spec ~0.85).
SLFN11_IHC_SENS, SLFN11_IHC_SPEC = 0.85, 0.85
# BH3 profiling reads apoptotic priming, which is correlated with S but is NOT the same variable.
BH3_PRIMED_GIVEN_S = np.array([0.80, 0.45])


def test_outcomes_D(name):
    """Tests that inform D directly. Returns [(label, per-driver likelihood vector), ...]."""
    if name == "DUX4_IHC":
        return [("DUX4+", HAS_DUX4_TAD), ("DUX4-", 1 - HAS_DUX4_TAD)]
    if name == "methylation_array":
        return [("CICclass", P_METH_CIC_CLASS), ("notCIC", 1 - P_METH_CIC_CLASS)]
    if name == "longread_WGS_RNAseq":
        find = P_FUSION_FINDABLE
        return [("junction_DUX4", find * HAS_DUX4_TAD),
                ("junction_nonDUX4", find * (1 - HAS_DUX4_TAD)),
                ("no_junction", 1 - find)]
    return None


def test_outcomes_S(name):
    """Tests that inform S directly. Returns [(label, per-state likelihood vector), ...]."""
    if name == "SLFN11_IHC":
        return [("SLFN11+", np.array([SLFN11_IHC_SENS, 1 - SLFN11_IHC_SPEC])),
                ("SLFN11-", np.array([1 - SLFN11_IHC_SENS, SLFN11_IHC_SPEC]))]
    if name == "BH3_profiling":
        return [("highly_primed", BH3_PRIMED_GIVEN_S),
                ("not_primed", 1 - BH3_PRIMED_GIVEN_S)]
    return None


def evsi(joint, name):
    """Expected value of sample information, computed on the POST-phenotype joint belief.

    A test is worth something only insofar as it can still flip a pursue/don't-pursue decision.
    `joint` is the full posterior over (D,S); a D-test reweights rows, an S-test reweights
    columns, and both marginals are recomputed from the updated joint so the two layers stay
    coherent. Because decision_value is a max of linear functions of the belief it is convex,
    which guarantees EVSI >= 0 — a negative value here would mean the base belief and the
    branch beliefs were built inconsistently.
    """
    base_d, base_s = joint.sum(axis=1), joint.sum(axis=0)
    base = decision_value(base_d, base_s)
    base_set = set(pursued_set(base_d, base_s))

    outs_d, outs_s = test_outcomes_D(name), test_outcomes_S(name)
    total, flips = 0.0, set()
    for _label, lik in (outs_d if outs_d is not None else outs_s):
        j = joint * (np.asarray(lik)[:, None] if outs_d is not None
                     else np.asarray(lik)[None, :])
        p_out = j.sum()
        if p_out <= 1e-12:
            continue
        j = j / p_out
        nd, ns = j.sum(axis=1), j.sum(axis=0)
        total += p_out * decision_value(nd, ns)
        flips |= set(pursued_set(nd, ns)) ^ base_set
    return total - base, sorted(flips)


# --------------------------------------------------------------------------- #
# 6. Run
# --------------------------------------------------------------------------- #
def main() -> None:
    out = lambda n: os.path.join(HERE, n)

    joint, post_d, post_s, p_o_given_d, evidence = joint_posterior(
        PRIOR_D, P_SHI_GIVEN_D, P_O1_GIVEN_S, P_O2_GIVEN_S)

    print("=" * 78)
    print("Sim 10 — chemo-response phenotype as evidence on driver AND DDR cell state")
    print("=" * 78)

    # ---- consistency check against published response rates (NOT fitted) ----
    p_good_single = (np.stack([P_SHI_GIVEN_D, 1 - P_SHI_GIVEN_D], axis=1) * P_O1_GIVEN_S).sum(axis=1)
    print("\n[CONSISTENCY CHECK] single good-response rate implied by the mechanistic S-layer")
    print("  (these were NOT fitted to the outcome literature — they fall out of P(S|D) x P(O1|S))")
    print(f"  D1 canonical CIC::DUX4 -> {p_good_single[0]:.3f}   "
          f"[published: ~0.30 of CIC patients respond well]")
    print(f"  D4 phenocopy/Ewing-like -> {p_good_single[3]:.3f}   "
          f"[published: ~0.53 good histologic response in Ewing]")

    # ---- driver: prior -> posterior ----
    print("\n[1] LATENT DRIVER D — prior vs posterior after the chemo-response phenotype")
    print(f"{'driver':<30}{'prior':>9}{'P(O|D)':>10}{'posterior':>12}{'change':>10}")
    rows = []
    for i, d in enumerate(DRIVERS):
        delta = post_d[i] - PRIOR_D[i]
        print(f"{d:<30}{PRIOR_D[i]:>9.3f}{p_o_given_d[i]:>10.3f}{post_d[i]:>12.3f}{delta:>+10.3f}")
        rows.append(dict(driver=d, prior=round(float(PRIOR_D[i]), 4),
                         likelihood_O_given_D=round(float(p_o_given_d[i]), 4),
                         posterior=round(float(post_d[i]), 4), change=round(float(delta), 4)))
    with open(out("driver_posterior.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

    top_prior, top_post = DRIVERS[int(PRIOR_D.argmax())], DRIVERS[int(post_d.argmax())]
    print(f"\n  most-likely driver: {top_prior}  ->  {top_post}"
          f"   {'*** FLIPPED ***' if top_prior != top_post else '(unchanged)'}")
    hD0, hD1 = entropy(PRIOR_D), entropy(post_d)
    print(f"  entropy over D: {hD0:.3f} -> {hD1:.3f} bits ({hD1 - hD0:+.3f})")
    if hD1 > hD0:
        print("  NOTE: entropy over D INCREASED. The phenotype did not identify the driver — it")
        print("        moved mass off a peaked D1 into a flatter D1-vs-D4 contest. The driver")
        print("        question got HARDER, not easier. Contrast with S in [2].")

    # ---- DDR state: the variable that actually gates therapy ----
    p_shi_prior = float(P_SHI_GIVEN_D @ PRIOR_D)
    print("\n[2] LATENT DDR / SLFN11 STATE S — the therapeutically decisive variable")
    print(f"{'state':<38}{'prior':>9}{'posterior':>12}")
    print(f"{STATES[0]:<38}{p_shi_prior:>9.3f}{post_s[0]:>12.3f}")
    print(f"{STATES[1]:<38}{1-p_shi_prior:>9.3f}{post_s[1]:>12.3f}")
    print(f"  entropy over S: {entropy([p_shi_prior, 1-p_shi_prior]):.3f} -> {entropy(post_s):.3f} bits "
          f"(reduction {entropy([p_shi_prior, 1-p_shi_prior]) - entropy(post_s):+.3f})")
    print(f"\n  >> the phenotype resolves S to {post_s[0]:.1%} while D remains "
          f"{post_d.max():.1%}/{sorted(post_d)[-2]:.1%} ambiguous.")
    with open(out("state_posterior.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["state", "prior", "posterior"])
        w.writerow([STATES[0], round(p_shi_prior, 4), round(float(post_s[0]), 4)])
        w.writerow([STATES[1], round(1 - p_shi_prior, 4), round(float(post_s[1]), 4)])

    # ---- interventions: what moved ----
    pri_s = np.array([p_shi_prior, 1 - p_shi_prior])
    print("\n[3] INTERVENTION RE-RANKING (expected payoff; prior belief -> posterior belief)")
    print(f"{'intervention':<34}{'p_on-target':>12}{'payoff_pre':>12}{'payoff_post':>13}{'delta':>9}  class")
    irows = []
    for k in INAMES:
        pay_post, pw_post = expected_payoff(post_d, post_s, k)
        pay_pre, _ = expected_payoff(PRIOR_D, pri_s, k)
        print(f"{k:<34}{pw_post:>12.3f}{pay_pre:>12.3f}{pay_post:>13.3f}"
              f"{pay_post - pay_pre:>+9.3f}  {INTERVENTIONS[k]['cls']}")
        irows.append(dict(intervention=k, p_on_target_post=round(pw_post, 4),
                          payoff_prior=round(pay_pre, 4), payoff_posterior=round(pay_post, 4),
                          delta=round(pay_post - pay_pre, 4),
                          pursued_post=pay_post > 0, cls=INTERVENTIONS[k]["cls"]))
    irows.sort(key=lambda r: -r["payoff_posterior"])
    with open(out("intervention_reranking.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(irows[0])); w.writeheader(); w.writerows(irows)

    print(f"\n  pursue-set BEFORE the phenotype: {sorted(pursued_set(PRIOR_D, pri_s))}")
    print(f"  pursue-set AFTER  the phenotype: {sorted(pursued_set(post_d, post_s))}")

    # ---- tests: EVSI recomputed on the post-phenotype belief ----
    print("\n[4] TEST VALUE (EVSI) — recomputed AFTER the phenotype update")
    print(f"{'test':<26}{'EVSI':>9}  decisions it can still flip")
    trows = []
    for t in ["longread_WGS_RNAseq", "DUX4_IHC", "methylation_array", "SLFN11_IHC", "BH3_profiling"]:
        v, flips = evsi(joint, t)
        print(f"{t:<26}{v:>9.4f}  {', '.join(flips) if flips else '(none — confirmatory only)'}")
        trows.append(dict(test=t, evsi=round(float(v), 4), flips=";".join(flips)))
    trows.sort(key=lambda r: -r["evsi"])
    with open(out("test_value_of_information.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(trows[0])); w.writeheader(); w.writerows(trows)

    # ---- sensitivity sweep over EVERY estimated parameter ----
    print(f"\n[5] SENSITIVITY SWEEP ({N_SWEEP} samples over the driver prior, P(S|D), and P(O|S) ranges)")
    flip_count = 0
    shi_samples, d4_top, slfn_pursued, slfn_beats_atr, mcl1_dropped = [], 0, 0, 0, 0
    for _ in range(N_SWEEP):
        lo = np.array([PRIOR_D_RANGE[d][0] for d in DRIVERS])
        hi = np.array([PRIOR_D_RANGE[d][1] for d in DRIVERS])
        pr = RNG.uniform(lo, hi); pr = pr / pr.sum()
        ps = RNG.uniform(P_SHI_GIVEN_D_RANGE[:, 0], P_SHI_GIVEN_D_RANGE[:, 1])
        o1 = RNG.uniform(P_O1_RANGE[:, 0], P_O1_RANGE[:, 1])
        o2 = RNG.uniform(P_O2_RANGE[:, 0], P_O2_RANGE[:, 1])
        o1 = np.sort(o1)[::-1]; o2 = np.sort(o2)[::-1]   # keep S_hi >= S_lo (model definition)
        _j, pd_, ps_, _, _ = joint_posterior(pr, ps, o1, o2)
        shi_samples.append(ps_[0])
        if pd_.argmax() == 3:
            d4_top += 1
        if pd_.argmax() != pr.argmax():
            flip_count += 1
        pay = {k: expected_payoff(pd_, ps_, k)[0] for k in INAMES}
        if pay["SLFN11_maintenance_EZH2i_HDACi"] > 0:
            slfn_pursued += 1
        # the decision the DDR-state layer actually forces: which DDR branch to back
        if pay["SLFN11_maintenance_EZH2i_HDACi"] > pay["ATR_CHK1i_synthlethal"]:
            slfn_beats_atr += 1
        if pay["MCL1i_reArm_DUX4"] <= 0:
            mcl1_dropped += 1
    shi_samples = np.array(shi_samples)
    stats = [
        ("n_samples", N_SWEEP),
        ("P_Shi_median", round(float(np.median(shi_samples)), 4)),
        ("P_Shi_ci5", round(float(np.percentile(shi_samples, 5)), 4)),
        ("P_Shi_ci95", round(float(np.percentile(shi_samples, 95)), 4)),
        ("pct_P_Shi_gt_0.80", round(100 * float((shi_samples > 0.80).mean()), 2)),
        ("pct_D4_top_driver", round(100 * d4_top / N_SWEEP, 2)),
        ("pct_driver_flip", round(100 * flip_count / N_SWEEP, 2)),
        ("pct_SLFN11maint_in_pursue_set", round(100 * slfn_pursued / N_SWEEP, 2)),
        ("pct_SLFN11maint_beats_ATRi", round(100 * slfn_beats_atr / N_SWEEP, 2)),
        ("pct_MCL1_dropped_from_pursue_set", round(100 * mcl1_dropped / N_SWEEP, 2)),
    ]
    print(f"  P(S_hi | phenotype): median {np.median(shi_samples):.3f}   "
          f"90% CI [{np.percentile(shi_samples, 5):.3f}, {np.percentile(shi_samples, 95):.3f}]")
    print(f"  P(S_hi) > 0.80 in {100*(shi_samples > 0.80).mean():.1f}% of samples")
    print(f"  D4 (phenocopy) is the top driver hypothesis in {100*d4_top/N_SWEEP:.1f}% of samples")
    print(f"  the update FLIPS the most-likely driver in {100*flip_count/N_SWEEP:.1f}% of samples")
    print(f"  SLFN11-maintenance stays in the pursue-set in {100*slfn_pursued/N_SWEEP:.1f}% of samples")
    print(f"  SLFN11-maintenance beats the ATR/CHK1i branch in {100*slfn_beats_atr/N_SWEEP:.1f}% of samples")
    print(f"  MCL1 're-arm' drops OUT of the pursue-set in {100*mcl1_dropped/N_SWEEP:.1f}% of samples")
    with open(out("sensitivity_sweep.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["metric", "value"]); w.writerows(stats)

    # ---- falsifiers ----
    print("\n[6] FALSIFIERS — single results that would overturn the above")
    for label, txt in [
        ("SLFN11 IHC negative on relapse tissue",
         "the S_hi inference is wrong; chemo-sensitivity runs through another route "
         "(e.g. HR/ARID1A) -> SLFN11-maintenance drops out, ATR/CHK1i branch opens"),
        ("methylation array returns CIC class",
         "D4 collapses; posterior returns toward D1/D3 and the CIC-directed catalog re-strengthens"),
        ("long-read WGS finds a canonical CIC::DUX4 junction",
         "D1 confirmed despite the phenotype -> this is a chemo-sensitive CIC::DUX4 outlier; "
         "the MCL1/junction lines re-open and the DDR read must be re-derived"),
        ("relapse biopsy shows POLE-high / repair-proficient signature",
         "contradicts S_hi directly; the whole SLFN11-maintenance rationale fails"),
    ]:
        print(f"  - if {label}\n      -> {txt}")

    with open(out("entities.txt"), "w") as fh:
        fh.write("\n".join([
            "SLFN11", "EZH2", "H3K27me3", "PRC2", "POLE", "EWSR1", "FLI1", "EWS-FLI1",
            "CIC", "DUX4", "CIC-DUX4", "BCOR", "ATR", "CHEK1", "GPX4", "KDM5A", "KDM5B",
            "MCL1", "ARID1A", "BRD4", "CDK4", "CCND1", "HLA-E", "MHC class I", "NKG2A",
            "ifosfamide", "cyclophosphamide", "doxorubicin", "vincristine", "etoposide",
            "entinostat", "romidepsin", "tazemetostat", "valemetostat", "decitabine",
            "CIC-rearranged sarcoma", "Ewing sarcoma", "drug-tolerant persister", "ferroptosis",
        ]) + "\n")
    print("\nWrote: driver_posterior.csv, state_posterior.csv, intervention_reranking.csv,")
    print("       test_value_of_information.csv, sensitivity_sweep.csv, entities.txt")
    print("\nDecision model — NOT a diagnosis, NOT medical advice.")


if __name__ == "__main__":
    main()
