---
name: proofpilot-elementor-calibration
description: "Elementor calibration and QA checks (proofpilot) for Kai."
---

# Elementor Skill — Host-Agnostic, Calibration-First

Build and edit Elementor pages on convenexevents.com from the CLI. Calibrate first so new pages match the existing design exactly.

## How It Works

```
Calibrate (export real page) → Build on staging (clone real atoms) → Inject (wp eval-file inject.php) → Verify → Promote to live
```

An Elementor page is a JSON tree in postmeta `_elementor_data`. This skill reads a real page (**calibration**) so it learns your exact widgets and global-kit colour/typography IDs, then **clones and re-contents** those elements into a new page and injects it with one WP-CLI call. That's why the output matches your site.

---

## Step 0: Calibration (Once per Design Change)

Before building any new page, export a real convenexevents.com page so Claude learns the design.

### With WP-CLI (via WordPress MCP connector or Jarvis)

```bash
# Get the homepage post ID
wp option get page_on_front --path=/path/to/wordpress

# Export its Elementor data (this is your calibration file)
wp post meta get HOMEPAGE_ID _elementor_data \
  --format=json \
  --path=/path/to/wordpress > /tmp/calibration-homepage.json

echo "Calibration file ready: /tmp/calibration-homepage.json"
```

### Without WP-CLI (Elementor browser export)

1. Open Elementor editor on the page you want to calibrate
2. Click the hamburger menu (top-left) → **Save as Template**
3. Go to **Templates → Saved Templates**
4. Click **Export** on the template
5. Hand Claude the downloaded `.json` file

### What Calibration Gives Claude

From the exported JSON, Claude learns:
- Which **widgetTypes** are actually in use (avoids inventing unsupported types)
- The **global kit colour IDs** (e.g. `globals.color.primary`) — uses these instead of hardcoded hex values
- The **spacing and padding patterns** specific to convenexevents.com
- The **typography settings** (font sizes, weights, line-heights) in use
- The **container structure** (flex direction, content width, breakpoints)

### Using Calibration for New Pages

Pass the calibration JSON with any new page brief:

```
"Here is our current homepage Elementor data: [paste calibration-homepage.json]
Now build a new 'Why Executive Dinners' page that matches this design exactly,
with these sections: [your brief]"
```

---

## Step 1: Build on Staging (Always Draft First)

**MANDATORY for convenexevents.com** — never inject directly to published pages.

```bash
# Create page as draft
NEW_ID=$(wp post create \
  --post_type=page \
  --post_title="Your New Page Title" \
  --post_status=draft \
  --porcelain \
  --path=/path/to/wordpress)

echo "Draft page ID: $NEW_ID — $(wp post get $NEW_ID --field=guid)"
```

Claude generates the Elementor JSON based on your brief + calibration data. Save to `/tmp/new-page.json`.

---

## Step 2: Inject

### inject.php (recommended — safer than inline wp eval)

```php
<?php
// inject.php — wp eval-file inject.php --path=/wordpress
$page_id   = PAGE_ID;           // ← set before running
$json_file = '/tmp/new-page.json';

$json = file_get_contents($json_file);
if (!$json) {
    WP_CLI::error("Cannot read: $json_file");
}

$data = json_decode($json, true);
if (!$data || !is_array($data)) {
    WP_CLI::error('Invalid JSON: ' . json_last_error_msg());
}

update_post_meta($page_id, '_elementor_data',          wp_slash(wp_json_encode($data)));
update_post_meta($page_id, '_elementor_edit_mode',     'builder');
update_post_meta($page_id, '_elementor_template_type', 'wp-page');
update_post_meta($page_id, '_elementor_version',       '3.28.4');
update_post_meta($page_id, '_wp_page_template',        'elementor_header_footer');
wp_update_post(['ID' => $page_id, 'post_content' => '']);

WP_CLI::success("Done → " . get_permalink($page_id));
```

```bash
# Run injection
wp eval-file /tmp/inject.php --path=/path/to/wordpress

# Flush CSS cache
wp elementor flush-css --path=/path/to/wordpress
```

---

## Step 3: Verify (Server + Frontend)

```bash
# Server-side: check meta was written correctly
wp post meta get PAGE_ID _elementor_edit_mode --path=/path/to/wordpress
# Expected: builder

wp post meta get PAGE_ID _elementor_template_type --path=/path/to/wordpress
# Expected: wp-page

# Get the draft preview URL
wp post get PAGE_ID --field=guid --path=/path/to/wordpress
```

Open the draft URL in browser and check:
- [ ] Layout matches calibration design
- [ ] Brand colours correct (black/pink/yellow)
- [ ] Typography matches (Fraunces headings, Libre Franklin body, IBM Plex Mono labels/data)
- [ ] Responsive at mobile (≤600px)
- [ ] No blank sections / "page has no sections" message

---

## Step 4: Approval Chain

1. Kai verifies visually (draft URL)
2. Callum confirms SEO checklist (focus keyword, meta, Rank Math ≥70)
3. Felix brand review (copy/visual consistency)
4. Freya sign-off
5. Nathan final approval

**Only after Nathan approves:**

```bash
wp post update PAGE_ID --post_status=publish --path=/path/to/wordpress
wp elementor flush-css --path=/path/to/wordpress
```

---

## WP-CLI Cheat Sheet for convenexevents.com

```bash
# List all Elementor pages
wp post list --post_type=page --meta_key=_elementor_edit_mode --meta_value=builder \
  --fields=ID,post_title,post_name,post_status --path=/path/to/wordpress

# Take a database backup before touching live content
wp db export /tmp/backup-$(date +%Y%m%d-%H%M).sql --path=/path/to/wordpress

# Flush Elementor CSS cache
wp elementor flush-css --path=/path/to/wordpress

# Check Elementor version
wp plugin get elementor --fields=version --path=/path/to/wordpress

# Validate JSON before injecting
jq 'type, length' /tmp/new-page.json
# Should return: "array" and a number > 0

# Check all Elementor postmeta on a page
wp post meta list PAGE_ID --keys=_elementor_data,_elementor_edit_mode,_elementor_template_type,_elementor_version --path=/path/to/wordpress
```

---

## Access for convenexevents.com

| Access method | Status | Notes |
|---|---|---|
| WordPress MCP connector | ✅ Live | 90 tools, no delete tools |
| Jarvis SSH | 🔮 Future | Config in jarvis/connectors.md |
| Direct WP-CLI | Via MCP or SSH | Not direct terminal access yet |

---

## Safety Rules (convenexevents.com specific)

- **Always draft first** — `post_status=draft` before any inject
- **Always back up** before touching any existing published page: `wp db export`
- **No delete tools** — technically blocked at MCP level regardless
- **Nathan approval** required before any `post_status=publish`
- **Callum SEO check** required before publish (Rank Math ≥70, focus keyword set)

---

## Global Kit Colour Reference

After calibrating from the homepage, Claude will know the actual global kit IDs. Typical CX structure:

```json
"settings": {
  "title_color": {
    "id": "primary",
    "global": "globals/colors?id=primary"
  }
}
```

Using global IDs (rather than hardcoded hex) means site-wide colour changes flow through automatically. Ask Claude to use global IDs wherever the calibration JSON shows them.
