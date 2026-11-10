# Footer newsletter form: fix spec

> Owner: Amara (Email & Lifecycle). Builder: Kai. Compliance check: Eleanor.
> Review chain: Felix > Freya > Nathan. Written 10 Nov 2026.
> **Status: DRAFT. Nothing in this file has been built, changed or sent.** No Make scenario has been created. All emails below are drafts for Nathan's sign-off.
>
> Everything in section 1 comes from read-only checks: the WordPress tools, the Make tools (scenarios 8415814, 8415795, 8397919 and the team's hook list), the CRM sheet header row, and the live HTML of `/`, `/contact-us/`, `/join-the-network/` and `/convene-x-events-privacy-policy/`.

---

## 1. How it works today

### 1.1 Where the form lives

The footer isn't the Elementor theme footer. It's **hand-coded HTML pasted into each page's own content**. Every page uses the `elementor_canvas` template and the `convene-x-child` theme (v2.2.7). A content search finds the footer block on about 42 published pages, plus the draft copies. Each page has its own copy of the footer markup and its own inline `<script>`.

- The Elementor library template "Footer" (ID 7435) does still exist. It has an Elementor Pro form widget (`0addc66`, one email field, button "Send", default actions, mail to enquiries@). **It isn't rendered on the live site**: there's no `elementor-location-footer` in the live HTML. Ignore it. Kai can archive it later so nobody edits the wrong footer.
- There are no classic widgets and no Elementor Custom Code snippet involved. The only 2 snippets are the cookie banner (10309) and Eva chat (11764).

### 1.2 Markup (identical on every page)

```html
<div class="foot foot-news rv">
  <h2>Newsletter</h2>
  <p class="foot-news-copy">Insights on executive events, delivered occasionally. No noise.</p>
  <form class="news-form" id="news-form" novalidate>
    <input type="email" class="news-input" id="news-email" placeholder="Your work email" aria-label="Email address" required>
    <button type="submit" class="btn news-btn">Subscribe</button>
    <span class="news-msg" id="news-msg" aria-live="polite"></span>
  </form>
</div>
```

- **Fields:** 1 email input. It has no `name` attribute and no visible label (only `aria-label`).
- **Consent text:** none. There's no checkbox, no privacy link in the form and no mention of what people are signing up to.
- **Spam protection:** none. No honeypot, no time check, no rate limit.

### 1.3 What happens on submit (2 competing scripts)

1. **Inline page script, `section('newsletter')`**, in every page's own `<script>`. It validates the email format, then shows **"Thanks, you are subscribed."** and clears the field. **It sends nothing.** This is the bug Nathan saw, and it's the fallback on any page where script 2 doesn't load.
2. **Site-wide script `<script id="cx-newsletter-js">`**, output at the end of `<body>` on every page (enqueued from the child theme, not page content). It listens for `submit` on `document` in the **capture phase**, then calls `preventDefault()` and `stopPropagation()`. That means it fires before script 1 and should block it. It POSTs JSON `{email, page, website:''}` to **`/wp-json/cx/v1/newsletter`** and shows "Thanks, you are on the list." if the response is `{ok:true}`.
   - That REST route exists (`cx/v1`, POST only, no declared args), but **what it does is unknown**. Its handler is PHP in the child theme, and I can't read that over REST. It may store the sign-up as a private post (the contact route's code comment says `cx/v1/contact` "emails enquiries@ and stores a copy as a private Enquiry post"), or it may do nothing. That private type isn't exposed, so I couldn't check.
   - Either way, **nothing reaches the CRM sheet or Make**. There's no newsletter hook in the Make team (9 hooks listed, none for the newsletter).
   - The `website:''` honeypot is hard-coded empty, so it doesn't protect anything.

**Net effect:** sign-ups never reach the CRM. Depending on the page and caching, the visitor sees either a false "subscribed" message or a message that depends on an endpoint nobody has checked. Neither path records consent.

### 1.4 How the working forms send leads (the pattern to reuse)

| Form | Front end | Server | CRM row |
|---|---|---|---|
| `/join-the-network/` waitlist | Native POST to n8n `convenexevents.app.n8n.cloud/webhook/cx-network-join`, plus `navigator.sendBeacon` to Make hook 4053168 (`bpgh15ei...`). Honeypot field `website`. | Make **8415814**: webhook > filter "Work email only" (18 free/competitor domains blocked) > Sheets addRow | Source "Join the Network", Stage New, opt-in **"yes" hard-coded**, Owner Nathan |
| `/contact-us/` | `fetch` JSON to `/wp-json/cx/v1/contact`. On success, fire-and-forget `fetch` (`no-cors`) to Make hook 4053164 (`mzr61gqs...`). Honeypot `website_url`. | Make **8415795**: webhook > filter "Real enquiry" (`website_url` empty, email present) > Sheets addRow | Source "Contact form", Stage New, opt-in "no", Owner Nathan |
| Planning-brief lead magnet | `fetch` to Make hook 4047473 | Make **8397919**: webhook > router: free domain > `WebhookRespond {"ok":false,"error":"work_email"}`; work email > notify email > send email to visitor > `WebhookRespond {"ok":true}` > Sheets addRow | Source "Planning brief", opt-in from the form |

