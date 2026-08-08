# Automation 3 — Sponsorship Agreement signed → update HubSpot deal

## Status
Draft-and-approve mode, same pattern as automation #1.

## Trigger
New submissions on **Sponsorship Agreement — Signature** (form id `262194432902051`).

## Dependency on automation #2
This form's "Deal / Invoice Reference Number" field is expected to be the raw HubSpot Deal ID
(`hs_object_id`), because automation #2 puts that ID in the draft email alongside the agreement
link. Automation #2 isn't built yet (it's last in the build order), so until it exists, whoever
sends the agreement link manually must include the HubSpot Deal ID as the reference number for
this automation to match correctly.

## Logic
1. List recent submissions on the form.
2. For each, look up `SELECT hs_object_id, dealname, dealstage, description FROM DEAL WHERE hs_object_id = '<reference number>'`.
3. **Match found:**
   - If `dealstage` is earlier than `decisionmakerboughtin` (appointmentscheduled / qualifiedtobuy / presentationscheduled / contractsent), propose moving it to `decisionmakerboughtin`. Never propose moving a deal backward (e.g. leave `closedwon` alone) — just propose the log note.
   - Propose appending a line to the deal's `description` property (fetch current value first, append — never overwrite): `[Automation] Sponsorship agreement signed by {Signatory Full Name} ({Signatory Job Title}) on {Date Signed}. JF#{submission_id}.` The `JF#{submission_id}` marker is the idempotency key — before proposing, check the existing `description` for that marker via `WHERE description LIKE '%JF#<submission_id>%'` and skip if already present.
4. **No match found:** Per the brief, don't fail silently. Propose creating a HubSpot task: "URGENT: Sponsorship Agreement signed with no matching Deal (ref: {reference}, company: {Sponsor/Company Name}, signed {Date Signed})" so a human is guaranteed to see it.
5. Present all pending proposals as a table and stop for approval, same as automation #1. Carry forward unapproved proposals across wakes.

## How it runs
Persistent Claude Code session + hourly Routine, same architecture as automation #1.
- Session ID: `session_013XnwAreFchiC8DaTNq3fDh`
- Routine (trigger) ID: `trig_01JNiSp4jsRqGnh4fmtHiui3`, fires hourly at :50
