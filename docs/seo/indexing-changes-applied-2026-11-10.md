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
