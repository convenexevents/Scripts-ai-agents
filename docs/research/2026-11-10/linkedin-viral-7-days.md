# LinkedIn: top-performing posts, 3 to 10 November 2026

**Prepared by:** Theo (Social & LinkedIn), for Nathan. Feeds Leo's week-long social campaign plan.
**Date:** 10 November 2026
**Status:** Internal research only. Nothing has been posted, commented on, liked or queued in Buffer.

---

## 1. Method, cost and how far to trust this

**Tool:** Apify actor `harvestapi/linkedin-post-search` (LinkedIn Post Search Scraper, no cookies). I picked it because it had the most users of the LinkedIn post-search actors (about 42,500 total and 11,600 monthly), a 4.95 rating, pay-per-result pricing at $0.002 per post, and a "past week" date filter.

**Runs (all on 10 Nov 2026, around 13:10 UTC):**

| Run | Queries | Window | Posts returned |
|---|---|---|---|
| 1 | executive dinner, corporate events, virtual roundtable, B2B webinar, event marketing, event ROI, roundtable senior leaders, events are broken, peer learning executives, field marketing events | past week | 250 |
| 2 | executive roundtable, dinner series pipeline, conference sponsorship, trade show booth, webinar attendance, in-person events pipeline, event marketer, networking senior leaders, intimate events, CMO events budget | past week | 250 |
| 3 | roundtable, event strategy, networking event, conference ROI, executive community, hosted dinner, webinars, conferences | past week | 100 |
| 4 (benchmark only) | executive dinner, event ROI, events are broken, virtual roundtable, B2B webinar | past month | 100 |

**Cost:** about 700 posts at $0.002, so roughly **$1.40 in total** (actor start fees are fractions of a cent). Each run had a spend cap of $0.30 to $1.00. Firecrawl wasn't needed: the Apify data covered the window directly.

**Ranking:** I used weighted engagement = reactions + (2 x comments) + (3 x reposts), because comments and reposts do more for distribution than reactions do. 562 unique posts fell in the 7-day window.

**Caveats (please read before using the numbers):**
- **The 7-day data is real but thin on topic.** LinkedIn keyword search matches loosely. The biggest posts it returned for "events are broken" were a security start-up's funding announcement, an embassy statement of mourning and a post about leaving academia, so I removed them by hand. Only 74 of the 562 posts scored 40 or more, and about 25 of those were on our topics. The top 20 below is the on-topic set, not the raw top 20.
- **Engagement is a snapshot** taken at about 13:10 UTC on 10 Nov. Posts from 9 and 10 Nov are still gathering engagement, so they're understated.
- **Impressions and follower counts weren't captured** (the scraper doesn't return follower counts for individuals). A large creator's audience inflates their numbers, so read "why it worked" with that in mind.
- **The sample leans American.** Most high-engagement authors are US-based, so posting times reflect US mornings.
- **No numbers have been invented.** Every figure is from the scraper output. Where a post quotes its own statistics (for example "$10B in ARR" or "100+ qualified demos"), that's the author's claim, not something we've checked.
- **30-day widening:** I didn't need it for the top 20, which is all 7-day data. Run 4 (past month) is used only as a labelled benchmark in section 4.

---

## 2. Top 20 on-topic posts, 3 to 10 November 2026

Ordered by weighted engagement. "Format" is from the scraper: text, single image, multi-image (n images), document (carousel), video or poll. All times are UTC, which is also UK time (GMT) in November.

### 1. "Men have been opening doors for each other for generations."
- **Author:** Individual. Founder and CEO of a US non-profit, with a large public profile (Reshma Saujani).
- **URL:** https://www.linkedin.com/posts/reshma-saujani_men-have-been-opening-doors-for-each-other-activity-7525575081104801792-4WqS
- **Date:** Mon 9 Nov, 15:08
- **Reactions / comments / reposts:** 1,404 / 88 / 2
- **Format:** Single image, about 100 words
- **Topic fit:** Adjacent: senior-leader networking and private dinners as access
- **Why it worked:** The hook names an unfairness everyone recognises ("deals get made over dinner... in rooms most women never see"), then pays it off with a real, named table. It's short, emotional and gives people a cause to back, from an author with a very large following.
- **How we'd improve it in our voice:** Take the idea that who gets a seat at the table is a decision, not an accident, and make it about curation. A calm post on how a guest list gets built and signed off, and why "who's in the room" is the event. No cause-marketing borrowed from others, no names.

