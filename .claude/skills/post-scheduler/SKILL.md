---
name: post-scheduler
description: Schedule a finished social post to one or more platforms via Buffer. Handles single-platform and multi-platform scheduling, fetches connected Buffer channels, applies a final pre-publish check, gets explicit sign-off, and returns scheduled time + post IDs. Triggers on "schedule this," "post this to [platform]," "queue this in Buffer," or as the final step in content-coach and post-writer flows. Falls back to saving the post as a copy-paste file if Buffer isn't connected.
argument-hint: "[post text or path] [platform(s)] [optional time]"
allowed-tools: Read, Write, Edit, Glob, AskUserQuestion, mcp__Buffer__get_account, mcp__Buffer__list_channels, mcp__Buffer__get_channel, mcp__Buffer__create_post, mcp__Buffer__list_posts
---

# Post Scheduler (Buffer)

You take an approved post and ship it via Buffer. You do NOT write or revise the post. That's `post-writer`'s job. By the time a post reaches you, it's been graded and approved.

If Buffer isn't available (connector missing, no channel for the platform), fall back gracefully: save the post to a file the user can paste manually. Don't fail the flow.

**House rule: nothing is sent to Buffer without explicit sign-off for that specific post.** A Buffer post that isn't a draft will publish and can't be unsent.

## Connected channels (as of November 2026)

Organisation "My organization" (Buffer free plan: 3 channels, max 10 scheduled posts at once). Account timezone: Europe/London.

| Platform | Channel | Type | Notes |
|---|---|---|---|
| LinkedIn | convene-x-events | company page | **Default for all company content** |
| LinkedIn | convene-x-events-363baa3a3 | personal profile | Only if the user asks for the personal profile |
| Instagram | convenexevents | personal profile | Needs an image or video; reminder-only (see below) |

Company page queue (Europe/London): Mon 21:25/22:09, Tue 21:05/22:21, Wed 16:08/17:52, Thu 13:25/15:57, Fri 14:16/16:47, Sat 06:56/09:09, Sun 06:52/22:06. Change these in Buffer > channel > Posting Schedule.

Booking link for CTAs: https://cal.com/convenexevents/15min. On LinkedIn, put it in `metadata.linkedin.firstComment`, not the post body.

Always re-fetch IDs with `list_channels` rather than trusting this table. Never guess a channel ID.

## When to Activate

- "Schedule this post"
- "Post this to LinkedIn tomorrow at 9am"
- "Queue this in Buffer"
- Auto-called as the final step of `content-coach` after user approval.

## Workflow

### Step 1: Get inputs

You need:
1. **Post text**: inline, or path to a file
2. **Platform(s)**: linkedin and/or instagram (the connected channels). For any other platform, say it isn't connected in Buffer and offer the paste file.
3. **Time**: default is Buffer's queue (`mode: addToQueue`). Use `customScheduled` + `dueAt` only if the user names a time.
4. **Media** (Instagram only, required): a public, directly downloadable image or video URL.

If platform is missing, ask. Don't guess. For LinkedIn, default to the company page.

### Step 2: Final pre-publish check

Before touching Buffer, scan the post one more time for:

- [ ] Zero em dashes
- [ ] No banned filler ("really," "very," "just," "basically," "literally," "actually")
- [ ] No banned words from `brand-brief.md` (unlock, leverage, elevate, seamless, etc.)
- [ ] No filler openers ("in today's world," "let me tell you")
- [ ] Active voice, contractions used, UK spelling
- [ ] Hashtag count fits platform (0-3 for LinkedIn, 3-5 for Instagram)
- [ ] For Instagram: media URL is attached
- [ ] For LinkedIn: external links are flagged (they reduce reach; suggest putting the link in the first comment via `metadata.linkedin.firstComment`)
- [ ] Convene X non-negotiables (from `brand-brief.md`): no personal names, proof framed as "in previous roles", no "Convene X has delivered", no promised leads/ROI, no pricing, no unconfirmed numbers

If anything fails, **stop and report**:

```
Pre-publish check failed:
- [issue 1]
- [issue 2]

Want me to send this back to post-grader, or override and ship as-is?
```

Wait for explicit user response. Don't auto-fix without permission.

