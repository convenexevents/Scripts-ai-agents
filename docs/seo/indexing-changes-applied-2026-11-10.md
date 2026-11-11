# Indexing changes applied: convenexevents.com, 10 Nov 2026

Applied by Kai (Web & UX) under Nathan's sign-off of fixes 1, 2, 3 and 7 from `indexing-fix-plan-2026-11-10.md`. Nothing outside those items was changed. All writes went through the Convene X Events WordPress MCP and are recorded in Easy MCP change history (wp-admin > Easy MCP AI > History), which also stores the before-values.

Verification was done logged-out with Firecrawl (maxAge 0). FlyingPress page cache could not be purged from the MCP (no purge route; `wp_clear_cache` only reaches Rank Math sitemap and Elementor CSS). Pages whose post was saved were re-cached automatically; archive pages were not (see Fix 3).

## Summary

| Fix | Plan item | Status |
|---|---|---|
| 1 | A1 mock-up files | Done |
| 1 | A2 BuddyPress screens and /register/ | Partly (member pages already noindex; /register/ and BP directories NOT changed: no permission) |
| 1 | A4 410 rules for dead plugin paths | Not done: no tool can create regex/410 redirections |
| 1 | A5 410 for query URLs | Not done (same reason) |
| 2 | B1 /blog/ canonical + stray og:url | Partly: canonical already correct; stray og:url not removed (source is code, not settings) |
| 2 | B2 homepage "Latest insights" + service-page links | Done |
| 2 | B3 posts 8983-8986 to 5+ links in and out | Done |
| 2 | B4 event pages linked from hub and sector pages | Already in place, no change needed |
| 3 | A3 categories noindex + out of sitemap | Done at origin; cached copies need a FlyingPress purge |
| 7 | B8 Eva widget name | Done on the website; Make scenario still uses the name (report below) |

## Change log

