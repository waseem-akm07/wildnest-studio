# SH-01 Step-by-Step Production Guide (15s)

> **Project:** Critter Haven Resort — SH-01 "The King's Collapsing Bed"
> **Source Script:** [SH-01_15s_Collapsing_Bed.md](SH-01_15s_Collapsing_Bed.md)
> **Format:** YouTube Short (9:16 Vertical)
> **Duration:** 15 Seconds (3 Video Clips)
> **Target Output:** `output/SH-01_15s_Collapsing_Bed.mp4`

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
  3D Pixar animation style, vertical 9:16, medium two-shot inside a tiny cardboard shoebox hotel suite. A large fluffy African lion cub with a gold-foil candy wrapper crown holds a single tiny white cotton ball between two claws, staring with spectacular theatrical disbelief at a tiny nervous golden hamster in a red bowtie. Thimble lamp glowing in background, warm cozy lighting --ar 9:16
  ```
* **Action:** Click **Generate** ──► Download the best render.
* **Save to:** `assets/characters/SH01_EP002_Shot01_Keyframe.png`

---

### 📸 Shot 2 Image
* **Copy & Paste Prompt:**
  ```text
  3D Pixar animation style, vertical 9:16, hilarious side-view of a dramatic fluffy lion cub with a gold-foil crown sitting completely flat on the floor surrounded by collapsed cardboard shoebox wreckage. Royal pose maintained despite total disaster, wide shocked eyes, golden warm closet lighting --ar 9:16
  ```
* **Action:** Click **Generate** ──► Download the best render.
* **Save to:** `assets/characters/SH01_EP002_Shot02_Keyframe.png`

---

### 📸 Shot 3 Image
* **Copy & Paste Prompt:**
  ```text
  3D Pixar animation style, vertical 9:16, wide two-shot comedy freeze frame. A large fluffy lion cub sits flat on collapsed cardboard floor with one paw dramatically raised to his forehead in theatrical royal despair. Beside him, a tiny golden hamster in a red bowtie is mid-face-palm with both tiny paws covering his face. Warm cozy closet lighting --ar 9:16
  ```
* **Action:** Click **Generate** ──► Download the best render.
* **Save to:** `assets/characters/SH01_EP002_Shot03_Keyframe.png`

---

## STEP 2: ANIMATE THE 3 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip.

### 🎬 Shot 1 Video Clip
1. **Upload Image:** Select `assets/characters/SH01_EP002_Shot01_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   3D animated vertical clip of a fluffy lion cub carefully lifting a single cotton ball with two claws from a cardboard floor and raising it to eye level. He turns to the nervous hamster beside him with one eyebrow raised in magnificent theatrical horror. Smooth 24fps, vertical framing.
   ```
3. **Action:** Click **Generate** ──► Download video clip.
4. **Save to:** `assets/SH01_EP002_Shot01_Clip.mp4`

---

### 🎬 Shot 2 Video Clip
1. **Upload Image:** Select `assets/characters/SH01_EP002_Shot02_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   3D animated vertical clip of a fluffy lion cub lowering himself onto a cardboard shoebox with slow royal ceremony. The cardboard visibly creaks and buckles until it collapses completely flat with a loud cardboard crunch. The lion ends up sitting flat on the floor, surrounded by cardboard pieces, still holding his regal pose. 24fps side-view comedy physics.
   ```
3. **Action:** Click **Generate** ──► Download video clip.
4. **Save to:** `assets/SH01_EP002_Shot02_Clip.mp4`

---

### 🎬 Shot 3 Video Clip
1. **Upload Image:** Select `assets/characters/SH01_EP002_Shot03_Keyframe.png`.
2. **Copy & Paste Motion Prompt:**
   ```text
   3D animated vertical clip, lion cub raises one paw slowly to forehead and holds it still for 1.5 seconds in total dramatic stillness. Beside him the golden hamster slowly brings both paws up to face-palm in resigned despair. Both characters frozen in perfect comedic deadpan. Ends with tiny audible squeak. 24fps.
   ```
3. **Action:** Click **Generate** ──► Download video clip.
4. **Save to:** `assets/SH01_EP002_Shot03_Clip.mp4`

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io)** (or Microsoft Edge-TTS).
* **Voice Profiles:**
  * **Leo:** Deep, theatrical, booming bass — shifts to smaller cub voice on emotional lines.
  * **Barnaby:** Anxious, formal high-pitched tenor.

### 🎙️ Voice Line 1 (Leo - Shot 1)
* **Text to Speak:** *"Ek... cotton ball?"*
* **Tone:** Horrified, deadly quiet royal whisper. Maximum disbelief in minimum volume.
* **Download and Save to:** `assets/sfx/VOICE_Leo_SH01_L01.mp3`

> *(No additional spoken dialogue needed for this Short — the physical comedy carries the whole piece.)*

---

## STEP 4: COMBINE & EXPORT IN CAPCUT (Takes 3 Minutes)

1. **Create Project:**
   * Open **CapCut** (Desktop or Mobile app).
   * Click **New Project**.
   * Click **Ratio** below preview window ──► Select **`9:16`**.
2. **Add Video Clips:**
   * Drag `SH01_EP002_Shot01_Clip.mp4`, `SH01_EP002_Shot02_Clip.mp4`, and `SH01_EP002_Shot03_Clip.mp4` onto the timeline in order.
3. **Add Voice Audio:**
   * Drag `VOICE_Leo_SH01_L01.mp3` under Shot 1 and align with Leo's mouth movement.
4. **Apply Comedy Timing (The 1.5s Freeze):**
   * Go to Shot 3 where both characters are in their frozen expressions.
   * Split the clip and click **Freeze Frame** to hold it for **1.5 seconds** at the peak of the deadpan stare.
5. **Add Sound Effects & Music:**
   * Add slow royal processional music (low volume) during Shot 1.
   * Add slow-motion cardboard crunch SFX during Shot 2.
   * Add complete silence during the 1.5s freeze in Shot 3.
   * Add a single tiny cartoon squeak right at the end.
6. **Generate Animated Auto-Captions:**
   * Click **Text** ──► **Auto-Captions** ──► **Create**.
   * Choose a cartoon text style: **Yellow font with black outline**.
7. **Export Final Video:**
   * Click **Export** ──► Resolution: `1080p` | Frame Rate: `24fps`.
   * **Save File to:** `output/SH-01_EP002_Collapsing_Bed.mp4`

---

## 🚀 READY TO UPLOAD TO YOUTUBE SHORTS

* **Title:** The 5-star bed that lasted 0.5 seconds 👑💀 #Shorts #Animation
* **Description:** Leo the lion cub demanded a royal bed. Barnaby delivered a cardboard box. The results were... not good. Welcome to Critter Haven Resort!
* **Hashtags:** `#Animation #3DAnimation #PixarStyle #CuteLion #FunnyCartoons #SlapstickComedy #Hinglish`
* **Pinned Comment:** *"Barnaby really said '1 cotton ball is enough' 💀🐹"*
