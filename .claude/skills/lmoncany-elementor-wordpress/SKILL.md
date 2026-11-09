---
name: lmoncany-elementor-wordpress
description: "Elementor + WordPress reference (lmoncany, official) for Kai."
---

# Elementor WordPress Skill

You are an expert at building WordPress Elementor pages entirely from the CLI using WP-CLI. You never need a browser. You create beautiful, modern pages using Elementor's Flexbox Container system.

## Core Workflow

```
1. Scrape source (optional) → 2. Build Elementor JSON → 3. Create WP page → 4. Inject JSON → 5. Flush cache
```

## Rules (CRITICAL)

### JSON Format
- Elementor data is ALWAYS a **flat JSON array** `[...]` — NEVER wrapped in `{"content": [...]}` or any object
- Every element MUST have a unique `"id"` field: 8-character hex string (e.g., `"a1b2c3d4"`)
- Use `"elType": "container"` with flex settings — NEVER use legacy `"section"` or `"column"`
- Widgets use `"elType": "widget"` with a `"widgetType"` field
- Every element must have an `"elements": []` array (even if empty for widgets)

### Injection
- Always use `wp_slash(wp_json_encode($data))` when writing to `_elementor_data`
- Set ALL five required meta fields (see below)
- Always flush CSS after injection: `wp elementor flush-css`
- For scripts with `&$variable` (pass-by-reference), use `wp eval-file`, NOT `wp eval`

### Safety
- Always validate JSON before injection: `jq '.' file.json`
- Take a DB backup first: `wp db export backup.sql`
- Test on a draft page first, then publish after approval

## Elementor JSON Structure

```json
[
  {
    "id": "a1b2c3d4",
    "elType": "container",
    "settings": {
      "content_width": "boxed",
      "flex_direction": "column",
      "padding": {
        "top": "80", "bottom": "80",
        "left": "30", "right": "30",
        "unit": "px", "isLinked": false
      }
    },
    "elements": [
      {
        "id": "e5f6g7h8",
        "elType": "widget",
        "widgetType": "heading",
        "settings": {
          "title": "Your Heading",
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
          "editor": "<p>Your content here.</p>"
        },
        "elements": []
      }
    ]
  }
]
```

## WP-CLI Injection

### Step 1: Create the page
```bash
PAGE_ID=$(wp post create \
  --post_type=page \
  --post_title="Page Title" \
  --post_status=draft \
  --porcelain \
  --path=/path/to/wordpress)
echo "Created page ID: $PAGE_ID"
```

### Step 2: Write JSON to file
```bash
cat > /tmp/elementor-page.json << 'ENDJSON'
[your json array here]
ENDJSON

# Validate
jq '.' /tmp/elementor-page.json > /dev/null && echo "✓ Valid" || echo "✗ Invalid"
```

### Step 3: Inject via wp eval-file (preferred)
```php
<?php
// save as /tmp/inject.php — run with: wp eval-file /tmp/inject.php --path=/wordpress
$page_id   = PAGE_ID;
$json_file = '/tmp/elementor-page.json';

$json = file_get_contents($json_file);
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

WP_CLI::success('Done → ' . get_permalink($page_id));
```

```bash
wp eval-file /tmp/inject.php --path=/path/to/wordpress
```

### Step 4: Flush cache
```bash
wp elementor flush-css --path=/path/to/wordpress
```

### Step 5: Verify
```bash
wp post meta get $PAGE_ID _elementor_edit_mode --path=/path/to/wordpress
# Should return: builder

wp post get $PAGE_ID --field=guid --path=/path/to/wordpress
# Open this URL to preview
```

## Common Widget Types

| Widget | `widgetType` | Key Settings |
|--------|-------------|--------------|
| Heading | `heading` | `title`, `header_size` (h1-h6), `title_color`, `align` |
| Text | `text-editor` | `editor` (HTML string) |
| Button | `button` | `text`, `link.url`, `button_background_color`, `button_text_color` |
| Image | `image` | `image.url`, `image.alt` |
| Spacer | `spacer` | `space.size` (px number as string) |
| Divider | `divider` | `color`, `weight` |
| Video | `video` | `youtube_url` |
| Icon List | `icon-list` | `icon_list` (array) |

## Scraping to Elementor

When asked to clone a page from an external URL:

1. Use Firecrawl (if API key available) to convert URL → clean Markdown
2. Or paste the page HTML/copy directly
3. Claude transforms the content structure into Elementor Flexbox Container JSON
4. Apply site brand tokens on top of the scraped layout
5. Inject via WP-CLI as a draft

## Convene X Brand Tokens

```
Background: #0a0a0a    Pink accent: #FF1FA9
Card bg:    #141414    Yellow accent: #FCD500
White:      #f5f5f5    Muted: #a3a3a3
Display font: Fraunces  Body font: Libre Franklin  Mono font: IBM Plex Mono
Section padding: 80px vertical, 30px horizontal
```

Always build as `post_status=draft`. Nathan must approve before publishing.

## Fixing Common Issues

### Page renders blank
```bash
wp elementor flush-css --path=/path/to/wordpress
wp post meta get PAGE_ID _elementor_edit_mode --path=/path/to/wordpress
# Must return: builder
```

### JSON wrapped in object error
```bash
# Wrong: {"content": [...]}
# Fix:
jq '.content // .data // .elements // .' /tmp/bad.json > /tmp/fixed.json
```

### Missing element IDs
```bash
wp eval '
function fix_ids(&$elements) {
    foreach ($elements as &$el) {
        if (empty($el["id"])) $el["id"] = substr(md5(uniqid(mt_rand(), true)), 0, 8);
        if (!empty($el["elements"])) fix_ids($el["elements"]);
    }
}
$data = json_decode(get_post_meta(PAGE_ID, "_elementor_data", true), true);
fix_ids($data);
update_post_meta(PAGE_ID, "_elementor_data", wp_slash(wp_json_encode($data)));
echo "Fixed.\n";
' --path=/path/to/wordpress
```

## Bulk Page Creation

```bash
declare -a PAGES=("Executive Dinners" "Virtual Roundtables" "Webinars" "About Us")

for TITLE in "${PAGES[@]}"; do
    ID=$(wp post create \
      --post_type=page \
      --post_title="$TITLE" \
      --post_status=draft \
      --porcelain \
      --path=/path/to/wordpress)
    echo "Created: '$TITLE' → ID $ID"
done
```
