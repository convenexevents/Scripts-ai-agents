# Visual review: LinkedIn visuals, 16 to 22 Nov 2026

**Reviewed by:** Felix Grant, Brand & Quality Reviewer. **Date:** 10 Nov 2026.
**Built by:** Rhys (`source/gen.py`). **Checked against:** the 4 FINAL (Felix) specs in `../posts.md`, `brand-brief.md`, and the live-site brand system (palette, type, logo, WCAG AA table).
**Method:** I rendered both PDFs to 1080 x 1350 PNGs (`pdftoppm -r 96`) and looked at all 15 slides and both cards at full size. I sampled the colours from the pixels, extracted the PDF text and diffed it against the spec, and listed the embedded fonts with `pdffonts`.

**Status: HOLD on 1 item (logo master file).** Everything else passes. I fixed 3 small build issues in `source/gen.py`, re-exported all 5 files and re-checked them. Nothing has been uploaded, scheduled or published.

## Verdict per visual

| Visual | Verdict | Notes |
|---|---|---|
| Mon carousel, 7 slides (PDF) | PASS on all checks once the logo is confirmed | Copy, palette and type match the spec. White hairline at the page foot fixed. Orphan words fixed (slides 3 and 7). |
| Wed stat card (PNG) | PASS on all checks once the logo is confirmed | Source line and save prompt now 30px. |
| Thu carousel, 8 slides (PDF) | PASS on all checks once the logo is confirmed | Source line (slide 2) and save prompt (slide 8) now 30px. White hairline fixed. |
| Sat checklist card (PNG) | PASS on all checks once the logo is confirmed | No changes needed. |
| contact-sheet.png | Rebuilt | Rebuilt from the new exports, so it matches what ships. |

## Checks

**1. Copy matches FINAL word for word: PASS.**
- Every label, headline, body line, source line, save prompt and tagline matches the spec tables in `posts.md`.
- The only differences are typographic: curly apostrophes, and UK single quotes around ‘very effective’. Those are correct.
- After my rebuild, the word sequence in both PDFs is identical to Rhys's export. I only changed where lines break.

**2. Palette and contrast: PASS.** Values are sampled from the pixels.
- Background #0A0A0A. Text #F5F5F5, not pure white.
- Pills are #FF1FA9 (or #FCD500 on Saturday) with #0A0A0A text, about 5.7:1 and 13.8:1. There's no white-on-pink text anywhere.
- Thursday's timeline labels are #A3A3A3 (7.9:1), as the spec requires.
- Wednesday: 46% is #A3A3A3 and 15% is #FCD500, with an #F5F5F5 arrow. Pink and yellow never sit at full saturation in the same block.
- Thursday's 38% is #FF1FA9, per the spec. Thin rules and the streak are #FF1FA9.
- The only pure #FFFFFF is the logo wordmark. That's the logo asset itself and must not be recoloured.
- The #3A3A3A timeline track and future-stage dots are decorative, and the current stage is carried by the pink pill. That's acceptable.

**3. Fonts: PASS. Rhys was right.**
- Embedded fonts are Fraunces (Regular and Italic), Libre Franklin and IBM Plex Mono (Medium and SemiBold).
- **Fraunces / Libre Franklin / IBM Plex Mono is the correct rule.** It's the live-site type system (`--display`, `--body`, `--mono` in cx-base-css). It's also in the brand guidelines (resolved 24 Sep 2026), my review checklist ("Not Poppins or Inter"), the campaign plan, and both FINAL specs in `posts.md`.
- Poppins is retired. No current file in this repo specifies it. Any brief that still says "Poppins" is out of date and should be corrected at source. (Note: "LibreFranklin-Thin" in `pdffonts` is just the variable font's default name. The text renders at the CSS weight, 400.)

**4. Logo: HOLD (confirm the master file).**
- **Usage passes.** It's the two-line lockup (CONVENE + pink X / EVENTS), kept together. It isn't stretched (height 112px, width auto) or recoloured, and sits bottom right on #0A0A0A on every piece, as specified.
- **I can't confirm the version.** `source/logo.png` is a 413 x 201 thumbnail with no recorded source. There's no master logo in this repo, and I couldn't read the live header logo from this session (it isn't a listed image on the home page).
- At the current size it's downscaled, not upscaled, so it looks sharp. The issue is provenance, not quality.
- **Required:** Rhys swaps `source/logo.png` for the master lockup from the brand kit (Canva brand kit or the vault brand assets: SVG, or PNG at 1000px wide or more), notes the file name here, and re-runs `python3 source/export.py`. If the master matches the thumbnail, this becomes PASS with no other changes.