**The pattern I recommend reusing is the lead-magnet one** (8397919): the browser calls a Make webhook and **reads a JSON reply** that Make sends with `WebhookRespond` and `Access-Control-Allow-Origin`. It's the only existing pattern where the page can honestly say "done", because the server answers. The waitlist (`sendBeacon`) and contact (`no-cors`) calls to Make are fire-and-forget: the page never learns whether the CRM row was written.

One fix to the pattern: 8397919 sends `{"ok":true}` **before** the Sheets addRow, with an Ignore error handler. So a failed CRM write still shows success. The newsletter scenario must reply only **after** the row is written.

### 1.5 CRM sheet check

Spreadsheet `1i3aTKkgNAlojyzZo79HAE-OEnIYssIsyTnk0JWIjv-Y`, tab **"Untitled"**, header row confirmed (18 columns, A to R):

`ID | Created | Source | Stage | First name | Last name | Email | Company | Job title | Interest | Topics chosen | Marketing opt-in | Owner | Next step | Next step date | Last contacted | Deal value | Notes`

This matches the order in the brief. Existing scenarios write by column index (0-17) through Make connection `12715952`. The newsletter scenario uses the same connection and index mapping. Existing ID prefixes are P, N, W and L. Newsletter rows use **S** (see 4.3).

### 1.6 Where sign-ups should go

**Decision: the Convene X CRM sheet, through a new Make webhook and scenario.** This is the default in the brief, and it's the same route every other website lead takes. Each sign-up becomes one row: Source "Newsletter", Stage "New", Owner blank, Marketing opt-in as set out in 2.3.

`/cx/v1/newsletter` is **not** the system of record. Kai checks what it does (4.6). If it stores anything, Kai exports it for Eleanor, then retires it or leaves it unused.

---

## 2. Proposed compliant flow (UK GDPR, PECR, EU GDPR and ePrivacy)

### 2.1 Fields and controls

| Element | Spec |
|---|---|
| Email | `type="email"`, `name="email"`, visible label (visually hidden is fine), `autocomplete="email"`, required. Work addresses only, using the same 18-domain block list as 8415814 and 8397919 (see 2.4). |
| Consent checkbox | `name="consent" value="yes"`, **unticked by default**, required to submit. Its label is the consent text in 3.2, which links to the privacy policy. |
| Privacy link | Inside the consent label: `https://convenexevents.com/convene-x-events-privacy-policy/`, opens in the same tab. |
| Honeypot | `name="website"`, off-screen, `tabindex="-1"`, `autocomplete="off"`, `aria-hidden`. Same field name as the waitlist, so the Make filters stay consistent. |
| Time trap | Hidden `t` = ms between page load and submit. Under 3,000 ms counts as a bot. |
| Client throttle | 1 accepted submit per browser per 60 s (`localStorage`). This is a nicety, not security. |
| Server-side spam rules | In Make: honeypot filled, `t` < 3000, or more than 1 submission for the same email in 10 minutes (Make data store) means no row and no email. The reply is a silent `{"ok":true,"status":"pending"}`, so bots learn nothing. |
| Success message | Shown **only** when Make replies `{"ok":true}` after the CRM row is written. |
| Error messages | Specific messages for each case: bad email, personal domain, unticked box, server error, network error, rate limit (3.3). |

**Why the checkbox is required, not optional.** The form has one purpose: joining the newsletter. An unticked submit has no lawful purpose, so we don't store it (data minimisation). This meets the brief's rule ("opt-in yes only when the box is ticked"): **an unticked box means no row at all**. Make enforces the same rule server-side (`consent` must equal `yes`), so a scripted POST without consent is rejected.

**Command Centre spam-burst tripwire.** I couldn't find its spec in this repo. Honeypot and time-trap hits never write a CRM row, so they won't trip it. Real bursts that get past the filters will show up as many "Newsletter" rows in a short window. Kai: confirm what the tripwire reads (CRM rows, Make executions or both) and make sure the new scenario's source value "Newsletter" is included in what it counts.

### 2.2 Double opt-in: **recommended (yes)**

Reasons:
1. **Proof of consent.** A footer form takes whatever is typed. Without confirmation, anyone can sign up a colleague, a competitor or a typo. A click from the inbox is the strongest evidence that the address owner agreed.
2. **EU reach.** We invite guests from the UK, Europe and the US. Several EU markets (Germany in particular) treat double opt-in as the expected standard for marketing email consent.
3. **Senior audience and brand.** A Director who gets a newsletter they never asked for is a complaint and a lost guest. "Never feel chased" starts here.
4. **List quality and deliverability.** Typos and bad addresses never reach the list, which keeps bounces and complaints down before Brevo comes in.
5. **There's a precedent.** The network waitlist already uses a "Check your inbox" (11653) and "You're on the list" (11654) flow.

