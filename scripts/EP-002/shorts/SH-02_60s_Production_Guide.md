# SH-02 Step-by-Step Production Guide (60s)

> **Project:** Critter Haven Resort — SH-02 "The King's Arrival" (60s Cut)
> **Source Script:** [SH-02_60s_Kings_Arrival_Cut.md](SH-02_60s_Kings_Arrival_Cut.md)
> **Format:** YouTube Short (9:16 Vertical)
> **Duration:** Exactly 60 Seconds (10 Fast-Paced Clips)
> **Target Output:** `output/SH-02_60s_Kings_Arrival.mp4`

Follow these 4 exact steps to generate and assemble this 60-second Short manually:

---

## 🛠️ RECOMMENDED FREE TOOLS TO OPEN

1. **AI Image Tool:** [Leonardo.ai](https://leonardo.ai/) (150 free daily credits) OR [Tensor.art / Flux](https://tensor.art/)
2. **AI Video Tool:** [Kling AI](https://klingai.com/) (Daily free credits) OR [Hailuo AI / Minimax](https://hailuoai.video/)
3. **AI Voice Tool:** [ElevenLabs](https://elevenlabs.io/) (Free tier) OR Microsoft Edge-TTS
4. **Video Editor:** [CapCut](https://www.capcut.com/) (Free desktop / mobile app with animated auto-captions)

---

## STEP 1: GENERATE THE 10 KEYFRAME IMAGES (Text-to-Image)

* **Where to go:** Open **Leonardo.ai** ──► Click **Image Generation**.
* **Canvas Setting:** Look at the left sidebar ──► Set **Aspect Ratio** to **`9:16` (Portrait)**.
* **Model:** Select **Leonardo Phoenix** or **Anime/3D Animation style**.

Copy and generate each prompt from [SH-02_60s_Kings_Arrival_Cut.md](SH-02_60s_Kings_Arrival_Cut.md):

1. **Shot 1 (Royal Reservation):** `3D Pixar animation style, vertical 9:16, cute chubby golden Syrian hamster in red twist-tie bowtie at miniature tea saucer reception desk, holding postage stamp clipboard with wide terrified eyes, warm 8AM morning sunlight --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot01_Keyframe.png`
2. **Shot 2 (Leo Tube Arrival):** `3D Pixar animation style, vertical 9:16, low-angle, fluffy dramatic African lion cub bursting out of colorful plastic tube hatch in shower of golden glitter, gold-foil candy crown tilted, one paw dramatically extended forward --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot02_Keyframe.png`
3. **Shot 3 (Cotton Ball Inspection):** `3D Pixar animation style, vertical 9:16, large fluffy lion cub holding a single tiny white cotton ball between two precise claws, staring with magnificent theatrical disbelief at a tiny nervous golden hamster in red bowtie inside cardboard shoebox --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot03_Keyframe.png`
4. **Shot 4 (Bed Collapse):** `3D Pixar animation style, vertical 9:16, hilarious side-view of dramatic lion cub with gold-foil crown sitting completely flat on floor surrounded by collapsed cardboard wreckage, paw raised to forehead in theatrical despair, Barnaby open-mouthed nearby --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot04_Keyframe.png`
5. **Shot 5 (Barnaby Panic Sprint):** `3D Pixar animation style, vertical 9:16, low-angle of chubby golden hamster in red bowtie sprinting at panic-blur speed through colorful plastic tube, legs motion-blurred, ears flat, mouth open wide mid-shout --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot05_Keyframe.png`
6. **Shot 6 (Rocco Cotton Tower):** `3D Pixar animation style, vertical 9:16, massive white rhinoceros calf balancing enormous wobbling tower of 50 white cotton balls on his golden horn, tongue out in concentration, tip-toeing forward, two small hamsters watching nervously --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot06_Keyframe.png`
7. **Shot 7 (Cotton Blizzard):** `3D Pixar animation style, vertical 9:16, rhino calf mid-trip launching 50 cotton balls in explosive slow-motion blizzard filling entire room, hamsters frozen in shock, only a gold-foil crown poking out of cotton pile --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot07_Keyframe.png`
8. **Shot 8 (1.5s Freeze + Crown Landing):** `3D Pixar animation style, vertical 9:16, deadpan close-up of cotton-coated golden hamster with pin-prick pupils staring directly at camera in frozen shock, behind him lion cub's crown pokes from cotton pile with one eye open --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot08_Keyframe.png`
9. **Shot 9 (Leo Sinks In + Sincerity):** `3D Pixar animation style, vertical 9:16, warm two-shot, large fluffy lion cub sinking into magnificent towering cotton mountain royal bed, one eye open looking gently at small golden hamster beside him, soft golden afternoon light --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot09_Keyframe.png`
10. **Shot 10 (Human Pats + Barnaby Smirk):** `3D Pixar animation style, vertical 9:16, smug fluffy lion cub in cotton mountain nest being gently patted by large human hand, eyes peacefully closed, gold-foil crown tilted in satisfaction, warm cozy evening glow --ar 9:16` ──► Save as `assets/characters/SH02_EP002_Shot10_Keyframe.png`

---

## STEP 2: ANIMATE THE 10 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com/)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip (Kling automatically matches 9:16).

For each shot:
1. Upload the corresponding keyframe image (`SH02_EP002_Shot01_Keyframe.png` to `Shot10`).
2. Copy the **AI Video Prompt** from [SH-02_60s_Kings_Arrival_Cut.md](SH-02_60s_Kings_Arrival_Cut.md).
3. Click **Generate** ──► Download video clip as `assets/SH02_EP002_Shot01_Clip.mp4` through `Shot10`.

> **Key Shot Notes:**
> - **Shot 7 (Cotton Blizzard):** Try Kling's slow-motion setting for maximum dramatic impact.
> - **Shot 8 (1.5s Freeze):** Generate normally — the freeze is applied manually in CapCut Step 4.
> - **Shot 9 (Sincerity):** Use Kling's "subtle motion" or lowest intensity setting to keep the moment tender.

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io/)**.
* **Voice Profiles:**
  * **Barnaby:** Anxious, slightly high-pitched, formal pompous tenor.
  * **Leo:** Deep theatrical booming bass, shifts to quieter cub register for emotional lines.

Generate these dialogue lines:
* **Line 1 (Barnaby - Shot 1):** *"Leo — 100 feather bed chahiye?!"* ──► `assets/sfx/VOICE_Barnaby_SH02_EP002_L01.mp3`
* **Line 2 (Leo - Shot 2):** *"Hmph. Show me my royal chambers."* ──► `assets/sfx/VOICE_Leo_SH02_EP002_L02.mp3`
* **Line 3 (Leo - Shot 3):** *"Ek... cotton ball?"* (Horrified whisper) ──► `assets/sfx/VOICE_Leo_SH02_EP002_L03.mp3`
* **Line 4 (Barnaby - Shot 5):** *"Pip! Rocco! Emergency hai!"* ──► `assets/sfx/VOICE_Barnaby_SH02_EP002_L04.mp3`
* **Line 5 (Leo - Shot 9):** *"...Theek hai. Acceptable."* ──► `assets/sfx/VOICE_Leo_SH02_EP002_L05.mp3`
* **Line 6 (Human Voice - Shot 10):** *"Aww, what a cozy nest!"* ──► `assets/sfx/VOICE_Human_SH02_EP002_L06.mp3`

---

## STEP 4: COMBINE & EXPORT IN CAPCUT (Takes 3 Minutes)

1. **Create Project:** Open **CapCut** ──► Click **New Project** ──► Set **Ratio: `9:16` (Vertical)**.
2. **Timeline Layout:**
   * Drag all 10 clips (`SH02_EP002_Shot01_Clip.mp4` to `Shot10`) onto the video track.
   * Trim clips slightly so the total runtime hits exactly **60 seconds**.
   * Drag the 6 voice audio tracks underneath their respective scenes and align with mouth movements.
3. **The 1.5-Second Comedy Freeze (Shot 8):**
   * Go to Shot 8 (cotton-coated Barnaby staring deadpan at the camera).
   * Freeze the frame for **1.5 seconds** right before the cotton ball drifts down to Leo's crown.
4. **The Sincerity Beat (Shot 9):**
   * Slightly slow down Shot 9 (0.8x speed) so the quiet gratitude nod has space to land.
5. **Music & SFX Track:**
   * Add playful brass hotel jazz music at `-18dB` throughout.
   * Add SFX: Door click (Shot 1), royal glitter shimmer fanfare (Shot 2), low dramatic bass note (Shot 3), slow cardboard crunch *CRACK!* (Shot 4), rubber band snap + cotton launch *WHOOOMP* (Shot 7), soft cotton *poof* (Shot 8), bowtie adjustment *PING* (Shot 10).
6. **Auto-Captions:**
   * Click **Text** ──► **Auto-Captions** ──► Select yellow cartoon font with black stroke.
7. **Export Master Short:**
   * Resolution: `1080p` | Frame Rate: `24fps`.
   * **Save Output to:** `output/SH-02_EP002_60s_Kings_Arrival.mp4`

---

## 🚀 READY TO UPLOAD TO YOUTUBE SHORTS

* **Title:** When your VIP guest ruins everything before 5 PM 👑🦁 #Shorts #Animation
* **Description:** Leo the lion cub checked into Critter Haven Resort expecting a 100-feather royal bed. Barnaby gave him a cardboard box. What followed was a cotton ball blizzard. Watch till the end 😂
* **Hashtags:** `#Animation #3DAnimation #PixarStyle #CuteAnimals #Cartoons #SlapstickComedy #Hinglish`
* **Pinned Comment:** *"Which one are you: Dramatic Leo or Panicking Barnaby? 👇"*
