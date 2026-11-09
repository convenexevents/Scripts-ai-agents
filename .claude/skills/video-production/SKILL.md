---
name: video-production
description: "Rhys Calder's video playbook for cloud sessions: briefs, platform specs, ffmpeg recipes for trimming, reframing, captions, music and loudness, and verification habits. Use for any short video job."
---

# Skills: Rhys Calder

All installed 2026-11-06 as Claude Code skills in `C:\Users\User\.claude\skills\`. Invoke a skill by name (e.g. `/video-director`) and follow its SKILL.md; that file is the source of truth for the tool's steps.

## Tool map: which skill for which job

| Job | First choice | Why |
|---|---|---|
| Promo / launch film / sponsor pitch film as coded motion graphics | **video-director** (plan + verify) with **huashu-motion** (build + point-at-frame studio) | Strong story and timing checks; huashu opens a browser studio where Nathan can click a frame and comment |
| A finished short film from a one-line brief, studio-style (strategist, writer, reviewer) | **take-one** | Runs the full team process, prices any paid route and asks first |
| Explainer with voice-over (how a roundtable works, a sector brief) | **explainroo** | Local voice, no API key, word-timed visuals |
| Walkthrough of the website (Build Your Room, membership, sponsor page) | **argo-guide** | Records Playwright scripts of the real site with voice-over and overlays |
| Animate a logo, icon, illustration or mascot so it feels alive | **rossark-motion-skill** | Believable idle motion, pivots, follow-through |
| "Make it move like this reference" (a site, gif, video) | **reanimate** | Frame-by-frame clone plus verification |
| Choosing, checking or reviewing sound | **earshot** | Measures loudness, sync, realness; matches descriptions to sounds |
| Full soundtrack from real licensed recordings | **real-sound** (uses earshot) | Cue list, licence audit, mix, master, credits |
| Editing real footage (trim, join, reframe, captions, music, loudness) | ffmpeg directly | Recipes below |

Related, owned by others: `scroll-film-studio` (Zara). Higgsfield / Canva connectors cost credits: ask Nathan first.

## Where the tools live

- huashu-motion CLI: `C:\Users\User\video-tools\huashu-motion` (the skill's `bin/om` points here)
- earshot: `C:\Users\User\video-tools\earshot`, Python at `.venv\Scripts\python.exe` (models, about 1.1 GB, download on first use)
- explainroo: `C:\Users\User\.explainroo` (`node bin/explainroo.js`)
- take-one: inside its skill folder (`bash scripts/doctor.sh` checks the machine)
- argo: installed per video project (`npm i -D @argo-video/cli` plus `kokoro-js@1` for free local voice)
- reanimate: needs Bun (installed); first run downloads Chromium and a static ffmpeg (about 250 MB). Upstream says Windows is untested.
- System: ffmpeg/ffprobe 9.0.1, Node 24, Bun, Python 3.13 with numpy, scipy, Pillow; Chrome.

## Platform specs (defaults)

| Platform | Aspect | Size | Length |
|---|---|---|---|
| LinkedIn feed | 1:1 or 4:5 | 1080x1080 / 1080x1350 | 15-45 s |
| Reels, TikTok, Shorts | 9:16 | 1080x1920 | 15-30 s |
| Website hero / YouTube | 16:9 | 1920x1080 | 30-90 s |

Always burn in captions for social (most autoplay is muted). Loudness: -14 LUFS for social, -16 for web. The first frame must make sense as a still.

## ffmpeg recipes (real footage)

```bash
# trim without re-encode
ffmpeg -ss 00:00:05 -to 00:00:20 -i in.mp4 -c copy clip.mp4
# 16:9 to 9:16 centre crop, 1080x1920
ffmpeg -i in.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" -c:a copy vertical.mp4
# join clips listed in list.txt (one "file 'a.mp4'" per line)
ffmpeg -f concat -safe 0 -i list.txt -c copy joined.mp4
# burn in subtitles
ffmpeg -i in.mp4 -vf "subtitles=captions.srt" out.mp4
# loudness normalise to -14 LUFS
ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:v copy out.mp4
# music bed under existing audio
ffmpeg -i in.mp4 -i music.mp3 -filter_complex "[1:a]volume=0.2[m];[0:a][m]amix=inputs=2:duration=first" -c:v copy out.mp4
# contact sheet for checking a cut
ffmpeg -i in.mp4 -vf "fps=1,scale=320:-1,tile=6x5" sheet.png
```

## Verification habits

- Look at frames (contact sheet, `om still`, `om qa`, video-director `check_timeline.py`) before calling a cut done.
- Any claim about audio quotes an earshot number.
- Brand: pink accents/buttons with white text, yellow with black (see `00-overview/brand-voice.md`).
