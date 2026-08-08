# Automation 2 — Deal reaches "Contract Sent" → draft email (not sent)

## Status
**Built, but disabled.** Per the brief's own build order ("Don't build #2 until #1 and #5 are
proven stable, since #2 touches the sending workflow"), the Routine exists but is turned off. Ask
to have it enabled once #1 and #5 have run reliably against real submissions/emails.

## Trigger
HubSpot deals that have reached the `contractsent` stage.

## Why no chat-approval gate on this one
Unlike #1/#3/#5/#6, this automation's own design is already the review step: it creates a Gmail
**draft**, never sends. A human still has to open it and hit send. Adding a second "approve in
chat" gate on top of that would be redundant, so the routine creates the draft directly. (It does
NOT touch HubSpot at all, so the CRM confirmation-gate question that applies to the other
automations doesn't come up here.)

## Known caveat — same mailbox mismatch as automation #5
The draft gets created in convenexevents@gmail.com's Drafts folder, since that's the only mailbox
this environment can reach. If sales actually operates out of sales@convenexevents.com (on Neo
Mail, not yet forwarding here — see automation #5's doc), someone will need to go find the draft
in convenexevents@gmail.com rather than their usual inbox, or manually copy it over. Revisit once
the enquiries@/sales@ mailbox setup is sorted.

## Logic
1. Query HubSpot: `SELECT hs_object_id, dealname, description FROM DEAL WHERE dealstage = 'contractsent'`.
2. For each: check existing Gmail drafts (list_drafts) for one that already mentions `Deal ID: {hs_object_id}` — if found, skip (already drafted, dedupe without needing a HubSpot write).
3. Otherwise, find the deal's associated contact's email, and create a Gmail draft:
   - To: the contact's email
   - Subject: `Sponsorship Agreement — {dealname}`
   - Body: a short note plus the Sponsorship Agreement — Signature form link (https://form.jotform.com/262194432902051) and clearly stated `Deal ID: {hs_object_id}` — the recipient needs to carry this ID into the form's "Deal / Invoice Reference Number" field, which is what lets automation #3 match the signature back to this deal.
4. Report a one-line summary each wake (how many drafts created, or "nothing new").

## How it runs
Persistent Claude Code session + hourly Routine — currently **disabled**.
- Session ID: `session_01GFNTMWv4fpFQkkSPjmFcw3`
- Routine (trigger) ID: `trig_012f8JYzK3LfY5js7FLYkAek`, would fire hourly at :15 once enabled (currently `enabled: false`)