Cost: some people never click. That's acceptable, because an unconfirmed address isn't consent we can rely on anyway.

### 2.3 Flow, step by step

```
Visitor ticks box + submits
  > browser POST (form-encoded, no preflight) to new Make hook "Convene X newsletter sign-ups"
  > Make: spam filter > validation (email, work domain, consent=yes)
  > Make: CRM lookup by email
      - new address:    add row  (Source Newsletter, Stage New, Owner blank, Marketing opt-in "pending")
      - existing row:   no new row; leave Source/Stage/Owner alone
  > Make: store token in data store "cx_newsletter_doi"
  > Make: send confirmation email (DRAFT 3.4) with link to confirm hook
  > Make: reply {"ok":true,"status":"pending"}   <- only now does the page show success
Visitor clicks link (within 7 days)
  > Make confirm scenario: token valid > CRM row Marketing opt-in "yes" + note
  > send welcome email (DRAFT 3.5) > redirect to /newsletter-confirmed/
```

**Marketing opt-in values.** The brief says to write "yes" when the box is ticked. With double opt-in, I recommend **"pending"** at sign-up and **"yes" only after the click**. Anything else would mark unconfirmed addresses as opted in, and Zoho Mail manual sends would pick them up. If Nathan prefers single opt-in for a first release, use the single opt-in variant (4.4): write "yes" at sign-up and send the welcome email straight away. **Nathan decides. Amara recommends double opt-in.** Jordan should confirm "pending" is an allowed value in the CRM app and the Command Centre.

**Existing contacts.** If the email is already in the CRM (for example an Outbound prospect with opt-in "no"), don't create a duplicate and don't change Source, Stage or Owner, which are Jordan's call. On confirmation, set Marketing opt-in "yes" on that row and append to Notes. If the row is already "yes", reply `{"ok":true,"status":"already"}` and send nothing.

**Unconfirmed sign-ups.** A weekly clean-up (Scenario C) removes tokens over 7 days old. It sets opt-in to "no" with the note "Newsletter sign-up not confirmed". It deletes rows that were created only by this form (Source Newsletter, never confirmed) after 30 days. Eleanor confirms the retention period.

**Unsubscribe.** Until Brevo is live, newsletters go out by hand from Zoho Mail. Every newsletter needs an unsubscribe route: a "reply unsubscribe" line plus a `mailto:enquiries@convenexevents.com?subject=Unsubscribe` link. Whoever handles enquiries@ sets the row's Marketing opt-in to "no" within 2 working days, and Jordan adds the address to the do-not-contact list. A one-click List-Unsubscribe header has to wait for Brevo.

### 2.4 Work email rule

The footer already says "Your work email", the privacy policy says generic addresses aren't permitted, and the other two Make scenarios block 18 domains. Use the same list (gmail.com, googlemail.com, yahoo.com, yahoo.co.uk, hotmail.com, hotmail.co.uk, outlook.com, live.com, icloud.com, me.com, aol.com, proton.me, protonmail.com, gmx.com, btinternet.com, elnevents.com, elnevents.org, execln.com). With consent, personal addresses would be lawful too, so this is a brand choice. Nathan can relax it.

---

## 3. Copy

House style: UK English, calm, no exclamation marks, no em dashes, no personal names. Felix reviews, then Freya, then Nathan.

### 3.1 Footer heading and line

- **Heading:** Newsletter
- **Line:** Occasional notes on executive dinners, roundtables and the rooms we're building. No noise, and you can leave any time.
- **Email placeholder:** Your work email
- **Button:** Subscribe (while sending: Sending...)

### 3.2 Consent text (checkbox label)

