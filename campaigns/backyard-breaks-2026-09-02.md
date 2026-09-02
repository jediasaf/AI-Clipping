# Campaign Audit — Backyard Breaks [Clipping Campaign]

**Auditor pass — 2026-09-02.** Independent re-verification of Campaign Scout's report.
Context: owner override OVR-001 (revenue-first). Runway pressure acknowledged.

**RATING: YELLOW (weak)** — conditions below. Most are satisfiable TODAY.
**Recommendation: proceed only as a hard-capped N=1 learning play on TikTok, or decline.
The revenue case does not serve the stated objective.**

> **Revision note.** This file was rewritten mid-audit after the orchestrator flagged that
> **contentrewards.com is not Whop**. My first pass credited this campaign with Whop ToS
> protections (enumerated rejection grounds, 48-hour auto-approval, discretionary pro-rata).
> **That was wrong and is retracted.** The re-check also **reversed a correction I had made
> against Scout** — see "My own errors this pass". Both errors are recorded, not quietly fixed.

---

## Sources fetched (all primary, this session)

| # | Source | Status |
|---|---|---|
| A | `contentrewards.com/discover/e509f6d0-13bf-42bc-8450-09e12c216c33` | Fetched (direct + re-rendered) |
| B | Doc 1 — **Account Creation Guide** `docs.google.com/document/d/197leSvDY78QbsKP7GsWi5YWSzDFrktCB` | Fetched via `/mobilebasic` |
| C | Doc 2 — **Master Clipper SOP** `.../1dG6Moh7TzSKqKfHtB_QL8HngdG_y015Q` | Fetched via `/mobilebasic` |
| D | Doc 3 — **Clipper Brand & Niche Guide** `.../1iGL3Px-ymZSCK36iE5jKv9W6vpT5bX_i` | Fetched via `/mobilebasic` |
| E | Clip Context Tracker `docs.google.com/spreadsheets/d/1eX0vqF73N9x2gtkRbalnKMHRd3nbd-CEv0Rt4D2glM4` | Fetched via CSV export |
| **F** | **`contentrewards.com/terms` — CR Creator Terms (GOVERNING)** | **Fetched, 2 independent passes** |
| **G** | **`contentrewards.com/creators` — CR creator page** | **Fetched** |
| H | Drive sample file `1vBvKlQ7Bxzl5z5AbmCiVi0QzjmCENz7W` | Download path tested |

### Finding 0 — Scout audited one document out of three
**VERIFIED.** The campaign links **four** reference materials. Docs 1 and 2 contain **the
majority of the binding operational rules** — the required hashtags, the caption formula, the
no-commenting rule, and the entire account specification. Doc 3's ID was truncated on the first
page read (`...ymSCK36...`); the true ID is `...ymZSCK36...`.

Same failure mode flagged for Bible BFF: **the listing page understates the rule set.** Working
from the campaign card alone would have missed every tag and caption requirement — each a live
rejection ground under source G.

### Finding 0b — the governing contract is Content Rewards, not Whop
**VERIFIED.** The "Join Campaign" button resolves to a `whop.com/experiences/...` URL, which is
what led my first pass astray. But **Content Rewards publishes its own creator terms** (F) and
its own creator-facing rules (G), and those govern. Whop is the payment rail only.

**Consequence: every Whop ToS protection recorded in `knowledge/clipping-playbook.md` claim 7
must NOT be relied on for this campaign.** Specifically retracted: the closed four-ground
rejection list, the 48-hour AI auto-approval backstop, and the discretionary pro-rata clause.

---

## Checklist

### Permitted platforms
**VERIFIED.** Source A, verbatim: *"post them across dedicated Backyard Breaks pages on
TikTok, Instagram Reels, and/or Youtube Shorts."* Source B checklist names TikTok, Instagram and
*"YouTube Shorts account/channel"* separately.
**YouTube here is Shorts, explicitly — confirms priority question 7.**

### Permitted content / source material
**VERIFIED.** Source A: *"Download Clips from the official Clip Context Tracker sheet."*
Source C checklist: *"The clip came from the approved tracker/library."*

Source material is **restricted to the tracker**. **UNKNOWN — NEEDS VERIFICATION** whether
clipping Backyard Breaks' public Whatnot/Twitch/IG output *outside* the tracker is permitted.
Do not assume it is.

Tracker contents (E): **58 data rows returned**. Scout reported 62. The discrepancy is
**UNKNOWN — NEEDS VERIFICATION**. Also:
- Row 17 is **not** a Drive link — it is `instagram.com/p/DNEWr0FSGhD/`, a post on the verified
  `@backyardbreaks` account. Not downloadable as a file.
