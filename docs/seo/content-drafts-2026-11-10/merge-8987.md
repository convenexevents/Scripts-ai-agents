# Fix 4 (plan item B5): merge the virtual-roundtable posts into 8987

## Felix review (Brand & Quality), 10 Nov 2026

**Verdict: Pass with edits.**

Voice is right: calm, specific, peer-level, UK English, no exclamation marks, no personal names, no proof claim. Every unsourced statistic and lead/ROI promise from 8782 is gone. The comparison table is proper markup, one H2 per section with H3s beneath, the focus keyword sits in the first line, and all 6 internal targets plus the 301 source resolve (checked on WordPress: 9414, 44, 6264, 8985, 48, 8984 published). Changes:
- **Opening link anchor.** The page's own focus keyword ("B2B virtual roundtables") was the anchor pointing at a different page, which tells Google another URL owns the term. The keyword is now plain text, and the service-page link moves to the end of the intro paragraph with the anchor "executive virtual roundtables".
- **Meta title** changed to `B2B Virtual Roundtable Guide: How to Run One Well` (49 chars). The old one, "How to Run One Leaders Stay For", misreads as "One Leaders" when it's cut short in search results. The description (151 chars) is unchanged.
- Numbers as digits: "Four things" becomes "4 things", and "two to three days" becomes "2 to 3 days".
- Blocking: none on copy. The 301 and inbound-link updates must ship in the same release (Kai, Callum).

## Freya sign-off (Head of Marketing & Content), 10 Nov 2026

**Verdict: Approved with edits. Kai may apply now, as one release with the 301 and the inbound-link updates.**

- Edit, opening: "Not because the format is bad, but because..." was the "not X, but Y" pattern we ban. It now makes the point directly.
- Edit: "This does two things" becomes "This does 2 things" (numbers as digits).
- No proof claim on this page, and none needed. Keep it that way.
- Release order for Kai: (1) new body, meta and cleared OG overrides on 8987; (2) 301 `how-to-host-a-virtual-roundtable` to `/b2b-virtual-roundtable-guide/` in Rank Math; (3) update every inbound link to the old URL (Callum pulls the list from the Rank Math link report); (4) move 8782 to draft; (5) check logged out after the FlyingPress purge. If step 2 can't be done (the Rank Math integration is still switched off for the MCP user), **don't ship step 1 on its own.** Stop and ask Nathan to add the redirect by hand first.

Status: **DRAFT for Felix's review.** Nothing has been changed on the live site.
Drafted by: Senior Content Writer, 10 November 2026.
Signed off for drafting by Nathan (plan items B5/B6). Kai applies after Felix > Freya.

## Summary

| | |
|---|---|
| Surviving post | 8987, `/b2b-virtual-roundtable-guide/` (keeps its URL) |
| Retiring post | 8782, `/how-to-host-a-virtual-roundtable/` (301 to 8987, set by Kai in Rank Math > Redirections in the same release) |
| Focus keyword (unchanged) | `b2b virtual roundtable` |
| Secondary keywords picked up from 8782 | how to host a virtual roundtable, virtual roundtable vs webinar, virtual roundtable best practices |
| Length | about 1,800 words (was about 750) |
| Structure | 8987's sections kept in order; 8782's unique material folded into them; one FAQ block at the end |

### Proposed meta (Rank Math)

- **SEO title (49 chars, changed by Felix):** `B2B Virtual Roundtable Guide: How to Run One Well`
- **Meta description (151 chars):** `How to run a B2B virtual roundtable senior leaders stay for: the guest list, format, facilitation, common mistakes and follow-up, with answers to FAQs.`
- **Post H1/title:** keep `How to Run a Virtual Roundtable Senior Leaders Stay For`
- **Excerpt:** keep the current one.
- **OG/Twitter title and description:** clear the overrides so they inherit the new title and description (currently they repeat the old excerpt).

### What changed, at a glance