> Email me the Convene X Events newsletter and occasional invitations to events. I can unsubscribe at any time. Read our [Privacy Policy](https://convenexevents.com/convene-x-events-privacy-policy/).

Notes for Eleanor:
- It's written in the first person ("Email me"), which is clearer for a consent statement. That's a deliberate exception to "address the reader as you".
- The scope covers the **newsletter and event invitations**. If Nathan only wants the newsletter, cut "and occasional invitations to events". Without it, sector invitations to these people would need a separate basis.
- Store this wording with a version tag (`v1-2026-11-10`) on every sign-up. If the text changes, bump the version.

### 3.3 On-page messages

| Case | Message |
|---|---|
| Success (double opt-in) | Nearly done. We've sent a confirmation link to {email}. Click it to join the list. |
| Success (single opt-in variant) | You're on the list. The next newsletter will come to {email}. |
| Already subscribed | You're already on the list. There's nothing more to do. |
| Invalid email | Please enter a valid work email address. |
| Personal domain | Please use your work email. We keep this list to work addresses. |
| Box not ticked | Please tick the box so we can email you. |
| Rate limited (browser) | You've just signed up from this browser. Please wait a minute before trying again. |
| Server error (`ok:false` / 5xx) | Sorry, that didn't go through. Please try again, or email enquiries@convenexevents.com and we'll add you. |
| Network error / timeout | We couldn't reach our server. Check your connection and try again. |

`{email}` is the address the visitor typed, inserted as text (not HTML) so they can spot a typo.

### 3.4 Confirmation email (double opt-in): DRAFT, NOT FOR SENDING

> **DRAFT for Nathan's sign-off. Nothing sends until he approves the copy and the scenario is switched on.**

- **From name:** Convene X Events
- **From address:** an address on the convenexevents.com domain (see 4.6, item 5)
- **Reply-to:** enquiries@convenexevents.com
- **Subject:** Confirm your Convene X Events newsletter sign-up
- **Preview text:** One click and you're on the list.

```
Hello,

Someone, hopefully you, asked for the Convene X Events newsletter to be sent to this address.

To confirm, use the button below. The link works for 7 days.

[ Confirm my sign-up ]   -> {{confirm_url}}

If the button doesn't work, copy this link into your browser:
{{confirm_url}}

If you didn't ask for this, you can ignore this email. We won't add you to the list and you won't hear from us again.

The Convene X Events team

--
You're getting this one-off email because this address was entered in the newsletter form on convenexevents.com.
Convene X Events Ltd. Registered in England and Wales, company number [CONFIRM THIS].
Registered office: 4th Floor, 14 Museum Place, Cardiff CF10 3BH.
enquiries@convenexevents.com
```

This email is a transactional confirmation of a request. It must contain **no promotion**: no event plugs and no booking link.

### 3.5 Welcome email (after confirmation): DRAFT, NOT FOR SENDING

> **DRAFT for Nathan's sign-off. Nothing sends until he approves it.**

- **From name / reply-to:** as 3.4
- **Subject:** You're on the Convene X Events list
- **Preview text:** What to expect, and one quick question.

```
Hello,

Thanks for confirming. You're on the list.

Here's what to expect. We write occasionally, not weekly. Each issue covers one thing: what senior leaders are raising at our tables (Chatham House, so never names), how good executive rooms get put together, and the dinners and roundtables coming up.

No pitches. If an issue isn't useful, tell us.

One quick question: what's your sector and role? Just reply with a line, for example "Finance, CFO". We'll use it to send you the rooms that fit, and nothing else.

The Convene X Events team

--
You're getting this because you signed up at convenexevents.com and confirmed your address.
To unsubscribe, reply "unsubscribe" or email enquiries@convenexevents.com with the subject Unsubscribe.
Convene X Events Ltd. Registered in England and Wales, company number [CONFIRM THIS].
Registered office: 4th Floor, 14 Museum Place, Cardiff CF10 3BH.
```

### 3.6 Confirmation landing page copy (`/newsletter-confirmed/`)

- **Confirmed:** H1 "You're on the list". Body: "Thanks for confirming. The next newsletter will come to your inbox. In the meantime, you can see the formats we run." Link: [Executive dinners](https://convenexevents.com/private-executive-dinners/).
- **Expired or invalid link** (`?status=expired`): H1 "That link has expired". Body: "Confirmation links last 7 days. Enter your work email in the form at the bottom of this page and we'll send a fresh one."

Set the page to noindex in Rank Math.

---

## 4. Build spec for Kai

**Do this on staging first** (WP Staging Pro is installed). Make scenarios stay **OFF** until Eleanor has cleared section 5 and Nathan has signed off the copy. Test only with internal addresses.

### 4.1 Form markup (replace the `<form id="news-form">...</form>` block in every page)

```html
<form class="news-form" id="news-form" novalidate>
  <label for="news-email" class="sr-only">Work email</label>
  <input type="email" class="news-input" id="news-email" name="email"
         placeholder="Your work email" autocomplete="email" required>

  <div class="news-hp" aria-hidden="true">
    <label for="news-website">Leave this field empty</label>
    <input type="text" id="news-website" name="website" tabindex="-1" autocomplete="off">
  </div>
  <input type="hidden" name="consent_version" value="v1-2026-11-10">

  <label class="news-consent" for="news-consent">
    <input type="checkbox" id="news-consent" name="consent" value="yes" required>
    <span>Email me the Convene X Events newsletter and occasional invitations to events. I can unsubscribe at any time. Read our <a href="https://convenexevents.com/convene-x-events-privacy-policy/">Privacy Policy</a>.</span>
  </label>

  <button type="submit" class="btn news-btn" id="news-btn">Subscribe</button>
  <p class="news-msg" id="news-msg" role="status" aria-live="polite"></p>
</form>
```

Also change the line above the form to the 3.1 copy:
`<p class="foot-news-copy">Occasional notes on executive dinners, roundtables and the rooms we're building. No noise, and you can leave any time.</p>`

CSS (add once to the child theme stylesheet, not per page):

```css
.sr-only{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.news-hp{position:absolute!important;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden}
.news-consent{display:flex;gap:10px;align-items:flex-start;font-size:12.5px;line-height:1.5;color:var(--text-2);cursor:pointer}
.news-consent input{margin-top:3px;width:16px;height:16px;flex:0 0 16px;accent-color:var(--pink)}
.news-consent a{color:var(--text);text-decoration:underline}
.news-consent a:hover{color:var(--yellow)}
.news-btn[disabled]{opacity:.6;cursor:wait}
```

Check contrast for `--text-2` on `--bg` at 12.5px (WCAG AA 4.5:1). Make sure the checkbox's focus ring is visible.

**How to roll it out across about 42 pages:**
- The footer is in each page's classic content (wpautop adds `<br />` when rendering). Match against the **raw** content (`wp_get_post` / `context=edit`), not the rendered HTML.
- Do one search-and-replace per page for the `<form ...news-form...>` block, and another to **delete the inline `section('newsletter', ...)` block** from each page's script. That block is the fake success message and must go, so it can't be a fallback.
- Include drafts and the duplicate pages (11893-11900), and keep a before-copy of each page in `docs/automations/backups/`, as with the Eva change.
- Later tidy-up, not part of this fix: move the footer into one shared source (child theme `wp_footer` include or a `[cx_footer]` shortcode) so the next change is one edit, not 42.

### 4.2 Submit script (replaces `cx-newsletter-js` in the child theme)

Swap the body of the existing site-wide `cx-newsletter-js` (find where the child theme enqueues or prints it). Keep it as a document-level capture listener, so it still wins over any page copy that wasn't cleaned. Replace `MAKE_HOOK_URL` with the new hook URL from 4.3.

```js
(function(){
  var HOOK = 'MAKE_HOOK_URL';
  var LOADED = Date.now();
  var FREE = ['gmail.com','googlemail.com','yahoo.com','yahoo.co.uk','hotmail.com','hotmail.co.uk','outlook.com','live.com','icloud.com','me.com','aol.com','proton.me','protonmail.com','gmx.com','btinternet.com','elnevents.com','elnevents.org','execln.com'];
  var T = {
    pending: function(e){ return 'Nearly done. We’ve sent a confirmation link to ' + e + '. Click it to join the list.'; },
    already: 'You’re already on the list. There’s nothing more to do.',
    email: 'Please enter a valid work email address.',
    work_email: 'Please use your work email. We keep this list to work addresses.',
    consent: 'Please tick the box so we can email you.',
    throttle: 'You’ve just signed up from this browser. Please wait a minute before trying again.',
    server: 'Sorry, that didn’t go through. Please try again, or email enquiries@convenexevents.com and we’ll add you.',
    network: 'We couldn’t reach our server. Check your connection and try again.'
  };
  function say(msg, text, ok){ msg.textContent = text; msg.className = 'news-msg ' + (ok ? 'ok' : 'err'); }

  document.addEventListener('submit', function(e){
    var f = e.target; if (!f || f.id !== 'news-form') return;
    e.preventDefault(); e.stopPropagation();
    var input = f.querySelector('#news-email'), box = f.querySelector('#news-consent'),
        hp = f.querySelector('#news-website'), ver = f.querySelector('[name=consent_version]'),
        msg = f.querySelector('#news-msg'), btn = f.querySelector('button[type=submit]');
    var v = (input && input.value || '').trim().toLowerCase();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) { say(msg, T.email); input && input.focus(); return; }
    if (FREE.indexOf(v.split('@')[1]) !== -1) { say(msg, T.work_email); input && input.focus(); return; }
    if (!box || !box.checked) { say(msg, T.consent); box && box.focus(); return; }
    try { var last = +localStorage.getItem('cxNewsLast') || 0; if (Date.now() - last < 60000) { say(msg, T.throttle); return; } } catch(_){}

    var body = new URLSearchParams({
      email: v, consent: 'yes', consent_version: ver ? ver.value : 'missing',
      consent_text: box.parentNode.textContent.replace(/\s+/g,' ').trim(),
      page: location.href, website: hp ? hp.value : '', t: String(Date.now() - LOADED)
    });
    var label = btn ? btn.textContent : ''; if (btn) { btn.disabled = true; btn.textContent = 'Sending...'; }
    var ctrl = ('AbortController' in window) ? new AbortController() : null;
    var timer = setTimeout(function(){ ctrl && ctrl.abort(); }, 15000);
    function done(){ clearTimeout(timer); if (btn) { btn.disabled = false; btn.textContent = label; } }

    // Form-encoded body and no custom headers = a "simple" CORS request, no preflight.
    fetch(HOOK, { method: 'POST', body: body, signal: ctrl ? ctrl.signal : undefined })
      .then(function(r){ return r.json().then(function(j){ return { http: r.ok, j: j }; }); })
      .then(function(res){
        done();
        if (res.http && res.j && res.j.ok === true) {
          try { localStorage.setItem('cxNewsLast', String(Date.now())); } catch(_){}
          say(msg, res.j.status === 'already' ? T.already : T.pending(v), true);
          f.reset();
        } else {
          say(msg, T[(res.j && res.j.error)] || T.server);
        }
      })
      .catch(function(){ done(); say(msg, T.network); });
  }, true);
})();
```

The success text is set with `textContent`, so the typed email can't inject HTML.

### 4.3 Make: Scenario A, "Convene X newsletter sign-ups to CRM" (new)

New custom webhook **"Convene X newsletter sign-ups"**, team 3316415. Leave "Get request headers" off unless Eleanor asks for IP and user-agent as consent evidence (section 5). Scheduling: immediately. Keep it **inactive** until sign-off.

| # | Module | Settings |
|---|---|---|
| 1 | Webhooks > Custom webhook | Fields: `email, consent, consent_version, consent_text, page, website, t` |
| 2 | Router | 4 routes, in this order |
| 2a | Route "Spam" > Webhook response | Filter (OR): `website` exists, or `t` < 3000 (numeric). Response 200, body `{"ok":true,"status":"pending"}`, headers `Access-Control-Allow-Origin: https://convenexevents.com`, `Content-Type: application/json; charset=utf-8`. No row, no email. |
| 2b | Route "Invalid" > Webhook response | Filter (OR): `email` not exists; `email` doesn't match `^[^\s@]+@[^\s@]+\.[^\s@]+$`; `consent` ≠ `yes`. Body `{"ok":false,"error":"email"}` or `{"ok":false,"error":"consent"}` (use 2 routes, or `if()` in the body). |
| 2c | Route "Personal domain" > Webhook response | Same 18 `text:endwith:ci` OR-conditions as 8397919 route 1. Body `{"ok":false,"error":"work_email"}`. |
| 2d | Route "Valid" | Filter: not the 3 routes above (copy the conditions in AND / not-endwith form as in 8415814). Then: |
| 3 | Data store > Search records (`cx_newsletter_doi`) | `email` = `{{lower(1.email)}}` and `created` later than now minus 10 min. If found, go to 3a. |
| 3a | Webhook response | Duplicate within 10 min. Body `{"ok":true,"status":"pending"}`, no further action (stops resend floods). |
| 4 | Google Sheets > Search rows | Connection 12715952, spreadsheet `1i3aTKkgNAlojyzZo79HAE-OEnIYssIsyTnk0JWIjv-Y`, sheet "Untitled", filter column G (Email) equals `{{lower(1.email)}}`, limit 1 |
| 5 | Router | 5a: row found and column L = "yes" > response `{"ok":true,"status":"already"}`, stop. 5b: row found, not "yes" > skip to step 7 (no new row). 5c: no row > step 6. |
| 6 | Google Sheets > Add a row | Same mapping style as 8415814 (by index, `USER_ENTERED`):<br>0 ID `S{{formatDate(now; "YYMMDD-HHmmss")}}{{substring(md5(1.email); 0; 2)}}`<br>1 Created `{{formatDate(now; "YYYY-MM-DD HH:mm")}}`<br>2 Source `Newsletter`<br>3 Stage `New`<br>4-5 First/Last name *(blank)*<br>6 Email `{{lower(1.email)}}`<br>7 Company, 8 Job title *(blank)*<br>9 Interest `Newsletter`<br>10 Topics chosen *(blank)*<br>11 Marketing opt-in `pending` *(single opt-in variant: `yes`)*<br>12 Owner *(blank)*<br>13 Next step, 14 Next step date, 15 Last contacted, 16 Deal value *(blank)*<br>17 Notes `Newsletter sign-up on {{1.page}}. Consent box ticked, wording {{1.consent_version}}, {{formatDate(now; "YYYY-MM-DD HH:mm"; "UTC")}} UTC. Double opt-in pending.`<br>**Error handler: Webhook response `{"ok":false,"error":"server"}` (status 200) then Break/Commit stop. Not Ignore.** |
| 7 | Data store > Add a record (`cx_newsletter_doi`) | Key = `{{uuid}}` (the token). Fields: `email`, `row_id` (step 6 ID or step 4 row), `created` = now, `status` = `pending`, `consent_version`, `consent_text`, `page`. |
| 8 | Email > Send an email | To `{{1.email}}`. Subject and body from **3.4** (HTML version, same layout as 8397919's email). `{{confirm_url}}` = `<CONFIRM_HOOK_URL>?t={{7.key}}`. Reply-to enquiries@. **Error handler: respond `{"ok":false,"error":"server"}`.** |
| 9 | Webhook response | `{"ok":true,"status":"pending"}`, headers as 2a. **This is the only success reply, and it comes after the row and the email.** |

Data store `cx_newsletter_doi` structure: `email` (text), `row_id` (text), `created` (date), `status` (text: pending / confirmed / expired), `consent_version` (text), `consent_text` (text), `page` (text), `confirmed_at` (date). This doubles as the consent record.

### 4.4 Make: Scenario B, "Convene X newsletter confirm" (new)

New custom webhook **"Convene X newsletter confirm"**, linked from the email.

| # | Module | Settings |
|---|---|---|
| 1 | Custom webhook | Query field `t` |
| 2 | Data store > Get a record | Key `{{1.t}}` |
| 3 | Router | Not found, or `created` older than 7 days, or status ≠ pending > response **302**, `Location: https://convenexevents.com/newsletter-confirmed/?status=expired`. If status = confirmed, redirect to `/newsletter-confirmed/` (repeat click, so no change). |
| 4 | Google Sheets > Search rows | Email = `{{2.email}}` |
| 5 | Google Sheets > Update a row | Column L Marketing opt-in = `yes`. Column R Notes = `{{4.Notes}} Double opt-in confirmed {{formatDate(now; "YYYY-MM-DD HH:mm"; "UTC")}} UTC.` Leave every other column alone. |
| 6 | Data store > Update record | status `confirmed`, confirmed_at now |
| 7 | Email > Send an email | Welcome email **3.5**. Ignore errors here, because the confirmation itself has already been recorded. |
| 8 | Webhook response | 302 to `https://convenexevents.com/newsletter-confirmed/` |

**Single opt-in variant** (only if Nathan chooses it): drop Scenario B and data store steps 3, 3a and 7. Write `yes` in step 6. In step 8, send **3.5** instead of 3.4. Use the single opt-in success text in the JS (`status:"subscribed"`) and add a `subscribed` key to `T`.

### 4.5 Make: Scenario C, "Convene X newsletter clean-up" (new, weekly)

Weekly schedule:
1. Search the data store for status `pending` and created more than 7 days ago.
2. For each record, set status `expired` and set the CRM row's Marketing opt-in to `no` with the note "Newsletter sign-up not confirmed".
3. Rows with Source `Newsletter` that were never confirmed and are more than 30 days old: delete the row (period subject to Eleanor).

### 4.6 Checks before building

1. **`/cx/v1/newsletter`:** read the child theme handler. What does it do with `{email,page,website}`? Does it store anything (private post type, option, email to enquiries@)? If it has stored sign-ups, export them for Eleanor. **Don't add them to the CRM as opted in, and don't email them**: there's no record of consent wording, and asking for consent by email is itself a marketing email under PECR. Then remove the route or leave it unused.
2. **`cx-newsletter-js`:** find where the child theme outputs it, and replace it with 4.2.
3. **WordPress page `/newsletter-confirmed/`:** create it as a draft with the 3.6 copy and noindex.
4. **Tripwire:** confirm the Command Centre spam-burst tripwire counts Source "Newsletter" (2.1).
5. **Sending account:** Make email account `12775186` (used by 8397919) is probably the convenexevents@gmail.com Google account. The confirmation and welcome emails should come from a **convenexevents.com** address through Zoho Mail SMTP, which needs SPF/DKIM aligned. Confirm which mailbox this is before switching on.
6. **CRM app:** ask Jordan to confirm that "pending" in Marketing opt-in won't break the CRM app or the Command Centre filters, and that "Newsletter" is a recognised Source.

### 4.7 Test steps (staging first, then live with the scenario on only after sign-off)

Use internal test addresses on the convenexevents.com domain, or a test domain.

1. **Fake success removed:** with Make scenario A **off**, submit a valid email with the box ticked. Expect the server error message, **not** "subscribed" or "on the list". This proves nothing fakes success.
2. **Unticked box:** submit without ticking. Expect "Please tick the box..." and no request in DevTools > Network.
3. **Bad email:** `abc@` gives the invalid email message. No request.
4. **Personal domain:** `x@gmail.com` gives the work-email message. No request. Then POST the same address straight to the hook with curl: expect `{"ok":false,"error":"work_email"}` and no row.
5. **Consent bypass:** curl POST with `consent=no`: expect `{"ok":false,"error":"consent"}` and no row.
6. **Honeypot:** fill `#news-website` in DevTools and submit. Expect the success text, but no CRM row and no email.
7. **Time trap:** curl POST with `t=500`. Expect no row.
8. **Happy path (double opt-in):** new work email, box ticked. Expect the "Nearly done..." message only after the response arrives (watch Network). The CRM gets 1 row: Source Newsletter, Stage New, Owner blank, opt-in `pending`, Notes with the wording version. The confirmation email arrives, with no promotion in it.
9. **Confirm:** click the link. You land on `/newsletter-confirmed/`. The row is now opt-in `yes` with the confirmation note, the data store status is `confirmed` and the welcome email arrives. Click again: same page, no duplicate email.
10. **Expired link:** change the data store `created` to 8 days ago and click. You land on the expired page and the row is unchanged.
11. **Duplicate:** submit the same email twice within 10 minutes. 1 row, 1 email.
12. **Already subscribed:** submit a confirmed email. "You're already on the list", no row, no email.
13. **Existing contact:** submit an email already in the CRM as an Outbound prospect with opt-in `no`. No new row. After confirming, opt-in `yes`; Source, Stage and Owner are unchanged.
14. **Sheets failure:** temporarily point step 6 at a missing sheet. Expect the server error message, not success.
15. **Throttle:** submit twice within 60 s from the same browser. The second gives the throttle message.
16. **Pages:** check 5 sample pages (home, contact-us, sponsor, one sector page, one venue page) plus mobile (iPhone Safari, Android Chrome). Check the checkbox is tappable, the link opens and keyboard tab order is email > consent > link > button (the honeypot is skipped).
17. **Email clients:** render 3.4 and 3.5 in Gmail, Outlook and Apple Mail, on desktop and mobile.
18. **Clean-up:** delete all test rows from the CRM and the data store. Purge the FlyingPress cache after the live page edits.
19. **Log:** record the result in the Convene X Agent Jobs sheet (Agent: Kai, Title: Footer newsletter form fix, Needs approval for: switching on Make scenarios A-C).

---

## 5. For Eleanor: GDPR and PECR check before go-live

*(Eleanor adds her not-legal-advice note to her reply.)*

1. **Consent wording (3.2):** is it specific and informed enough? Is the scope right (newsletter **and** event invitations, or newsletter only)? Is the first-person wording okay?
2. **Double opt-in vs single:** confirm the recommendation for UK and EU visitors.
3. **Privacy policy** (`/convene-x-events-privacy-policy/`, last updated 7 June 2026) **doesn't mention the newsletter at all.** It needs:
   - newsletter sign-up as a purpose, with **consent** as the lawful basis, and how to withdraw;
   - the processors and where data goes: Make (EU, eu1), Google Sheets/Google Workspace (possible US transfer), Zoho Mail, and later Brevo;
   - a retention period for subscribers and for unconfirmed sign-ups (proposed: unconfirmed deleted after 30 days; subscribers reviewed after 24 months without engagement, as in Amara's playbook);
   - a correction: section 6 promises an "Unsubscribe link in our emails". Manual Zoho Mail sends must actually include one (reply or mailto route, 2.3);
   - a check on section 4's "processing within the United Kingdom" claim against Make (EU) and Google.
4. **Consent record:** is timestamp + wording version + wording text + page URL + confirmation timestamp enough? Or do we also capture IP and user-agent (turn on "Get request headers" in the hook)? Data minimisation suggests no, unless Eleanor wants it.
5. **Company details:** the site footer and the draft emails show "Registered in England & Wales" and the registered office but **no company number**. Companies Act disclosure on websites and business emails needs the number. [CONFIRM THIS] Also note the privacy policy calls us "a Wales-based business".
6. **Previously lost sign-ups:** if `/cx/v1/newsletter` stored any addresses, decide what happens to them (proposed: not mailed, deleted, because there's no consent record).
7. **Related flags found during this check (not part of this fix, for Eleanor and Jordan):**
   - Make 8415814 (network waitlist) writes Marketing opt-in **"yes" for every submission**, whatever the waitlist's consent box says.
   - Make 8397919 (planning brief) replies `{"ok":true}` **before** writing the CRM row (errors ignored), and the visitor email is **signed with a personal name**, which is against the house rule. The Eva scenario was fixed the same way on 10 Nov (see `backups/eva-8263231-before-2026-11-10.md`).

---

## 6. Sign-off checklist

| Step | Who | Status |
|---|---|---|
| Copy (3.1-3.6) brand review | Felix | To do |
| Copy sign-off | Freya | To do |
| GDPR/PECR check (section 5) | Eleanor | To do |
| Double opt-in vs single opt-in decision | Nathan | To do (Amara recommends double) |
| Email copy approval (3.4, 3.5) | Nathan | To do. **Nothing sends before this.** |
| "pending" value and Source "Newsletter" in the CRM | Jordan | To do |
| Build on staging (4.1-4.5), tests (4.7) | Kai | After the above |
| Switch on Make scenarios A-C, live page edits | Kai, with Nathan's explicit go | After tests pass |
