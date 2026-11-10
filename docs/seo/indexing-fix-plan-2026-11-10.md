# Indexing fix plan: convenexevents.com

Date: 10 November 2026 · Prepared by: SEO & Technical Auditor (internal) · Status: **DRAFT, read-only diagnosis. Nothing has been changed on the live site.** Every fix below needs Nathan's sign-off before Kai (or Callum) applies it.

---

## 1. The short version

The "254 of 280 URLs unknown to Google" figure looks much worse than the real position.

- **Nothing is blocking Google.** robots.txt is clean, the sitemap is clean, every key page checked returns `index, follow` with a self-referencing canonical, and http/www redirect to `https://convenexevents.com/`.
- **Most of the "unknown" URLs should not exist.** Rank Math's inspection table tracks 282 objects, but the live sitemap only lists **70 URLs**. The other ~210 are mostly dead URLs left behind by removed plugins (Eventin `/etn/`, `/etn-schedule/`, `/eve-flow/`, WooCommerce `/shop/` and `/product/`, `/event/`) and BuddyPress screens (`/groups/`, `/register/` etc.). Sampled ones return 404 or redirect. Google is right to ignore them.
- **The real problem is a smaller one:** about a third of the pages that matter are not confirmed indexed. Google has *found* them but is choosing not to crawl or index them yet. The likely causes are weak internal links to the blog, near-duplicate venue pages, overlapping blog posts, and crawl budget spent on leftover junk URLs.

---

## 2. What I checked and what I found

| Check | Result | Evidence |
|---|---|---|
| robots.txt | OK | Only blocks `/wp-admin/`, declares `sitemap_index.xml`. No AI or Googlebot blocks. |
| Sitemap contents | OK, lean | `sitemap_index.xml` has 3 child sitemaps: pages (42 URLs), posts (22 posts + /blog/), categories (5 sector categories). No attachments, tags, authors, templates or test pages. 70 URLs in total. |
| Noindex on key pages | OK | Home, /sponsor/, /services/, /executive-webinars/, /blog/, venue pages and guides all `index, follow`. |
| Canonicals | Mostly OK | Self-referencing everywhere checked. **Exception: /blog/ has no canonical tag at all**, and outputs a second `og:url` pointing to `/executive-dinner-format/`. |
| http / www | OK | `http://www.` redirects to `https://convenexevents.com/`. |
| The 404 | Harmless | `/shop/the-ai-advantage/` (old WooCommerce product). Google found it via an old `product-sitemap.xml` that no longer exists on the site. |
| "Unknown to Google" URLs | Mostly junk | Sample: `/etn/applied-ai-machine-learning-summit-2026/` = 404 + noindex; `/etn-schedule/day-1..3/`, `/eve-flow/send-certificate/`, `/shop/...`, `/event/...`, `/groups/`. None are in the sitemap. |
| Leftover junk Google *has* found | Problem | `/wp-content/uploads/2026/08/member-profile.html`, `member-directory.html`, `activity-feed.html` (static mock-ups, 200 OK, indexable, contain a made-up member bio); `/register/` (BuddyPress sign-up, indexable); `/?etn_action=download_ics&event_id=...`; `/?tec-tc-cart=redirect`; `/?post_type=tribe_events...`; category and comment feeds; `/achievements-1/viewer/`. |
| Internal links to blog posts | Weak | The homepage and main nav link to /blog/ only, never to a post. /blog/ itself is "Discovered, not indexed". Newer posts have only 2-3 internal links (e.g. /conference-sponsorship-enterprise-b2b/ 2, /b2b-virtual-roundtable-guide/ 2, /executive-dinner-format/ 3, /senior-executives-say-no-to-events/ 3). |
| Internal links to venue pages | Good | Homepage links to all 16 venue pages. |
| Venue page uniqueness | Weak | Each venue page has ~250 words of unique copy built on the same sentence template ("...well suited to executive dinners in London, private leadership gatherings and intimate senior-level conversation... the polish of a genuinely premium London address"), then a 15-venue carousel identical on every page. Google sees mostly duplicate content. The Ivy Club is "Discovered, not indexed". |
| Overlapping blog posts | Problem | Virtual roundtable: `/how-to-host-a-virtual-roundtable/` (Crawled, not indexed) and `/b2b-virtual-roundtable-guide/` cover the same topic; `/executive-webinars-vs-virtual-roundtables/` overlaps both. Executive dinner: six posts on near-identical intent (what-is, format, what-makes-different, best-practices, how-to-host, why-dinners-lead). |
| Category archives | Problem | The 5 sector category archives are in the sitemap but list largely the same posts (most posts sit in 5-10 categories). They compete with the real sector pages (e.g. `/category/sector-finance/` vs `/executive-dinners-for-cfos/`). |
| /join/ vs /join-the-network/ | Decision needed | Two join pages. `/join/` is in the sitemap and nav. `/join-the-network/` (waitlist) is `noindex, nofollow`. |
| Public personal name | House-rule flag | The "Eva" chat widget on venue pages says "Leave your details and **Nathan** will get back to you". Not an indexing issue, but it breaks the no-personal-names rule on public pages. |

