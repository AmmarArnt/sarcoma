# 07 — OpenMed NER Models: Per-Team Mapping and Usage

This file maps each agent in `06-agent-architecture.md` to one or more OpenMed NER models that the agent should call when it needs to extract structured biomedical entities (genes, drugs, chemicals, diseases, anatomy, organisms, DNA elements, proteins) from passages of literature, clinical-trial text, or its own draft output.

The models are *Named Entity Recognition* models — they label spans, not generate prose. Their role in this simulation is **grounding**: they let an agent verify that the entities it is talking about are recognised, well-named biomedical terms, not invented words. They are **not** a replacement for the agent's reasoning, mechanism statements, or evidence-tiering — those still come from the agent itself.

---

## Install (one-time)

Apple Silicon Mac (this machine):

```bash
python3.13 -m venv .venv
.venv/bin/pip install --upgrade pip 'openmed[mlx]' torch
```

`torch` is required because the MLX backend uses HuggingFace's `AutoModelForTokenClassification` once per model to fetch and convert weights to MLX format; after conversion, inference runs on MLX-Metal without torch.

Models download from HuggingFace on first use and are cached under `~/.cache/openmed/` (MLX-converted weights) and `~/.cache/huggingface/` (tokenizers/configs).

---

## How an agent invokes a model

The simplest call pattern (Python — for agents that shell out via `Bash`):

```python
from openmed import analyze_text, OpenMedConfig

cfg = OpenMedConfig(backend="mlx")
result = analyze_text(
    "EZH2 inhibition with tazemetostat depletes H3K27me3 and may restore MHC-I.",
    model_name="oncology_detection_superclinical",   # registry alias
    config=cfg,
    confidence_threshold=0.65,
)
for e in result.entities:
    print(f"{e.label:<25} {e.text:<30} {e.confidence:.2f}")
```

A wrapper CLI is provided at `scripts/openmed_ner.py` so agents can call models from the shell:

```bash
.venv/bin/python scripts/openmed_ner.py \
    --team v3-epigenetic \
    --text "EZH2 inhibition with tazemetostat depletes H3K27me3."
```

It prints JSON with one entity per row and applies the per-team default model(s).

---

## Model registry — what each model detects

| Registry alias | HuggingFace ID | Detects | Recommended confidence |
|---|---|---|---|
| `oncology_detection_superclinical` | `OpenMed/OpenMed-NER-OncologyDetect-SuperClinical-434M` | Cancer, Cell, Gene_or_gene_product | 0.65 |
| `disease_detection_superclinical` | `OpenMed/OpenMed-NER-DiseaseDetect-SuperClinical-434M` | DISEASE, CONDITION, PATHOLOGY | 0.65 |
| `pharma_detection_superclinical` | `OpenMed/OpenMed-NER-PharmaDetect-SuperClinical-434M` | CHEM, DRUG, MEDICATION | 0.70 |
| `chemical_detection_pubmed` | `OpenMed/OpenMed-NER-ChemicalDetect-PubMed-335M` | Simple_chemical, CHEM | 0.65 |
| `genome_detection_bioclinical` | `OpenMed/OpenMed-NER-GenomeDetect-BioClinical-108M` | Gene_or_gene_product, GENE, PROTEIN | 0.65 |
| `dna_detection_supermedical` | `OpenMed/OpenMed-NER-DNADetect-SuperMedical-125M` | Gene_or_gene_product, DNA | 0.65 |
| `protein_detection_pubmed` | `OpenMed/OpenMed-NER-ProteinDetect-PubMed-109M` | Gene_or_gene_product, PROTEIN | 0.65 |
| `anatomy_detection_electramed` | `OpenMed/OpenMed-NER-AnatomyDetect-ElectraMed-109M` | Organ, Tissue, ANATOMY | 0.60 |
| `species_detection_bioclinical` | `OpenMed/OpenMed-NER-SpeciesDetect-BioClinical-108M` | Organism, SPECIES | 0.60 |

