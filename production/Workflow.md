# WildNest Studio Production Workflow

> **Document ID:** WSPW-001  
> **Version:** 1.0  
> **Status:** Canonical Daily Operational Playbook  
> **Owner:** Chief Operating Officer (COO) & Executive Producer  
> **Last Updated:** 2026-08-05  

---

> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** [Studio README](file:///e:/Animation/wildnest-studio/README.md) ──► [production/](file:///e:/Animation/wildnest-studio/production/index.md) ──► `Workflow.md`  
> 🎯 **Canonical Source:** [WPOS-001 AI Production Pipeline OS](file:///e:/Animation/wildnest-studio/docs/09_Production/01_AI_Production_Pipeline.md)  
> 📜 **Governing Standard:** [STD-PROD-001 Production Standard](file:///e:/Animation/wildnest-studio/standards/Production_Standard.md)  

---


## Executive Summary & Primary Business Objective

This document is the **official daily operational workflow (WSPW-001)** for WildNest Studio. Authored by the Chief Operating Officer (COO) and Executive Producer, this manual is the single file opened every morning before animation production begins.

### The Primary Business Objective
> **OPERATIONAL GOAL:** Publish high-quality AI-generated YouTube Shorts and Episodes as quickly, consistently, and efficiently as possible while building an automated, scalable AI animation factory.

This playbook eliminates decision fatigue, context switching, duplicate work, and tool confusion by codifying every step from raw idea to published video.

---

## Section 1 — Production Philosophy

1. **We Optimize for Publishing:** A finished video published on YouTube generates real audience data; an unfinished masterpiece on a local hard drive generates zero value.
2. **We Build Reusable Asset Moats:** Every completed character turnaround, master 3D environment set, color swatch, and prompt manifest is archived to permanently reduce future production time.
3. **Shipping Over Perfection:** We pursue high production quality through rapid iterative feedback rather than delayed perfectionism.
4. **Data-Driven Evolution:** Real audience retention graphs, CTR metrics, and viewer comments dictate pipeline improvements.
5. **Tool-Agnostic Capability Architecture:** Software tools change rapidly; our underlying production capabilities, character consistency protocols, and quality standards are permanent studio IP.

---

## Section 2 — Daily Production Workflow (The 14-Stage Chain)

Every WildNest video follows a strict 14-stage sequential execution chain:

```
[1. IDEA] ──► [2. BRIEF] ──► [3. SCRIPT] ──► [4. SHOT LIST] ──► [5. ASSET GEN] ──► [6. VIDEO GEN] ──► [7. VOICE GEN]
                                                                                                      │
[14. RETRO] ◄── [13. ANALYTICS] ◄── [12. UPLOAD] ◄── [11. THUMBNAIL] ◄── [10. QA AUDIT] ◄── [9. EDITING] ◄── [8. MUSIC & SFX]
```

### Stage Breakdown
1. **Idea:** Concept submission adhering to core story pillars (Workplace comedy, secret pet resort).
2. **Brief:** Complete `00_Brief.md` defining goals, theme, character flaw engines, and budget.
3. **Script:** Write script enforcing Hinglish 8-word sentence rule and Silent Mute Test.
4. **Shot List:** Break down screenplay into Scene IDs, lens angles, and AI prompt asset manifests.
5. **Asset Generation:** Generate locked 3D background sets and character keyframe poses (Flux/SDXL).
6. **Video Generation:** Render 24fps progressive video clips (Veo/Runway) with ControlNet pose guides.
7. **Voice Generation:** Synthesize Hinglish dialogue & non-verbal squeaks (ElevenLabs soundbanks).
8. **Music & SFX:** Layer 110 BPM music stems, pneumatic tube *thwips*, water squirts, and foley.
9. **Editing Assembly:** NLE timeline assembly; enforce mandatory 1.5-second (36-frame) reaction holds.
10. **QA Audit:** Execute 8-Gate Studio Quality Inspection Checklist.
11. **Thumbnail:** Render 3-Element CTR thumbnail (60% emotion face + 30% tube bg + 10% prop).
12. **Upload & Publishing:** Upload 4K MP4 to YouTube; attach 3 SRT subtitle tracks; lock metadata.
13. **Analytics Tracking:** Monitor 24h & 48h Retention (>70%), CTR (>10.5%), and Shorts conversion.
14. **Retrospective:** Document production bottlenecks, update `CHANGELOG.md`, and refine prompts.

---

## Section 3 — Standard Folder Structure

Every production sprint must instantiate this exact workspace directory layout under `production/current/`:

```
production/current/[PRODUCTION_ID]/
├── 00_Brief.md              <-- Creative & production brief
├── 01_Script.md             <-- Locked screenplay / dialogue lines
├── 02_Shot_List.md          <-- Timecoded shotboard & prompt manifest
├── assets/                  <-- Source reference models & character turnaround LoRAs
├── outputs/                 <-- Raw AI image renders & video clips (Timestamped, un-edited)
├── review/                  <-- Selected candidate shots & QA audit feedback
└── final/                   <-- Master 4K video render, SRT subtitles, & published thumbnail
```

---

## Section 4 — Standard File Naming Conventions

All assets across local depots and AI prompt parameters must follow strict naming syntax:

```
ASSET CATEGORY          NAMING CONVENTION FORMULA                       EXAMPLE
──────────────          ─────────────────────────                       ───────
Character Turnaround    [CHR_ID]_[VIEW]_[VERSION].[ext]                 CHR-001_FRONT_V01.png
Environment Master Set  [ENV_ID]_[PRESET]_[VERSION].[ext]              ENV-LOBBY_ANGLE01_V01.png
Raw Video Shot          [PROD_ID]_SC[SCENE]_TAKE[TAKE].[ext]            SHORT-001_SC03_TAKE02.mp4
Voice Stem              VOICE_[CHAR]_[LINE_ID]_[LANG].[ext]             VOICE_BARNABY_L01_HINGLISH.wav
Music Track             MUSIC_[MOOD]_[BPM]BPM_V[VER].[ext]              MUSIC_TENSION_135BPM_V01.wav
Master Prompt File      [PROD_ID]_PROMPT_[MODEL]_V[VER].txt             EP-001_PROMPT_FLUX_V01.txt
Final Master Render     [PROD_ID]_MASTER_[RES]_[DATE].[ext]             EP-001_MASTER_4K_20260805.mp4
```

---

## Section 5 — Daily Production Checklist

### Morning Ritual (08:00 – 08:30)
- [ ] Review today's target production goal & delivery deadline.
- [ ] Open active workspace in `production/current/[PRODUCTION_ID]/`.
- [ ] Inspect yesterday's QA feedback notes and rendering logs.
- [ ] Confirm batch render queues and API compute token availability.

### Active Production (08:30 – 17:00)
- [ ] Execute shot generation strictly following `02_Shot_List.md`.
- [ ] Save incremental version passes (`V01`, `V02`) for every prompt iteration.
- [ ] Move raw renders to `outputs/` and filter top candidates into `review/`.
- [ ] Verify 1.5-second reaction holds during NLE timeline editing.

### End-of-Day Wrap (17:00 – 17:30)
- [ ] Commit all updated script files, shot lists, and notes to Git.
- [ ] Move 100% approved assets into `final/`.
- [ ] Update `CHANGELOG.md` with daily production progress.
- [ ] Queue overnight batch image renders and set next morning's priority task.

---

## Section 6 — AI Tool Workflow & Capabilities Stack

WildNest maps software tools to **functional production capabilities**, allowing seamless vendor replacement without workflow disruption:

```
CAPABILITY AREA             CURRENT RECOMMENDED SOFTWARE      FALLBACK / REPLACEMENT SOFTWARE
─────────────────────────   ────────────────────────────      ───────────────────────────────
Creative & Scripting        ChatGPT Plus / Claude 3.5 Sonnet   Local Llama 3 70B
Image Generation            Flux Dev 1.0 (Local GPU)          Midjourney v6.0 / SDXL Turbo
Video Generation            Runway Gen-3 Alpha / Veo          Luma Dream Machine / Pika 2.0
Voice Synthesis             ElevenLabs Professional Voice     Local Chatterbox TTS / VITS
Audio Editing & Foley       DaVinci Resolve Fairlight         Adobe Audition / Reaper
NLE Timeline Editing        DaVinci Resolve Studio 19         Premiere Pro / Final Cut Pro
Subtitle Generation         Whisper AI Auto-Caption           CapCut Pro / Aegisub
Publishing & Analytics      YouTube Studio Dashboard          Vidalytics / TubeBuddy
```

---

## Section 7 — Mandatory Production Rules

1. **Never Overwrite Approved Assets:** Always increment version numbers (`V01` ──► `V02`). Never save over files in `final/`.
2. **Version All Prompts:** Save positive and negative prompt text files alongside generated image batches.
3. **Preserve Source Files:** Store multi-track NLE project files (`.drp` / `.prproj`) and raw audio WAV stems.
4. **Mandatory Asset Reuse:** Reuse established Lobby Tower sets and Barnaby LoRAs across episodes before rendering new environments.
5. **Strict Brief Tracing:** Every scene and dialogue line must trace back to an approved `00_Brief.md`.
6. **Sprint Retrospective Gate:** No production sprint is closed until a post-mortem retrospective is completed.

---

## Section 8 — Quality Gates Matrix

Before advancing an asset to the next stage, verify all **8 Quality Gates**:

- [ ] **Gate 1 (Story):** 6-beat hybrid structure verified; script passes Silent Mute Test.
- [ ] **Gate 2 (Character):** Barnaby matches Golden Amber fur (`#D48C46`) and Red Twist-Tie Bowtie (`#D62828`) in 100% of shots.
- [ ] **Gate 3 (Visual Consistency):** Zero set drift or perspective warping across camera angles.
- [ ] **Gate 4 (Animation Quality):** 24fps smooth render with zero AI melting artifacts.
- [ ] **Gate 5 (Voice):** Hinglish dialogue cadence clear; non-verbal squeaks integrated.
- [ ] **Gate 6 (Music & SFX):** Stereo music balanced; audio mixed to -14 LUFS integrated.
- [ ] **Gate 7 (Branding):** WildNest 3D end card & subscriber callout attached.
- [ ] **Gate 8 (Thumbnail):** Passes 3-Element CTR rule (60% emotion face + 30% background + 10% prop).

---

## Section 9 — MVP Launch Strategy

WildNest executes a progressive 4-phase rollout strategy:

```
  PHASE 1: 10 YOUTUBE SHORTS  ──►  PHASE 2: PIPELINE TUNING  ──►  PHASE 3: EPISODE 001  ──►  PHASE 4: RECURRING SERIES
  (Viral Slapstick Test)           (Data Retention Audit)          (Flagship Pilot Launch)     (Scalable 24-Ep Season)
```

### Why Shorts First?
YouTube Shorts provide the fastest path to channel validation:
* **Rapid Iteration:** Produce and publish in 24–48 hours.
* **Algorithm Exposure:** Rapid organic reach testing visual slapstick hooks.
* **Immediate Data Feedback:** 30-second retention graphs isolate precise viewer drop-off points.

---

## Section 10 — Weekly Production Rhythm

```
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐
│   MONDAY    │   TUESDAY   │  WEDNESDAY  │  THURSDAY   │   FRIDAY    │  SATURDAY   │   SUNDAY    │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤
│  Planning & │ Asset & Prompt│ Video Render │ NLE Edit &  │ QA Audit &  │ Analytics   │ Pipeline &  │
│  Scripting  │ Generation  │ & Voice Mix │ Subtitles   │ Publishing  │ Tracking    │ Prompt Fixes│
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
```

---

## Section 11 — Production Metrics & KPI Dashboard

Track production performance weekly using these core benchmarks:

```
METRIC                      TARGET BENCHMARK            BUSINESS PURPOSE
──────────                  ────────────────            ────────────────
Publishing Velocity         2 Shorts + 1 Ep / Week      Channel growth & content density
Compute Cost per Short      < $15 USD / Short           Operational margin efficiency
Compute Cost per Episode    < $40 USD / Episode         Scale economics
AI First-Pass Yield         > 85% Success Rate          Minimizing wasted render compute
Asset Reuse Ratio           > 75% Set & Model Reuse     Production speed acceleration
Audience Retention (30s)    > 70% Viewer Retention      Algorithm promotion trigger
YouTube CTR                 > 10.5% Click Rate          Thumbnail & title effectiveness
```

---

## Section 12 — Continuous Improvement Framework

After every published video, the production team conducts a 15-minute retrospective addressing **5 Core Questions**:

1. *What worked exceptionally well in this render?*
2. *What failed or produced visual glitches?*
3. *What bottleneck slowed down editing or asset generation?*
4. *What repetitive task can be automated via Python scripts or ComfyUI nodes?*
5. *What operational insight should be added to studio documentation?*

---

## Section 13 — CEO Operating Principles

1. **Publish Before Perfect:** Market feedback beats internal speculation.
2. **Systems Over Hacks:** Build reusable workflows, not one-off tricks.
3. **Characters Are Long-Term IP Assets:** Consistency creates emotional brand equity.
4. **Documentation Serves Production:** Docs must be short, practical, and executable.
5. **Production Serves Audience:** Every frame must deliver joy, cuteness, or cozy resolution.
6. **Audience Feedback Drives Evolution:** Data tells us what to refine next.
7. **Build a Repeatable AI Animation Factory:** Scale throughput without sacrificing quality.

---

## References

* WSPW-001 Master Playbook (UNI-001, CHR-BIBLE-001, CHR-001, ART-001, BRAND-001, WPOS-001, WPOS-MVP-001, EP-001 Brief, PROD-CHR-001, 00_Prompt_Guidelines.md, 01_Master_Image_Prompt.md, 02_Negative_Prompt.md).
* WildNest Studio Operational Register (August 5, 2026).