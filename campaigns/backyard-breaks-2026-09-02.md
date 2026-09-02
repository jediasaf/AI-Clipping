# Campaign Audit — Backyard Breaks [Clipping Campaign]

**Auditor pass — 2026-09-02.** Independent re-verification of Campaign Scout's report.
Context: owner override OVR-001 (revenue-first). Runway pressure acknowledged.

**RATING: YELLOW** — conditions below. Most are satisfiable TODAY.

---

## Sources fetched (all primary, this session)

| # | Source | Status |
|---|---|---|
| A | `contentrewards.com/discover/e509f6d0-13bf-42bc-8450-09e12c216c33` | Fetched |
| B | Doc 1 — **Account Creation Guide** `docs.google.com/document/d/197leSvDY78QbsKP7GsWi5YWSzDFrktCB` | Fetched via `/mobilebasic` |
| C | Doc 2 — **Master Clipper SOP** `.../1dG6Moh7TzSKqKfHtB_QL8HngdG_y015Q` | Fetched via `/mobilebasic` |
| D | Doc 3 — **Clipper Brand & Niche Guide** `.../1iGL3Px-ymZSCK36iE5jKv9W6vpT5bX_i` | Fetched via `/mobilebasic` |
| E | Clip Context Tracker `docs.google.com/spreadsheets/d/1eX0vqF73N9x2gtkRbalnKMHRd3nbd-CEv0Rt4D2glM4` | Fetched via CSV export |
| F | Whop Content Rewards ToS `whop.com/content-rewards-terms-of-service/` | Fetched |
| G | Whop Docs — Content Rewards | Fetched |
| H | Drive sample file `1vBvKlQ7Bxzl5z5AbmCiVi0QzjmCENz7W` | Download path tested |

### Finding 0 — Scout audited one document out of three

**VERIFIED.** The campaign links **four** reference materials, not one. Scout's task
description named only the brief and the tracker. Doc 1 (Account Creation Guide) and Doc 2
(Master Clipper SOP) contain **the majority of the binding operational rules** — including
the required hashtags, the caption formula, the no-commenting rule, and the entire account
specification. Doc 3's ID was truncated in the first page read (`...ymSCK36...`); the true
ID is `...ymZSCK36...`.

This is the same failure pattern flagged for Bible BFF: **the listing page understates the
rule set**. Anyone working from the campaign card alone would have missed every tag and
caption requirement and would have been validly rejectable under Whop ToS ground (i).

---

## Checklist

### Permitted platforms
**VERIFIED.** Source A, verbatim: *"post them across dedicated Backyard Breaks pages on
TikTok, Instagram Reels, and/or Youtube Shorts."* Source B checklist names *"TikTok account"*,
*"Instagram account"*, *"YouTube Shorts account/channel"*.

**YouTube here is Shorts, explicitly — confirms priority question 7.** See "Platform policy
interaction" below.

### Permitted content / source material
**VERIFIED.** Source A: *"Download Clips from the official Clip Context Tracker sheet."*
Source C submission checklist: *"The clip came from the approved tracker/library."*

Source material is **restricted to the tracker**. Clipping arbitrary Backyard Breaks streams
is not authorized by these materials. **UNKNOWN — NEEDS VERIFICATION** whether clipping from
their public Whatnot/Twitch/IG output outside the tracker is permitted; do not assume it is.

Tracker contents (source E): **58 data rows returned** by CSV export. Scout reported 62.
The 4-row discrepancy is **UNKNOWN — NEEDS VERIFICATION** (possible fetch truncation or
possible Scout overcount). Also note:
- Row 17 is **not** a Drive link — it is `instagram.com/p/DNEWr0FSGhD/`, a post on the
  verified `@backyardbreaks` account. Not downloadable as a file.
- Two rows (Buzz / Woody, Toy Story 30th) share the **same** Drive ID
  `1bDtnx7eHcOb9sjPQBlXMCXRA53UpCm_W` — 57 unique assets at most, not 62.

### Required tags
**VERIFIED.** Source C, verbatim: *"#BackyardBreaks #BBPulls #Whatnot"*. Stated as a
requirement, not a suggestion.