---

## 3. Priority pages that MUST be indexed (53)

Status key: **Indexed (GSC)** = confirmed by Google's URL Inspection via Rank Math, inspected 5-10 Nov. **Not indexed (GSC)** = confirmed not indexed. **Seen in search** = appears in a `site:` web search (good sign, but not Google Search Console proof). **No evidence** = not confirmed either way.

**Totals: 11 confirmed indexed · 4 confirmed not indexed · 27 seen in search (likely indexed, unverified) · 11 no evidence.**

### Core and service pages (13)
| Page | ID | Status |
|---|---|---|
| / | 9110 | Indexed (GSC) |
| /executive-events/ | 9410 | Indexed (GSC) |
| /private-executive-dinners/ | 9415 | Seen in search |
| /executive-virtual-roundtables/ | 9414 | Seen in search |
| /sponsor/ | 10806 | Seen in search |
| /london-venues/ | 9412 | Seen in search |
| /about-us/ | 9382 | Seen in search |
| /contact-us/ | 9449 | Seen in search |
| /us-executive-events/ | 10307 | Seen in search |
| /partners/ | 10653 | Seen in search |
| /services/ | 9411 | No evidence |
| /executive-webinars/ | 9413 | No evidence |
| /join/ | 9517 | No evidence |

### Sector pages (5)
| Page | ID | Status |
|---|---|---|
| /executive-dinners-for-cfos/ | 10667 | Seen in search |
| /ciso-roundtables/ | 10668 | Seen in search |
| /procurement-leaders/ | 10670 | Seen in search |
| /marketing-leaders/ | 10671 | Seen in search |
| /cio-cto-dinners/ | 10669 | No evidence |

### Venue pages (16)
| Page | ID | Status |
|---|---|---|
| /the-connaught-london-private-dining-venue/ | 10707 | Indexed (GSC) |
| /the-lanesborough-london-private-dining-venue/ | 10709 | Indexed (GSC) |
| /the-dorchester-london-private-dining-venue/ | 10710 | Indexed (GSC) |
| /the-goring-london-private-dining-venue/ | 10711 | Indexed (GSC) |
| /the-beaumont-london-private-dining-venue/ | 10712 | Indexed (GSC) |
| /the-stafford-london-private-dining-venue/ | 10713 | Indexed (GSC) |
| /the-ivy-club-london-private-dining-venue/ | 10717 | **Not indexed (GSC): Discovered, not crawled** |
| /soho-hotel-london/ | 9476 | Seen in search |
| /searcys-horizon-22/ | 9479 | Seen in search |
| /haymarket-hotel-london/ | 9480 | Seen in search |
| /covent-garden-hotel-london/ | 9481 | Seen in search |
| /claridges-london-executive-dinner-venue/ | 9477 | No evidence |
| /the-ned-london-executive-dinner-venue/ | 9478 | No evidence |
| /brown-s-hotel-london-private-dining-venue/ | 10714 | No evidence |
| /nomad-london-private-dining-venue/ | 10715 | No evidence |
| /royal-automobile-club-london-private-dining-venue/ | 10716 | No evidence |

