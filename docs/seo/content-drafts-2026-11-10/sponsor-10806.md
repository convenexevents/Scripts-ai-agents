# Rewrite: /sponsor/ (page 10806)

## Nathan's decisions (10 Nov 2026) — Kai builds these

1. **Call length: 15 minutes.** Use Version A for the "How do we start?" FAQ with "15-minute": "Book a 15-minute exploratory call..." The booking link stays cal.com/convenexevents/15min.
2. **Guest-list sign-off: dinners and roundtables only.** Use Freya's Version B everywhere (hero, meta, OG, Twitter, step 2, FAQ).
3. **12-week lead time and seniority bars: yes, state them.** Use Version A (drafted wording) for section 7 and both FAQs.
4. **Reach: UK, Europe and the US.** Replace every "UK and US" / "the UK and US" with "the UK, Europe and the US" (section 7, the "Who is actually in the room?" FAQ, anywhere else it appears).

5. **Dinner size: 6 to 20 guests** (Nathan, 10 Nov). Replace every "10 to 25" on this page with "6 to 20" (formats card, room-size FAQ, anywhere else).

Callum's FAQPage schema must match the built FAQ text word for word.


## Felix review (10 Nov 2026)

**Verdict: PASS WITH EDITS.** I've made the edits below in this file. It can go to Freya. Nothing on the live site has been touched.

| Check | Result |
|---|---|
| Proof claim | Pass. Team framing in previous roles. No personal names, no "Convene X has delivered", no event counts, no time windows. Section 6 now uses the website proof line wording ("our founding team spent several years"). |
| Brand voice | Pass. UK English, contractions, digits, no em dashes, no banned words, no exclamation marks. The H1 and section 2 are the strongest parts of the page. |
| Sponsor promises | Pass after edit. No lead, pipeline, meeting or ROI promises are left. In step 4, "The relationship is yours" asserted an outcome, so it's now "The next step is yours to earn." |
| Accuracy | Pass with open items. Every figure traces to `brand-brief.md`, and the brief is the standard. The live service pages disagree with the brief in places (see table below). Those pages need fixing; this draft doesn't. |
| Call length | Fixed. "45-minute" removed from the FAQ. No length is stated anywhere on the page now. |
| SEO | Pass. The title (48 characters) is unchanged. The meta description (138) has the focus keyword in its first 4 words. I've written the OG description (158) and the Twitter description (151). |
| GDPR | None on this page. One flag on the webinar page (see Open). |

### Edits I made
1. **Section 4, webinar card:** "for 25 to 50 senior registrations" is now "aiming for 25 to 50 senior registrations". This matches the FAQ ("aim for"), so it doesn't read as a guaranteed number.
2. **Section 5, step 4:** "The relationship is yours... Any next step" is now "The next step is yours to earn... Any follow-up". We can't promise that a relationship forms.
3. **Section 6, proof:** "our team spent several years in previous roles" is now "our founding team spent several years, in previous roles,", aligned to the approved website proof line. It's still team framing, with no names.
4. **Section 7, lede:** "Every guest is invited and vetted, not registered" is now "Every guest is invited and vetted against the profile you agree with us". The old line contradicted the webinar card and FAQ, which talk about registrations.
5. **FAQ, room size:** "so everyone at the table takes part" is now "small enough for a real conversation". At 25 dinner guests, "everyone takes part" overclaims, and a webinar isn't a table.
6. **FAQ, how do we start:** "Book a 45-minute exploratory call" is now "Book an exploratory call". The link is `/15min` and the length isn't confirmed.
7. **Meta:** I wrote the OG and Twitter descriptions. Rank Math is currently filling both with the whole page body, old pipeline and founder lines included. That's confirmed via the Rank Math read.
8. **Housekeeping:** I updated "Why this rewrite" item 3 and flags 2 and 3 to reflect today's brand-brief update.

### Accuracy check against the live service pages (read 10 Nov)