### Required captions
**VERIFIED.** Source C caption formula, verbatim:
> `[Value or rarity] + [reaction/emotion] + Watch the next break live on Whatnot 👇 + #BackyardBreaks #BBPulls #Whatnot`

Source C checklist: *"Caption is short and uses the consistent Whatnot line."*

### Account restrictions
**VERIFIED — and this is materially more restrictive than "no entry gates" implies.**

Source B, verbatim:
- *"Use a dedicated Backyard Breaks clip page. Do not post campaign submissions from your personal account."*
- *"The account should look like a clean Backyard Breaks highlights/fan page, not a random repost account."*
- *"New accounts should be set up fully before the first post: handle, profile photo, bio, and link."*
- Naming: `backyardbreaks_[word]`, `backyardbreaksclips`, `bbreaks_[word]`, `backyard_[word]`.
- Prohibited handles: personal names; random meme handles; handles resembling a different
  card brand; *"Handles using another agency, unrelated business, or unrelated creator name."*
- Profile picture: *"Use a logo provided in the folder below."* Prohibited: *"a personal photo,
  a custom image, another brand logo, or an unrelated sports card image."*
- Bio: one of four approved templates.
- Link in bio: *"must always point to the Backyard Breaks live stream or approved Backyard
  Breaks destination."* Prohibited: *"your personal page, another creator, another store, a
  linktree you control, or an unrelated site."*
- Source B checklist: a **separate account on each platform posted to**.

**Now the part Scout got right, and it matters:**
- Follower minimum — **NOT PRESENT** in any of A/B/C/D. Not "zero"; simply absent.
- Engagement-rate floor — **NOT PRESENT**.
- Account age / warm-up protocol — **NOT PRESENT**.
- Application or review-to-join — **NOT PRESENT**. Source A shows a direct "Join Campaign" button.
- One-account-per-person limit — **UNKNOWN — NEEDS VERIFICATION.** Not stated anywhere.
  Do not assume multi-account is permitted **or** forbidden.

So Scout's headline claim ("no gates") is **VERIFIED as to the four gates that killed MW4 and
threaten Bible BFF**. But it omits that the account specification is itself a hard
precondition: three purpose-built, fully-configured branded accounts must exist before the
first submission. That is **owner-gated work** under `CLAUDE.md` (account creation).

### Geographic restrictions
**VERIFIED — targeting guidance, not a measured eligibility gate.**

Source B, verbatim: *"This campaign is built for US awareness and US stream traffic."*
*"Set account language, captions, hashtags, posting times, and references for a US audience."*
*"Post during US-friendly windows when possible: afternoon/evening Eastern Time..."*
*"Use US sports context when relevant: NBA, NFL, MLB, WNBA, college hoops..."*

**Confirms Scout: no measured audience-geography threshold.** No stated "must be X% US
viewers." No creator-residency requirement anywhere in A/B/C/D.

**But flag the residual risk honestly:** US targeting *is* "criteria set forth in the Offer,"
so under Whop ToS ground (i) a rejection asserting non-US audience is structurally available.
Because no numeric threshold is published, **compliance cannot be proven in advance**. This is
a genuine unappealable-rejection vector — smaller than a hard gate, larger than zero.

### Minimum clip duration
**UNKNOWN — NEEDS VERIFICATION.** No minimum is stated in A, B, C or D.

### Maximum clip duration
**UNKNOWN — NEEDS VERIFICATION.** No maximum is stated in A, B, C or D.

Source C's three format templates run to **20s, 25s and 20s** respectively
(*"4-20s: let the host reaction breathe"*, *"10-25s: replay the strongest reaction moment"*,
*"2-20s: build the rip"*). That is a **structural implication, not a stated rule** — treat as
INFERENCE. Do not record 20–25s as a campaign requirement.

### Editing requirements
**VERIFIED.** Source C, verbatim:
- *"The first 3 seconds should show money, rarity, reaction, or tension."*
- *"Keep text huge, simple, and readable in under 2 seconds."* Text limited to 2 lines.
- Price/value must be **on screen**, checked against the tracker: *"The value/range is checked
  against the tracker."*