- Two rows (Buzz / Woody, *Toy Story 30th*) share the **same** Drive ID
  `1bDtnx7eHcOb9sjPQBlXMCXRA53UpCm_W` → **≤57 unique assets**, not 62.

### Required tags
**VERIFIED.** Source C, verbatim: *"#BackyardBreaks #BBPulls #Whatnot"*. Required, not suggested.
Source G names *"missing tags"* as a typical rejection reason — load-bearing.

### Required captions
**VERIFIED.** Source C caption formula, verbatim:
> `[Value or rarity] + [reaction/emotion] + Watch the next break live on Whatnot 👇 + #BackyardBreaks #BBPulls #Whatnot`

Source C checklist: *"Caption is short and uses the consistent Whatnot line."*

**⚠ CONFLICT — the mandated caption contains no sponsorship disclosure.** See "Unappealable
rejection risk". This is the sharpest ambiguity in the campaign.

### Account restrictions
**VERIFIED — materially more restrictive than "no entry gates" implies.** Source B, verbatim:
- *"Use a dedicated Backyard Breaks clip page. Do not post campaign submissions from your personal account."*
- *"The account should look like a clean Backyard Breaks highlights/fan page, not a random repost account."*
- *"New accounts should be set up fully before the first post: handle, profile photo, bio, and link."*
- Naming: `backyardbreaks_[word]`, `backyardbreaksclips`, `bbreaks_[word]`, `backyard_[word]`.
- Prohibited handles: personal names; random meme handles; handles resembling another card
  brand; *"Handles using another agency, unrelated business, or unrelated creator name."*
- Profile picture: *"Use a logo provided in the folder below."* Prohibited: *"a personal photo,
  a custom image, another brand logo, or an unrelated sports card image."*
- Bio: one of four approved templates.
- Link in bio: *"must always point to the Backyard Breaks live stream or approved Backyard
  Breaks destination."* Prohibited: *"your personal page, another creator, another store, a
  linktree you control, or an unrelated site."*
- Source B checklist implies **a separate account on each platform posted to**.

**Scout's load-bearing claim, tested against the actual briefs — it holds:**
- Follower minimum — **NOT PRESENT** in A/B/C/D or F. Not "zero"; absent.
- Engagement-rate floor — **NOT PRESENT**.
- Account age / warm-up protocol — **NOT PRESENT**.
- Application or review-to-join — **NOT PRESENT**. Source A shows a direct "Join Campaign" button.

**Added from CR terms (F), which Scout did not consult:**
- **Age 18+ — VERIFIED.** *"You must be at least 18 years old. The Platform is not directed to
  and may not be used by anyone under 18."*
- **OFAC / sanctioned-jurisdiction screening — VERIFIED.** Creators must represent they are
  *"not on the U.S. Treasury's Office of Foreign Assets Control (OFAC) Specially Designated
  Nationals (SDN) list"* and not in prohibited jurisdictions.
- **One-account-per-person / multi-account policy — UNKNOWN — NEEDS VERIFICATION.** Source F
  does not address it. Do not assume permitted or forbidden.

So: **no follower/ER/account-age/application gate — VERIFIED.** But the account specification is
itself a hard precondition: up to three purpose-built, fully-configured branded accounts must
exist before the first submission. **Owner-gated work** under `CLAUDE.md`.

### Geographic restrictions
**VERIFIED — targeting guidance, not a measured eligibility gate.** Source B, verbatim:
*"This campaign is built for US awareness and US stream traffic."* / *"Set account language,
captions, hashtags, posting times, and references for a US audience."* / *"Post during
US-friendly windows when possible: afternoon/evening Eastern Time..."* / *"Use US sports context
when relevant: NBA, NFL, MLB, WNBA, college hoops..."*

**Confirms Scout: no measured audience-geography threshold and no creator-residency requirement**
(beyond OFAC screening in F).

**Residual risk, larger than in my first pass:** US targeting is part of the brief, and under
source G rejection grounds are open-ended and human-decided. With no published numeric threshold,
**compliance cannot be proven in advance.**

### Minimum clip duration
**UNKNOWN — NEEDS VERIFICATION.** No minimum stated in A, B, C, D or F.

### Maximum clip duration
**UNKNOWN — NEEDS VERIFICATION.** No maximum stated in A, B, C, D or F.

Source C's three format templates run to **20s, 25s and 20s** (*"4-20s: let the host reaction
breathe"*, *"10-25s: replay the strongest reaction moment"*, *"2-20s: build the rip"*). That is a
**structural implication, not a stated rule** — INFERENCE. Do not record 20–25s as a requirement.