| Claim in draft | Brand brief | 9415 Dinners | 9414 Roundtables | 9413 Webinars | Call |
|---|---|---|---|---|---|
| Dinners 10 to 25 | 10 to 25 | **Conflicts:** "Ten seats", "Ten at the table", final CTA "Ten seats. One question.", FAQ "typically 8 to 12" | n/a | n/a | Draft is right. 9415 needs fixing. |
| Roundtables 6 to 12 | 6 to 12 | n/a | Matches: "6 to 12" (FAQ), "Six to twelve" (body) | n/a | OK (body should use digits: "6 to 12") |
| Webinars 25 to 50 registrations | 25 to 50 | n/a | n/a | No figure stated | Brief only. OK. |
| Director+ for dinners and roundtables | Director+ | "C-suite leaders and senior decision-makers... heads of function". No Director+ bar stated | "senior leaders". No bar stated | n/a | Brief only. OK. Service pages are vaguer, not contradictory. |
| Senior Manager+ for webinars | Senior Manager+ | n/a | n/a | **Conflicts:** FAQ says "typically manager level and above" | Draft is right. 9413 needs fixing. |
| 12 weeks (2 weeks plan, 10 weeks recruit) | Yes | Not stated | Not stated | Not stated | Brief only. OK. |
| Host signs off the guest list | Yes (sponsor-hosted model) | Not stated | Not stated | Not stated | Brief only. Applies to webinars? See Open. |

### Open: for Freya
- **Button swap in section 10** (Book Exploratory Call as primary). I recommend approving it, because it matches the hero and the brief's primary CTA.
- **Service page fixes (Iris to draft, Kai to build; not this page):**
  - **9415 dinners:** "Ten seats" / "Ten at the table" / "Ten seats. One question. No pitch." and FAQ "8 to 12" all conflict with 10 to 25. The FAQ "What do we get out of hosting one?" promises "warm introductions" and "meaningful commercial opportunities", which is a sponsor-promise breach. The venues copy says "trusted by global enterprise brands", which is unsubstantiated.
  - **9413 webinars:** the **"Founder led" band** ("our founder... throughout his career") is the same house-rule breach we've just fixed here. It needs the same team rewrite. The seniority line "manager level and above" should read "Senior Manager level and above". The CTA reads "Book a Discovery Call" where every other page says "Exploratory".
  - **9414 roundtables:** "build trusted commercial relationships" leans towards an outcome promise. It's a light edit.
- **Pattern for Iris (recurring):** the founder band and the "warm follow-up / commercial opportunities" phrasing appear on 3 pages now. Worth a site-wide search for "founder", "his career", "pipeline", "warm" and "commercial opportunit" before the next batch.

### Open: for Nathan
1. **Call length.** Is it 45 minutes or 15? The brief says 45 and the link slug says `/15min`. Until you confirm, the page states no length. If the call is 45 minutes, consider renaming the slug, and update `brand-brief.md` if it's 15.
2. **Guest-list sign-off for webinars.** The hero, meta, OG, Twitter, step 2 and FAQ all say "you sign off the guest list". The brief supports this for sponsor-hosted events, but no service page confirms it, and webinars run on registrations. If it doesn't hold for webinars, the fallback for the FAQ is "For dinners and roundtables, you sign off the guest list." The meta still works as written.
3. **12-week lead time and Director+ / Senior Manager+.** These are stated publicly for the first time on this page (they come from the brief). Please confirm you're happy to commit to them in public copy.
4. **GDPR flag for Eleanor (9413, not this page).** The webinar FAQ promises sponsors a report "detailing who attended live, any chat messages, submitted questions". Sharing attendee identities and chat content with a sponsor needs a lawful basis and a registration-page notice. Worth Eleanor's check.

### Post 8986 ("The Case Against Conference Sponsorship"): noted, not rewritten
Yes, it needs a light fix before this page sends more hosts to it:
- "Conference sponsorship at scale produces low-quality pipeline at scale" is a category comparison (no named competitor), so it's acceptable. But "what would 12 curated dinners per year... produce at your close rate from relationship-led pipeline?" invites the reader to model ROI from our dinners. That's an implied ROI/pipeline promise. Suggest reframing it as a question about conversation quality, without the close-rate maths.
- These lines are unsubstantiated: "The cost-per-relationship is lower, often significantly", "the metrics know it" and "Teams that run this calculation honestly often find a case for moving at least part of the budget". Each needs a source or softer framing.
- "Twelve people in a room" sits within 10 to 25, so it's fine, but "12 senior, qualified guests" per dinner reads as a standard size. Minor.
- The OG and Twitter descriptions for 8986 are empty (they fall back to defaults). Worth setting at the same time.

## Freya sign-off (10 Nov 2026)

**Verdict: APPROVED WITH EDITS, for Nathan's review.** Felix's review is done and I agree with all 8 of his edits. I've checked the copy against the updated `brand-brief.md` (event counts banned in public copy). There are no event counts, time windows, personal names, "Convene X has delivered" lines or lead, meeting or ROI promises. There are no em dashes, exclamation marks or banned words, and the copy is UK English with contractions and digits. It reads like a person wrote it, and the H1, section 2 and the "a host who pitches loses the room" FAQ make the page worth reading. **I haven't touched the live site.**