**5. Legibility on a phone: PASS after fixes.**
- I assumed a 390px-wide feed, which scales each 1080px slide to about 0.36.
- Headlines (92 to 104px) come out at about 33px and body text (46px) at about 17px. Both are comfortable.
- The source lines (24px Thursday, 26px Wednesday) and save prompts (26px) came out at about 9px. That's too small for a source line we rely on for compliance. **Fixed:** all 4 are now 30px (about 11px on a phone).
- The Thursday timeline labels stay at 24px. They're wayfinding, and the headline carries the meaning.

**6. Source lines on the stat slides: PASS.**
- Thursday slide 2: "Source: Forrester, The Next Era of B2B Events, 25 Jun 2026", in Plex Mono #A3A3A3 at the foot.
- Wednesday card: "Source: Bizzabo 2026 State of Events Benchmark (vendor survey)", in Plex Mono #A3A3A3.
- Both match the spec and Nadia's safe-to-use table. No other numbers appear.

**7. Last slides carry the tagline and URL: PASS.**
- Mon slide 7: "Who's in the room is the event." as the headline, with convenexevents.com in Plex Mono at the foot.
- Thu slide 8: the tagline in Fraunces italic, "SAVE THIS FOR YOUR NEXT POST-EVENT REPORT", and convenexevents.com.
- Neither has a UTM URL.

**8. No people, photos or third-party logos: PASS.** Everything is type and brand graphics. No venue is named. The only mark is ours.

## Fixes I made (all in `source/`, re-run and verified)

1. **White hairline at the foot of every PDF slide.** Chrome rounds the PDF page up to 1013.04 pt (1350.72px), but only 1350px is painted, so each page ended in a white sliver. New `source/export.py` trims the page box to exactly 810 x 1012.5 pt. Verified: 15/15 pages are 1080 x 1350 and #0A0A0A to the edge.
2. **Source lines and save prompts raised to 30px.** I added `.src` and `.save` classes in `gen.py`, used on Thu slides 2 and 8 and on the Wednesday card. The Thursday source wraps to 2 lines (max width 600px) so it stays clear of the logo.
3. **Orphan words.** Added `text-wrap: pretty` to `h1` and `.body`. "enough.", "write." and "ends." no longer sit alone on a line. The words are unchanged.
4. **One-command rebuild.** `python3 source/export.py` runs `gen.py`, prints and trims the PDFs, screenshots the cards, and rebuilds `contact-sheet.png`. Rhys's originals are unchanged apart from these fixes. The file names are the same.

## Optional refinements (not required for PASS)

- The logo sits 84px from the bottom edge, a little under the X-height clear space (about 105px). The footer could move up to `bottom:112px` if the master logo confirms the X height. It also gives more room above LinkedIn's document page counter on mobile.
- Thursday's timeline hides future stages as dots, which follows the slide 7 "reveal" note. The spec line "the others sit in #A3A3A3" read on its own would show all labels. I'm happy with the reveal reading.

## For Freya

- The visual chain called for a Canva brand check first. These were built in code, not in Canva, so that tool doesn't apply. This review covers the same points: palette, type, logo and copy.
- Once Rhys confirms the master logo file, all 4 visuals are ready for your sign-off, then Nathan's per post.

## Pattern to raise

The brief's "Poppins" conflicts with the type system everywhere else. Whoever owns that brief template should correct it at source, so the next builder doesn't have to choose.

## Logo swap (Rhys, 10 Nov 2026), for Felix's final look

**Source.** Nathan's logo: the "Convene X Events" script lockup, with white brush-script "Convene" and "Events" around the pink brush X. Original raster: `source/logo-master-from-nathan-2026-11-10.png` (1439 x 954), untouched (md5 `0831ed7f…` before and after). The slides use the vector trace of it, `docs/brand/logo/convene-x-events-logo.svg`, copied byte for byte to `source/logo-footer.svg` and embedded as SVG.
- The trace has a transparent background, a #FFFFFF wordmark and a #FC1595 X (sampled from Nathan's original), with no glow or reflection.
- It's tightly cropped to the words and the X.
- I didn't redraw, recolour or distort anything. The rendered X samples as #FC1595 on the slides.
- Note: the X is #FC1595 and the site/pill pink is #FF1FA9. They sit a few px apart on the Wed and Sat cards (strip rule vs the X) and read as the same pink. I kept the logo as traced, per `docs/brand/logo/README.md`.
- `source/logo.png` (the old "CONVENE X / EVENTS" thumbnail) is no longer used by the build. I've left it in place.

**Glow and reflection: dropped.** Before the vector arrived, I matted the raster myself, in two versions: a clean one, and one with the glow kept at 30%. At footer size the glow read as a brown smudge under the X, so clean was the better choice. The vector trace has no glow, so the question is settled. Neither raster cut-out is in the repo.

