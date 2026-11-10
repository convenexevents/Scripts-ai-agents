# Venue page draft: The Ivy Club (page 10717)

## Felix review (Brand & Quality), 10 Nov 2026

**Verdict: Pass with edits. Not ready for go-live until the member-access question is answered (Freya).**

Spot-checked against the-ivyclub.co.uk with Firecrawl (home, /privatedining/, /the-loft/, /the-private-room/). Loft figures, timings, Brudnizki and the September 2008 opening all check out. Changes:
- **Directions were wrong.** The draft sent guests to The Ivy restaurant's entrance. The club's homepage says the club entrance is further up West Street, through The Flower Shop on the left. Fixed in the copy and the FAQ.
- **The Private Room:** the club's page calls it "The Private Room at The Ivy" and compares it with "the restaurant downstairs", so it may be The Ivy restaurant's room rather than the club's. Copy now says the club's private dining pages list it, rather than presenting it as a club room. Kai/Nathan to confirm with the events team.
- **Address resolved:** the club homepage gives 9 West Street, WC2H 9NE. Use that in the address block and schema.
- "Dinner runs from 18:30..." is a Loft timing, so the copy now says so.
- **Member access (Freya):** the club's private dining index is described as "members' only private dining". Until we know a non-member host can book, this page shouldn't be promoted to sponsors.

## Freya sign-off (Head of Marketing & Content), 10 Nov 2026

**Verdict: Not approved. HELD. Apply the interim fix below now.**

- Decision: **hold.** This isn't a copy problem. The club describes "members' only private dining", and The Private Room may belong to The Ivy restaurant rather than the club. If a non-member host can't book it, the whole page promotes a room our sponsors can't use. Writing copy that steps around that point would be a quiet form of misleading, so I won't publish it.
- **Interim fix: yes, Kai removes the wrong facts from the live page now.** Strip only; add no new copy:
  1. Delete the sentence "For a private dinner, the Loft seats up to 30 guests and the Private Dining Room up to 18, giving flexibility for a tightly curated table or a slightly larger gathering."
  2. Remove the "Up to 30" capacity tile, the walk-time tile and "Audio-visual support available" (and any matching schema `description` text).
  3. Change the address block and schema to the club's own address: 9 West Street, WC2H 9NE (from the club homepage, confirmed by Felix).
  4. Leave the carousel as it is until the full copy goes in.
