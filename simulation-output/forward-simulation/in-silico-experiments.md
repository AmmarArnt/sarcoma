# In-Silico Experiment Catalog — Forward Simulation on CIC-DUX4

> **Supplementary team output: "In-Silico Experiment Designer."** This is a *floor-not-ceiling*, forward-simulation deliverable. It answers the literal question: **"What computational simulations could a skilled developer run on the molecule themselves, in a software environment, to generate forward hypotheses about CIC-DUX4 (and the fusion-unconfirmed atypical case)?"**
>
> **One-line summary:** A runnable catalog of in-silico experiments — structure prediction, condensate/LLPS prediction, docking/virtual screen, molecular dynamics, network/dynamical modeling, transcriptomic-signature reversal, dependency mining, and PK exposure modeling — with the real tools, real data sources, compute/skill cost, and an honest statement of what each result would and would NOT tell you. It deliberately **excludes**: any clinical dosing, any wet-lab protocol, any claim that a simulation result is therapeutic evidence.
>
> **Confidence: medium.** The tools, databases, and methods named here are well-established in the computational-biology literature through the assistant's January 2026 knowledge cutoff and are the standard instruments a skilled person would reach for. **However, this environment had no network access — WebSearch, WebFetch, and outbound HTTP were all blocked — so I could NOT live-verify a single tool URL, database accession, or PDB ID at write time.** Per the project contract ("never invent a database, tool, or accession; if unsure, say so"), every accession, PDB ID, cell-line ID, and tool name below carries a **[VERIFY]** flag. Treat each as a *strong lead to confirm in one click*, not as a confirmed fact. Where I am genuinely unsure something exists, I say so explicitly rather than presenting it as real.

---

## How to read the [VERIFY] flags

- **[VERIFY]** — I believe this tool/database/accession is real and correctly named from training knowledge, but I could not confirm it live. Confirm before relying on it. This is the default state of everything network-dependent in this document.
- **[VERIFY-EXISTENCE]** — I am specifically unsure whether the *specific instance* exists (e.g., whether a particular cell line is actually in DepMap, or whether a CIC-DUX4 PDB structure has been deposited). Stated as a question to resolve, not an asserted fact.
- No flag — a method, algorithm, or biological fact that is not a single lookupable accession.

**Atypical-case framing applied throughout:** ~5% of tumors that look like CIC-rearranged sarcoma clinically/histologically have **no confirmed fusion** (not CIC-DUX4, CIC-NUTM1, or CIC-FOXO4) on sequencing. Every experiment below is tagged for whether it **requires a known fusion/junction** (does not apply to the atypical case) or is **fusion-agnostic** (may apply). This matters for *your* patient context: if the junction is unconfirmed, the entire "model the exact fusion protein" branch becomes "model a family of candidate architectures" — which is itself a useful forward experiment (Track A2).

---

## The single most important input you must obtain first: the protein sequence(s)

Almost every structure/condensate/docking experiment needs an amino-acid sequence. For a confirmed CIC-DUX4 case you need the **fusion junction**, which you do not have. So you will work with:

1. **Wild-type CIC** — UniProt **Q96RK0** (human CIC / Capicua) **[VERIFY]**. Contains the HMG-box DNA-binding domain.
2. **Wild-type DUX4** — UniProt **Q9UBX2** (human DUX4) **[VERIFY]**. Contains the tandem (double) homeodomain and the C-terminal acidic transactivation domain.
3. **Constructed fusion candidates** — because the junction is unconfirmed, you *build* candidate fusion sequences in silico by concatenating CIC(N-terminus + HMG-box) to DUX4(C-terminal transactivation domain) at several plausible breakpoints reported in the literature (CIC is commonly broken near exon ~20; DUX4 contributes its C-terminus). This is exactly the kind of "what-if" the patient's atypical/unconfirmed status motivates.

> Sequence retrieval is doable offline-ish: UniProt entries can be downloaded as FASTA; PDB structures as `.pdb`/`.cif`. You will need network access on *your* machine (this analysis environment did not have it).

---

# TRACK A — STRUCTURE PREDICTION

**Fusion-status:** A1 is fusion-agnostic (model the wild-type domains). A2 explicitly handles the **unconfirmed-junction** case and is the most relevant branch for the atypical patient.

### A1. Predict the structure of the individual functional domains and the wild-type proteins

1. **Question it answers:** What is the 3D fold of the CIC HMG-box (DNA-binding), the DUX4 double-homeodomain (DNA-binding), and the DUX4 C-terminal transactivation domain (likely disordered)? Where are the structured vs. disordered regions?
2. **Tools (real names):**
   - **ColabFold** (AlphaFold2 + MMseqs2) — Google Colab notebook, free GPU tier. **[VERIFY]** (`ColabFold` / `AlphaFold2_mmseqs2.ipynb`, Mirdita et al., *Nat Methods* 2022 — **[VERIFY] PMID**).
   - **ESMFold** — single-sequence, no MSA, very fast; runnable locally or via the ESM Atlas API. **[VERIFY]** (Lin et al., *Science* 2023 — **[VERIFY] PMID**).
   - **AlphaFold3** server (free for non-commercial via the AlphaFold Server / Google DeepMind) for complexes including protein–DNA. **[VERIFY]** that AF3 server access terms still permit your use case.
   - You may also simply **download the existing AlphaFold DB models** for Q96RK0 and Q9UBX2 from the **AlphaFold Protein Structure Database (alphafold.ebi.ac.uk)** **[VERIFY]** — no compute needed.
