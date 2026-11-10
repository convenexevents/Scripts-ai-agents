# Rewrite: /sponsor/ (page 10806)

Status: **DRAFT for Felix's review.** Nothing has been changed on the live site.
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
- P: Before establishing Convene X Events, our founding team spent several years, in previous roles, designing and delivering senior-level events and executive programmes for large enterprise organisations. That experience shapes every room we build: who's invited, how the question is framed and how the evening runs.
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

1. **Proof line wording.** `brand-voice.md` and `convenex-brain.md` aren't in this repo, so I couldn't check the exact approved website proof line (the agent notes say it reads "our founding team spent several years..."). I used "our team... in previous roles" per Nathan's brief. Felix to check it against brand-voice.md.
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
