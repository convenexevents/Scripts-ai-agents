# Automation 5 — New enquiry email → HubSpot task

## Status
**Built but dormant** — see "Known gap" below. Draft-and-approve is not really needed for the
HubSpot task creation itself (see Approach), but the automation still can't do anything useful
yet because the mail it's supposed to watch doesn't reach the connected mailbox.

## Known gap: enquiries@ / sales@ aren't on Gmail
The brief assumed Gmail/Google Workspace mailboxes for enquiries@convenexevents.com and
sales@convenexevents.com. In reality (checked 2026-08-08), those addresses are being set up on
**Neo Mail** (neo.space), a separate email host — password-setup emails for both only arrived
today, forwarded as copies into convenexevents@gmail.com, which is the only mailbox this
environment's Gmail connector has access to. A direct search for `to:enquiries@convenexevents.com
OR to:sales@convenexevents.com` against that connector returns zero results, and will continue to
until one of these happens:
- Neo Mail is configured to forward enquiries@/sales@ mail into convenexevents@gmail.com (or
  another Gmail/Workspace mailbox this environment can reach) with original headers intact, or
- A Gmail/Workspace connector for the actual enquiries@/sales@ mailboxes gets connected to this
  environment.

The automation is built against the `to:` address, not which mailbox received it, so **no changes
should be needed once mail actually starts arriving** — it'll just start finding threads.
Until then it runs hourly and harmlessly reports nothing found.

## Trigger
New Gmail threads addressed to enquiries@convenexevents.com or sales@convenexevents.com.

**Scope discipline:** the connected mailbox (convenexevents@gmail.com) has ~1,500 messages, almost
all unrelated personal/account mail. The search query must stay hard-scoped to the `to:` filter
above — never broadened to "all unread" or similar, which would flood HubSpot with tasks for
irrelevant mail.

## Approach
Same draft-and-approve gate as automations #1/#3/#6 — HubSpot task creation goes through the same
CRM-object confirmation requirement as deals/contacts, so it's proposed and held for a human to
approve, not created directly. (An earlier draft of this automation's briefing said task creation
could skip approval as "low stakes" — that was a mistake, corrected before the automation ever
ran live, since the owner's approval-gate decision was meant to apply to all HubSpot/Xero writes
with no carve-outs.)

## Logic
1. Ensure two Gmail labels exist (create if missing): `Automation-5/Pending Review`,
   `Automation-5/Task Created`.
2. Search threads: `to:enquiries@convenexevents.com OR to:sales@convenexevents.com` minus threads
   already carrying the `Task Created` label.
3. For each new thread: work out a proposed HubSpot task titled `Review enquiry from {sender}`
   with the subject/snippet and a link back to the thread in the task notes, and check for an
   existing HubSpot contact matching the sender's email to propose associating (don't create a new
   contact — out of scope for this automation). Present as a table and stop for approval, carrying
   forward anything still unapproved from earlier wakes.
4. Only once a human approves: create the task(s) for real, then label the corresponding thread(s)
   `Automation-5/Task Created`.
5. Report a one-line summary each wake (how many pending/new proposals, or "nothing new").

## How it runs
Persistent Claude Code session + hourly Routine.
- Session ID: `session_01RuZrLtusdKT3Eoip7Hjgcr`
- Routine (trigger) ID: `trig_01F37Gw4B32M493qR5419hgh`, fires hourly at :05