### Editing requirements
**VERIFIED.** Source C, verbatim:
- *"The first 3 seconds should show money, rarity, reaction, or tension."*
- *"Keep text huge, simple, and readable in under 2 seconds."* Text limited to 2 lines.
- Price/value on screen, checked against the tracker: *"The value/range is checked against the tracker."*
- *"Host audio/reaction is included."* / *"The card reveal is easy to see."*
- Three approved formats: **Price Reveal**, **Reaction First**, **Jackpot/ROI**.
- Objective, verbatim: *"Make cold US viewers understand the money fast. Price stops the scroll,
  reaction earns the watch time, rarity drives comments."*

### Prohibited modifications
**VERIFIED, and short.** Source C: *"Do not cover the card."* / *"Do not make viewers guess why
the pull matters."*

**Standing behavioural rule, easy to breach by reflex.** Source C, verbatim:
> *"NO commenting/responding to user comments on posts."*

Must be written into the posting SOP.

**Also VERIFIED (G):** *"the post being edited or deleted after you submitted"* is a named
rejection reason. **Posts must not be edited or deleted after submission.**

### Watermark rules
**UNKNOWN — NEEDS VERIFICATION.** No watermark rule in A, B, C, D or F. The campaign neither
requires nor forbids one.

Our own constraint applies independently (never cross-post a TikTok-watermarked export to Reels
— `campaigns/verification-2026-09-02.md`, claim 5, VERIFIED). **That is our rule, not the
campaign's.** Do not represent it as a campaign requirement.

### View qualification rules
**VERIFIED (F/G), and better documented than Whop's equivalent:**
- *"CR verifies views through the social platforms' APIs"* (§4.1). CPM pays *"per 1,000 verified views"* (§6.1).
- Fraud screening via a **Bot Score** (§9.2), but §9.3: *"The final decision on your Submission —
  approval, rejection, or resolution of a flag — is always made by a person, not by the Bot Score."*
- *"an open fraud flag pauses settlement until the flag is resolved"* (§7.3).

**EARNING WINDOW — VERIFIED, and it is short. Scout did not report this.** Source G, verbatim:
> *"On CPM your clip earns for 7 days from approval, then the payout is held 3 days"*

**A clip earns for only 7 days from approval, then a 3-day hold before payout.** A hard cap on
per-clip lifetime earnings that interacts badly with the runway. Source F §7.3 separately states
*"CPM earnings settle in recurring cycles (currently every 3 days)"* — reconcilable but not
identical; treat the 7-day earning window as the planning figure.

### Payment caps
**VERIFIED (A):** **$2.00 per 1,000 views**; **$2 minimum per submission**; **$250 maximum per
submission**. Identical across all three platforms.

**CREATOR FEE — 25%. VERIFIED. SCOUT WAS RIGHT; MY FIRST PASS WAS WRONG.**
Source F §5 and source G agree independently. CPM campaigns carry a fee tiered by **lifetime
platform earnings at the time a payout is processed**:

| Lifetime earnings | Fee |
|---|---|
| **under $1,000** | **25%** |
| $1,000+ | 20% |
| $2,500+ | 12.5% |
| $5,000+ | 7% |

Source G, verbatim: *"25% to start, then 20% past $1,000 lifetime, 12.5% past $2,500, 7% past $5,000"*.

**We are at $0 lifetime earnings → the 25% tier.**
→ **Net rate = $1.50 per 1,000 views. Scout's figure is VERIFIED.**

My first pass cited Whop's ToS (10% charged to the *seller*) and concluded no creator-side
deduction existed. Wrong contract. **Retracted.**

- $250 max ÷ $2/1k = **125,000 views per post** ceiling (gross). INFERENCE (arithmetic).
- **UNKNOWN — NEEDS VERIFICATION:** whether the **$2 minimum and $250 maximum are gross or net**
  of the 25% fee. Not stated. Materially affects the floor.
- Per-account and per-period caps: **NOT PRESENT.** UNKNOWN — NEEDS VERIFICATION.
- Withdrawal minimum: **VERIFIED none.** Source G: *"There is no minimum"* withdrawal.

### Submission process
**VERIFIED in outline.** Source C: *"Post is live before submitting to Whop."* Source B:
*"Account is ready before clips are submitted to Whop."* Publish first, then submit the live post.
Source F §7.2: *"A Brand moderator approves or rejects your Submission. CR Support cannot approve
or reject a Submission on a Brand's behalf."*

Exact creator-side submission fields remain **UNKNOWN — NEEDS VERIFICATION**. Resolves on first
real submission.

