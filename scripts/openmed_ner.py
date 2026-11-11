#!/usr/bin/env python3
"""Run OpenMed NER on a piece of text using the model(s) assigned to a given agent team.

Team IDs follow `docs/07-openmed-models.md`. Run with `--list-teams` to see them.

Examples:
    python scripts/openmed_ner.py --team v3-epigenetic \
        --text "EZH2 inhibition with tazemetostat depletes H3K27me3."

    echo "BRD4 binds H3K27ac at super-enhancers." | \
        python scripts/openmed_ner.py --team v1-lead

    python scripts/openmed_ner.py --team orchestrator \
        --text-file simulation-output/v3-hot-patching/v3-summary.md \
        --threshold 0.7 --format jsonl

    python scripts/openmed_ner.py --check            # is grounding runnable here?
    python scripts/openmed_ner.py --prefetch         # download every team model now

Runtime behaviour:
- Finds the project venv even when run from a git worktree (worktrees have no .venv of
  their own) or with a different interpreter. Override with SARCOMA_VENV=/path/to/venv.
- Offline-first: when every model a run needs is already in the local Hugging Face cache,
  the Hub is never contacted (HF_HUB_OFFLINE=1). A blocked or rate-limited Hub then cannot
  break grounding.
- Backend is auto-detected: MLX on Apple Silicon, PyTorch ("hf") elsewhere (e.g. Linux
  cloud sessions). Override with --backend.
- If weights are missing and the Hub is unreachable, exits with code 3 and a diagnostic on
  stderr. Callers must then record grounding as NOT RUN - never invent scores.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
EXIT_UNAVAILABLE = 3

# Registry alias -> Hugging Face repo id. Kept here (not looked up from openmed) because the
# offline decision has to be made before openmed/transformers are imported. `--check`
# verifies this map against the installed openmed registry.
MODEL_REPOS: dict[str, str] = {
    "anatomy_detection_electramed": "OpenMed/OpenMed-NER-AnatomyDetect-ElectraMed-109M",
    "chemical_detection_pubmed": "OpenMed/OpenMed-NER-ChemicalDetect-PubMed-335M",
    "disease_detection_superclinical": "OpenMed/OpenMed-NER-DiseaseDetect-SuperClinical-434M",
    "dna_detection_supermedical": "OpenMed/OpenMed-NER-DNADetect-SuperMedical-125M",
    "genome_detection_bioclinical": "OpenMed/OpenMed-NER-GenomeDetect-BioClinical-108M",
    "oncology_detection_superclinical": "OpenMed/OpenMed-NER-OncologyDetect-SuperClinical-434M",
    "pharma_detection_superclinical": "OpenMed/OpenMed-NER-PharmaDetect-SuperClinical-434M",
    "protein_detection_pubmed": "OpenMed/OpenMed-NER-ProteinDetect-PubMed-109M",
    "species_detection_bioclinical": "OpenMed/OpenMed-NER-SpeciesDetect-BioClinical-108M",
}

TEAMS: dict[str, list[str]] = {
    "orchestrator": [
        "oncology_detection_superclinical",
        "pharma_detection_superclinical",
        "disease_detection_superclinical",
    ],
    "v1-lead": [
        "chemical_detection_pubmed",
        "pharma_detection_superclinical",
        "oncology_detection_superclinical",
    ],
    "v1-food": ["chemical_detection_pubmed"],
    "v1-supplement": [
        "pharma_detection_superclinical",
        "chemical_detection_pubmed",
    ],
    "v1-bioavailability": [
        "pharma_detection_superclinical",
        "chemical_detection_pubmed",
    ],
    "v2-lead": [
        "dna_detection_supermedical",
        "chemical_detection_pubmed",
        "disease_detection_superclinical",
    ],
    "v2-antioxidant": [
        "chemical_detection_pubmed",
        "oncology_detection_superclinical",
    ],
    "v2-dna-repair": [
        "dna_detection_supermedical",
        "genome_detection_bioclinical",
        "protein_detection_pubmed",
    ],
    "v2-anti-inflammatory": [
        "chemical_detection_pubmed",
        "disease_detection_superclinical",
    ],
    "v3-lead": [
        "oncology_detection_superclinical",
        "pharma_detection_superclinical",
        "protein_detection_pubmed",
    ],
    "v3-epigenetic": [
        "oncology_detection_superclinical",
        "pharma_detection_superclinical",
        "protein_detection_pubmed",
    ],
    "v3-differentiation": [
        "oncology_detection_superclinical",
        "chemical_detection_pubmed",
    ],
    "v3-protac-aso": [
        "pharma_detection_superclinical",
        "oncology_detection_superclinical",
        "protein_detection_pubmed",
    ],
    "v3-synthetic-lethality": [
        "oncology_detection_superclinical",
        "genome_detection_bioclinical",
        "protein_detection_pubmed",
    ],
    "v4-lead": [
        "disease_detection_superclinical",
        "oncology_detection_superclinical",
        "anatomy_detection_electramed",
    ],
    "v4-checkpoint": [
        "pharma_detection_superclinical",
        "disease_detection_superclinical",
        "anatomy_detection_electramed",
    ],
    "v4-nk": [
        "protein_detection_pubmed",
        "disease_detection_superclinical",
        "anatomy_detection_electramed",
    ],
    "v4-microbiome": [
        "species_detection_bioclinical",
        "chemical_detection_pubmed",
    ],
    "v4-neoantigen": [
        "pharma_detection_superclinical",
        "protein_detection_pubmed",
        "oncology_detection_superclinical",
    ],
    "mrna-vaccine-lead": [
        "disease_detection_superclinical",
        "pharma_detection_superclinical",
        "oncology_detection_superclinical",
    ],
    "mrna-immune-effects": [
        "disease_detection_superclinical",
        "protein_detection_pubmed",
        "anatomy_detection_electramed",
    ],
    "mrna-oncogenic-risk": [
        "oncology_detection_superclinical",
        "disease_detection_superclinical",
        "pharma_detection_superclinical",
    ],
    "metastatic-specialist": [
        "oncology_detection_superclinical",
        "anatomy_detection_electramed",
        "disease_detection_superclinical",
    ],
}

INSTALL_HINT = (
    "Create the venv in the main checkout:\n"
    "  python3.13 -m venv .venv\n"
    "  Apple Silicon: .venv/bin/pip install --upgrade pip 'openmed[mlx]' torch\n"
    "  Linux / other: .venv/bin/pip install --upgrade pip 'openmed[hf]' torch\n"
    "or point SARCOMA_VENV at an existing venv that has openmed installed."
)

UNAVAILABLE_HINT = (
    "Fix one of:\n"
    "  - allow huggingface.co, *.hf.co and cas-bridge.xethub.hf.co in this environment's network\n"
    "    policy (cloud sessions: https://code.claude.com/docs/en/claude-code-on-the-web), then retry;\n"
    "  - run `scripts/openmed_ner.py --prefetch` on a machine with Hub access and copy its\n"
    "    ~/.cache/huggingface/hub (and ~/.cache/openmed on Apple Silicon) here.\n"
    "Until then record grounding as NOT RUN (CLAUDE.md section 5). Do not invent scores."
)


# --------------------------------------------------------------------------- environment


def _candidate_venvs() -> list[Path]:
    cands: list[Path] = []
    if os.environ.get("SARCOMA_VENV"):
        cands.append(Path(os.environ["SARCOMA_VENV"]).expanduser())
    cands.append(ROOT / ".venv")
    # In a git worktree the venv lives in the main checkout, next to the shared .git dir.
    try:
        common = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "--path-format=absolute", "--git-common-dir"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        if common:
            cands.append(Path(common).parent / ".venv")
    except (OSError, subprocess.SubprocessError):
        pass
    seen, out = set(), []
    for c in cands:
        key = str(c.resolve()) if c.exists() else str(c)
        if key not in seen:
            seen.add(key)
            out.append(c)
    return out


def _ensure_openmed_interpreter() -> None:
    """Re-exec into a venv that has openmed, without importing openmed here."""
    if importlib.util.find_spec("openmed") is not None:
        return
    if not os.environ.get("_OPENMED_NER_REEXEC"):
        for venv in _candidate_venvs():
            py = venv / "bin" / "python"
            if py.exists() and Path(sys.prefix).resolve() != venv.resolve():
                os.environ["_OPENMED_NER_REEXEC"] = "1"
                os.execv(str(py), [str(py), str(Path(__file__).resolve()), *sys.argv[1:]])
    tried = ", ".join(str(v) for v in _candidate_venvs())
    sys.stderr.write(f"error: openmed is not importable (looked in: {tried}).\n{INSTALL_HINT}\n")
    sys.exit(2)


def _hf_cache_dir() -> Path:
    if os.environ.get("HF_HUB_CACHE"):
        return Path(os.environ["HF_HUB_CACHE"]).expanduser()
    if os.environ.get("HF_HOME"):
        return Path(os.environ["HF_HOME"]).expanduser() / "hub"
    return Path.home() / ".cache" / "huggingface" / "hub"


def _repo_id(model: str) -> str | None:
    return model if "/" in model else MODEL_REPOS.get(model)


def _is_cached(model: str) -> bool:
    repo = _repo_id(model)
    if repo is None:
        return False
    snaps = _hf_cache_dir() / ("models--" + repo.replace("/", "--")) / "snapshots"
    return any(snaps.glob("*/config.json"))


def _hub_reachable(repo: str = "OpenMed/OpenMed-NER-OncologyDetect-SuperClinical-434M") -> str:
    import urllib.error
    import urllib.request

    url = f"{os.environ.get('HF_ENDPOINT', 'https://huggingface.co').rstrip('/')}/api/models/{repo}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=10) as r:
            return f"ok (HTTP {r.status})"
    except urllib.error.HTTPError as e:
        return f"BLOCKED (HTTP {e.code})"
    except Exception as e:  # noqa: BLE001 - any network failure is a diagnosis, not a crash
        return f"UNREACHABLE ({type(e).__name__}: {str(e)[:80]})"


def _resolve_backend(choice: str) -> str | None:
    """None lets openmed auto-detect (MLX on Apple Silicon, PyTorch elsewhere)."""
    return None if choice == "auto" else choice


# --------------------------------------------------------------------------- actions


def _read_text(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    if args.text_file is not None:
        with open(args.text_file, "r", encoding="utf-8") as fh:
            return fh.read()
    data = sys.stdin.read()
    if not data.strip():
        sys.exit("error: no --text, --text-file, or stdin input provided")
    return data


def _emit(rows: Iterable[dict], fmt: str) -> None:
    rows = list(rows)
    if fmt == "json":
        json.dump(rows, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    elif fmt == "jsonl":
        for r in rows:
            sys.stdout.write(json.dumps(r, ensure_ascii=False) + "\n")
    elif fmt == "tsv":
        sys.stdout.write("model\tlabel\ttext\tconfidence\tstart\tend\n")
        for r in rows:
            sys.stdout.write(
                f"{r['model']}\t{r['label']}\t{r['text']}\t{r['confidence']:.3f}\t{r.get('start', '')}\t{r.get('end', '')}\n"
            )


def _run_models(models: list[str], text: str, backend: str | None, threshold: float | None) -> list[dict]:
    from openmed import OpenMedConfig, analyze_text

    cfg = OpenMedConfig(backend=backend)
    rows: list[dict] = []
    for model in models:
        kwargs: dict = {"config": cfg}
        if threshold is not None:
            kwargs["confidence_threshold"] = threshold
        try:
            if "/" in model:
                result = analyze_text(text, model_id=model, **kwargs)
            else:
                result = analyze_text(text, model_name=model, **kwargs)
        except Exception as e:  # noqa: BLE001 - classify, then report
            if _is_cached(model):
                raise
            sys.stderr.write(
                f"GROUNDING UNAVAILABLE: weights for {model!r} are not cached and could not be "
                f"downloaded ({type(e).__name__}: {str(e)[:200]}).\n"
                f"Hub check: {_hub_reachable()}\n{UNAVAILABLE_HINT}\n"
            )
            sys.exit(EXIT_UNAVAILABLE)
        for e in result.entities:
            rows.append(
                {
                    "model": model,
                    "label": e.label,
                    "text": e.text,
                    "confidence": round(float(e.confidence), 3),
                    "start": getattr(e, "start", None),
                    "end": getattr(e, "end", None),
                }
            )
    return rows


def _check(models: list[str], backend_choice: str) -> int:
    print(f"interpreter : {sys.executable}  (prefix {sys.prefix})")
    print(f"backend     : {backend_choice}")
    print(f"HF cache    : {_hf_cache_dir()}")
    print(f"HF_HUB_OFFLINE: {os.environ.get('HF_HUB_OFFLINE', 'unset')}")
    missing = [m for m in models if not _is_cached(m)]
    for m in models:
        print(f"  {'cached ' if _is_cached(m) else 'MISSING'}  {m}  ->  {_repo_id(m) or '?'}")
    hub = _hub_reachable()
    print(f"Hub         : {hub}")
    # Verify the static alias map still matches the installed registry.
    from openmed.core.model_registry import get_model_info

    drift = [a for a, repo in MODEL_REPOS.items() if (i := get_model_info(a)) and i.model_id != repo]
    if drift:
        print(f"WARNING: MODEL_REPOS disagrees with the openmed registry for: {', '.join(drift)}")
    if missing and not hub.startswith("ok"):
        print(f"\nRESULT: grounding UNAVAILABLE for {len(missing)} model(s).\n{UNAVAILABLE_HINT}")
        return EXIT_UNAVAILABLE
    print("\nRESULT: grounding runnable" + (" offline (all weights cached)." if not missing else
                                            f" (will download {len(missing)} model(s))."))
    return 0


# --------------------------------------------------------------------------- main


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--team", help="Agent team ID (see --list-teams).")
    ap.add_argument("--list-teams", action="store_true", help="Print the team->model map and exit.")
    ap.add_argument(
        "--model",
        action="append",
        default=None,
        help="Override the team's model list. Repeatable. Accepts a registry alias OR full HF model id.",
    )
    ap.add_argument("--text", help="Input text. If omitted, --text-file or stdin is used.")
    ap.add_argument("--text-file", help="Path to a file whose contents are the input text.")
    ap.add_argument("--threshold", type=float, default=None,
                    help="Confidence floor. Default: each model's recommended threshold.")
    ap.add_argument("--format", choices=("json", "jsonl", "tsv"), default="json",
                    help="Output format (default: json).")
    ap.add_argument("--backend", choices=("auto", "mlx", "hf"), default="auto",
                    help="Inference backend (default: auto - MLX on Apple Silicon, PyTorch elsewhere).")
    ap.add_argument("--check", action="store_true",
                    help="Report venv, backend, cache and Hub status for the selected (default: all) models.")
    ap.add_argument("--prefetch", action="store_true",
                    help="Download and warm the selected (default: all) models while the Hub is reachable.")
    args = ap.parse_args()

    if args.list_teams:
        for team, models in TEAMS.items():
            print(f"{team:<25} {', '.join(models)}")
        return
    if args.team and args.team not in TEAMS:
        ap.error(f"unknown team {args.team!r}; run with --list-teams")

    all_models = sorted(MODEL_REPOS)
    if args.model:
        models = args.model
    elif args.team:
        models = TEAMS[args.team]
    elif args.check or args.prefetch:
        models = all_models
    else:
        ap.error("either --team or --model is required")

    _ensure_openmed_interpreter()

    # Offline-first: never touch the network when the weights are already here.
    if not args.prefetch and "HF_HUB_OFFLINE" not in os.environ and all(_is_cached(m) for m in models):
        os.environ["HF_HUB_OFFLINE"] = "1"
    backend = _resolve_backend(args.backend)

    if args.check:
        sys.exit(_check(models, args.backend))
    if args.prefetch:
        _run_models(models, "EZH2", backend, None)
        print(f"prefetched {len(models)} model(s) into {_hf_cache_dir()}")
        return

    _emit(_run_models(models, _read_text(args), backend, args.threshold), args.format)


if __name__ == "__main__":
    main()