**Build changes (`source/gen.py`, `source/export.py`)**
- `export.py` now passes `source/logo-footer.svg`. `gen.py` embeds it as `image/svg+xml`, or as PNG if a .png is passed.
- Logo height went from 112px to 164px (331px wide), still bottom right. The script words measure 33px tall on the slide, about 12px on a 390px phone feed, which is above the 30px / 11px floor we set for source lines. The new lockup is wide and short, so it needs more height than the old stacked one to be readable.
- Your clear-space fix is applied: `.footer` and `.strip` now sit at `bottom:112px` (was 84px). `.hero` bottom moved from 260 to 300px to keep the hero clear of the taller footer.
- Wed card: the save prompt moved up from bottom:300 to bottom:360. At 300 it would have crossed the strip's pink rule.
- Sat card: the pill moved from top 200 to 180 and the content from 360 to 330, so the list clears the strip rule by 46px (it was 16px).
- `text-wrap: balance` is now on `.tag` and `.src`. With the wider logo, the strip tagline would have left "event." alone on a line, and the Thu source line would have left "2026" alone. They now break as "Who's in the room / is the event." and as 3 even source lines. No words changed: the PDF word sequence is identical to the previous commit.

**Checks after `python3 source/export.py`**
- 17/17 pages are 1080 x 1350 and #0A0A0A to the edge (no white hairline).
- Looked at all 15 slides and both cards at full size, plus `contact-sheet.png` and a 390px phone-width preview.
- Measured the element boxes in Chrome, from each element to the logo box. Nothing is closer than 84px. Closest: Thu slide 2 source line 203px, Sat list 85px, Wed save prompt 84px, URLs 211px. The strip rule clears the Wed save prompt by 45px and the Sat list by 46px.
- Fonts unchanged (Fraunces, Libre Franklin, IBM Plex Mono embedded).
- PDFs are larger (Mon 144 KB to 431 KB, Thu 185 KB to 506 KB) because the vector logo is embedded on each page. That's well within LinkedIn's document limit.

