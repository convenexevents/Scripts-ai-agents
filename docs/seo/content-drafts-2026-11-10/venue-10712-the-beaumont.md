# Venue page draft: The Beaumont (page 10712)

## Felix review (Brand & Quality), 10 Nov 2026

**Verdict: Pass with edits.**

Spot-checked against thebeaumont.com with Firecrawl (occasions, Lotos, Sargent, Munnings, contact). Room names and all capacities match. Changes:
- **Address was wrong.** The hotel's contact page gives "Brown Hart Gardens, London, W1K 6TF", not 8 Balderton Street. The opening ("off Balderton Street") and closing line are fixed. Kai: check the live address block and schema `streetAddress`.
- **Opening over-claimed.** "Three panelled private rooms" isn't true of the Munnings Room, which has gold wall coverings. Opening rewritten. The Munnings paragraph now carries its real character (equestrian paintings by Alfred Munnings and George Stubbs).
- Sargent Room: "a screen is built in" becomes the hotel's own wording, a plasma screen for presentations.
- Munnings figures are now confirmed from a full scrape, not just a search excerpt.

Status: **DRAFT for Felix's review.** Nothing has been changed on the live site.
Plan item: B6 (make venue pages genuinely distinct). Kai builds after Felix > Freya.
Page: `/the-beaumont-london-private-dining-venue/`
Verification: **Fully verified**

## 1. New opening sentence

Replaces the first sentence of "About this venue" (the shared template line "...well suited to executive dinners in London... the polish of a genuinely premium London address").

> The Beaumont, on Brown Hart Gardens in Mayfair, has three private rooms, each hung with art and each as ready for a boardroom table as for dinner.

## 2. New venue-specific copy block (213 words)

Replaces the remaining "About this venue" paragraphs, including the shared closing paragraph ("Convene X curates the full evening here..."), which is identical on every venue page.

The Beaumont's private rooms seat from 10 to 45, and each can be set around one boardroom table, which suits a dinner built around a single conversation.

**The Sargent Room**, on the ground floor, has natural daylight, mahogany panelling and paintings by Kees van Dongen and John Singer Sargent. Its hand-made boardroom table seats 20, or it can be laid for up to 30 at three tables. It also has a plasma screen for presentations.

**The Lotos Room**, at 68 m², is panelled in banded cherrywood and walnut and hung with portraits of 1920s and 1930s film stars by Hollywood photographer George Hurrell. An 18-seat boardroom table sits at its centre; set for dining, it takes 45 at separate tables, or 60 for drinks.

**The Munnings Room**, at 72 m², is the largest and lightest of the three, with gold wall coverings and equestrian paintings by Alfred Munnings and George Stubbs. It seats up to 40 at four tables or 60 standing, with a 24-seat boardroom table available for business use.

For a peer dinner of 16 to 20, the Sargent Room's single table or the Lotos Room's 18-seat table puts everyone in one conversation, which is how we'd run it. The Munnings Room suits a larger dinner of 30 to 40 at separate tables, with a drinks welcome in the same room. The hotel is on Brown Hart Gardens, W1K 6TF.

## 3. FAQ (3 questions, for an FAQ block plus FAQPage schema)

**Q: How many private rooms does The Beaumont have?**
A: Three: the Lotos Room, the Sargent Room and the Munnings Room, seating from 10 to 45 between them, according to the hotel.

**Q: Which Beaumont room suits a single-table dinner for 20?**
A: The Sargent Room, whose hand-made boardroom table seats 20. The Lotos Room has an 18-seat boardroom table.

**Q: Can The Beaumont host a drinks reception before dinner?**
A: Yes. The Lotos Room and the Munnings Room each hold up to 60 standing, and the Sargent Room up to 50.

## 4. "Other rooms in the portfolio" carousel: keep these only

Cut the 15-card carousel to these 4 nearby venues (same card markup, other cards removed):

1. Claridge's (Brook Street, Mayfair)
2. The Connaught (Mayfair)
3. Brown's Hotel (Mayfair)
4. The Dorchester (Park Lane)

## 5. Sources (venue's own website)

- https://thebeaumont.com/occasions/ (three private rooms: Lotos, Sargent, Munnings; seating 10 to 45, up to 60 standing)
- https://thebeaumont.com/occasions/the-lotos-room/ (68 m², cherrywood and walnut, 18-seat boardroom table, George Hurrell portraits, 45 dining / 60 standing)
- https://thebeaumont.com/occasions/the-sargent-room/ (ground floor, daylight, mahogany, boardroom table for 20, 30 at three tables, 50 standing, van Dongen and Sargent paintings, plasma screen)
- https://thebeaumont.com/occasions/the-munnings-room/ (72 m², gold wall coverings, Munnings and Stubbs paintings, 40 at four tables, 60 standing, 24-seat boardroom table; full page checked by Felix)
- https://thebeaumont.com/contact/ (address: Brown Hart Gardens, London, W1K 6TF)

## 6. Unverified items, corrections and flags

- **Live page names a room that isn't on the hotel site.** It says 'the Lotos Room seats up to 30 guests and the Cub Room up to 16'. There's no 'Cub Room' among the hotel's private rooms; the three are Lotos, Sargent and Munnings. Lotos dining is 45 (18 at the boardroom table), not 30.
- Munnings Room figures come from the official page's search excerpt; I didn't scrape that page in full.
- Nearest Tube 'Bond Street, 4 minutes': not on the hotel site. Left out.

### Elsewhere on this page (Kai, when applying)

- **Felix decision (carousel cards, summary tiles, amenities):** remove walk times, Michelin claims, royal warrants, founding dates and "since" lines, "58th Floor", "longest-standing" and AV claims, unless the fact is on the venue's own site and listed in section 5. Default is remove.

- Update the summary tiles, the "What this venue offers" list and the schema `description` so they match the copy above. Remove any room name, capacity or feature listed in section 6 as wrong or unverified.
- Keep the address and access block, but don't add walk times that aren't in the copy unless they're checked.
- No personal names; no claim that Convene X has hosted here.