### Campaign deadline
**UNKNOWN — NEEDS VERIFICATION — one of two decisive gaps.**

No end date, deadline, expiry or "days left" field appears on source A, on either a direct fetch
or a re-render. The `contentrewards.com/discover` index shows campaign cards **carry no end-date
field at all** — name, age, description, budget progress, participant count, CPM only.

Source F confirms budget is the operative terminator: *"A Campaign draws down its funded budget
as Submissions are approved and validated; remaining budget stays available for new Submissions
until it is exhausted."* No Max-Payout/End-Date clause of the Whop kind appears in F.

→ **Budget exhaustion is the binding terminator.** An End Date may exist unsurfaced; resolvable
only after joining or by asking the campaign manager.

### Campaign budget — THE DECIDING VARIABLE
**VERIFIED (levels):** *"$24k/$32.2k"*, **74% consumed**, **$8,200 remaining**, **87 creators**.
Scout's figures confirmed. Re-render adds **total views 4.2M** and chart window **Aug 3 – Sep 2**.

**Burn rate — INFERENCE, with an honest range. I cannot make this precise.**

| Basis | Elapsed | Implied burn | Days left on $8.2K |
|---|---|---|---|
| Source A: *"Posted 2 months ago"* (~62d) | 62 days | ~$387/day | **~21 days** |
| Chart window Aug 3 → Sep 2 (30d), all $24K in it | 30 days | ~$800/day | **~10 days** |

I attempted to read per-date values off the campaign chart. The values returned were smoothly
linear and are, in my judgement, **interpolated by the page reader rather than read from data
labels — I am not treating them as evidence.** No figure here rests on them.

**An unreconciled discrepancy the owner should know about.** 4.2M total views × $2/1,000 =
**$8,400** — but **$24,000** is reported consumed. These do not reconcile at the stated CPM.
Possible explanations: 4.2M is a 30-day figure while spend is lifetime; "consumed" includes fees
or reserved budget; one figure is stale. **UNKNOWN — NEEDS VERIFICATION.** I flag it rather than
pick the convenient reading. Note that **every explanation that reconciles them implies
views-to-date are lower relative to spend than the CPM alone suggests.**

**Conclusion: 10–21 days of payable capacity. Scout's ~20 days is the optimistic end, not the
midpoint.** Two adverse considerations:
1. Burn is unlikely to be linear. Creator count grows over a campaign's life; 87 draw on it now,
   fewer did at the start. Average burn **understates** current burn. **~10 days is the
   decision-relevant figure.**
2. **The 7-day earning window compounds this.** A clip approved on day 3 of a 10-day remaining
   runway earns for 7 days *only if budget survives that long*. Budget exhaustion truncates
   earnings on already-approved clips. **The effective window for a clip produced today is
   shorter than either number alone suggests.**

**Economic consequence, stated plainly (INFERENCE, arithmetic on verified figures):**
$8,200 ÷ 87 creators ≈ **$94 per creator** if evenly split. It will not be split evenly — the top
earner visible on A (`sub.version`, 363.8K views ≈ $727 gross / **$545 net**) has run the whole
campaign on established accounts.

A cold start entering at **74% budget consumption**, needing to build up to three branded accounts
first, at **$1.50 net per 1,000 views**, with a **7-day per-clip earning window** and **~10–21
days of budget**, should expect realistic capture in the **low tens to low hundreds of dollars**.

**Against $8.2K cash and a $12K/month burn, this campaign cannot materially change the runway.**
Not a compliance objection and not my veto — it is the number the revenue-first objective has to
be judged against, and the owner should have it before committing editing hours.

### Copyright / licensing the campaign actually grants
**Mixed. Footage provenance is good; the contract structure pushes risk onto us.**

**VERIFIED — the footage is first-party.** Backyard Breaks is a real, operating card-breaking
business streaming its own breaks on its own channels (its site states daily breaks across 10
Whatnot channels plus Twitch `@backyardbreaks`). The tracker's sole non-Drive row resolves to a
post on the **verified `@backyardbreaks` Instagram account**. The Drive assets are recordings of
**Backyard Breaks' own streams** in **Backyard Breaks'/ClipHouse's own Drive**.

→ **This is NOT the Boxabl defect.** The orchestrator's test — *"If Backyard Breaks' own streams
are the source, this is fine"* — is **satisfied**. The tracker does not link third-party
breakers' footage.

**VERIFIED — express licence exists, but narrow and revocable.** Source F §19.1:
> *"Where a Brand provides footage or assets for a Campaign, the Brand grants you a limited,
> revocable, non-exclusive license"* — for that use only.