- *"Host audio/reaction is included."*
- *"The card reveal is easy to see."*
- Three approved formats: **Price Reveal**, **Reaction First**, **Jackpot/ROI**.
- Objective, verbatim: *"Make cold US viewers understand the money fast. Price stops the
  scroll, reaction earns the watch time, rarity drives comments."*

### Prohibited modifications
**VERIFIED, and short.** Source C:
- *"Do not cover the card."*
- *"Do not make viewers guess why the pull matters."*

**Operational restriction that is easy to miss and easy to breach:** Source C, verbatim:
> *"NO commenting/responding to user comments on posts."*

This is a standing behavioural rule on our own accounts, not a per-clip rule. It must be
written into the posting SOP or it will be violated by reflex.

### Watermark rules
**UNKNOWN — NEEDS VERIFICATION.** No watermark rule appears in A, B, C or D. The campaign
neither requires nor forbids one.

Our own constraint still applies independently (never cross-post a TikTok-watermarked export
to Reels — `campaigns/verification-2026-09-02.md`, claim 5, VERIFIED). That is our rule, not
the campaign's. Do not represent it as a campaign requirement.

### View qualification rules
**VERIFIED** (Whop ToS, source F — this campaign runs on Whop; the "Join Campaign" button
resolves to `whop.com/experiences/exp_ZqS6e8CmhdI57P/campaigns/...`).

> *"Rates ... are calculated based on the legitimate views a Deliverable achieves as determined
> by Whop in its sole discretion, which for avoidance of doubt, excludes views generated by, or
> suspected to be generated by any bots, script, macro or other automated means or system..."*

Hold period / view-counting window: **UNKNOWN — NEEDS VERIFICATION.** Neither the campaign
docs nor Whop's public docs state how long after posting views accrue.

### Payment caps
**VERIFIED** (source A): **$2.00 per 1,000 views**; **$2 minimum per submission**;
**$250 maximum per submission**. Rate is identical across all three platforms.

- $250 max ÷ $2/1k = **125,000 views per post** is the earnings ceiling per clip. INFERENCE
  (arithmetic on verified figures).
- Per-account and per-period caps: **NOT PRESENT** in any source. UNKNOWN — NEEDS VERIFICATION.

**CORRECTION TO SCOUT — the net rate is not $1.50.**
Scout reported *"net $1.50 after the platform's 25% creator fee."* **I could not verify a 25%
creator fee from any primary source, and the ToS says something different.** Source F, verbatim:

> *"Whop will deduct from the Seller's Whop account a fee payable to Whop in the amount of 10%
> of all amounts paid from Seller to Participants"*

That fee is charged to the **seller**, on top of what participants are paid — it does not
reduce our $2. No creator-side deduction appears in the ToS or in Whop's docs. A ~7% clipper
fee is repeated in secondary vendor blogs; **no primary source states it** and I did not accept
it.

→ **Net payout rate is UNKNOWN — NEEDS VERIFICATION.** It is somewhere between $1.86 and
$2.00 per 1,000 views on available evidence, and **not** the $1.50 Scout modelled. Note the
direction: Scout was **pessimistic** here, where its previous pass erred optimistic. The
lesson is that Scout's numbers are unreliable in *both* directions, not that they lean one way.

### Submission process
**VERIFIED in outline.** Source C: *"Post is live before submitting to Whop."* Source B:
*"Account is ready before clips are submitted to Whop."* So: publish first, then submit the
live post to Whop.

Exact creator-side submission fields remain **UNKNOWN — NEEDS VERIFICATION** (consistent with
the standing residual unknown in `campaigns/verification-2026-09-02.md`). Resolves on first
real submission.

### Campaign deadline
**UNKNOWN — NEEDS VERIFICATION, and this is one of the two decisive gaps.**

No end date, deadline, expiry or "days left" field appears on source A. I checked the
`contentrewards.com/discover` index: campaign cards **do not carry an end-date field at all** —
they show name, age, description, budget progress, participant count and CPM only.

Whop ToS (F) confirms an End Date is a real campaign parameter:
> *"Participant may receive compensation at the Rate until such time as the Max Payout is met
> or the End Date is reached, whichever occurs first."*

