# Freya sign-off and go-list for Kai: content drafts, 10 Nov 2026

Signed off by: Head of Marketing & Content, 10 Nov 2026. Felix's brand and quality review was done first on every file (see the top of each file).
Scope: indexing plan fixes 4 (B5), 5 (B6) and 6 (B7). Every file has a "Freya sign-off" section under Felix's, and my edits are already made in the files.
**I have not touched the live site.** Kai applies only what's listed under "Apply now", and only once Nathan has approved this list. That's the house rule: nothing goes live without his sign-off.

---

## 1. Apply now (after Nathan's approval)

Apply each file's sections 1 to 4 (opening, copy block, FAQ plus FAQPage schema, carousel), plus its "Elsewhere on this page" notes and the conditions in my sign-off. Felix's carousel/tile/amenity rule applies to every venue page: walk times, Michelin claims, royal warrants, founding/"since" lines, "58th Floor", "longest-standing" and AV claims come off unless they're on the venue's own site and listed in section 5. If in doubt, remove.

| # | File | Page | Verdict | Conditions for Kai |
|---|---|---|---|---|
| 1 | venue-10707-the-connaught.md | 10707 | Approved with edits | None beyond the tile rule |
| 2 | venue-10709-the-lanesborough.md | 10709 | Approved | None |
| 3 | venue-10710-the-dorchester.md | 10710 | Approved | None |
| 4 | venue-10711-the-goring.md | 10711 | Approved with edits | The Michelin line stays (attributed to the hotel) |
| 5 | venue-10712-the-beaumont.md | 10712 | Approved | Address and schema become Brown Hart Gardens, W1K 6TF. Remove "Cub Room" |
| 6 | venue-10713-the-stafford.md | 10713 | Approved with edits | None |
| 7 | venue-10714-browns-hotel.md | 10714 | Approved with edits | No per-room Roosevelt/Niagara figures, combined 80 only |
| 8 | venue-10715-nomad-london.md | 10715 | Approved with edits (overrides Felix's hold) | **No capacity anywhere.** The tile reads "Capacity on request" or goes. Leave the address and schema as they are now |
| 9 | venue-10716-royal-automobile-club.md | 10716 | Approved with edits, kept "by arrangement" | Capacity tile reads "By arrangement". Short descriptors elsewhere read "Member-sponsored, by arrangement" |
| 10 | venue-9476-soho-hotel.md | 9476 | Approved | Leave the address and schema as they are now |
| 11 | venue-9477-claridges.md | 9477 | Approved with edits | None |
| 12 | venue-9478-the-ned.md | 9478 | Approved with edits | The carousel uses Covent Garden Hotel in place of Horizon 22 (already in the file) |
| 13 | venue-9479-searcys-horizon-22.md | 9479 | Approved with edits | Leave the postcode and schema as they are now. Remove "58th Floor" and "Private Dining Suite (30)" |
| 14 | venue-9480-haymarket-hotel.md | 9480 | Approved | The tile shows "Up to 22" once |
| 15 | venue-9481-covent-garden-hotel.md | 9481 | Approved | Remove the "All executive dinners run under the Chatham House Rule" line |
| 16 | merge-8987.md | 8987 (+ 301 from 8782) | Approved with edits | **One release:** body and meta, then the 301, then the inbound links, then 8782 to draft. If the 301 can't be made over the MCP, don't ship the body. Ask Nathan to add the redirect by hand first |

After each page: verify logged out after a FlyingPress purge, then hand to Callum for the pre-publish check. Nathan requests indexing only after a page is live (plan section C).

## 2. Interim fix for a held page (apply now, after Nathan's approval)

**The Ivy Club (10717): strip the wrong facts and add nothing.**
1. Delete: "For a private dinner, the Loft seats up to 30 guests and the Private Dining Room up to 18, giving flexibility for a tightly curated table or a slightly larger gathering."
2. Remove the "Up to 30" capacity tile, the walk-time tile and "Audio-visual support available", plus any matching schema `description` text.
3. Address block and schema: 9 West Street, WC2H 9NE (the club's own homepage).
4. Leave the rest of the page and its carousel unchanged.

## 3. Held, and why

| File | Why it's held | What unblocks it |
|---|---|---|
| venue-10717-the-ivy-club.md | The club describes "members' only private dining", and The Private Room may be The Ivy restaurant's room. If a non-member host can't book it, the page promotes a venue our sponsors can't use. | Nathan or Marcus emails the club: can a non-member company host in The Loft, and who owns and books The Private Room? If the answer to the first is yes, Felix does a quick re-check and then Kai applies. Nathan: hold the GSC indexing request until then. |
| join-merge-9517.md | Copy approved; **build blocked.** The `cx/v1/join` handler is unknown, Eleanor hasn't answered on consent and the GDPR basis, the n8n redirects still point at /join-the-network/, and the footer newsletter form drops sign-ups. | All 4 closed, then Kai builds from the file as it stands. Nathan also confirms "nothing recorded" as a policy and whether invitations name the host. |

## 4. My decisions on Felix's points

1. **Horizon 22:** it's dropped from the executive-dinner set and the page stays as a large-format venue. It comes out of The Ned's carousel (Covent Garden Hotel goes in). Copy no longer claims breakfasts or awards evenings as our formats.
2. **Royal Automobile Club:** kept, marked "by arrangement". The member-sponsorship rule is stated plainly in the copy.
3. **The Ivy Club:** held, with the interim strip above. I won't publish copy written to step around whether the venue can be booked at all.
4. **NoMad London:** approved now, with no capacities and the address left unchanged. Holding it would leave wrong figures live, and the new copy adds nothing unverified. The working rule for the set: publish when the copy holds only verified facts and the venue is genuinely open to our hosts. Hold when the venue's availability is in doubt.
5. **/join/ hosting line:** it doesn't hold. It's now "Some rooms are hosted by a partner organisation that covers the cost; others we run ourselves." Chatham House becomes "where relevant" in the facts strip, and it's removed from the meta description.
6. **Dinner seats:** **10 to 25 everywhere**, per the brand brief. Venue copy that described *our* table at 8 now says 10. Room facts from the venue stay as published. Pages that still say 8 to 25 aren't in this go-list (see follow-ups).
7. **"34 events" vs the ban on event counts:** **the ban wins for public copy.** A team count sitting next to a company that hasn't run its first event reads as a company claim, the reader can't check it, and the "18 months" window dates. None of these drafts use it, so nothing changes here. Nathan to confirm, then the Story Vault line in brand-brief.md is updated to match. Proof stays as the team "in previous roles", with no counts. Also note that brand-voice.md, which the role files refer to, isn't in the repo.
8. **/sponsor/ band:** **yes, to Iris for a rewrite.** Founder/"his career" language breaks the no-names rule in spirit, and pipeline promises break "never promise sponsors leads or ROI". It's a high-priority follow-up, ideally live before Nathan requests indexing for /sponsor/ (GSC Day 1). It isn't rewritten here.

## 5. Follow-ups (not authorised by this go-list)

- Callum: list every live page still saying "8 to 25" (or similar) for dinners. One known example is the /join-the-network/ card, which goes away with the merge. Also check the guest counts in /executive-roundtable-vs-executive-dinner/ against the brief (roundtables 6 to 12 virtual, dinners 10 to 25). Iris corrects, then Felix, me and Nathan sign off.
- Iris: /sponsor/ band rewrite (point 8).
- Kai: say where Horizon 22 appears on /london-venues/ and the homepage venue list so the wording there can stop calling it a dinner room.
- Marcus: correct the Drive sheet "London Private Dining Venues", or mark it unverified. Nobody should use it as a source for public copy.
- Nathan or Marcus: confirm the open venue facts with the venues: NoMad capacities and address, Brown's Roosevelt/Niagara, Haymarket Rocklin, Horizon 22 postcode, Soho Hotel address.
- Recheck The Goring's Michelin status before any republish.
