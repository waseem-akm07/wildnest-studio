# SH-01 Step-by-Step Production Guide

> **Project:** Critter Haven Resort — SH-01 "Barnaby's Water Leak Panic"  
> **Source Script:** [SH-01_Cheek_Panic.md](SH-01_Cheek_Panic.md)  
> **Format:** YouTube Short (9:16 Vertical)  
> **Duration:** 15 Seconds (3 Video Clips)  
> **Target Output:** `output/SH-01_Cheek_Panic.mp4`

Follow these 4 exact steps to generate and assemble this Short manually:

---

## 🛠️ RECOMMENDED FREE TOOLS TO OPEN

1. **AI Image Tool:** [Leonardo.ai](https://leonardo.ai) (150 free daily credits) OR [Tensor.art / Flux](https://tensor.art)
2. **AI Video Tool:** [Kling AI](https://klingai.com) (Daily free credits) OR [Hailuo AI / Minimax](https://hailuoai.video/)
3. **AI Voice Tool:** [ElevenLabs](https://elevenlabs.io) (Free tier) OR Microsoft Edge-TTS
4. **Video Editor:** [CapCut](https://www.capcut.com) (Free desktop / mobile app with animated auto-captions)

---

## STEP 1: GENERATE THE 3 KEYFRAME IMAGES (Text-to-Image)

* **Where to go:** Open **Leonardo.ai** ──► Click **Image Generation**.
* **Canvas Setting:** Look at the left sidebar ──► Set **Aspect Ratio** to **`9:16` (Portrait)**.
* **Model:** Select **Leonardo Phoenix** or **Anime/3D Animation style**.

### 📸 Shot 1 Image
* **Copy & Paste Prompt:**
  ```text
  3D Pixar animation style, vertical 9:16 aspect ratio, a cute chubby golden Syrian hamster wearing a tiny red twist-tie bowtie inside a vertical colorful plastic hamster tube. A sudden burst of crystal clear splashing water sprays from a pipe joint above, dynamic water droplets in mid-air, bright cinematic lighting, volumetric light, 8k resolution --ar 9:16
  ```
* **Action:** Click **Generate** ──► Download the best render.
* **Save to:** `assets/characters/SH01_Shot01_Keyframe.png`

---

### 📸 Shot 2 Image
* **Copy & Paste Prompt:**
  ```text
  3D Pixar animation style, vertical 9:16 close-up of a golden hamster with absurdly gigantic swollen cheek pouches, 3 times normal head size, holding a miniature sponge. Bulging shiny metal thimbles visible inside stretched cheeks, hilarious wide-eyed panic, dripping spiky fur --ar 9:16
  ```
* **Action:** Click **Generate** ──► Download the best render.
* **Save to:** `assets/characters/SH01_Shot02_Keyframe.png`

---

### 📸 Shot 3 Image
* **Copy & Paste Prompt:**
  ```text
  3D Pixar animation style, vertical 9:16 framing, hilarious deadpan expression on a drenched golden hamster with spiky wet fur and pin-prick pupils staring directly into camera. A giant clear spherical water bubble floats directly over his head, dramatic studio rim lighting, 8k --ar 9:16
  ```
* **Action:** Click **Generate** ──► Download the best render.
* **Save to:** `assets/characters/SH01_Shot03_Keyframe.png`

---

## STEP 2: ANIMATE THE 3 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip.

### 🎬 Shot 1 Video Clip
1. **Upload Image:** Select `assets/characters/SH01_Shot01_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   3D animated vertical clip, hamster proudly adjusts his red bowtie, suddenly startled as a spray of water shoots from above directly onto his face, flailing his tiny pink paws in funny surprise. Smooth 24fps motion, vertical framing.
   ```
3. **Action:** Click **Generate** ──► Download video clip.
4. **Save to:** `assets/SH01_Shot01_Clip.mp4`

---

### 🎬 Shot 2 Video Clip
1. **Upload Image:** Select `assets/characters/SH01_Shot02_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   3D animated vertical clip, close-up of hamster frantically stuffing tiny objects into his cheeks, his cheek pouches expanding rapidly to 3x normal size, wobbling as he tries to speak with muffled squeaks. High-energy comedy physics, 24fps.
   ```
3. **Action:** Click **Generate** ──► Download video clip.
4. **Save to:** `assets/SH01_Shot02_Clip.mp4`

---

### 🎬 Shot 3 Video Clip
1. **Upload Image:** Select `assets/characters/SH01_Shot03_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   3D animated vertical clip, drenched hamster freezes completely still for 1.5 seconds staring into the camera with tiny pupils, completely unmoving. Then a water bubble above his head pops, splashing his face as he slides downward out of frame. 24fps.
   ```
3. **Action:** Click **Generate** ──► Download video clip.
4. **Save to:** `assets/SH01_Shot03_Clip.mp4`

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io)** (or Microsoft Edge-TTS).
* **Voice Selection:** Pick an expressive, fast, animated voice (e.g. "Adam", "Fin", or "Leo").

### 🎙️ Voice Line 1 (Barnaby - Shot 1)
* **Text to Speak:** *"Arey baap re! Leak kahan se aaya?!"*
* **Tone:** Sudden panic & frantic.
* **Download and Save to:** `assets/sfx/VOICE_Barnaby_SH01_L01.mp3`

---

### 🎙️ Voice Line 2 (Barnaby - Shot 2)
* **Text to Speak:** *"Mmmph! Sambhal loonga... maybe!"*
* **Tone:** Muffled, squeaky, struggling to talk through stuffed cheeks.
* **Download and Save to:** `assets/sfx/VOICE_Barnaby_SH01_L02.mp3`

---

## STEP 4: COMBINE & EXPORT IN CAPCUT (Takes 3 Minutes)

1. **Create Project:**
   * Open **CapCut** (Desktop or Mobile app).
   * Click **New Project**.
   * Click **Ratio** below preview window ──► Select **`9:16`**.
2. **Add Video Clips:**
   * Drag `SH01_Shot01_Clip.mp4`, `SH01_Shot02_Clip.mp4`, and `SH01_Shot03_Clip.mp4` onto the timeline in order.
3. **Add Voice Audio:**
   * Drag `VOICE_Barnaby_SH01_L01.mp3` under Shot 1.
   * Drag `VOICE_Barnaby_SH01_L02.mp3` under Shot 2.
   * Align them with Barnaby's mouth movement.
4. **Apply Comedy Timing (The 1.5s Freeze):**
   * Go to Shot 3 where Barnaby has spiky hair and is staring at the camera.
   * Cut or split the clip, select the frame where he stares, and click **Freeze Frame** to hold it for **1.5 seconds** right before the bubble bursts!
5. **Add Sound Effects & Music (Optional but Recommended):**
   * Add a cartoon splash SFX when the bubble bursts.
   * Add upbeat playful jazz background music at volume `-18dB`.
6. **Generate Animated Auto-Captions:**
   * Click **Text** ──► **Auto-Captions** ──► **Create**.
   * Choose a cartoon text style: **Yellow font with black outline**.
7. **Export Final Video:**
   * Click **Export** ──► Resolution: `1080p` | Frame Rate: `24fps`.
   * **Save File to:** `output/SH-01_Cheek_Panic.mp4`

---

## 🚀 READY TO UPLOAD TO YOUTUBE SHORTS

* **Title:** When you try to fix plumbing yourself 💀🐹 #Shorts #Animation
* **Description:** Barnaby thought he could stop a water leak with his cheeks... it did not end well. Welcome to Critter Haven Resort!
* **Hashtags:** `#Animation #3DAnimation #PixarStyle #CuteHamster #FunnyCartoons #Slapstick`
