# Plan item B7: merge /join-the-network/ into /join/ (page 9517)

Status: **DRAFT for Felix's review.** Nothing has been changed on the live site.
Decision (Nathan): one page at `/join/`; `/join-the-network/` (11638) then 301s to `/join/`.
Drafted by: Senior Content Writer, 10 November 2026. Kai builds after Felix > Freya, and only once the form questions in section 2 are settled.

---

## 1. Read this first: the two pages send leads to different places

I read both pages (read only) and checked the Make scenarios and WordPress REST routes they use. **The forms are not interchangeable**, and one form on /join/ doesn't send anything anywhere.

### Every form on both pages

| Page | Form | Built with | Fields (name attribute) | Where it submits | Reaches the CRM? |
|---|---|---|---|---|---|
| **/join/ (9517)** | Membership application, 2 steps (`<form id="cxf" class="cxf-form">`) | Hand-coded HTML + inline JS (no form plugin) | Step 1: `firstName`*, `lastName`*, `email`* (business only, JS blocks 17 free domains), `phone`*, `linkedin`* (URL). Step 2: `company`*, `jobTitle`*, `companySize`* (select), `industry`* (select, 13 options), `meet` (optional textarea, 600 chars), `gdpr`* (checkbox), `terms`* (checkbox) | JS `fetch` POST (JSON) to **`https://convenexevents.com/wp-json/cx/v1/join`**, a custom WordPress REST route (namespace `cx/v1`, POST only). Shows an in-page "Application received" message on `{ok:true}`. | **Unknown.** No Make webhook is referenced on the page. The route's handler is in a custom plugin/snippet I can't read over REST. Kai must check what `cx/v1/join` does (email? WP user? CRM sheet?). |
| /join/ (9517) | Footer newsletter (`<form id="news-form">`) | Hand-coded HTML + inline JS | email (no `name` attribute) | **Nowhere.** The JS validates the address, shows "Thanks, you are subscribed." and clears the field. No request is sent. A `cx/v1/newsletter` route exists on the site but this form doesn't call it. | **No. Sign-ups are being lost.** Separate fix, see section 2. |
| **/join-the-network/ (11638)** | Waitlist (`<form id="waitlist" method="post">`) | Hand-coded HTML (no form plugin) | `first_name`*, `last_name`*, `email`* (company only), `company`*, `job_title`*, `linkedin`* (pattern must be linkedin.com/in/), `mobile` (optional), `seniority`* (CXO / VP / Director / Head of / Senior Manager), `function`* (10 options), `topics[]` (6 checkboxes), `formats[]` (3 checkboxes), `region` (select), `consent`* (checkbox), `website` (hidden honeypot) | **Two routes on one submit:** (1) native form POST to the n8n webhook **`https://convenexevents.app.n8n.cloud/webhook/cx-network-join`** (n8n then redirects; the page reads `?error=email|linkedin|missing|consent|spam` on return); (2) a `navigator.sendBeacon` copy to the Make webhook **`hook.eu1.make.com/bpgh15eiwk8zvqxwont439dg25heyfkg`** = hook 4053168, which feeds **Make scenario 8415814 "Convene X network waitlist to CRM"** (active). | **Yes.** Scenario 8415814 filters out free email domains and adds a row to the CRM sheet (Source "Join the Network", Status "New", next action "Check LinkedIn and match to a room", due in 2 days). |

I also confirmed scenario **8415795 "Convene X contact form to CRM"** (hook 4053164) is **not** used by either page. It expects different field names (`name`, `surname`, `message`, `prefer`, `website_url` honeypot), so don't point either join form at it.

There's also an older Make hook, **3964980 "Join the Network — waitlist"**, with **no scenario attached**. Nothing on these two pages calls it. Worth deleting later (Kai/Nathan) so nobody wires a form to a dead hook.

### Recommendation: keep the waitlist form (from /join-the-network/), unchanged in its wiring