### Event pages (7)
| Page | ID | Status |
|---|---|---|
| /ai-advantage-enterprise-efficiency-decision-making-webinar/ | 10567 | Seen in search |
| /treasury-liquidity-navigating-market-volatility-roundtable/ | 10570 | Seen in search |
| /cfo-leadership-dinner-capital-strategy-london-2026/ | 10568 | Seen in search |
| /us-executive-webinar-february-2027/ | 10305 | Seen in search |
| /us-executive-virtual-roundtable-march-2027/ | 10306 | Seen in search |
| /human-edge-leadership-culture-age-of-automation-roundtable/ | 10566 | No evidence |
| /modern-finance-function-automation-ai-controls-roundtable/ | 10569 | No evidence (Google has crawled it: it is listed as a referring page) |

### Blog hub and key posts (12)
| Page | ID | Status |
|---|---|---|
| /why-invitation-only-events/ | 6264 | Indexed (GSC) |
| /private-dining-rooms-in-mayfair/ | 8769 | Indexed (GSC) |
| /what-is-an-executive-conference/ | 8878 | Indexed (GSC) |
| /blog/ | 206 | **Not indexed (GSC): Discovered, not crawled** |
| /how-to-host-a-virtual-roundtable/ | 8782 | **Not indexed (GSC): Crawled, not indexed** |
| /why-senior-leaders-value-conversation/ | 44 | **Not indexed (GSC): Discovered, not crawled** (7 Nov) |
| /what-is-an-executive-dinner/ | 7865 | Seen in search |
| /how-to-host-executive-dinners/ | 11413 | Seen in search |
| /executive-roundtable-vs-executive-dinner/ | 8984 | Seen in search |
| /executive-dinner-format/ | 8983 | Seen in search |
| /b2b-virtual-roundtable-guide/ | 8987 | Seen in search |
| /conference-sponsorship-enterprise-b2b/ | 8986 | Seen in search |

---

## 4. Draft fixes, in order

Do them in this order: clean up junk first (frees crawl budget), then strengthen the pages, then ask Google to recrawl. **All need Nathan's sign-off. Verify every change in a logged-out/incognito window (FlyingPress caching).**

### (a) Rank Math / WordPress settings

| # | What | Where | Why | Risk |
|---|---|---|---|---|
| A1 | Delete the three static mock-up files: `member-profile.html`, `member-directory.html`, `activity-feed.html` | `/wp-content/uploads/2026/08/` (Media Library or file manager, Kai) | They are indexable, show up in search, and contain a made-up member profile. Brand and data-protection risk (flag to Legal & Compliance). | Low. Check nothing links to them first. |
| A2 | Set BuddyPress screens to noindex | Rank Math > Titles & Meta > BuddyPress Directories (and the `/register/` screen) | `/register/` ("Create an Account") is indexed. Members-area screens have no search value. | Low. Members still reach them by link. |
| A3 | Set category archives to noindex and remove them from the sitemap | Rank Math > Titles & Meta > Categories (Robots: No Index); Rank Math > Sitemap Settings > Categories (exclude) | 5 thin archives listing the same posts compete with the 5 real sector pages. | Low. `/category/sector-finance/` is in search today and will drop out, which is the aim. |
| A4 | Return 410 (Content deleted) for dead plugin URL patterns | Rank Math > Redirections, regex rules, type 410: `^etn/`, `^etn-schedule/`, `^eve-flow/`, `^shop/`, `^event/`, `^product/` | Tells Google these are gone for good, so it stops spending crawl budget on ~200 dead URLs. `/product/sunglasses/` currently redirects to the homepage, which Google treats as a soft 404. | Low-medium. Check Rank Math's 404 monitor first; if any old URL has backlinks, 301 it to its closest live page instead. No live URL is changed, so no 301 is owed. |
| A5 | Handle leftover plugin query URLs | Rank Math > Redirections, "contains" rules for `etn_action=`, `tec-tc-cart=`, `post_type=tribe_events` -> 410 | They serve the homepage with a 200, creating duplicates. | Low. Optional; canonical already points to the home page. |
| A6 | (Optional, later) Clear stale Rank Math analytics objects | Rank Math > Status & Tools > Database Tools | So the inspection stats reflect the 70 real URLs, not 282. | Medium: loses historical analytics in Rank Math. Do it only after A4 and only if the dashboard noise matters. |

