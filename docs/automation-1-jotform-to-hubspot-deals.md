# Automation 1 — Jotform submission → HubSpot deal

## Status
Draft-and-approve mode. Live via a Claude Code Routine, not standalone code — see "How it runs" below.

## Trigger
New submissions on exactly two of the five Jotform forms:
- **New Deal Form** (id `262186498450062`)
- **New Deal Registration** (id `262168382728062`)

Explicitly *not* triggered by: Sponsorship Agreement — Signature (that's automation #3, updates an existing deal), Event Kick-Off Form, or Audience Builder (post-sale operational forms with no company/package/price data — firing deal creation off these would create bogus duplicate "Appointment Scheduled" deals).

## Field mapping

**Contact** (search by email first; propose UPDATE if found, CREATE if not):
| HubSpot property | Source |
|---|---|
| `email` | Primary Contact Email / Main contact email |
| `firstname`/`lastname` | Parsed from Primary Contact Name / Main contact name |
| `company` | Company Name / Sponsor Name |
| `jobtitle` | Job Title |
| `phone` | Primary Contact Phone Number / Main contact mobile |

**Deal** (pipeline `default`, stage `appointmentscheduled`):
| HubSpot property | Source |
|---|---|
| `dealname` | `{Company/Sponsor Name} — {Package Selection} (JF#{submission_id})` — the `JF#` suffix is the idempotency key |
| `amount` | Total fee (excl. VAT), or Custom price if set (New Deal Registration only — New Deal Form has no price field) |
| `dealtype` | `existingbusiness` if "Has the sponsor worked with us before?" = Yes, else `newbusiness` |
| associations | Contact from above |

Fields with no clean HubSpot property home (PO Number, VAT Number, Billing Address, Sales Person, marketing-fund flag, event(s) selected, pricing notes) are captured in a note attached to the deal so nothing captured on the form is silently dropped.

## Idempotency
Before proposing a create, run `SELECT hs_object_id FROM DEAL WHERE dealname LIKE '%JF#<submission_id>%'`. A match means it's already been created — skip. No custom HubSpot property was created for this (the available HubSpot tools can't define new properties); the submission ID embedded in the deal name is the dedup key and is visible to humans in the HubSpot UI.

## How it runs
This automation is **not** a script executed by a host process. It runs as a **Claude Code Routine**:
- A persistent Claude Code session ("Automation 1 — Jotform → HubSpot Deals") holds the full process instructions above.
- An hourly Routine wakes that session, which checks both forms for submissions not yet represented as a deal.
- The session **proposes** creates/updates as a table and stops — it never calls the HubSpot write tool unattended, because that tool requires a live human's explicit approval on every write, and a scheduled firing has no human present.
- A human (routine owner) reviews and replies to approve (all or a subset) in that same session; only then does the agent execute the write, since a real approval was just given in that turn.
- Pending (unapproved) proposals are carried forward and re-shown, not silently dropped or re-proposed as new.

- Session ID: `session_012iMa6qMoTcVzivFDZot2hK` ("Automation 1 — Jotform → HubSpot Deals")
- Routine (trigger) ID: `trig_01PsXRzTRhrb72dARUD955tH`, fires hourly at :45
- Verified 2026-08-08: fired once manually, completed with tool access intact, correctly reported no new submissions (both source forms have zero submissions at time of writing)

## Why draft-and-approve instead of fully unattended
The brief calls automation #1 an internal system-to-system update that shouldn't need per-item human review. In practice, the connected HubSpot tool enforces a confirmation step on every write regardless, and a scheduled Routine firing has no human present to satisfy it. Rather than have the agent fabricate approval on an unattended run, the owner chose (2026-08-08) to keep a human in the loop for HubSpot/Xero writes across all six automations, checking in on each Routine firing instead of it running fully silently. This is more manual than the brief envisioned but preserves the actual intent of the confirmation safeguard.

## Not yet built
Automations #2–6, per the brief's suggested build order (build and prove #1 and #5 before touching #2, since #2 touches the sending workflow).