1. **Opening link fixed.** 8987's first sentence linked to `/how-to-host-a-virtual-roundtable/`, which is about to 301 back to this page. It now links to the service page instead.
2. **New short definition section** ("What a B2B virtual roundtable is") from 8782, tightened, so the page answers the query early (AEO).
3. **Comparison table** from 8782 rebuilt as a real `<table>` with `<thead>`/`<th>` header cells. On 8782 the headers "Feature / Virtual Roundtable / Webinar" were H2 headings and the values were three loose lists that didn't line up row by row (group size and interaction level were swapped). Fixed (closes plan item B10 as well).
4. **Pre-event section** now also covers who to invite and how to sharpen the topic (from 8782).
5. **Facilitator section** gets 8782's "what a good moderator does" list, merged into 8987's facilitator paragraph so there's one section, not two.
6. **Run of show** added, adapted to our format (one moderated conversation, not speed-networking rotations).
7. **Common mistakes** from 8782, rewritten for our format.
8. **Follow-up** merges both posts' 48-hour advice into one section.
9. **FAQ block** from 8782 (5 questions), answers aligned with 8987 and the brand brief (6 to 12 guests, 60 to 75 minutes ideal, 90 maximum).
10. **CTA**: one explicit next step at the end (book the 45-minute exploratory call), plus the service-page link in context.

### Internal links in the new body (8 internal, 1 external)

| Anchor text | Target | Why |
|---|---|---|
| executive virtual roundtables | `/executive-virtual-roundtables/` (9414) | Service page, end of the intro paragraph (Felix moved it off the focus-keyword anchor) |
| why senior leaders value conversation over presentation | `/why-senior-leaders-value-conversation/` (44) | Supports the "format" argument; 44 is "Discovered, not crawled", so this also helps B3 |
| why invitation-only rooms get better conversation | `/why-invitation-only-events/` (6264) | Guest-list section |
| why senior executives say no to events | `/senior-executives-say-no-to-events/` (8985) | Pre-event section; 8985 needs more internal links (B3) |
| executive webinars vs virtual roundtables | `/executive-webinars-vs-virtual-roundtables/` (48) | Under the comparison table, for readers who want the longer comparison |
| how an executive roundtable differs from an executive dinner | `/executive-roundtable-vs-executive-dinner/` (8984) | Opening section on virtual vs in-person; 8984 needs links (B3) |
| executive virtual roundtables (CTA block) | `/executive-virtual-roundtables/` (9414) | Repeat service link in the closing block |
| Book a 45-minute exploratory call | `https://cal.com/convenexevents/15min` | Primary CTA from the brand brief |
| Chatham House Rule (external) | `https://www.chathamhouse.org/about-us/chatham-house-rule` | Kept from 8987 |

That takes 8987 from 2 to 6 distinct internal targets, which meets B3's "5+ links out".

**Inbound links Kai must update in the same release** (so nothing points at the 301): any post or page linking to `/how-to-host-a-virtual-roundtable/`. Callum can pull the list with Rank Math's link report for post 8782. The service page 9414 should link to 8987 (that's already plan item B2).

### What I dropped from 8782, and why

