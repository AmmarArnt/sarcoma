# Tumor Inception-to-Diagnosis Timeline — Back-Extrapolation from Size at Presentation

**Type:** Case-anchored growth-kinetics estimate (Tier 2 analytical layer). **Date:** 2026-07-17.
**Status of the numbers:** `Theoretical` / `Mechanistic` extrapolation — **not** a measured or clinical
determination. **Not medical advice.** This estimates *how long the tumor may have been growing*, not
anything actionable about treatment.

---

## The question

> Patient first diagnosed **June 2024**. At diagnosis: primary tumor **~10 cm diameter**, plus
> **12 lung metastatic nodules**. How far back could the tumor have been triggered (incepted) and begun
> to grow?

This is a tumor-growth back-extrapolation problem. The honest answer is a **band, not a date** — and the
band is wide because (a) CIC-DUX4 sarcoma has **no published volume-doubling-time (VDT) series** (it is
ultra-rare), so the growth rate must be borrowed from proxy entities, and (b) real tumors grow
**Gompertzian** (fast when small, slowing as they enlarge), which breaks naïve single-rate extrapolation.

**Headline estimate:** the primary lesion most plausibly began its clonal outgrowth **~1.5–4 years before
diagnosis — i.e. roughly 2020–2022, best point estimate late-2021 to 2022** — with a defensible outer
range of ~1 year (if growth was very fast) to ~5 years. The *initiating molecular event* (the fusion-
creating translocation) may predate that clonal-outgrowth clock by an unknowable additional interval (see
caveat 4). The already-established lung metastases independently argue **against** a very recent (<1 year)
inception.

---

## Step 1 — Size → number of cell doublings

Standard clinical approximations (`Established` biophysics): tumor tissue density ≈ 1 g/cm³ and
≈ **10⁹ cells per cm³ (per gram)**. Volume of a sphere = (4/3)πr³.

| Landmark | Diameter | Volume | Cell count | Doublings from 1 cell (log₂) |
|---|---|---|---|---|
| Single transformed cell | ~10–20 µm | — | 1 | 0 |
| CT-detectable lung nodule | ~5 mm | 0.065 cm³ | ~6.5 × 10⁷ | ~26 |
| "Detection threshold" nodule | ~10 mm | 0.52 cm³ | ~5 × 10⁸ | ~29 |
| **Primary at diagnosis** | **~100 mm** | **524 cm³** | **~5 × 10¹¹** | **~39** |

So the 10 cm primary represents roughly **39–40 doublings** from a single fully-transformed cell.
Crucially, ~30 of those doublings occur while the tumor is still **microscopic/occult** (1 cell → ~1 cm),
and only the **last ~10 doublings** (1 cm → 10 cm) occur in the clinically detectable range.

## Step 2 — How long is a doubling? (the weakest link)

There is **no CIC-DUX4-specific VDT in the literature** — the entity is too rare for a serial-imaging
series. What we can say (`Mechanistic` / transfer-distance P1–P2 under ADR-0014):

- CIC-DUX4 sarcoma is characteristically **highly proliferative** — a high Ki-67 / mitotic index is a
  described feature (docs/02), consistent with a **short** VDT.
- **Proxy VDTs** from aggressive high-grade and round-cell sarcoma pulmonary metastases fall roughly in
  the **~20–70-day** range, with the most aggressive round-cell/Ewing-family lesions toward **~20–40
  days**. Given CIC-DUX4's reputation as *more* aggressive than Ewing, a central VDT band of
  **~20–40 days** is defensible, with an outer envelope of ~15–60 days.

**This borrowing is the dominant source of uncertainty.** Tag it `Theoretical`; do not present the
resulting date as fact.

## Step 3 — Naïve constant-rate back-extrapolation

39 doublings × VDT:

| VDT assumption | Time to reach 10 cm | ≈ Inception (before June 2024) |
|---|---|---|
| 15 d (very fast) | ~585 d | ~1.6 y → early 2023 |
| 20 d | ~780 d | ~2.1 y → mid-2022 |
| **30 d (central)** | **~1170 d** | **~3.2 y → early 2021** |
| 40 d | ~1560 d | ~4.3 y → early 2020 |
| 60 d (slow) | ~2340 d | ~6.4 y → early 2018 |

Constant-rate central tendency: **~2–4 years.**

## Step 4 — Gompertzian correction (pulls the estimate *in*)

Constant-VDT extrapolation is biased. Real solid tumors grow **Gompertzian**: near-exponential and *fast*
while small and well-perfused, then progressively **slowing** as hypoxia, necrosis and cell loss set in
(a 10 cm round-cell sarcoma is typically necrosis-prone — high cell loss). Consequences:

- The **measured/observed VDT is from the late, slowed phase.** The earlier ~30 occult doublings almost
  certainly ran *faster* than that. So applying a late-phase VDT to *all* 39 doublings **over**estimates
  the true age.
- Net effect: the realistic estimate sits at the **lower half** of the Step-3 band. This is why the
  headline lands at **~1.5–4 years (best point ~2021–2022)** rather than the 3–4-year midpoint a purely
  linear read would give.

## Step 5 — The metastases as an independent clock (rules out "very recent")

Twelve **discrete, countable** lung nodules at diagnosis is informative. The metastatic cascade requires,
in sequence: the primary reaching **angiogenic/invasive competence** (usually already ≥~1–2 cm, i.e. past
the halfway point of its doublings) → intravasation → survival in circulation → extravasation →
colonization → outgrowth of each seed from 1 cell to CT-visible (~5 mm ≈ **~26 doublings**).

At a lung-met VDT of ~30 days, growing a single extravasated cell to a 5 mm nodule is itself ~26 × 30 ≈
**~2 years** — and seeding cannot precede the primary's angiogenic switch. Even allowing that mets seed
from an already-sizable primary and that some seeds arrive as small clusters (shortening their visible-
outgrowth time), the presence of **12 established** nodules implies seeding occurred **many months to
~1–2 years before diagnosis**, which in turn requires the primary to have **already existed and been
vascularized** before that. This corroborates a primary age of **at least ~1.5–3 years** and makes a
**<1-year** inception biologically implausible for this presentation.

---

## Synthesis

| Interpretation of "inception" | Estimated interval before June-2024 diagnosis |
|---|---|
| Onset of **successful clonal outgrowth** (single transformed cell begins the expansion that became the 10 cm mass) | **~1.5–4 years** (best point ~2021–2022); outer envelope ~1–5 y |
| **Angiogenic switch / metastatic-seeding competence** of the primary | likely **~1–2.5 years** before diagnosis (mets already visible ⇒ seeded well before Dx) |
| **Initiating molecular event** (the fusion-creating translocation itself) | ≥ the clonal-outgrowth interval, plus an **unknowable** occult/immune-equilibrium lead time (caveat 4) — cannot be dated |

**Bottom line:** the growth kinetics point to a tumor that began measurable clonal expansion on the order
of **a couple of years — roughly 2 to 3 years, plausibly anywhere from ~1.5 to ~4 years — before the June
2024 diagnosis** (i.e. **~2021–2022**). The founding translocation could be older still. A brand-new
(months-old) origin is not compatible with a 10 cm primary already accompanied by a dozen grown-out lung
metastases.

---

## What I could **not** establish (golden rule #4)

1. **No CIC-DUX4 VDT exists.** Every day-count here rides on a VDT borrowed from Ewing/round-cell/high-
   grade-sarcoma proxies (`Theoretical`; transfer-distance P1–P2). A patient-specific VDT (two dated
   scans) would collapse most of the uncertainty and is the single highest-value missing input.
2. **No serial imaging for this patient** (only the June-2024 snapshot). Everything is single-time-point
   back-extrapolation; the width of the band cannot be narrowed from the data given.
3. **Gompertzian parameters are assumed, not fit.** The magnitude of the early-fast/late-slow correction
   (Step 4) is directional and defensible but not quantified for this entity — it justifies "lower half of
   the band," not a precise shrinkage.
4. **The initiation ≠ outgrowth gap is unmeasurable.** A driver clone can sit in immune **elimination/
   equilibrium** (Schreiber/Dunn immunoediting) for an unknown period before escaping and expanding. That
   prepends occult time no growth model sees — so the *translocation* may substantially predate the
   *outgrowth* clock. Conversely, CIC-DUX4 is a "single-catastrophic-driver," genomically quiet tumor
   with **few cooperating lesions** needed (see `tumorigenesis-reverse-engineering/`), so unlike stepwise
   carcinomas the driver-to-tumor latency is more likely **months-to-a-few-years than decades**.
5. **Atypical-fusion flag (~5%, golden rule #9).** If this case is one of the clinically/histologically
   CIC-rearranged but **fusion-unconfirmed** tumors, the "single-catastrophic-driver / quiet-genome"
   assumption in caveat 4 is weaker and the driver-latency argument is correspondingly softer.
6. **This is not a clinical determination.** Individual variation in growth rate is large; this exercise
   is hypothesis-space kinetics for the research framework, not a finding about the person, and carries no
   treatment implication.

**Method note:** cell-count↔size biophysics is `Established`; the doubling arithmetic is exact given the
inputs; the VDT band and the resulting dates are `Theoretical`/`Mechanistic` extrapolations from proxy
entities and standard Gompertzian tumor-growth theory. No citation was fabricated; where a CIC-DUX4-
specific source does not exist, that absence is stated rather than papered over.