Combined with source A's *"Download Clips from the official Clip Context Tracker sheet and post
them"*, the tracker footage is licensed for campaign use. **Note "revocable".**

**⚠ VERIFIED — the third-party rights warranty is on US.** Source F §19.2:
> *"You warrant that your Clip does not infringe anyone's rights, and that you have cleared all
> third-party rights it uses."*

§19.3: *"You grant CR and the Brand a license to your Clip. The Brand's license takes effect only
once the Clip is approved and posted."*

**This is the contractual sting.** §19.1 licenses only what the Brand provides. §19.2 makes **us**
warrant clearance of **everything else in the frame** — and card-break footage is dense with
third-party IP we cannot clear: league marks (NFL/NBA/MLB shields, team logos), player likenesses
and autographs, and licensed entertainment properties visible in the tracker:
**Star Wars** ("Obiwan, Anakin, Padme triple auto"), **Toy Story 30th** (Buzz/Woody), **Pokémon**
("GOD PACK").

Whether Backyard Breaks can sub-license Disney, Lucasfilm, Pokémon and league marks is
**UNKNOWN — NEEDS VERIFICATION** and, on available evidence, unlikely to be express.

**In practice** the risk is low — filming physical trading cards is established commercial
practice and the brand streams it publicly at scale. **Contractually, it is assigned to us.**

→ **Mitigation, zero cost: use sports-card rows only. Avoid the Star Wars, Toy Story and Pokémon
rows.** ~53 sports rows remain — ample. Removes the sharpest edge of a warranty we cannot satisfy.

**VERIFIED — logo use is authorized for the profile picture.** Source B: *"Use a logo provided in
the folder below"*, with substitutes forbidden. Express grant for this use.
**UNKNOWN — NEEDS VERIFICATION:** the logo folder link was not captured in the fetched text;
folder accessibility unconfirmed.

### Drive links actually downloadable
**VERIFIED — yes, publicly, without sign-in.** Tested `1vBvKlQ7Bxzl5z5AbmCiVi0QzjmCENz7W`. The
`drive.google.com/uc?export=download` path resolves to `drive.usercontent.google.com` and returns
Google's large-file interstitial:
> *"Google Drive can't scan this file for viruses."*
> *"Logoman Full.mp4 (1.2G) is too large for Google to scan for viruses."*
> *"Would you still like to download this file?"*

Two operational facts:
1. Link-sharing is public — no authentication needed. **Confirms Scout.**
2. **These are full-length stream recordings at ~1.2 GB each, not pre-cut moments.** The name
   (*"Logoman Full"*) and size mean we download and locate the moment ourselves. Bandwidth and
   mining time per asset are **non-trivial** and were not in Scout's model. Only the first tested
   file's size is verified; the other ~56 are **UNKNOWN**.

### Reasons submissions can be rejected
**⚠ THE SECTION MY FIRST PASS GOT WRONG. Rejection risk is HIGHER and LESS APPEALABLE than
`knowledge/clipping-playbook.md` claim 7 implies.**

**VERIFIED — nothing auto-approves.** Source G, verbatim:
> *"Every submission is reviewed by the brand or their campaign manager, and nothing approves
> automatically."*

Source F §9.3: *"The final decision on your Submission — approval, rejection, or resolution of a
flag — is always made by a person, not by the Bot Score."*
Source F §7.2: *"A Brand moderator approves or rejects your Submission. CR Support cannot approve
or reject a Submission on a Brand's behalf."*

→ **The Whop 48-hour AI auto-approval backstop does NOT apply here. Retracted.**
→ **CR Support cannot override a brand rejection** — there is no escalation path.

**VERIFIED — rejection grounds are illustrative, not a closed list.** Source G, verbatim:
> *"wrong platform, missing tags or disclosure, reused content, or the post being edited or
> deleted after you submitted"*

Framed as what submissions *typically* get rejected for. **No enumerated, closed set of grounds
exists in F or G.** The Whop four-ground limit does not govern. **Retracted.**

**Practical consequence:** a brand moderator may reject on grounds not published in advance, with
no auto-approval fallback and no CR Support escalation. Combined with the subjective criteria
below, **a compliant-looking clip can be rejected and we have no appeal.**

**Latent ambiguity:** *"reused content"* is listed as a rejection reason **in a campaign that
requires posting the brand's own supplied footage.** The intended meaning is presumably reposting
others' clips or duplicates, not campaign-supplied assets — but that is **INFERENCE**, not stated.
**UNKNOWN — NEEDS VERIFICATION.**

