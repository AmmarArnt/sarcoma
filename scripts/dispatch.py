#!/usr/bin/env python3
"""Sarcoma simulation dispatcher - validates prerequisites and prints the wave plan.

The agents are launched by Claude Code via its Agent tool. This script does NOT spawn
agents - it validates the environment, names the run-scoped output paths, enforces the
wave-1 gate, and confirms the orchestrator runs last.

Runs are versioned so a fresh cycle never overwrites a baseline (CLAUDE.md section 0).
Run N writes:
    <vector-dir>/<lead>-summary-vN.md      lead summaries
    <vector-dir>/vN/<specialist>.md        specialist outputs
    simulation-output/protocol-vN.md       the orchestrator's catalog
N defaults to (highest existing protocol-vN.md) + 1. Override with SARCOMA_RUN=N or --run N.

Modes:
    plan      Print the wave plan, context files and run-scoped output paths (default).
    check     Prerequisite checks (venv, output tree, openmed, NER grounding availability).
    gate      Wave-1 gate - this run's mRNA output and V3 MHC-I section are on disk.
    ready     Orchestrator preconditions - this run's four vector summaries + mRNA output.

Exit codes: 0 ok · 1 prerequisite check failed · 2 gate not yet satisfied.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIM = ROOT / "simulation-output"
NER_CLI = ROOT / "scripts" / "openmed_ner.py"

BASELINE = "CASE-BASELINE.md"

# (role, agent / NER team id, output dir under simulation-output, summary stem, context files)
WAVE_1 = [
    ("mRNA Vaccine Research Team Lead", "mrna-vaccine-lead", "mrna-vaccine-research", "mrna-vaccine-summary",
     [BASELINE, "docs/00-README.md", "docs/01-general-sarcoma-knowledge.md", "docs/02-cic-sarcoma-knowledge.md"]),
    ("V1 Rate Limiting Lead", "v1-lead", "v1-rate-limiting", "v1-summary",
     [BASELINE, "docs/00-README.md", "docs/02-cic-sarcoma-knowledge.md", "docs/04-biology-engineering-analogy.md",
      "docs/05-attack-vectors.md (V1 section)"]),
    ("V3 Hot Patching Lead", "v3-lead", "v3-hot-patching", "v3-summary",
     [BASELINE, "docs/00-README.md", "docs/01-general-sarcoma-knowledge.md", "docs/02-cic-sarcoma-knowledge.md",
      "docs/04-biology-engineering-analogy.md", "docs/05-attack-vectors.md (V3 section)"]),
]

WAVE_2 = [
    ("V2 Compiler Protection Lead", "v2-lead", "v2-compiler-protection", "v2-summary",
     [BASELINE, "docs/00-README.md", "docs/03-dna-genome-protein-interactions.md",
      "docs/04-biology-engineering-analogy.md", "docs/05-attack-vectors.md (V2 section)", "this run's mRNA summary"]),
    ("V4 Immune Watchdog Lead", "v4-lead", "v4-immune-watchdog", "v4-summary",
     [BASELINE, "docs/00-README.md", "docs/01-general-sarcoma-knowledge.md", "docs/02-cic-sarcoma-knowledge.md",
      "docs/05-attack-vectors.md (V4 section)", "this run's V3 summary (MHC-I section)", "this run's mRNA summary"]),
]

ORCH_CONTEXT = [BASELINE, "docs/00-README.md", "docs/01-05 knowledge files", "this run's four vector summaries",
                "this run's mRNA summary", "standing analytical layers (sarcoma-orchestrator-intake step 1B)"]


def _ok(msg: str) -> None:
    print(f"  ok   {msg}")


def _fail(msg: str) -> None:
    print(f"  FAIL {msg}")


def _info(msg: str) -> None:
    print(f"  ..   {msg}")


def _heading(title: str) -> None:
    print(f"\n=== {title} ===")


def _rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def run_number(override: int | None) -> int:
    if override is not None:
        return override
    if os.environ.get("SARCOMA_RUN"):
        return int(os.environ["SARCOMA_RUN"])
    versions = [int(m.group(1)) for p in SIM.glob("protocol-v*.md")
                if (m := re.fullmatch(r"protocol-v(\d+)\.md", p.name))]
    return max(versions, default=0) + 1


def summary_path(subdir: str, stem: str, n: int) -> Path:
    return SIM / subdir / f"{stem}-v{n}.md"


def specialist_dir(subdir: str, n: int) -> Path:
    return SIM / subdir / f"v{n}"


def protocol_path(n: int) -> Path:
    return SIM / f"protocol-v{n}.md"


def _venv_python() -> Path | None:
    cands = []
    if os.environ.get("SARCOMA_VENV"):
        cands.append(Path(os.environ["SARCOMA_VENV"]).expanduser())
    cands.append(ROOT / ".venv")
    try:  # git worktrees share the main checkout's venv
        common = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--path-format=absolute", "--git-common-dir"],
                                capture_output=True, text=True, timeout=10).stdout.strip()
        if common:
            cands.append(Path(common).parent / ".venv")
    except (OSError, subprocess.SubprocessError):
        pass
    for c in cands:
        if (c / "bin" / "python").exists():
            return c / "bin" / "python"
    return None


def check_prerequisites(n: int) -> int:
    _heading(f"Prerequisite checks (run v{n})")
    failures = 0

    if (ROOT / BASELINE).exists():
        _ok(f"{BASELINE} present - every agent reads it first")
    else:
        _fail(f"{BASELINE} missing")
        failures += 1

    py = _venv_python()
    if py:
        _ok(f"venv python: {py}")
        result = subprocess.run([str(py), "-c", "import openmed; print(openmed.__version__)"],
                                capture_output=True, text=True, cwd=ROOT)
        if result.returncode == 0:
            _ok(f"openmed import OK (version {result.stdout.strip()})")
        else:
            _fail(f"openmed import failed: {result.stderr.strip()[-300:]}")
            failures += 1
    else:
        _fail(".venv not found (checked SARCOMA_VENV, this checkout, and the main worktree). Create it with:\n"
              "       python3.13 -m venv .venv && .venv/bin/pip install --upgrade pip "
              "'openmed[mlx]' torch   # Linux: 'openmed[hf]' torch")
        failures += 1

    for _, _, subdir, _, _ in (*WAVE_1, *WAVE_2):
        d = SIM / subdir
        if d.exists():
            _ok(f"output dir {_rel(d)}/")
        else:
            _fail(f"output dir missing: {_rel(d)}/")
            failures += 1

    # Grounding availability is reported, not fatal: an agent that cannot ground records
    # "NOT RUN" (CLAUDE.md section 5) instead of blocking the whole research run.
    if py and NER_CLI.exists():
        r = subprocess.run([str(py), str(NER_CLI), "--check"], capture_output=True, text=True, cwd=ROOT)
        last = (r.stdout.strip().splitlines() or ["(no output)"])[-1]
        (_ok if r.returncode == 0 else _info)(f"NER grounding: {last}")
        if r.returncode != 0:
            _info("grounding unavailable - agents must record grounding as NOT RUN; "
                  "see `scripts/openmed_ner.py --check` for the fix")
    return failures


def check_wave1_gate(n: int) -> int:
    """Wave 2 may start only when this run's mRNA output and V3 MHC-I section are on disk."""
    _heading(f"Wave-1 gate (run v{n})")
    missing = 0
    mrna = summary_path("mrna-vaccine-research", "mrna-vaccine-summary", n)
    v3 = summary_path("v3-hot-patching", "v3-summary", n)
    if mrna.exists() and mrna.stat().st_size > 0:
        _ok(f"mRNA team output present: {_rel(mrna)}")
    else:
        _info(f"mRNA team output not yet on disk: {_rel(mrna)}")
        missing += 1
    if v3.exists() and v3.stat().st_size > 0:
        if "MHC-I Upregulation Candidates" in v3.read_text(errors="ignore"):
            _ok(f"V3 summary present with MHC-I section: {_rel(v3)}")
        else:
            _fail(f"V3 summary has no 'MHC-I Upregulation Candidates' section - V4 cannot consume the bridge: {_rel(v3)}")
            missing += 1
    else:
        _info(f"V3 summary not yet on disk: {_rel(v3)}")
        missing += 1
    if missing:
        print(f"\n  -> Wave 2 (V2, V4) is NOT yet cleared to start. {missing} prerequisite(s) outstanding.")
        return 2
    print("\n  -> Wave 2 (V2, V4) cleared to start.")
    return 0


