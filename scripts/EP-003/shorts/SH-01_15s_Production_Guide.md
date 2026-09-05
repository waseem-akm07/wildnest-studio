# SH-01 Step-by-Step Production Guide (15s)

> **Project:** Critter Haven Resort — SH-01 "Button Spam Arrival"
> **Source Script:** [SH-01_15s_Button_Spam.md](SH-01_15s_Button_Spam.md)
> **Format:** YouTube Short (9:16 Vertical)
> **Duration:** 15 Seconds (3 Video Clips)
> **Target Output:** `output/SH-01_15s_Button_Spam.mp4`

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
  3D Pixar animation style, vertical 9:16, a cute chubby golden Syrian hamster in a red twist-tie bowtie standing behind a miniature tea saucer desk, casually shrugging with a relaxed confident grin while reading a tiny clipboard. Warm 8AM morning sunlight, soft cozy cage background, 8k --ar 9:16
  ```
* **Action:** Click **Generate** ──► Download the best render.
* **Save to:** `assets/characters/SH01_EP003_Shot01_Keyframe.png`

---

### 📸 Shot 2 Image
* **Copy & Paste Prompt:**
  ```text
  3D Pixar animation style, vertical 9:16, a small energetic squirrel monkey with cinnamon-brown fur and a golden chest patch pressing a large shiny button on a colorful plastic tube hatch with both tiny hands, mouth open in a wide excited grin, massive dilated eyes. A chubby golden hamster in a red bowtie flinches in the background. Bright vibrant lighting --ar 9:16
  ```
* **Action:** Click **Generate** ──► Download the best render.
* **Save to:** `assets/characters/SH01_EP003_Shot02_Keyframe.png`

---

### 📸 Shot 3 Image
* **Copy & Paste Prompt:**
  ```text
  3D Pixar animation style, vertical 9:16, extreme close-up of a golden hamster's face with wide terrified eyes, his tiny red twist-tie bowtie vibrating in a blur of motion. Behind him in soft focus, a squirrel monkey reaches toward another button with outstretched fingers. Bright lobby lighting, 8k --ar 9:16
  ```
* **Action:** Click **Generate** ──► Download the best render.
* **Save to:** `assets/characters/SH01_EP003_Shot03_Keyframe.png`

---

## STEP 2: ANIMATE THE 3 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip.

### 🎬 Shot 1 Video Clip
1. **Upload Image:** Select `assets/characters/SH01_EP003_Shot01_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   3D animated vertical clip, chubby hamster casually reads a tiny clipboard, shrugs with a relaxed smile, and nods confidently. Smooth calm 24fps motion, warm morning lighting, vertical framing.
   ```
3. **Action:** Click **Generate** ──► Download video clip.
4. **Save to:** `assets/SH01_EP003_Shot01_Clip.mp4`

---

### 🎬 Shot 2 Video Clip
1. **Upload Image:** Select `assets/characters/SH01_EP003_Shot02_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   3D animated vertical clip, a monkey rapidly presses a shiny button 7 times in quick succession, bouncing with glee after each press. Behind him, a hamster flinches progressively harder, his bowtie vibrating by the last press. Fast comedic rhythm, 24fps, vertical framing.
   ```
3. **Action:** Click **Generate** ──► Download video clip.
4. **Save to:** `assets/SH01_EP003_Shot02_Clip.mp4`

---

### 🎬 Shot 3 Video Clip
1. **Upload Image:** Select `assets/characters/SH01_EP003_Shot03_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   3D animated vertical clip, close-up of a terrified hamster staring at camera, his red bowtie vibrating rapidly. His left eye twitches. In the soft background, a monkey reaches for another button. Holds for 2 seconds then abrupt cut to black. 24fps.
   ```
3. **Action:** Click **Generate** ──► Download video clip.
4. **Save to:** `assets/SH01_EP003_Shot03_Clip.mp4`

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io)** (or Microsoft Edge-TTS).
* **Voice Profiles:**
  * **Barnaby:** Relaxed, confident tone shifting to terror.
  * **Milo:** Fast, chirpy, ecstatic monkey chatter.

### 🎙️ Voice Line 1 (Barnaby - Shot 1)
* **Text to Speak:** *"Gym pass. Easy hai, aaj."*
* **Tone:** Casual, relaxed, confident — he thinks today will be easy.
* **Download and Save to:** `assets/sfx/VOICE_Barnaby_SH01_EP003_L01.mp3`

---

### 🎙️ Voice Line 2 (Milo - Shot 2)
* **Text to Speak:** *"Ooh! Button! Ek aur!"*
* **Tone:** Ecstatic, hyper-fast, barely able to contain excitement.
* **Download and Save to:** `assets/sfx/VOICE_Milo_SH01_EP003_L02.mp3`

---

## STEP 4: COMBINE & EXPORT IN CAPCUT (Takes 3 Minutes)

1. **Create Project:**
   * Open **CapCut** (Desktop or Mobile app).
   * Click **New Project**.
   * Click **Ratio** below preview window ──► Select **`9:16`**.
2. **Add Video Clips:**
   * Drag `SH01_EP003_Shot01_Clip.mp4`, `SH01_EP003_Shot02_Clip.mp4`, and `SH01_EP003_Shot03_Clip.mp4` onto the timeline in order.
3. **Add Voice Audio:**
   * Drag `VOICE_Barnaby_SH01_EP003_L01.mp3` under Shot 1.
   * Drag `VOICE_Milo_SH01_EP003_L02.mp3` under Shot 2.
   * Align them with character mouth movements.
4. **Add 7 Button Sound Effects (Shot 2):**
   * This is the KEY moment. Add 7 unique escalating cartoon SFX:
   * BEEP → BOOP → BONK → DING → HONK → SQUEAK → FOGHORN
   * Space them across 3 seconds for rhythmic comic impact.
5. **Add Music & Final SFX:**
   * Add upbeat hotel jazz music at `-18dB` for Shot 1.
   * Add a tiny bowtie vibration *bzzz* SFX in Shot 3.
   * Cut all music at the final black screen.
6. **Generate Animated Auto-Captions:**
   * Click **Text** ──► **Auto-Captions** ──► **Create**.
   * Choose a cartoon text style: **Yellow font with black outline**.
7. **Export Final Video:**
   * Click **Export** ──► Resolution: `1080p` | Frame Rate: `24fps`.
   * **Save File to:** `output/SH-01_EP003_Button_Spam.mp4`

---

## 🚀 READY TO UPLOAD TO YOUTUBE SHORTS

* **Title:** When the guest starts pressing ALL the buttons 💀🐒 #Shorts #Animation
* **Description:** Milo the monkey hasn't even checked in yet and he's already broken 7 things. Barnaby was NOT ready for this guest. Welcome to Critter Haven Resort!
* **Hashtags:** `#Animation #3DAnimation #PixarStyle #CuteMonkey #FunnyCartoons #SlapstickComedy #Hinglish`
* **Pinned Comment:** *"Milo is that one friend who touches EVERYTHING in your house 💀"*
