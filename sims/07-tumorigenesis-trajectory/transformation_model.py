#!/usr/bin/env python3
"""Sim 7 — CIC-DUX4 tumorigenesis as a "build recipe": a Boolean transformation model.

INVERSE of the repo's usual question. Instead of "how do we attack an existing
CIC-DUX4 sarcoma cell," this asks the FORWARD / engineering "steps to reproduce"
question: *what set of perturbations, applied to a normal stem/progenitor cell,
is minimally sufficient to BUILD a fully transformed CIC-DUX4 sarcoma cell, and
does the ORDER of those steps matter?* Each construction step is then mapped back
onto the four fixed attack vectors (V1-V4) so the "undo" of every build step is
explicit — that is the reverse-engineering payoff.

This is a LITERATURE-PARAMETERIZED LOGIC MODEL (same engine class as sims 03-05),
not a data download. Every wiring rule traces to a cited mechanism in
docs/02-cic-sarcoma-knowledge.md / docs/03-dna-genome-protein-interactions.md and
the team's specialist briefs in
simulation-output/tumorigenesis-reverse-engineering/. No fabricated data: the
model encodes published mechanism and then enumerates its consequences exhaustively.
It is a hypothesis-structuring tool (Mechanistic/Theoretical tier), NOT evidence
that any particular genotype transforms, and NOT medical advice.

Outputs (all in this directory):
  transformation_states.csv   full enumeration of 2^7 input combinations -> outcome
  minimal_sets.csv            minimal sufficient perturbation sets for full transformation
  node_necessity.csv          per-node necessity / substitutability
  trajectory_orderings.csv    for the minimal set: every application ORDER -> viable?
  reverse_engineering_map.csv each build node -> attack-vector that undoes it (+ gaps)
  entities.txt                biomedical entities for OpenMed NER grounding
"""
from __future__ import annotations
import os, itertools, csv
from dataclasses import dataclass

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# INPUT PERTURBATIONS — the discrete "things you do to the cell" (the build kit).
# Each is a switch you can install (True) or not (False).
# ---------------------------------------------------------------------------
NODES = {
    # symbol : (human label, the function it serves, grounding pointer)
    "progenitor": ("Permissive progenitor / cell-of-origin state",
                   "open & bivalent chromatin, proliferative, in the developmental window",
                   "docs/03 Cell-of-Origin + Developmental-Window; cell-of-origin-specialist"),
    "fusion":     ("CIC-DUX4 fusion introduced",
                   "HMG-box retained (same ETS addresses) + DUX4 transactivation (logic inverted)",
                   "docs/02 The CIC-DUX4 Fusion; driver-engineering-specialist"),
    "apop_buffer":("Apoptosis buffering via the MCL1 / BCL2 anti-apoptotic axis",
                   "tolerate the DUX4 transactivation-domain death program (the fragility); "
                   "MCL1 is a verified CIC::DUX4 dependency and the DUX4 death program is largely "
                   "p53-INDEPENDENT, so p53/TP53 loss does NOT substitute for this node",
                   "driver-engineering-specialist (MCL1, PMID 40841513); cooperating-lesions-specialist"),
    "TP53_loss":  ("TP53 pathway loss",
                   "blocks BOTH oncogene-induced apoptosis AND oncogene-induced senescence",
                   "cooperating-lesions-specialist"),
    "CDKN2A_loss":("CDKN2A/CDKN2B (p16/p14ARF) loss",
                   "relieves the senescence brake (Rb + p53-ARF arm); frequent CIC-DUX4 co-event",
                   "docs/02 (CDKN2A frequent co-occurrence); cooperating-lesions-specialist"),
    "immortalize":("Telomere maintenance (TERT activation or ALT)",
                   "replicative immortality — escape telomere crisis",
                   "cooperating-lesions-specialist"),
    "amplify":    ("Super-enhancer / BRD4 amplification of the ETS output",
                   "makes the fusion's ETV4/5 output oncogenically DOMINANT",
                   "docs/02 Epigenetic Amplification; epigenetic-permissiveness-specialist"),
}
SYMS = list(NODES)