So an End Date may exist and simply not be surfaced publicly. **This is resolvable only after
joining** (or by asking the campaign manager). Absent it, **budget exhaustion is the binding
terminator** for planning purposes.

### Campaign budget — THE DECIDING VARIABLE
**VERIFIED (levels):** *"$24k/$32k"* on the card; **$24,000 of $32,200, 74% consumed,
$8,200 remaining**, **87 creators**. Scout's figures are confirmed.

**Burn rate — INFERENCE, with an honest range. I cannot make this precise.**

Two anchors, and they disagree:

| Basis | Elapsed | Implied burn | Days left on $8.2K |
|---|---|---|---|
| Source A: campaign *"Posted 2 months ago"* (~62d) | 62 days | ~$387/day | **~21 days** |
| Source A chart window: **Aug 3 → Sep 2** (30d) | 30 days | ~$800/day | **~10 days** |

I attempted to read per-date values off the campaign chart. The values returned were smoothly
linear and are, in my judgement, **interpolated by the page reader rather than read from data
labels — I am not treating them as evidence** and no burn figure here rests on them.

**Conclusion: 10–21 days of payable capacity remaining. Scout's ~20 days is the optimistic end
of the range, not the midpoint.** Two further considerations, both adverse:

1. Burn is **very unlikely to be linear**. Creator count grows over a campaign's life; 87
   creators are drawing on the budget now, fewer were at the start. Average burn therefore
   **understates** current burn. The 10-day figure is the more decision-relevant one.
2. Under Whop ToS ground (iv), *"the Max Payout is met or the End Date is reached"* is an
   **enumerated valid rejection ground**. A fully compliant, high-performing clip can be
   legitimately unpaid because the budget emptied first. This is the exact mechanism named in
   `campaigns/verification-2026-09-02.md` as *"the real way clipping hours get burned on Whop."*

**Economic consequence the owner needs stated plainly (INFERENCE, arithmetic on verified figures):**
$8,200 remaining ÷ 87 creators ≈ **$94 per creator** if evenly split. It will not be evenly
split — the top earner visible on source A (`sub.version`) shows 363.8K views ≈ $727 gross —
but that creator has been running the whole campaign with established accounts.

A cold start entering at 74% budget consumption, needing to build three accounts first, should
expect a realistic capture in the **low hundreds of dollars** before the budget empties.
**Against a $12K/month burn and $8.2K cash, this campaign cannot materially change the
runway.** That is not a compliance objection and it is not my veto — it is the number the
revenue-first objective has to be judged against, and the owner should have it before
committing editing hours.

### Copyright / licensing the campaign actually grants
**Largely favourable — this is the strongest part of the campaign, and it is NOT the Boxabl
defect.**

**VERIFIED — the footage is first-party.** Backyard Breaks is a real, operating card-breaking
business that streams its own breaks on its own channels (its site states daily breaks across
10 Whatnot channels plus Twitch `@backyardbreaks`). The tracker's sole non-Drive row resolves
to a post on the **verified `@backyardbreaks` Instagram account**. The Drive assets are
recordings of **Backyard Breaks' own streams**, held in **Backyard Breaks'/ClipHouse's own
Drive**. This is materially different from a campaign distributing third-party streams it does
not control.

**VERIFIED — an express instruction to use the material.** Source A: *"Download Clips from the
official Clip Context Tracker sheet and post them."* Combined with a named campaign manager
(ClipHouse) and a controlled asset library, this is an operative authorization to use the
tracker footage for campaign purposes.

**VERIFIED — logo use is authorized for the profile picture.** Source B instructs *"Use a logo
provided in the folder below"* and forbids substitutes. That is an express grant for this use.
**UNKNOWN — NEEDS VERIFICATION:** the logo folder link itself was not captured in the fetched
text; folder accessibility is unconfirmed.

**Residual UNKNOWNs — do not fill these in:**
- No **written licence grant, scope, or indemnity clause** appears in A, B, C or D. The
  authorization is by instruction, not by contract term. **UNKNOWN — NEEDS VERIFICATION.**
