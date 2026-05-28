#!/usr/bin/env python3
"""Sarcoma simulation dispatcher — validates prerequisites and prints the wave plan.

The actual agents are launched by Claude Code (or another LLM harness) via its
Task tool. This script does NOT spawn agents itself — it validates that the
environment is ready, that the wave-1 gate is honored, and that the orchestrator
runs last.

Modes:
    plan      Print the wave plan + per-agent context files and exit (default).
    check     Run prerequisite checks only (venv, output tree, openmed import).
    gate      Verify wave-1 gate state — confirm mRNA team output and V3 MHC-I
              section are on disk before wave 2 starts.
    ready     Check the orchestrator preconditions — all four vector summaries
              and the mRNA team output exist.

Exit codes:
    0  ok
    1  prerequisite check failed
    2  gate not yet satisfied (informational, not an error per se)

Usage:
    python scripts/dispatch.py            # plan (default)
    python scripts/dispatch.py check
    python scripts/dispatch.py gate
    python scripts/dispatch.py ready
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIM = ROOT / "simulation-output"
VENV_PY = ROOT / ".venv" / "bin" / "python"

WAVE_1 = [
    ("mRNA Vaccine Research Team Lead",
     "mrna-vaccine-lead",
     ["docs/00-README.md", "docs/01-general-sarcoma-knowledge.md", "docs/02-cic-sarcoma-knowledge.md"],
     "simulation-output/mrna-vaccine-research/mrna-vaccine-summary.md"),
    ("V1 Rate Limiting Lead",
     "v1-lead",
     ["docs/00-README.md", "docs/02-cic-sarcoma-knowledge.md", "docs/04-biology-engineering-analogy.md", "docs/05-attack-vectors.md (V1 section)"],
     "simulation-output/v1-rate-limiting/v1-summary.md"),
    ("V3 Hot Patching Lead",
     "v3-lead",
     ["docs/00-README.md", "docs/01-general-sarcoma-knowledge.md", "docs/02-cic-sarcoma-knowledge.md", "docs/04-biology-engineering-analogy.md", "docs/05-attack-vectors.md (V3 section)"],
     "simulation-output/v3-hot-patching/v3-summary.md"),
]

WAVE_2 = [
    ("V2 Compiler Protection Lead",
     "v2-lead",
     ["docs/00-README.md", "docs/03-dna-genome-protein-interactions.md", "docs/04-biology-engineering-analogy.md", "docs/05-attack-vectors.md (V2 section)", "simulation-output/mrna-vaccine-research/mrna-vaccine-summary.md"],
     "simulation-output/v2-compiler-protection/v2-summary.md"),
    ("V4 Immune Watchdog Lead",
     "v4-lead",
     ["docs/00-README.md", "docs/01-general-sarcoma-knowledge.md", "docs/02-cic-sarcoma-knowledge.md", "docs/05-attack-vectors.md (V4 section)", "simulation-output/v3-hot-patching/v3-summary.md (MHC-I section)", "simulation-output/mrna-vaccine-research/mrna-vaccine-summary.md"],
     "simulation-output/v4-immune-watchdog/v4-summary.md"),
]

ORCHESTRATOR = (
    "Orchestrator",
    "orchestrator",
    ["docs/00-README.md", "docs/01–05 knowledge files", "all four v{N}-summary.md", "simulation-output/mrna-vaccine-research/mrna-vaccine-summary.md"],
    "simulation-output/protocol-v1.md",
    "Launches the Metastatic Disease Specialist sub-agent during synthesis; consumes its `metastatic-disease-considerations.md` and writes the final `protocol-v1.md`.",
)

WAVE_1_OUTPUTS = [Path(spec[3]) for spec in WAVE_1]
WAVE_2_OUTPUTS = [Path(spec[3]) for spec in WAVE_2]
ORCH_OUTPUT = Path(ORCHESTRATOR[3])
MRNA_OUTPUT = Path("simulation-output/mrna-vaccine-research/mrna-vaccine-summary.md")
V3_OUTPUT = Path("simulation-output/v3-hot-patching/v3-summary.md")


def _ok(msg: str) -> None:
    print(f"  ok   {msg}")


def _fail(msg: str) -> None:
    print(f"  FAIL {msg}")


def _info(msg: str) -> None:
    print(f"  ..   {msg}")


def _heading(title: str) -> None:
    print(f"\n=== {title} ===")


def check_prerequisites() -> int:
    """Verify venv, output tree, openmed import."""
    _heading("Prerequisite checks")
    failures = 0

    if VENV_PY.exists():
        _ok(f".venv present at {VENV_PY.relative_to(ROOT)}")
    else:
        _fail(".venv missing. Create with: python3.13 -m venv .venv && "
              ".venv/bin/pip install --upgrade pip 'openmed[mlx]' torch")
        failures += 1

    if SIM.exists():
        _ok(f"output tree present at {SIM.relative_to(ROOT)}")
        for sub in ("v1-rate-limiting", "v2-compiler-protection", "v3-hot-patching",
                    "v4-immune-watchdog", "mrna-vaccine-research"):
            if (SIM / sub).exists():
                _ok(f"  sub-dir {sub}/")
            else:
                _fail(f"  sub-dir missing: simulation-output/{sub}/")
                failures += 1
    else:
        _fail("simulation-output/ missing. Run: mkdir -p simulation-output/{v1-rate-limiting,"
              "v2-compiler-protection,v3-hot-patching,v4-immune-watchdog,mrna-vaccine-research}")
        failures += 1

    if VENV_PY.exists():
        result = subprocess.run(
            [str(VENV_PY), "-c", "import openmed; print(openmed.__version__)"],
            capture_output=True, text=True, cwd=ROOT,
        )
        if result.returncode == 0:
            _ok(f"openmed import OK (version {result.stdout.strip()})")
        else:
            _fail(f"openmed import failed: {result.stderr.strip()}")
            failures += 1

    cli = ROOT / "scripts" / "openmed_ner.py"
    if cli.exists():
        _ok(f"NER CLI present at {cli.relative_to(ROOT)}")
    else:
        _fail("scripts/openmed_ner.py missing")
        failures += 1

    return failures


def check_wave1_gate() -> int:
    """Wave 2 may start only when mRNA output and V3 MHC-I section are on disk."""
    _heading("Wave-1 gate")
    missing = 0
    if MRNA_OUTPUT.exists() and MRNA_OUTPUT.stat().st_size > 0:
        _ok(f"mRNA team output present: {MRNA_OUTPUT}")
    else:
        _info(f"mRNA team output not yet on disk: {MRNA_OUTPUT}")
        missing += 1
    if V3_OUTPUT.exists() and V3_OUTPUT.stat().st_size > 0:
        # V4 only strictly needs the MHC-I section; we check the file exists
        # and contains the expected header. Cheap heuristic — not a full parse.
        text = V3_OUTPUT.read_text(errors="ignore")
        if "MHC-I" in text:
            _ok(f"V3 summary present with MHC-I section: {V3_OUTPUT}")
        else:
            _fail(f"V3 summary present but no 'MHC-I' header found — V4 cannot consume the bridge section: {V3_OUTPUT}")
            missing += 1
    else:
        _info(f"V3 summary not yet on disk: {V3_OUTPUT}")
        missing += 1
    if missing:
        print(f"\n  → Wave 2 (V2, V4) is NOT yet cleared to start. {missing} prerequisite(s) outstanding.")
        return 2
    print("\n  → Wave 2 (V2, V4) cleared to start.")
    return 0


def check_orchestrator_ready() -> int:
    """Orchestrator runs after all four vector summaries and mRNA output exist."""
    _heading("Orchestrator preconditions")
    missing = 0
    for path in (*WAVE_1_OUTPUTS, *WAVE_2_OUTPUTS):
        if path.exists() and path.stat().st_size > 0:
            _ok(str(path))
        else:
            _info(f"missing: {path}")
            missing += 1
    if missing:
        print(f"\n  → Orchestrator NOT yet ready. {missing} input(s) outstanding.")
        return 2
    print("\n  → Orchestrator cleared to run.")
    return 0


def print_plan() -> int:
    _heading("Sarcoma simulation — wave plan")
    print("""
