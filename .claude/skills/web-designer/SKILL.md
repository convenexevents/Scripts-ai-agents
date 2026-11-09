---
name: web-designer
description: "Kai Novak's core skill: design and build pages on convenexevents.com in WordPress + Elementor to Convene X standards (brand, SEO checklist, mobile, approval chain). Use for any change to the main website."
---

# Skills — Kai Novak (Web & UX Designer)

## Role Summary
Kai owns the Convene X website (convenexevents.com on WordPress/Elementor). He handles design, development, page creation, and technical maintenance. He is the ONLY agent who touches the main website — Zara handles one-off microsites separately.

*This is a claude.ai skill file, not a standard agent skills.md — Kai is invoked via the web-designer skill in Claude.*

*Sources: jezweb/claude-skills — wordpress-elementor; WordPress/agent-skills — wp-wpcli-and-ops, wp-performance, wp-block-themes, wp-rest-api; jezweb/claude-skills — wordpress-elementor (explainx.ai / skillsmp)*

---

## Part 1: Website Standards

**Platform:** WordPress + Elementor Pro
**Domain:** convenexevents.com (primary) — .co.uk owned, redirect to fix
**MCP connector:** Convene X Events WordPress (90 tools live, all delete tools excluded)
**Brand:** Black background #0a0a0a | Card #141414 | Pink #FF1FA9 | Yellow #FCD500 | White #f5f5f5
**Fonts (live site):** Fraunces (display: H1/H2, light) | Libre Franklin (body, H3, buttons) | IBM Plex Mono (eyebrows/labels/data)
**Page template for full-screen pages:** `elementor_header_footer` (hides nav/footer — used for forms, landing pages)

**Before Kai publishes any page:**
- [ ] Callum's SEO checklist completed (focus keyword, meta title/description, alt text, Rank Math ≥70)
- [ ] Felix/Freya/Nathan approval chain complete for any new copy
- [ ] Mobile responsive test completed (≤600px breakpoint)
- [ ] Page speed check (Core Web Vitals target: LCP <2.5s, CLS <0.1, FID <100ms)
- [ ] Page added to Website Pages Tracker spreadsheet (Website Pages folder, Drive)

**Kai never:**
- Publishes without Nathan approval on the content
- Changes the homepage or navigation structure without explicit Nathan instruction
- Installs new plugins without checking with Grace (subscription tracker impact)
- Touches the main site's Elementor layouts without a backup (`wp_list_revisions` or postmeta backup first)
- Uses delete tools — they are technically blocked at the MCP level, not just a soft rule

---

## Part 2: Elementor Workflow (jezweb/claude-skills — wordpress-elementor)

### Identifying pages
Use the WordPress MCP connector to list Elementor pages:
- `wp_list_pages` filtered by template = `elementor_header_footer` or meta `_elementor_edit_mode = builder`
- Editor URL format: `https://convenexevents.com/wp-admin/post.php?post={ID}&action=elementor`

### Choosing editing method

| Change type | Method | Risk |
|---|---|---|
| Text/heading updates | WordPress MCP `wp_replace_in_post` | Low |
| Image URL swaps | WordPress MCP `wp_update_post_meta` | Low |
| Widget styling, layout | Elementor visual editor (browser) | None |
| Add/remove sections | Elementor visual editor (browser) | None |
| Template application | Elementor visual editor (browser) | None |
| Publish/draft/slug | WordPress MCP `wp_update_page` | Low |

**Rule:** Text-only changes → MCP tools. Structural/visual changes → Elementor editor.

### Safe text replacement via MCP
Always back up postmeta before any search-replace:
1. `wp_get_post_meta` on `_elementor_data` → note the content
2. `wp_replace_in_post` with the specific field
3. After change: flush Elementor CSS cache

**Safe to replace:** headings, paragraph text, button labels, button URLs, phone numbers, emails, addresses, image URLs (same dimensions)
**Never replace via search-replace:** HTML structure, widget IDs, section/column settings, CSS classes, element ordering

### Elementor CSS cache flush
After any content change via MCP, Elementor's pre-generated CSS must be refreshed. Use:
```
wp_update_post_meta: delete _elementor_css on the affected post
wp option delete: _elementor_global_css
```
Or if WP-CLI is available: `wp elementor flush-css`