- The footage depicts **third-party IP embedded in the products**: league marks (NFL/NBA/MLB
  shields, team logos), player likenesses and autographs, and licensed entertainment
  properties visible in the tracker (**Star Wars** — "Obiwan, Anakin, Padme triple auto";
  **Toy Story 30th** — Buzz/Woody; **Pokémon** "GOD PACK"). Backyard Breaks' authority to
  license *its own stream footage* is credible; its authority to sub-license **Disney,
  Lucasfilm, Pokémon and league marks** is **UNKNOWN — NEEDS VERIFICATION** and, on the
  evidence available, unlikely to be express.
  → **Practical mitigation, low cost:** the tracker offers ~57 assets; the sports-card rows
  alone are ample. **Prefer sports rows; avoid the Star Wars, Toy Story and Pokémon rows.**
  This costs us nothing and removes the sharpest edge of the residual IP question.

**Verdict on rights: acceptable, and not a curable-by-override defect of the Boxabl kind.**
The footage is the brand's own and its use is expressly instructed.

### Drive links actually downloadable
**VERIFIED — yes, publicly, without sign-in.** Tested `1vBvKlQ7Bxzl5z5AbmCiVi0QzjmCENz7W`.
The `drive.google.com/uc?export=download` path resolves to `drive.usercontent.google.com` and
returns Google's large-file interstitial:

> *"Google Drive can't scan this file for viruses."*
> *"Logoman Full.mp4 (1.2G) is too large for Google to scan for viruses."*
> *"Would you still like to download this file?"*

Two operational facts follow:
1. Link-sharing is public — no authentication needed. Confirms Scout.
2. **These are full-length stream recordings at ~1.2 GB each, not pre-cut moments.** The file
   name (*"Logoman Full"*) and size indicate we must download and locate the moment ourselves.
   Bandwidth and mining time per asset are **non-trivial** and were not in Scout's model. Only
   the first tested file's size is verified; the other 56 are **UNKNOWN**.

### Reasons submissions can be rejected
**VERIFIED (Whop ToS, source F) — enumerated and closed.** A seller may reject ONLY if:
> *"(i) the Participant does not follow the criteria set forth in the Offer, (ii) the
> Participant does not follow these Program Terms, (iii) there is a reasonable suspicion of
> fraud, and/or (iv) the Max Payout is met or the End Date is reached."*

Plus the 48-hour auto-approval backstop recorded in `campaigns/verification-2026-09-02.md`.
Arbitrary-rejection risk is therefore **structurally low**. Ground (i) is the live one, and it
incorporates every rule in Docs 1–3 — which is exactly why auditing only the campaign card
would have been dangerous.

**Subjective / non-pre-determinable criteria (real, but bounded):**
- Source A: *"Post must be exciting, engaging, and upbeat."* Not objectively testable.
- Source B: account must look *"clean ... not a random repost account."* Not objectively testable.
- Source B: US-targeting rules with no measurable threshold (above).

**No self-contradiction found.** I looked specifically for the Independent Voter News failure
mode. Docs 1–3 are mutually consistent; Doc 1 governs accounts, Doc 2 governs clip craft,
Doc 3 governs domain context. No conflicting instruction was identified.

### Participation cost
**No cost is disclosed anywhere in the campaign flow** — source A shows a free "Join Campaign"
button with no fee, application or approval step.

**UNKNOWN — NEEDS VERIFICATION:** ClipHouse's Whop storefront (`whop.com/the-cliphouse/`,
15,299 joined, 4.7★/104 reviews) renders its price field via JavaScript and returned no price
on fetch. I am **not** inferring "free" from the absence of a rendered price.
→ Resolvable in about two minutes by opening the Join button and confirming no payment step
appears. **If joining costs money, this is disqualifying and the rating drops to RED.**

---

## Platform policy interaction (noted, not re-verified)

Per the standing instruction, I did not re-verify these; both are already VERIFIED in
`campaigns/verification-2026-09-02.md`.