def check_orchestrator_ready(n: int) -> int:
    _heading(f"Orchestrator preconditions (run v{n})")
    missing = 0
    for _, _, subdir, stem, _ in (*WAVE_1, *WAVE_2):
        p = summary_path(subdir, stem, n)
        if p.exists() and p.stat().st_size > 0:
            _ok(_rel(p))
        else:
            _info(f"missing: {_rel(p)}")
            missing += 1
    if protocol_path(n).exists():
        _fail(f"{_rel(protocol_path(n))} already exists - pick a new run number (SARCOMA_RUN) rather than overwrite")
        missing += 1
    if missing:
        print(f"\n  -> Orchestrator NOT yet ready. {missing} issue(s) outstanding.")
        return 2
    print(f"\n  -> Orchestrator cleared to run; it writes {_rel(protocol_path(n))}.")
    return 0


def print_plan(n: int) -> int:
    _heading(f"Sarcoma simulation - wave plan (run v{n})")
    if n > 1:
        print(f"NOTE: protocol-v1..v{n - 1} already exist. Reuse them unless you intend a fresh cycle,\n"
              "      need scope they don't cover, or are expanding the findings (CLAUDE.md section 0).\n"
              "      A fresh cycle writes run-scoped files and never overwrites a baseline.")
    for label, wave in (("Wave 1 (parallel)", WAVE_1), ("Wave 2 (parallel, after `gate`)", WAVE_2)):
        _heading(label)
        for role, team, subdir, stem, context in wave:
            print(f"- {role}  [agent / NER team: {team}]")
            print(f"    context:      {', '.join(context)}")
            print(f"    summary:      {_rel(summary_path(subdir, stem, n))}")
            print(f"    specialists:  {_rel(specialist_dir(subdir, n))}/")
    _heading("Orchestrator (after `ready`)")
    print("- Orchestrator  [agent / NER team: orchestrator]")
    print(f"    context:      {', '.join(ORCH_CONTEXT)}")
    print(f"    metastatic:   {_rel(SIM / f'metastatic-disease-considerations-v{n}.md')}")
    print(f"    catalog:      {_rel(protocol_path(n))}")
    _heading("Sequence")
    print("check -> Wave 1 via the Agent tool -> gate -> Wave 2 -> ready -> Orchestrator.\n"
          f"Pass the run number (v{n}) to every lead so all agents write the same run's paths.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", nargs="?", default="plan", choices=("plan", "check", "gate", "ready"))
    ap.add_argument("--run", type=int, default=None, help="Run number N (default: SARCOMA_RUN or next protocol version).")
    args = ap.parse_args()
    n = run_number(args.run)

    if args.mode == "plan":
        return print_plan(n)
    if args.mode == "check":
        return 0 if check_prerequisites(n) == 0 else 1
    if args.mode == "gate":
        return check_wave1_gate(n)
    return check_orchestrator_ready(n)


if __name__ == "__main__":
    sys.exit(main())
