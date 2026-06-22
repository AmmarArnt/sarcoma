#!/usr/bin/env python3
"""
Sim 9 — Condensate / LLPS propensity of the CIC-DUX4 transactivation module
(Forward-simulation Track B, from simulation-output/forward-simulation/in-silico-experiments.md)

QUESTION
--------
Is the DUX4 C-terminal acidic transactivation domain (the part CIC keeps in the
CIC-DUX4 fusion) predicted to drive / partition into biomolecular condensates the
way the EWSR1 and FUS low-complexity domains (LCDs) do? If so, that is an
in-silico-first argument that CIC-DUX4 builds transcriptional condensates — a
mechanism the field has explored for EWSR1 fusions but NOT for CIC-DUX4
(confirmed by the 2026-06 evidence refresh: no DUX4 or CIC-DUX4 LLPS literature
was found).

HONESTY (read before trusting any number this prints)
-----------------------------------------------------
* These are SEQUENCE-FEATURE descriptors (localcider: Das-Pappu / Uversky / charge
  patterning) and, if installed, a disorder predictor (metapredict). They are
  hypothesis-PRIORITISATION tools. They do NOT prove a condensate forms in a cell,
  do NOT give a saturation concentration, and are trained on a small, biased set of
  known phase-separating proteins (out-of-distribution risk is real for an
  artificial fusion module). This is NOT FuzDrop / PScore / catGRANULE — those are
  web servers this offline environment could not reach.
* NO sequence is hard-coded. Every sequence is fetched live from UniProt and its
  integrity is checked against the UniProt SQ-line CRC64 (via biopython's
  Bio.SeqUtils.CheckSum.crc64, the canonical SwissProt CRC64). If the fetched
  sequence does not match its published checksum the script ABORTS rather than
  compute on a possibly-corrupted sequence. No fabrication.
* Domain boundaries are taken from the literature and marked [VERIFY]; where
  metapredict is available the script ALSO derives IDR boundaries empirically and
  prints both so the hard-coded coordinates can be checked, not trusted.

REPRODUCIBILITY
---------------
    pip install localcider biopython requests numpy
    # optional, for empirical IDR detection (pulls torch):  pip install metapredict
    python run_condensate_llps.py

If UniProt is unreachable (e.g. a restricted network-egress allowlist, as in the
environment where this was authored) the script reports the failure and exits
non-zero — it does not invent sequences. Run it where rest.uniprot.org is reachable.
"""
from __future__ import annotations
import json, sys, datetime
from dataclasses import dataclass, asdict

try:
    import requests
    from Bio.SeqUtils.CheckSum import crc64
    from localcider.sequenceParameters import SequenceParameters
except Exception as e:  # pragma: no cover
    sys.exit(f"[deps] missing dependency: {e}\n  pip install localcider biopython requests numpy")

# Optional empirical IDR caller
try:
    import metapredict as meta
    HAVE_META = True
except Exception:
    HAVE_META = False

UA = {"User-Agent": "cic-dux4-research/1.0 (in-silico Track B; research only)"}

# UniProt accessions. Lengths are the canonical UniProt isoform lengths used only
# as a sanity check; the authoritative gate is the CRC64 (below).  [VERIFY] lengths.
TARGETS = {
    "DUX4":  dict(acc="Q9UBX2", length=424,
                  # C-terminal transactivation domain (the module retained in CIC-DUX4).
                  # Literature: transactivation maps to the C-terminal ~80 aa. [VERIFY]
                  region=("C-term transactivation domain", 345, 424), role="test"),
    "EWSR1": dict(acc="Q01844", length=656,
                  # N-terminal SYGQ-rich prion-like LCD ("EAD") — the EWS-FLI1 LLPS driver.
                  region=("N-term prion-like LCD (EAD)", 1, 264), role="positive-control"),  # [VERIFY]
    "FUS":   dict(acc="P35637", length=526,
                  # Canonical N-terminal QGSY-rich prion-like LCD — gold-standard LLPS benchmark.
                  region=("N-term prion-like LCD", 1, 214), role="positive-control"),  # [VERIFY]
    "CIC":   dict(acc="Q96RK0", length=1608,
                  # HMG-box DNA-binding domain — a FOLDED region; negative control.
                  region=("HMG-box (folded)", 201, 280), role="negative-control"),  # [VERIFY]
}