Two models in the OpenMed catalogue are intentionally **not** in the default mapping:

- **PathologyDetect (ModernClinical-395M)** — uses ModernBERT, which the current openmed MLX backend does not yet support; PyTorch-only on Apple Silicon, which negates the MLX speed-up. Not needed for any of the four vectors here.
- **BloodCancerDetect (SuperClinical-434M)** — for hematologic malignancies. CIC-rearranged sarcoma is a solid mesenchymal tumour, so this model would mislabel and is excluded by design.

---

## Team → Model mapping

The rule of thumb behind these assignments:

- **Oncology + Genomics/Protein models** for any agent reasoning about the fusion, downstream transcriptional program, or targeted therapy.
- **Chemical + Pharma models** for any agent reasoning about compounds, supplements, drugs, or PK.
- **Disease + Anatomy models** for any agent reasoning about the tumour microenvironment, immune cells, or clinical presentation.
- **Species model** for microbiome work.
- **DNA / Protein models** for DNA-repair and synthetic-lethality work.

Each team gets a **primary** model (always-on) and optional **secondary** models that the agent should reach for when its draft mentions the relevant entity class.

### Orchestrator

Synthesises across all four vectors; needs broad coverage to deduplicate entries and resolve conflicts.

- Primary: `oncology_detection_superclinical`
- Secondary: `pharma_detection_superclinical`, `disease_detection_superclinical`

### V1 — Rate Limiting

Targets RAS/ERK amplitude, BRD4 super-enhancer amplification, CDK4/CCND1 — all compound-and-target territory.

- **V1 Lead**: `chemical_detection_pubmed` + `pharma_detection_superclinical` + `oncology_detection_superclinical`
- **V1 Food Specialist**: `chemical_detection_pubmed` (bioactive plant compounds)
- **V1 Supplement Specialist**: `pharma_detection_superclinical` + `chemical_detection_pubmed` (drug-supplement interactions, CYP3A4/2C9/P-gp)
- **V1 Bioavailability Specialist**: `pharma_detection_superclinical` + `chemical_detection_pubmed` (PK terminology)

### V2 — Compiler Protection

Targets double-strand-break rates and repair fidelity in mesenchymal progenitors.

- **V2 Lead**: `dna_detection_supermedical` + `chemical_detection_pubmed` + `disease_detection_superclinical`
- **V2 Antioxidant Specialist**: `chemical_detection_pubmed` + `oncology_detection_superclinical` (ROS sources, polyphenols, the ATBC/CARET/SELECT harm signal in cancer outcomes)
- **V2 DNA Repair Specialist**: `dna_detection_supermedical` + `genome_detection_bioclinical` + `protein_detection_pubmed` (Ku70/Ku80, NHEJ/HR, PARP, sirtuins)
- **V2 Anti-Inflammatory Specialist**: `chemical_detection_pubmed` + `disease_detection_superclinical` (cytokines, SPMs, NF-κB)

### V3 — Hot Patching

The most clinically loaded vector. EZH2/BET/HDAC inhibitors, differentiation agents, PROTAC/ASO pipeline, synthetic lethality.

- **V3 Lead**: `oncology_detection_superclinical` + `pharma_detection_superclinical` + `protein_detection_pubmed`
- **V3 Epigenetic Therapy Specialist**: `oncology_detection_superclinical` + `pharma_detection_superclinical` + `protein_detection_pubmed` (must also handle MHC-I upregulation entities — the V3→V4 bridge)
- **V3 Differentiation Therapy Specialist**: `oncology_detection_superclinical` + `chemical_detection_pubmed` (ATRA, vitamin D3 axis, butyrate)
- **V3 PROTAC/ASO Specialist** (clinical): `pharma_detection_superclinical` + `oncology_detection_superclinical` + `protein_detection_pubmed` (clinical pipeline + NCT IDs)
- **V3 Synthetic Lethality Specialist**: `oncology_detection_superclinical` + `genome_detection_bioclinical` + `protein_detection_pubmed` (BRD4 addiction, PRC2 dependency, CDK4/CCND1)

