# Experiment Log

Every experiment is recorded **before** we see the result. A prediction written after the fact
is not a prediction, and a log that only contains confirmed hypotheses is a marketing
document rather than a record.

## Format

```
### EXP-###  <short name>
- **Date opened:**
- **Hypothesis:** (falsifiable — state what would prove it wrong)
- **Prediction:** (specific and numeric where possible)
- **Design:** (what we will produce, how many, what varies, what is held constant)
- **Sample size target:** N =
- **Result:** (filled in after data)
- **Verdict:** CONFIRMED / REFUTED / INCONCLUSIVE — with N
- **Alternative explanations considered:**
- **Action taken:**
```

Also log here: **owner overrides of a YELLOW/RED campaign audit**, with the reason given at
the time.

---

## Open experiments

### EXP-001  Does our selection process beat random?
- **Date opened:** 2026-09-02
- **Hypothesis:** Clips chosen by the Clip Miner scoring rubric achieve a higher median view
  count than clips cut from randomly selected moments in the same source material.
- **Prediction:** Median views of rubric-selected clips ≥ 2× median views of random-selected
  clips, over the same campaign, platform, and posting window.
- **Design:** Once a campaign is live and source material is approved, publish a control arm
  of randomly chosen moments alongside the rubric-selected arm. Hold constant: source video,
  platform, clip length band, posting time-of-day band.
- **Sample size target:** N = 20 per arm before drawing any conclusion. Below N=20 this is a
  weak signal at best.
- **Result:** _pending — no campaign selected yet_
- **Verdict:** _pending_
- **Alternative explanations considered:** _pending_
- **Action taken:** _pending_

**Note:** This is the experiment the whole 7-day plan exists to run. Milestone G is its
verdict. Everything else is instrumentation.

### MEAS-001  Campaign runway and payout realization
- **Date opened:** 2026-09-02
- **Not an experiment — a measurement with a scheduled second reading.** Logged here because
  acting on the first reading alone would be acting on an inference we could cheaply verify.
- **Problem:** every runway figure we hold is a single progress-bar observation divided by a
  coarse "1mo ago" post date. Scout checked for Wayback snapshots of these campaign pages;
  none exist. So there is no second point available from the past — the only way to get one
  is to take a reading now and another later.
- **Reading 1 (2026-09-02, VERIFIED as of today):**
  - Boxabl — $13.1K paid of $85,000 (15% used), 18.7M cumulative views, 294 creators
  - Lovable — $4.7K of $50,000 (9% used), 6.4M views, 109 creators
  - LiveMap — $1.6K of $45,000 (4% used), 34 creators
  - MW4 — $86.5K remaining of $105,000, 26M views, 237 creators
- **Reading 2 due:** 2026-09-04 to 2026-09-05. Re-read the same four progress bars and view
  counts. Two dated readings give burn rate directly, converting every runway figure from
  INFERENCE to VERIFIED, and exposes the true payout realization rate.
- **The open anomaly:** Boxabl shows $13,100 paid against 18.7M views = $0.70 effective per
  1,000, which is *above* its own $0.50 headline. The arithmetic does not close. Lovable runs
  the other way at ~73% of its headline. Until this is resolved we do not know what an editing
  hour is actually worth, and realization risk is unbounded in both directions.
- **Why this matters economically:** headline CPM is not take-home CPM. We are about to choose
  where to spend the only resource we have, and the deciding number is one nobody publishes.

---

## Closed experiments

_None yet._

---

## Override log

_None yet._