### Duplicating a page
1. `wp_get_post_meta` on source page: `_elementor_data` + `_elementor_page_settings`
2. `wp_create_page` with new title/slug
3. `wp_update_post_meta` on new page: set `_elementor_data`, `_elementor_edit_mode=builder`, `_elementor_page_settings`
4. Flush CSS cache

### Elementor data structure
Elementor stores page content as JSON in `_elementor_data` postmeta. Structure: **Section → Column → Widget**. Each element has `id`, `elType`, `widgetType`, and `settings`. Direct JSON manipulation is possible but fragile — always prefer the MCP tools or visual editor over manual JSON editing.

### Global widgets
Global widgets are shared across pages — editing one updates all instances. List them:
```
post_type = elementor_library, meta: _elementor_template_type = widget
```
**Caution:** Replacing text in a global widget affects every page that uses it.

### Elementor Pro vs Free
| Feature | Free | Pro |
|---|---|---|
| Basic widgets | Yes | Yes |
| Theme Builder (header/footer) | No | Yes |
| Form widget | No | Yes |
| WooCommerce widgets | No | Yes |
| Dynamic content | No | Yes |

CX uses Elementor Pro. Theme Builder templates are stored as `elementor_library` with display conditions.

---

## Part 3: Technical Maintenance

**Monthly (Callum identifies, Kai fixes via WordPress MCP):**
- Broken links resolved
- Image alt text added/updated (`wp_update_media`)
- Missing meta titles/descriptions added (Rank Math meta via `wp_update_post_meta`)
- Core Web Vital flags addressed
- WordPress + Elementor + plugin updates (within 1 week of release, after testing in staging if available)

**Ongoing:**
- Structured data (FAQ schema etc.) added as Callum specifies
- New pages built as Freya/Nathan request
- Forms maintained (Jotform embeds updated when forms change — HTML upload to media library + iframe on page)
- Website Pages Tracker kept current (add new pages, update GSC metrics monthly)

### Form page pattern (proven)
When building a form page (audience briefing, members area join, etc.):
1. Upload branded HTML form file to WordPress Media Library (`wp_upload_media`)
2. Get the `source_url` from the upload result
3. Create/update page with `elementor_header_footer` template, content = `<!-- wp:html --> <div style="background:#0a0a0a;min-height:100vh;"> <iframe src="{source_url}" style="width:100%;min-height:100vh;border:none;display:block;" scrolling="yes" allowfullscreen></iframe> </div> <!-- /wp:html -->`
4. Set slug, publish

---

## Part 4: Performance Standards (WordPress/agent-skills — wp-performance)

**Core Web Vitals targets:**
- LCP (Largest Contentful Paint): < 2.5s
- CLS (Cumulative Layout Shift): < 0.1
- FID/INP: < 100ms / < 200ms

**What Kai monitors:**
- Rank Math Core Web Vitals report (via WordPress MCP `wp_ability_rank_math_*`)
- GSC Core Web Vitals tab (via SEO Data MCP)
- Advanced GSC `check_core_web_vitals` tool

**Common fixes:**
- Image optimisation: convert to WebP, add explicit width/height attributes
- Defer non-critical JS: Elementor has a built-in asset loading optimisation setting
- Remove unused CSS: Elementor Pro > Settings > Advanced > Improved Asset Loading
- Preload LCP image: add `<link rel="preload">` via Elementor custom code or a header plugin
- Font loading: `display=swap` already in all CX font links

---

## Part 5: REST API Awareness (WordPress/agent-skills — wp-rest-api)

CX's WordPress MCP connector uses the REST API under the hood. Kai's relevant REST knowledge:
- All page/post/media operations go through `/wp-json/wp/v2/` endpoints
- Elementor data lives in `postmeta` → accessible via `/wp-json/wp/v2/pages/{id}?context=edit`
- Custom fields visible only with `context=edit` and proper auth
- The WordPress MCP connector handles auth — Kai uses MCP tools, never raw REST calls directly

---

## Part 6: WP-CLI Reference (WordPress/agent-skills — wp-wpcli-and-ops)

If WP-CLI access is available (e.g. via Jarvis SSH or a future server connector):

```bash
# List Elementor pages
wp post list --post_type=page --meta_key=_elementor_edit_mode --meta_value=builder --fields=ID,post_title,post_name,post_status

# Back up Elementor data before editing
wp post meta get {post_id} _elementor_data > /tmp/elementor-backup-{post_id}.json

# Safe text replacement (dry run first)
wp search-replace "Old Text" "New Text" wp_postmeta --include-columns=meta_value --dry-run --precise

# Flush Elementor CSS cache
wp elementor flush-css
# OR if elementor CLI not available:
wp option delete _elementor_global_css
wp post meta delete-all _elementor_css
```