# ---------------------------------------------------------------------------
# WIRING — derived biological states as Boolean functions of the inputs.
# Each rule cites the mechanism it encodes. NOTE the deliberate OR-substitutions:
# a single lesion can serve two functions, which is what makes the minimal-set
# analysis informative (esp. TP53 double-duty).
# ---------------------------------------------------------------------------
def evaluate(state: dict) -> dict:
    s = {k: bool(state.get(k, False)) for k in SYMS}

    # The fusion's HMG-box can only ACTIVATE its ETS target loci if that chromatin
    # is accessible. In a differentiated cell those loci are closed -> the fusion
    # binds nothing productive. Permissive progenitor chromatin = the precondition.
    # (docs/03 "Why progenitor/stem cells are preferentially transformed")
    chromatin_open = s["progenitor"]
    ets_on = s["fusion"] and chromatin_open

    # DUX4's transactivation domain is intrinsically pro-death in somatic cells
    # (the FSHD death program; docs/02). Driving the program WITHOUT buffering kills
    # the cell. The verified buffer in CIC::DUX4 is the MCL1/BCL2 axis (PMID 40841513),
    # and the DUX4 death program is largely p53-INDEPENDENT (FSHD literature) -- so
    # TP53 loss does NOT rescue it. This makes the MCL1/BCL2 buffer an irreducible,
    # NON-substitutable build node (the central reverse-engineering payoff).
    apoptosis_blocked = s["apop_buffer"]

    # Oncogene-induced senescence (OIS) is the second brake. In real CIC-DUX4 tumors
    # this is removed mainly by CDKN2A/2B 9p21 loss (p16->Rb AND p14ARF->p53 arms);
    # TP53 mutation is rare but is a logically equivalent alternative route.
    senescence_blocked = s["CDKN2A_loss"] or s["TP53_loss"]

    # Super-enhancer amplification makes the ETS output dominant rather than a
    # transient/abortive burst (docs/02 amplification layer; CIC-DUX4 = transfer
    # from Ewing, Mechanistic).
    dominant = ets_on and s["amplify"]

    immortal = s["immortalize"]

    # --- outcome classification (priority order) ---
    if ets_on and not apoptosis_blocked:
        outcome = "death (DUX4/oncogene apoptosis, unbuffered)"        # hard fail
    elif not ets_on:
        outcome = ("no oncogenic program (no permissive substrate)"
                   if s["fusion"] else "no driver")                    # fail to transform
    elif not senescence_blocked:
        outcome = "oncogene-induced senescence / arrest"               # abortive
    elif not immortal:
        outcome = "proliferative but mortal (telomere crisis ahead)"   # partial
    elif not dominant:
        outcome = "transient / unstable hyperplasia (output not dominant)"  # partial
    else:
        outcome = "FULLY TRANSFORMED CIC-DUX4 sarcoma cell"            # success

    return dict(chromatin_open=chromatin_open, ets_on=ets_on,
                apoptosis_blocked=apoptosis_blocked,
                senescence_blocked=senescence_blocked, dominant=dominant,
                immortal=immortal, outcome=outcome)

SUCCESS = "FULLY TRANSFORMED CIC-DUX4 sarcoma cell"
DEATH_PREFIX = "death"


def is_success(state: dict) -> bool:
    return evaluate(state)["outcome"] == SUCCESS


# ---------------------------------------------------------------------------
# 1) Full enumeration of all 2^7 input combinations.
# ---------------------------------------------------------------------------
def enumerate_all():
    rows = []
    for combo in itertools.product([False, True], repeat=len(SYMS)):
        state = dict(zip(SYMS, combo))
        d = evaluate(state)
        row = {k: int(state[k]) for k in SYMS}
        row["n_inputs"] = sum(combo)
        row.update({k: (int(v) if isinstance(v, bool) else v) for k, v in d.items()})
        rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# 2) Minimal sufficient sets — smallest input sets that yield full transformation
#    such that no proper subset also succeeds.
# ---------------------------------------------------------------------------
def minimal_sets():
    succ = []
    for combo in itertools.product([False, True], repeat=len(SYMS)):
        state = dict(zip(SYMS, combo))
        if is_success(state):
            succ.append(frozenset(k for k in SYMS if state[k]))
    minimal = []
    for sset in succ:
        if not any(other < sset for other in succ):   # no proper subset succeeds
            minimal.append(sset)
    minimal.sort(key=lambda x: (len(x), sorted(x)))
    return minimal, succ