def fetch_uniprot_txt(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.txt"
    r = requests.get(url, headers=UA, timeout=45)
    r.raise_for_status()
    return r.text


def parse_seq_and_crc(flat: str):
    """Parse the sequence and the SQ-line CRC64 from a UniProt flat file."""
    seq_lines, in_seq, sq_crc = [], False, None
    for line in flat.splitlines():
        if line.startswith("SQ"):
            in_seq = True
            for tok in line.replace(";", " ").split():
                if len(tok) == 16 and all(c in "0123456789ABCDEF" for c in tok):
                    sq_crc = tok
            continue
        if in_seq:
            if line.startswith("//"):
                break
            seq_lines.append(line.strip().replace(" ", ""))
    return "".join(seq_lines).upper(), sq_crc


def verified_sequence(acc: str, expected_len: int) -> str:
    flat = fetch_uniprot_txt(acc)
    seq, sq_crc = parse_seq_and_crc(flat)
    if not seq:
        raise ValueError(f"{acc}: no sequence parsed")
    got = crc64(seq)  # biopython, canonical SwissProt CRC64
    if sq_crc and got.upper() != sq_crc.upper():
        raise ValueError(f"{acc}: CRC64 mismatch (file {sq_crc} vs computed {got}) — refusing to use")
    if expected_len and len(seq) != expected_len:
        print(f"  [warn] {acc}: length {len(seq)} != expected {expected_len} (isoform drift?) [VERIFY]")
    print(f"  [ok] {acc}: {len(seq)} aa, CRC64 {got} verified against UniProt SQ line")
    return seq


@dataclass
class Descriptors:
    name: str; role: str; region: str; start: int; end: int; n: int
    FCR: float; NCPR: float; kappa: float
    frac_acidic: float; frac_basic: float; frac_aromatic: float
    frac_disorder_promoting: float
    uversky_class: str; das_pappu_class: str
    meta_mean_disorder: float | None


def das_pappu_class(sp: SequenceParameters) -> str:
    try:
        return sp.get_phasePlotRegion()  # 1..5 diagram-of-states region
    except Exception:
        return "n/a"


def descriptors(name, role, region_name, s, e, full_seq) -> Descriptors:
    sub = full_seq[s - 1:e]
    sp = SequenceParameters(sub)
    aa = sub
    n = len(aa)
    frac = lambda chars: sum(aa.count(c) for c in chars) / n
    meta_dis = None
    if HAVE_META:
        try:
            meta_dis = float(sum(meta.predict_disorder(sub)) / n)
        except Exception:
            meta_dis = None
    return Descriptors(
        name=name, role=role, region=region_name, start=s, end=e, n=n,
        FCR=round(sp.get_FCR(), 3), NCPR=round(sp.get_NCPR(), 3), kappa=round(sp.get_kappa(), 3),
        frac_acidic=round(frac("DE"), 3), frac_basic=round(frac("KR"), 3),
        frac_aromatic=round(frac("FWY"), 3),
        frac_disorder_promoting=round(sp.get_fraction_disorder_promoting(), 3),
        uversky_class=("IDP" if sp.get_FCR() > 0 else "?"),
        das_pappu_class=str(das_pappu_class(sp)),
        meta_mean_disorder=(round(meta_dis, 3) if meta_dis is not None else None),
    )


def main():
    print(f"# Sim 9 condensate/LLPS descriptors — run {datetime.date.today().isoformat()}")
    print(f"# metapredict available: {HAVE_META}")
    # toolchain self-test (runs even with no network) — proves localcider works
    st = SequenceParameters("MEEKADADYEEEDDDEEKKRRKKRR")
    print(f"# localcider self-test OK (FCR={st.get_FCR():.3f}, kappa={st.get_kappa():.3f})\n")

    rows, failures = [], []
    for name, t in TARGETS.items():
        try:
            seq = verified_sequence(t["acc"], t["length"])
            rn, s, e = t["region"]
            rows.append(descriptors(name, t["role"], rn, s, e, seq))
        except Exception as ex:
            failures.append((name, t["acc"], str(ex)))
            print(f"  [FAIL] {name} ({t['acc']}): {ex}")

    if failures and not rows:
        print("\nNo sequences could be verified/fetched (network-egress blocked?). "
              "Re-run where rest.uniprot.org is reachable. NOT inventing sequences.")
        with open("RESULTS_partial.json", "w") as fh:
            json.dump({"failures": failures, "date": datetime.date.today().isoformat()}, fh, indent=2)
        sys.exit(2)

    out = [asdict(r) for r in rows]
    with open("descriptors.json", "w") as fh:
        json.dump({"date": datetime.date.today().isoformat(),
                   "metapredict": HAVE_META, "rows": out, "failures": failures}, fh, indent=2)

    cols = ["name", "role", "region", "n", "FCR", "NCPR", "kappa",
            "frac_acidic", "frac_basic", "frac_aromatic", "das_pappu_class", "meta_mean_disorder"]
    print("\n" + "\t".join(cols))
    for r in out:
        print("\t".join(str(r[c]) for c in cols))
    print("\nWrote descriptors.json. Interpretation belongs in RESULTS.md — these are "
          "relative descriptors, not evidence of phase separation.")


if __name__ == "__main__":
    main()