**Logo status:** the master is now confirmed (Nathan's file), so the HOLD in check 4 can close if you're happy with the look. One caveat from the brand README: this is an auto-trace of a 1439px raster, so the finest brush texture is simplified. If the designer's original vector turns up, swap it into `source/logo-footer.svg` and re-run the export. No other changes are needed.

Nothing has been uploaded, scheduled or published.

## Felix final check (logo swap), 10 Nov 2026

**Method.** I re-rendered both PDFs at 96 dpi (`pdftoppm -r 96`, 15 slides at 1080 x 1350) and looked at the contact sheet, Thu slide 2, Mon slide 7, the Wed card and the Sat card at full size. I also made a 2x zoom of the Wed strip and logo, and a 390px phone-width preview of Wed, Sat, Thu 2 and Mon 7. Logo box, distances and colours are measured from the pixels, not the CSS. I checked against my brand rule: "lockup kept together, clear space = height of the X, never stretched, recoloured off-palette or placed on a busy or light background."

**Measured on every piece:** the logo's painted area is 323 x 157px, from x 657 to 980 and y 1078 to 1234. The X is 156px tall, so the X is the full height of this mark. That makes the clear space the rule asks for 156px. Edges: 99px to the right, 115px to the bottom. `source/logo-footer.svg` is byte-identical to `docs/brand/logo/convene-x-events-logo.svg` (md5 `62bb6a2d…`).

| Check | Mon carousel | Thu carousel | Wed card | Sat card |
|---|---|---|---|---|
| Lockup intact | PASS | PASS | PASS | PASS |
| Clear space (156px) to other elements | PASS. Nearest is the URL on slide 7, 219px away. Every other slide is 316px or more. | PASS. Nearest is the source line on slide 2, 210px away. URL on slide 8 is 219px. | **FAIL.** The pink strip rule sits 41px above the tip of the X. The save prompt is about 93px above the logo. | **FAIL.** The pink strip rule sits 41px above the tip of the X. List item 5 is about 85px above the logo. |
| Nothing colliding | PASS | PASS | **FAIL.** The X's top-right brush stroke points straight at the rule. At phone width the gap is about 15px, so the X reads as hanging off the line. | **FAIL.** Same as Wed. |
| Readable at phone width (390px) | PASS. "Convene" and "Events" come out at about 12px and are legible. The X is clear. | PASS | PASS | PASS |
| #FC1595 X next to the #FF1FA9 rule | n/a (no rule near the logo) | n/a. The slide 2 "38%" is #FF1FA9, more than 500px away. Side by side they read as one pink. | Colour PASS: sampled X (252,21,149) and rule (255,31,169) read as the same pink at 1x and 2x. The problem is the spacing, not the colour. Two near-identical pinks 41px apart make a small shift look like a mistake. | As Wed |

**Notes**
- **Lockup.** The script words and the X sit exactly as in Nathan's master. The mark isn't stretched (323:157 matches the SVG), recoloured or separated, and it's on flat #0A0A0A. My rule still says "two-line lockup". That describes the old CONVENE X / EVENTS mark, and Nathan's master is a single-line script lockup. I'll update the rule wording to "lockup kept together as supplied". The intent is unchanged.
- **Rhys's measurement missed the rule.** His "nothing closer than 84px" measured text boxes against the logo box. The strip's `border-top` rule wasn't in that measurement, and it is the closest element on both cards.
- **Canvas edges.** The logo sits 99px from the right edge and 115px from the bottom, against a 156px X. That lines up with the 96px layout margin used by all the type. I treated edge distance as a refinement in my first review, not a fail, and I'm keeping that reading. It still needs a decision, because the X-height rule was written for a mark whose X was a small part of it. See "For Nathan" below.
- **Trace quality.** This is an auto-trace and some fine brush texture is simplified. At 2x zoom the edges are clean and there are no stray specks, so it's fine for these uses.

**Result.**
- The HOLD on logo provenance closes.
- Mon carousel and Thu carousel: **PASS.**
- Wed stat card and Sat checklist card: **HOLD on clear space.** The pink strip rule sits 41px above the X, against 156px required. The save prompt (Wed, about 93px) and list item 5 (Sat, about 85px) are also inside the clear space.
- Fix for Rhys, `source/gen.py`. These are layout changes only, with no copy changes:
  1. End the strip rule at least 156px left of the logo, so the rule sits over the tagline only (about x 96 to 500). Or move the rule up so it is 156px or more above the logo top.
  2. Raise the Wed save prompt and the Sat list so that their lowest line is 156px or more above the logo top (y 922 or less). On Sat, tighten the list's `margin-bottom` from 34px to about 20px so it still fits.
  3. Re-run `python3 source/export.py`, re-measure from the pixels with the rule included, and refresh the contact sheet.

## Freya sign-off, 10 Nov 2026

**Reviewed:** Felix's review and final logo check above. I also looked at the contact sheet, Thu slide 2, Mon slide 7 and both cards at full size, plus the 390px phone preview. I agree with Felix's measurements. The rule-to-X gap on Wed and Sat is visible without measuring once you know to look: it's the first thing your eye catches in the bottom third of both cards.

| Checklist | Mon carousel | Wed stat card | Thu carousel | Sat checklist card |
|---|---|---|---|---|
| Felix brand review completed | Yes | Yes, failed on logo clear space | Yes | Yes, failed on logo clear space |
| Brand voice and proof framing (no company track-record claims, no event counts, no names) | Pass | Pass | Pass | Pass |
| Claims sourced | No numbers | Bizzabo, labelled as a vendor survey | Forrester, dated | No numbers |
| Anti-AI writing / no hype or fake urgency | Pass | Pass | Pass | Pass |
| No names of anyone at Convene X | Pass | Pass | Pass | Pass |
| Nothing implying Convene X has delivered events | Pass | Pass | Pass ("Leads, meetings or ROI" slide is framed as things to look at, not promises) | Pass |
| CTA right for stage | Save prompt and URL. The booking link goes in the first comment, per the brief. | Save prompt | Save prompt and URL | Save prompt |
| Logo | Pass | **Fail: clear space** | Pass | **Fail: clear space** |
| Timing | Mon 16 Nov | Wed 18 Nov | Thu 19 Nov | Sat 21 Nov |

**Verdicts**
- **Mon carousel (7 slides): APPROVED for Nathan's review.**
- **Thu carousel (8 slides): APPROVED for Nathan's review.**
- **Wed stat card: HOLD.** It goes back to Rhys for the strip and logo spacing fix above. It comes back to Felix for a pixel re-check (including the rule), and to me after that. No copy changes, so it's a quick turnaround that fits the 18 Nov slot.
- **Sat checklist card: HOLD.** Same fix and the same route as the Wed card.

**For Nathan**
1. **Clear space for your new logo.** The rule "clear space = height of the X" was written for the old stacked mark. On your script lockup the X is the whole height of the logo (156px at footer size), so applied literally it also asks for 156px to the canvas edges. Today the edges are 99px and 115px, aligned to the 96px type margin. My recommendation: X height between the logo and any other element, and the 96px layout margin to the canvas edges. Mon and Thu pass on that basis. If you want the literal reading instead, every piece needs the logo moved in or made smaller.
2. **Two pinks.** The logo's X is #FC1595 (sampled from your file) and the brand/site pink is #FF1FA9. They're indistinguishable at normal viewing. We've kept your logo as supplied. Let us know if you'd like the logo X standardised to #FF1FA9, or the reverse, so the brand file states one pink.
3. **Logo source.** The SVG is an auto-trace of your 1439px PNG. If the designer's original vector exists, send it over and Rhys will swap it in with one command.

Nothing has been uploaded, posted, scheduled or published.
