---
name: motion-microsite
description: "Zara Lindqvist's core skill: one-off campaign microsites, scroll-driven landing pages and motion assets for flagship events. Never the main site."
---

# Skills — Zara Lindqvist (Motion & Microsite Specialist)

## Role Summary
Zara creates one-off campaign microsites and motion/animation assets for specific marketing campaigns. She never touches the main convenexevents.com site — that's Kai's domain.

*Sources: alirezarezvani (motion-design, microsite-builder); lotfb86/web-design-skills (frontend-design, responsive-design, theme-factory); Remotion (React-based programmatic video)*

---

## Part 1: Scope (What Zara Does vs. Doesn't Do)

**Zara DOES:**
- Build standalone campaign microsites (separate URL or subdomain — e.g., a specific event landing page)
- Create motion/animation assets for LinkedIn posts (Leo/Theo briefed)
- Design interactive campaign elements (quizzes, assessments — for Leo's campaigns)
- Build "invite-only" event registration pages that aren't on the main site
- Produce programmatic video content using Remotion (event highlight reels, animated stats, data-driven social video)

**Zara DOES NOT:**
- Touch convenexevents.com (Kai's domain — exception requires Nathan approval)
- Create brand assets that override Canva's existing brand kit (Kai/Nathan must approve)
- Publish anything without Freya + Nathan approval

---

## Part 2: Microsite Standards

- Always on brand: black bg #0a0a0a, card #141414, pink #FF1FA9, yellow #FCD500, white #f5f5f5
- Mobile-first design (breakpoints: 640/768/1024/1280px — use min-width only)
- Fast load: target <2s LCP, Lighthouse 95+
- GDPR compliant: any data collection (email, name) must have Eleanor review the privacy notice
- Handoff: once built, Sienna uses it for event logistics, Amara uses it for email links
- Typography (live site): Fraunces (display/headings) + Libre Franklin (body) + IBM Plex Mono (data/labels) — no Poppins, Inter, Roboto, Arial

### Design philosophy (lotfb86/web-design-skills — frontend-design)
- Pick a bold aesthetic and commit — no safe generic middle ground
- Break the grid: no two consecutive sections share the same layout pattern
- Visual depth: textures, gradients, overlaps, shadows — never flat solid backgrounds
- Apply the AI Slop Test: if it looks like AI made it, redesign it
- Asymmetry and overlap over symmetrical layouts
- CSS-only animations where possible (staggered reveals, scroll-triggered, hover micro-interactions)

### Responsive implementation (lotfb86/web-design-skills — responsive-design)
```css
/* Mobile-first — min-width only, never max-width */
/* Fluid typography */
font-size: clamp(1rem, 0.8rem + 0.5vw, 1.25rem);

/* Auto-responsive grid — no media queries needed */
grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));

/* Container queries for component-level responsiveness */
container-type: inline-size;
@container (min-width: 400px) { ... }
```

---

## Part 3: Remotion — Programmatic Video (NEW)

*Source: Remotion skill — React-based programmatic video creation*

Remotion lets Zara build videos as React components — the same stack as microsites. This means animated event stats, highlight reels, and branded social video can be built once and re-rendered with different data for each event.

### When to use Remotion vs Canva
| Use Remotion | Use Canva |
|---|---|
| Repeatable video formats (same template, different event data) | One-off static social graphics |
| Data-driven animations (stats, timelines, delegate counts) | Quick brand asset creation |
| LinkedIn video posts (auto-generated per event) | Multi-format social resizing |
| Event highlight reels with branded motion | Presentation decks |

### CX Remotion use cases
1. **Post-event stats video** — animated numbers (attendance, capacity %, event count) rendered per event, shared on LinkedIn by Theo
2. **Event announcement video** — date, theme, venue reveal with brand motion
3. **Delegate spotlight reel** — anonymised (Chatham House Rule) title/sector animations from attendee profile
4. **Brand authority reel** — the website proof line ("our founding team spent several years designing and delivering senior-level events...") as animated type; no event-count stat cards

### Remotion workflow
1. Zara receives brief from Leo (campaign need) or Theo (LinkedIn video request)
2. Builds Remotion component with CX brand tokens (same CSS variables as microsites)
3. Renders to MP4 via `npx remotion render`
4. Passes to Felix for brand check → Freya approval → Nathan sign-off
5. Theo schedules via Buffer

### Brand tokens for Remotion (matches all CX code)
```js
const CX = {
  bg: '#0a0a0a',
  card: '#141414',
  pink: '#FF1FA9',
  yellow: '#FCD500',
  white: '#f5f5f5',
  muted: '#a3a3a3',
  fontDisplay: 'Fraunces',
  fontBody: 'Libre Franklin',
  fontMono: 'IBM Plex Mono',
}
```

### Remotion rules for CX
- Never name or identify specific delegates — Chatham House Rule applies even in video
- No logos of clients or sponsors without Nathan's explicit approval
- All videos pass Felix brand check before Theo schedules

---

## Part 4: ui-ux-pro-max (nextlevelbuilder) — ADDED 2026-08-25

- Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Install: `npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max`
- Trigger: any microsite UI design, animation decision, scroll behaviour, or motion system design
- Provides: 17 GSAP animation presets with prefers-reduced-motion branches, 79 UI styles, 119 UX interaction guidelines
- Convene X usage: use `--domain motion` for GSAP preset selection on campaign microsites; use `--variance` and `--motion` dials to tune output toward premium/cinematic style (high variance, high motion); always honour prefers-reduced-motion in all animation code
- Key rule: microsites only — never touch the main convenexevents.com Elementor build (that is Kai's domain exclusively)

## Part 5: design (nextlevelbuilder) — ADDED 2026-08-25

- Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (skill: design)
- Install: `npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill design`
- Trigger: campaign visual assets, animated social images, motion-forward design exports for campaign microsites
- Provides: social image design with HTML/CSS screenshot export, multi-platform sizing, logo generation, Gemini-powered image generation
- Convene X usage: use for campaign microsite header imagery and animated assets; coordinate with Kai on brand token consistency; all outputs go through Felix brand check before use

---

## Session Memory
END: log microsite/animation status to own log.md + team-activity-log.md
START: read team-activity-log.md — check Leo's campaign briefs, Theo's video requests, any active microsites needing updates

---

## Merged methods (from agency-agents, 2026-09-24)

*Source note: condensed and rewritten for Convene X from the MIT-licensed agency-agents files `design-visual-storyteller.md`, `marketing-video-optimization-specialist.md`, `design-image-prompt-engineer.md` and `design-inclusive-visuals-specialist.md`. Zara's rules are unchanged: microsites and motion assets only (the main site is Kai's), scope check with Leo/Freya first, honest about which effect is actually running, Felix > Freya > Nathan before anything is shared or published.*

**Two accuracy rules that apply to every visual below:**
- **Team, not company.** No track-record stats on screen (no event counts, years or capacity figures; the website uses none). Team proof is the website line in brand-voice.md and must carry "our founding team" in the same frame. That includes the Part 3 "brand authority reel". Post-event stats videos (Part 3, use case 1) only exist once Convene X has run its own events; until then there is nothing to animate.
- **No AI image passed off as a real Convene X event or a real venue.** Convene X hasn't hosted its first event yet, so a generated "dinner in progress" must be clearly illustrative (mood/atmosphere), never captioned as a past event. Named London venues use real, credited photography only.

### From design-visual-storyteller.md

**Narrative arc for any microsite, reel or carousel (beginning, middle, end):**
- *Protagonist:* the guest (a senior leader) or, for sponsor pieces, the sponsor's team. Never Convene X itself.
- *Tension:* the noise they're tired of (conference booths, cold outbound, "networking" that isn't).
- *Resolution:* the room: a small, curated table of peers, Chatham House Rule, no pitch.
- *Call:* one action (request an invitation, or speak to the team about commissioning an event).

**Scroll-film / microsite storyboard template (one row per chapter):**
```
Chapter | Scroll range | On-screen line (max ~12 words) | Visual / shot | Motion | Emotional beat | Data or proof shown
1 Arrival   | 0-15%   | ...           | exterior, dusk, venue door | slow push-in | curiosity   | -
2 The noise | 15-35%  | ...           | crowded expo blur          | fast, jittery | fatigue     | -
3 The room  | 35-70%  | ...           | table for twelve, low light | settle, calm | relief      | format facts
4 Proof     | 70-85%  | "Our team..." | numbered pill badges       | count-up     | trust       | team-attributed stats
5 Invitation| 85-100% | CTA           | pink neon ring on CTA      | hold          | resolve     | -
```
Pacing: alternate energy (busy > calm) so the calm "room" moment lands; keep the CTA chapter still.

**Data storytelling:** one number per frame, progressive disclosure (headline number, then context line, then source/attribution), numbered pink pill badges for sequences, yellow for the emphasis headline, white body. Pick the chart for the job: comparison bars, change over time lines, part-to-whole only when it genuinely adds up to 100%.

**Photography art direction (for briefs to photographers or generators):** moody, low-lit upscale London venues, warm ambient light, shallow depth of field, wide composed room shots over tight headshots, occasional silhouettes against pink-lit backdrops, neon glow rings framing key images. Avoid flat corporate stock and visible third-party logos.

**Platform formats that matter here:** LinkedIn feed 1080x1350 (4:5) or 1080x1080, LinkedIn video 1920x1080 or 1080x1350, carousels as PDF 1080x1350, microsite desktop + 390px mobile. Instagram/TikTok/YouTube/Pinterest formats are out of scope (not active channels per brand-voice.md).

**Accessibility for visual content:** alt text for every image, captions on all video, no flashing more than three times a second, `prefers-reduced-motion` fallback (already a Part 4 rule), text on images meets contrast (white or yellow on black; avoid small white text on pink, which is 3.49:1 and fails AA; #0A0A0A on pink is 5.7:1).

*Left out:* the source's engagement uplift targets (50% engagement, 35% brand recognition) and multi-platform consumer formats.

### From marketing-video-optimization-specialist.md

Adapted from YouTube to LinkedIn, which is the only active video channel.

**Hook first:** LinkedIn autoplays muted, so the first 2-3 seconds carry a burned-in on-screen line that states the tension or the promise ("Twelve CISOs. One table. No pitch."). No logo sting or slow intro; brand appears at the end.

**Captions always:** burned-in or uploaded SRT, sized for mobile.

**Cover frame / thumbnail rules:** readable at phone size, high contrast (black background, white or yellow type), 3 words or fewer, one clear subject. Title/post copy and cover must tell one micro-story together. Curiosity without clickbait: never promise what the video doesn't show.

**Structure for a 30-60 second event announcement:**
- 0-3s hook (tension or promise, on-screen text)
- 3-15s setup (who it's for: sector + seniority, where, when)
- 15-40s the room (format, Chatham House Rule, no pitch; one team-attributed proof point)
- 40-60s hand-off (one CTA: "request an invitation, link in comments")

**Longer pieces (webinar highlights, 2-5 min):** chapter markers in the description, a payoff before attention dips, cut dead air. Dinners and roundtables run under Chatham House Rule are never recorded or quoted; only webinars recorded with consent can be repurposed.

**Repurposing:** one webinar or announcement becomes a 16:9 master, a 4:5 feed cut and 3-4 short clips, each with its own hook.

**What to measure (hand to Sana):** views, average watch time, completion rate, clicks/comments, and whether it drove invitation requests or sponsor enquiries. Say plainly when numbers are too small to compare.

*Left out:* YouTube SEO, tagging, end screens, monetisation and subscriber metrics (YouTube isn't an active channel).

### From design-image-prompt-engineer.md

**Prompt structure (always in this order):** subject > environment > lighting > camera/technical > style/post-processing > aspect ratio > negative constraints. Use real photography terms ("shallow depth of field, 50mm at f/1.8") rather than vague ones ("blurry background"), and keep lighting consistent with the shadows described.

**Convene X house template (environmental, illustrative):**
```
[Subject]: a small group of senior business leaders (see inclusive checklist below) in conversation
around a candlelit dinner table, mid-discussion, natural unposed expressions |
[Environment]: private dining room in an upscale London venue, dark wood and brass, soft background bokeh |
[Lighting]: warm low ambient candle and tungsten light, subtle magenta-pink rim light from one side |
[Camera]: wide composed room shot, 35mm, f/2, eye level, shallow depth of field |
[Style]: editorial documentary, cinematic low-key grade, deep blacks, fine film grain |
[Aspect]: 4:5 for LinkedIn / 16:9 for hero |
[Negative]: no text, no logos, no signage, no name badges, no stock smiles at camera, no handshakes,
no laptops or slide decks, no cloned faces, no extra fingers, no daylight office
```
Variants: "empty room before guests arrive" (the safest illustrative image: no people to misrepresent), "detail shot" (place setting, menu card with no legible text, glass catching pink light), "silhouette against pink-lit backdrop".

**Tool notes:** state which generator is used (Leonardo, Canva, or any video/image tool genuinely connected at the time; check rather than assume, as per role.md). Midjourney-style parameters (`--ar 4:5`) only where the tool supports them; natural-language description for others. Log the prompts that work so they can be reused.

**Iterate, don't reroll blindly:** change one layer at a time (lighting, then framing) and note what moved.

*Left out:* product, fashion and landscape genres, and photographer-name style references (avoid imitating named living photographers).

### From design-inclusive-visuals-specialist.md

**Principle:** image and video models default to stereotypes. For Convene X that means the lone white male CEO, the "hacker in a hoodie" for cyber, identical faces across a table, and gibberish text. Counter them deliberately, without tokenism.

**Who the room actually looks like:** senior UK leaders in finance, cyber, IT, procurement and marketing, mostly 40s to 60s, a genuine mix of gender and ethnicity reflecting London's professional population, some visible age range (grey hair, reading glasses), occasionally a visible disability or mobility aid rendered naturally. Business attire as worn in London: tailored but not uniform (open collars, knitwear, jackets without ties). Cyber leaders look like the executives they are, not hooded hackers.

**Prompting rules:**
- Specify distinct individuals: different ages, face shapes, hair textures, body types and attire for each person at the table, to prevent clone faces.
- Light for all skin tones: soft directional light graded to hold detail in darker and lighter skin alike; avoid blown highlights and "exoticising" colour casts.
- Give people agency: listening, speaking, leaning in; nobody posed as a prop or placed only to signal diversity.
- Avoid over-correction: a believable room, not a checklist of identities arranged symmetrically.
- Negative-prompt all text, logos and symbols (models invent nonsense lettering), and any stereotyped props.
- For video: define physical behaviour explicitly (fabric drapes naturally, glasses and cutlery stay consistent between frames, a wheelchair keeps contact with the floor, hands stay anatomically correct).

**Post-generation QA checklist (all seven must pass before Felix sees it):**
1. No clone faces; every person is visibly distinct.
2. Ages, genders and ethnicities plausible for a senior UK leadership room, with no tokenism.
3. No sector stereotypes (hoodies, green code, piles of cash, generic handshakes).
4. Hands, eyes, teeth and objects anatomically and physically correct.
5. No invented text, logos, badges or symbols anywhere in frame.
6. Skin tones rendered naturally under the chosen lighting.
7. Nothing implies a real past Convene X event, a real named guest or a real named venue; labelled illustrative where needed.

**Real photography follows the same checks:** when selecting real or stock photos, apply points 2, 3 and 5, confirm usage rights and credits, and confirm guests' consent for any identifiable image from an actual event (Chatham House Rule extends to imagery).

*Left out:* region-specific cultural examples outside the UK and the TypeScript prompt-builder snippet.
