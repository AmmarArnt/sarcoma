# Hypothesis Steering & Adversarial Reasoning (the reasoning-process layer)

**In response to GitHub issue #32** — *"Human-Guided Hypothesis Steering and Clinical Reasoning Loops"*
(@Cerimagic).

**Status:** framework methodology doc / [ADR-0017](adr/0017-hypothesis-steering-adversarial-reasoning.md).
This is a **process** layer — it governs *how* the multi-agent framework explores and prunes the
hypothesis space, not *what* biology it considers. It is **not a fifth attack vector** (golden rule #8) and
**not a biological analytical layer** like host-biology or VoI (it does not feed a catalog section with new
mechanisms). Research-simulation note, **not medical advice**.

**Confidence: medium.** The clinical cognitive-debiasing component is grounded in a real, well-cited
literature; the claim that *structured* adversarial reasoning improves *this framework's* hypothesis quality
is **mechanistic/theoretical** (we cannot run the controlled comparison here — see §6). **Evidence tier of
this layer:** `Mechanistic` for the framework claims; the supporting human-factors citations are
`Established` in their own domain (clinical decision-making), transferred here at reduced confidence.

> **See also:** the framework's existing debiasing surfaces — golden rule #5 (the *two-lane* forward rule)
> in [`CLAUDE.md`](../CLAUDE.md) §1; the orchestrator's **RESOLVE CONFLICTS** step
> ([`sarcoma-orchestrator-intake`](../.claude/skills/sarcoma-orchestrator-intake/SKILL.md) §4); the
> [`sarcoma-pre-output-check`](../.claude/skills/sarcoma-pre-output-check/SKILL.md) self-audit; the
> driver-uncertainty *alternative-hypothesis* model ([ADR-0008](adr/0008-driver-uncertainty-decision-model.md));
> and the counterfactual trial forensics in `simulation-output/forward-simulation/`.

---

## 1. The question, restated

The issue observes that expert clinical reasoning is **not** a single linear pass. Experts iteratively
expand and narrow the hypothesis space through directed questioning, alternative-hypothesis generation,
red-team challenges, counterfactuals, and explicit attempts to *disprove* a favored explanation. Because
LLMs and autonomous agents are highly sensitive to how the search space is framed, the issue asks:

> **Can human-guided steering improve the quality of generated hypotheses compared with purely autonomous
> exploration?** — and proposes mechanisms for clinician-in-the-loop steering, adversarial hypothesis
> testing, diagnostic debiasing workflows, structured challenge-response cycles, and dynamic
> expansion/contraction of the search space.

**Short answer (three parts):**

1. **Yes, with grounding.** Human-guided steering and *structured* adversarial testing are the standard
   counter-measures to the cognitive failure modes that affect both clinicians and autonomous reasoners
   (anchoring, confirmation bias, premature closure). This is `Established` in the clinical
   decision-making literature (Croskerry's dual-process / cognitive-debiasing work) and has a direct
   machine analogue in LLM self-verification methods (Chain-of-Verification). See §5.
2. **The framework already embodies most of the proposed mechanisms** — but *implicitly and unevenly*. The
   multi-agent team structure, golden rule #5, the orchestrator's conflict-resolution step, the
   pre-output self-audit, and the driver-uncertainty model each implement a piece of it (§2). The gap the
   issue correctly identifies is that there is **no single, explicit, named protocol** for it, and **no
   standing red-team step**.
3. **So this doc names the protocol** (§4): a lightweight **Red-Team / Challenge-Response pass**, a
   short **debiasing checklist** targeted at *this project's* specific biases (§3), explicit
   **search-space expansion/contraction** rules, and a map of the **clinician-in-the-loop channels** that
   already exist (the GitHub issue thread; `AskUserQuestion`). It is deliberately small — a forcing
   function, not a new bureaucracy.

---

## 2. The framework already implements most of this — implicitly

The issue lists five mechanisms. Each already has a partial home in the framework. Naming the mapping
matters: it prevents us from "inventing" machinery that exists, and it shows precisely where the gaps are.

| Issue's proposed mechanism | Where it already lives | Gap this doc closes |
|---|---|---|
| **Clinician-in-the-loop steering** | The **GitHub Issues workflow** ([`github-issue-runner`](../.claude/skills/github-issue-runner/SKILL.md), ADR-0002) *is* the human-steering channel — every analytical layer (ADR-0001…0016) was steered into existence by a human-posted issue. In-session, `AskUserQuestion` is the steering primitive. | Make it explicit that issues + `AskUserQuestion` are the sanctioned steering interface, and that a steering input may **widen** as well as narrow scope. |
| **Adversarial hypothesis testing** | Golden rule #5 ("known research is the FLOOR not the ceiling — ask *why* it failed"); the orchestrator's **RESOLVE CONFLICTS** step (§4 — "surface the conflict explicitly, do not paper over it"); the feasibility **attrition-reason** annotation (ADR-0013 — "discontinued ≠ biologically invalidated"). | A **standing red-team pass** an agent runs against its *own* leading hypothesis before writing, not only the orchestrator reconciling *across* agents. |
| **Diagnostic debiasing workflows** | `sarcoma-pre-output-check` (9 failure modes) is already a debiasing checklist — but it targets *citation/evidence* hygiene, not *reasoning* bias. The confidence axis (docs/08) and transferability ladder (docs/10) debias over-weighting of weak/transferred evidence. | Add the *reasoning*-bias half (anchoring, confirmation, premature closure) — §3. |
| **Structured challenge-response cycles** | The **two-lane rule** (confirmatory lane vs Forward-Hypotheses lane) forces a generative counter-move to every pruning move. The driver-uncertainty model (ADR-0008) is a formal challenge: "what if the favored driver is wrong?" — it marginalizes over alternatives. | Generalize the challenge from the driver question to *any* high-leverage hypothesis (§4 step 3). |
| **Dynamic expansion/contraction of the search space** | The **wave architecture** is literally expand-then-contract: parallel specialists *expand* (V1–V4 sub-agents fan out), each lead *contracts* (reconciles, merges duplicates, keeps strongest tier), the orchestrator contracts again. Spawning a *supplementary team* is a deliberate expansion (ADR-0007). | Name the **triggers** for re-expanding a prematurely-narrowed space (§4 step 4). |

**Conclusion:** the issue is not asking for something foreign to the framework — it is asking us to make a
diffuse, implicit capability **explicit, named, and consistently applied.** That is what §3–§4 do.

---

## 3. The biases that specifically threaten *this* framework

Generic debias-everything advice is low-value. These are the failure modes most likely *here*, each with
the counter-measure (existing or added). The biases are named from Croskerry's taxonomy
(PMID 23882089); the application to this project is ours.

| Bias | How it shows up in *this* framework | Counter-measure |
|---|---|---|
| **Anchoring** | The **four fixed vectors** (golden rule #8) are a deliberate, useful anchor — but they can crowd out a mechanism that fits none of them. Issue #33 (modality expansion) is exactly this risk surfacing. | Vectors stay fixed, but the **supplementary-team escape hatch** (ADR-0007) and the Forward-Hypotheses lane exist precisely to hold what the vectors anchor out. Red-team prompt: *"what real mechanism fits none of V1–V4?"* |
| **Confirmation bias** | Over-weighting a compound because it is "promising" / appears in many vectors, while under-searching for the disconfirming trial. | The **attrition-reason** annotation (ADR-0013) forces the disconfirming question; the orchestrator's failure-mode scan (#3 cancer-class generalization, #8 padding) catches enthusiasm-driven inclusion. |
| **Premature closure** | Converging on the headline catalog (`protocol-v2.md`) and treating it as settled; not re-opening when a new layer should perturb the ranking. | ADR-0016 (full-cycle layer ingestion) + `findings-ranking.md` maintenance rule force re-reconciliation. Red-team prompt: *"which top-5 finding would flip if the single most uncertain input were wrong?"* |
| **Base-rate neglect / rarity blindness** | In a rare tumor, transferring a solid-tumour result as if it were CIC-DUX4 evidence. | The **transferability ladder** (docs/10, ADR-0014): rarity lowers the Directness rung (confidence), never excludes — but the rung must be *stated*. |
| **Availability bias** | Recency/volume of a literature making a well-published target feel more supported than a sparse-but-direct one. | RANK criterion (b): mechanistic alignment with CIC-DUX4 *specifically* outranks generic-cancer evidence volume. |
| **Sycophancy (the LLM-specific one)** | An agent agreeing with the steer's implied preferred answer, or with a confident-sounding upstream sub-agent, rather than testing it. | The red-team pass (§4) is run **against the steer too**: a human steer reframes the search; it does not get to *assert a biological conclusion* unchallenged. Steering inputs are treated as `Theoretical` until grounded. |

---

## 4. The protocol (small, explicit, a forcing function)

Four steps. Steps 1–2 are standing (every substantive analytical output); steps 3–4 are triggered.

### Step 1 — Name the leading hypothesis and its single most load-bearing assumption
Before writing, state the one claim the output most depends on, and the one input whose being-wrong would
most change the conclusion. (This is the diagnostic analogue of "what's my working diagnosis and what would
change it.") One sentence; it lives in the existing "What I Could Not Establish" section.

### Step 2 — Run a one-pass red-team against your *own* leading hypothesis
A short, mandatory self-challenge appended to `sarcoma-pre-output-check`. Ask and answer, briefly:
- **Disconfirmation:** what is the strongest *published* evidence *against* this, and did I search for it
  as hard as for the supporting evidence? (counters confirmation bias)
- **Alternative:** what is the best hypothesis that fits the same data but sits *outside* my vector/lane?
  (counters anchoring)
- **Flip test:** if my single load-bearing assumption (step 1) is wrong, does the conclusion survive? If
  not, the entry is **driver-/assumption-contingent** and must be tagged so (as ADR-0008 tags the
  fusion-contingent entries).
- **Steer audit:** if a human steer pointed me here, am I confirming it or testing it? A steer reframes;
  it does not supply a tier. (counters sycophancy)

This mirrors **Chain-of-Verification** (arXiv:2309.11495): draft → generate verification questions →
answer them independently → revise. It is the machine form of Croskerry's "forcing function" (PMID 23996094).

### Step 3 — Structured challenge-response on high-leverage hypotheses (triggered)
When a finding is both **high-leverage** (would change the top-tier ranking or a clinician-facing brief)
**and** rests on a contestable assumption, run an explicit challenge-response: state the challenge, attempt
to answer it from real sources, and record the residual uncertainty. The **driver-uncertainty model**
(ADR-0008) is the worked template — generalize its "treat the driver as a latent variable, marginalize,
compute the value of resolving it" pattern to the contestable assumption at hand.

### Step 4 — Dynamic search-space expansion/contraction (triggered)
The wave architecture contracts by default. **Re-expand** when any trigger fires:
- a red-team **Alternative** (step 2) names a real mechanism that fits no current vector/team → propose a
  **supplementary team** (ADR-0007 pattern; consent required, golden rule §2/§3);
- a human steer **widens** scope (e.g. issue #33's modality expansion) → expansion is the correct response,
  not forcing the ask into the existing taxonomy;
- a new standing layer perturbs the ranking (ADR-0016) → re-reconcile rather than defend the prior catalog.

**Contract** (the default) by the existing rules: leads merge duplicates and keep the strongest tier; the
orchestrator dedupes and ranks. **The load-bearing guardrail:** contraction prunes the *confirmatory* lane
only — it **never prunes the Forward-Hypotheses lane** (golden rule #5). Expansion and contraction are the
two-lane rule in motion.

### The clinician-in-the-loop channels (no new machinery)
- **Asynchronous / between-runs:** the **GitHub issue thread** — the sanctioned steering interface
  (ADR-0002). A `needs attention` follow-up (ADR-0010) is a steer on an already-answered question.
- **In-session:** **`AskUserQuestion`** — use it when a steer is ambiguous, when a red-team Alternative
  needs a scope decision, or before spawning a new team (consent). A steer may legitimately *widen* the
  space; do not collapse it to the nearest existing artifact.

---

## 5. Evidence and honest limits

**Grounded (Established, in their own domains):**
- **Croskerry P. Cognitive debiasing 1: origins of bias and theory of debiasing.** *BMJ Qual Saf* 2013;22
  (Suppl 2):ii58–ii64. PMID **23882089**, doi:10.1136/bmjqs-2012-001712. (Dual-process theory of diagnostic
  reasoning; the bias taxonomy in §3.)
- **Croskerry P. Cognitive debiasing 2: impediments to and strategies for change.** *BMJ Qual Saf* 2013;22
  (Suppl 2):ii65–ii72. PMID **23996094**, doi:10.1136/bmjqs-2012-001713. (Forcing functions, cognitive
  forcing strategies; the "make the checklist a forcing function" rationale in §4.)
- **Dhuliawala S, et al. Chain-of-Verification Reduces Hallucination in Large Language Models.**
  arXiv:**2309.11495**; ACL Findings 2024. (The machine analogue of step 2 — self-generated verification
  questions answered independently of the draft.)

**What I could not establish:**
- **No CIC-DUX4-specific evidence**, and none possible — this is a reasoning-process question, not a
  biology question. Evidence-in-CIC-DUX4: `None — N/A`.
- **No controlled comparison within this framework.** I cannot show, here, that steered + red-teamed runs
  produce measurably *better* CIC-DUX4 hypotheses than autonomous runs — that would require a held-out
  evaluation with a quality metric and blinded scoring, which the repo's real-data-only sim rule and the
  absence of a ground-truth hypothesis-quality label both preclude. The claim in §1.1 is therefore
  `Mechanistic`, by transfer from the clinical and LLM literatures, **not** an in-repo measurement.
- **Transfer-distance caveat (per docs/10).** Croskerry's evidence is in *human* clinical diagnosis;
  CoVe is in *generic* LLM factuality. Applying them to *multi-agent biological hypothesis generation* is a
  P3–P4 transfer (pathway/analogy-level) — admitted at reduced confidence, not excluded.
- **Cost/over-correction risk.** A red-team pass on every output adds tokens and can induce
  *over-hedging* (rejecting a sound hypothesis because a weak counter-argument exists). Mitigated by
  keeping step 2 to one pass and reserving steps 3–4 for high-leverage / triggered cases. Whether the net
  effect is positive is itself unmeasured here.

---

## 6. Direct answer to the guiding question

**Can human-guided steering improve the quality of generated hypotheses compared with purely autonomous
exploration?** — **Yes, on mechanistic and transferred-empirical grounds, with three honest qualifiers:**

1. **The mechanism is the standard debiasing one.** Steering and structured adversarial testing counter
   anchoring, confirmation bias, and premature closure — the documented failure modes of both human
   diagnosticians (Croskerry) and autonomous LLM reasoners (CoVe). The framework already gets much of this
   from its multi-agent structure and golden rule #5; the value added here is making the red-team step
   **explicit and standing** rather than emergent.
2. **Steering helps most by *widening*, not just narrowing.** The largest demonstrated wins in this repo —
   every issue-driven analytical layer — came from a human steer that *expanded* the search space the
   autonomous run had implicitly closed (host biology, diagnostics, modality). Premature convergence is the
   real enemy (§3), and human steering is the most effective counter to it.
3. **But steering can also *harm* — via sycophancy.** A steer that smuggles in a preferred conclusion can
   make an agreeable agent *worse*. Hence the rule that a steer reframes the search but does not supply an
   evidence tier (§3, §4 step 2). Human-in-the-loop is a net positive **when the loop is adversarial, not
   confirmatory.**

So: not "autonomous vs human-guided," but **autonomous exploration *plus* an explicit adversarial,
expansion-capable human loop** — which is what the GitHub-issue workflow already is, now with a named
protocol behind it.

---

## 7. Forward hypotheses

- **[Forward Hypothesis] A "red-team delta" is measurable.** *Hypothesis:* running step 2 changes the
  output (tier downgrades, added contingency tags, new alternatives) at a non-trivial rate. *Test:* on the
  next full re-run, log per-output red-team outcomes and count entries changed; a near-zero rate means the
  pass is theatre, a high rate means it is load-bearing. *Why not yet done:* the pass did not exist before
  this doc. This is the cheapest empirical check of whether the protocol earns its token cost.
- **[Forward Hypothesis] Adversarial steering > neutral steering for forward-hypothesis yield.** *Hypothesis:*
  issues phrased as red-team challenges ("disprove X", "what fits none of V1–V4") generate more, and more
  defensible, Forward Hypotheses than open prompts. *Test:* compare Forward-Hypothesis sections produced
  under challenge-framed vs open-framed issues, scored on falsifiability + mechanistic specificity. *Why
  not yet done:* requires a small labelled set of past issues by framing type.
- **[Forward Hypothesis] Sycophancy is detectable via the steer-audit.** *Hypothesis:* outputs where the
  conclusion matches the steer's implied preference *and* the disconfirmation search is thin are the
  highest-risk entries. *Test:* flag such outputs and have the orchestrator re-challenge them; measure how
  often the re-challenge changes the entry. *Why not yet done:* needs the steer-audit field (§4 step 2) to
  be captured in outputs first.

---

*This is a research-simulation methodology note, not medical advice. It changes how the framework reasons,
not what any patient should do.*