# ---------------------------------------------------------------------------
# 3) Node necessity / substitutability across the success set.
# ---------------------------------------------------------------------------
def node_necessity(success_sets):
    rows = []
    for sym in SYMS:
        in_all = all(sym in s for s in success_sets)
        in_any = any(sym in s for s in success_sets)
        rows.append({"node": sym,
                     "necessary (in EVERY sufficient set)": in_all,
                     "appears in some sufficient set": in_any,
                     "n_sufficient_sets_with_node": sum(sym in s for s in success_sets)})
    return rows


# ---------------------------------------------------------------------------
# 4) Trajectory / order analysis. Death is IRREVERSIBLE: any application order
#    that drives the ETS program before apoptosis is buffered kills the cell and
#    the build fails. We brute-force every ordering of a target set, applying one
#    perturbation at a time, and check whether any intermediate state is death.
# ---------------------------------------------------------------------------
def trajectory_orderings(target_set):
    target = sorted(target_set)
    rows, viable = [], 0
    for order in itertools.permutations(target):
        installed, failed_at, fail_mode = {}, None, ""
        for i, step in enumerate(order):
            installed[step] = True
            oc = evaluate(installed)["outcome"]
            if oc.startswith(DEATH_PREFIX):     # irreversible -> build aborts
                failed_at, fail_mode = i + 1, oc
                break
        ok = failed_at is None and is_success(installed)
        viable += int(ok)
        rows.append({"order": " -> ".join(order),
                     "viable_route": ok,
                     "aborted_at_step": failed_at if failed_at else "",
                     "failure_mode": fail_mode})
    return rows, viable, len(rows)


# ---------------------------------------------------------------------------
# 5) Reverse-engineering map — each build node -> the attack vector that UNDOES it.
#    "gap" = no current vector cleanly targets this construction step => forward
#    hypothesis. (V1 Rate-Limiting, V2 Compiler-Protection, V3 Hot-Patching,
#    V4 Immune-Watchdog.)
# ---------------------------------------------------------------------------
REVERSE_MAP = [
    ("progenitor",  "Permissive progenitor state / failure to differentiate",
     "V3 (force differentiation closes the substrate)",
     "PARTIAL GAP: no vector PREVENTS the permissive developmental window; differentiation therapy only acts after the fact"),
    ("fusion",      "CIC-DUX4 driver present",
     "V2 (prevent the translocation) upstream; V3 (ASO / PROTAC degrade the fusion) downstream",
     "V2 is prophylactic only; direct fusion degradation is experimental (fusion-dependent => atypical ~5% caveat)"),
    ("apop_buffer", "DUX4 apoptosis is buffered (the fragility the tumor had to suppress)",
     "(no current vector)",
     "GAP -> FORWARD: re-arm the DUX4/oncogene death program. The buffer is partly MCL1 - "
     "MCL1 inhibition kills CIC::DUX4 tumoroids (Nat Commun 2025, PMID 40841513); BH3-mimetic / "
     "restore the apoptotic priming the build had to defeat"),
    ("TP53_loss",   "p53 senescence brake removed (RARE as a mutation in CIC-DUX4; CDKN2A/ARF is the usual route)",
     "(no current vector; V3-adjacent)",
     "GAP -> FORWARD: TP53 is usually wild-type here, so MDM2 inhibition could restore the p53 brake "
     "the CDKN2A/ARF loss disabled (combine with CDK4/6i for the p16 arm)"),
    ("CDKN2A_loss", "p16/ARF senescence brake removed",
     "V1/V3 (CDK4/6 inhibition is pro-senescence, substitutes for the lost p16 brake)",
     "Convergent with Sim 1/2/3 CDK4 finding: CDK4/6i re-imposes the brake CDKN2A loss removed"),
    ("immortalize", "Telomere maintenance (TERT/ALT)",
     "(no current vector)",
     "GAP -> FORWARD: telomerase / ALT-pathway targeting is absent from V1-V4"),
    ("amplify",     "p300/CBP -> H3K27ac super-enhancer amplification of ETS output (BRD4-read)",
     "V3 (p300/CBP inhibition = the WRITER; also restores MHC-I -> V3->V4 bridge); V1 (BETi = the READER)",
     "CIC-DUX4-specific anchor: p300 is essential and the state is REVERSIBLE on p300i/fusion loss "
     "(Bakaric, Cancers 2024, PMID 38275898; Mol Cancer 2025, PMC12659477) -> 'deep but drainable attractor,' "
     "no hard epigenetic point-of-no-return demonstrated -> supports V3 differentiation premise"),
    ("(survivors)", "Any cell that completes the build",
     "V4 (immune visibility + clearance) — orthogonal end-stage net",
     "V4 acts regardless of which build steps were used; depends on MHC-I restoration (V3->V4 bridge)"),
]


