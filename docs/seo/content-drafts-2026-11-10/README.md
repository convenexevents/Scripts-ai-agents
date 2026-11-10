# Content drafts, 10 November 2026 (indexing plan fixes B5, B6, B7)

Source plan: `docs/seo/indexing-fix-plan-2026-11-10.md`.
Drafted by: Senior Content Writer. **All files are drafts. Nothing has been changed on the live site.**
Pipeline: Felix (brand/quality) > Freya (sign-off) > Nathan (approval) > Kai applies > Callum pre-publish check.

## Files

| File | Plan item | What it is | Status |
|---|---|---|---|
| `merge-8987.md` | B5 (+ B10, part of B3) | Full new body (HTML) for post 8987 `/b2b-virtual-roundtable-guide/`, folding in 8782's unique material; new meta; internal links; drop list; 301 note for `/how-to-host-a-virtual-roundtable/` | Draft, ready for Felix |
| `join-merge-9517.md` | B7 | Merged page copy for `/join/`, full form audit of both pages, recommended form, reconnect checklist, meta | Draft. **Blocked for build** until Kai confirms what `POST /wp-json/cx/v1/join` does (see file, section 1) |
| `venue-10717-the-ivy-club.md` | B6 | The Ivy Club | Verified; confirm address and non-member access |
| `venue-10707-the-connaught.md` | B6 | The Connaught | Fully verified |
| `venue-10709-the-lanesborough.md` | B6 | The Lanesborough | Fully verified |
| `venue-10710-the-dorchester.md` | B6 | The Dorchester | Fully verified |
| `venue-10711-the-goring.md` | B6 | The Goring | Verified; Silver Room capacity not published |
| `venue-10712-the-beaumont.md` | B6 | The Beaumont | Fully verified |
| `venue-10713-the-stafford.md` | B6 | The Stafford London | Fully verified |
| `venue-9477-claridges.md` | B6 | Claridge's | Fully verified |
| `venue-9478-the-ned.md` | B6 | The Ned | Fully verified |
| `venue-10714-browns-hotel.md` | B6 | Brown's Hotel | Verified; hotel site conflicts on Roosevelt/Niagara capacities |
| `venue-10716-royal-automobile-club.md` | B6 | Royal Automobile Club | Fully verified; events need a member sponsor |
| `venue-9476-soho-hotel.md` | B6 | The Soho Hotel | Verified for 2 rooms |
| `venue-9480-haymarket-hotel.md` | B6 | Haymarket Hotel | Verified; Nash/Rocklin figures identical on hotel site |
| `venue-9481-covent-garden-hotel.md` | B6 | Covent Garden Hotel | Fully verified |
| `venue-9479-searcys-horizon-22.md` | B6 | Searcys Horizon 22 | Partly verified; no small private room found; fit question for Freya |
| `venue-10715-nomad-london.md` | B6 | NoMad London | Partly verified; official site blocked the scraper, no capacities verified |

Each venue file has: new opening sentence, a 150 to 300 word copy block, a 3-question FAQ, 3 to 4 carousel picks, sources (venue's own site), and unverified items/corrections.

## Things Felix, Freya and Kai need to know before anything is built

1. **The live venue pages carry wrong room names and capacities on most of the 16 pages.** They were built from the Drive sheet "London Private Dining Venues" (and `London_Private_Dining_Venues_v2.xlsx`), which doesn't match the venues' own websites. Examples: Royal Automobile Club "Mountbatten Room up to 18" (official 210); The Beaumont "Cub Room" (no such private room); The Ned "Wren Room" (not on The Ned's list); Horizon 22 "Private Dining Suite (30)" (not found); The Ivy Club "Loft up to 30" (official 50). Each venue file lists the corrections. This is a factual accuracy problem on live pages, separate from indexing, and worth fixing even if the new copy waits.
2. **The Drive venue sheet should be corrected or marked as unverified** (Marcus owns venues). Until then, nobody should use it as a source for public copy.
3. **Carousel card blurbs** on every venue page contain claims I didn't verify in this pass: Connaught and Dorchester "Michelin-starred", Goring "since 1910" and "royal warrant", Brown's "open since 1837", Horizon 22 "58th Floor". The new copy avoids them. Felix to decide whether the cards keep them until checked.
4. **Walk times** in the venue summary tiles ("6 min walk" etc.) aren't on the venues' sites. The new copy leaves them out.
5. **No copy claims Convene X has hosted at any venue.** Fit sentences are written as "we'd" / "suits". The shared closing paragraph "Convene X curates the full evening here..." is replaced on every page.
6. **The footer newsletter form doesn't submit anywhere** (found while auditing /join/). Sign-ups are lost. See `join-merge-9517.md`, section 1, item 4.
7. **Royal Automobile Club** events must be sponsored by a Club member. Not on our page today. Freya to decide whether it stays in the public portfolio.
8. **Horizon 22** is one 817 m² space for up to 280. Weak fit for 10 to 25 seat dinners; better for large formats and breakfasts.

## Carousel picks at a glance

| Venue | Keep in "Other rooms" |
|---|---|
| The Ivy Club | NoMad London, Covent Garden Hotel, The Soho Hotel, Haymarket Hotel |
| The Connaught | Claridge's, The Beaumont, Brown's Hotel, The Dorchester |
| The Lanesborough | The Goring, The Dorchester, The Connaught, The Stafford London |
| The Dorchester | The Lanesborough, The Connaught, The Beaumont, Claridge's |
| The Goring | The Lanesborough, The Stafford London, Royal Automobile Club, The Dorchester |
| The Beaumont | Claridge's, The Connaught, Brown's Hotel, The Dorchester |
| The Stafford London | Royal Automobile Club, Brown's Hotel, Haymarket Hotel, The Goring |
| Claridge's | The Connaught, The Beaumont, Brown's Hotel, The Dorchester |
| The Ned | Searcys Horizon 22, NoMad London, The Ivy Club |
| Brown's Hotel | The Stafford London, Claridge's, The Connaught, Royal Automobile Club |
| Royal Automobile Club | The Stafford London, Haymarket Hotel, Brown's Hotel, The Goring |
| The Soho Hotel | Haymarket Hotel, Covent Garden Hotel, The Ivy Club, Brown's Hotel |
| Haymarket Hotel | Royal Automobile Club, The Stafford London, The Soho Hotel, Covent Garden Hotel |
| Covent Garden Hotel | The Ivy Club, NoMad London, The Soho Hotel, Haymarket Hotel |
| Searcys Horizon 22 | The Ned, NoMad London, Covent Garden Hotel |
| NoMad London | Covent Garden Hotel, The Ivy Club, The Ned, Haymarket Hotel |

## How this was checked

- WordPress: posts 8782 and 8987, all 16 venue pages and pages 9517 and 11638 read with the Convene X Events WordPress tools (read only). REST route list for `cx/v1` read.
- Make: scenarios 8415814 and 8415795 and the team's webhook list read (read only).
- Venue facts: the venues' own websites via Firecrawl (scrape in direct-quote mode, plus site-restricted search). NoMad's official site (hilton.com) returned 403 to the scraper, so only its search excerpts were used.
- Drive: "London Private Dining Venues" sheet read; treated as unverified wherever it disagreed with the venue's site.
- Not used: any third-party venue listing (Hire Space, Cvent, etc.) as a source for copy.