### V4 — Immune Watchdog

Restoring immune visibility and clearance. Depends on V3 for the MHC-I upregulation handoff.

- **V4 Lead**: `disease_detection_superclinical` + `oncology_detection_superclinical` + `anatomy_detection_electramed`
- **V4 Checkpoint / T-cell Specialist**: `pharma_detection_superclinical` + `disease_detection_superclinical` + `anatomy_detection_electramed` (PD-1/PD-L1/CTLA-4, SARC028)
- **V4 NK Cell Specialist**: `protein_detection_pubmed` + `disease_detection_superclinical` + `anatomy_detection_electramed` (KIR, NKG2D, missing-self)
- **V4 Microbiome-Immune Specialist**: `species_detection_bioclinical` + `chemical_detection_pubmed` (Akkermansia, Bifidobacterium, SCFAs)
- **V4 Neoantigen Vaccine Specialist** (clinical): `pharma_detection_superclinical` + `protein_detection_pubmed` + `oncology_detection_superclinical` (BNT122, mRNA-4157, CAR-T)

### mRNA Vaccine Research Team (supplementary)

Investigates whether BNT162b2 modulates immune, inflammatory, or genomic context relevant to sarcoma. Mostly disease + pharma + immune entities; oncology coverage needed for pharmacovigilance signal-checking.

- **mRNA Vaccine Team Lead** (`mrna-vaccine-lead`): `disease_detection_superclinical` + `pharma_detection_superclinical` + `oncology_detection_superclinical`
- **mRNA Immunological Effects Specialist** (`mrna-immune-effects`): `disease_detection_superclinical` + `protein_detection_pubmed` + `anatomy_detection_electramed` (T-cell, NK, cytokines, lymphoid tissue)
- **mRNA Oncogenic Risk Specialist** (`mrna-oncogenic-risk`): `oncology_detection_superclinical` + `disease_detection_superclinical` + `pharma_detection_superclinical` (pharmacovigilance signal review)

### Metastatic Disease Specialist (orchestrator sub-agent)

Examines whether the four vectors apply equally to distant metastases. Multi-organ disease biology; needs oncology + anatomy + disease coverage to handle bone/lung/liver/CNS metastatic sites and their stromal/immune environments.

- **Metastatic Disease Specialist** (`metastatic-specialist`): `oncology_detection_superclinical` + `anatomy_detection_electramed` + `disease_detection_superclinical`

---

## How to use the models inside the agent workflow

The intended pattern, per the constraints in `00-README.md` (mechanism before recommendation, real citations, evidence tiers):

1. **Draft.** The agent writes its candidate list with mechanisms in its own words.
2. **Ground.** The agent runs each compound / gene / drug / pathway mention through its primary model (`scripts/openmed_ner.py --team <team-id>`).
3. **Reconcile.**
   - If an entity is **recognised** with high confidence (≥ recommended threshold above) → use it as written.
   - If an entity is **not recognised** → either it is a novel coinage or a misspelling. The agent must either (a) restate it using the canonical term the model would recognise, or (b) flag it explicitly as "no canonical NER match — verify spelling/term."
4. **Cross-reference.** For each entity the model surfaces, the agent's mechanism statement should explain how that entity participates in the vector's intervention logic — anchored to a real citation per the constraints in `06-agent-architecture.md`.

The NER models do **not** evaluate evidence, dose, or safety. They only confirm that the words name real biomedical entities. The orchestrator and human review still bear the citation-discipline burden.

---

## Failure modes the NER step does NOT catch

- Fabricated citations — NER does not check PMIDs / NCT IDs.
- Concentration mismatches — NER does not know if 50 µM is achievable in vivo.
- Analogy-as-evidence drift — NER does not flag "hot-patch" prose.
- Standard-of-care contraindications — NER does not know that high-dose antioxidants interfere with doxorubicin.

These remain the responsibility of the agents and orchestrator, per `06-agent-architecture.md` § "Common Failure Modes".