### Unappealable rejection risk — priority question 6
**Subjective / non-pre-determinable criteria (real, and now unbuffered by any auto-approval):**
- Source A: *"Post must be exciting, engaging, and upbeat."* Not objectively testable.
- Source B: account must look *"clean ... not a random repost account."* Not objectively testable.
- Source B: US-targeting rules with no measurable threshold.
- Source G: open-ended rejection grounds, human decision, no escalation.

**⚠ THE ONE NEAR-CONTRADICTION — sponsorship disclosure.**
Source G names *"missing tags or **disclosure**"* as a typical rejection reason. Source F requires
compliance with *"the FTC disclosure requirements in our FTC Compliance page."* But **the caption
formula mandated by source C contains no disclosure whatsoever** — it is
`[Value or rarity] + [reaction/emotion] + Watch the next break live on Whatnot 👇 + #BackyardBreaks #BBPulls #Whatnot`.

Following the brief's mandated caption exactly may leave us non-compliant with CR's own disclosure
requirement; adding a disclosure deviates from the mandated caption. **Which prevails is not
stated anywhere.** This is the Independent Voter News failure mode — not a flat self-contradiction,
but a genuine conflict between two binding documents where **compliance cannot be determined in
advance.**

**UNKNOWN — NEEDS VERIFICATION.** Must be resolved with the campaign manager before publishing.
I did not fetch CR's FTC Compliance page; **the exact required disclosure format is UNKNOWN and I
am not guessing it.**

### Participation cost
**No cost is disclosed anywhere in the campaign flow** — source A shows a free "Join Campaign"
button with no fee, application or approval step. CR's model is a **percentage of earnings**
(25% at our tier), not an upfront charge — consistent with no participation cost.

**UNKNOWN — NEEDS VERIFICATION:** ClipHouse's Whop storefront (`whop.com/the-cliphouse/`, 15,299
joined, 4.7★/104 reviews) renders its price via JavaScript and returned no price. I am **not**
inferring "free" from an unrendered field.
→ Resolvable in ~2 minutes by opening the Join button and confirming no payment step.
**If joining costs money, this is disqualifying → RED.**

---

## Platform policy interaction (noted, not re-verified)

Per instruction, not re-verified; both already VERIFIED in `campaigns/verification-2026-09-02.md`.

1. **YouTube = Shorts, confirmed.** Our output is a captioned cut-down of another party's stream →
   squarely the reused-content profile. Enforcement is **channel-level**, and **permission is
   expressly no defence**. Consequence is loss of **YPP monetization only** — not removal, not
   reach. Since the campaign is the revenue mechanic, **this does not block the campaign.** It
   does mean the Backyard Breaks YouTube channel can never be counted on for AdSense.

2. **Instagram is the surface that actually costs money here.** A dedicated account whose entire
   output is cut-downs of another party's footage is exactly the profile Instagram's Original
   Content Guidelines target; the stated consequence is **account-level ineligibility for
   recommendation to non-followers on a rolling 30-day basis** — which suppresses precisely the
   payable views. Combined with the verified finding that **follower count is a stated Reels
   ranking input** (unlike TikTok), a cold IG account is the weakest of the three surfaces.
   → **TikTok first. Instagram is not a free third of the yield.**

---

## The payout floor — priority question 3
**VERIFIED: the floor is $2.00 per submission, which at $2/1,000 views is exactly 1,000 views.**
Both figures printed on source A. **Scout's arithmetic confirmed.**

