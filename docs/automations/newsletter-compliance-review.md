# Footer newsletter form: GDPR and PECR review

> **Not legal advice.** This is AI-generated analysis intended as a starting point only. Consult a licensed solicitor before signing any contract or relying on any generated document.

> Reviewer: Legal & Compliance (Eleanor). Written 10 Nov 2026, for Amara's spec `docs/automations/newsletter-form-fix.md` (sections 1 to 5).
> Owner of decisions: Nathan. Review chain for copy: Felix > Freya > Nathan.
> **Status: DRAFT.** Nothing has been changed, published, built, sent or edited in Make. All checks were read-only.

## What I checked (read-only)

| Source | How | What it showed |
|---|---|---|
| Live privacy policy, `/convene-x-events-privacy-policy/` | Firecrawl, `maxAge: 0` | "Last Updated: June 7, 2026". 8 sections. No newsletter, no processors, no retention, no transfers, no ICO complaint right, no legal entity details. Page is set `noindex`. |
| Make 8415814 "Convene X network waitlist to CRM" | `scenarios_get` | Active. Webhook > filter "Work email only" > Sheets addRow. Column 11 (Marketing opt-in) is the literal `"yes"`. The webhook receives no consent field at all. |
| `/join-the-network/` (page 11638) | WordPress `wp_get_page` | Consent box is `required`: "I'm happy for Convene X Events to contact me about events. See the privacy policy." The `sendBeacon` to Make sends 12 fields; `consent` is not one of them. |
| Make 8397919 "Convene X lead magnet downloads" | `scenarios_get` | Active. Order on the work-email route: notify email (4) > visitor email (8, errors **ignored**) > `WebhookRespond {"ok":true}` (6) > Sheets addRow (10, errors **ignored**). Visitor email signed with the founder's full name and "Founder". `Access-Control-Allow-Origin: *`. Footer has no company number. |
| `/planning-briefs/` (page 11789) | WordPress | **Draft**, not published (live URL returns "Page Not Found"). Has a required "store my details" box and a separate, optional, unticked "Send me occasional Convene X insights" box, sent as `optin` yes/no. |
| CRM sheet, column C (Source) | Google Sheets read | No "Join the Network", "Planning brief" or "Newsletter" rows yet. So neither problem in item 6 has touched real people's data so far. |
| Companies House | Public register | CONVENE X EVENTS LTD, company number **16933370**, registered office Fourth Floor, 14 Museum Place, Cardiff CF10 3BH, active, incorporated 29 Dec 2025. |

Not checked: the child-theme PHP behind `/wp-json/cx/v1/newsletter` (not readable over REST), and the n8n side of the waitlist (the n8n connection failed this session). Both stay on Kai's list in spec 4.6.

---

## Summary of verdicts

| # | Point | Verdict | Risk if left |
|---|---|---|---|
| 1 | Consent wording and scope | **Approve with edits.** Keep newsletter **and** event invitations, but name the event types and keep it one box. | [MEDIUM] |
| 2 | Double vs single opt-in | **Double opt-in. Agree with Amara.** One build change is essential: the confirm link must not confirm on a plain GET (link scanners will click it). | [HIGH] for the GET issue |
| 3 | Privacy policy | **Must be updated before the form goes live.** 14 tracked changes below (P1 to P14). | [HIGH] |
| 4 | Consent record | Version + server-side wording register + timestamps + page path. **No IP, no user-agent.** Keep for the subscription plus 6 years (solicitor to confirm). | [MEDIUM] |
| 5 | Company number | **Add 16933370** to the site footer, every email footer and the privacy policy. Nathan confirms against the certificate. | [MEDIUM] |
| 6a | Waitlist 8415814 hard-codes opt-in "yes" | Real problem, no live data yet. Fix before any newsletter send reads the opt-in column. | [MEDIUM] now, [HIGH] once newsletters go out |
| 6b | Planning brief 8397919 order and signature | Real problem, page still draft. Fix before the page is published. | [MEDIUM] |

---

## 1. Consent wording and scope

**Amara's draft (3.2):**
> Email me the Convene X Events newsletter and occasional invitations to events. I can unsubscribe at any time. Read our Privacy Policy.

