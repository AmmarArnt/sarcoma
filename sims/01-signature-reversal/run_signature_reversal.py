#!/usr/bin/env python3
"""CIC-DUX4 signature-reversal drug repurposing.

Real data only:
  - GEO GSE60740 series matrix (microarray, GPL17811 Brainarray Entrez CDF, gcrma log2).
    The CIC-DUX4 on/off contrast is IB120 cells: empty vector (fusion ON) vs
    CIC-DUX4 shRNA (fusion OFF/knockdown).
  - NCBI Homo_sapiens.gene_info.gz for Entrez->HGNC symbol mapping.
  - L1000CDS2 (Ma'ayan lab) for signature reversal (aggravate=False = find perturbagens
    that REVERSE the input signature, i.e. mimic CIC-DUX4 knockdown).

No fabrication: every value is computed from the downloaded files / live API.
"""
from __future__ import annotations
import gzip, io, json, os, sys, hashlib, datetime, urllib.request
import pandas as pd, numpy as np, requests

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
os.makedirs(DATA, exist_ok=True)

MATRIX_URL = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE60nnn/GSE60740/matrix/GSE60740_series_matrix.txt.gz"
GENEINFO_URL = "https://ftp.ncbi.nlm.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz"
L1000_URL = "https://maayanlab.cloud/L1000CDS2/query"

# Sample groups read from the real series-matrix metadata (see MANIFEST).
ON_GSM  = ["GSM1486562", "GSM1486563"]                               # IB120 empty vector = CIC-DUX4 ON
OFF_GSM = ["GSM1486558", "GSM1486559", "GSM1486560", "GSM1486561"]   # IB120 CIC-DUX4 shRNA = OFF
N_SIG = 150  # top genes per direction


def _download(url, path):
    if not os.path.exists(path):
        print(f"  downloading {url}")
        urllib.request.urlretrieve(url, path)
    return path


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_matrix(path):
    rows, in_tab = [], False
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("!series_matrix_table_begin"):
                in_tab = True; continue
            if line.startswith("!series_matrix_table_end"):
                break
            if in_tab:
                rows.append(line.rstrip("\n"))
    df = pd.read_csv(io.StringIO("\n".join(rows)), sep="\t")
    df = df.rename(columns={df.columns[0]: "probe"}).set_index("probe")
    # Brainarray probe "<entrez>_at" -> Entrez ID
    df.index = [p.strip('"').replace("_at", "") for p in df.index]
    df.columns = [c.strip('"') for c in df.columns]
    return df


def entrez_to_symbol(path):
    m = {}
    with gzip.open(path, "rt") as fh:
        header = fh.readline().rstrip("\n").lstrip("#").split("\t")
        gi, si = header.index("GeneID"), header.index("Symbol")
        for line in fh:
            f = line.rstrip("\n").split("\t")
            m[f[gi]] = f[si]
    return m


def l1000_reverse(up, dn):
    payload = {"data": {"upGenes": up, "dnGenes": dn},
               "config": {"aggravate": False, "searchMethod": "geneSet",
                          "share": True, "combination": False, "db-version": "latest"}}
    r = requests.post(L1000_URL, data=json.dumps(payload),
                      headers={"content-type": "application/json"}, timeout=120)
    r.raise_for_status()
    return r.json()


# Mechanistic class tags for interpretation (substring match on pert_desc, lowercased).
CLASS = {
    "MEK/ERK": ["selumetinib", "trametinib", "pd-0325901", "pd-184352", "ci-1040", "pd-98059", "u0126", "refametinib", "binimetinib", "cobimetinib"],
    "BET/BRD4": ["jq1", "i-bet", "bet bromodomain", "otx015", "birabresib"],
    "HDAC": ["vorinostat", "trichostatin", "panobinostat", "entinostat", "mocetinostat", "belinostat", "scriptaid", "hdac", "apicidin", "romidepsin"],
    "CDK": ["palbociclib", "alvocidib", "flavopiridol", "dinaciclib", "pha-793887", "roscovitine", "seliciclib", "cdk", "purvalanol", "sns-032"],
    "EZH2/PRC2": ["ezh2", "tazemetostat", "gsk126", "ell3"],
    "TopoII/anthracycline": ["doxorubicin", "etoposide", "daunorubicin", "mitoxantrone", "teniposide", "idarubicin", "epirubicin"],
    "IGF1R": ["linsitinib", "bms-754807", "nvp-aew541", "igf-1r", "picropodophyllin", "ppp", "gsk1838705"],
    "PI3K/mTOR/AKT": ["wortmannin", "ly-294002", "rapamycin", "sirolimus", "everolimus", "torin", "pi-103", "akt", "mk-2206", "pictilisib"],
    "HSP90": ["geldanamycin", "tanespimycin", "17-aag", "radicicol", "alvespimycin", "hsp90"],
    "Proteasome": ["bortezomib", "mg-132", "carfilzomib", "mg132"],
    "Aurora/PLK/WEE1/mitotic": ["aurora", "plk", "wee1", "mk-1775", "adavosertib", "barasertib", "tozasertib", "vx-680", "alisertib"],
    "Topoisomerase I": ["camptothecin", "topotecan", "irinotecan", "sn-38"],
}


def classify(desc):
    d = (desc or "").lower()
    return [cls for cls, kws in CLASS.items() if any(k in d for k in kws)]