### 2. "I was at a dinner last week with about 20 CROs, CMOs, and VPs of Sales, RevOps, and Marketing collectively representing about $10B in ARR."
- **Author:** Individual. CEO of a revenue-leader community and podcast host (Sam Jacobs, Pavilion).
- **URL:** https://www.linkedin.com/posts/samfjacobs_i-was-at-a-dinner-last-week-with-about-20-activity-7524489592729878528-tQYJ
- **Date:** Fri 6 Nov, 15:15
- **Reactions / comments / reposts:** 975 / 206 / 24
- **Format:** Text only, about 390 words
- **Topic fit:** Core: executive dinners, event ROI, in-person as demand generation
- **Why it worked:** It opens on an insider scene with a specific headcount and seniority, then gives one answer from the room ("PIPELINE"). It argues in-person and community are "the only thing that works right now" and backs it with rough unit economics (dinner cost against opportunities). It's polarising ("legacy SaaS playbooks are dead") and very quotable, and the comment count shows it started an argument. **This is the most relevant high performer in the set.**
- **How we'd improve it in our voice:** Keep the shape (one room, one question, one answer) and drop the shouting capitals and the hype. Our version is about why that room works: the guests were peers, nobody pitched, and someone chose the list. We don't have a dinner of our own to describe yet, so use the format argument, not a fake scene.

### 3. "what's the difference between events and experiential?"
- **Author:** Individual. Experiential producer (Juliette Paige).
- **URL:** https://www.linkedin.com/posts/juliettepaige_whats-the-difference-between-events-and-activity-7524559685136334848-3pAZ
- **Date:** Fri 6 Nov, 19:53
- **Reactions / comments / reposts:** 481 / 37 / 9
- **Format:** Single image, about 210 words
- **Topic fit:** Core: event marketing and ROI
- **Why it worked:** It defines a term people argue about ("events are one-way, experiential is two-way") and invents a new metric (ROE, return on experience). It ends with a real request for the reader's own definition. Definitional posts invite correction, and correction is comments.
- **How we'd improve it in our voice:** Our own definition post: "An executive dinner isn't a smaller conference. It's a different format." Two-way conversation, peers, no stage. Skip the new acronym, because "ROE" invites eye-rolls from finance readers.

### 4. "SMALL GATHERING. POWERFUL WOMEN. LASTING INSPIRATION."
- **Author:** Individual. Healthcare futurist and keynote speaker (Philippe Gerwill).
- **URL:** https://www.linkedin.com/posts/philippegerwill_womenempowerment-meaningfulconnections-dubai-activity-7525074290854043648-Msnc
- **Date:** Sun 8 Nov, 05:58
- **Reactions / comments / reposts:** 196 / 20 / 3
- **Format:** Multi-image (7), about 230 words
- **Topic fit:** Adjacent: small events and intimate gatherings
- **Why it worked:** Mostly the author's audience and the photos, plus a gratitude tone. The closing question ("the topic, the people, or the conversations you never expected to have?") is easy to answer.
- **How we'd improve it in our voice:** Keep the closing question, which is good, but put it behind a sharper idea. Something like: "What people remember from a small event is rarely the agenda." No stacked capitals, no adjective triplets (our brief bans them).

### 5. "Assessing ROI at a conference is a lot different than at a curated event."
- **Author:** Individual. Consultant on deal flow and partnerships, former SaaS marketing leader (Alexis Rivera Scott).
- **URL:** https://www.linkedin.com/posts/alexisriverascott_assessing-roi-at-a-conference-is-a-lot-different-activity-7524498110929063936-X9FI
- **Date:** Fri 6 Nov, 15:49
- **Reactions / comments / reposts:** 206 / 11 / 1
- **Format:** Single image, about 220 words
- **Topic fit:** Core: event ROI, curated against open events
- **Why it worked:** It ranks event types (invite-only, then niche small, then niche open) from the author's own experience as a marketing leader. The ranking is simple and easy to save. It's almost exactly our wedge, said by someone else.
- **How we'd improve it in our voice:** Make the ranking ours and make it about the guest list, not the author's network. "Director+ means Director+." End on a conversation, not "my inbox is open".