**Mechanism — DOWNGRADED from my first pass.** I previously explained the floor using Whop's
brand-side wording (*"minimum amount a creator can earn from a video before it reaches your review
queue"*). **That is Whop's contract, not CR's, and I retract the explanation.** Source F states
**no per-submission minimum at all** — the $2 minimum is a **campaign-level parameter** set by the
brand and shown on source A. Its exact mechanism under CR — whether a sub-$2 post is unreviewable,
rejected, or simply pays nothing — is **UNKNOWN — NEEDS VERIFICATION**. The *number* is verified;
the *mechanism* is not.

Also **UNKNOWN**: whether $2 is measured **gross or net of the 25% fee**. If net, the true floor
is ~1,334 views, not 1,000.

**Do unpaid submissions count toward anything?** Nothing in A–G states that they do. No
participation credit, no ranking benefit, no carry-forward is described. → **A sub-floor post
earns $0 and, on available evidence, accrues nothing.** Stated as absence of evidence, not a
verified negative rule.

**No pro-rata provision exists in CR's terms.** My first pass cited Whop's discretionary pro-rata
clause; **that does not govern here and is retracted.** Model sub-floor posts at **$0**.

**On Scout's "roughly 80% of a cold account's clips will earn exactly $0":** the *floor* is
VERIFIED; the *80%* is **UNKNOWN — NEEDS VERIFICATION**. A modelling assumption with no source,
at N=0. I flag it because it reads like a measured figure and is not one. Directionally I agree
the floor, not the CPM, is the binding constraint at N=0 — but that agreement is **INFERENCE and
should not carry a number.**

---

## Brand-safety note (not a rules defect — but the owner is branding accounts with this name)
**VERIFIED as reported by trade press.** In early 2025 Backyard Breaks was the subject of a
significant hobby controversy: co-founder Grant Telford and another member made remarks on a live
break widely condemned as sexualizing a child. Whatnot **suspended the personal `backyardgrant`
account** (87,200 followers at suspension); **Backyard Breaks as a company was not banned** and
continued streaming, and Telford has since returned. A petition seeking the brand's removal from
Whatnot, Twitch and major conventions drew ~7,700 signatures.

Why it belongs here: the campaign requires accounts **named and branded as Backyard Breaks**,
carrying its logo and linking to its stream. Those accounts inherit the brand's reputational
exposure and are **not reusable for anything else afterwards**. A real cost of participation, and
a decision only the owner can make. **Not** a reason to rate RED.

---

## RISK RATING: **YELLOW (weak)**

**Why not GREEN.** Six material problems; the re-check made four of them worse:
1. **No verifiable end date**, **10–21 days** of budget runway on a burn rate I cannot pin down,
   plus an **unreconciled views-vs-spend discrepancy** (4.2M views vs $24K consumed).
2. **Net rate is $1.50, not $2.00** — a verified 25% fee at our earnings tier.
3. **Nothing auto-approves; rejection grounds are open-ended; CR Support cannot override a brand
   rejection.** No appeal path.
4. **A genuine disclosure conflict** between the mandated caption (no disclosure) and CR's own
   rejection ground for *"missing ... disclosure"*. Compliance cannot be determined in advance.
5. **§19.2 assigns third-party rights clearance to us** for IP we cannot clear.
6. **Participation cost undisclosed** (likely zero, unverified).

**Why not RED.** The campaign is genuine and unusually well documented across four sources. Rights
*provenance* is sound — first-party footage, expressly instructed use, publicly downloadable
assets, authorized logo — so **this is not the Boxabl defect**. No entry gate of the kind that
killed MW4 exists: **no follower minimum, no engagement floor, no account-age rule, no
application, no measured audience-geography gate — Scout's central claim is VERIFIED.** Budget
remains; not expired, not out of budget. Nothing asks us to do something we won't do.

**The honest summary: compliance is achievable; the economics do not serve the objective.**
At $1.50 net per 1,000 views, a 1,000-view floor per post, a 7-day per-clip earning window, up to
three accounts to build first, and ~10–21 days of budget, **the realistic outcome is tens to low
hundreds of dollars.** That does not move a $12K/month burn. Under a revenue-first objective this
campaign's main value is **learning at N=0**, not revenue — precisely what OVR-001 deprioritized.

**Recommendation: proceed only as a hard-capped learning play (TikTok only, 3–5 clips), or decline
and have Scout find a campaign with more budget headroom.** I do not recommend a multi-platform
build-out at 74% budget consumption.

---

## What would make this GREEN

All but one are satisfiable **TODAY**, before any editing hour is spent.

| # | Condition | Satisfiable today? |
|---|---|---|
| 1 | **Confirm joining is free.** Open the Join button; confirm no payment step. **If it costs money → RED.** | **YES** — ~2 min |
| 2 | **Obtain the End Date, or confirm none exists.** Visible post-join, or ask the ClipHouse campaign manager. | **YES if visible post-join**; else needs a manager reply |
| 3 | **Resolve the disclosure conflict.** Ask the campaign manager whether a paid-partnership disclosure is required, and read CR's FTC Compliance page. **Blocking — do not publish until answered.** | **Partly** — FTC page today; manager answer not in our control |
| 4 | **Confirm whether the $2 floor and $250 cap are gross or net** of the 25% fee. | **YES** — post-join |
| 5 | **Confirm the logo folder is accessible** and contains a usable logo. | **YES** |
| 6 | **Ask the campaign manager, one message:** (a) min/max clip duration; (b) multi-account policy; (c) whether tracker-supplied footage is exempt from the *"reused content"* rejection ground. | Asked today; **answer time not in our control** |
| 7 | **Re-read remaining budget immediately before editing and again before publishing.** Abort below ~$2K. | **YES** — standing check |

**Conditions 1, 4, 5 and the FTC half of 3 are satisfiable today and require only joining.**
Conditions 2, 6 and the manager half of 3 require information available **only after joining or
after a campaign-manager reply**. Of these, **only #3 is blocking** — #2 and #6 affect planning,
not eligibility.

**Binding conditions if the owner proceeds:**
1. **Condition 1 first.** Participation cost is disqualifying.
2. **Condition 3 before any clip publishes.** The disclosure conflict is the one item that can
   make a fully compliant clip rejectable with no appeal.
3. **TikTok only for the first cycle.** Prove one account before spending on IG or YouTube.
4. **Sports-card rows only.** Avoid Star Wars, Toy Story and Pokémon rows — §19.2 puts that
   warranty on us and the mitigation is free.
5. **Hard budget checkpoint** before editing and before publishing. Abort below ~$2K remaining.
6. **Cap exposure at 3–5 clips.** Do not commit hours the realistic capture cannot justify.
7. **Write the no-comment and no-edit-after-submission rules into the posting SOP.**
8. **Nothing publishes without owner approval**, per `CLAUDE.md`. Account creation is owner-gated.

---

## Corrections to Campaign Scout's report

| Scout claim | Audit finding |
|---|---|
| $2/1k on YT/IG/TikTok | **VERIFIED** |
| **Net $1.50 after 25% creator fee** | **VERIFIED.** CR §5 and the CR creator page independently confirm 25% at <$1,000 lifetime earnings. **Scout was right. My first-pass "correction" was wrong and is retracted.** |
| $2 min payout ⇒ 1,000-view floor | **Number VERIFIED.** Mechanism and gross/net basis **UNKNOWN**. |
| $250 max per post | **VERIFIED** (⇒ 125,000-view gross ceiling) |
| $24k/$32k, ~$8.2K left | **VERIFIED**, but does not reconcile with the 4.2M view total — flagged |
| 87 creators | **VERIFIED** |
| No follower min / no ER floor / no measured geo gate | **VERIFIED** — the load-bearing claim holds. Adds 18+ and OFAC screening from CR terms. |
| ~20 days runway | **Optimistic end of a 10–21 day range.** ~10 days is decision-relevant. |
| Tracker has 62 rows | **58 returned**, ≤57 unique (one duplicate ID, one Instagram link) |
| ~80% of clips earn $0 | Floor VERIFIED; **the 80% is unsourced** and must not be quoted as data |
| Dedicated `backyardbreaks_*` account required | **VERIFIED**, stricter than summarized: **one per platform**, plus mandated logo, bio template, bio link |
| (not reported) | **Scout audited 1 of 3 documents** — Docs 1–2 carry the hashtags, caption formula, no-comment rule and account spec |
| (not reported) | **Clips earn for only 7 days from approval**, then a 3-day hold |
| (not reported) | **Nothing auto-approves**; open-ended rejection grounds; no CR Support escalation |
| (not reported) | **§19.2 puts third-party rights clearance on the creator** |
| (not reported) | **Drive assets are ~1.2 GB full stream recordings**, not pre-cut moments |

**On the Scout bias hypothesis.** The task asked me to look for errors all running one direction
(optimistic). **I did not find that pattern here.** Scout's rate, fee, budget, creator count,
gates and floor were all accurate; its runway estimate was optimistic within a range; its tracker
count was slightly high; its "80%" was an unsourced number presented as analysis. The real defect
was **omission** — auditing one of three rule documents, and missing the earning window, the
approval mechanics and the rights warranty. **Scout's errors here are gaps, not spin.**

## My own errors this pass (recorded, not hidden)

1. **Applied the wrong contract.** My first pass credited Whop ToS protections — closed
   four-ground rejection list, 48-hour auto-approval, discretionary pro-rata — to a **Content
   Rewards** campaign. All three retracted. The `whop.com` join URL misled me; **the join URL does
   not determine the governing terms.**
2. **Corrected Scout wrongly on the 25% fee.** I searched Whop's fee schedule, found a 10%
   seller-side fee, found no creator-side fee, and downgraded Scout's verified figure to UNKNOWN.
   Scout was right. **I applied skepticism to Scout's number without first confirming I was
   reading the right contract** — the same class of error I exist to catch. Had this gone
   unchallenged it would have overstated net revenue by 25%.
3. **Process fix for future audits:** identify the governing terms *before* auditing rate,
   rejection and rights mechanics. Add to the audit checklist: **"Which entity's terms govern, and
   what is the primary-source URL for them?"**
