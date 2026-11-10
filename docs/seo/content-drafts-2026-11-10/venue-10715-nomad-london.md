# Venue page draft: NoMad London (page 10715)

## Felix review (Brand & Quality), 10 Nov 2026

**Verdict: Pass with edits. Hold go-live until the hotel's events team confirms capacities and the address.**

- The address line is removed from the copy. It came from our page and the Drive sheet, not the hotel. Kai can show it in the address block once it's confirmed.
- The sector-fit sentence contrasted NoMad with "a formal hotel dining room", but NoMad is a hotel. Rewritten.
- FAQ answer 1 said "entrance through the original courtroom entrance". Fixed.
- No capacities are published, and that's correct: third-party listings are not sources.

Status: **DRAFT for Felix's review.** Nothing has been changed on the live site.
Plan item: B6 (make venue pages genuinely distinct). Kai builds after Felix > Freya.
Page: `/nomad-london-private-dining-venue/`
Verification: **Partly verified (official site blocked the scraper; room capacities not verified)**

## 1. New opening sentence

Replaces the first sentence of "About this venue" (the shared template line "...well suited to executive dinners in London... the polish of a genuinely premium London address").

> NoMad London occupies the former Bow Street Magistrates' Court, and the original courtroom is now the Magistrates' Ballroom, with two private dining rooms beside it.

## 2. New venue-specific copy block (161 words)

Replaces the remaining "About this venue" paragraphs, including the shared closing paragraph ("Convene X curates the full evening here..."), which is identical on every venue page.

NoMad London's events floor is built around the building's history. The original Magistrates' Courtroom has been reimagined as the **Magistrates' Ballroom**, a formal space with two adjacent private dining rooms, a separate bar, and its own street entrance through the original courtroom doors. The hotel offers more than 800 m² of event space in total.

**The Fielding Room** is a private dining space off the Magistrates' Ballroom. It connects to **the De Veil Room**, which has its own full bar, so drinks and dinner can run side by side without guests crossing the hotel.

That layout suits a two-part evening: a short reception in the De Veil Room, then a single-table dinner in the Fielding Room, with a dedicated entrance that keeps arrivals discreet. It suits technology, media and marketing leaders who'd rather spend the evening in Covent Garden than in a traditional Mayfair dining room.

## 3. FAQ (3 questions, for an FAQ block plus FAQPage schema)

**Q: What's the history of NoMad London's event spaces?**
A: The hotel's Magistrates' Ballroom is the building's original Magistrates' Courtroom, with its own street entrance through the original courtroom doors.

**Q: Which NoMad London room suits a private dinner?**
A: The Fielding Room, a private dining space off the Magistrates' Ballroom, connected to the De Veil Room and its bar. We'd confirm the seated capacity with the hotel for your numbers.

**Q: Does NoMad London have a separate entrance for events?**
A: Yes. The Magistrates' Ballroom and its adjoining private dining rooms have a dedicated entrance from the street.

## 4. "Other rooms in the portfolio" carousel: keep these only

Cut the 15-card carousel to these 4 nearby venues (same card markup, other cards removed):

1. Covent Garden Hotel (Seven Dials)
2. The Ivy Club (Covent Garden)
3. The Ned (City)
4. Haymarket Hotel (St James's / Trafalgar Square)

## 5. Sources (venue's own website)

- https://www.hilton.com/en/hotels/lonnmnd-nomad-london/ (official hotel page; search excerpt: over 800 m² of event space; Magistrates' Courtroom now the Magistrates' Ballroom, two adjacent private dining rooms, separate bar, dedicated street entrance)
- https://www.hilton.com/en/hotels/lonnmnd-nomad-london/events/ (official events page; search excerpt: Fielding Room is a private dining space off the Magistrates' Ballroom, connected to the De Veil Room with a full bar). A direct scrape returned 403, so only the search excerpts were read.

## 6. Unverified items, corrections and flags

- **Room capacities not verified from the official site.** Third-party listings (Hire Space, The Vendry, Cvent) give the Fielding Room about 30 and the De Veil Room 10-30 depending on layout. Not used. Kai or Nathan to get figures from the hotel's events team before we publish numbers. Copy is 150 words partly for this reason.
- **Live page is wrong on rooms.** 'The Magistrates Room up to 16' doesn't match: the space is the Magistrates' Ballroom, a large formal room. 'Fielding Room seats up to 30' is third-party only.
- Address '28 Bow Street, WC2E 7AW': from our page and Drive sheet; not re-checked on the official page.
- The sector-fit sentence is my judgement, not a venue claim.
- 'Covent Garden, 3 minutes' and AV: not verified. Left out.

### Elsewhere on this page (Kai, when applying)

- **Felix decision (carousel cards, summary tiles, amenities):** remove walk times, Michelin claims, royal warrants, founding dates and "since" lines, "58th Floor", "longest-standing" and AV claims, unless the fact is on the venue's own site and listed in section 5. Default is remove.

- Update the summary tiles, the "What this venue offers" list and the schema `description` so they match the copy above. Remove any room name, capacity or feature listed in section 6 as wrong or unverified.
- Keep the address and access block, but don't add walk times that aren't in the copy unless they're checked.
- No personal names; no claim that Convene X has hosted here.