- It's the only one of the two that's **confirmed** to reach the CRM (scenario 8415814), and it also goes to n8n.
- Its fields match how we actually run rooms: seniority, function, topics and formats are exactly what the guest-list matching needs.
- Move the `<form id="waitlist">` block and its two scripts (`crm-copy` beacon and `form-error`) onto /join/ **byte for byte**: same `action`, same field `name`s, same honeypot. Only the visible heading and button label change (see the copy below). Changing labels doesn't affect n8n or Make.
- Retire the /join/ two-step `cxf` form **only after** Kai confirms what `cx/v1/join` does. If it creates member accounts for the members area (the footer says "Join the Members Area" and the nav has "Login"), removing it would stop new member accounts being created. Nathan decides; see the checklist.

### What Kai or Nathan must reconnect or check (in this order)

1. **Check `POST /wp-json/cx/v1/join`** (Kai): what it does and where the data goes. If it's the only place member accounts are created, decide with Nathan whether that still happens at sign-up or after a request is approved.
2. **n8n workflow behind `webhook/cx-network-join`** (Nathan or Kai, in n8n): update every redirect URL that points at `/join-the-network/` (the error redirects `?error=...` and any success/thank-you redirect) to `/join/`. Don't rely on the 301: redirects can drop the query string, and then the error message won't show.
3. **Make scenario 8415814**: no change needed if field names stay the same. Its Source column says "Join the Network"; fine to leave. Run one test submission after go-live and check a row lands in the CRM sheet.
4. **Footer newsletter form** (site-wide footer, also on /join/): it doesn't submit anywhere. Either connect it to `cx/v1/newsletter` (if that route stores sign-ups) or remove it until there's somewhere for the data to go. Flag for Amara (email) and Eleanor (consent wording).
5. **Consent wording** (Eleanor): the /join/ form had two ticks (data processing + Terms & Privacy Policy); the waitlist has one ("happy for Convene X Events to contact me about events", linking the privacy policy). Confirm the single tick is enough for what we do with the data, or add the Terms acceptance as a second checkbox. If a field is added, it must be added to the n8n and Make mappings too.
6. **Redirect** (Kai, Rank Math > Redirections): 301 `join-the-network` → `/join/`, in the same release. Then move 11638 to draft.
7. **Links**: update any internal link to `/join-the-network/` (Rank Math link report). Footer label "Join the Members Area" → "Request an invitation" (or keep, if the members area stays; Nathan).
8. **Test** in a logged-out window (FlyingPress cache): one valid submission, one with a Gmail address (should show the email error), one without LinkedIn.

---

## 2. Merged page copy for /join/