### (b) Per-page changes

| # | What | Where | Why | Risk |
|---|---|---|---|---|
| B1 | Add a self-referencing canonical to /blog/ and remove the stray `og:url` that points to /executive-dinner-format/ | Page 206, Elementor posts-page template (Kai) | /blog/ is the only route to the posts and is "Discovered, not indexed". Conflicting signals don't help. | Low. |
| B2 | Add a "Latest insights" block on the homepage linking 4-6 posts, and contextual links from service pages to their guides | Home 9110; Private Executive Dinners 9415 -> 7865, 11413, 8984, 8983; Executive Virtual Roundtables 9414 -> 8987; Executive Webinars 9413 -> 48, 29, 1908; Sponsor 10806 -> 8986, 8985; London Venues 9412 -> 8769, 1321 | Posts get no links from strong pages today. Internal links are the main signal Google uses to decide what is worth crawling. | Low. Use the existing link styles. |
| B3 | Bring the newest posts up to 5+ internal links in and out | Posts 8983, 8984, 8985, 8986, 8987 | They currently have only 2-3. | Low. |
| B4 | Link every event page from /executive-events/ and its matching sector page | Page 9410, plus 10667 (CFO events 10568, 10569, 10570), US events from 10307 | Two event pages have no evidence of indexing. Event pages expire, so get them crawled while they are live. | Low. |
| B5 | Resolve the virtual-roundtable overlap: one page owns "how to host/run a virtual roundtable" | 8782 and 8987 | 8782 is "Crawled, not indexed". Google is picking one and dropping the other. **Default proposal:** merge 8782's unique sections (FAQ, common mistakes, comparison table) into 8987 and **301 /how-to-host-a-virtual-roundtable/ -> /b2b-virtual-roundtable-guide/**. Confirm the owner with GSC page+query data first (see C5). Hand the rewrite to the Content Writer. | Medium. The URL change must ship with the 301 in Rank Math > Redirections, plus updated internal links. |
| B6 | Make venue pages genuinely different | All 16 venue pages, starting with The Ivy Club 10717 | Add 150-300 words of venue-specific detail (rooms, layout, best format/sector fit, a short FAQ); cut the "Other rooms" carousel to 3-4 nearby venues; vary the templated opening sentence. Content Writer drafts, Kai builds. | Low-medium (editing time). No URL changes. |
| B7 | Decide which join page is the "request an invitation" page | 9517 /join/ and 11638 /join-the-network/ | Two pages with the same purpose. Either (i) keep /join/ indexed and leave the waitlist noindexed but switch **nofollow -> follow**, or (ii) make /join-the-network/ the indexed page and **301 /join/ -> /join-the-network/**, then update the nav. Minimum fix: change nofollow to follow on 11638. | Low for (i); medium for (ii). Nathan decides. |
| B8 | Remove the personal name from the chat widget ("Nathan will get back to you" -> "the team will get back to you") | Eva chat widget (site-wide snippet / floating element) | House rule: no personal names on public pages. | Low. |
| B9 | (Phase 2) Cannibalisation check on the six executive-dinner posts | 7865, 8983, 51, 1857, 11413, 33 | Same intent, split signals. Don't merge anything until GSC page+query data shows which page owns which query. | n/a until data is in. |
| B10 | Fix table header cells marked up as H2 headings ("Feature", "Virtual Roundtable", "Webinar") | 8782 (if it survives B5) | Breaks the heading outline. | Low. |

### (c) Steps Nathan must do in Google Search Console

I can't do these myself because there is no Search Console connector.

1. **Sitemaps report:** remove any old sitemap still listed (for example `product-sitemap.xml` or any Eventin/event sitemaps). Then resubmit `https://convenexevents.com/sitemap_index.xml` and check it reads "Success" with about 70 discovered URLs. (Do this after A3.)
2. **Removals tool (temporary removal):** after A1 and A2 are live, request removal of the prefix `https://convenexevents.com/wp-content/uploads/2026/08/` and of `https://convenexevents.com/register/`.
3. **URL Inspection > Request indexing** for these priority URLs. The quota is roughly 10 a day, so spread them out, and only request a page once its on-page fix (B1-B6) is live:
   - **Day 1 (core):** /services/, /executive-webinars/, /private-executive-dinners/, /executive-virtual-roundtables/, /sponsor/, /join/ (or the page chosen in B7), /cio-cto-dinners/, /blog/, /contact-us/, /london-venues/
   - **Day 2 (venues and events):** /the-ivy-club-london-private-dining-venue/, /claridges-london-executive-dinner-venue/, /the-ned-london-executive-dinner-venue/, /brown-s-hotel-london-private-dining-venue/, /nomad-london-private-dining-venue/, /royal-automobile-club-london-private-dining-venue/, /human-edge-leadership-culture-age-of-automation-roundtable/, /modern-finance-function-automation-ai-controls-roundtable/, /treasury-liquidity-navigating-market-volatility-roundtable/, /cfo-leadership-dinner-capital-strategy-london-2026/
   - **Day 3 (posts):** /b2b-virtual-roundtable-guide/ (after B5), /why-senior-leaders-value-conversation/, /what-is-an-executive-dinner/, /how-to-host-executive-dinners/, /executive-roundtable-vs-executive-dinner/, /executive-dinner-format/, /conference-sponsorship-enterprise-b2b/, /senior-executives-say-no-to-events/, /us-executive-virtual-roundtable-march-2027/, /us-executive-webinar-february-2027/
4. **Pages report:** export the "Crawled - currently not indexed", "Discovered - currently not indexed" and "Excluded by noindex" lists, and share them so I can confirm the 2 noindexed URLs and the 1 redirect, and re-score this plan.
5. **Performance report:** export page + query data for the last 3 months, filtered to "virtual roundtable" and "executive dinner". It's needed to settle B5 and B9.

**Expectation:** after the fixes and requests, allow 2-6 weeks before judging. "Discovered, not indexed" on a young, low-authority site often clears slowly. Recheck on the 1 December monthly audit.

---

## 5. What I could not check, and why

- **Search Console directly:** there's no connector, so I couldn't see the full Pages report, request indexing, or see sitemaps submitted in the past.
- **Per-URL inspection for every page:** the Rank Math `inspectionResults` route ignores paging and filter arguments and always returns the latest 25 rows. The per-post analytics route returns nothing for pages with no GSC traffic. So GSC-confirmed status exists for only about 15 URLs. The rest is based on a `site:` web search (via Firecrawl), which suggests but does not prove Google indexing.
- **Which 2 URLs are "excluded by noindex" and which is the "1 redirect":** they weren't in the 25 rows returned. Likely candidates are /join-the-network/ (noindex) and /uk-events-about-us/ or /product/sunglasses/ (both redirect).
- **Rank Math settings screens** (Titles & Meta robots defaults per post type and taxonomy): these can't be read over REST. I inferred them from the live robots tags.
- **Direct fetches:** the session proxy blocks curl to the site, so all live checks went through Firecrawl.
- **Backlinks to the dead URLs:** DataForSEO is out of credit (HTTP 402), so check Rank Math's 404 monitor before A4.
- **Not checked in this pass:** Core Web Vitals, JavaScript-disabled rendering of /blog/ and the venue carousels, robots status of /build-your-room/.