### 6. "I want to start speaking more"
- **Author:** Individual. B2B influencer-marketing specialist (Ifeoluwa Akinyemi).
- **URL:** https://www.linkedin.com/posts/ifeoluwaakin_frominsidemycampaigns-activity-7525580904635858944-quOR
- **Date:** Mon 9 Nov, 15:31
- **Reactions / comments / reposts:** 76 / 29 / 2
- **Format:** Single image, about 100 words
- **Topic fit:** Adjacent: webinars, panels, speakers
- **Why it worked:** A plain, honest ask with 3 specific talk topics. Comments come from people offering platforms or tagging hosts. A high comment-to-reaction ratio (about 38%).
- **How we'd improve it in our voice:** This isn't one to copy for a company page. The lesson is that a specific, low-friction ask gets comments. Our version: "What should a senior table in [sector] be talking about in Q1?" It's a real question that also tells us what our audience wants.

### 7. "The misconception that field marketing is just a 'nice-to-have' is officially a thing of the past."
- **Author:** Individual. Sponsorship director at a large fintech event series (Pauline Jorge, Money20/20 Asia).
- **URL:** https://www.linkedin.com/posts/pauline-jorge_money2020asia-money2020australia-activity-7523594917378543616-NYY_
- **Date:** Wed 4 Nov, 04:00
- **Reactions / comments / reposts:** 90 / 22 / 0
- **Format:** Multi-image (11), about 175 words
- **Topic fit:** Core: event marketing value
- **Why it worked:** It validates the people doing the work ("your work matters"), and event marketers love to share that. Photos from a live event week add proof.
- **How we'd improve it in our voice:** Validation without the siren emoji and "magic happens". A more specific version: "Field marketing teams are being asked for pipeline, not photos. Here's what a senior room gives you that a booth can't." Then no promise of leads, in line with the brief.

### 8. "This day was the day I realized networking events were completely overrated"
- **Author:** Individual. B2B sales trainer (Kimberly Price).
- **URL:** https://www.linkedin.com/posts/kimberly-price1_this-day-was-the-day-i-realized-networking-activity-7525668475470548994-cJ_s
- **Date:** Mon 9 Nov, 21:19
- **Reactions / comments / reposts:** 104 / 7 / 0
- **Format:** Single image, about 135 words, numbered list of 5
- **Topic fit:** Core: "events are broken" take
- **Why it worked:** A blunt contrarian opener plus a 5-point list. Readers who've sat through a bad networking event agree, and the list is quick to read.
- **How we'd improve it in our voice:** Agree with the frustration and move it on: networking events don't fail because people dislike meeting. They fail because nobody chose who's in the room. That keeps the contrarian energy and points to our wedge without sneering at anyone.

### 9. "I don't choose events by the agenda anymore. I choose them by the hallway."
- **Author:** Individual. Consumer brand CEO and operator (Beatriz Nahuz).
- **URL:** https://www.linkedin.com/posts/beatriznahuz_ecomtherapy-eventstrategy-creatorcommerce-activity-7525535754412883968-HhDp
- **Date:** Mon 9 Nov, 12:32
- **Reactions / comments / reposts:** 75 / 17 / 0
- **Format:** Single image, about 190 words, 5-point scorecard
- **Topic fit:** Core: event ROI and attendee perspective
- **Why it worked:** **Strongest hook in the set.** A two-beat line with a reversal. The body is a saveable scorecard ("cost per real conversation, not cost per badge").
- **How we'd improve it in our voice:** Write our own guest-side checklist: what a senior leader checks before giving up an evening (who else is coming, will anyone pitch, is it under Chatham House, how many seats). It's useful to delegates and quietly sells the format to hosts.

### 10. "Big News: Today we're launching Sponsor ROI as part of Bizzabo's OS"
- **Author:** Individual. Co-founder and CEO of an event-tech platform (Eran Ben-Shushan, Bizzabo).
- **URL:** https://www.linkedin.com/posts/eranbenshushan_big-news-today-were-launching-sponsor-roi-activity-7523448668994138112-VQSM
- **Date:** Tue 3 Nov, 18:19
- **Reactions / comments / reposts:** 78 / 4 / 5
- **Format:** Text with link, about 190 words
- **Topic fit:** Core: sponsor ROI
- **Why it worked:** Mostly network and team support for a launch (few comments). The useful line is the problem statement: "sponsors bought the booth, sent their team, and hoped it was worth it."
- **How we'd improve it in our voice:** Don't do launch posts in this style. Do use the sponsor pain ("hoped it was worth it") as an opener for a sponsor-reader post about knowing who'll be in the room before you commit, because the host signs off the guest list.

