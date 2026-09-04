# SH-[XX] Step-by-Step Production Guide

> **Project:** Critter Haven Resort — SH-[XX] "[Short Title]"  
> **Source Script:** [SH-[XX]_[Title].md](SH-[XX]_[Title].md)  
> **Format:** YouTube Short (9:16 Vertical)  
> **Duration:** [15s / 30s / 60s] ([X] Video Clips)  
> **Target Output:** `output/SH-[XX]_[Title].mp4`

Follow these 4 exact steps to generate and assemble this Short manually:

---

## 🛠️ RECOMMENDED FREE TOOLS TO OPEN

1. **AI Image Tool:** [Leonardo.ai](https://leonardo.ai) (150 free daily credits) OR [Tensor.art / Flux](https://tensor.art)
2. **AI Video Tool:** [Kling AI](https://klingai.com) (Daily free credits) OR [Hailuo AI / Minimax](https://hailuoai.video/)
3. **AI Voice Tool:** [ElevenLabs](https://elevenlabs.io) (Free tier) OR Microsoft Edge-TTS
4. **Video Editor:** [CapCut](https://www.capcut.com) (Free desktop / mobile app with animated auto-captions)

---

## STEP 1: GENERATE THE KEYFRAME IMAGES (Text-to-Image)

* **Where to go:** Open **Leonardo.ai** ──► Click **Image Generation**.
* **Canvas Setting:** Set **Aspect Ratio** to **`9:16` (Portrait)**.
* **Model:** Select **Leonardo Phoenix** or **Anime/3D Animation style**.

### 📸 Shot 1 Image
* **Copy & Paste Prompt:**
  ```text
  [Paste Image Prompt from Short script] --ar 9:16
  ```
* **Save to:** `assets/characters/SH[XX]_Shot01_Keyframe.png`

*(Repeat for each shot)*

---

## STEP 2: ANIMATE THE VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip.

### 🎬 Shot 1 Video Clip
1. **Upload Image:** Select `assets/characters/SH[XX]_Shot01_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   [Paste Video Motion Prompt from Short script], 24fps.
   ```
3. **Save to:** `assets/SH[XX]_Shot01_Clip.mp4`

*(Repeat for each shot)*

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io)**.
* **Voice Selection:** Select character voice profile.

### 🎙️ Voice Line 1 ([Character] - Shot 1)
* **Text to Speak:** *"[Hinglish Dialogue Line]"*
* **Save to:** `assets/sfx/VOICE_[Char]_SH[XX]_L01.mp3`

---

## STEP 4: COMBINE & EXPORT IN CAPCUT

1. **Create Project:** Open **CapCut** ──► Click **New Project** ──► Set **Ratio: 9:16**.
2. **Add Video Clips:** Drag clips onto timeline in numerical order (`Shot01`, `Shot02`, ...).
3. **Add Voice Audio:** Align voice lines with character mouth movement.
4. **Apply Comedy Timing:** Add a **Freeze Frame** for **1.5 seconds** on the reaction face hold before the slapstick payoff.
5. **Add Sound Effects & Music:** Add cartoon SFX and background music at `-18dB`.
6. **Generate Animated Auto-Captions:** Click **Text** ──► **Auto-Captions** ──► Choose Yellow Cartoon style.
7. **Export Final Video:** Resolution `1080p` | `24fps` ──► Save to `output/SH-[XX]_[Title].mp4`.
