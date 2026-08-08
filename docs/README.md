# Convene X Events automation — status overview

Six automations connecting Jotform, HubSpot, Xero, and Gmail. Each runs as a persistent Claude
Code session woken hourly by a Routine (trigger), rather than as standalone hosted code — see
each automation's doc for why. All CRM/financial writes go through a draft-and-approve gate: the
routine proposes changes and stops, and only writes once a human replies approving in that
session's conversation.

| # | Automation | Status | Doc |
|---|---|---|---|
| 1 | Jotform (New Deal Form / New Deal Registration) → HubSpot deal | **Live**, hourly, draft-and-approve | [automation-1-jotform-to-hubspot-deals.md](automation-1-jotform-to-hubspot-deals.md) |
| 2 | HubSpot "Contract Sent" → Gmail draft (never sent) | **Built, disabled** — per brief, wait until #1 and #5 are proven | [automation-2-contract-sent-draft-email.md](automation-2-contract-sent-draft-email.md) |
| 3 | Sponsorship Agreement signed → update HubSpot deal | **Live**, hourly, draft-and-approve | [automation-3-sponsorship-agreement-to-hubspot.md](automation-3-sponsorship-agreement-to-hubspot.md) |
| 4 | HubSpot "Closed Won" → draft Xero invoice | **Blocked** — the connected Xero integration is read-only, no write tool exists | *(no session yet — see below)* |
| 5 | New email to enquiries@/sales@ → HubSpot task | **Live but dormant** — those addresses aren't reaching this environment's Gmail yet | [automation-5-enquiry-email-to-hubspot-task.md](automation-5-enquiry-email-to-hubspot-task.md) |
| 6 | Xero invoice paid → update HubSpot deal | **Live**, hourly, draft-and-approve, read-only on Xero | [automation-6-xero-paid-to-hubspot.md](automation-6-xero-paid-to-hubspot.md) |

## Two open items that need a decision from the business owner

1. **Automation #4 is not built yet.** The Xero integration connected to this environment only
   exposes reporting tools (get_invoices, get_contacts, get_aged_receivables, etc.) — there is no
   create/write tool for invoices at all. This isn't a safety gate that can be satisfied with
   approval, like the HubSpot ones — the capability simply isn't there. Decision (2026-08-08): get
   the Xero connector granted write access first, then build #4 properly — draft invoice creation
   matched to the deal, 0% VAT, same draft-and-approve pattern as the other automations. Once
   write access is added, tell Claude and it can be built the same session.
2. **enquiries@/sales@convenexevents.com aren't reachable yet.** They're being set up on Neo Mail,
   a separate host from the Gmail account connected here (convenexevents@gmail.com). Automations
   #5 and #2 are built against the right `to:` addresses and `Deal ID:` conventions, so they
   should start working with no changes once mail forwarding (or a direct connector) is in place —
   there's just nothing for them to find yet.

## Common conventions across automations
- **Idempotency:** since there's no spare HubSpot custom property available to mark records as
  processed, dedupe markers are embedded directly in existing fields — `JF#{jotform_submission_id}`
  in the deal name (automation #1) or appended to the deal description (automations #3/#6), and
  `Deal ID: {hs_object_id}` in Gmail draft bodies (automation #2, matched against via list_drafts).
- **The Deal ID chain:** automation #2 puts the HubSpot Deal ID in the agreement email → the
  client copies it into the Sponsorship Agreement form's reference field → automation #3 matches
  it back to the deal → (once #4 exists) the invoice reference carries the same ID → automation #6
  matches paid invoices back to the deal the same way.