3. **Input + where to get it:** UniProt FASTA for Q96RK0, Q9UBX2 **[VERIFY]**. For the DNA-bound HMG-box, an experimental template may exist — **[VERIFY-EXISTENCE]** whether a CIC HMG-box:DNA co-crystal is in the PDB; I cannot assert a specific PDB ID for it without inventing one, so I am NOT giving one. (HMG-box:DNA structures from *other* proteins, e.g. SRY/LEF1/SOX family, exist and are widely used as templates — confirm a real ID before use.)
4. **Compute/skill:** Low. A single domain folds in minutes on free Colab GPU. Skill: copy-paste a sequence into a notebook.
5. **What a result tells you / does NOT:** Tells you the fold and per-residue confidence (pLDDT) — high pLDDT for the HMG-box and homeodomains, low pLDDT (= predicted disorder) for the transactivation/acidic region. Does **NOT** tell you the *fusion* behavior, DNA-binding affinity, or anything functional; pLDDT is a confidence metric, not a stability or activity measurement.
6. **CIC-DUX4 angle:** Establishes the structural parts list before you build the fusion. The expectation — HMG-box folded, DUX4 homeodomains folded, DUX4 C-terminus disordered/acidic — is the structural substrate for the condensate hypothesis in Track B.

### A2. Model candidate fusion architectures (the unconfirmed-junction experiment)

1. **Question:** Given no confirmed junction, what does each plausible CIC-DUX4 architecture look like, and do any of them place the HMG-box and the DUX4 transactivation domain in a configuration that could co-fold or sterically interfere?
2. **Tools:** ColabFold/AF3 on each constructed fusion FASTA (see "single most important input" above). Run 3–5 junction variants. Compare with **FoldSeek** **[VERIFY]** to cluster the predicted folds.
3. **Input:** Self-constructed fusion FASTAs (CIC N-term+HMG ⊕ DUX4 C-term at varying breakpoints). No external accession needed beyond the two parent sequences.
4. **Compute/skill:** Low–medium. A few Colab runs. Skill: string manipulation in Python to build the constructs; judgment to choose plausible breakpoints (consult the CIC-DUX4 fusion literature for reported exon boundaries — **[VERIFY] the specific exon numbers** before trusting any single construct).
5. **What it tells you / does NOT:** Tells you whether the linker/junction region is predicted ordered or disordered and whether domains are predicted to pack against each other. Does **NOT** tell you which junction your patient actually has, nor whether the fusion is functional — and AF/ESM are trained on natural proteins, so **predictions on artificial fusions are lower-confidence by construction**. Treat as hypothesis generation only.
6. **CIC-DUX4 angle:** This is the *forward* move the unconfirmed-fusion status demands — instead of one structure, you enumerate the architecture space and ask which features are invariant across junction choices (those invariants are the robust drug-target hypotheses).

### A3. Disorder prediction