1. **YouTube = Shorts, confirmed.** Our output is a captioned cut-down of someone else's stream
   → squarely the reused-content profile. Enforcement is **channel-level**, and **permission is
   expressly no defence** (*"This policy applies even if you have permission from the original
   creator"*). Consequence is loss of **YPP monetization only** — not removal, not reach. Since
   the campaign is the revenue mechanic and YouTube monetization was never the payable channel,
   **this does not block the campaign.** It does mean the Backyard Breaks YouTube channel should
   never be counted on for AdSense.

2. **Instagram is the one that actually costs money here.** A dedicated account whose entire
   output is cut-downs of another party's footage is the exact profile Instagram's Original
   Content Guidelines target, and the stated consequence is **account-level ineligibility for
   recommendation to non-followers, on a rolling 30-day basis**. On Reels that suppresses
   precisely the payable views. Combined with the verified finding that **follower count is a
   stated Reels ranking input** (unlike TikTok), a cold IG account is the weakest of the three
   surfaces.
   → **Operational read: TikTok first. Treat Instagram as speculative, not as a free third of
   the yield.** This bears directly on the $2/1,000-view floor below.

---

## The payout floor — priority question 3

**VERIFIED: the floor is $2.00 per submission, which at $2/1,000 views is exactly 1,000 views.**
Both figures are printed on source A. Scout's arithmetic is confirmed.

**Mechanism confirmed** (source G, Whop docs, brand-side wording): the brand sets *"the minimum
amount a creator can earn from a video before it reaches your review queue."* A post that never
reaches $2 earned **never enters review**, and therefore is never approved or paid.

**Do unpaid submissions count toward anything?** Nothing in A, B, C, D, F or G states that they
do. No participation credit, no ranking benefit, no carry-forward is described.
→ **A sub-1,000-view post earns $0 and, on available evidence, accrues nothing.**
Stated as absence of evidence, not as a verified negative rule.

**One qualifier in our favour, and it is discretionary — do not plan on it.** ToS (F):
*"Whop may in its discretion issue pro-rata payments to Participants for views fewer than the
designated threshold on a first-come first-served basis."* Sub-threshold payment is **possible
but not owed**. Model at $0.

**On Scout's "roughly 80% of a cold account's clips will earn exactly $0":** the *floor* is
VERIFIED; the *80%* is **UNKNOWN — NEEDS VERIFICATION**. It is a modelling assumption with no
source and no data behind it, and we have N=0. I flag it because it reads like a measured
figure and is not one. Directionally I agree the floor, not the CPM, is the binding constraint
at N=0 — but that agreement is INFERENCE, and it should not be given a number.

---

## Brand-safety note (not a rules defect — owner should know before branding accounts)

**VERIFIED as reported by trade press:** in early 2025 Backyard Breaks was the subject of a
significant hobby controversy. Co-founder Grant Telford and another member made remarks on a
live break widely condemned as sexualizing a child. Whatnot **suspended the personal
`backyardgrant` account** (87,200 followers at suspension); **Backyard Breaks as a company was
not banned** and continued streaming, and Telford has since returned. A petition seeking the
brand's removal from Whatnot, Twitch and major conventions drew ~7,700 signatures.

Why this belongs in the audit: the campaign requires us to create accounts **named and branded
as Backyard Breaks**, carrying its logo and linking to its stream. Those accounts inherit the
brand's reputational exposure, and they are not reusable for anything else afterwards. That is
a real cost of participation and a decision only the owner can make. It is **not** a reason to
rate the campaign RED.

---

## RISK RATING: **YELLOW**

**Why not GREEN.** Four material unknowns remain, and two are economic rather than cosmetic:
the campaign has **no verifiable end date**, its **remaining runway is 10–21 days on a burn
rate I cannot pin down**, the **net payout rate is unconfirmed**, and **participation cost is
undisclosed**. Under Whop ToS ground (iv), budget exhaustion makes non-payment of compliant
work a *legitimate* outcome — so these are not paperwork gaps, they are the difference between
paid and unpaid hours.

**Why not RED.** The campaign is genuine and unusually well documented. The rights position is
sound — first-party footage, expressly instructed use, publicly downloadable assets, authorized
logo. Rejection grounds are contractually enumerated and closed, with a 48-hour auto-approval
backstop. No entry gate of the kind that killed MW4 exists. Nothing here asks us to do anything
we won't do. Budget remains. It is not expired and not out of budget.

**The honest summary:** compliance is achievable; the economics are marginal and shrinking.

---

## What would make this GREEN

All but one are satisfiable **TODAY**, before any editing hour is spent.

| # | Condition | Satisfiable today? |
|---|---|---|
| 1 | **Confirm joining is free.** Open the Join button; confirm no payment step. **If it costs money → RED, campaign abandoned.** | **YES** — ~2 min |
| 2 | **Obtain the End Date, or confirm none exists.** Visible on the campaign page after joining, or ask the ClipHouse campaign manager directly. | **YES if visible post-join**; otherwise needs a manager reply |
| 3 | **Confirm the creator-side fee.** Whop payout page after joining will show gross vs net. Settles $1.50 vs $2.00 — a 25% swing in every projection. | **YES** — post-join, no editing needed |
| 4 | **Confirm the logo folder is accessible** and contains a usable logo. | **YES** |
| 5 | **Ask the campaign manager three questions in one message:** (a) min/max clip duration; (b) one-account-per-person / multi-account policy; (c) whether views have a counting window or hold period. | Asked today; **answer time not in our control** |
| 6 | **Re-read remaining budget immediately before committing editing hours**, and again before publishing. If it drops below ~$2K, stop. | **YES** — and should be a standing check |

**Conditions 1–4 are satisfiable today and require only joining, which costs nothing but the
account.** Condition 5 requires information available only after contacting the campaign
manager, and its three items are **low-severity** — none blocks production, because we control
clip length, we can simply not run multiple accounts, and the hold period affects timing rather
than eligibility.

**Binding conditions if the owner proceeds:**

1. **Condition 1 must be cleared first.** Participation cost is disqualifying.
2. **TikTok first.** Build and prove one TikTok account before investing in Instagram or
   YouTube. IG's originality regime and follower-weighted Reels ranking make a cold IG account
   the weakest surface; do not treat three platforms as three times the yield.
3. **Sports-card tracker rows only.** Avoid the Star Wars, Toy Story and Pokémon rows until the
   sub-licensing question is answered. Zero cost to comply.
4. **Hard budget checkpoint.** Re-check remaining budget before editing and before publishing.
   Abort below ~$2K remaining.
5. **Cap the exposure.** Do not commit more editing hours than the realistic capture justifies
   — low hundreds of dollars, not thousands.
6. **Write the no-comment rule into the posting SOP.** *"NO commenting/responding to user
   comments on posts"* is easy to breach by reflex and is a ground-(i) rejection risk.
7. **Nothing publishes without owner approval**, per `CLAUDE.md`. Account creation is
   owner-gated and this campaign requires up to three new branded accounts.

---

## Corrections to Campaign Scout's report

| Scout claim | Audit finding |
|---|---|
| $2/1k on YT/IG/TikTok | **VERIFIED** |
| Net $1.50 after "25% creator fee" | **NOT VERIFIED.** No 25% creator fee in any primary source. ToS charges **10% to the seller**. Net rate **UNKNOWN**, likely $1.86–$2.00. Scout erred **pessimistic** here. |
| $2 min payout ⇒ 1,000-view floor | **VERIFIED** |
| $250 max per post | **VERIFIED** (⇒ 125,000-view ceiling per clip) |
| $24k/$32k, ~$8.2K left | **VERIFIED** |
| 87 creators | **VERIFIED** |
| No follower min / no ER floor / no measured geo gate | **VERIFIED** — the load-bearing claim holds |
| ~20 days runway | **Optimistic end of a 10–21 day range.** Burn is likely accelerating; ~10 days is the decision-relevant figure. |
| Tracker has 62 rows | **58 returned**, ~57 unique (one duplicate ID, one Instagram link). Discrepancy UNKNOWN. |
| ~80% of clips earn $0 | Floor VERIFIED; **the 80% figure is unsourced** and should not be quoted as data. |
| Dedicated `backyardbreaks_*` account required | **VERIFIED**, and stricter than summarized: **one per platform**, plus mandated logo, bio template and bio link. |
| (not reported) | **Scout audited 1 of 3 documents.** Docs 1–2 carry the hashtags, caption formula, no-comment rule and full account spec. |
| (not reported) | **Drive assets are ~1.2 GB full stream recordings**, not pre-cut moments. Mining cost is real. |
