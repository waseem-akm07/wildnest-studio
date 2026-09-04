# WildNest Studio — Manual Production Standard Operating Procedure (SOP)

> **Document:** Master Manual Production Guide  
> **Version:** 1.1  
> **Purpose:** Step-by-step manual production checklist, explanations, and rules to create animated episodes and YouTube Shorts manually from this repository.

---

## TABLE OF CONTENTS
1. [The 3 Golden Rules of AI Animation](#1-the-3-golden-rules-of-ai-animation)
2. [Folder Setup (What to Copy)](#2-folder-setup--starting-a-new-project)
3. [Context Files (What to Feed to the AI Scriptwriter)](#3-context-files--what-to-give-the-ai)
4. [Deep-Dive: Step-by-Step Production Workflow](#4-deep-dive-step-by-step-production-workflow)
   - [Step 1: Script & Shot Board](#step-1-script--shot-board)
   - [Step 2: Generating Keyframe Images (In-Depth Guide)](#step-2-generating-keyframe-images-text-to-image)
   - [Step 3: Animating Video Clips (Image-to-Video Guide)](#step-3-animating-video-clips-image-to-video)
   - [Step 4: Generating Character Voices (TTS)](#step-4-generating-character-voices-tts)
   - [Step 5: Timeline Assembly & Captions in CapCut](#step-5-timeline-assembly--captions-in-capcut)
5. [AI Tools Directory (Free vs. Paid Options)](#5-ai-tools-directory-free-vs-paid)
6. [Pre-Upload Quality Checklist](#6-pre-upload-quality-checklist)

---

## 1. THE 3 GOLDEN RULES OF AI ANIMATION

1. **NEVER Use Text-to-Video Directly for Characters:**
   * If you ask an AI video generator directly: *"Make a video of a hamster in a bowtie"*, the hamster’s face, fur color, and clothes will morph and change every single time.
   * **Always use the 2-step method:**
     `Text-to-Image (Keyframe)` ──► `Image-to-Video (Motion)`.
2. **Always Keep Clips Short (3 to 5 Seconds):**
   * Current AI video generators maintain physical consistency and clean motion for 3–5 seconds. If a scene needs 10 seconds, split it into two 5-second shots.
3. **Respect the 1.5-Second Reaction Freeze:**
   * Comedy in WildNest Studio lives in the deadpan freeze (36 frames / 1.5s) where the character stares motionless at the camera with pin-prick pupils right before disaster strikes.

---

## 2. FOLDER SETUP — STARTING A NEW PROJECT

### For a Full Master Episode (2.5 Minutes, 16:9):
1. Duplicate `scripts/_template/`
2. Rename the copy to `scripts/EP-[XXX]/` (e.g., `scripts/EP-002/`).
3. You will have 3 files ready to fill:
   * `concept.md` — Episode idea & 6-Beat outline.
   * `script.md` — Dialogue & action beats.
   * `shot-list.md` — Timecoded shots with image & video prompts.

### For YouTube Shorts (15s – 60s, 9:16 Vertical):
1. Open the episode folder: `scripts/EP-[XXX]/shorts/`
2. Duplicate `scripts/_template/shorts/short_template.md`
3. Save it as `scripts/EP-[XXX]/shorts/SH-[Number]_[Title].md`
   * Example: `scripts/EP-001/shorts/SH-01_Cheek_Panic.md`

---

## 3. CONTEXT FILES — WHAT TO GIVE THE AI

When co-writing scripts or prompts with an AI assistant (in this IDE chat, Gemini, or Claude), provide these reference files from `bible/`:

| What You Need | File to Reference / Attach | What It Tells the AI |
|:---|:---|:---|
| **Character Visuals & Props** | [`bible/characters.md`](bible/characters.md) | Species, red bowtie, accessories, personality flaws. |
| **Art Style & Lighting** | [`bible/style-guide.md`](bible/style-guide.md) | 3D Pixar style, 24fps, lighting tones, camera angles. |
| **Story Arc & Comedy Rules** | [`bible/story-framework.md`](bible/story-framework.md) | 6-Beat structure, Hinglish rules (< 8 words), 1.5s freeze. |
| **Prompt Syntax** | [`prompts/video-prompts.md`](prompts/video-prompts.md) | Master formulas for dialogue and slapstick clips. |

---

## 4. DEEP-DIVE: STEP-BY-STEP PRODUCTION WORKFLOW

### Step 1: Script & Shot Board (Scriptwriter AI Instructions)

When co-writing with the **Scriptwriter AI** (in this IDE chat, Gemini, or Claude), the AI must always follow these strict aspect ratio rules:

1. **For Master Episodes (`scripts/EP-XXX/`):**
   * **Mandatory Ratio:** **`16:9` (Cinematic Widescreen)**
   * **Staging:** Horizontal room composition (allows characters to run left-to-right, wide lobby vistas).
   * **AI Image Prompts:** Must end with `--ar 16:9`.
   * **AI Video Prompts:** Must specify widescreen cinematic composition.

2. **For Shorts (`scripts/EP-XXX/shorts/`):**
   * **Mandatory Ratio:** **`9:16` (Vertical Tall)**
   * **Staging:** Vertical, tight framing centered on character faces and vertical gags (e.g. falling drops, flying upward).
   * **AI Image Prompts:** Must end with `--ar 9:16`.
   * **AI Video Prompts:** Must specify vertical 9:16 framing.

3. **Every shot produced by the AI must contain:**
   * **Timing & Beat:** Exact seconds and 6-Beat label.
   * **Hinglish Dialogue Line:** Maximum 8 words per sentence.
   * **Physical Action:** Slapstick movement + 1.5s freeze hold.
   * **AI Image Prompt:** Ready to copy for Flux/Midjourney.
   * **AI Video Prompt:** Ready to copy for Kling/Runway/Hailuo (I2V mode).

---

### Step 2: Generating Keyframe Images (Text-to-Image)

#### 🎥 The Studio Aspect Ratio Standard:
* **Full Episodes (EP-001, EP-002, etc.):** Always use **`16:9` (Widescreen Horizontal)**. This gives the cinematic Pixar movie look for TV, laptops, and tilted mobile screens.
* **YouTube Shorts (SH-01, SH-60, etc.):** Always use **`9:16` (Vertical Tall)**. This fills 100% of mobile screens in the Shorts feed.

---

#### 🤖 Do I Need to Tell the AI Tool Which Ratio to Use? (YES! Here is HOW):

| Tool Type | Tool Name | How to Tell It the Aspect Ratio |
|:---|:---|:---|
| **1. The Scriptwriter AI** | **This IDE Chat / Gemini / Claude** | When asking for a shot list, specify: *"This is for a 16:9 Episode"* OR *"This is for a 9:16 Short"*. The AI will automatically format the prompts with the correct tags. |
| **2. Image Generator (Discord)** | **Midjourney** | Add **`--ar 16:9`** (for episodes) or **`--ar 9:16`** (for shorts) at the very end of your prompt text. |
| **3. Image Generator (Web UI)** | **Leonardo.ai / Flux / Tensor.art** | Look at the sidebar settings: Click the **Aspect Ratio dropdown** and choose **`16:9 (Landscape)`** or **`9:16 (Portrait)`**. You do not need to type anything in the prompt box. |
| **4. Video Generator (I2V)** | **Kling AI / Hailuo AI / Runway** | **AUTOMATIC!** When you upload your keyframe image in **Image-to-Video** mode, the video AI automatically detects the image dimensions and matches it. (Upload a 16:9 image ──► outputs a 16:9 video; upload a 9:16 image ──► outputs a 9:16 video). Some tools also have a dropdown where you can confirm `16:9` or `9:16`. |
| **5. Video Editor** | **CapCut / DaVinci Resolve** | Click **Ratio** below the video preview window and choose **`16:9`** (Episode) or **`9:16`** (Shorts). |

---

#### 🛠️ How to Generate the Image (Action Steps):
1. Open your image generator: **Leonardo.ai** (Free daily tokens), **Flux.1** (via Fal.ai/Tensor.art), or **Midjourney**.
2. Set the canvas shape:
   * Select **`16:9`** for full episodes.
   * Select **`9:16`** for YouTube Shorts.
3. Copy the **AI Image Prompt** from your shot list:
   * **For 16:9 Episode (Shot 1):**
     ```text
     3D Pixar animation style, cinematic 16:9, a cute chubby golden Syrian hamster named Barnaby popping out of fluffy cedar wood shavings inside a luxury modern hamster cage, red twist-tie bowtie, warm morning sunlight, volumetric light, 8k resolution --ar 16:9
     ```
   * **For 9:16 Short (Shot 1):**
     ```text
     3D Pixar animation style, vertical 9:16 aspect ratio, a cute chubby golden Syrian hamster wearing a tiny red twist-tie bowtie inside a vertical colorful plastic hamster tube, bright cinematic lighting, volumetric light, 8k resolution --ar 9:16
     ```
4. Click **Generate**.
5. Pick the best image where Barnaby looks chubby, expressive, and has his **red twist-tie bowtie**.
6. Click **Download** and save the file into your local project:
   * Path: `assets/characters/EP001_Shot01_Keyframe.png` (or `assets/characters/SH01_Shot01_Keyframe.png`)

---

### Step 3: Animating Video Clips (Image-to-Video)

#### 🧐 What is Image-to-Video (I2V)?
Image-to-Video is a mode inside AI video generators where you **upload an image as the starting frame**, and describe only how that image should move.

#### 🛠️ How to Generate the Video Clip:
1. Open your AI video generator: **Kling AI** (free credits), **Hailuo AI / Minimax** (free), or **Runway Gen-3**.
2. Switch the mode from *Text-to-Video* to **Image-to-Video (I2V)**.
3. Click the **Upload Image** box and select your saved keyframe: `SH01_Shot01_Keyframe.png`.
4. In the motion prompt box, paste the **AI Video Prompt** from your shot list:
   ```text
   3D animated vertical clip, hamster proudly adjusts his red bowtie, suddenly startled as a spray of water shoots from above directly onto his face, flailing his tiny pink paws in funny surprise. Smooth 24fps motion, vertical framing.
   ```
5. Set duration to **5 seconds**.
6. Click **Generate**.
7. Download the finished 5-second video clip and save it to your repo:
   * Path: `assets/SH01_Shot01_Clip.mp4`

---

### Step 4: Generating Character Voices (TTS)
1. Open **Microsoft Edge-TTS** (free) or **ElevenLabs**.
2. Select or customize your voice profile:
   * **Barnaby:** Expressive, slightly high-pitched, nervous, energetic.
   * **Pip:** Fast-talking, raspy, hyperactive dwarf squeak.
3. Paste the Hinglish dialogue line (e.g., *"Arey baap re! Leak kahan se aaya?!"*).
4. Download the audio file and save it to:
   * Path: `assets/sfx/VOICE_Barnaby_Shot01.wav`

---

### Step 5: Timeline Assembly & Captions in CapCut
1. Open **CapCut** (Desktop or Mobile app — completely free).
2. Click **New Project**.
3. Set the canvas aspect ratio:
   * For Shorts: Click **Ratio ──► 9:16**.
   * For Standard Episodes: Click **Ratio ──► 16:9**.
4. Drag your generated video clips (`Shot01.mp4`, `Shot02.mp4`, etc.) into the timeline in numerical order.
5. Drag your voice audio tracks beneath the corresponding clips and line them up with mouth movements.
6. **Apply the 1.5s Comedy Freeze:**
   * On the reaction shot (e.g. Barnaby staring with pin-prick pupils), use the **Freeze Frame** tool in CapCut to hold the frame still for exactly 1.5 seconds before the bubble bursts.
7. Add subtle background jazz music (set volume to -18dB so voice is clearly audible).
8. Click **Text ──► Auto-Captions ──► Create**:
   * CapCut will automatically transcribe the voice lines into animated captions.
   * Choose a vibrant cartoon preset (yellow fill with bold black stroke).
9. Click **Export** at 1080p / 24fps:
   * Path: `output/SH-01_Cheek_Panic.mp4`

---

## 5. AI TOOLS DIRECTORY (FREE VS. PAID)

| Production Stage | Free / Budget Option | Paid / Professional Option | Notes |
|:---|:---|:---|:---|
| **1. Brainstorm & Prompts** | **Gemini (Free) / DeepSeek V3** | **Claude 3.7 Sonnet / ChatGPT Plus** | Free models work great when fed `bible/` files. |
| **2. Keyframe Images** | **Flux.1 Schnell / Leonardo.ai (Daily Free Credits)** | **Midjourney v6.1 / Flux.1 Pro** | Always specify `--ar 16:9` or `--ar 9:16`. |
| **3. Video Animation** | **Kling AI (Daily Free Credits) / Hailuo AI (Minimax Free)** | **Runway Gen-3 Alpha / Kling Pro / Luma Dream Machine** | Always use **Image-to-Video** mode for consistency. |
| **4. Voiceover (TTS)** | **Microsoft Edge-TTS (100% Free via Python/Web)** | **ElevenLabs (Starter/Creator Plan)** | ElevenLabs gives the highest emotional range. |
| **5. Video Editing** | **CapCut (Desktop/Mobile - Free) / DaVinci Resolve (Free)** | **DaVinci Resolve Studio / Premiere Pro** | CapCut has the best free one-click auto-captions. |
| **6. Sound Effects (SFX)** | **Freesound.org / Pixabay Audio (Royalty-Free)** | **Epidemic Sound / Artlist** | Search: "cartoon squeak", "slide whistle", "splash". |

---

## 6. PRE-UPLOAD QUALITY CHECKLIST

Before uploading to YouTube, verify this 6-point checklist:

- [ ] **Visual Consistency:** Does Barnaby have his red twist-tie bowtie and correct fur pattern in every shot?
- [ ] **Pacing Check:** Is there any clip longer than 6 seconds without a camera cut or comedic action?
- [ ] **The 1.5s Rule:** Did you include the deadpan freeze reaction before the catastrophe?
- [ ] **Mute Test:** Can a viewer understand the comedy with sound turned OFF?
- [ ] **Aspect Ratio:** Is it strictly 9:16 vertical (Shorts) or 16:9 horizontal (Standard Episode)?
- [ ] **Loop Test (Shorts only):** Does the last frame transition smoothly back into the opening hook?

---
*Created for WildNest Studio. Governed by [bible/style-guide.md](bible/style-guide.md) and [bible/story-framework.md](bible/story-framework.md).*
