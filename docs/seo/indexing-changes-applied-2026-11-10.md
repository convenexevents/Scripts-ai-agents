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