**What works.** It names the sender, it's affirmative and unticked (spec 2.1), it says how to withdraw, it links to the policy, and it isn't a condition of anything else. First person is fine for a consent statement; I'd keep it.

**What needs to change.**
- **"invitations to events" is too loose.** It could read as anyone's events, including sponsors'. Consent has to be specific. Say whose events and what kind.
- **Sponsors.** Event invitations will include sponsor-hosted rooms. That's fine as long as Convene X is the sender and the subscriber's details don't go to the sponsor because they subscribed. The privacy policy addition (P5) says so. Don't put a sponsor promise in the checkbox itself; it would make the label too long.
- **One box or two?** Both are Convene X's own email marketing about the same subject, so one box is defensible and keeps the footer short. Two boxes would be more granular but would cost sign-ups for little gain. **I recommend one box** with the specific wording below. If Nathan wants the newsletter only, use the newsletter-only variant. Event invitations to those people would then rest on another basis: for UK corporate addresses, PECR allows B2B email with an opt-out, plus a documented legitimate interests assessment; for EU recipients, some member states (Germany in particular) expect consent for B2B email too. That needs a specialist if you rely on it.

**Wording change (tracked).**

| | Text |
|---|---|
| Was | Email me the Convene X Events newsletter and occasional invitations to events. I can unsubscribe at any time. Read our Privacy Policy. |
| **Now (recommended, v1-2026-11-10)** | Email me the Convene X Events newsletter and occasional invitations to Convene X Events dinners, roundtables and webinars. I can unsubscribe at any time. Read our [Privacy Policy](https://convenexevents.com/convene-x-events-privacy-policy/). |
| Newsletter-only variant (if Nathan chooses it) | Email me the Convene X Events newsletter. I can unsubscribe at any time. Read our [Privacy Policy](https://convenexevents.com/convene-x-events-privacy-policy/). |

If the label in 4.1 is changed, the version tag must change too. Since nothing has gone live, it's fine to keep `v1-2026-11-10` for whichever version ships, as long as the wording register (section 4) records the exact final text.

**Footer line (3.1)** "No noise, and you can leave any time." is fine.

**Other copy points in the spec (for Felix and Amara):**
- **[MEDIUM] Welcome email (3.5): "what senior leaders are raising at our tables".** Convene X hasn't run its own first event yet. This implies it has, which is the team-not-company problem in marketing-claims terms. Suggested: "what senior leaders are weighing up in their sectors, how good executive rooms get put together, and the dinners and roundtables coming up."
- **[LOW] "Already subscribed" message (3.3).** Anyone can type a colleague's address and learn whether they're on the list. Return the same "Nearly done..." message for already-subscribed addresses, and send nothing. Drop the `already` branch from the page script.
- **[LOW] Confirmation email (3.4).** "We won't add you to the list" is true, but we do keep a pending record for up to 30 days. Change the line to: "If you didn't ask for this, you can ignore this email. We won't add you to the list, and we'll delete your address within 30 days."
- The confirmation email must stay free of promotion, as Amara says. Keep it neutral: one email, sent straight away, no event plugs, no booking link.

## 2. Double opt-in versus single opt-in

**Recommendation: double opt-in.** I agree with Amara's reasons.

- Neither UK GDPR nor EU GDPR nor PECR says "double opt-in" in terms. What they do require is that you can **demonstrate** consent (UK and EU GDPR Article 7(1)). A footer form accepts any address anyone types. A click from that inbox is the strongest evidence you'll have.
- For EU visitors, double opt-in is widely treated as the expected way to evidence email consent, especially in Germany. Specialist point if you ever need to rely on it, but adopting it removes the question.
- For US visitors, CAN-SPAM is an opt-out regime, so consent plus double opt-in goes well beyond it. What CAN-SPAM does need in every commercial email: a working opt-out, honoured within 10 business days, and a valid physical postal address. The draft footers already have the address. (Verify detail with a solicitor if US sends become a large share.)

**Conditions that must be true for double opt-in to work as evidence:**

1. **[HIGH] The confirm link must not confirm on a plain GET.** Corporate mail filters (link-scanning services used by most large employers) open every link in an incoming email automatically. Scenario B as specified (4.4) would mark the address "yes" the moment a scanner opens the link, before the person sees the email. That would make our "proof of consent" worthless for exactly the senior corporate audience we want. Fix: the email link opens `/newsletter-confirmed/?t=...`, which shows a **"Confirm my sign-up" button**. The button sends a POST to the confirm hook. Only the POST changes the record. A GET to the hook does nothing but redirect to that page.
2. **"pending" means no marketing.** No newsletter, no invitation, and no Zoho Mail manual send to a row with opt-in "pending". Jordan should make sure any send list filters on the exact value "yes".
3. **Scenario C must only touch rows it set.** As written (4.5 step 2), the weekly clean-up sets opt-in "no" on the CRM row of every unconfirmed sign-up. For an existing contact (spec 2.3, "existing row"), that row's opt-in was never set to "pending", so the clean-up could overwrite a valid "yes" or a waitlist consent from another form. Change step 2 to: "only if the row's Marketing opt-in is currently `pending`".
4. **Do-not-contact list.** Before sending the confirmation email, check Jordan's do-not-contact list. If the address is on it, send nothing and return the normal "Nearly done" reply. Someone who objected to our emails shouldn't get one because a third party typed their address. If they really want back in, they can email enquiries@. (This is a cautious choice; Nathan can relax it.)
5. **Single opt-in variant**, if Nathan chooses it anyway: lawful if the box is ticked and recorded, but weaker evidence and more risk of mailing people who never asked. If chosen, I'd still want the consent record in section 4 and a first-send audit by Jordan.

## 3. Privacy policy: gaps and tracked additions

### 3.1 Gaps found in the live policy (7 June 2026)

Amara's list is right. Reading the live page, I found more:

| Gap | Why it matters | Risk |
|---|---|---|
| No newsletter purpose, lawful basis or withdrawal route | People must be told this when we collect their data (UK and EU GDPR Article 13). | [HIGH] |
| No legal entity details: "Convene X Events" only, no "Ltd", no company number, no registered office | The controller's identity and contact details are a required item. | [HIGH] |
| No list of processors or recipients (Make, Google, Zoho, n8n and others) | Recipients or categories of recipients are required. | [MEDIUM] |
| Section 4 says processing is in the UK and "approved secure jurisdictions"; Make is EU (eu1), Google may be US, Zoho location unconfirmed | Transfers outside the UK and the safeguard used must be stated. The current wording overstates. | [MEDIUM] |
| No retention periods | Required item. | [HIGH] |
| Section 6 promises an "Unsubscribe link in our emails"; manual Zoho sends don't have one | A promise in the policy we don't keep. | [MEDIUM] |
| Rights list is partial: no restriction, portability, or right to withdraw consent; **no right to complain to the ICO** | Required items. | [HIGH] |
| Only UK GDPR named; we collect from EU visitors | EU GDPR applies to EU visitors we market to. Possible EU representative requirement (Article 27) has an exemption for occasional, low-risk processing. **Needs a specialist.** | [MEDIUM] |
| Section 3: event registration shares "Business Email Address" with sponsors, under legitimate interests, but also says "you acknowledge and agree" | Mixed basis (consent language for an LI basis). It also conflicts with our internal rule that sponsors get name, title, company and LinkedIn only, not email, unless the attendee consents to sponsor email. Out of scope for this fix, but it should be put right in the same update. | [HIGH], separate item |
| Section 2 describes the site as a BuddyBoss community with "subscribing to groups" | Check this still describes the site. Out of scope. | [LOW] |
| "Last Updated" date | Must change with any edit. | n/a |

The `noindex` setting on the policy page isn't a legal problem, as long as the page is linked from every form (it is).

### 3.2 Tracked list of additions (DRAFT, not published)

Insert or replace exactly as below. Text in **[CONFIRM: ...]** needs Nathan or a vendor check before publishing. **The whole updated policy should go to the solicitor before it goes live**, in line with how the T&C were handled.

**P1. Header date.**
- Replace: `Last Updated: June 7, 2026`
- With: `Last updated: [date of publication] 2026`

**P2. Section 1, Overview: who we are.** Add after the first paragraph:
> Convene X Events Ltd is the controller of your personal data. We're a private limited company registered in England and Wales, company number 16933370. Our registered office is Fourth Floor, 14 Museum Place, Cardiff CF10 3BH. You can contact us about anything in this policy at enquiries@convenexevents.com.
>
> This policy applies to people in the UK, the European Economic Area and elsewhere who use our website, sign up to our emails or take part in our events. Where we say "UK GDPR", the same rights apply to you under the EU General Data Protection Regulation if you're in the EEA.

**P3. Section 2, Data Collection and Sources.** Add a bullet after "Direct Collection":
> - Newsletter sign-up: when you sign up to our newsletter, we collect your work email address, the date and time, the page you signed up on, the version of the sign-up wording you agreed to, and the date and time you confirmed by email. If you reply to our welcome email with your sector and role, we add those too.

**P4. New section 3, "Our newsletter and event invitations".** Insert before the current section 3 and renumber the rest:
> **3. Our newsletter and event invitations**
>
> - What you get: our newsletter, sent occasionally, and occasional invitations to Convene X Events dinners, roundtables and webinars. *[If Nathan chooses newsletter only: delete "and occasional invitations..."]*
> - Lawful basis: your consent. You give it by ticking the box on our sign-up form and then confirming from the email we send you. Until you confirm, we don't send you anything else.
> - Withdrawing consent: you can unsubscribe at any time, for free, by replying "unsubscribe" to any of our emails, by using the unsubscribe link where an email has one, or by emailing enquiries@convenexevents.com with the subject "Unsubscribe". We act on it within 2 working days. Withdrawing doesn't affect anything we sent before.
> - We keep a short record that you unsubscribed (your email address and the date) so we don't email you again.
> - Work addresses only: our sign-up form accepts work email addresses only.

**P5. Newsletter and sponsors.** Add as the last bullet of the new section 3:
> - We don't share newsletter subscribers' details with event sponsors. Your details only go to a sponsor if you register for or attend a sponsored event, as explained in section 4. **[CONFIRM: true in practice, and Jordan's sponsor exports exclude newsletter-only rows]**

**P6. New section, "Who processes your data for us".** Insert after the sponsor section:
> **5. Who processes your data for us**
>
> We use these service providers to run our website, emails and records. They act on our instructions:
>
> | Provider | What for | Where data is held |
> |---|---|---|
> | Make (Celonis) | Moving sign-ups and enquiries from our website into our records, and sending confirmation emails | European Union **[CONFIRM: eu1 region]** |
> | Google (Sheets and Workspace) | Our contact and pipeline records | **[CONFIRM: account type and region; may include the United States]** |
> | Zoho (Zoho Mail) | Sending and receiving email, including our newsletter | **[CONFIRM: zoho.eu or zoho.com data centre]** |
> | n8n | Processing waitlist requests from our website | **[CONFIRM: region]** |
> | Our website host and WordPress | Running convenexevents.com | **[CONFIRM: host and region]** |
>
> If we change providers (for example to a dedicated email platform), we'll update this list.

Note for Nathan: Cal.com, Jotform, Apollo.io, the Eva chat assistant's AI provider and the cookie/analytics tools also process personal data and belong in this table. They're outside this fix, but the table should be complete when the policy is republished.

**P7. Section 4 (now 6), Data Security: replace the UK-only line.**
- Replace: `As a Wales-based business, we prioritise the secure handling, processing, and storage of data within the United Kingdom and approved secure jurisdictions.`
- With:
> We're based in Wales, UK. Some of our providers hold data outside the UK, in the European Union and the United States. Transfers to the EU rely on the UK's adequacy regulations for the EEA. Transfers to the United States rely on the UK Extension to the EU-US Data Privacy Framework where the provider is certified, or otherwise on the UK International Data Transfer Addendum to the EU Standard Contractual Clauses. You can ask us for details of the safeguard for any provider. **[CONFIRM per provider; solicitor to check]**

**P8. New section, "How long we keep your data".**
> **7. How long we keep your data**
>
> - Newsletter sign-ups that are never confirmed: deleted within 30 days of sign-up.
> - Newsletter subscribers: kept while you're subscribed. We review subscribers we've had no contact with for 24 months and remove them unless they tell us they want to stay.
> - Unsubscribe and objection records: your email address and the date, kept for as long as we need them to make sure we don't contact you again.
> - Consent records (what you agreed to, when and where): kept while you're subscribed and for 6 years after, so we can show we had your consent. **[CONFIRM with solicitor; see review section 4]**
> - Other records (events, sponsors, enquiries): **[Nathan and Eleanor to set; outside this fix]**

**P9. Section 6 (now 8), Your Rights: replace the unsubscribe bullet.**
- Replace: `Right to Object / Unsubscribe: You can opt-out of direct communications from us at any time by clicking the "Unsubscribe" link in our emails.`
- With:
> Right to object and to unsubscribe: you can stop our marketing emails at any time. Reply "unsubscribe" to any email from us, use the unsubscribe link where an email has one, or email enquiries@convenexevents.com with the subject "Unsubscribe". Your objection to direct marketing is always respected, without exception.

**P10. Your Rights: add the missing rights.** Add these bullets:
> - Right of access: you can ask for a copy of the personal data we hold about you.
> - Right to rectification: you can ask us to correct data that's wrong or incomplete.
> - Right to restriction and to data portability, where they apply.
> - Right to withdraw consent: where we rely on your consent, you can withdraw it at any time.
>
> We reply to rights requests within one month. If a request is complex, we may extend this by up to two more months and we'll tell you why within the first month.

**P11. Your Rights: erasure timing.** Keep "up to 7 business days" only if Grace and Jordan can meet it across the CRM, Make data store, Zoho Mail and backups. Otherwise replace with: `We'll complete erasure requests within one month.`

**P12. Your Rights: right to complain.** Add as the last bullet:
> - Right to complain: if you're unhappy with how we've handled your data, you can complain to the Information Commissioner's Office (ico.org.uk). If you're in the EEA, you can also complain to the data protection authority where you live or work. We'd appreciate the chance to put things right first, so please contact us at enquiries@convenexevents.com.

**P13. Section 3 (now 4), sponsor sharing: flag only, wording for the solicitor.** Not part of this fix, but don't republish the policy without addressing it. Replace "By registering for and attending an event on our platform, you acknowledge and agree that your professional contact details (Name, Job Title, Company Name, and Business Email Address) will be shared" with wording that matches our actual practice (name, title, company and LinkedIn URL after the event; email only with the attendee's specific consent) and a single lawful basis. **Solicitor to settle.**

**P14. Section 8, Contact Us.** Replace the bullet with:
> - Email: enquiries@convenexevents.com
> - Post: Convene X Events Ltd, Fourth Floor, 14 Museum Place, Cardiff CF10 3BH

## 4. The consent record

**Store these for every sign-up (Make data store `cx_newsletter_doi`, plus a summary line in CRM Notes):**

| Field | Store? | Notes |
|---|---|---|
| Email (lower-cased) | Yes | |
| Sign-up timestamp (UTC, server time) | Yes | Use Make's `now`, not the browser's clock. |
| Consent wording version | Yes | e.g. `v1-2026-11-10`. |
| Consent wording text | Yes, but **the authoritative copy is server-side** | The spec takes the text from the page (`consent_text`). A scripted request could send anything. Keep a **wording register** (a small table in this repo: version, exact text, date live, date retired, pages) and treat the version as the evidence. The submitted text is a cross-check only. |
| Source page | Yes, **path only** | Use `location.origin + location.pathname`, not `location.href`. Full URLs can carry query strings with tracking IDs or, occasionally, personal data. |
| Form identifier | Yes | e.g. `footer-newsletter`. |
| Confirmation timestamp | Yes | Set only by the POST from the confirmation page (see 2.1). |
| Confirmation method | Yes | e.g. `email-link-button`. |
| Status | Yes | pending / confirmed / expired / withdrawn. |
| Withdrawal timestamp and method | **Add** | Missing from the spec. Needed for accountability and for the suppression list. Whoever handles enquiries@ records it when actioning an unsubscribe. |
| IP address | **No** | Personal data, and it adds little: the confirmation click is far better evidence that the inbox owner agreed. Data minimisation points the same way. Revisit only if Brevo (which logs this itself) is adopted. |
| User-agent / request headers | **No** | Leave "Get request headers" off in the Make hook, as Amara proposes. |

**How long to keep it:**
- Unconfirmed: token expires after 7 days; record and CRM row deleted within 30 days (agree with Amara's proposal).
- Confirmed: for the life of the subscription and **6 years after it ends**, minimal fields only (email, version, timestamps, page, status). Six years lines up with UK limitation periods, so the record exists if a claim or complaint ever needs answering. A solicitor may prefer a shorter period (2 to 3 years is also defensible for marketing consent); that's their call. **Solicitor to confirm.**
- Scenario C must never delete or expire a **confirmed** record.
- Make data stores have size limits. Jordan should add a quarterly export of confirmed and withdrawn records to the CRM's records so evidence doesn't sit only in Make.

**Previously lost sign-ups** (spec 5.6): agree. If `/cx/v1/newsletter` stored any addresses, don't mail them and don't import them as opted in. Record the count and date in this file, then delete them. There's no consent record, and an email asking them to confirm would itself be a marketing email.

## 5. Company number and trading disclosures

- **Finding:** the site footer ("© 2026 Convene X Events Ltd. Registered in England & Wales." plus the registered office), the draft emails (3.4, 3.5) and the live planning-brief email all leave out the company number. The privacy policy names no legal entity at all.
- **Rule in plain English:** a UK company must show its registered name, registered number, where it's registered and its registered office address on its website and in its business emails. This comes from the Companies Act 2006 trading disclosure rules (the Company, Limited Liability Partnership and Business (Names and Trading Disclosures) Regulations 2015), and the Electronic Commerce (EC Directive) Regulations 2002 also expect the registration number on a business website. **Solicitor to confirm the references.** If the company is VAT-registered, the VAT number also belongs on the website. Priya to confirm whether it is.
- **Number from the public register:** **16933370** (Companies House, checked 10 Nov 2026). Registered office on the register: Fourth Floor, 14 Museum Place, Cardiff CF10 3BH, which matches the site. **Nathan to confirm against the certificate of incorporation**, including whether the company is registered as "England and Wales" or "Wales", before anything goes live.

**Exact wording (replace `[CONFIRM THIS]` everywhere):**

- Site footer (all ~42 pages, can go in the same edit as the form):
  > © 2026 Convene X Events Ltd. Registered in England and Wales, company number 16933370. Registered office: Fourth Floor, 14 Museum Place, Cardiff CF10 3BH.
- Email footers (3.4, 3.5, the planning-brief email, and the manual Zoho newsletter template):
  > Convene X Events Ltd. Registered in England and Wales, company number 16933370.
  > Registered office: Fourth Floor, 14 Museum Place, Cardiff CF10 3BH.
- The spec's "4th Floor" is fine; "Fourth Floor" just matches the register.
- Side note for Grace: the register shows the first confirmation statement due by 11 January 2027.

## 6. Problems in other Make scenarios

### 6a. Waitlist, Make 8415814: every sign-up marked opted in

**Confirmed.** Column 11 (Marketing opt-in) is the literal `"yes"`. The page's `sendBeacon` payload doesn't include `consent`, so Make couldn't read the box even if it tried.

**What softens it:** the box is `required` and the form has no `novalidate`, so a normal browser submit only fires once the box is ticked. And the CRM has no "Join the Network" rows yet, so no one has been mis-recorded.

**What's still wrong:**
1. **[HIGH once newsletters go out] Wrong scope.** The waitlist box says "contact me about events". Writing "yes" in the shared Marketing opt-in column makes those people look like newsletter subscribers. The moment Amara's newsletter goes to everyone with "yes", waitlist people get a newsletter they never agreed to.
2. **[MEDIUM] No evidence.** No wording version, no timestamp of consent, no record of what the box said. We couldn't show their consent if asked.
3. **[MEDIUM] Writes "yes" for requests the site rejected.** The beacon fires on submit, before n8n validates. If n8n rejects the request (bad LinkedIn URL, spam), Make still writes a "yes" row. And anyone who reads the hook URL in the page source can POST to it directly and create "yes" rows with no box at all.
4. **[LOW] Two copies.** Data goes to both n8n and Make. Both need to be in the privacy policy (P6), and both need to honour erasure requests.

**Recommended fix (Kai builds, Jordan owns the values; not done):**
- Page script: add `consent: f.elements.consent.checked ? 'yes' : 'no'` and `consent_version: 'waitlist-v1-2026-10-08'` (or whatever date that wording went live) to the beacon payload.
- Make: add `{{1.consent}}` equals `yes` to the "Work email only" filter, so no row without consent.
- Make column 11: write a **scope-limited** value, not "yes". I recommend Jordan defines the opt-in vocabulary for the whole CRM, for example: `no`, `pending`, `events` (event invitations only), `yes` (newsletter and event invitations). Waitlist rows write `events`. Newsletter sends go to `yes` only; event invitations go to `events` or `yes`.
- Make column 17 (Notes): append `Consent: waitlist box, wording {{1.consent_version}}, {{formatDate(now; "YYYY-MM-DD HH:mm"; "UTC")}} UTC.`
- Add the waitlist wording to the wording register (section 4).
- Optional: move the beacon to fire only after n8n accepts, or have n8n write the CRM row instead, so there's one path.

### 6b. Planning brief, Make 8397919: replies before the CRM row, personal-name signature

**Confirmed.** Route order is notify (4) > visitor email (8, errors ignored) > `{"ok":true}` reply (6) > Sheets addRow (10, errors ignored). The visitor email signs off with the founder's full name and title. The page is still a **draft**, so there's no live exposure unless the hook is called from somewhere else. The scenario itself is **active**.

**Risks:**
1. **[MEDIUM] Silent loss of the consent choice.** If the Sheets write fails, the visitor sees success and gets the email, but no CRM row exists. Their `optin` choice is lost. If they opted out, a later manual list built from Gmail notifications could pick them up. If they opted in, we have no record of it. Either way, accountability fails.
2. **[MEDIUM] Marketing content in an email to people who said no.** The visitor email includes "tell us who you'd invite" and "book 15 minutes" links, and goes to everyone, including people who left the "insights" box unticked. A message sent because someone asked for a download is fine. Adding promotion to it for someone who declined marketing is the grey area PECR enforcement has focused on. Remove the two promotional links for `optin = no` (use `if()` in the HTML), or remove them for everyone.
3. **[LOW legal, house-rule breach] Personal name.** Against the house rule (no personal names in public output). Legally it's the founder's own data, but it also ties every lead to one person. Sign off as "The Convene X Events team".
4. **[MEDIUM] Footer disclosures.** No company number and no "Registered in England and Wales". Use the section 5 footer. The existing "reply unsubscribe" line is good; keep it.
5. **[LOW] `Access-Control-Allow-Origin: *`.** Any website can call this hook and read the reply. Restrict it to `https://convenexevents.com`, as Amara does for the new scenario.
6. **[LOW] Sending account.** Email account 12775186 and the notification address are a consumer Gmail account. Consumer Google accounts don't come with the same business data processing terms as Google Workspace. Send from a convenexevents.com address (Amara's spec 4.6 item 5), and **confirm who owns the CRM spreadsheet**. If it's in the consumer Gmail account, moving it into a business account with processor terms should be on the list. Needs a check, not a guess.
7. **[LOW] Consent for storing details.** The required box says "I agree that Convene X Events can store my details to send me this brief". Storing details to fulfil a request doesn't need consent (it's closer to legitimate interests or steps at the person's request). Asking for consent you don't need muddies things, but it's harmless. Leave it, and tidy it when the page is next edited: "We'll use your details to send you this brief. See the privacy policy." as plain text, not a checkbox.

**Recommended fix (Kai, after a backup like the Eva change; not done):**
- New order on the work-email route: **Sheets addRow** (error handler: `WebhookRespond {"ok":false,"error":"server"}`, then stop; not Ignore) > **visitor email** (error handler: respond `{"ok":false,"error":"server"}`, so the page shows the error and the mailto fallback) > **`{"ok":true}` reply** > internal notify (Ignore errors is fine here).
- Add Notes text: `Planning brief. Insights opt-in {{1.optin}}, wording pb-v1-2026-11-06, {{formatDate(now; "YYYY-MM-DD HH:mm"; "UTC")}} UTC.` Add both planning-brief box wordings to the register.
- Column 11: write `yes` only for `optin = yes`, and that "yes" means "occasional insights" (newsletter). It doesn't cover event invitations. Under the vocabulary above, Jordan may want a separate value (e.g. `newsletter`). His call.
- Visitor email: signature "The Convene X Events team"; footer per section 5; promotional links only when `optin = yes`.
- `Access-Control-Allow-Origin: https://convenexevents.com`.
- Don't publish `/planning-briefs/` until these are done. Nathan may want the scenario switched off until then; that's his call, and I haven't touched it.

---

## Other build points in the spec (for Kai and Amara)

- **[MEDIUM] Consent text from the client.** See section 4: version is authoritative; keep the wording register.
- **[LOW] `page: location.href`** in 4.2: change to `location.origin + location.pathname`.
- **[LOW] Unsubscribe handling (2.3).** 2 working days is fine (CAN-SPAM's outer limit is 10 business days; PECR expects prompt action). Whoever actions it must also update the data store record to `withdrawn` and add the address to the do-not-contact list.
- **[LOW] Work-email-only rule.** Agree it's a brand choice. Note that a company domain doesn't prove a corporate subscriber under PECR (sole traders and some partnerships count as individuals). With consent, it doesn't matter.
- **[INFO] Eva chat.** On the live privacy page, the Eva details form says "Leave your details and Nathan will get back to you", while the planning-brief page's copy says "the team". That's a house-rule issue on some pages, not a legal one. Kai to check which pages still carry the old wording.

---

## What must be true before Kai builds

1. **Nathan decides:** double opt-in (recommended) and scope (newsletter **and** Convene X Events dinners, roundtables and webinars, recommended; or newsletter only).
2. **Consent label** uses the section 1 wording, and the final text is entered in a **wording register** in this repo with its version tag.
3. **Confirm step uses a button and a POST**, not a GET link (section 2, condition 1). Scenario B and `/newsletter-confirmed/` change accordingly.
4. **Scenario C** only changes rows whose opt-in is `pending` and never deletes confirmed records.
5. **Do-not-contact check** before the confirmation email.
6. **"Already subscribed"** returns the same reply as a new sign-up.
7. **Jordan** confirms the opt-in vocabulary (`no` / `pending` / `events` / `yes`, or his version) and that every send list filters on the right value.
8. **Company number 16933370** is confirmed by Nathan and goes in the site footer, all email footers and the privacy policy.
9. **Privacy policy changes P1 to P12 and P14** are drafted into a full revised policy, the [CONFIRM] items are checked (Make region, Google account type and region, Zoho data centre, n8n region, host), it goes to the solicitor, and **it's published before or at the same moment the new form goes live.** P13 (sponsor sharing) is fixed in the same republish.
10. **Welcome email** loses "at our tables" (team-not-company).
11. **Sending address** is on convenexevents.com, not the consumer Gmail account.
12. **Waitlist 8415814** is fixed (section 6a) **before** the first newsletter is sent, so waitlist rows can't be mistaken for newsletter consent.
13. **`/cx/v1/newsletter`**: Kai reports whether it stored anything. If it did, record the count here and delete; don't mail.
14. Build on staging only. Make scenarios stay **off** until Nathan gives the explicit go.

Building on staging (step 4.1 to 4.5 of the spec, with the changes above) can start once 1 to 7 are settled. Switching on and publishing the live form needs 8 to 12 as well.

## Open points for a solicitor

- Final privacy policy text, especially transfers (P7), retention (P8) and sponsor sharing (P13).
- Whether Convene X needs an EU representative under EU GDPR Article 27, given it invites and markets to people in the EU.
- Retention of consent records (6 years proposed).
- Trading disclosure references in section 5.

---

## Log

| Date | Item | Result | Outcome (from solicitor or Nathan) |
|---|---|---|---|
| 2026-11-10 | Newsletter form spec, sections 1 to 5; Make 8415814 and 8397919 (read-only) | This review. Nothing changed live. | To be filled in |