| # | What | Where | Before | After | Verified logged-out |
|---|---|---|---|---|---|
| A1 | Deleted Media Library attachment member-profile.html | Attachment 9021 | 200 OK, indexable, fake member bio | Deleted (file and attachment) | Yes (attachment gone; text saved first) |
| A1 | Deleted member-directory.html | Attachment 9020 | 200 OK | Deleted | Yes |
| A1 | Deleted activity-feed.html | Attachment 9022 | 200 OK | Deleted | Yes |
| A1 | Link check before deletion | Post/page content (all statuses), `_elementor_data`, Elementor library | n/a | No links or embeds found (only the files linked each other) | n/a |
| A2 | Member pages /activity/ 9544, /dashboard/ 9545, /directory/ 9539, /groups/ 9543, /profile/ 9542 | Rank Math per-page robots | Already `noindex, follow`; logged-out visitors are redirected to /login/ (also noindex) | No change | Yes |
| A2 | /register/ (buddypress post 7131) and BP directories (members 7122, spaces 7116, activity-2 7123, activate 7130) | Rank Math | `/register/` = `follow, index` | NOT changed: the MCP user gets "not allowed to edit this post" on the `buddypress` post type, and the Rank Math settings integration is switched off | /register/ still `follow, index` |
| A3 | Category robots | Term meta `rank_math_robots` (via Rank Math's own /rankmath/v1/updateMeta) on 569 sector-finance, 570 sector-cyber, 571 sector-it, 572 sector-procurement, 573 sector-marketing | No term meta (inherited index) | `["noindex","follow"]` | Origin: yes (`/category/sector-finance/?cxv=...` = `noindex, follow`). Sitemap: yes (category sitemap gone; index now lists post + page sitemaps only). Cached URL still shows `index` until FlyingPress is purged |
| A3 | The other 10 categories (Business, Design, Events, etc.) | Term meta | Already `noindex` | No change | Yes (/category/business/ = `follow, noindex`) |
| B1 | /blog/ canonical | Page 206 | Live head already has `<link rel="canonical" href="https://convenexevents.com/blog/">` | No change | Yes |
| B1 | Stray `<meta name="og:url">` | Sitewide wp_head output | Prints the permalink of the first post in the main query on every page (on /blog/ it is /executive-dinner-format/, on /register/ it is empty) | NOT changed: it is printed by PHP code, not a setting (see notes) | Still present |
| B2 | "Latest insights" section, 6 post cards + "All insights" button to /blog/ | Home 9110, inserted before the final CTA, reusing the site's `formats` / `fmt-card` components; page-scoped CSS for cards 4-6, 2 columns at 601-900px, text-only cards at 600px and below | No post links on the homepage | Links to 8983, 8987, 8984, 8985, 8986, 44 and /blog/ | Yes, desktop 1440 and mobile 360 screenshots checked |
| B2 | "Further reading" cards (text-only fmt-cards) before the FAQ | 9415 Private Executive Dinners | No guide links | 7865, 11413, 8983, 8984 | Rank Math link counts updated |
| B2 | Same | 9414 Executive Virtual Roundtables | Linked 8782 and 48 only | 8987, 48 | Yes |
| B2 | Same | 9413 Executive Webinars | No guide links | 29, 1908, 48 | Yes |
| B2 | Same, before "Before you ask" FAQ | 10806 Sponsor | No guide links | 8986, 8985 | Yes |
| B2 | Same, before FAQ | 9412 London Venues | No guide links | 8769, 1321 | Yes |
| B3 | Wrapped existing phrases in links (no copy changed) | 8983 | 3 internal out | 8 out / 7 in (Rank Math) | Yes |
| B3 | Same | 8984 | 3 out | 8 out / 9 in | Yes |
| B3 | Same | 8985 | 3 out | 8 out / 6 in | Yes |
| B3 | Same | 8986 | 2 out | 7 out / 6 in | Yes |
| B4 | Event links | 9410, 10667, 10307 | Already link every live event (9410: all 7; 10667: 10568, 10569, 10570; 10307: 10305, 10306) | No change | Yes |
| B8 | Eva widget text | Elementor Custom Code snippet 11764 "CX Eva Chat Assistant", meta `_elementor_code` | 4 public mentions of Nathan (see below) | "the team" wording | Yes (homepage HTML: "Leave your details and the team will get back to you", 0 matches for "Nathan") |

### B8 text changes (snippet 11764)
1. "Leave your details and Nathan will get back to you" > "Leave your details and the team will get back to you"
2. "Please use your work email so Nathan can reply." > "Please use your work email so the team can reply."
3. "Thanks, I've passed your details to Nathan. He'll be in touch soon." > "Thanks, I've passed your details to the team. They'll be in touch soon."
4. "Sorry, that didn't send. Please email enquiries@convenexevents.com and Nathan will get back to you." > "... and the team will get back to you."

## Rollback

- A1: not reversible from WordPress (permanent delete was the approved action). Full text is saved in `docs/seo/backups/a1-mockup-files-text-2026-11-10.md`.
- A3: Easy MCP history entries 10560-10564 (term meta created). To undo, delete `rank_math_robots` term meta on terms 569-573, or set each term's Robots back to Index in Posts > Categories > edit > Rank Math.
- B8: Easy MCP history entry 10565 holds the full before-value of `_elementor_code`; re-apply it with wp_history_apply, or reverse the 4 strings above in Elementor > Custom Code > CX Eva Chat Assistant.
- B2 (pages 9110, 9415, 9414, 9413, 10806, 9412): each added block starts with an HTML comment `<!-- ============ LATEST INSIGHTS (added 2026-11-10 ...` or `<!-- ============ FURTHER READING (added 2026-11-10 ...` and ends at `</section>`. Delete that block to roll back. A WordPress revision was saved with each edit (homepage: new revision 11838). Pre-change revisions: 9110 > 11737, 9415 > 11627, 9414 > 11625, 9413 > 11610, 10806 > 11830, 9412 > 11611. Note: for 9110, 9415, 9414, 9413 and 9412 the live content was a few characters longer than these revisions (unsaved meta-only edits), so removing the block is safer than restoring the old revision.
- B3: each change only wraps an existing phrase in `<a href>`; remove the anchor to roll back. Revisions were saved per edit (posts 8983, 8984, 8985, 8986).

## Things Nathan needs to do by hand

1. **FlyingPress > Purge pages** (or Purge everything). The 5 sector category archives are still served from cache with `index`; the origin already returns `noindex`. Then check `/category/sector-finance/` in an incognito window.
2. **A4/A5 redirections (410)**: add in Rank Math > Redirections (or enable Easy MCP AI > Tools > Rank Math integration so Kai can do it). Rules, type 410, Regex: `^etn/`, `^etn-schedule/`, `^eve-flow/`, `^shop/`, `^event/`, `^product/`. Conflict check done: no live or draft page slug starts with `etn/`, `eve-flow/`, `shop/`, `event/` or `product/` (`event-attendance-cancellation-policy` and draft `event-checkin` do not match `^event/` because of the trailing slash; `/events/` and `/executive-events/` do not match). Existing rules that overlap: Rank Math redirect IDs 2 (`product/single` > home, 301) and 3 (`product/sunglasses` > home, 301) should be disabled when `^product/` 410 goes in (they are the soft-404s the plan mentions); IDs 23 (`etn` > /executive-events/) and 24 (`etn_category` > /executive-events/) only match the bare base paths and can stay. The 404 monitor could not be read (integration off), so check it for backlinked URLs first. For A5, Rank Math redirections match the path, not the query string, as far as I can tell; I did not test this.
3. **A2 /register/ noindex**: Rank Math > Titles & Meta > BuddyPress (or edit the Register directory in BuddyPress settings) and set Robots: noindex. My API user cannot edit `buddypress` posts.
4. **A3 global setting (optional, recommended)**: Rank Math > Titles & Meta > Categories > Robots Meta: No Index, so new categories inherit it. The per-term settings already cover all 15 existing categories.
5. **Eva's Make scenario** (Make > "Convene X website chat (Eva)", scenario 8263231, eu1): the name still appears in public output from Make, not WordPress:
   - Module 3 (Claude prompt): "The founder is Nathan Pritchard." and "If someone wants Nathan to follow up, tell them to tap Leave my details". Eva can say the name in chat replies.
   - Module 8 (auto-reply email to the visitor): "Nathan will read your message and come back to you personally..." signed "Nathan Pritchard, Founder, Convene X Events".
   - Module 10 (CRM sheet "Owner" = Nathan) is internal only and fine.
   Suggested wording: "Someone from our team will read your message and come back to you, usually within one working day," signed "The Convene X Events team". Remove the founder line from the prompt, or change it to "If asked who runs Convene X, say it is run by a small team with backgrounds in senior B2B events, and do not give names."
6. **Stray og:url**: a `<meta name="og:url" content="...">` tag is printed on every page from PHP in wp_head (right after an inline `ajaxurl` script, before Elementor's generator tag). It isn't Rank Math (Rank Math uses `property=`), and it isn't an Elementor Custom Code snippet. Likely sources: the child theme's functions.php, or Royal Elementor Addons. It needs a developer/file-manager look; it can't be removed from settings over the MCP. It is low-impact (non-standard `name=` attribute), but it is wrong on /blog/ and empty on some pages.

## Also noticed (not changed, outside approval)

- `groups.html` (attachment 9019) and `community-dashboard.html` (9018) in `/uploads/2026/08/` belong to the same mock-up set and are still public. Other HTML uploads there (homepage drafts, old forms) are also public. Recommend the same clean-up.
- The /directory/ page (9539, noindex, login-walled) has a Rank Math meta description of a CSS fragment and an auto-generated OG description listing the same invented member names. Not indexable, but worth fixing.
- After deletion, GSC removal for `/wp-content/uploads/2026/08/` is still step C2 of the plan (Nathan, Search Console).

## Round 2 (10 Nov 2026, afternoon): Freya go-list, built as previews only

Nathan wants to see the pages before anything goes live, so Round 2 was built as **draft copies with preview links**. No published page or post was edited. Apply each draft with `wp_republish_post` once Nathan approves; the original's revision is saved automatically. The original HTML of every page is also kept locally (Kai's session scratchpad, `raw/{id}.html`).

Preview links expire around 13:48 UTC on 11 Nov 2026. If they lapse, run `wp_create_preview_link` on the draft ID again.

| Page (live ID) | Draft ID | Scope |
|---|---|---|
| The Connaught (10707) | 11865 | full venue go-list |
| The Lanesborough (10709) | 11884 | full venue go-list |
| The Dorchester (10710) | 11885 | full venue go-list |
| The Goring (10711) | 11886 | full venue go-list |
| The Beaumont (10712) | 11887 | full venue go-list, address Brown Hart Gardens W1K 6TF |
| The Stafford (10713) | 11888 | full venue go-list |
| Brown's Hotel (10714) | 11889 | full venue go-list |
| NoMad London (10715) | 11890 | full venue go-list, "Capacity on request" |
| Royal Automobile Club (10716) | 11891 | full venue go-list, "by arrangement" |
| The Ivy Club (10717) | 11892 | interim strip only (9 West Street, WC2H 9NE); no new copy |
| The Soho Hotel (9476) | 11893 | full venue go-list |
| Claridge's (9477) | 11894 | full venue go-list |
| The Ned (9478) | 11895 | full venue go-list; Horizon 22 swapped for Covent Garden Hotel in carousel |
| Searcys Horizon 22 (9479) | 11896 | full venue go-list; "58th Floor" removed |
| Haymarket Hotel (9480) | 11897 | full venue go-list |
| Covent Garden Hotel (9481) | 11898 | full venue go-list |
| Home (9110) | 11899 | "last ten minutes" > "last 10 minutes" |
| Virtual roundtables (9414) | 11900 | "last ten minutes" > "last 10 minutes" |
| Post 8987 (/b2b-virtual-roundtable-guide/) | 11901 | merged body + Rank Math title/description; no redirect, 8782 untouched |

**Dinner size 6 to 20 (Nathan, 10 Nov):** wherever the venue copy states our recommended dinner size, the drafts now use a figure within 6 to 20 (the venues' own published capacities are unchanged). Full list of edits is in Kai's handback.

**Only live change in Round 2 (incident):** seo_redirects record 11864 (/how-to-host-a-virtual-roundtable/ > /b2b-virtual-roundtable-guide/, 301, Rank Math redirect ID 44) was created as a draft at 13:03:20 UTC but the bridge activated it in Rank Math. It was deactivated at 13:03:57 (`seo_redirect_active` = 0) and the origin returns 200 for the old URL again. The record is kept inactive for release. FlyingPress may have cached the redirect in that 37-second window; purge /how-to-host-a-virtual-roundtable/ to be safe. At release, also retarget redirect 11629 (/how-to-host-a-virtual-roundtable-2026/) straight to /b2b-virtual-roundtable-guide/ to avoid a chain.

**Release order for the merge (after Nathan's OK):** republish 11901 into 8987 > reactivate redirect 11864 > retarget 11629 > update inbound links to /how-to-host-a-virtual-roundtable/ > set 8782 to draft > purge FlyingPress > verify logged-out.

**Not done (waits for approval):** the 301, the 8782 draft, the inbound link updates, cache purge, logged-out checks of live URLs, and indexing requests. /join/, /sponsor/ and the Drive sheet were not touched.

**Also noticed, outside the go-list:** the homepage "London Venues" carousel (9110) still shows the old claims: Michelin (Connaught, Dorchester), "since 1910" and royal warrant (Goring), "open since 1837" and "longest-standing" (Brown's), "58th Floor" (Horizon 22), Ivy Club at 1-5 West St WC2H 9NQ, and The Beaumont at 8 Balderton St. It needs the same clean-up once Freya approves.

## Round 3: release (10 Nov 2026, evening)

Released by Kai on Nathan's approval of all Round 2 previews ("Approve all previews", 10 Nov 2026, relayed by Jarvis). All writes went through the Convene X Events WordPress MCP and are in Easy MCP change history. Verification was done logged-out with Firecrawl (maxAge 0), desktop and mobile.

### Pre-release fix
| What | Where | Before | After |
|---|---|---|---|
| Call length | Draft 11901 (8987 merge), closing CTA | "book a 45-minute exploratory call" | "book a 15-minute exploratory call" |
| "45-minute" check | All other drafts (11865, 11884-11900), title, excerpt and content | None found (the only "45" hits were CSS values) | No change |

### Releases (wp_republish_post; each saved a revision of the original first and moved the copy to the trash)
| Live page | Draft | Revision (undo) | Audit ID | Released | Verified logged-out (desktop + mobile) |
|---|---|---|---|---|---|
| The Connaught 10707 | 11865 | 12250 | 5026 | Yes | Yes |
| The Lanesborough 10709 | 11884 | 12252 | 5027 | Yes | Yes |
| The Dorchester 10710 | 11885 | 12254 | 5028 | Yes | Yes |
| The Goring 10711 | 11886 | 12256 | 5029 | Yes | Yes |
| The Beaumont 10712 | 11887 | 12258 | 5030 | Yes | Yes |
| The Stafford 10713 | 11888 | 12260 | 5031 | Yes | Yes |
| Brown's Hotel 10714 | 11889 | 12262 | 5032 | Yes | Yes |
| NoMad London 10715 | 11890 | 12264 | 5033 | Yes | Yes |
| Royal Automobile Club 10716 | 11891 | 12266 | 5034 | Yes | Yes |
| The Ivy Club 10717 (interim) | 11892 | 12268 | 5035 | Yes | Yes (address only; page has no FAQ, as before) |
| The Soho Hotel 9476 | 11893 | 12270 | 5036 | Yes | Yes |
| Claridge's 9477 | 11894 | 12272 | 5037 | Yes | Yes |
| The Ned 9478 | 11895 | 12274 | 5038 | Yes | Yes |
| Searcys Horizon 22 9479 | 11896 | 12276 | 5039 | Yes | Yes |
| Haymarket Hotel 9480 | 11897 | 12278 | 5040 | Yes | Yes |
| Covent Garden Hotel 9481 | 11898 | 12280 | 5041 | Yes | Yes |
| Home 9110 | 11899 | 12282 | 5042 | Yes | Yes ("last 10 minutes" live) |
| Executive Virtual Roundtables 9414 | 11900 | 12284 | 5043 | Yes | Yes |
| Post 8987 /b2b-virtual-roundtable-guide/ | 11901 | 12286 | 5044 | Yes | Yes |

Slugs, status and authors of every original are unchanged (checked after release). Template stayed `elementor_canvas` on every page. Venue checks: every new sentence from the approved drafts is present (13 to 22 per page), FAQPage + Place schema present, robots `index, follow`. To undo any row: `wp_restore_revision` with the revision ID, then `wp_history_apply` with the audit ID.

Warning seen on the homepage release: WordPress holds an older unsaved autosave of 9110 from another user. If someone restores that autosave in the editor, or presses Publish in Elementor on an old session, it would overwrite this release. Discard it rather than restore it.

### 8987 merge
| Step | Record | Before | After | Verified |
|---|---|---|---|---|
| 1. Body + meta | 8987 | Old body | Merged body (Round 2 draft, 15-minute fix) | Yes |
| 2. Redirect on | seo_redirects 11864 (Rank Math ID 44) | draft, `seo_redirect_active` 0 | publish, active 1, 301 to `/b2b-virtual-roundtable-guide/` | Yes: `/how-to-host-a-virtual-roundtable/` lands on `/b2b-virtual-roundtable-guide/` |
| 3. No chain | seo_redirects 11629 (Rank Math ID 43) | `/how-to-host-a-virtual-roundtable-2026/` to `/how-to-host-a-virtual-roundtable/` | to `/b2b-virtual-roundtable-guide/` (301) | Yes |
| 4. Internal links | 9414 post_content | 1 link to `/how-to-host-a-virtual-roundtable/` | `/b2b-virtual-roundtable-guide/` | Yes |
| 4. Internal links | Posts 8983-8987, all other posts and pages (content and Elementor data) | No hard-coded links found | No change | Origin check: no page or post links the old URL |
| 5. Retire | Post 8782 | publish | draft (not deleted) | Yes |

Cached copies of 13 blog posts still show 8782 in their auto-generated "related posts" cards (the origin no longer does; checked with a cache-busting query). They clear with the FlyingPress purge below.

### Leftover drafts
`wp_republish_post` moved every copy to the trash itself (11865, 11884-11901 all `trash`, none left as draft). Nothing else to remove.

### Cache
`wp_clear_cache` (posts scope, 20 IDs): Rank Math sitemap cache and Elementor CSS cleared. FlyingPress is not reachable from the MCP.

### Fix 7: Nathan's name (Eva form and site-wide)
Snippet 11764 (Eva) was already fixed in B8 and still reads "the team" in all 4 places. Fresh logged-out scrapes of all 42 sitemap pages, all 21 published posts, /blog/, /register/, /build-your-room/ and /join-the-network/ found **no remaining "Nathan will get back to you" text** (earlier hits were FlyingPress copies cached before B8; they have since refreshed). Database search (page and post content, Elementor data, Elementor library, Custom Code, terms) found one remaining public occurrence, which was **not changed**:

| Where | Text | Why not changed |
|---|---|---|
| About Us 9382, "single point of ownership" section | Founder card: photo `nathan-pritchard-photo.jpg`, alt "Nathan Pritchard, founder of Convene X Events", name "Nathan Pritchard", label "Founder, Convene X Events" | It is a deliberate named founder card with a photo, not the Eva form. Swapping the name for "the team" under a portrait would read wrongly. It needs a decision (remove the card, or keep it as an agreed exception to the house rule). |

No before-state to record because nothing was edited in this step.

### /sponsor/ preview (not published)
Draft 12289 (copy of 10806), template `elementor_canvas`, built from `content-drafts-2026-11-10/sponsor-10806.md` with Nathan's decisions: 15-minute call (FAQ "How do we start?"), guest-list sign-off for dinners and roundtables only (Version B: hero, step 2, FAQ, meta, OG, Twitter), 12-week minimum and seniority bars stated (Version A: section 7, "Who is actually in the room?", "How long does it take to set up?"), reach "the UK, Europe and the US" everywhere (chip reads "UK, Europe and US reach"), dinners 6 to 20. Freya's approved final-CTA button swap is in. 35 text swaps, each matched exactly once; class names, IDs, CSS and script untouched; the Further reading block is unchanged. Rank Math description, OG description and Twitter description set as in the file; SEO title unchanged.
Preview: https://convenexevents.com/?page_id=12289&preview=true&easy_mcp_ai_preview=1.1794432106.0e48d9503498ba733ac014756278b5ad (expires 11 Nov 2026, 21:21 UTC). Release later with `wp_republish_post { copy_id: 12289 }`.

### Found during release, not changed
- **Booking links say 45 minutes.** The site-wide header ("Book a Call"), footer ("Book a Call") and the post-template CTA link to `cal.com/convenexevents/45min`; page bodies and Eva use `/15min`. Now that the call is 15 minutes, the header/footer templates should point at `/15min` (navigation change, needs Nathan's OK).
- **/events/ returns 404.** There is no page, archive or redirect at that path (it was not touched in this release). /executive-events/ returns 200. Suggest a 301 from /events/ to /executive-events/ if anything links to it.
- **8987 has no FAQPage schema** (BlogPosting only). The FAQ is visible. Callum to add FAQ schema matching the 5 questions.
- **Twitter description on /sponsor/** shows the OG text in the preview, because Rank Math's "Use data from Facebook tab" is on and the MCP can't switch it off (Rank Math integration disabled). Switch it off in Rank Math > Social on 12289/10806 before release.
- **/sponsor/ preview styling:** 14 page-scoped CSS rules target `body.page-id-10806`, so the preview (page ID 12289) misses some dividers, FAQ width and button styling. They apply once the copy is released into 10806. Review the copy, not those details.
- **Site-wide "Continue with Convene X" script** still says "in the UK and US". Theme-level, outside this release.

## Round 4: booking links and reach wording (10 Nov 2026, late evening)

Applied by Kai on Nathan's approval ("yes switch buttons to 15 min and fix UK wording", 10 Nov 2026, relayed by Jarvis). All writes went through the Convene X Events WordPress MCP and are in Easy MCP change history (audit IDs below; history holds every before-value). Out of scope and untouched: /join/ (9517), the homepage venue carousel, and the /sponsor/ draft 12289.

### Where the old values actually live
- **cal.com/convenexevents/45min**: no page, post, Custom Code snippet, widget, menu, theme mod or Elementor page data contains it. It was in one Elementor global widget (5724 "Button") and, for everything visitors see, in the **child theme files** (`convene-x-child` 2.2.7): header "Book a Call", footer "Book a Call", mobile menu "Book a Call", venue drawer "Book a call" and the partner panel "Book Exploratory Call". The Elementor header (6771) and footer (7435) templates are not the live header/footer (footer 7435 already said 15min). The MCP cannot read or write theme files (`wp_privileged_files_read_query` is off and there is no file-write tool).
- **"Continue with Convene X"**: injected on every blog post by the Custom Code snippet 10309 "CX Cookie Consent Banner" (script `cx-postcta-js`). The copies inside the `post_content` of 18 posts are not rendered (those posts are Elementor-built), so they were left alone.
- **"UK & US" top strip** on public pages: also from the child theme. The member-area pages carry their own copy in page content.

### Change log
| # | What | Where | Before | After | Audit / revision |
|---|---|---|---|---|---|
| R4-1 | Global widget link | Elementor library 5724 "Button" (Book Exploratory Call) | `https://cal.com/convenexevents/45min` | `https://cal.com/convenexevents/15min` | audit 5184, revision 12325 |
| R4-2 | "Continue with Convene X" text (all blog posts) | Custom Code 10309, `_elementor_code`, script `cx-postcta-js` | "...for senior leaders in the UK and US. Explore the formats..." | "...for senior leaders in the UK, Europe and the US. Explore the formats..." | audit 5187, history 11971 (full before-value) |
| R4-3 | Interim override for theme-rendered links and top strip (new, appended at the end of 10309) | Custom Code 10309, new `<script id="cx-booking-1110">` with an explanatory comment | none | Rewrites any `a[href*="cal.com/convenexevents/45min"]` to `/15min` (MutationObserver, so the venue drawer, mobile menu and partner panel are covered when built) and the theme top strip "UK & US · Invitation only" to "UK, Europe & US · Invitation only" | same as R4-2. Remove this block once the theme is fixed |
| R4-4 | Event-page network paragraph | Pages 10566, 10567, 10568, 10569, 10570, 10305, 10306 | "...senior decision-makers in the UK and US." | "...senior decision-makers in the UK, Europe and the US." | audits 5211-5217, one revision each |
| R4-5 | Sector-page network paragraph | Pages 10667, 10668, 10669, 10670, 10671 | same | same | audits 5206-5210 (10667 revision 12326) |
| R4-6 | Partner profile | Page 10654 | "for senior leaders in the UK and US." / "audiences in the UK and the US." | "...in the UK, Europe and the US." (both) | audits 5218, 5219 |
| R4-7 | Partners hub | Page 10653 | pill "Partners · UK and US"; "for senior leaders in the UK and US."; "Demo profile · UK and US" | "Partners · UK, Europe and US"; "...in the UK, Europe and the US."; "Demo profile · UK, Europe and US" | audits 5220-5222 |
| R4-8 | Partners hub meta description (Rank Math, also OG/Twitter) | Page 10653 `rank_math_description` | "...roundtables and webinars in the UK and US." | "...roundtables and webinars in the UK, Europe and the US." | audit 5244 (+ resave) |
| R4-9 | /sponsor/ live page (not the 12289 draft) | Page 10806, 5 strings | "reaches your ICP in the UK and US at once"; chip "UK and US reach"; "in London and across the UK and US."; "...the profile we agree with you, in the UK and US."; "...reach your audience across the UK and US in a single session." | "...in the UK, Europe and the US at once"; "UK, Europe and US reach" (matches draft 12289); "...across the UK, Europe and the US."; "...in the UK, Europe and the US."; "...across the UK, Europe and the US in a single session." | audits 5223-5227 |
| R4-10 | Member/login header strip | Pages 9859 /login/, 8388 /my-account/, 9545, 9544, 9543, 9542, 9539 | `UK &amp; US &middot; Invitation only` | `UK, Europe &amp; US &middot; Invitation only` | audits 5228-5234 |
| R4-11 | Dinners hero pill + rotator | Page 9415 | "Invitation-Only · UK &amp; US" and rotator `t:"Invitation-Only · UK & US"` | "Invitation-Only · UK, Europe &amp; US" / `t:"Invitation-Only · UK, Europe & US"` | audits 5235, 5236 |
| R4-12 | Services hero rotator | Page 9411 | `t:"Executive Formats · UK & US"` | `t:"Executive Formats · UK, Europe & US"` | audit 5237 |
| R4-13 | Homepage splash subline (not the venue carousel) | Page 9110 | "UK and US · Invitation only" | "UK, Europe and US · Invitation only" | audit 5238 |
| R4-14 | Maintenance-mode page | Elementor library 11514 "We'll be back soon" | "Invitation only &middot; UK &amp; US" | "Invitation only &middot; UK, Europe &amp; US" | audit 5240, revision 12359 |

Every text swap used an exact-match search with expected count 1, so nothing else on those pages changed. Visible "45-minute"/"45 min" call-length text next to the buttons: none found on the site (the buttons say "Book a Call" / "Book Exploratory Call"). Webinar-length mentions ("45 minutes") are format lengths, not the call, and were left.

### Cache
`wp_clear_cache` scope `site`: Rank Math sitemap and Elementor CSS cleared. FlyingPress still has no purge route over the MCP.

### Verification (Firecrawl, logged-out, maxAge 0, rendered DOM)
| URL | Booking links in the page | Reach wording |
|---|---|---|
| / | 7 links, all `/15min` (header, footer, hero, band, final CTA) | top strip "UK, Europe & US · Invitation only"; splash "UK, Europe and US · Invitation only" |
| /the-connaught-london-private-dining-venue/ | 7 rendered links, all `/15min` | top strip updated |
| /why-senior-leaders-value-conversation/ (post 44) | all rendered links `/15min`, incl. the post's "Book a Call with the Team" | "Continue with Convene X" block reads "...in the UK, Europe and the US." |
| /contact-us/ | 7 rendered links, all `/15min` | top strip updated |
| Extra: /sponsor/, /private-executive-dinners/, /partners/ | all rendered links `/15min` | all edited strings live; partners meta/OG/Twitter description updated |
The only `45min` strings left in page source are inside the theme's own JavaScript templates (venue drawer, partner panel, mobile menu on posts) and the override script itself; the override rewrites them as soon as those elements are added to the page. Crawlers that do not run JavaScript will still see `45min` in those theme templates until the theme is fixed.

### FlyingPress purge needed
The snippet change (R4-2/R4-3) affects every page, so **Purge everything** is the right action. If purging by URL: /, /sponsor/, /partners/, /partners/convene-x-events/, /private-executive-dinners/, /services/, /login/, /my-account/, /dashboard/, /activity/, /groups/, /profile/, /directory/, /executive-dinners-for-cfos/, /ciso-roundtables/, /cio-cto-dinners/, /procurement-leaders/, /marketing-leaders/, /human-edge-leadership-culture-age-of-automation-roundtable/, /ai-advantage-enterprise-efficiency-decision-making-webinar/, /cfo-leadership-dinner-capital-strategy-london-2026/, /modern-finance-function-automation-ai-controls-roundtable/, /treasury-liquidity-navigating-market-volatility-roundtable/, /us-executive-webinar-february-2027/, /us-executive-virtual-roundtable-march-2027/, and every blog post URL (for the post CTA block).

### Not changed (needs the theme, a decision, or is outside scope)
1. **Child theme files** (`convene-x-child`): header/footer/mobile-menu/venue-drawer/partner-panel links still say `cal.com/convenexevents/45min` in the theme source, and the theme top strip says "UK & US · Invitation only". The override in R4-3 fixes what visitors see; the permanent fix is a find-and-replace in the theme files (or switch on `wp_privileged_files_read_query` plus a file-edit route). Then delete the `cx-booking-1110` block from snippet 10309.
2. **Theme-level meta descriptions** (not Rank Math, not page content): /contact-us/ says "...or book a 45-minute exploratory call." and /private-executive-dinners/ says "...for senior leaders across the UK and US." Both come from the theme (Rank Math's own description for 9415 is different and correct). Suggested: "...or book a 15-minute exploratory call." and "...across the UK, Europe and the US."
3. **Old Royal Addons footer template** (wpr_templates 7450): "Book a Call" links to `tidycal.com/convenexevents/45-minute-sales-call-block`. It is not the live footer and not the cal.com link, so it was left; worth deleting or repointing.
4. **Drafts, not public**: 6873 brochure page ("Book a 45-minute exploratory call"), 10564 event draft, 8782/31/1288 post drafts (post-CTA copies in post_content), 11707/11722 ("two 45-minute" set-up calls, a different subject). Fix 6873 before it is ever published.
5. **Revisions pruned by WordPress**: this round's saves pushed some pages over the site's revision limit and WordPress deleted their oldest revisions, including several Round 1 rollback points listed above (9110: 11737 and 11838; 9415: 11626 and 11627; 10806: 11829, 11830, 11842). Round 1 rollback still works by deleting the dated blocks, and Easy MCP history holds the before-values. Round 3 revisions (12250-12286) were not in the pruned set.

## Round 5: hide the sponsorship deal form, mobile tables (10 to 11 Nov 2026)

Applied by Kai on Nathan's own instruction (10 Nov 2026, relayed by Jarvis). The job was cut off by a system restart at about 23:40 UTC on 10 Nov and resumed on 11 Nov. Easy MCP history was checked first, so nothing was applied twice. All writes went through the Convene X Events WordPress MCP and are in Easy MCP change history.

### 1. Sponsorship deal form: unlisted, not removed
The form is page **8960** "Sponsorship Deal Form & Contract" (template `elementor_canvas`; it embeds `/wp-content/uploads/2026/08/sponsorship-deal-form-v2-1.html`). It stays published at the same slug, with no password, and works by direct link (checked logged-out: the form renders, "Deal details", "Sponsor details" and the rest).

**Direct URL for Nathan: https://convenexevents.com/sponsorship-deal/**

Before-state: published; Rank Math robots `noindex, follow` (it was already noindex); not in any menu; linked from /partners/ (6 links) and /partners/convene-x-events/ (2 links), every one labelled "Become a partner", "Your organisation here" or "Partnership overview".

| # | What | Where | Before | After | Audit / revision |
|---|---|---|---|---|---|
| R5-1 | Rank Math robots | Page 8960 `rank_math_robots` | `noindex, follow` | `noindex, nofollow` | audit 5265, history 12082 (applied 10 Nov, 23:38 UTC) |
| R5-2 | Partner links repointed | Page 10653 /partners/: hero "Become a partner" button, both "Your organisation here" card titles, both card "Become a partner" buttons, the partner-drawer script's "Become a partner" link, and the final CTA "Become a partner" (6 links plus 1 script link) | `https://convenexevents.com/sponsorship-deal/` | `https://convenexevents.com/sponsor/` | audit 5270, revision 12360 (before: revision 12342) (10 Nov, 23:39 UTC) |
| R5-3 | Partner profile links repointed | Page 10654 /partners/convene-x-events/: resources list "Partnership overview" and the CTA "Become a partner" | `https://convenexevents.com/sponsorship-deal/` | `https://convenexevents.com/sponsor/` | audit 5271, revision 12361 (10 Nov, 23:39 UTC) |

The links now go to /sponsor/, the public page for partner enquiries, so every button still has somewhere to go.

Checked with nothing found to change: all 14 classic menus (no item points at 8960 or the slug; none is assigned to a theme location, as the header and footer are hard-coded in the child theme and do not link to it); /sponsor/ (10806) and the /sponsor/ preview draft 12289 (no link to the form, checked in the raw content); Custom Code 10309 and 11764; Elementor library and Royal templates; posts and pages (content search for the slug finds only 8960 itself).

Sitemap: Rank Math leaves noindex pages out of the sitemap. After the cache clear, the live `page-sitemap.xml` (125 URLs) does not contain /sponsorship-deal/.

### 2. Blog comparison tables on phones
Cause: the theme sets `.article-body table { min-width: 520px }` and only wraps Elementor or block tables in a scroll container. A plain table in a post (8987 is a classic post) is 520px wide inside a 324px column, and `html, body { overflow-x: clip }` cuts off the third column.

| # | What | Where | Before | After | Audit / revision |
|---|---|---|---|---|---|
| R5-4 | Site-wide mobile table CSS (block `cx-table-1111`) | Customizer Additional CSS, theme `convene-x-child` (custom_css post 12362) | empty | At 767px and below, every `.article-body` table scrolls sideways inside its own rounded, bordered box. The first column stays fixed while the rest scrolls, and a yellow mono "Swipe to see all columns →" hint sits at the top. Pink scrollbar, 14px text, and brand tokens (#141414 / #2a2a2a / #FF1FA9 / #FCD500). It also stops the theme styling the first body row like a header when a table already has a `<thead>` (on 8987, "Peer exchange and relationships" was showing in uppercase pink). | audit 5312, revision 12363 |

Posts with tables: 8987 /b2b-virtual-roundtable-guide/ (3 columns, `<thead>`) and 8878 /what-is-an-executive-conference/ (4 columns, header in the first row). /executive-webinars-vs-virtual-roundtables/ (48) has no HTML table on the live page (checked the rendered DOM), so there is nothing to fix there. The CSS applies to any future table in a post automatically.

To roll back, delete the `cx-table-1111` block from Additional CSS (the file was empty before).

### Cache
`wp_clear_cache` scope `site` (11 Nov, 21:51 UTC): Rank Math sitemap and Elementor CSS cleared. FlyingPress still has no purge route over the MCP.

### Verification (Firecrawl, logged-out, maxAge 0)
- /sponsorship-deal/: 200, the form renders, `<meta name="robots" content="nofollow, noindex">`.
- page-sitemap.xml: no /sponsorship-deal/.
- /, /sponsor/, /partners/, /partners/convene-x-events/: no link to /sponsorship-deal/ (the partner pages are already serving the 23:39 versions).
- Tables: the cached copy of 8987 that FlyingPress serves does not have the new CSS yet. A cache-bypassing fetch (`?cxv=1111`) does: "Swipe to see all columns" and the thead fix are in the page. That uncached HTML was rendered in Playwright at 360 and 390px (the live host is blocked from this container's browser, so the Firecrawl copy with its inlined CSS was used). The table sits inside the column (left 18, right 342 at 360 and right 372 at 390), the page has no sideways overflow, and swiping shows the full Webinar column with the first column fixed. The 4-column 8878 table was checked the same way and also works.

### FlyingPress purge needed
**Purge everything** (Additional CSS is in every page's head), or at least: /b2b-virtual-roundtable-guide/, /what-is-an-executive-conference/, /partners/, /partners/convene-x-events/, /sponsorship-deal/. Until the purge, phones still see the cut-off table on cached posts.

### Not done (no tool for it)
- **Site search still lists the form.** `/?s=sponsorship` shows /sponsorship-deal/ (the search page itself is noindex, and nothing on the site links to it). WordPress search ignores Rank Math robots, and the MCP cannot add PHP. Permanent fix: one filter in the child theme's functions.php, e.g. `add_action('pre_get_posts', function($q){ if(!is_admin() && $q->is_main_query() && $q->is_search()){ $q->set('post__not_in', array_merge((array)$q->get('post__not_in'), [8960])); } });`. Second best, if Nathan approves: a small script in Custom Code 10309 that removes `/sponsorship-deal/` results on search pages (visual only). Pages are not in any archive (category, tag, date or author), so no archive lists it.
