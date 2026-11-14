# General ad: "Nobody sells" (14s, 9:16)

Owner: Rhys (Video). Status: **animatic draft**. Review: Felix > Freya > Nathan. Nothing is published.

## Brief
- **Audience:** senior leaders (guests) and B2B marketing/sales leaders (would-be hosts), on LinkedIn.
- **Platform:** LinkedIn feed and Reels, 9:16 1080x1920 (1:1 cut-down later).
- **Length:** 14s (10.4s of speakers + 3.6s end card).
- **One message:** invitation-only rooms of real senior peers, where nobody sells.
- **CTA:** Book a 15-minute call (link in the first comment on LinkedIn).

## Script and cast
The speakers are fictional and AI-generated. They are not testimonials and not presented as attendees of any Convene X event. A small "AI-generated" label stays on screen.

| Time | Speaker (fictional) | Line | Caption highlight |
|---|---|---|---|
| 0.0–2.2 | Exec 1, UK woman, 50s, warm and measured | "Real conversations." | Real |
| 2.2–4.2 | Exec 2, US man, 40s, relaxed and direct | "With genuine peers." | peers. |
| 4.2–6.4 | Exec 3, German woman, 40s, crisp | "Director level and above." | Director |
| 6.4–8.4 | Exec 4, UK man, 60s, dry and low | "Invitation only." | only. |
| 8.4–10.4 | Exec 5, French woman, 30s, half-smile | "And nobody sells." | nobody |
| 10.4–14.0 | End card | CONVENE X EVENTS · Executive dinners, roundtables and webinars for senior leaders. · [Book a 15-minute call] · convenexevents.com | |

Brand checks: UK English, no exclamation marks, no em dashes, no banned words, no stats, no event counts, no promise of leads or ROI, no names. "Director level and above" is cleared public copy (brand brief, 10 Nov).

## Look
- One shared setting so the cuts feel like one room: a warm, low-lit private dining room, candle and glassware bokeh behind, each person seated at the table and speaking straight to camera, chest-up framing, eye line centre-frame.
- Hard cut on each line with a 2-frame flash and a soft whoosh.
- Captions: Inter ExtraBold, off-white #F5F5F5, key word in pink #FF1FA9, lower third.
- End card: black #0A0A0A, pink rule and "EVENTS", yellow #FCD500 button with black text.

## Image prompts (one still per exec, 9:16)
Shared tail for all 5: *photorealistic, seated at a candlelit private dining table in a warm, upscale London restaurant, chest-up, looking directly into the camera, shallow depth of field, soft warm key light, 85mm, editorial, natural skin texture, no text, no logos.*
1. Woman in her 50s, British, short silver bob, navy blazer, calm confident expression, slight smile.
2. Man in his 40s, American, open-collar white shirt and charcoal jacket, relaxed posture, friendly.
3. Woman in her 40s, German, dark hair pulled back, black roll-neck, composed and precise.
4. Man in his 60s, British, grey beard, tweed jacket, dry knowing look.
5. Woman in her 30s, French, shoulder-length brown hair, cream silk blouse, playful half-smile.

## Voices (ElevenLabs)
Generate each line as its own file and leave about 0.15s of silence at the head and tail. Settings to start from: Stability 45, Similarity 75, Style 20, speaker boost on. Pick from the Voice Library by description:
1. British female, mature, warm, conversational.
2. American male, 40s, relaxed, natural.
3. German-accented English, female, clear, professional.
4. British male, older, deep, dry.
5. French-accented English, female, young, light and smiling.

Name the files `exec1.mp3` to `exec5.mp3` and Rhys will time them to the cut.

## Build route (needs Nathan's OK to spend)
1. 5 stills (image model).
2. Lip-sync each still to its voice file. Higgsfield **Intone** (talking-head, takes a character image and voice recording) fits this exactly; about 4s per clip.
3. Rhys swaps each clip into the animatic timeline, keeps the captions, end card and whooshes, then normalises to -14 LUFS and runs a contact sheet.

**Blocker:** the Higgsfield account has 0 credits (free plan), and ElevenLabs isn't connected to this session. Either top up Higgsfield or send the 5 voice files and stills.

## Files
- `convene-x-ad-animatic-9x16.mp4`: timed animatic with placeholder silhouettes, captions, end card and whooshes (measured -13.1 LUFS integrated).
- `render.py`: rebuilds the animatic (Python + Pillow + ffmpeg).

## v1 build (14 Nov): `convene-x-ad-v1-9x16.mp4`
Built without Higgsfield or Canva:
- **Faces:** 5 fictional executives, kie.ai nano-banana-2 at 1K, 8 credits each (40 credits, about $0.20). Prompts are in `stills.py`, and the outputs are in `stills/`.
- **Voices (ElevenLabs, eleven_multilingual_v2):** 1 Lily (British), 2 Chris (American), 3 Bella (American), 4 George (British), 5 Sarah (American). The cast was adjusted to match the available voices: Exec 3 is now American, not German, and Exec 5 is South Asian American, not French. Files are in `voices/`.
- **Ambience:** ElevenLabs sound effects, a restaurant murmur mixed low.
- **Style:** candid documentary, with the voice over a still photo and a slow push-in. There's no lip-sync, so the speakers are shown mid-conversation rather than talking to camera.
- **Checks:** 1080x1920, 14.0s, -14.6 LUFS integrated, -4.3 dBFS peak. Contact sheet reviewed.
- **Rebuild:** `python3 render_final.py out.mp4`, then the ffmpeg mix (voices at 0.15/2.3/4.3/6.5/8.5s, ambience at 0.18, whooshes at 0.25, loudnorm -14).

**Licence note:** check that the ElevenLabs plan allows commercial use of these voices before this runs as a paid ad.
