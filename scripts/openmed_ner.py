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
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import Iterable

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
}


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
    else:
        sys.exit(f"error: unknown format {fmt!r}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--team", help="Agent team ID (see --list-teams).")
    ap.add_argument("--list-teams", action="store_true", help="Print the team→model map and exit.")
    ap.add_argument(
        "--model",
        action="append",
        default=None,
        help="Override the team's model list. Repeatable. Accepts a registry alias OR full HF model id.",
    )
    ap.add_argument("--text", help="Input text. If omitted, --text-file or stdin is used.")
    ap.add_argument("--text-file", help="Path to a file whose contents are the input text.")
    ap.add_argument(
        "--threshold",
        type=float,
        default=None,
        help="Confidence floor. Default: each model's recommended threshold.",
    )
    ap.add_argument(
        "--format",
        choices=("json", "jsonl", "tsv"),
        default="json",
        help="Output format (default: json).",
    )
    args = ap.parse_args()

    if args.list_teams:
        for team, models in TEAMS.items():
            print(f"{team:<25} {', '.join(models)}")
        return

    if not args.team and not args.model:
        ap.error("either --team or --model is required")

    models = args.model if args.model else TEAMS[args.team]
    if args.team and args.team not in TEAMS:
        ap.error(f"unknown team {args.team!r}; run with --list-teams")

    # Imports deferred so --list-teams stays instant.
    from openmed import analyze_text, OpenMedConfig

    cfg = OpenMedConfig(backend="mlx")
    text = _read_text(args)

    rows: list[dict] = []
    for model in models:
        kwargs = {"config": cfg}
        if args.threshold is not None:
            kwargs["confidence_threshold"] = args.threshold
        # analyze_text accepts either a registry alias via model_name or a HF id via model_id
        if "/" in model:
            result = analyze_text(text, model_id=model, **kwargs)
        else:
            result = analyze_text(text, model_name=model, **kwargs)
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

    _emit(rows, args.format)


if __name__ == "__main__":
    main()
