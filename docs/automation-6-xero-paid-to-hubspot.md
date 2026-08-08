# Automation 6 — Xero invoice marked paid → update HubSpot deal

## Status
Draft-and-approve mode, same pattern as automations #1/#3. Read-only on the Xero side (no Xero write needed for this one), write-with-approval on the HubSpot side.

## Trigger
Invoices in Xero whose status is PAID, checked hourly via `get_invoices(status="PAID", ...)`.

## Dependency on automation #4
Matching a paid invoice to a HubSpot deal relies on the invoice's Reference field containing the HubSpot Deal ID. Automation #4 (Closed Won → draft Xero invoice) is meant to set that reference automatically, but **automation #4 can't be built yet** — the connected Xero integration only exposes read tools (get_invoices, get_contacts, get_aged_receivables, etc.), no create/write tool for invoices. Until #4 exists (or the Xero connector gets write access), whoever creates invoices manually in Xero needs to put the HubSpot Deal ID in the invoice Reference field for this automation to find the right deal.

## Logic
1. Pull recently-paid invoices from Xero (e.g. `get_invoices(status="PAID", issued_date_start=<~30 days back>)`).
2. For each, try to match the invoice's Reference field to `hs_object_id` on a HubSpot deal (`SELECT hs_object_id, dealname, description FROM DEAL WHERE hs_object_id = '<reference>'`).
3. No match → propose a HubSpot task flagging it ("Paid Xero invoice {invoice number} has no matching HubSpot deal reference — needs manual reconciliation"), same "don't fail silently" principle as automation #3.
4. Match found → check the deal's `description` for the marker `XEROPAID#{invoice number}` first (idempotency — skip if already logged). Otherwise propose appending: `[Automation] Payment received: Invoice {invoice number}, paid {payment date}, amount {amount} {currency}. XEROPAID#{invoice number}.` to the deal's description (fetch-then-append, never overwrite).
5. Present all pending proposals as a table and stop for approval. Carry forward unapproved proposals across wakes.

## How it runs
Persistent Claude Code session + hourly Routine, same architecture as automation #1.
- Session ID: `session_01TMJu31q6KFHMbQgqWENCK1`
- Routine (trigger) ID: `trig_01SRkWKbM8HGKwAd6S7bsFrR`, fires hourly at :55