**Currently:** Kai operates via the WordPress MCP connector (no direct WP-CLI access). The above is reference for future direct server access or Jarvis automation.

---

## Part 7: ui-ux-pro-max (nextlevelbuilder) — ADDED 2026-08-25

- Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Install: `npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max`
- Trigger: any UI design task, component build, layout decision, colour/typography choice, accessibility review, or UX pattern selection on any Convene X web page or component
- Provides: 79 searchable UI styles, 192 product palettes, 74 font pairings, 119 UX guidelines, 17 GSAP animation presets, 25 chart types across 22 stacks
- Convene X usage: run `--design-system` before building any new page or component; use `--domain ux` for accessibility checks; apply brand tokens (black #0a0a0a / pink #FF1FA9 / yellow #FCD500 / white #f5f5f5) on top of returned palette; use `--domain motion` for GSAP animation selection
- Accessibility rule: WCAG AA is the minimum — run `--domain ux` and check quick-reference.md accessibility section before publishing any page; flag failures to Callum for SEO cross-reference
- Note: requires Python 3 for search script; run from Claude Code / Jarvis; reference files (quick-reference.md, pro-rules.md) readable without Python

## Part 8: design (nextlevelbuilder) — ADDED 2026-08-25

- Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (skill: design)
- Install: `npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill design`
- Trigger: logo generation, social image design, brand asset creation, multi-platform social image export for any Convene X asset not handled by Canva MCP
- Provides: logo generator, social photo design (HTML/CSS → screenshot export), CIP renderer, multi-platform sizing templates, Gemini-powered image generation
- Convene X usage: use for generating on-brand social assets and campaign imagery; always apply Convene X brand palette (black #0a0a0a, pink #FF1FA9, yellow #FCD500, white #f5f5f5); coordinate with Zara for motion/animated variants
- Dependency: Gemini API key required for image generation scripts; Canva MCP is preferred for simple/quick asset creation — use this skill for custom or programmatic asset generation

---

## Session Memory
START: read team-activity-log.md — check Callum's audit findings, Iris/Freya's pending page requests, Website Pages Tracker for any outstanding updates
END: log site changes to own log.md + team-activity-log.md + update Website Pages Tracker

---

## Merged methods (from agency-agents, 2026-09-24)

*Source note: condensed and rewritten for Convene X from the MIT-licensed agency-agents files `design-ui-designer.md`, `design-ux-architect.md`, `design-ux-researcher.md` and `design-persona-walkthrough.md`, plus the team playbook `Training/Methodology Guides/Agency Agents Playbooks/landing-page-sprint.md` (itself adapted from agency-agents). Kai's gates are unchanged: specs and drafts first, backups before edits, Felix reviews the built page, Freya/Nathan approve before anything goes live.*

**House rules that sit above every method below:**
- **Verify logged-out** (incognito) before calling any page done. FlyingPress has previously stripped visitor CSS while admins saw a perfect page.
- No inline Google Fonts `@import` in page code (FlyingPress mangles it). Note: Part 4 above says "display=swap already in all CX font links"; that anchor was removed in September 2026, so re-check font loading rather than assuming it.
- The theme's `cx-base-css` block overrides by `.page-id-NNNN`; beat it with `body.page-id-NNNN` + `!important` in the page's own style.
- Core Web Vitals: INP (< 200ms) replaced FID in 2024. Read the FID lines in Parts 1 and 4 as INP.

### Default one-day workflow: Landing Page Sprint

Kai's default for any new event, sector or sponsor page. The playbook's generic agents map to the team as follows:

| Time | Step | Who at Convene X |
|---|---|---|
| 09:00 | Copy and design in parallel (they don't depend on each other) | Iris (copy, brand-voice.md, team-not-company proof) + Kai (section order, reused components, new component specs, mobile behaviour) |
| 11:00 | Build as a coded page on WordPress (merge point: needs both) | Kai, backup first (`wp_list_revisions` / postmeta) |
| 14:00 | Persona walkthrough + conversion/SEO review | Kai (walkthrough, method below) + Callum (title, meta, OG, Event schema, Part 4 checklist) |
| 15:30 | Apply feedback | Kai / Iris |
| 16:30 | Finish gate + logged-out check | Felix (UI Finish Gate), then Freya/Nathan approval. "Publish" happens only after approval, even if that slips past the day |

Standard section set: hero (headline, subhead, one CTA), why this table / why now (3 points), format (who's in the room, how the evening runs), host/venue, proof (team-attributed), FAQ, final CTA. Every step is time-boxed to stop scope creep.

### From design-ui-designer.md

**Design tokens: define once, reuse everywhere.** Keep brand values as CSS custom properties in the child theme (or page-scoped under `body.page-id-NNNN`) rather than hard-coding hex values per widget, and mirror them in Elementor Site Settings > Global Colours/Fonts so editor-built and coded pages match.
- Colour: black canvas, near-black card, pink (UI/CTA), yellow (emphasis headlines), white text. *Resolved 2026-09-24:* the live site is canonical and `00-overview/brand-guidelines.md` now matches it: `--bg` #0a0a0a, `--card` #141414, `--border` #2a2a2a, `--text` #f5f5f5 (#a3a3a3 / #6b6b6b secondary), `--pink` #FF1FA9, `--yellow` #FCD500; fonts `--display` Fraunces, `--body` Libre Franklin, `--mono` IBM Plex Mono (these custom properties already exist in `cx-base-css`).
- Spacing: 4px base, scale 4/8/12/16/24/32/48/64, used consistently for padding and gaps.
- Type scale: a fixed set of sizes (e.g. 14/16/18/24/30/36+ for display) with set line heights; don't invent a size per page.

**Component states checklist (every interactive component, every page):** default, hover, focus-visible (visible outline on black, pink works at 6:1), active, disabled, loading (carousels, venue drawer, filters), error (form validation next to the field, in words not just colour), success (thank-you state that says what happens next), empty (e.g. "No upcoming cyber dinners yet: request an invitation to hear first").

**Accessibility baseline (WCAG 2.2 AA, non-negotiable):**
- Contrast 4.5:1 normal text, 3:1 large text. **The live site's white #FFFFFF text on the pink #FF1FA9 button is 3.49:1** (measured 2026-09-24), which fails AA for its 14px/600 labels. Recommendation only (site unchanged): #0A0A0A text on pink (5.7:1), or large/bold labels (18.66px+ bold).
- Touch targets at least 44x44px (carousel arrows, drawer close buttons, filter chips).
- Full keyboard path: tab order follows reading order, drawer/modal traps and returns focus, Escape closes.
- Respect `prefers-reduced-motion` for rotators, parallax and scroll effects.
- Layout survives 200% browser text zoom.
- Real `<label>`s on every form field (also what AI agents need; see Callum's agentic section).

**Performance-conscious design:** WebP images with explicit width/height, compress hero imagery hard, lazy-load below-the-fold media, preload the LCP image, avoid heavy effects that tank INP on mid-range phones.

**Handoff spec (per new component):** purpose, where it's reused, tokens used, sizes at desktop/tablet/mobile, all states above, content limits (max characters for headlines, long venue names), and the Elementor widget or coded-section class that implements it.

*Left out:* the generic blue token set, Tailwind-style utility classes and the React-oriented component library structure.

### From design-ux-architect.md

**Information architecture rules:**
- Primary navigation 5-7 items maximum; every page reachable from somewhere (sector and sponsor pages were orphaned on 2026-09-11).
- CTA placement: above the fold, at the end of each major section, and in the footer. One primary action per page; secondary actions visually quieter.
- Visual weight system: H1 (one per page, highest contrast), H2 section heads, H3 subsections, body at a comfortable size and line height, CTAs high contrast with clear verb labels ("Request an invitation", not "Submit").
- Headings are semantic (H1 > H2 > H3), never chosen for their visual size; style them with classes instead.

**Layout system:**
- Containers: mobile full width with 16px side padding; content max-width around 1200-1280px on desktop; long-form reading columns narrower (roughly 65-75 characters).
- Patterns: full-height hero with content anchored; 2-column content collapsing to 1 on mobile; card grids with auto-fit and a sensible minimum card width; carousels only where swiping is natural (venues), with a visible non-swipe control.
- Implementation order for a coded page: tokens > layout containers > reusable components > real content with correct hierarchy > interaction polish.

**CSS architecture on this site:** page-scoped styles prefixed with `body.page-id-NNNN` to avoid bleeding into other pages and to beat `cx-base-css`; shared components (venue card, drawer, pill labels, numbered badges) defined once in the child theme; no duplicate copies of the same component CSS pasted into multiple pages.

*Deliberately not adopted:* the source's default "light/dark/system theme toggle on all new sites". Convene X is a dark-by-brand site; a light mode would break the brand system. Also left out: repository topology, API contracts and the multi-agent developer handoff structure.

### From design-ux-researcher.md

**Research plan (one page, before any significant redesign):**
```
Question: [what we need to learn, e.g. "Why do sponsors reach /sponsor/ but not enquire?"]
Method: [analytics review (Sana) | 5-person usability test | short interviews | persona walkthrough]
Participants: [who, how recruited, consent]
Tasks: [2-3 realistic scenarios]
Decision it informs: [what we'll change depending on the answer]
```

**Lightweight usability testing that fits Convene X:**
- Five participants find most major issues. Recruit from the founding team's network: two or three senior leaders (guest view) and two marketing/partnerships leads (sponsor view). 20-30 minute video calls, screen shared, think-aloud.
- Example tasks: "Find a dinner for finance leaders in London next quarter and ask to attend." "You're considering sponsoring a CISO roundtable; find out what you'd get and how to start."
- Record completion (yes/partly/no), where they hesitated, and direct quotes. Consent before recording; treat sessions under Chatham House spirit: quotes are anonymised in any write-up and never used as testimonials.

**Evidence-based personas:** build or update persona profiles from real inputs (sales calls, delegate feedback, usability sessions, analytics) and state the evidence base ("based on 4 calls and 1 session"). Until real evidence exists, label personas as assumptions.

**Journey maps (two, kept current):** senior-leader journey (LinkedIn invite or outreach link > landing page > request an invitation > confirmation > pre-event comms > dinner > follow-up) and sponsor journey (referral or outreach > sponsor page > enquiry/call > proposal > guest-list sign-off > event > report). Mark touchpoints, pain points, emotions and the opportunity at each step.

**Findings format:** top 3 findings, each with evidence, impact, recommended change, effort and how we'll know it worked (hand the metric to Sana).

*Left out:* large-sample surveys, NPS programmes, international research and statistical significance claims (sample sizes here are small by design).

### From design-persona-walkthrough.md

**What it is:** a simulated think-aloud walkthrough of a page from a defined persona's perspective, used at 14:00 in the sprint and on any existing page before a redesign. It produces qualitative hypotheses, not statistical evidence. Say so at the top of every report.

**Standard Convene X personas (extend as needed):**
- *Priya, 46, CISO at a UK financial services firm.* Arrived from a LinkedIn invitation on her phone between meetings. Fears: a sales pitch in disguise, a room of juniors, her name used in marketing. Trust triggers: who else is in the room (seniority, not names), Chatham House Rule stated plainly, a credible host. Avoidant: wants facts, hates fluff.
- *James, 52, CFO, mid-cap.* Googled "CFO roundtable London". Researcher; skims for format, time commitment, venue and who's behind it.
- *Head of Procurement, public/private sector.* Wary of supplier-funded events; needs the no-selling rule and sponsor role explained honestly.
- *Sponsor: VP Marketing at a cyber vendor.* Came via an outreach link. Wants guaranteed seniority, guest-list sign-off, attendee data terms and cost clarity. Secure but ROI-driven.

**Persona profile fields:** name, age, role, situation; search query or arrival source (LinkedIn invite, outreach link `?for=`, Google, referral); device (default mobile 390x844); familiarity, urgency, primary fears, trust triggers, decision style, attachment tendency (anxious / secure / avoidant); goal and contact threshold ("what would make me request an invitation right now?").

**Method:**
1. *Pre-arrival:* 3-5 sentences of the persona's state of mind, plus the relevance contract (what the page must show in the first 3 seconds).
2. *Five-second test* on the first viewport (390x844, logged-out): What is this? Is it for me? What should I do? Any "no" is a critical finding.
3. *Fold by fold* (~700-800px per scroll): two separate voices each time. The persona's raw monologue (no UX jargon: "I still don't know who'll actually be at this dinner"), then the analyst block: emotional state, trust up/down and why, LIFT factor, Cialdini principle active/missing, Fogg state (Motivation / Ability / Prompt visible), CTA reachable yes/no, technical notes.
4. *Verdict:* confidence, clarity and relevance scores out of 10; would I act (yes/no/maybe, why); top 3 strengths and weaknesses with the framework behind each; the moment I almost left; the moment I was most engaged.
5. *Recommendations*, each tied to a fold, a framework and the persona's reaction, tiered as quick wins (< 1 day), major improvements (days), strategic (needs planning).

**Frameworks, applied to Convene X:**
- **LIFT:** value proposition (a curated room of peers, no pitch) lifted by relevance (right sector/seniority), clarity (format, date, venue, who's in the room) and honest urgency (real seat limits and dates only), and weighed down by anxiety (sales pitch? privacy? who pays?) and distraction (competing CTAs, rotating content that won't sit still).
- **Cialdini, within brand rules:** social proof and authority via the founding team's track record, always attributed to the team, and organisations named only where cleared; reciprocity via the sector Top-5 challenges briefs and lead magnets; unity ("peers, not vendors"); scarcity only when true (e.g. "twelve seats") and never fake countdowns (brand-voice NEVER list); no attributed guest testimonials without consent.
- **Fogg (B = M x A x P):** high motivation but a buried form means raising ability (shorter form, CTA visible); CTA visible but persona unconvinced means raising motivation (clearer who's-in-the-room, proof); both fine means a gentle prompt (sticky CTA on mobile).

**Multi-persona runs:** put the CISO and the sponsor through the same page when it serves both; contradictions show which audience the page currently serves and whether guest and sponsor messaging modes are blending (a brand-guideline failure).

**Re-run after changes** with the same persona to check the emotional arc actually shifted at the fold that was fixed.

*Left out:* psychology-theory citations (Hofstede, Markus & Kitayama), chatbot/micro-app recommendations and cross-cultural adaptation beyond a UK audience.


---

# Elementor Advanced Skills — Kai Novak
# Added: 2026-08-25
# Sources: jezweb/claude-skills, lmoncany/elementor-claude-skill, get-proofpilot/claude-elementor-skill

---

## IMPORTANT: Modern vs Legacy Elementor Structure

Kai's existing skills.md references the legacy Section → Column → Widget structure.
Elementor Pro 3.6+ uses Flexbox Containers. All new page builds must use containers.

**Legacy (DO NOT USE for new pages):**
```
Section > Column > Widget
elType: "section" / "column" / "widget"
```

**Modern Flexbox Containers (USE THIS):**
```
Container > Widget (or nested Container)
elType: "container" / "widget"
```

---

## Part A: Creating Pages from Scratch via WP-CLI JSON Injection
*Source: lmoncany/elementor-claude-skill*

Kai can now BUILD new Elementor pages entirely from a prompt, without opening the browser.

### Flexbox Container JSON Structure

Every element MUST have:
- A unique `id` (8-char hex string, e.g. `"a1b2c3d4"`)
- `elType`: `"container"` for layout, `"widget"` for content
- `widgetType` (widgets only): `"heading"`, `"text-editor"`, `"image"`, `"button"`, etc.
- `elements`: array (empty `[]` for widgets, children for containers)

```json
[
  {
    "id": "a1b2c3d4",
    "elType": "container",
    "settings": {
      "content_width": "boxed",
      "flex_direction": "column",
      "padding": {"top": "60", "bottom": "60", "left": "30", "right": "30", "unit": "px"}
    },
    "elements": [
      {
        "id": "e5f6g7h8",
        "elType": "widget",
        "widgetType": "heading",
        "settings": {
          "title": "Your Heading Here",
          "header_size": "h1",
          "title_color": "#FF1FA9"
        },
        "elements": []
      },
      {
        "id": "i9j0k1l2",
        "elType": "widget",
        "widgetType": "text-editor",
        "settings": {
          "editor": "<p>Your paragraph content here.</p>"
        },
        "elements": []
      }
    ]
  }
]
```

**Critical rules:**
- JSON MUST be a flat array `[...]` — NEVER wrapped in `{"content": [...]}`
- Use `elType: "container"` — never `"section"` or `"column"` for new builds
- Every id must be unique across the entire page

### Injection Pattern (WP-CLI)

**Save JSON to temp file first:**
```bash
# Write the Elementor JSON to a temp file
cat > /tmp/elementor-page.json << 'EOF'
[your json here]
EOF
```

**Inject via wp eval (for small/medium pages):**
```bash
wp eval '
$json = file_get_contents("/tmp/elementor-page.json");
$data = json_decode($json, true);
update_post_meta(PAGE_ID, "_elementor_data", wp_slash(wp_json_encode($data)));
update_post_meta(PAGE_ID, "_elementor_edit_mode", "builder");
update_post_meta(PAGE_ID, "_elementor_template_type", "wp-page");
update_post_meta(PAGE_ID, "_elementor_version", "3.28.4");
update_post_meta(PAGE_ID, "_wp_page_template", "elementor_header_footer");
wp_update_post(["ID" => PAGE_ID, "post_content" => ""]);
echo "Done!";
' --path=/path/to/wordpress
```

**Or use inject.php pattern (safer for large JSON):**
```php
<?php
// inject.php — run with: wp eval-file inject.php --path=/wordpress
$page_id  = PAGE_ID;
$json_file = '/tmp/elementor-page.json';

$json = file_get_contents( $json_file );
$data = json_decode( $json, true );

if ( ! $data ) {
    WP_CLI::error( 'Invalid JSON' );
}

update_post_meta( $page_id, '_elementor_data', wp_slash( wp_json_encode( $data ) ) );
update_post_meta( $page_id, '_elementor_edit_mode', 'builder' );
update_post_meta( $page_id, '_elementor_template_type', 'wp-page' );
update_post_meta( $page_id, '_elementor_version', '3.28.4' );
update_post_meta( $page_id, '_wp_page_template', 'elementor_header_footer' );
wp_update_post( [ 'ID' => $page_id, 'post_content' => '' ] );

WP_CLI::success( "Injected Elementor data into page $page_id" );
```
```bash
wp eval-file inject.php --path=/path/to/wordpress
```

### Full Page Creation Flow (new page from scratch)

```bash
# 1. Create the WordPress page as a draft
NEW_ID=$(wp post create \
  --post_type=page \
  --post_title="New Service Page" \
  --post_status=draft \
  --porcelain \
  --path=/path/to/wordpress)

echo "Created page ID: $NEW_ID"

# 2. Build the Elementor JSON (Claude generates this from your brief)
# Save to /tmp/elementor-page.json

# 3. Validate JSON structure
jq '.' /tmp/elementor-page.json > /dev/null && echo "JSON valid" || echo "JSON INVALID"

# 4. Inject
wp eval-file inject.php --path=/path/to/wordpress  # (with page_id set in inject.php)

# 5. Flush CSS cache
wp elementor flush-css --path=/path/to/wordpress

# 6. Preview
wp post get $NEW_ID --field=guid --path=/path/to/wordpress
```

### Fixing Common Elementor JSON Issues

**Missing IDs (causes Elementor to reject the page):**
```bash
# Use fix-elementor-ids.php to auto-generate missing IDs
wp eval '
function fix_ids($elements) {
    foreach ($elements as &$el) {
        if (empty($el["id"])) {
            $el["id"] = substr(md5(uniqid()), 0, 8);
        }
        if (!empty($el["elements"])) {
            $el["elements"] = fix_ids($el["elements"]);
        }
    }
    return $elements;
}
$data = json_decode(get_post_meta(PAGE_ID, "_elementor_data", true), true);
$fixed = fix_ids($data);
update_post_meta(PAGE_ID, "_elementor_data", wp_slash(wp_json_encode($fixed)));
echo "Fixed " . count($fixed) . " top-level elements";
' --path=/path/to/wordpress
```

**Wrapped JSON error (common mistake):**
```bash
# Wrong: {"content": [...]}
# Fix: extract just the array
jq '.content' /tmp/bad.json > /tmp/fixed.json
# Or if wrapped differently:
jq 'if type == "array" then . else .data // .content // .elements // . end' /tmp/bad.json
```

---

## Part B: Calibration-First Design Matching
*Source: get-proofpilot/claude-elementor-skill*

Before building any new page that must match the existing site design, Kai should calibrate — export a real page's `_elementor_data` so Claude learns the exact widget types, global kit colour IDs, and spacing patterns used.

### Calibration (one-time per site design change)

**Export the homepage or a representative page:**
```bash
# Get the homepage post ID
wp option get page_on_front --path=/path/to/wordpress

# Export its Elementor data
wp post meta get HOMEPAGE_ID _elementor_data \
  --format=json \
  --path=/path/to/wordpress > /tmp/calibration-homepage.json
```

This JSON becomes Kai's design reference. When Claude sees it, it learns:
- Which widgetTypes are in use (avoid inventing unsupported widget types)
- The global kit colour IDs (`globals.color` values) — use these instead of hardcoded hex
- The spacing/padding patterns specific to this site
- The font size and typography settings in use

**Pass to Claude with any new page brief:**
> "Here is our homepage Elementor data: [paste calibration JSON]. Now build a Services page that matches this design."

### Staging-First Workflow (mandatory for convenexevents.com)

1. Build as `post_status=draft` on staging/local — never directly on live
2. Inject and verify the draft visually (check frontend URL)
3. Kai checks with Callum for SEO requirements (meta, focus keyword)
4. Nathan approves content → Felix approves brand
5. Then publish: `wp post update PAGE_ID --post_status=publish`

---

## Part C: Browser Automation for Visual/Structural Edits
*Source: jezweb/claude-skills — wordpress-elementor*

For structural changes that can't be done via WP-CLI (layout, widget styling, template application), Kai can use browser automation via claude-in-chrome or playwright-cli.

### Login Flow
1. Navigate to `https://convenexevents.com/wp-admin/`
2. Enter credentials (Kai uses the admin account — Nathan holds these)
3. Click Log In → wait for dashboard

### Open Elementor Editor
```
https://convenexevents.com/wp-admin/post.php?post={PAGE_ID}&action=elementor
```
Wait for the Elementor loading overlay to disappear (5–10 seconds) before interacting.

### Common Visual Edits (browser only)
- **Edit text in place**: click element → left sidebar Content tab → edit field → Ctrl+S
- **Change image**: click image widget → Media Library → select → Insert Media → save
- **Edit button**: click button → Content tab (text/URL) → Style tab (colours/padding) → save
- **Add section**: click + icon in editor → drag widget from left panel
- **Apply template**: click folder icon → My Templates → Insert

### playwright-cli Pattern
```bash
playwright-cli -s=wp-editor open "https://convenexevents.com/wp-admin/"
# Login, then:
playwright-cli -s=wp-editor navigate "https://convenexevents.com/wp-admin/post.php?post={ID}&action=elementor"
playwright-cli -s=wp-editor screenshot --filename=before-edit.png
# Make changes via click/type interactions
playwright-cli -s=wp-editor screenshot --filename=after-edit.png
```

---

## Part D: Scraping External Sites to Elementor Pages
*Source: lmoncany/elementor-claude-skill*

Kai can convert any external URL's content structure into a new Elementor page.

### Pipeline
```
Scrape URL → Clean Markdown → Elementor JSON → WP-CLI Injection → Live Draft
```

**Scrape with Firecrawl (requires Firecrawl API key):**
Ask Claude Code to use Firecrawl to scrape the target URL and return clean Markdown. Claude then transforms the content structure into Elementor Flexbox Container JSON matching the CX brand.

**Without Firecrawl:** paste the target page's HTML/copy directly and ask Claude to build an Elementor page from it with the CX brand applied.

**Use case for CX:** competitor venue pages, event format examples, or agency reference pages can be scraped, re-themed with CX brand colours, and used as layout inspiration for new pages.

---

## Part E: WP-CLI Install Commands for These Skills

```bash
# Install all three Elementor skills into Jarvis/Claude Code
# Run from G:\My Drive\Doctor Doom

# jezweb (browser automation + WP-CLI editing)
npx skills add https://github.com/jezweb/claude-skills --skill wordpress-elementor

# lmoncany (JSON injection + page creation from scratch)
# Manual copy — no npx installer:
# Download elementor-wordpress.md and place in .claude/skills/

# get-proofpilot (host-agnostic, calibration-first)
git clone https://github.com/get-proofpilot/claude-elementor-skill ~/.claude/skills/elementor
```

---

## Summary: Kai's Updated Capability Map

| Task | Method | Skill source |
|---|---|---|
| Edit text/URLs in existing page | WP-CLI search-replace | Existing skills.md |
| Edit layout/styling visually | Browser automation / Elementor editor | jezweb + existing |
| Create new page from JSON prompt | WP-CLI eval + Flexbox Container JSON | lmoncany |
| Build page matching site design | Calibration export → Claude → inject | get-proofpilot |
| Bulk create pages from list | WP-CLI loop + JSON injection | lmoncany |
| Scrape → Elementor page | Firecrawl → JSON → inject | lmoncany |
| Fix broken Elementor JSON | ID fixer + JSON validator | lmoncany |
| Template duplication | WP-CLI meta copy | Existing skills.md |