def main():
    print("[1] downloading inputs")
    mpath = _download(MATRIX_URL, os.path.join(DATA, "GSE60740_series_matrix.txt.gz"))
    gpath = _download(GENEINFO_URL, os.path.join(DATA, "Homo_sapiens.gene_info.gz"))

    print("[2] loading matrix + mapping")
    df = load_matrix(mpath)
    missing = [g for g in ON_GSM + OFF_GSM if g not in df.columns]
    if missing:
        sys.exit(f"FATAL: expected samples missing from matrix: {missing}")
    sym = entrez_to_symbol(gpath)

    print(f"    matrix: {df.shape[0]} probes x {df.shape[1]} samples")
    print(f"    ON (empty vector):  {ON_GSM}")
    print(f"    OFF (CIC-DUX4 shRNA): {OFF_GSM}")

    print("[3] differential expression (log2FC = mean ON - mean OFF; data are gcrma log2)")
    on = df[ON_GSM].mean(axis=1)
    off = df[OFF_GSM].mean(axis=1)
    lfc = (on - off).rename("log2FC").to_frame()
    lfc["symbol"] = [sym.get(e) for e in lfc.index]
    lfc = lfc.dropna(subset=["symbol"])
    lfc = lfc[~lfc["symbol"].duplicated(keep="first")]  # one probe per symbol (already 1:1 in CDF)

    up = lfc.sort_values("log2FC", ascending=False).head(N_SIG)   # CIC-DUX4-activated
    dn = lfc.sort_values("log2FC", ascending=True).head(N_SIG)    # CIC-DUX4-repressed
    up_syms = up["symbol"].tolist()
    dn_syms = dn["symbol"].tolist()
    lfc.sort_values("log2FC", ascending=False).to_csv(os.path.join(HERE, "cic_dux4_signature.csv"))
    print(f"    up (fusion-activated) n={len(up_syms)}; e.g. {up_syms[:8]}")
    print(f"    dn (fusion-repressed) n={len(dn_syms)}; e.g. {dn_syms[:8]}")

    print("[4] L1000CDS2 reversal query (aggravate=False -> mimic knockdown)")
    res = l1000_reverse(up_syms, dn_syms)
    top = res.get("topMeta", [])
    share_id = res.get("shareId") or res.get("share_id")
    print(f"    returned {len(top)} perturbagen hits; shareId={share_id}")

    recs = []
    for m in top:
        recs.append({
            "pert_desc": m.get("pert_desc"), "score": m.get("score"),
            "cell_id": m.get("cell_id"), "pert_dose": m.get("pert_dose"),
            "pert_time": m.get("pert_time"), "pubchem_id": m.get("pubchem_id"),
            "classes": ";".join(classify(m.get("pert_desc"))),
        })
    out = pd.DataFrame(recs)
    out.to_csv(os.path.join(HERE, "l1000_reversers.csv"), index=False)

    # Class-level summary among named hits
    named = out[out["pert_desc"].notna() & (out["pert_desc"] != "-666")]
    class_hits = {}
    for _, row in named.iterrows():
        for c in (row["classes"].split(";") if row["classes"] else []):
            class_hits.setdefault(c, []).append(row["pert_desc"])

    print("\n=== TOP REVERSERS (named) ===")
    for _, row in named.head(20).iterrows():
        print(f"    score={row['score']:.3f}  {row['pert_desc']:<22} [{row['classes']}]  ({row['cell_id']})")
    print("\n=== MECHANISTIC CLASS HITS ===")
    for c, lst in sorted(class_hits.items(), key=lambda kv: -len(kv[1])):
        uniq = sorted(set(lst))
        print(f"    {c}: {len(lst)} hit(s) -> {uniq[:6]}")

    # entities for NER grounding
    ents = sorted(set(up_syms[:30] + dn_syms[:30] + named["pert_desc"].head(25).tolist()))
    with open(os.path.join(HERE, "entities.txt"), "w") as fh:
        fh.write(". ".join(str(e) for e in ents) + ".\n")

    with open(os.path.join(HERE, "result_meta.json"), "w") as fh:
        json.dump({"shareId": share_id, "n_hits": len(top),
                   "class_hits": {k: sorted(set(v)) for k, v in class_hits.items()},
                   "up_top": up_syms[:30], "dn_top": dn_syms[:30]}, fh, indent=2)

    # manifest
    with open(os.path.join(HERE, "MANIFEST.md"), "w") as fh:
        fh.write("# Manifest — signature reversal\n\n")
        fh.write(f"Access date: {datetime.date.today().isoformat()}\n\n")
        fh.write(f"- GSE60740 series matrix: {MATRIX_URL}\n")
        fh.write(f"  - sha256: {sha256(mpath)}  size: {os.path.getsize(mpath)} bytes\n")
        fh.write(f"- NCBI gene_info: {GENEINFO_URL}\n")
        fh.write(f"  - sha256: {sha256(gpath)}  size: {os.path.getsize(gpath)} bytes\n")
        fh.write(f"- L1000CDS2: {L1000_URL} (aggravate=False, geneSet); shareId={share_id}\n")
        fh.write(f"  - view: https://maayanlab.cloud/L1000CDS2/#/result/{share_id}\n")
        fh.write("\nSample groups (from series-matrix metadata):\n")
        fh.write(f"- CIC-DUX4 ON (IB120 empty vector): {ON_GSM}\n")
        fh.write(f"- CIC-DUX4 OFF (IB120 CIC-DUX4 shRNA_1/_2): {OFF_GSM}\n")

    print("\n[done] wrote cic_dux4_signature.csv, l1000_reversers.csv, result_meta.json, entities.txt, MANIFEST.md")


if __name__ == "__main__":
    main()