def write_csv(path, rows, fieldnames=None):
    if not rows:
        return
    fieldnames = fieldnames or list(rows[0].keys())
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def main():
    print("=" * 78)
    print("Sim 7 — CIC-DUX4 tumorigenesis 'build recipe' (Boolean transformation model)")
    print("=" * 78)

    all_rows = enumerate_all()
    write_csv(os.path.join(HERE, "transformation_states.csv"), all_rows)
    n_succ = sum(r["outcome"] == SUCCESS for r in all_rows)
    n_death = sum(str(r["outcome"]).startswith(DEATH_PREFIX) for r in all_rows)
    print(f"\n[1] Enumerated {len(all_rows)} input combinations "
          f"({len(SYMS)} switches).")
    print(f"    -> {n_succ} reach FULL transformation; {n_death} end in death; "
          f"{len(all_rows)-n_succ-n_death} are abortive/partial.")

    minimal, succ = minimal_sets()
    mrows = [{"size": len(s), "perturbation_set": " + ".join(sorted(s))} for s in minimal]
    write_csv(os.path.join(HERE, "minimal_sets.csv"), mrows)
    print(f"\n[2] Minimal sufficient transformation sets ({len(minimal)}):")
    for s in minimal:
        print(f"    ({len(s)})  {' + '.join(sorted(s))}")

    nec = node_necessity(succ)
    write_csv(os.path.join(HERE, "node_necessity.csv"), nec)
    print("\n[3] Node necessity (necessary = in EVERY sufficient set):")
    for r in nec:
        tag = "NECESSARY" if r["necessary (in EVERY sufficient set)"] else "substitutable/optional"
        print(f"    {r['node']:14s} {tag}")

    # smallest minimal set drives the ordering analysis
    target = min(minimal, key=len)
    trows, viable, total = trajectory_orderings(target)
    write_csv(os.path.join(HERE, "trajectory_orderings.csv"), trows)
    print(f"\n[4] Trajectory/order analysis for smallest minimal set "
          f"{{{' + '.join(sorted(target))}}}:")
    print(f"    {viable}/{total} application orders yield a viable build; "
          f"{total-viable} abort (mostly death before apoptosis is buffered).")
    # surface the ordering constraint
    safe_first = {}
    for r in trows:
        if r["viable_route"]:
            first = r["order"].split(" -> ")[0]
            safe_first[first] = safe_first.get(first, 0) + 1
    print(f"    Viable routes by FIRST step installed: {safe_first}")

    write_csv(os.path.join(HERE, "reverse_engineering_map.csv"),
              [{"build_node": a, "what_it_installs": b,
                "attack_vector_that_undoes_it": c, "note_or_gap": d}
               for (a, b, c, d) in REVERSE_MAP])
    print("\n[5] Reverse-engineering map written (build node -> undo vector / gap).")
    gaps = [a for (a, b, c, d) in REVERSE_MAP if "GAP" in d]
    print(f"    Build steps with NO current vector (forward-hypothesis gaps): {gaps}")

    with open(os.path.join(HERE, "entities.txt"), "w") as fh:
        ents = ["CIC-DUX4", "CIC", "DUX4", "ETV4", "ETV5", "CDKN2A", "TP53",
                "TERT", "BRD4", "CDK4", "RB1", "mesenchymal stem cell",
                "oncogene-induced senescence", "Ewing sarcoma", "CIC-rearranged sarcoma"]
        fh.write(". ".join(ents) + ".\n")

    print("\n[done] wrote transformation_states.csv, minimal_sets.csv, node_necessity.csv,")
    print("       trajectory_orderings.csv, reverse_engineering_map.csv, entities.txt")


if __name__ == "__main__":
    main()