This page doesn't need to wait for the service-page fixes below. It removes a live house-rule breach (the founder band) and the pipeline promises, so holding it would leave both live.

### My edit
1. **Section 6, proof line:** I took out the commas around "in previous roles". It now reads "our founding team spent several years in previous roles designing and delivering...". Felix's version had 3 commas in a row, which made the line hard to read. The framing hasn't changed. On Felix's flag 1: `brand-voice.md` isn't in the repo for me either, but the same proof line ("Before establishing Convene X Events, our founding team spent several years...") appears in the Felix, Andrew and Victor agent files. I'm treating it as the approved line. "Several years" is the approved wording, not a count, so the ban doesn't apply to it.

### Decisions
1. **Final CTA button swap: approved.** Book Exploratory Call becomes the primary button and Build Your Room the alt. That matches the hero and the brief's primary CTA.
2. **The 3 open points for Nathan: no answer means the fallback.** Kai builds Version A of a point only if Nathan explicitly confirms it. If Nathan approves the page without answering a point, Kai builds Version B for that point. Callum's FAQPage schema must match whichever FAQ text is built, word for word.

### Point 1: call length
**Decision:** build with no length stated (Felix's edit). Nobody adds a length until the stated length and the link slug agree.

- **Version B (default, build this now):** FAQ "How do we start?" stays as drafted: "Book an exploratory call. It's a conversation about your audience and goals, not a pitch. If you'd like to sketch the room first, use Build Your Room."
- **Version A (only if Nathan confirms a length *and* the cal.com slug matches it):** "Book a [45/15]-minute exploratory call. It's a conversation about your audience and goals, not a pitch. If you'd like to sketch the room first, use Build Your Room."
- The buttons read "Book Exploratory Call" in both versions. If the answer is 15 minutes, `brand-brief.md` gets updated (owner: me, once Nathan answers).

### Point 2: guest-list sign-off for webinars
**Decision:** until Nathan confirms that the host signs off the guest list for webinars too, the sign-off claim covers dinners and roundtables only, everywhere on the page. I don't agree with Felix that the meta "still works as written". "Dinners, roundtables and webinars, with a guest list you sign off" reads as covering all 3, so the meta gets the fallback as well.

- **Version A (Nathan confirms it holds for webinars):** build everything as drafted above.
- **Version B (default):**

| Where | Version B wording |
|---|---|
| Hero lede | Sponsor an executive event your buyers will make time for. We invite senior leaders who match your ideal customer profile, and you host an honest conversation over a private dinner, a virtual roundtable or a webinar. For dinners and roundtables, you sign off the guest list. |
| Meta description (142 chars, keyword still in the first 4 words) | Sponsor an executive event senior buyers make time for: invitation-only dinners and roundtables with a guest list you sign off, plus webinars. |
| OG description (155 chars) | Invitation-only executive dinners, virtual roundtables and webinars for B2B teams who want real conversations with senior buyers. No pitch, no badge scans. |
| Twitter description (146 chars) | Host an invitation-only dinner, roundtable or webinar for senior leaders who match your profile. You agree the audience. No pitch, no badge scans. |
| Section 5, step 2 | **We invite the guests.** Our team invites and confirms senior leaders who match that profile, and shapes the question that earns their time. For dinners and roundtables, you sign off the guest list. |
| FAQ "What exactly does a sponsor get?" | The right people in the room and a conversation worth having. We invite senior leaders who match the profile you agree with us, design the format and theme around your goals, and position your brand as the host. For dinners and roundtables, you sign off the guest list. We don't sell lead lists: what happens after the event is down to the conversation. |

The OG and Twitter descriptions in Version B leave the sign-off out rather than qualify it. There isn't room to qualify it cleanly in a share card, and a half-claim reads worse than no claim.

### Point 3: 12-week lead time and the Director+ / Senior Manager+ bars
**Decision:** I approve the copy as drafted. Both points come straight from `brand-brief.md`, where they're listed as public angles ("Director+ means Director+"; "12 weeks minimum"), and they're the most specific things on the page. Stating them in public is still a positioning commitment, which is Nathan's call, not mine. So the same rule applies: Version A only if Nathan explicitly says yes.

- **Version A (Nathan confirms):** sections 7 and 9 as drafted above.
- **Version B (default):**

| Where | Version B wording |
|---|---|
| Section 7, P | We invite chief officers, vice presidents, directors and other senior leaders across financial services, cybersecurity, IT and technology, procurement and marketing, from London and across the UK and US. We agree the seniority bar for each event with you before any invitations go out. |
| FAQ "Who is actually in the room?" | Senior decision-makers who match your profile: chief officers, vice presidents and directors across financial services, cybersecurity, IT, procurement and marketing in the UK and US. We agree the seniority bar with you before invitations go out, and every guest is invited and vetted. |
| FAQ "How long does it take to set up?" | Most of the time goes on inviting and confirming the right guests, not on logistics. Rushing that part fills seats with the wrong people, so we'll agree a realistic timeline with you on the first call. |

Points 2 and 3 are independent. Kai can build A for one and B for the other. Section 7's lede ("vetted against the profile you agree with us") works in every combination.

### Other notes for Nathan (not blocking)
- "UK and US" reach (hero chips, roundtable card, section 7 and the FAQ) is carried over from the live page, so it isn't new, but nobody has checked it operationally (flag 7). If we can't recruit US guests today, tell me and it comes out.
- I agree with Felix on the GDPR flag for 9413. It goes to Eleanor and doesn't block this page.

### Follow-ups, in priority order (Iris drafts, then Felix, me and Nathan; Kai builds; Callum checks. None of these is authorised by this sign-off.)
1. **Site-wide search (Callum, read-only, first).** Search for "founder", "his career", "pipeline", "warm", "commercial opportunit", "Discovery Call", "Ten seats", "8 to 12", "manager level", "34 events" and "18 months". It's cheap, and it scopes items 2 to 5 so Iris fixes each page once, not twice.
2. **9413 webinars.** The "Founder led" band is the same house-rule breach we've just removed here. It's live now, and /sponsor/ links to this page. Also: "manager level and above" becomes "Senior Manager level and above" (to match Version A of point 3; if Nathan picks Version B, align to that instead), and "Book a Discovery Call" becomes "Book Exploratory Call". Eleanor checks the attendee and chat report in the FAQ in parallel.
3. **9415 dinners.** Sponsor-promise breach ("warm introductions", "meaningful commercial opportunities"), plus "Ten seats", "Ten at the table", "Ten seats. One question." and the FAQ "8 to 12", which all contradict 10 to 25 on this page. "Trusted by global enterprise brands" comes out unless we can substantiate it. Ideally 2 and 3 ship in the same release as /sponsor/, or straight after, because the "Explore →" cards send readers to both.
4. **Post 8986 (ROI framing).** It's linked from this page's Further reading block. Take out the close-rate maths and the unsourced "cost-per-relationship is lower" and "the metrics know it" lines, and set the empty OG and Twitter descriptions. Fix it before Nathan requests indexing for /sponsor/.
5. **9414 roundtables (light edit).** Soften "build trusted commercial relationships" and change "Six to twelve" to "6 to 12".

---

Status: **DRAFT, Felix-reviewed (Pass with edits), Freya-approved with edits (10 Nov), for Nathan's review.** Nothing has been changed on the live site.
Drafted by: Senior Content Writer, 10 November 2026, at Nathan's request.
Pipeline: Felix (brand/quality) > Freya (sign-off) > Nathan (preview and approval) > Kai builds > Callum pre-publish check.

## Why this rewrite

From Felix and Freya's review on 10 Nov:
1. The band "A founder who has done this before... our founder... his career" refers to one person. Proof belongs to the team "in previous roles".
2. "The room your pipeline is missing", "From ICP to pipeline" and "Warm pipeline follows" lean towards a pipeline promise. The brand brief rules out lead, meeting and ROI promises.
3. No event counts in public copy. Nathan's decision (10 Nov) is now in `brand-brief.md`, and the "34 events" claim is retired.
4. Dinner size is 10 to 25 guests everywhere. The dinner card currently says "ten".

## Summary

| | |
|---|---|
| Page | 10806, `/sponsor/` (URL unchanged) |
| Focus keyword (unchanged) | `sponsor an executive event` |
| Reader | Senior marketing, partnerships and sales leaders at B2B companies thinking about hosting |
| Primary CTA | Book Exploratory Call (cal.com link, as now) |
| Secondary CTA | Build Your Room |
| Structure | All 10 sections kept, in the same order. The "Further reading" block (Kai, 10 Nov, posts 8986 and 8985) is kept exactly as it is. 2 FAQs added (room size, timeline). |

### How the page is built (note for Kai)

The layout read shows **this page isn't Elementor-built.** It's one Gutenberg `wp:html` block (inline CSS, sections, footer and GSAP script) on the `elementor_canvas` template, and `_elementor_data` is empty. Copy changes are text swaps inside that HTML block. Keep every class name, `id`, `rv` class and the `/*cx-sp-*/` CSS as they are. Only the visible text below changes. Save a revision first. The pre-B2 revision is 11830, but the Further reading block was added after it, so don't restore that revision.

### Proposed meta (Rank Math)

- **SEO title (48 chars, unchanged):** `Sponsor an Executive Event in London | Convene X`
- **Meta description (138 chars, new):** `Sponsor an executive event senior buyers make time for: invitation-only dinners, roundtables and webinars, with a guest list you sign off.`
- Current description (for reference): "Put your brand in the room with senior decision-makers. Invitation-only executive dinners, virtual roundtables and webinars built around your ICP." It doesn't contain the focus keyword and leans on "ICP" jargon.
- **OG description (158 chars, new, written by Felix):** `Invitation-only executive dinners, virtual roundtables and webinars for B2B teams who want real conversations with senior buyers. You sign off the guest list.`
- **Twitter description (151 chars, new, written by Felix):** `Host an invitation-only dinner, roundtable or webinar for senior leaders who match your profile. You sign off the guest list. No pitch, no badge scans.`
- Both must be set explicitly in Rank Math (Social tab). Confirmed live on 10 Nov: Rank Math is filling both fields with the whole page body, including "The room your pipeline is missing", "our founder... his career" and "Warm pipeline follows", so the old copy would keep appearing on LinkedIn shares after the rewrite.
- **OG and Twitter title:** leave inheriting the SEO title.
- Rank Math reports an SEO score of 0 for this page. That's probably because the content is one HTML block. Callum to check after the build.

---

## Section by section

Format: **Current**, then **New**, then **Why**.

### 1. Hero

**Current**
- Pill: For Marketing, Growth & Enterprise Sales Leaders
- H1: The room your / pipeline is / *missing.*
- Lede: Reach the senior decision-makers who never answer cold outreach. Convene X puts your brand at the table with a curated audience of your exact ICP, over an executive dinner, a virtual roundtable, or a webinar.
- Buttons: Book Exploratory Call (primary) / Build Your Room (alt)

**New**
- Pill: For Marketing, Partnerships & Sales Leaders
- H1 (same 3-span structure): `<span>The room your</span> <span>buyers say</span> <em>yes to.</em>`
- Lede: Sponsor an executive event your buyers will make time for. We invite senior leaders who match your ideal customer profile, you sign off the guest list, and you host an honest conversation over a private dinner, a virtual roundtable or a webinar.
- Buttons: unchanged.

**Why:** Drops the pipeline promise from the H1, puts the focus keyword in the first sentence, and names the 3 things the reader gets (the right people, the guest-list sign-off, a real conversation). The pill now includes partnerships leaders, who are part of the audience.

### 2. The problem (01)

**Current**
- Eyebrow: The problem
- H2: Your buyers stopped answering.
- Lede: The people you most need to reach, the C-suite and their direct reports, are the hardest audience in the market. They screen calls, delete cold email, and skip the ads.
- P: Sponsoring another crowded conference buys you a logo and a lanyard, not a conversation. Gated content generates contacts who never had budget. The channels that scale are the channels your ideal buyer has learned to ignore.
- P: What senior leaders still say yes to is a small, relevant room and a question worth their evening.

**New**
- Eyebrow: The problem (unchanged)
- H2: Your buyers stopped answering. (unchanged)
- Lede: The people you most need to reach, the C-suite and their direct reports, are the hardest audience to get in front of. They screen calls, delete cold email and scroll past the ads.
- P: A stand at another crowded conference buys you a logo and a lanyard, not a conversation. Gated content brings in contacts who were never going to buy. The channels that scale are the ones senior buyers have learned to ignore.
- P: What they still say yes to is a small room of genuine peers and a question worth their evening.

**Why:** This section already works, so it only gets a tighter edit. "Hardest audience in the market" was an unprovable superlative. The last line now sets up the new H1.

### 3. The shift (02)

**Current**
- Eyebrow: The shift
- H2: Trust is built in rooms, not inboxes.
- Lede: Enterprise decisions move on relationships and peer conviction. A senior buyer will give an hour to a table of equals long before they give a minute to a demo.
- P: Convene X convenes that table. We bring together a curated group of the exact leaders you want to know, around a theme that matters to them, and we position you as the host of the conversation rather than the seller in the room.
- P: You leave with relationships that cold outreach could never open, and a reason for them to take your next call.

**New**
- Eyebrow: The shift (unchanged)
- H2: Trust is built in rooms, not inboxes. (unchanged)
- Lede: Enterprise decisions move on relationships and peer trust. A senior buyer will give an evening to a table of equals long before they'll sit through a demo.
- P: We build that table. We invite a small group of the leaders you want to know, set a theme that matters to them, and run the evening so you're the host of the conversation, not the seller in the room.
- P: You get unhurried time with the right people and a first-hand view of the problems they're working on. No badge scans and no lead list, just a conversation that was worth having.

**Why:** "Relationships that cold outreach could never open" and "a reason for them to take your next call" promised an outcome. The new close describes what the host actually gets on the night.

### 4. Formats

**Current**
- Eyebrow: What you can sponsor
- H2: Three ways to own the room.
- Intro: Every format is private, curated, and built around your ideal customer profile. You choose the audience and the question. We design the evening and put your brand at the centre of it.
- Dinner card: *Executive Dinners · In person* / H3: Host a table of your ICP. / An invitation-only London dinner for ten senior leaders, curated to your target audience, with you as host of an off-the-record conversation.
- Roundtable card: *Virtual Roundtables · Digital* / H3: Convene peers across markets. / A moderated, closed-door discussion that reaches your ICP in the UK and US at once, built for peer exchange and warm follow-up, not a pitch.
- Webinar card: *Executive Webinars · Broadcast* / H3: Lead the agenda at scale. / A professionally produced session that positions your leaders as the authority on the topic your buyers care about, with a qualified, senior audience.

**New**
- Eyebrow: What you can sponsor (unchanged)
- H2: 3 ways to host the room.
- Intro: Every format is private, invitation-only and built around your ideal customer profile. You agree the audience and the question with us. We invite the guests, design the format and run it on the day.
- Dinner card: *Executive Dinners · In person* / H3: Host a table of your ICP. / An invitation-only London dinner for 10 to 25 senior leaders who match your profile, with you hosting an off-the-record conversation.
- Roundtable card: *Virtual Roundtables · Digital* / H3: Convene peers across markets. / A moderated, closed-door discussion for 6 to 12 senior leaders across the UK and US, built for peer exchange, not a pitch.
- Webinar card: *Executive Webinars · Broadcast* / H3: Put your experts on the agenda. / A professionally produced session on a topic your buyers care about, led by your experts, aiming for 25 to 50 senior registrations.
- "Explore →" links: unchanged.

**Why:** Fixes the dinner size (10 to 25), drops "warm follow-up" and "at scale", and gives each format its real size from the brand brief. "Own the room" didn't fit a page that says the host shouldn't dominate the room. "Three" becomes "3" (numbers as digits).

### 5. How it works (03)

**Current**
- Eyebrow: How it works
- H2: From ICP to pipeline, in four moves.
- 1. **Build your room.** We agree the exact seniority, sectors, and accounts worth an evening of your budget.
- 2. **We curate the room.** Our team invites and confirms a table of that audience, and shapes the question that earns their time.
- 3. **You host the conversation.** On the night, your brand hosts. We handle venue, table composition, pacing, and flow.
- 4. **Warm pipeline follows.** You leave with real relationships and permission for the next conversation, not a stack of cold leads.
- Button: Build Your Room

**New**
- Eyebrow: How it works (unchanged)
- H2: From brief to room, in 4 steps.
- 1. **Agree the room.** Together we set the seniority, sectors and accounts worth an evening of your budget.
- 2. **We invite the guests.** Our team invites and confirms senior leaders who match that profile, and shapes the question that earns their time. You sign off the guest list.
- 3. **You host the conversation.** On the day, your brand hosts. We handle the venue or platform, the seating, the pacing and the moderation.
- 4. **The next step is yours to earn.** You've spent real time with the right people. Any follow-up happens at their pace, which is why it counts for more than a badge scan.
- Button: Build Your Room (unchanged)

**Why:** Removes both pipeline lines. Step 4 also implied guests give "permission" for follow-up, which we can't promise. It adds the guest-list sign-off, which is our clearest point of difference. Step 3 now covers virtual formats as well as dinners.

### 6. Band: proof (the house-rule breach)

**Current**
- Eyebrow: Proven at enterprise level
- H2: A founder who has done this before.
- P: Before establishing Convene X Events, our founder spent several years designing and delivering senior-level events and executive programmes for large enterprise organisations, achieving consistent results throughout his career.
- Chips: Senior-level audiences / UK and US reach / Discreet, invitation-only delivery
- Button: Book Exploratory Call

**New**
- Eyebrow: Experience in the room
- H2: A team that's done this before.
- P: Before establishing Convene X Events, our founding team spent several years in previous roles designing and delivering senior-level events and executive programmes for large enterprise organisations. That experience shapes every room we build: who's invited, how the question is framed and how the evening runs.
- Chips: unchanged.
- Button: unchanged.

**Why:** Replaces the reference to one individual ("our founder", "his career") with team framing in previous roles, per the house rule. Cuts "achieving consistent results", an unverifiable outcome claim. There are no event counts, per Freya's ruling. "Proven at enterprise level" overclaimed for a company that hasn't run its own first event yet.

### 7. The audience (04)

**Current**
- Eyebrow: The audience
- H2: The seniority you cannot cold-email.
- Lede: Every guest is selected, not registered. You sit with the exact level of buyer your sales team struggles to reach.
- P: We convene chief officers, vice presidents, and senior directors across financial services, cybersecurity, IT and technology, procurement, and marketing, in London and across the UK and US.
- Chips: Financial services / Cybersecurity / IT & technology / Procurement / Marketing

**New**
- Eyebrow: The audience (unchanged)
- H2: The seniority you can't cold-email.
- Lede: Every guest is invited and vetted against the profile you agree with us. You sit with the level of buyer your sales team struggles to reach.
- P: For dinners and roundtables, that means Director level and above: chief officers, vice presidents and directors across financial services, cybersecurity, IT and technology, procurement and marketing. Webinars are open to Senior Manager level and above. We invite guests from London and across the UK and US.
- Chips: unchanged.

**Why:** States the seniority bar exactly as the brand brief sets it (Director+ for dinners and roundtables, Senior Manager+ for webinars). The old copy implied every format was C-suite and VP only. Uses contractions throughout.

### 8. Further reading (Kai, added 10 Nov)

**Current:** Eyebrow "Further reading", H2 "Worth reading before you host.", cards linking 8986 (`/conference-sponsorship-enterprise-b2b/`) and 8985 (`/senior-executives-say-no-to-events/`).

**New:** No change. Keep the block exactly as it is, including the `<!-- FURTHER READING (added 2026-11-10, indexing fix B2) -->` comment, which is the rollback marker.

**Why:** The copy is clean and the block is part of indexing fix B2.

### 9. FAQ

**Current**
- Eyebrow: Before you ask / H2: The questions sponsors ask first.
- **What exactly does a sponsor get?** You get the room. We curate and confirm an audience of your ideal customer profile, design the format and the theme around your goals, and position your brand as the host. You leave with senior relationships and warm follow-up, not a list of cold contacts.
- **Who is actually in the room?** Senior decision-makers only. Chief officers, vice presidents, and senior directors across financial services, cybersecurity, IT, procurement, and marketing. Every guest is invited and vetted against the profile we agree with you, in the UK and US.
- **Is this a pitch slot?** No. These rooms work precisely because no one is being sold to. You host a genuine conversation on a topic your buyers care about. The trust that builds is what earns your next meeting.
- **In person or virtual?** Both. Executive dinners are hosted in person at leading London venues. Virtual roundtables and webinars reach your audience across the UK and US in a single session.
- **How do we start?** Build your room with us or book an exploratory call. We will shape the audience, the format, and the question, then design the room around it. You begin with context, not commitment.

**New** (eyebrow and H2 unchanged; 2 questions added, marked NEW)
- **What exactly does a sponsor get?** The right people in the room and a conversation worth having. We invite senior leaders who match the profile you agree with us, design the format and theme around your goals, and position your brand as the host. You sign off the guest list. We don't sell lead lists: what happens after the event is down to the conversation.
- **Who is actually in the room?** Senior decision-makers who match your profile. That's Director level and above for dinners and roundtables, and Senior Manager and above for webinars, across financial services, cybersecurity, IT, procurement and marketing in the UK and US. Every guest is invited and vetted.
- **How many guests are there? (NEW)** Executive dinners seat 10 to 25 guests and virtual roundtables 6 to 12, small enough for a real conversation. Webinars aim for 25 to 50 registrations.
- **Is this a pitch slot?** No. These rooms work because nobody's being sold to. You host a genuine conversation on a topic your buyers care about, and a host who pitches loses the room.
- **In person or virtual?** Both. Executive dinners are held in person in private dining rooms in London. Virtual roundtables and webinars bring together senior leaders from across the UK and US in one session.
- **How long does it take to set up? (NEW)** Allow 12 weeks from kick-off: about 2 weeks to plan and 10 to invite and confirm the right guests. Anything faster tends to fill seats with the wrong people.
- **How do we start?** Book an exploratory call. It's a conversation about your audience and goals, not a pitch. If you'd like to sketch the room first, use Build Your Room.

**Why:** Removes "warm follow-up" and "earns your next meeting" (outcome promises). Adds the 2 questions a host asks before booking a call (room size, lead time), using figures from the brand brief. "Leading London venues" was an unverifiable superlative. The last answer now points to the primary CTA. **Callum:** suggest FAQPage schema for these 7 Q&As, matching the visible text word for word.

### 10. Final CTA

**Current**
- H2: Let us build your room.
- P: Tell us who belongs at the table, and we will design the evening around it, the format, the guest list, and the question worth asking. Begin with context, not commitment.
- Buttons: Build Your Room (primary) / Book Exploratory Call (alt)

**New**
- H2: Let's build your room.
- P: Tell us who belongs at the table. We'll design the format, the guest list and the question worth asking around them. Start with a conversation, not a commitment.
- Buttons, **recommended swap:** Book Exploratory Call (primary) / Build Your Room (alt)

**Why:** Contractions and a cleaner sentence (the old one stacked 4 commas). The button swap makes the brand brief's primary CTA the main action, matching the hero. Freya to confirm the swap. If it's declined, the copy still works with the current order.

### Not changed

- The hidden `cx-personal` personalisation `div`, the footer, the inline CSS and the script. The footer is shared site chrome and outside this brief.

---

## Couldn't verify / flags for reviewers

1. **Proof line wording.** `brand-voice.md` and `convenex-brain.md` aren't in this repo, so I couldn't check the exact approved website proof line (the agent notes say it reads "our founding team spent several years..."). I used "our team... in previous roles" per Nathan's brief. Felix to check it against brand-voice.md. **Felix: brand-voice.md isn't in this repo for me either. I aligned the line to the proof line in my review checklist ("our founding team spent several years..."). Freya to confirm against the vault copy.**
2. **Brand brief conflict.** `brand-brief.md` still lists "34 events in the last 18 months, 32 at or over capacity" as the approved proof claim. Freya's ruling bans event counts in public copy, so it's not used here. The brief needs updating, or the next writer will reuse the number. **Felix: resolved. `brand-brief.md` was updated on 10 Nov; event counts are banned and the claim is retired.**
3. **Call length vs link.** The brand brief calls it a 45-minute exploratory call, but the link slug is `cal.com/convenexevents/15min`. The new FAQ says "45-minute". Confirm the length, and whether the slug should change. **Felix: length removed from the FAQ ("Book an exploratory call."). Open with Nathan.**
4. **Webinar figures.** "25 to 50 registrations" and "Senior Manager+" come from the brand brief, and "professionally produced" is from the current page. I didn't check them against the webinar service page (9413).
5. **Roundtable size (6 to 12)** and the **12-week timeline** (2 weeks to plan, 10 to recruit) come from the brand brief. Not checked against the service pages.
6. **"You sign off the guest list"** is in the brand brief's sponsor-hosted model. Confirm it holds for every format, including webinars.
7. **UK and US recruitment reach** is carried over from the current page. I didn't verify it operationally.
8. **Dinner size elsewhere.** I fixed "ten" on this page only. I didn't check whether other pages (for example 9415 Private Executive Dinners) still say 10 or another number. Worth a site search by Callum.
9. **Linked post 8986** (in Further reading) says "Conference sponsorship at scale produces low-quality pipeline" and "relationship-led pipeline". That's comparison language, not a promise to hosts, but Felix may want to look at it, given this page now avoids pipeline framing.
10. **For Kai, outside this copy brief:**
    - The webinar card image is `convene-x-champagne-reception.jpg`, but its alt text says "Executive webinar broadcast". The alt text doesn't describe the image.
    - The footer newsletter form doesn't submit anywhere. The script shows "Thanks, you are subscribed" without sending the email. This needs fixing or removing, site-wide.
11. **URL.** The keyword isn't in the URL (`/sponsor/`). I'm not suggesting a change, because the page is seen in search and a 301 would cost more than it gains.
