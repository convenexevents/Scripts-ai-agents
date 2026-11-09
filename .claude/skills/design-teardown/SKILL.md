---
name: design-teardown
description: "Compare two products or websites and turn the differences into design actions (Kai)."
---

# Design Teardown — Kai Novak Usage Notes

Primary use: benchmark convenexevents.com against competitor executive event agencies to identify specific CSS/design gaps — not opinions, actual measured values.

## Trigger phrases
- `/design-teardown https://convenexevents.com https://competitor.com`
- "compare our site to [competitor] and tell me what to fix"
- "why does their site look more premium than ours"

## What it produces
1. Measured token diff across 9 dimensions (surfaces, hairlines, text roles, letter spacing, accent, type scale, radii, elevation, rhythm)
2. Fix list ranked by visible effect per hour — split into Mechanical (find-and-replace today) and Needs a Decision (someone must choose)
3. Interactive HTML teardown page with live controls (before/after toggle on B key, sliders, steppers)
4. Notion page if Notion MCP is connected

## Nine dimensions measured
| Dimension | What it catches |
|---|---|
| Surfaces | Canvas + card backgrounds, elevation levels |
| Hairlines | Border colour and width |
| Text roles | Heading, secondary, body, muted — four separate values |
| Letter spacing | Tracking in em at display and body size |
| Accent | Hue + how many times it appears in one viewport |
| Type scale | Every distinct rendered size and weight |
| Radii | Every distinct radius in the DOM |
| Elevation | Shadow layers and spread vs inset hairlines |
| Rhythm | Container width, section padding, divider usage |

## Convene X usage
- Run monthly after Callum's SEO audit — pair with competitors identified in Nadia's competitive reports
- Good reference sites for CX: executive event agencies, premium B2B consultancy sites, members club sites (Soho House, YPO)
- Never copy competitor brand colours or copy — take the discipline (spacing, tracking, contrast), not the identity
- All fixes route through the normal approval chain: Kai implements → Felix brand check → Freya → Nathan

## Hard rules
1. Every number must come from the live DOM — never from memory or estimation
2. Never copy the reference's copy, marks, imagery or brand colour
3. Leave anything of CX's own design that is already strong
4. Real logos only — pull actual SVGs from their sites, never draw approximations