1. **Question:** Which regions of CIC, DUX4, and the fusion are intrinsically disordered (the regions most relevant to phase separation and to "undruggable by classic pocket docking")?
2. **Tools:** **IUPred3** (iupred3.elte.hu) **[VERIFY]**; **AlphaFold pLDDT** as an orthogonal disorder proxy (low pLDDT ≈ disorder); **metapredict v2** **[VERIFY]** for a fast consensus; **flDPnn** **[VERIFY]** as a third method.
3. **Input:** The same FASTA sequences.
4. **Compute/skill:** Trivial. Web forms or a pip-installable package. Minutes.
5. **What it tells you / does NOT:** Tells you the disordered fraction and where the low-complexity/acidic stretches are. Does **NOT** prove phase separation (that's Track B) and does **NOT** distinguish "disordered and functional" from "disordered and inert."
6. **CIC-DUX4 angle:** The DUX4 C-terminal acidic transactivation domain is the prime suspect for an IDR-driven condensate; quantifying its disorder is the prerequisite for Track B's LLPS prediction.

---

# TRACK B — CONDENSATE / LIQUID-LIQUID PHASE SEPARATION (LLPS)

**Fusion-status:** Fusion-agnostic for the parent domains; fusion-specific when you score a constructed junction. The whole track is **Mechanistic / Theoretical** for CIC-DUX4 — the contract docs explicitly warn that condensate biology is best-supported for **EWSR1-based** fusions (Ewing, DSRCT) and is *less directly demonstrated* for CIC-DUX4. Keep that front-and-center.

### B1. Predict phase-separation propensity of the fusion and its low-complexity/acidic regions

1. **Question:** Is CIC-DUX4 (or its DUX4-derived acidic region) predicted to drive or partition into biomolecular condensates, the way EWS-FLI1's IDR does?
2. **Tools (all real, all sequence-based predictors):**
   - **FuzDrop** (fuzdrop.bio.unipd.it) **[VERIFY]** — droplet-promoting probability (pDP) and per-residue droplet-promoting regions.
   - **catGRANULE 2.0** **[VERIFY]** — RNA/protein granule propensity (Bologna group).
   - **PScore** **[VERIFY]** — π-π contact-based LLPS predictor (Vernon et al., *eLife* 2018 — **[VERIFY] PMID**).
   - **PLAAC** (plaac.wi.mit.edu) **[VERIFY]** — prion-like domain detector (relevant for low-complexity sequence).
   - Optional cross-check: **PSPredictor / PSPHunter** family **[VERIFY-EXISTENCE]** — I am less certain of the exact current name; verify before citing.
3. **Input:** FASTA of the fusion candidates and, as a positive-control benchmark, **EWSR1-FLI1** (build from UniProt **Q01844** EWSR1 **[VERIFY]** + **Q01543** FLI1 **[VERIFY]**) and a known LLPS protein (e.g., FUS) as a calibration anchor.
4. **Compute/skill:** Low. Mostly web servers; PLAAC/PScore have downloadable code. Hours including interpretation.
5. **What a result tells you / does NOT:** Tells you a *relative ranking* of phase-separation propensity (e.g., "DUX4 acidic region scores in the LLPS-prone range, comparable to FUS; the HMG-box does not"). Does **NOT** prove condensates form in cells, does **NOT** give saturation concentration, and these predictors are trained largely on a small set of known LLPS proteins → **out-of-distribution risk is high**. This is a hypothesis-prioritization tool, not evidence.
6. **CIC-DUX4 angle — the forward hypothesis embedded here:** *If* CIC-DUX4 scores LLPS-prone in a region that is invariant across junction choices, that is an in-silico-first argument that CIC-DUX4 forms transcriptional condensates like EWS-FLI1 — a mechanism the literature has under-explored for this fusion. It directly motivates a wet-lab follow-up (1,6-hexanediol sensitivity, optoDroplet, live imaging) without committing wet-lab resources prematurely.

### B2. Coarse-grained MD of the IDR (bridge to Track D)

1. **Question:** Does the predicted IDR actually self-associate / demix in a physics simulation?
2. **Tools:** **HOOMD-blue** or **OpenMM** with the **Mpipi** or **HPS / CALVADOS** coarse-grained IDR force fields **[VERIFY]** (the CALVADOS model, Tesei et al., is the current standard for single-chain and multi-chain IDR phase behavior — **[VERIFY] PMID**).
3. **Input:** IDR sequence from Track A3.
4. **Compute/skill:** Medium–high. CG slab simulations are cheaper than all-atom but still want a GPU and real MD literacy.
5. **What it tells you / does NOT:** Can estimate a relative phase diagram / saturation concentration *within the model's assumptions*. Does **NOT** capture sequence-specific chemistry beyond the CG resolution, nor the in-cell crowding/partners.
6. **CIC-DUX4 angle:** Turns the static B1 score into a (model-bound) phase diagram you can compare against EWS-FLI1 IDR run identically — an apples-to-apples in-silico contrast of the two sarcoma fusions.

---

# TRACK C — DOCKING / VIRTUAL SCREEN

**Honesty banner for the whole track:** Docking scores are **not** binding free energies and **not** Kd. They rank poses; they routinely mis-rank affinities. Every "hit" here is a hypothesis to test, and for **dietary compounds** the dominant reality is the **concentration mismatch** — a compound that docks well at a target it inhibits at 10 µM in a cell line is irrelevant if achievable plasma is 0.1–0.5 µM (Track H quantifies this). This track must be read together with Track H.

**Fusion-status:** C1–C2 are fusion-agnostic (real, structurally characterized targets downstream of the fusion). C3 (docking the *fusion:DNA interface*) is fusion-specific and depends on a predicted structure (Track A) — lowest confidence.

### C1. Dock dietary compounds AND clinical agents against BRD4 BD1

1. **Question:** Do the candidate molecules (EGCG, curcumin, apigenin, quercetin) plausibly occupy the BRD4 BD1 acetyl-lysine pocket, and how do their predicted poses/scores compare to a known BET inhibitor (JQ1, OTX015)?
2. **Tools (real):** **AutoDock Vina** **[VERIFY]**; **smina** (Vina fork, better scoring/minimization) **[VERIFY]**; **gnina** (CNN-rescored docking) **[VERIFY]**; **DiffDock** (diffusion-based blind docking) **[VERIFY]**. Prep with **Meeko/AutoDockTools** and **Open Babel** **[VERIFY]**.
3. **Input + source:** Receptor — **PDB 3MXF** is the ID commonly cited for **BRD4 BD1 in complex with a small-molecule inhibitor (the (+)-JQ1 series)** **[VERIFY]**. *I could not live-confirm 3MXF in this environment — verify it on rcsb.org before use; if it is not BD1+inhibitor, substitute a confirmed BRD4-BD1 structure such as one of the well-known BD1 entries (verify a real ID).* Ligands — fetch SMILES/SDF from **PubChem** **[VERIFY]** (EGCG CID 65064 **[VERIFY]**, curcumin CID 969516 **[VERIFY]**, JQ1 CID 46907787 **[VERIFY]** — confirm each CID). Positive control: co-crystallized ligand redocking (RMSD < 2 Å validates your setup).
4. **Compute/skill:** Low–medium. Vina docks one ligand in seconds–minutes on CPU. Skill: receptor/ligand prep is where errors hide; do the redocking control.
5. **What it tells you / does NOT:** Tells you whether a pose in the BD1 pocket is geometrically plausible and gives a *rank*. Does **NOT** give Kd, does **NOT** confirm cellular BRD4 inhibition, and a good score for a dietary polyphenol does **NOT** overcome the bioavailability gap (Track H). EGCG/curcumin are also notorious **PAINS / promiscuous binders** — flag any hit as likely non-specific until proven otherwise.
6. **CIC-DUX4 angle:** BRD4 at ETS super-enhancers is the documented amplification layer of the fusion's output (docs 02/03). Quantifying how far dietary BET-pathway modulators sit below clinical BET inhibitors *in the same docking experiment* operationalizes the docs' caveat that "dietary BET modulators are weak compared to JQ1/OTX015."

### C2. Dock against EZH2 and CDK6 (and CDK4)

1. **Question:** Same as C1 for the other documented vulnerabilities — EZH2 (PRC2 catalytic SET domain) and CDK4/6.
2. **Tools:** Same docking stack.
3. **Input:** EZH2 — confirm a real EZH2 SET-domain / PRC2 structure on rcsb.org (e.g., EZH2 with a SAM-competitive inhibitor; **I will not assert a PDB ID I cannot verify**). CDK6 — confirm a CDK6:palbociclib-class structure **[VERIFY-EXISTENCE of the exact ID]**. Reference ligands: tazemetostat (EZH2), palbociclib/abemaciclib (CDK4/6) from PubChem **[VERIFY CIDs]**.
4. **Compute/skill:** Low–medium, same as C1.
5. **What it tells you / does NOT:** Same caveats. Note CDK4 vs CDK6 are not interchangeable structurally — pick the right receptor for the right claim.
6. **CIC-DUX4 angle:** EZH2 (silences apoptosis/differentiation; MHC-I bridge to V4) and CDK4/CCND1 (forced cell-cycle gate) are both in the docs' vulnerability table. This lets you compare clinical-agent poses (the real intervention) against dietary "EZH2 modulators" (EGCG/quercetin) to *quantify the gap* rather than assert equivalence.

### C3. Virtual-screen a library against the CIC-DUX4:DNA interface

1. **Question:** Is there any small molecule predicted to block the fusion's HMG-box (or homeodomain) from binding its DNA motif — i.e., disable the fusion's targeting rather than its amplifier?
2. **Tools:** **AutoDock Vina / smina** in batch; orchestrate with **DOCKSTRING** or a simple Python harness; consider **gnina** for rescoring. For the DNA-protein interface, treat the DNA-contacting surface as the "pocket" (HMG-box binds in the minor groove — a shallow, flat interface that is *hard* for small molecules; manage expectations).
3. **Input — libraries (real):** **ZINC20 / ZINC22** (free, purchasable subsets) **[VERIFY]**; **Enamine REAL** (lead-like, screen the free downloadable subsets) **[VERIFY]**; **DrugBank** (approved drugs, for repurposing — note licensing) **[VERIFY]**. Receptor: the Track-A predicted fusion:DNA model (low confidence) or, better, a confirmed CIC/HMG-box:DNA structure if one exists **[VERIFY-EXISTENCE]**.
4. **Compute/skill:** Medium–high. Screening 10⁴–10⁶ compounds wants batching and ideally a GPU/cluster or a long Colab budget. Skill: library prep, hit triage, decoy controls (DUD-E-style) to estimate enrichment.
5. **What it tells you / does NOT:** Tells you *candidate* DNA-binding blockers to prioritize. Does **NOT** account for the docs' point that protein–DNA interfaces are large/flat and historically poor small-molecule targets; a top docking score here is weaker evidence than a top score in a deep enzyme pocket. Very high false-positive rate expected.
6. **CIC-DUX4 angle:** This is the most "attack-the-fusion-directly" in-silico experiment available without wet lab. **Requires a known/assumed junction → does NOT apply to the ~5% atypical fusion-unconfirmed case**, except in the architecture-enumeration sense of Track A2 (screen against the invariant HMG-box, which is present in all CIC-derived fusions).

---

# TRACK D — MOLECULAR DYNAMICS

**Fusion-status:** Pose-stability MD is fusion-agnostic (depends on the target, not the junction). Fusion-domain-dynamics MD on the predicted fusion is fusion-specific and inherits Track A's uncertainty.

### D1. Binding-pose stability MD (rescue docking hits)

1. **Question:** Do the top docking poses from Track C stay bound over a short simulation, or do they drift/dissociate?
2. **Tools:** **OpenMM** (Python-native, Colab-friendly) **[VERIFY]** or **GROMACS** **[VERIFY]**; force fields **AMBER ff14SB/ff19SB** (protein) + **GAFF2/OpenFF** (ligand) **[VERIFY]**; system prep via **OpenFF/OpenMM-Forcefields**, **CHARMM-GUI** **[VERIFY]**.
3. **Input:** Docked complexes from Track C.
4. **Compute/skill:** Medium–high. Even 20–100 ns per complex wants a GPU; Colab can do short runs. Real MD literacy required (equilibration, RMSD/RMSF, contact analysis).
5. **What it tells you / does NOT:** Tells you relative pose stability — a useful triage filter on top of docking. Does **NOT** give Kd from a plain MD run; sampling is far too short for spontaneous binding/unbinding of most ligands.
6. **CIC-DUX4 angle:** Filters the BRD4/EZH2/CDK Track-C hits down to the ones whose poses survive physics, before you ever invoke the expensive free-energy methods.

### D2. Free-energy ranking (MM-GBSA / FEP)

1. **Question:** Among surviving poses, which ligands are predicted to bind more tightly?
2. **Tools:** **MM-GBSA/MM-PBSA** via **gmx_MMPBSA** or **AmberTools (MMPBSA.py)** **[VERIFY]** (cheap, approximate, good for *relative* ranking of congeneric series); **FEP/TI** via **OpenFE** **[VERIFY]** or **GROMACS** (rigorous relative binding free energy for similar ligands, expensive).
3. **Input:** Equilibrated complexes from D1.
4. **Compute/skill:** MM-GBSA medium; FEP high (this is where amateurs get wrong numbers — perturbation maps, convergence checks).
5. **What it tells you / does NOT:** MM-GBSA gives a rough ΔG ranking, unreliable across chemically dissimilar ligands. FEP gives defensible *relative* ΔΔG between similar ligands — still not an absolute Kd, and still model-dependent.
6. **CIC-DUX4 angle:** Lets you ask, quantitatively-within-model, "how many kcal/mol does a dietary polyphenol give up to JQ1 at BRD4 BD1?" — the rigorous version of the concentration-mismatch story.

### D3. Fusion-domain / condensate-region dynamics

1. **Question:** Is the predicted fusion architecture (Track A2) conformationally stable? How does the IDR behave?
2. **Tools:** OpenMM/GROMACS all-atom for folded domains; CALVADOS/Mpipi CG (Track B2) for the IDR.
3. **Input:** Track-A predicted fusion model.
4. **Compute/skill:** High.
5. **What it tells you / does NOT:** Tells you whether the AF-predicted junction is dynamically plausible. Does **NOT** validate that this is the real junction.
6. **CIC-DUX4 angle:** Stress-tests the architecture hypotheses from A2 — junction variants that fall apart in MD are deprioritized.

---

# TRACK E — NETWORK / DYNAMICAL MODEL (the heart of "endless what-if")

**Fusion-status: largely fusion-agnostic.** You model the *pathway logic* (RAS/ERK → CIC de-repression → ETV1/4/5 → BRD4/super-enhancer → CCND2/CDK4/6 → Rb/E2F → proliferation, plus EZH2/HDAC repression of apoptosis/differentiation and MHC-I/immune output). This logic is the same whether or not your patient's junction is sequenced, so **this track applies to the atypical case too** — arguably it is the *most* appropriate track when the molecule itself is uncertain.

### E1. Boolean network model

1. **Question:** Which single-node and combination interventions collapse the "proliferation" output node, and which trigger compensatory feedback escape?
2. **Tools (real):** **PyBoolNet** (Python) **[VERIFY]**; **BoolNet** (R) **[VERIFY]**; **GINsim** (graphical, qualitative logical models) **[VERIFY]**; **MaBoSS** (continuous-time Boolean, stochastic — gives quasi-probabilities of phenotypes) **[VERIFY]**; **CellCollective** **[VERIFY]** for community models.
3. **Input + source:** *You build the model from the docs' wiring* (docs 02/03 give the edges explicitly: CIC-DUX4 ⊣→ ETV4/5 inverted; ETV4 → CCND1/MYC; CDK4 ⊣ Rb; Rb ⊣ E2F; EZH2 ⊣ apoptosis/differentiation; BRD4 amplifies ETS super-enhancers). Cross-check edges against **SIGNOR**, **Reactome**, **OmniPath**, or **KEGG (hsa04010 MAPK)** **[VERIFY]** so the topology is literature-grounded, not invented. Node activities can be seeded from a CIC-DUX4 expression signature (Track F/G).
4. **Compute/skill:** Low–medium and **no GPU needed**. Skill: logical-modeling literacy; the hard part is justifying each rule, not running it.
5. **What it tells you / does NOT:** Tells you *qualitative* attractors (proliferative vs. arrested/apoptotic) and which perturbation sets flip the attractor — i.e., candidate combinations (e.g., BETi + CDK4/6i, or EZH2i + checkpoint-priming) that the model predicts collapse proliferation, vs. single hits that the network reroutes around. Does **NOT** give doses, kinetics, or quantitative effect sizes; Boolean = ON/OFF abstraction. Results are only as good as the hand-built wiring.
6. **CIC-DUX4 angle:** This is the literal in-silico realization of the project's "infinite loop with the break condition deleted." You can encode the deleted break (CIC repression) and then test, in silico, every combination of "re-introduce a brake" (EZH2i, BETi, CDK4/6i) and "add a watchdog" (MHC-I up → immune kill node) to find the minimal combination that the network cannot escape. **This is the single highest-leverage, lowest-barrier forward-simulation in the catalog.**

### E2. Continuous / ODE model

1. **Question:** With kinetics added, do the same combinations still win, and where are the dose/timing thresholds and feedback-escape dynamics?
2. **Tools (real):** **Tellurium / libRoadRunner** (Python, SBML) **[VERIFY]**; **PySB** (rule-based, Python) **[VERIFY]**; **COPASI** (GUI + headless, parameter scans, sensitivity) **[VERIFY]**; **BioNetGen** **[VERIFY]**.
3. **Input:** Convert the E1 topology to ODEs; parameterize from literature rate constants where available (**BioModels** repository **[VERIFY]** for reusable MAPK/cell-cycle models — e.g., existing RAS/ERK and Rb-E2F models you can adapt rather than build from scratch).
4. **Compute/skill:** Medium. CPU-only. Skill: ODE modeling, parameter sensitivity, acknowledging that most parameters are uncertain.
5. **What it tells you / does NOT:** Tells you timing/threshold behavior and feedback-escape kinetics (e.g., does ERK reactivation defeat a BETi-only intervention over time?). Does **NOT** give patient-specific predictions; parameters are borrowed and uncertain — do global sensitivity analysis and report ranges, not point predictions.
6. **CIC-DUX4 angle:** Lets you simulate *sequencing* hypotheses (the docs' "optimal sequencing hypothesis": V2 continuous → V1 → V3 priming → V4) as time-ordered perturbations and ask which order maximizes collapse of the proliferation output. Pairs naturally with the supplementary "pulsed adjunct" timing analysis already in `simulation-output/supplementary-pulsed-adjunct/`.

---

# TRACK F — TRANSCRIPTOMIC SIGNATURE REVERSAL (drug repurposing)

**Fusion-status:** Requires a CIC-DUX4 *signature* (so it leans fusion-specific), but a signature derived from fusion-confirmed lines/tumors can still be tested against an atypical case's own RNA-seq for similarity (fusion-agnostic application).

### F1. Connectivity-map signature reversal

1. **Question:** Which existing drugs/compounds produce a transcriptional signature *anti-correlated* with the CIC-DUX4 up/down signature (i.e., candidates to "reverse" the program)?
2. **Tools (real):** **CLUE.io / Connectivity Map (CMap) L1000** query interface (free account) **[VERIFY]**; the **LINCS L1000** data via **clue.io** or **GEO (GSE92742 / GSE70138** are the canonical L1000 Phase I/II accessions — **[VERIFY] these GSE IDs**); local analysis with **cmapPy** **[VERIFY]** or **signatureSearch** (Bioconductor) **[VERIFY]**; **GSEA / fgsea** **[VERIFY]** for enrichment.
3. **Input — how to get a REAL CIC-DUX4 signature (this is the crux):**
   - Search **GEO** and **ArrayExpress/BioStudies** for CIC-DUX4 RNA-seq. Candidate search terms: "CIC-DUX4", "CIC-rearranged sarcoma", "CIC DUX4 RNA-seq". **[VERIFY-EXISTENCE]** of specific accessions — I will **not invent a GSE number** for a CIC-DUX4 dataset; you must confirm what is actually deposited. (CIC-DUX4 cell-line and PDX transcriptomes have been published; the exact GSE IDs must be looked up, not asserted.)
   - Alternatively derive a signature from **DepMap/CCLE** expression (Track G) if CIC-DUX4 lines are present there.
   - Define up/down gene sets by differential expression vs. appropriate controls (ETV4/ETV5/MYC/CCND1 should be in the "up" set as a sanity check — they are the documented hallmarks).
4. **Compute/skill:** Low–medium, CPU-only. Skill: RNA-seq DE analysis (DESeq2/limma), gene-ID mapping, careful control selection.
5. **What it tells you / does NOT:** Tells you a *ranked list of compounds* predicted to oppose the CIC-DUX4 program (HDACi, BETi, CDK inhibitors plausibly surface — a built-in sanity check). Does **NOT** prove efficacy; L1000 is measured mostly in non-sarcoma cell lines (MCF7, A375, etc.), so a reversal in those lines may not transfer to CIC-DUX4 mesenchymal context. Signature reversal is hypothesis generation, not validation.
6. **CIC-DUX4 angle:** A model-free, data-driven complement to the mechanism-driven Tracks C–E: instead of guessing targets, you let the transcriptome nominate compounds. If BETi/HDACi/CDK4-6i surface unprompted, that cross-validates the docs' vulnerability map.

---

# TRACK G — DEPENDENCY MINING

**Fusion-status:** Fusion-agnostic in execution (you query a public portal), but the *value* depends on whether CIC-DUX4 / Ewing-like lines exist in the resource.

### G1. DepMap genetic-dependency mining

1. **Question:** What genes are selectively essential (CRISPR/RNAi) in CIC-DUX4 / Ewing-like cell lines — i.e., what does the fusion make the cell addicted to?
2. **Tools (real):** **DepMap portal** (depmap.org) — CRISPR (**Chronos/CERES** scores from the **Achilles/Project Score** screens), RNAi (**DEMETER2**), and **CCLE/Expression** **[VERIFY]**. Programmatic access via the DepMap data downloads + Python (pandas).
3. **Input + the honest existence check:**
   - **First action:** on depmap.org, search the cell-line list for CIC-DUX4 sarcoma lines. **Candidate line names to look for: IB120, Kitra-SRS, NCC-CDS-X-series, and the "CIC-DUX4" / "CIC-rearranged" lineage tag.** **[VERIFY-EXISTENCE]** — I am **not certain** these specific lines are in DepMap; some published CIC-DUX4 lines (e.g., Kitra-SRS, IB120) exist in the *literature*, but DepMap coverage of this ultra-rare entity may be **zero or near-zero**. Confirm directly; if absent, fall back to **Ewing sarcoma lines** (well-represented: A673, SK-N-MC, TC71, etc. **[VERIFY]**) as the closest fusion-driven proxy, and state the transfer caveat.
4. **Compute/skill:** Low. Point-and-click portal, or pandas on the downloaded matrices. No GPU.
5. **What it tells you / does NOT:** Tells you candidate dependencies (BRD4, CDK4/6, EZH2, and possibly fusion-specific co-dependencies) ranked by selectivity. Does **NOT** apply directly if no CIC-DUX4 line exists in DepMap — Ewing is a *proxy*, not the same disease (docs note CIC-DUX4 is more aggressive, more CDKN2A-co-deleted, less chemosensitive). 
6. **CIC-DUX4 angle:** The fastest empirical reality-check on the docs' vulnerability table. If CIC-DUX4 lines are absent from DepMap, that *gap itself* is a finding worth reporting upstream.

### G2. cBioPortal genomics mining

1. **Question:** What co-occurring alterations (e.g., CDKN2A deletion) and clinical correlates exist in CIC-rearranged sarcoma cohorts?
2. **Tools (real):** **cBioPortal** (cbioportal.org) **[VERIFY]**; programmatic via the cBioPortal web API or **cBioPortalData** (Bioconductor) **[VERIFY]**.
3. **Input:** Search cBioPortal for CIC / sarcoma studies. **[VERIFY-EXISTENCE]** of a dedicated CIC-rearranged sarcoma study; given rarity, you may only find CIC alterations within pan-sarcoma or pan-cancer cohorts (e.g., MSK-IMPACT, TCGA-SARC **[VERIFY]**). Do not assume a large dedicated cohort exists.
4. **Compute/skill:** Low.
5. **What it tells you / does NOT:** Tells you mutation co-occurrence patterns (CDKN2A status is the docs' flagged co-event). Does **NOT** give functional dependency (that's DepMap) and small-n cohorts limit statistics.
6. **CIC-DUX4 angle:** Confirms/contextualizes the CDKN2A-deletion co-occurrence the docs flag, which is itself a CDK4/6-inhibitor rationale (loss of p16 → unopposed CDK4/6).

---

# TRACK H — PK / EXPOSURE MODELING (turn "concentration mismatch" into a number)

**Fusion-status: fully fusion-agnostic** — this is pharmacokinetics of the *compound*, independent of the patient's molecular subtype. Applies to typical and atypical cases identically.

### H1. Simple compartmental PK to quantify the plasma-vs-IC50 gap

1. **Question:** For each dietary compound, what peak/steady-state plasma concentration is realistically achievable, and how far below the in-vitro IC50 (from the cell-line studies) does it sit?
2. **Tools (real):** Plain **Python + SciPy** (`scipy.integrate.odeint`/`solve_ivp`) for a 1- or 2-compartment oral-absorption model; **PK-Sim / OSP Suite** (open-source PBPK) **[VERIFY]** if you want full physiological modeling; **mrgsolve** or **nlmixr2** (R) **[VERIFY]** as alternatives.
3. **Input — where the numbers come from:** Published human PK parameters (Cmax, Tmax, t½, oral bioavailability F) for EGCG, curcumin, quercetin, resveratrol from pharmacokinetic papers. **Do NOT invent these constants** — pull them from cited human PK studies (and note the docs' warning: curcumin/EGCG/quercetin oral bioavailability is poor and plasma is often 10–1000× below cell-line concentrations; for curcumin+piperine, the Shoba 1998 "~2000%" figure is n=10, single-dose, control-below-LOD and must not be used as a universal multiplier). IC50 values come from the cell-line studies you cite — with their assay system stated.
4. **Compute/skill:** Low. A few dozen lines of Python; no GPU. This is the most accessible quantitative experiment in the catalog.
5. **What it tells you / does NOT:** Produces a concrete number — e.g., "achievable plasma EGCG ≈ 0.1–0.5 µM vs. BRD4-relevant cell-line IC50 ≈ 10–50 µM → a ~20–500× gap." Does **NOT** account for tissue accumulation, active metabolites (polyphenols are heavily metabolized — the metabolites, not the parent, reach tissue), or intratumoral concentration. So the gap it reports is a *first-order* estimate; flag that metabolites could change the picture in either direction.
6. **CIC-DUX4 angle:** This converts the contract's mandatory "concentration-mismatch" caveat from a qualitative warning into a per-compound number the user can compute and put next to every Track-C docking hit. It is the quantitative backbone that keeps the dietary-compound hypotheses honest.

> **Chemo-interaction note (contract-required):** Several compounds modeled in Track H (curcumin, EGCG, quercetin) have documented CYP3A4/CYP2C9/P-gp interactions, and high-dose antioxidants (NAC, vitamin C/E) may interfere with ROS-dependent chemotherapeutics (doxorubicin, ifosfamide) in the CIC-rearranged SOC backbone (VDC/IE). A PK model that ignores drug–drug interaction underestimates risk. Any in-silico PK result that informs a real decision must be reviewed against the SOC regimen by the patient's oncologist (see `/sarcoma-chemo-interactions`).

---

# Suggested starting sequence (highest leverage, lowest barrier — bias to no-wet-lab)

Run these **three first**; together they generate the most forward hypotheses for the least compute and the least uncertainty, and **none requires the confirmed junction** (so all three apply to the atypical case):

1. **Track G1 — DepMap dependency mining (start here, today).** Point-and-click, no GPU, immediately tells you whether the field's empirical dependency data even covers this disease. First sub-task is a 5-minute existence check ("is any CIC-DUX4 line in DepMap?"). Highest signal-to-effort ratio; also reality-checks the docs' vulnerability table.
2. **Track F1 — LINCS L1000 signature reversal.** Model-free drug nomination; CPU-only; built-in sanity check (BETi/HDACi/CDK4-6i should surface). The main work is obtaining a *real* CIC-DUX4 signature from GEO — which you should verify exists before committing.
3. **Track E1 — Boolean network model of the loop.** No GPU, no external data dependency, and it is the literal in-silico version of the project's "infinite loop / deleted break condition." It is the only track that lets you run *endless combination what-ifs* and find the minimal multi-node perturbation the network cannot escape — directly serving the simulation's "no single vector is sufficient" hypothesis. Promote to Track E2 (ODE, via BioModels-sourced kinetics) once the Boolean attractors are characterized.

Structure/docking/MD (Tracks A–D) are higher-barrier and lower-confidence for *this* problem (no confirmed junction, flat protein–DNA interface, dietary concentration gaps) — valuable, but second-wave. Track H (PK) is cheap and should be run *alongside* any Track-C docking work to keep it honest.

---

# What in-silico CANNOT tell you (honesty section)

- **Whether anything works in a patient.** Every output above is a *hypothesis generator*. None is evidence of clinical benefit. Docking scores ≠ Kd; Boolean attractors ≠ tumor response; signature reversal ≠ efficacy; pLDDT ≠ stability or activity.
- **Your patient's actual fusion junction.** No simulation can recover an unconfirmed junction. Tracks that need it (C3 fusion:DNA screen, any junction-specific design) are inapplicable to the ~5% fusion-unconfirmed atypical case except in the architecture-enumeration sense (A2).
- **In-cell condensate behavior.** LLPS predictors (Track B) are trained on a small, biased set of known phase-separating proteins; a "LLPS-prone" score on CIC-DUX4 is a lead, not a demonstration. The contract docs explicitly note condensate biology is *less established* for CIC-DUX4 than for EWSR1 fusions.
- **Absolute binding affinities.** Even FEP (the most rigorous tool here) gives *relative* ΔΔG within a model, not a measured Kd; force-field and sampling errors are real.
- **Whether a dietary compound reaches the tumor.** PK modeling (Track H) estimates plasma exposure but cannot resolve intratumoral concentration, active-metabolite contribution, or tissue accumulation — all of which can move the answer.
- **Causation vs. correlation in omics mining.** DepMap selectivity and cBioPortal co-occurrence are associative; they nominate dependencies, they do not prove the fusion *causes* them.
- **Anything about safety, dosing, or drug interactions in a human.** Out of scope by contract; the SOC-interaction flag above is a reason to involve an oncologist, not a substitute for one.

---

## What I Could Not Establish

- **Live verification of any URL, tool name, database, accession, PDB ID, GSE ID, CID, or cell-line ID.** This environment blocked WebSearch, WebFetch, and outbound HTTP (curl). Per the contract, I therefore flagged every such item **[VERIFY]** / **[VERIFY-EXISTENCE]** and declined to assert IDs I could not confirm (notably: I gave **no** PDB ID for an EZH2 or CDK6 structure, and **no** GSE number for a CIC-DUX4 dataset, because asserting one unverified would be fabrication). **PDB 3MXF is named because it is the ID I associate with BRD4-BD1+JQ1-series from training, but it is explicitly unconfirmed here — confirm on rcsb.org before use.**
- **Whether any CIC-DUX4 cell line is actually present in DepMap/CCLE.** Given the disease's rarity (hundreds of cases worldwide), coverage may be zero. This is itself a key finding to confirm first (Track G1).
- **Whether a deposited CIC-DUX4 transcriptomic signature exists in GEO/CMap-compatible form.** Track F's value hinges on this; verify before building the pipeline.
- **The exact reported CIC and DUX4 breakpoints/exon boundaries** for constructing fusion candidates (Track A2) — the literature describes variable junctions; confirm specific exon numbers before trusting any single construct.
- **Current access terms** for the AlphaFold3 server and CLUE.io for the user's intended (personal/research) use.

---

## Forward Hypotheses

**[Forward Hypothesis 1] — CIC-DUX4 forms transcriptional condensates driven by the DUX4 acidic transactivation IDR, and this propensity is invariant across junction variants.**
- *Mechanistic basis:* The DUX4 C-terminal transactivation domain is acidic and predicted-disordered (Track A3); acidic IDRs are a documented LLPS driver class. Because every CIC-DUX4 junction retains the DUX4 C-terminus, the LLPS-driving element should be present regardless of the CIC breakpoint — making condensate formation a *junction-robust* property and therefore a target that does not require knowing the patient's exact junction.
- *In-silico test:* Score all constructed junction variants (A2) with FuzDrop/catGRANULE2.0/PScore/PLAAC (B1) and run CALVADOS/Mpipi CG slab simulations (B2) on the shared DUX4 IDR; benchmark head-to-head against an identically-run EWS-FLI1 IDR. Invariance across variants + EWS-FLI1-comparable phase behavior would support the hypothesis.
- *Why not yet tested:* CIC-DUX4 is rare and the field's condensate work has concentrated on EWSR1 fusions; an in-silico-first comparison is cheap and apparently under-explored.

**[Forward Hypothesis 2] — A minimal two-node perturbation (BRD4 super-enhancer throttle + CDK4/6 brake) collapses the proliferation attractor that single-node perturbations cannot, because the network reroutes single hits via ERK-driven CIC-de-repression feedback.**
- *Mechanistic basis:* The docs describe a loop with multiple parallel reinforcement arms (BRD4 amplification, ETV-driven CCND1/MYC, EZH2-silenced apoptosis). A single brake should be escapable by the others; the "no single vector is sufficient" thesis predicts a small combination is needed.
- *In-silico test:* Build the Boolean model (E1), enumerate all 1- and 2-node perturbations, and identify the minimal set that drives every initial state to the arrested/apoptotic attractor with no escape; confirm timing/threshold robustness in the ODE version (E2). Then check whether L1000 signature reversal (F1) independently nominates the same pair of mechanisms — convergence of a mechanism-driven and a data-driven method would be strong (in-silico) support.
- *Why not yet tested:* No published Boolean/ODE model specific to the CIC-DUX4 wiring (as opposed to generic RAS/ERK or Rb-E2F models) appears to exist; assembling one from the documented edges is a tractable, novel contribution.

**[Forward Hypothesis 3] — The DepMap dependency profile of CIC-DUX4 (if any line exists) diverges from Ewing on the EZH2/PRC2 axis due to the docs' flagged frequent CDKN2A co-deletion, predicting EZH2i sensitivity is *not* simply transferable from Ewing.**
- *Mechanistic basis:* CDKN2A loss (p16) reshapes both the CDK4/6 dependency and, via altered chromatin context, potentially the PRC2 dependency. Treating Ewing as a perfect proxy (the fallback when CIC-DUX4 lines are absent) may mis-predict the EZH2 axis specifically.
- *In-silico test:* In DepMap (G1), compare EZH2/EED/SUZ12 and CDK4/CDK6 dependency scores between Ewing lines stratified by CDKN2A status; in cBioPortal (G2) quantify CDKN2A co-deletion frequency in CIC cohorts. A CDKN2A-status-dependent EZH2 dependency would flag the transfer caveat quantitatively.
- *Why not yet tested:* Requires deliberately stratifying a proxy disease by a co-mutation to model a rarer one — an analysis that is straightforward but not obviously motivated unless you are specifically reasoning about CIC-DUX4, as here.