### 11. "Last week, I was on a call with a restaurant where we had to jump through hoops to get Champagne sabering approved."
- **Author:** Individual. Founder of a US executive-dinner practice (Ami Arad, "Dinner-Led Growth"). **Closest like-for-like competitor voice in the set.**
- **URL:** https://www.linkedin.com/posts/amiarad_last-week-i-was-on-a-call-with-a-restaurant-activity-7523392682572906496-ZkLG
- **Date:** Tue 3 Nov, 14:36
- **Reactions / comments / reposts:** 61 / 10 / 0
- **Format:** Text, about 90 words. It mentions a 40-second clip, but the scraper didn't detect native video.
- **Topic fit:** Core: executive dinners, behind the scenes
- **Why it worked:** A specific behind-the-scenes detail (the sabering request) and a clear point: set the tone in the first 10 minutes so strangers relax.
- **How we'd improve it in our voice:** The idea of the first 10 minutes is strong and ours to explore without the theatre. A calm post on how a well-run table starts: introductions, the opening question, why the host speaks last. Better as a process post than a stunt. (Flag for Nadia: worth tracking as a competitor.)

### 12. "Are you noticing a shift in how events are being run this autumn?"
- **Author:** Individual. UK-based connector and partnership strategist (Penny Triantafillou).
- **URL:** https://www.linkedin.com/posts/pennytriantafillou_are-you-noticing-a-shift-in-how-events-are-activity-7523755505626939392-Cc1d
- **Date:** Wed 4 Nov, 14:38
- **Reactions / comments / reposts:** 24 / 19 / 3
- **Format:** Text, about 155 words
- **Topic fit:** Core: in-person against virtual
- **Why it worked:** Comments are nearly equal to reactions. A balanced, inclusive point ("every time we choose an event format, we're also deciding who can realistically attend") gives readers room to share their own experience.
- **How we'd improve it in our voice:** Our brief bans rhetorical-question openers, so lead with the point instead: "Choosing a format is choosing who can come." Then explain why we run both dinners and virtual roundtables. This is the best brief for a virtual-roundtable post.

### 13. "I received ~150 cold emails leading up to Money 20/20 last month. I trashed 95% of them."
- **Author:** Individual. Event strategy and pipeline marketer (Nausheen Ahmad).
- **URL:** https://www.linkedin.com/posts/nausheen-ahmad_i-received-150-cold-emails-leading-up-to-activity-7524153523643604993-fM7F
- **Date:** Thu 5 Nov, 16:59
- **Reactions / comments / reposts:** 41 / 9 / 1
- **Format:** Text, about 240 words, 3-point list
- **Topic fit:** Core: event marketing and outreach
- **Why it worked:** A receipt-style hook (her own numbers), written from the buyer's side, with practical fixes. Sales and marketing readers both feel it.
- **How we'd improve it in our voice:** The guest's view of a bad invitation. "Senior leaders don't ignore invitations. They ignore invitations that could have gone to anyone." Don't invent inbox counts. If we want a number, ask Nathan for a real one or use [CONFIRM THIS].

### 14. "Last night was a special milestone for us as we officially introduced The DC Collective at our first Executive Dinner in Frankfurt!"
- **Author:** Individual. Co-founder of a data-centre leadership collective (Rebecca Sewell).
- **URL:** https://www.linkedin.com/posts/rebecca-meta-u-coaching_thedccollective-datacentres-collaboration-activity-7524503348738166784-xymK
- **Date:** Fri 6 Nov, 16:09
- **Reactions / comments / reposts:** 36 / 7 / 4
- **Format:** Multi-image (5), about 140 words
- **Topic fit:** Core: executive dinners, launch recap
- **Why it worked:** Photos and co-founder tags, so the tagged people and their networks engaged. A typical "milestone" post: warm, but a weak hook.
- **How we'd improve it in our voice:** When our first event happens, the recap should lead with the question the table discussed (no attendee names, no photos without consent), not with "special milestone". Until then, this is a format to avoid.