Combines the best of both pages with no duplication: the waitlist page's headline, facts strip, "how it works", room cards and FAQ; the /join/ page's "why join" points (rewritten so they don't repeat the facts strip) and the email fallback. One path: **Request an invitation**. No personal names. No claim about past events.

**Structure:** Hero > Facts strip > Why join > Form > How it works > The rooms > Before you join (FAQ) > Questions fallback.

### Hero

- Eyebrow: `The Convene X network`
- H1: **A seat at the table you'd clear your diary for.**
- Lede: Request an invitation to invite-only executive dinners and virtual roundtables with your peers. Small rooms, one good question, nothing recorded.
- Button (anchors to the form): `Request an invitation`

### Facts strip (3 items, unchanged from the waitlist page)

| Label | Value |
|---|---|
| Cost to you | Free |
| House rule | Chatham House |
| In the room | Director and up |

### H2: Why join

- **Rooms you can trust.** Every guest is a senior decision-maker, checked against their company email and LinkedIn profile before anyone is invited.
- **Off the record.** Conversations happen among peers who carry the same responsibility. Nothing is recorded, and nobody is on a stage.
- **Invitations that fit.** You're only invited to dinners, roundtables and webinars that match your role and the topics you care about.
- **No obligation.** Say yes to the rooms you want and pass on the rest.

### H2 (form heading): Request an invitation

Sub-line: Two minutes. We review every request by hand.

Form: the waitlist form, unchanged except:
- form heading text "Join the waitlist" → **"Request an invitation"**
- submit button text "Join the waitlist" → **"Request an invitation"**

Field labels and hints stay as they are on /join-the-network/ (they're already clear and calm), including: "Company addresses only. Gmail, Outlook and other personal addresses can't be accepted.", "We check every request against LinkedIn before inviting anyone." and "Only used to reach you in the week of an event you've accepted."

Success state: whatever n8n currently returns. If Kai builds an in-page message, use: **"Thank you. We review every request by hand and will email you once we've had a look. You're never obliged to accept an invitation."**

### H2: From request to your seat

1. **Request an invitation.** Tell us your role and the topics you'd give up an evening for.
2. **We match you to a room.** When a dinner or roundtable fits your seniority and interests, we add you to the guest list.
3. **You get a personal invitation.** Date, venue, the question on the table and who else is coming, by role. Say yes or pass.

(Step 3 changed "who else is coming" to "who else is coming, by role", so it matches our practice of not sharing guest names without consent.)

### H2: Small by design

- **Executive dinners.** One table, one conversation, peers from across your sector. `8 to 25 seats · In person`
- **Virtual roundtables.** Cameras on, a chair keeping it moving, from wherever you are. `6 to 12 seats · Online`
- **Webinars.** A sharper briefing on one topic, with time for your questions. `Up to 50 · Online`

### H2: Before you join

**Is it really free?**
Yes. Each room is hosted by a partner organisation, which is why invited guests never pay.

**Who is it for?**
Senior leaders, Director level and up for dinners and roundtables. Webinars are open to Senior Managers too.

**What happens after I request an invitation?**
We confirm we've received it, check it by hand, then invite you when a room fits. You're never obliged to say yes.

**What do you do with my details?**
We use them to match you to rooms and invite you. Read the [privacy policy](https://convenexevents.com/convene-x-events-privacy-policy/) for the detail.

### Closing line

Questions before you request an invitation? Email enquiries@convenexevents.com.

(No booking-call CTA on this page on purpose: it's the guest path. The exploratory call is the host/sponsor path and would split attention.)

### What I dropped and why

| Dropped | From | Why |
|---|---|---|
| "Convene X is invitation-only. Membership is required to attend any executive dinner, virtual roundtable or webinar." | /join/ | Framed as an application to a membership scheme, which competes with the "request an invitation" path. The idea survives in the lede and the FAQ. |
| "Membership is complimentary for qualifying executives. We review each application individually." | /join/ | Duplicates "Cost to you: Free" and "We review every request by hand". |
| "Access to every format" | /join/ | Slight over-promise (you're invited to rooms that fit, not all of them). Rewritten as "Invitations that fit". |
| The two-step membership form and its fields (phone required, company size, industry, "Which leaders would you most value meeting?") | /join/ | See section 1. If Nathan wants "Which leaders would you most value meeting?" back, add it to the waitlist form as an optional field **and** map it in n8n and Make scenario 8415814, in the same release. |
| "Application received" message | /join/ | Replaced by the waitlist flow's response. |

### Points for Felix

- Seat counts: the waitlist page says dinners are "8 to 25 seats"; the brand brief says 10 to 25. I've kept 8 to 25 as it's the live, approved card text; Felix to decide.
- "Each room is hosted by a partner organisation" is the sponsor-hosted model stated plainly. It's true to the brand brief, and it answers "why is it free" honestly. Keep.
- No exclamation marks, no personal names, UK spelling. Numbers as digits.

---

## 3. Meta for /join/ (Rank Math)

- **SEO title (50 chars):** `Request an Invitation | Join the Convene X Network`
- **Meta description (153 chars):** `Request an invitation to invite-only executive dinners and virtual roundtables for Director-level leaders and above. Free for guests. Chatham House Rule.`
- **Focus keyword:** keep `join our network` for now (avoids a new overlap with `/why-invitation-only-events/`). Dev to check search demand for "executive network invitation" before changing it.
- **Robots:** index, follow (as now).
- **Page title (WordPress):** change "Join Our Network" → "Request an Invitation".
- **OG title/description:** inherit from the above.

After it's live: Nathan requests indexing for `/join/` (plan section C, Day 1).