| Dropped | Reason |
|---|---|
| All unsourced statistics: "63% of organisers plan to increase virtual investment", "73% of B2B marketers say virtual events are best for leads", "up to 40% of participants converted to qualified leads", "cost around 75% less than in-person", "increase completion rates by 22%", "only 20-30% of event contacts get followed up", "89% say video brings strong ROI", "74% see positive ROI only after six months" | None carried a source on the page. House rule: no unverified statistics. |
| "84% of [executives] base purchasing decisions on peer recommendations", linked to HBR | The linked HBR article is titled "84% of B2B sales start with a referral, not a salesperson". The sentence on 8782 misstated what it says. Dropped rather than reworded, as we haven't read the full source. |
| The "Generating high-quality leads", "Filling the sales pipeline" and lead-KPI framing | Brand brief: never promise sponsors leads, guaranteed meetings or ROI. The format is sold on conversation quality, not lead counts. |
| Speed-networking mechanics: pre-booked 1:1 meeting rounds, "two pre-scheduled meeting rounds" in the agenda, matchmaking tools, "meetings per attendee" and "meeting completion rate" KPIs, "breakout roulette", overbooking rotations | That describes a virtual networking event, not our 6 to 12 person moderated roundtable. Mixing the two would confuse readers and contradict 8987's structure. The useful core (ask structured questions at sign-up, plan for no-shows) is kept in our own terms. |
| "Design a dedicated event page", "Promote across social and email channels", "Select the right platform" checklist (CRM integration, analytics) | Generic event-marketing advice, not about running the room. Platform point kept in one line and in the FAQ. |
| "Repurpose content for marketing: blog posts from transcripts, video clips for social" | Conflicts with the off-the-record ground rule in 8987 (never publish without every participant's consent; Chatham House). Kept only the consented, non-attributable summary. |
| "Key takeaways" list | Repeated points already made in the body. |
| "in 2026" in headings and the H1 | Dates the page; not needed for the keyword. |
| The two AI-generated infographics (`Copilot_20260729_160208.png` and `gpt-image-2_Minimalist_corporate_infographic...jpg`) | The alt text of one is the image-generation prompt, and the mistakes infographic lists points we've rewritten. If Kai wants a visual, brief a new one from the comparison table. |
| Closing line "Convene X specialises in designing and delivering curated executive roundtables" | Reads as a past-delivery claim. Replaced by a future-facing CTA. |

### Points for Felix to check

- I've used "6 to 12 guests" (brand brief) rather than 8782's "6 to 10".
- No proof claim is used. If Freya wants one, use the approved team framing only ("our team, in previous roles").
- No personal names. No exclamation marks. UK spelling.

---

## New body for post 8987 (paste into the block editor as Custom HTML, or convert to blocks)

```html
<p>Most B2B virtual roundtables have a reputation problem, and the format isn't to blame. Most of them are run badly, and senior leaders have learned to expect a 60-minute call that could have been a well-written email.</p>

<p>The ones that work share a handful of structural choices that most organisers don't make. This guide covers them: who to invite, how to design the hour, how to facilitate, what goes wrong, and what to do afterwards. It's also how we design our own <a href="https://convenexevents.com/executive-virtual-roundtables/">executive virtual roundtables</a>.</p>

<h2>What a B2B virtual roundtable is</h2>

<p>A B2B virtual roundtable is a private, invitation-only video discussion where a small group of senior leaders, usually 6 to 12, work through one specific business question together. A facilitator guides the conversation, and the participants, not a speaker, are the programme.</p>

<p>4 things separate it from other online formats:</p>

<ul>
<li><strong>Curated attendance.</strong> Every seat is chosen. Nobody joins from a public registration link.</li>
<li><strong>A small group.</strong> Small enough that everyone speaks, large enough for a range of views.</li>
<li><strong>A facilitator, not a presenter.</strong> Their job is to hold the conversation, not to fill it.</li>
<li><strong>Clear confidentiality.</strong> What's said stays in the room unless everyone agrees otherwise.</li>
</ul>

<h2>Virtual roundtable vs webinar</h2>

<p>The two formats are often confused, and the difference decides almost every other choice you make.</p>

<table>
<thead>
<tr>
<th scope="col">Feature</th>
<th scope="col">Virtual roundtable</th>
<th scope="col">Webinar</th>
</tr>
</thead>
<tbody>
<tr>
<th scope="row">Primary goal</th>
<td>Peer exchange and relationships</td>
<td>Sharing content with an audience</td>
</tr>
<tr>
<th scope="row">Group size</th>
<td>6 to 12 participants</td>
<td>Dozens to hundreds of registrations</td>
</tr>
<tr>
<th scope="row">Interaction</th>
<td>High: everyone contributes</td>
<td>Low: mostly listening, with Q&amp;A</td>
</tr>
<tr>
<th scope="row">Participant role</th>
<td>Active contributor</td>
<td>Audience member</td>
</tr>
<tr>
<th scope="row">Format</th>
<td>Discussion-led</td>
<td>Presentation-led</td>
</tr>
<tr>
<th scope="row">Typical length</th>
<td>60 to 75 minutes, 90 at most</td>
<td>30 to 60 minutes</td>
</tr>
</tbody>
</table>

<p>For a longer comparison of when to choose each, see <a href="https://convenexevents.com/executive-webinars-vs-virtual-roundtables/">executive webinars vs virtual roundtables</a>.</p>

<h2>The number one error: treating virtual as a substitute for in-person</h2>

<p>It isn't. Virtual removes the environmental cues that make in-person executive events work: the room, the shared meal, the social friction of being physically present with people. You can't compensate for this by trying harder in the same direction. You compensate by making different structural choices.</p>

<p>Virtual roundtables work best when the conversation itself is valuable enough that it's worth giving up 60 minutes for, not when the format is being used to approximate something that should have been done in person. If you're weighing the two, here's <a href="https://convenexevents.com/executive-roundtable-vs-executive-dinner/">how an executive roundtable differs from an executive dinner</a>.</p>

<h2>Pre-event: the guest list and the brief matter more than the invitation</h2>

<h3>Invite for the conversation, not the headcount</h3>

<p>Start with the people the question matters to. Look for leaders who own the problem you're discussing, have the authority to act on what they hear, and are dealing with it now rather than in theory. A room of 8 people who all carry the same responsibility beats a room of 20 with mixed job titles every time. It's the same reason <a href="https://convenexevents.com/why-invitation-only-events/">invitation-only rooms get better conversation</a>.</p>

<p>Ask a few structured questions when someone accepts: their role, the size and type of their organisation, and what they'd most like to get from the hour. It lets you balance the room and gives the facilitator something to work with.</p>

<h3>Make the question specific</h3>

<p>A broad theme produces a scattered conversation. "The future of AI" gives nobody anything to say. "How are finance teams deciding which AI pilots to stop?" gives everyone something to bring. Pick one live, specific question your guests are wrestling with this quarter.</p>

<h3>Send a participant brief</h3>

<p>Most virtual roundtable invitations describe the format and the date. The ones that produce good attendance and good conversation send a participant brief 2 to 3 days before. It should include the opening question, the guest list by role and company type (not individual names unless agreed), the facilitation structure, and what a participant who comes prepared should think about in advance.</p>

<p>This does 2 things. It filters out passive attendees who were never going to contribute. It prepares the active ones to arrive with something worth saying. It also answers most of the reasons <a href="https://convenexevents.com/senior-executives-say-no-to-events/">senior executives say no to events</a> before they come up.</p>

<h2>On the day: format design</h2>

<p>90 minutes is the outer limit for virtual senior executive attention. 60 to 75 minutes is better. Within that window, the structure should include:</p>

<p><strong>A standing start with no warm-up ceremony.</strong> Senior leaders don't need to be welcomed, introduced to the technology, or told what's about to happen. They know what a video call is. Start with the opening question.</p>

<p><strong>Small breakout pairs for the first 10 minutes, then reconvene.</strong> Breakouts break the passive-observer dynamic that sinks most virtual roundtables. Everyone has spoken to at least one person before the main discussion begins.</p>

<p><strong>One facilitator, clearly introduced, with explicit permission to interrupt and redirect.</strong> On a video call, a dominant voice kills the conversation faster than it does in person, because there's no non-verbal signal for others to use to interject.</p>

<h3>A sample 60-minute run of show</h3>

<ul>
<li><strong>0 to 2 minutes:</strong> the opening question, straight away.</li>
<li><strong>2 to 12 minutes:</strong> breakout pairs on the question.</li>
<li><strong>12 to 50 minutes:</strong> the full group, facilitated, building on what came out of the pairs.</li>
<li><strong>50 to 58 minutes:</strong> each participant names one thing they'll take away or test.</li>
<li><strong>58 to 60 minutes:</strong> close, with what happens next and when.</li>
</ul>

<p>Share the run of show with the facilitator and anyone supporting behind the scenes, so timings and handovers are agreed before the call starts.</p>

<h3>What a good facilitator does</h3>

<p>A virtual roundtable only works if people feel comfortable speaking. Without the right facilitator, one or two voices dominate and the rest stay quiet. A good facilitator:</p>

<ul>
<li>speaks the least, and makes sure everyone gets a turn;</li>
<li>reads the call and brings quieter voices in by name;</li>
<li>senses when the conversation needs grounding and when it needs space;</li>
<li>creates warmth without forcing familiarity;</li>
<li>holds the conversation rather than controlling it.</li>
</ul>

<p>That matters more than the platform or the slides, because, as we've argued before, <a href="https://convenexevents.com/why-senior-leaders-value-conversation/">senior leaders value conversation over presentation</a>.</p>

<h2>On the technology</h2>

<p>The one technology rule that matters: all participants on camera, or no participants on camera. Mixed camera-off rooms create a two-tier experience where the people on camera feel exposed and the people off camera feel uninvested. Make camera-on a condition of the invitation, or make the format explicitly audio-only for everyone.</p>

<p>Platform matters less than people think. Zoom or Microsoft Teams is fine for most roundtables, as long as breakout rooms work. Test audio, video, links and breakouts with your facilitator before the day. The one exception: if participants are joining from several regions, latency adds up, so choose a platform that performs well where most of your guests are.</p>

<h2>Common mistakes to avoid</h2>

<p>Most virtual roundtables that fall flat break one of the same rules:</p>

<ul>
<li><strong>A webinar in disguise.</strong> 40 minutes of presentation, with "discussion" squeezed in at the end. Design for conversation from the first minute.</li>
<li><strong>A guest list built for numbers.</strong> Inviting anyone who'll accept fills the call with people who can't contribute. Invite for the question.</li>
<li><strong>Signing people up with an email address and nothing else.</strong> Without knowing roles and interests, you can't balance the room or brief the facilitator.</li>
<li><strong>Planning for 100% turnout.</strong> Senior diaries move. Plan the conversation so it still works if one or two people drop out on the day.</li>
<li><strong>Silence afterwards.</strong> No thank-you, no summary, no next step within 48 hours. The goodwill fades fast.</li>
</ul>

<h2>Follow-up</h2>

<p>Within 48 hours, send every participant a personal thank-you, and one clear next step, such as the date of the next session or an invitation to continue the conversation. A short feedback question while the call is still fresh tells you what to change next time.</p>

<p>Virtual roundtables that produce good conversation often produce a shared insight document too. This is the one material difference from a dinner: there's usually something worth writing up. If you've agreed it in advance, a short, <a href="https://www.chathamhouse.org/about-us/chatham-house-rule">non-attributable</a> summary of the discussion gives you a reason to get back in touch with every participant individually.</p>

<p>One caveat: never publish anything without explicit consent from every participant. The candour that makes the conversation good depends on the ground rules holding.</p>

<h2>Frequently asked questions</h2>

<h3>How many people should be invited to a virtual roundtable?</h3>

<p>Between 6 and 12. That's enough for a range of views while making sure everyone has time to speak. Below 12, a single facilitated conversation works best; above it, people start to watch rather than take part.</p>

<h3>How long should a virtual roundtable be?</h3>

<p>60 to 75 minutes is ideal, and 90 is the outer limit. Under 45 minutes rarely leaves room for more than one real exchange. If you have more to cover than 90 minutes can hold, run a series rather than one long session.</p>

<h3>What platform should I use for a virtual roundtable?</h3>

<p>Zoom or Microsoft Teams is enough for most roundtables. What matters more is that breakout rooms work, everyone can be on camera, and the facilitator can manage the room. Test it with the facilitator before the day.</p>

<h3>What's the difference between a virtual roundtable and a webinar?</h3>

<p>A webinar shares content from a few speakers with a largely listening audience. A virtual roundtable exists so a small group of peers can talk to each other: the participants are the programme, and success is measured by the quality of the conversation, not the number of people watching.</p>

<h3>How do I measure whether a virtual roundtable worked?</h3>

<p>Look at who came against who you invited, whether everyone contributed, what participants said in the feedback question, and how many asked to be invited back or continued the conversation afterwards.</p>

<h2>Run your next virtual roundtable with us</h2>

<p>If you'd like a B2B virtual roundtable run this way, with a guest list you sign off and a facilitator who keeps it a conversation, see our <a href="https://convenexevents.com/executive-virtual-roundtables/">executive virtual roundtables</a>.</p>

<p><strong>Next step:</strong> <a href="https://cal.com/convenexevents/15min">book a 45-minute exploratory call</a>. It's a conversation about your audience and the question you'd want on the table, not a pitch.</p>
```

### Notes for Kai

- Keep the existing "Continue with Convene X" post-CTA block (`.cx-postcta`) if it's injected by the template; it's not part of this body. If it's in the post content, it can stay below the last paragraph; it doesn't duplicate anything above.
- Tables: if the theme doesn't style `<table>`, a WordPress Table block (`core/table` with "Header section" on) gives the same markup.
- Redirect: Rank Math > Redirections, 301, source `how-to-host-a-virtual-roundtable`, destination `/b2b-virtual-roundtable-guide/`. Ship in the same release as this body. Then move 8782 to draft (don't delete, so its revision history stays).
- After it's live: Nathan requests indexing for `/b2b-virtual-roundtable-guide/` (plan section C, Day 3).