### 15. "Executive education is changing in the age of AI."
- **Author:** Individual. Keynote speaker and future-of-work researcher (Dr Mansoor Soomro).
- **URL:** https://www.linkedin.com/posts/mansoorsoomro_executiveeducation-ai-learning-activity-7524477682538086400-q4w4
- **Date:** Fri 6 Nov, 14:27
- **Reactions / comments / reposts:** 20 / 21 / 0
- **Format:** Single image, about 240 words
- **Topic fit:** Adjacent: peer learning
- **Why it worked:** It concedes 3 points to AI and then holds 2 that AI can't replace: peer learning and experience. Comments outnumber reactions, so the argument landed with a debating crowd.
- **How we'd improve it in our voice:** The strongest line is "sitting across the table from another leader who sees the same problem through a completely different lens". Our own take: AI can answer a question, but it can't tell a CFO what happened when the person two seats down made the same call. Lead with that, not with "is changing in the age of AI" (a generic opener).

### 16. "I'm hiring for our next BDR. In person events have become the single biggest pipeline driver for Echelon."
- **Author:** Individual. Founding growth lead at an AI start-up (George Goodfellow).
- **URL:** https://www.linkedin.com/posts/george-goodfellow_im-hiring-for-our-next-bdr-in-person-activity-7524176912135593984-_5or
- **Date:** Thu 5 Nov, 18:32
- **Reactions / comments / reposts:** 33 / 7 / 2
- **Format:** Single image, about 105 words
- **Topic fit:** Core: in-person events and pipeline (inside a hiring post)
- **Why it worked:** A hiring post with a proof line ("3 days at Gartner, 100+ qualified demos", the author's claim). Hiring posts get reposts from people's networks.
- **How we'd improve it in our voice:** Not one for us to copy. It's evidence that B2B buyers now say "in-person = pipeline" in public, which supports our sponsor-reader posts. Cite the trend, not this company.

### 17. "In person events... The best way to break through the noise."
- **Author:** Individual. Former start-up co-founder, now in AI tools at a large CRM vendor (Keegan Otter).
- **URL:** https://www.linkedin.com/posts/keeganotter_events-corporategifting-gtmtactic-activity-7524187266953437184-ORKw
- **Date:** Thu 5 Nov, 19:13
- **Reactions / comments / reposts:** 35 / 8 / 0
- **Format:** Single image, about 90 words
- **Topic fit:** Core: event ROI, executive dinners
- **Why it worked:** A short "if I were a CRO again" thought: put the AI savings into dinners and events, because "the ROI has always been there... it just takes effort and planning".
- **How we'd improve it in our voice:** The idea of AI savings moving into human rooms is a good one for a Monday insight post. Our angle: as outbound gets automated, the scarce thing is a room of peers who chose to come. Don't name vendors.

### 18. "The power of relationships."
- **Author:** Individual. Events and marketing coordinator for an education summit (Giorgia Burgess).
- **URL:** https://www.linkedin.com/posts/giorgia-burgess-cmktr_the-power-of-relationships-now-that-outstanding-activity-7525517508997476354-5_nv
- **Date:** Mon 9 Nov, 11:19
- **Reactions / comments / reposts:** 34 / 8 / 0
- **Format:** Multi-image (10), about 260 words
- **Topic fit:** Adjacent: networking, post-event reflection
- **Why it worked:** Photos from a yacht evening and a dinner, plus a reflective tone. The engagement comes from attendees.
- **How we'd improve it in our voice:** The useful line is "some of the best conversations happen when you're not trying to have a business conversation at all". That's the no-pitch wedge. Use it as the payoff of a post, never as a three-word hook.

### 19. "Tip from a CEO to all the Marketing leaders out there. When you bring event results to your CEO, event week is the least useful part of the story."
- **Author:** Individual. Co-founder and CEO of a revenue-AI company (Gorish Aggarwal, Sybill).
- **URL:** https://www.linkedin.com/posts/gorish_tip-from-a-ceo-to-all-the-marketing-leaders-activity-7524515962750971904-BpAE
- **Date:** Fri 6 Nov, 17:00
- **Reactions / comments / reposts:** 24 / 12 / 0
- **Format:** Text, about 190 words, 3-point list
- **Topic fit:** Core: event ROI
- **Why it worked:** An authority callout ("from a CEO") plus a counter-intuitive claim (event week is the least useful data), with a concrete fix: show meetings per week after the event, by stage. It's practical and easy to save.
- **How we'd improve it in our voice:** A sponsor-reader post on measuring a dinner 6 weeks later, not on the night. Careful: we never promise outcomes, so frame it as "what to look at", not "what you'll get".

### 20. "I've been running webinar programs for almost a decade, and one thing that still surprises people is just how much pipeline a well-executed webinar strategy can generate."
- **Author:** Individual. Demand generation leader (Rachel Hentges).
- **URL:** https://www.linkedin.com/posts/rachel-hentges_ive-been-running-webinar-programs-for-almost-activity-7525014985597587457-h2Og
- **Date:** Sun 8 Nov, 02:03
- **Reactions / comments / reposts:** 16 / 15 / 0
- **Format:** Text, about 275 words, arrow list
- **Topic fit:** Core: B2B webinars
- **Why it worked:** Experience-based credibility plus 4 lessons (consistency, segmentation, think beyond the event, measure pipeline). It ends with a direct question, and the comment ratio is high.
- **How we'd improve it in our voice:** The hook is too long to survive the "see more" cut. Our webinar angle: "A webinar with the wrong 50 people is worse than one with the right 15." That pairs with our Senior Manager+ gate for webinars.

### High-engagement posts excluded (keyword matches, but not on topic)
For transparency, these ranked high in the raw data and were removed: a security start-up's $15M launch (673 / 364 / 46), an embassy condolence post (1,101 / 18 / 64), a post on leaving academia (701 / 29 / 38), and a run of event-marketing **career and hiring posts**: a new field-marketing role announcement (370 / 79 / 0), an event marketer open to work after redundancy (307 / 51 / 27), a list of remote events jobs (377 / 25 / 19), and a CMO hiring for an events team (194 / 14 / 12). **Pattern worth knowing:** in the event-marketing feed this week, career posts out-performed opinion posts. Event marketers are an active, supportive community on LinkedIn.

---

## 3. Patterns

### Hooks
- **A scene with a number beats a statement.** The best on-topic post opens on one room with a headcount and seniority (#2). The other receipt-style openers (#13's "150 cold emails", #16's "3 days at Gartner") also out-performed abstract openers of similar length.
- **Two-beat reversals are the most saveable.** "I don't choose events by the agenda anymore. I choose them by the hallway." (#9) The shape is short line, turn, payoff.
- **Contrarian takes on networking work, but sneering gets reactions, not comments.** #8 ("networking events were completely overrated") got 104 reactions and only 7 comments. The balanced or questioning posts (#12, #15, #20) got close to 1 comment per reaction.
- **Generic openers under-perform even from big accounts:** "SMALL GATHERING. POWERFUL WOMEN...", "The power of relationships.", "Big News: Today we're launching..."
- **Hooks that name the reader's role** ("Tip from a CEO to all the Marketing leaders") pull in that exact audience.

### Formats
- Top 20: **9 single image, 7 text only, 4 multi-image, 0 carousels or documents, 0 native video detected, 0 polls.**
- Across all 562 posts: single-image posts had a median weighted score of 9, against 4 for text-only and 4 for documents (only 16 documents, all low). **Carousels didn't feature on these topics this week.** That's a gap and a chance for us, not proof they don't work.
- The image is usually a real photo of the author or the room, not a designed graphic.

### Length
- Top 20 range from about 90 to about 390 words, with a median of about 190.
- Length isn't the driver: #1 is about 100 words and #2 is about 390. **One clear idea** is the common factor.
- Short paragraphs and white space throughout. Lists of 3 to 5 in about half of the top 20.

### Posting days and times (UTC = UK time in November)
- **Days:** Fri 6, Mon 4, Thu 3, Tue 2, Wed 2, Sun 2, Sat 0. Friday over-indexed this week. Small sample: treat it as a hint, not a rule.
- **Times:** 12 of the 20 went out between **11:00 and 17:00 UK** (morning on the US East Coast). The two biggest posted at about 15:00 UK.
- For a UK senior audience, test this against the playbook's 07:00 to 09:00 and 12:00 to 13:00 UK slots. Leo's plan should A/B these rather than assume.

### Topics that over-index
1. **In-person and community as the answer to pipeline pressure** (#2, #16, #17). This is the dominant B2B theme this week.
2. **Curated or invite-only against open conferences** (#5, #9). This is almost exactly our wedge, and nobody owns it in a calm UK voice.
3. **Networking is broken / networking done right** (#8, plus Junuz Jakupović on padel against networking breakfasts and Abby Wood on "god awful" events, both just outside the top 20).
4. **Proving event ROI after the event** (#3, #19, #10).
5. **Peer learning as the thing AI can't replace** (#15, and a UK peer-group chair post on "decisions you can't share with the team": 32 / 5 / 1, just outside the top 20).

### Author type
- **All 20 are individuals.** Across the pool, individual posts had a median score of 6 against 3 for company pages, and company-page posts on these topics hardly registered. **Implication for Leo:** the campaign's reach will depend on the founder's personal profile and host or partner reshares, with the company page as the archive. Company voice and personal voice stay separate drafts.

### Hashtags
- Most top posts use 0 to 2 hashtags. In the pool, posts with 3+ hashtags had the same or slightly lower median engagement than posts with fewer. Our 3 to 5 hashtag rule doesn't hurt, but it doesn't help either.

---

## 4. 30-day benchmark (labelled: past month, not the 7-day window)

From run 4, for context on what lasts beyond a week:
- Heike Young, a B2B content leader (21 Oct): "If I could tell every B2B company on the planet three things about webinars..." 107 / 69 / 4. Text, list of 3. This is the strongest webinar post of the month and suggests webinar opinion posts get comments.
- Sydney Gorski, chief of staff (14 Oct): "For nine years I lived and breathed live events..." 213 / 6 / 1. A personal story post about events.
- Kayla Drake, field marketing (15 Oct): "Your 2027 event calendar shouldn't be a copy/paste of 2026." 99 / 23 / 0. **Planning-season hook. Timely for November and December.**
- Annie Demenik, event strategy (26 Oct): "The event is over. But is the work really done?" 32 / 13 / 1. The post-event follow-up angle again.

---

## 5. Post-grader: top 5 (scored against the post-grader rubric; voice match is against our brand brief)

The scores rate each post's craft against our standard, not how well it performed. Audience size explains much of the gap between the two.

| # | Post | Hook (50%) | Curiosity (10%) | Emotion (10%) | Share (10%) | Voice match vs our brief (10%) | Polarity (5%) | Platform fit (5%) | Rule fails | **Grade** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | "Men have been opening doors for each other for generations." | 8 | 6 | 9 | 8 | 6 | 7 | 8 | 0 | **7.7** |
| 2 | "I was at a dinner last week with about 20 CROs, CMOs..." | 8 | 9 | 7 | 8 | 5 | 8 | 7 | 1 (dash) | **7.2** |
| 3 | "what's the difference between events and experiential?" | 6 | 6 | 5 | 6 | 5 | 7 | 8 | 1 (filler: "just") | **5.5** |
| 4 | "SMALL GATHERING. POWERFUL WOMEN. LASTING INSPIRATION." | 5 | 4 | 6 | 4 | 4 | 2 | 7 | 1 (4 hashtags) | **4.3** |
| 5 | "Assessing ROI at a conference is a lot different than at a curated event." | 6 | 6 | 5 | 7 | 6 | 7 | 6 | 1 (filler: "very") | **5.6** |

**Notes and top fixes per post (what we'd do differently, not rewrites of theirs):**

1. **Reshma Saujani (7.7).** Strong hook built on injustice, short and emotional. *Fixes:* (a) name what was discussed at the table, not only who hosted it, because it lacks substance; (b) a closing question would turn reactions into comments (88 comments on 1,404 reactions is low); (c) for our voice, drop the heart emoji and thank-you framing.
2. **Sam Jacobs (7.2).** The best idea in the set. *Fixes:* (a) the hook runs about 160 characters before the question, so it gets cut off on mobile; "20 revenue leaders. One question. One answer." would land inside the cut; (b) the shouting capitals ("WE MUST ACCEPT", "BOTTOM LINE") and jokes ("kissing babies", "$100 bills") are off-voice for us; (c) the unit economics are the author's own estimates, and we'd never publish figures like that without a source.
3. **Juliette Paige (5.5).** *Fixes:* (a) a question opener is weaker than stating the definition: "Events tell. Experiential listens." would be stronger; (b) "ROE" needs one concrete example; (c) the closing question is good, so keep that pattern.
4. **Philippe Gerwill (4.3).** *Fixes:* (a) the hook is a stack of 3 adjective-noun pairs with no tension, so replace it with one specific moment from the room; (b) the body is gratitude, not insight, so add 1 thing learned; (c) cut the hashtags, including the author's own name as a tag.
5. **Alexis Rivera Scott (5.6).** *Fixes:* (a) the hook states a difference without saying what it is: "A booth is a volume play. A curated room is a precision play." gives the point at once; (b) the ranking is the saveable asset, so make it a 3-line list near the top; (c) the closing "my inbox is open" turns insight into a pitch, so end on a question instead.

**Takeaway for our drafts:** the posts that performed best had a scene and a single clear claim. The posts that graded worst opened with labels or announcements. Every hook we ship should pass the first-3-words test and fit before the "see more" cut (about 110 to 140 characters on mobile).

---

## 6. 10 hook ideas for Convene X (original, for Leo's campaign week)

Written to our brief: calm, UK English, no exclamation marks, no rhetorical-question openers, no em dashes, no names, no invented numbers. Only the approved proof claim is used, with the team framing. Each is mapped to the viral-hooks category and the pattern from this research that it builds on. These are hooks only. Full posts go through Draft > Humanize > Felix > Freya > Nathan.

| # | Hook | Category | Built on | Reader | Suggested format |
|---|---|---|---|---|---|
| 1 | The best sponsored dinner is the one where the sponsor doesn't pitch. | Contrarian | The wedge, plus the curated-against-conference theme (#5, #9) | Would-be host | Text |
| 2 | A full room of the wrong job titles isn't a good event. It's an expensive one. | Negative frame | Sponsor pain, "hoped it was worth it" (#10) | Would-be host | Text |
| 3 | Networking events don't fail because people are tired of meeting. They fail because nobody chose the room. | Myth-buster | The "networking is broken" cluster (#8) | Both | Text |
| 4 | A virtual roundtable with 40 people on the call isn't a roundtable. It's a webinar with cameras on. | Contrarian | Format choice (#12), virtual roundtables of 6 to 12 | Both | Single image (table diagram) |
| 5 | Judge an executive dinner 6 weeks after it ends, not on the night. | Curiosity gap | Proving ROI after the event (#19) | Would-be host | Carousel: what to look at in weeks 1, 2, 4 and 6 (no promised outcomes) |
| 6 | Before a senior leader gives up an evening, they check 4 things. The menu isn't one of them. | Listicle / insider | The guest-side scorecard (#9) | Senior guest | Carousel (fills the format gap) |
| 7 | 12 weeks is the minimum for an executive dinner worth attending. Anything faster is filling seats. | Receipt / contrarian | The brief's 12-week angle, plus planning season (30-day benchmark) | Would-be host | Text |
| 8 | A senior leader can ask AI for a framework. They can't ask it what happened when the CFO two seats down made the same call. | Contrarian | Peer learning against AI (#15) | Senior guest | Text |
| 9 | Across their careers, our team has run 34 events in the last 18 months, 32 of them at or over capacity. The guest list did more of that work than the venue. | Receipt (approved claim only) | Scene-plus-number hooks (#2, #13) | Would-be host | Single image (real photo only, with consent) |
| 10 | Most event invitations land in a senior inbox looking like they could have gone to anyone. That's why they're ignored. | Negative frame | The inbox-side view (#13) | Would-be host | Text, with a question at the end for comments |

**Notes on use:**
- Hook 9 must keep the approved wording exactly. The second sentence is an opinion, not a measured result. Felix should check it, and it can be cut if the team prefers the claim on its own.
- Hooks 5 and 6 are the carousel candidates. Nobody on these topics posted a document this week, so they give us a format to ourselves. Build them in Canva to the brand kit.
- Close each post with a real question (the comment-heavy posts in this set all did) and put the booking link in the first comment, per the brief.
- Mix the reader across the week: 6 host-facing, 2 guest-facing and 2 for both, which avoids an all-promotional feed.
- Founder-profile versions should be separate drafts in the personal voice. Don't blur the two.

---

## 7. Hand-offs
- **Leo:** sections 3 and 6 are the inputs for the week plan. Suggest testing UK 12:00 to 13:00 against 15:00 posting slots, and leading with the founder's profile.
- **Nadia:** the US executive-dinner practitioner in #11 is the closest like-for-like voice seen. Worth adding to the monthly benchmark.
- **Dev:** "event ROI", "curated events" and "executive dinner" are worth a search-demand check before hooks are finalised.
- **Felix and Freya:** review hooks 1 to 10 before Leo slots them in.

*Raw data: Apify datasets FV4hFmFqYtapRxAHr, A2Cak3tVYrFQ9esIa, T1fjK0dFySE0sUKAw (7-day) and HMWmrW1LQiPtschAo (30-day), kept under the Apify account's standard retention.*