Wave 1 (parallel): mRNA team, V1 Lead, V3 Lead.
Wave-1 gate:       mRNA output written; V3 MHC-I Upregulation Candidates section written.
Wave 2 (parallel): V2 Lead, V4 Lead.
Orchestrator:      runs after all four vector summaries + mRNA output exist;
                   launches Metastatic Disease Specialist as a sub-agent;
                   writes simulation-output/protocol-v1.md.
""".strip())

    for wave_label, wave in [("Wave 1", WAVE_1), ("Wave 2", WAVE_2)]:
        _heading(wave_label)
        for role, team_id, context, out in wave:
            print(f"- {role}")
            print(f"    team-id (NER):  {team_id}")
            print(f"    context:        {', '.join(context)}")
            print(f"    output:         {out}")

    _heading("Orchestrator")
    role, team_id, context, out, note = ORCHESTRATOR
    print(f"- {role}")
    print(f"    team-id (NER):  {team_id}")
    print(f"    context:        {', '.join(context)}")
    print(f"    output:         {out}")
    print(f"    note:           {note}")

    _heading("Next steps")
    print("Run:  python scripts/dispatch.py check     # prerequisite checks")
    print("Then dispatch wave-1 agents via Claude Code Task tool.")
    print("Once wave 1 lands, run:  python scripts/dispatch.py gate")
    print("If the gate passes, dispatch wave-2 agents.")
    print("Once wave 2 lands, run:  python scripts/dispatch.py ready")
    print("If ready, dispatch the Orchestrator task.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", nargs="?", default="plan", choices=("plan", "check", "gate", "ready"))
    args = ap.parse_args()

    if args.mode == "plan":
        return print_plan()
    if args.mode == "check":
        rc = check_prerequisites()
        return 0 if rc == 0 else 1
    if args.mode == "gate":
        return check_wave1_gate()
    if args.mode == "ready":
        return check_orchestrator_ready()
    return 0


if __name__ == "__main__":
    sys.exit(main())