### Step 3: Fetch channels

1. `mcp__Buffer__get_account()` → organisation ID and `currentTime` (the reference for "now", "tomorrow", etc.). Tell the user which organisation you're using.
2. `mcp__Buffer__list_channels({ organizationId })` → match requested platforms to channel IDs. Skip any channel with `isDisconnected` or `isLocked` true and tell the user.

If a requested platform has **zero** channels:
```
No [platform] channel is connected to Buffer. To connect one, open
buffer.com > Channels > Connect a channel, then re-run this.

For now, I can save the post to a file so you can paste it manually. Want that?
```

### Step 4: Confirm before sending (required)

Show exactly what will happen and wait for an explicit yes:

```
Ready to send to Buffer:

| Channel | Mode | Time |
|---|---|---|
| LinkedIn company page (convene-x-events) | Queue | Next free slot |

Reply "schedule" to queue it, "draft" to save it as a Buffer draft instead, or "cancel".
```

"Draft" is the safe option: it sits in Buffer for a final review and never publishes on its own.

### Step 5: Send to Buffer

One `create_post` call per channel:

```
mcp__Buffer__create_post({
  channelId: "<exact id from list_channels>",
  schedulingType: "automatic",          // see Instagram note
  mode: "addToQueue",                   // or "customScheduled" + dueAt
  dueAt: "2026-11-12T09:00:00+00:00",   // only with customScheduled; Europe/London offset, must be in the future
  saveToDraft: false,                   // true if the user chose "draft"
  text: "<post text>",
  assets: [{ image: { url: "<public url>", metadata: { altText: "<description>" } } }]  // optional for LinkedIn
})
```

Platform specifics:
- **LinkedIn**: text-only is fine. Optional `metadata.linkedin.firstComment` for a link.
- **Instagram** (personal profile): requires an image or video asset, `metadata.instagram: { type: "post" | "reel" | "story", shouldShareToFeed: true }`, and **`schedulingType: "notification"`**. Buffer sends a phone reminder and the user publishes by hand. Tell them that.
- Never use `mode: "shareNow"` unless the user says "post now" or "publish immediately".

Buffer's free plan allows 10 scheduled posts at once. If `create_post` fails on a limit, tell the user and offer to save as a draft instead.

### Step 6: Report results

```
## Scheduled in Buffer

| Platform | Channel | Time | Status | Post ID |
|----------|---------|------|--------|---------|
| LinkedIn | convene-x-events (page) | Queue: Thu 12 Nov, 09:00 | Scheduled | 6a5... |

View or edit at https://publish.buffer.com
```

Use the `dueAt`/status the API returns, not your guess. For partial failures, report successes and failures separately. Don't roll back.

### Step 7: Fallback (no Buffer)

If the Buffer tools error out or aren't available:

```
Buffer isn't reachable right now. I've saved your post so you can copy-paste it manually.
```

Save to `post-ready-to-paste.txt` in the current directory:

```
=== POST FOR [PLATFORM] ===
Scheduled for: [time or "manual posting"]

[POST TEXT HERE]

=== END POST ===
```

If multi-platform, save one block per platform. Tell the user the file path.

## What NOT to Do

- **Don't send anything to Buffer without the Step 4 sign-off.** Every post, every time.
- **Don't auto-fix voice issues.** That's `post-grader` and `post-writer`'s job. You only flag and ask.
- **Don't skip the pre-publish check.** It's the last line of defence.
- **Don't publish immediately by default.** Default is the queue.
- **Don't guess channel IDs or timezones.** Use `list_channels` and `get_account`.
- **Don't fail silently.** Retry once, fall back to the file, or show the exact error.
- **Don't report success without the Buffer post ID.**

## Error Handling

- **Auth error**: Buffer connector needs reconnecting in claude.ai connector settings. Fall back to the file.
- **Rate limit**: Buffer returns `rateLimit` with `resetSeconds`. Wait or tell the user; retry once.
- **Validation error** (e.g. Instagram without media): show the error, ask for the missing piece.
- **Scheduled-post limit reached**: offer to save as a draft.
- **Post over character limit** (LinkedIn 3,000; Instagram 2,200): don't auto-truncate. Ask.
