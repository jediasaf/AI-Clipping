# Operating Plan

**Status:** Stage 1 — Become good at clipping
**Capital budget:** $0
**Tooling:** free tools only, unless there is a strong economic justification otherwise
**Owner:** human. **Orchestrator:** Clipping COO (main Claude session).

---

## The actual objective

The primary objective of the first seven days is **not revenue**.

It is to determine whether we can **systematically create clips that outperform baseline
distribution** — that is, whether our selection and packaging process beats posting a random
moment from the same source.

This matters because the entire long-term business rests on it. If our process does not beat
random, then everything downstream — multiple campaigns, niche playbooks, selling distribution
to creators — is built on nothing. Better to find that out in week one, cheaply, than in month
six, expensively.

A week of clips that all flop but produce a clear reason **is a successful week**. A week with
one lucky 300k-view clip and no idea why **is not**.

---

## 7-day experiment

### Day 1 — Ground truth
- Campaign Scout: find opportunities.
- Campaign Auditor: audit the best campaign.
- Select **ONE** primary campaign. Focus beats diversification at N=0.
- Download and organize approved source material into `sources/`.
- Clip Miner: identify **at least 15** candidate moments.
- Select top 5.

### Day 2 — First production
- Create 3–5 clips. **Do not make them identical.**
- Test different hook hypotheses — one clip per hypothesis where possible.
- Publish only once requirements have been verified (Auditor GREEN).
- Record every post in `analytics/clips.csv` at time of posting, not later.

### Days 3–4 — First read
- Analyze early results. Expect the sample to be anecdotal (N<5) — do not over-read it.
- Produce another 5–10 clips at **70% exploitation / 30% new experiments**.
- **Do not blindly copy the first winner.** At this N, the first winner is probably variance.

### Days 5–6 — Prune and press
- Continue publishing.
- Kill repeatedly weak formats.
- Increase production around evidence-backed winners only.

### Day 7 — Week 1 Report
Performance Analyst produces:

total clips · total views · median views · best clip · worst clip · view distribution ·
gross earnings · net earnings · editing hours · revenue per hour · winning hook types ·
weak hook types · campaign acceptance rate · lessons · next experiments

---

## First milestones

| | Milestone |
|---|-----------|
| A | 10 published clips |
| B | 10,000 legitimate cumulative views |
| C | 30 clips |
| D | 100,000 legitimate cumulative views |
| E | First 100k-view clip |
| F | First meaningful payout |
| G | **Repeatable evidence that our process beats random posting** |

Milestone G is the one that matters. A–F are progress markers; G is the thesis.

**Do not celebrate vanity milestones that do not improve expected business performance.**

---

## Go / No-Go — evaluate at ~30 published clips

**CONTINUE AGGRESSIVELY if:**
- multiple clips outperform baseline
- at least one format shows repeatability
- campaign acceptance is high
- production time is falling
- economics show credible upside

**CONTINUE EXPERIMENTING if:**
- results are mixed
- some hooks work but sample size is small
- there is evidence of learning

**PAUSE / CHANGE CAMPAIGN if:**
- source material is weak
- campaign repeatedly rejects valid submissions
- campaign economics deteriorate
- budget disappears
- campaign rules make scaling impractical

**STOP THIS APPROACH if, after substantial testing:**
- there is no evidence our clip selection improves
- distribution remains consistently negligible
- expected earnings per hour are structurally poor
- opportunity cost exceeds realistic upside

**Do not rationalize failure.** The go/no-go criteria are written now, before we have results,
precisely so that we cannot move them later to protect a conclusion we have grown attached to.
If we hit STOP conditions, the correct action is to stop, and the week was still worth it.

---

## RUN DAILY — command centre routine

When the owner says `RUN DAILY`:

1. Read current project state (`analytics/*.csv`, `experiments/experiment-log.md`).
2. Check campaign status — budget, deadline, rule changes.
3. Review clips awaiting action, by pipeline stage.
4. Delegate appropriate tasks to agents **in parallel**.
5. Analyze latest metrics.
6. Decide today's highest-value actions by expected economic value.
7. Produce the daily brief:

```
TODAY'S OBJECTIVE
TOP 3 ACTIONS
CLIPS TO CREATE
EXPERIMENT BEING TESTED
CURRENT BOTTLENECK
RISKS
METRICS TO WATCH
```

8. Update project files.
9. Ask the owner **only** for decisions or actions that genuinely require a human — publishing
   approval, account access, spending, campaign sign-up, or a judgment call between real
   alternatives.

---

## Longer-term path — DO NOT IMPLEMENT YET

| Stage | |
|-------|---|
| 1 | Become good at clipping |
| 2 | Prove distribution with data |
| 3 | Operate several campaigns |
| 4 | Build reusable playbooks by niche |
| 5 | Approach creators/brands with actual case studies |

Eventually the offer is not "video editing" — it is **short-form content distribution**.

Possible later model: creator supplies long-form → our system mines it → distributed
editors create variants → multiple pieces published → performance data identifies winning
formats → winners inform future production.

**We earn the right to build this only after Stage 1 works.** Building Stage 5 infrastructure
before Stage 1 is proven is the most common way operations like this die.