- Edit for when this resumes: "a table of 8 to 10" becomes "a table of 10 to 12".
- To unblock (Nathan or Marcus, by email to the club's events team): (1) Can a non-member company host a private dinner in The Loft? (2) Is The Private Room the club's or The Ivy restaurant's, and is it bookable through the club? If the answer to (1) is yes, this file goes back to Felix for a 5-minute check and then to Kai.
- Nathan: don't request indexing for this URL (GSC Day 2 list) until it's resolved.

Status: **DRAFT for Felix's review.** Nothing has been changed on the live site.
Plan item: B6 (make venue pages genuinely distinct). Kai builds after Felix > Freya.
Page: `/the-ivy-club-london-private-dining-venue/`
Verification: **Verified, with 2 items to confirm (address, non-member access)**

## 1. New opening sentence

Replaces the first sentence of "About this venue" (the shared template line "...well suited to executive dinners in London... the polish of a genuinely premium London address").

> Three floors above The Ivy on West Street, The Ivy Club gives a Covent Garden dinner a private home of its own, close to Leicester Square.

## 2. New venue-specific copy block (234 words)

Replaces the remaining "About this venue" paragraphs, including the shared closing paragraph ("Convene X curates the full evening here..."), which is identical on every venue page.

The Ivy Club opened in September 2008 across three floors above The Ivy restaurant, with interiors by designer Martin Brudnizki. Its private dining pages list two rooms.

**The Loft** sits on the top floor. By day, light comes through the club's harlequin windows; in the evening, rich fabrics and contemporary art set a quieter tone. It holds up to 50 seated or 100 standing, so a table of 20 or so senior guests has room to breathe, and a short drinks welcome can run in the same space before everyone sits down.

The club's pages also list **The Private Room** at The Ivy, which seats up to 60, or 100 standing. A refurbishment added a bespoke bar and a collection of contemporary art alongside the signature harlequin stained glass and oak panelling.

Both rooms are generous for an executive dinner, which makes The Ivy Club a better fit for a slightly larger evening: a sector dinner for 20 to 30 marketing, technology or professional-services leaders who know the West End, with drinks and dinner in one room. For a table of 10 to 12, a smaller room elsewhere in the portfolio will feel more intimate.

Dinner in The Loft runs from 18:30 to midnight, with host access from 18:00. The nearest Tube is Leicester Square: leave by Exit 3, walk up Charing Cross Road and turn right into Litchfield Street. On West Street, walk past The Ivy to The Flower Shop on your left, which is the club's entrance.

## 3. FAQ (3 questions, for an FAQ block plus FAQPage schema)

**Q: How many guests can The Ivy Club seat for a private dinner?**
A: The Loft seats up to 50 and the Private Room up to 60, according to the club. Both suit a dinner of around 20 to 30 better than a very small table.

**Q: Which room at The Ivy Club suits a drinks reception before dinner?**
A: The Loft holds 100 standing as well as 50 seated, so a short reception and the dinner can happen in the same room without moving guests.

**Q: How do guests get to The Ivy Club?**
A: The nearest Tube is Leicester Square. From Exit 3, walk up Charing Cross Road and turn right into Litchfield Street. The club's entrance is further up West Street, through The Flower Shop on the left.

## 4. "Other rooms in the portfolio" carousel: keep these only

Cut the 15-card carousel to these 4 nearby venues (same card markup, other cards removed):

1. NoMad London (Covent Garden)
2. Covent Garden Hotel (Seven Dials)
3. The Soho Hotel (Soho)
4. Haymarket Hotel (St James's / Trafalgar Square)

## 5. Sources (venue's own website)

- https://the-ivyclub.co.uk/ (opened September 2008, three floors above The Ivy restaurant; Martin Brudnizki design, meta description)
- https://the-ivyclub.co.uk/privatedining/ (two private dining rooms: The Private Room, The Loft)
- https://the-ivyclub.co.uk/privatedining/the-loft/ (top floor, 50 seated / 100 standing, harlequin windows, timings, travel directions, events contact 9 West St WC2H 9NE)
- https://the-ivyclub.co.uk/privatedining/the-private-room/ (60 seated / 100 standing, Brudnizki refurbishment, bespoke bar, harlequin stained glass, oak panelling)

## 6. Unverified items, corrections and flags

- **Live page is wrong on capacity and room names.** It says 'the Loft seats up to 30 and the Private Dining Room up to 18' and shows an 'Up to 30' tile. Official: The Loft 50 seated, The Private Room 60 seated. The room is called 'The Private Room', not 'Private Dining Room'. These figures came from the Drive sheet 'London Private Dining Venues', which doesn't match the venue site.
- **Address to confirm.** Our page uses 1-5 West St, WC2H 9NQ (The Ivy restaurant). The club's events contact address is 9 West St, WC2H 9NE. Kai should confirm which to show and update the schema `streetAddress` and `postalCode` to match.
- **Member access.** The club's private dining index is described as 'members' only private dining'. The enquiry form is public, but whether a non-member host can book wasn't stated. Confirm with the club before we promote it to sponsors. The copy and FAQ avoid the point.
- Exactly where The Private Room sits in the building isn't stated (the club says it's 'as glamorous ... as the restaurant downstairs'). I haven't given a floor.
- Audio-visual support: not confirmed on the club's pages (the Loft page mentions 'screenings and presentations' as uses). Left out of the copy; remove 'Audio-visual support available' from the amenities list unless confirmed.
- '3 minutes' walk from Leicester Square' (summary tile): not on the club site. Left out of the copy.
- Drive sheet phone/email (020 3301 0200, events@theivyclub.co.uk) differ from the club site (0203 727 6548, events@theivy-collection.com). Internal only, but the sheet needs correcting.

### Elsewhere on this page (Kai, when applying)

- **Felix decision (carousel cards, summary tiles, amenities):** remove walk times, Michelin claims, royal warrants, founding dates and "since" lines, "58th Floor", "longest-standing" and AV claims, unless the fact is on the venue's own site and listed in section 5. Default is remove.

- Update the summary tiles, the "What this venue offers" list and the schema `description` so they match the copy above. Remove any room name, capacity or feature listed in section 6 as wrong or unverified.
- Keep the address and access block, but don't add walk times that aren't in the copy unless they're checked.
- No personal names; no claim that Convene X has hosted here.
