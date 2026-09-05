# SH-02 Step-by-Step Production Guide (60s)

> **Project:** Critter Haven Resort — SH-02 "The Button Maniac" (60s Cut)
> **Source Script:** [SH-02_60s_Button_Maniac_Cut.md](SH-02_60s_Button_Maniac_Cut.md)
> **Format:** YouTube Short (9:16 Vertical)
> **Duration:** Exactly 60 Seconds (10 Fast-Paced Clips)
> **Target Output:** `output/SH-02_60s_Button_Maniac.mp4`

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

Copy and generate each prompt from [SH-02_60s_Button_Maniac_Cut.md](SH-02_60s_Button_Maniac_Cut.md):

1. **Shot 1 (Button Spam):** `3D Pixar animation style, vertical 9:16, small squirrel monkey pressing shiny button on tube hatch with both hands, grinning with massive eyes. Golden hamster in red bowtie flinching in background, bright lobby lighting --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot01_Keyframe.png`
2. **Shot 2 (Red Button Warning):** `3D Pixar animation style, vertical 9:16, hamster pointing at red buttons while monkey nods innocently, monkey's tail coiled around red lever behind his back, gym with wheels and pulleys --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot02_Keyframe.png`
3. **Shot 3 (Belt Snap + Blender):** `3D Pixar animation style, vertical 9:16, hamster wheel spinning extreme speed, rubber-band belt snapping, fruit blender spraying mango pulp, panda chef in doorway splattered, chaotic lighting --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot03_Keyframe.png`
4. **Shot 4 (3 Wheels at Max):** `3D Pixar animation style, vertical 9:16, high angle, three wheels spinning dangerously, rubber bands sparking, monkey pressing buttons gleefully, hamster sprinting in panic, emergency orange glow --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot04_Keyframe.png`
5. **Shot 5 (Pip vs Milo):** `3D Pixar animation style, vertical 9:16, tiny dwarf hamster snipping rubber band, squirrel monkey pressing restart button, wheel between them, speed lines, emergency lighting --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot05_Keyframe.png`
6. **Shot 6 (Tarzan Swing):** `3D Pixar animation style, vertical 9:16, monkey swinging from rubber band across gym ceiling Tarzan-style pressing ceiling button mid-swing, tiny hamster on skateboard below, colorful pulleys --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot06_Keyframe.png`
7. **Shot 7 (Pip's Freeze):** `3D Pixar animation style, vertical 9:16, deadpan close-up tiny dwarf hamster with pin-prick pupils frozen in shock, paperclip visor slid over eye, monkey swinging in background, emergency orange lighting --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot07_Keyframe.png`
8. **Shot 8 (Rubber Band Lure):** `3D Pixar animation style, vertical 9:16, hamster holding gleaming yellow rubber band, mesmerized monkey reaching with dilated pupils, tiny hamster pulling emergency lever in background, golden light --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot08_Keyframe.png`
9. **Shot 9 (Sincerity Beat):** `3D Pixar animation style, vertical 9:16, warm floor-level two-shot, hamster kneeling to tie yellow rubber band around sad monkey's wrist, broken machinery background, golden afternoon light --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot09_Keyframe.png`
10. **Shot 10 (TV Remote):** `3D Pixar animation style, vertical 9:16, squirrel monkey staring at TV remote with enormous dilated pupils and mischievous grin, hamster peeking from hut with one horrified eye, warm evening glow --ar 9:16` ──► Save as `assets/characters/SH02_EP003_Shot10_Keyframe.png`

---

## STEP 2: ANIMATE THE 10 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com/)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip (Kling automatically matches 9:16).

For each shot:
1. Upload the corresponding keyframe image (`SH02_EP003_Shot01_Keyframe.png` to `Shot10`).
2. Copy the **AI Video Prompt** from [SH-02_60s_Button_Maniac_Cut.md](SH-02_60s_Button_Maniac_Cut.md).
3. Click **Generate** ──► Download video clip as `assets/SH02_EP003_Shot01_Clip.mp4` through `Shot10`.

> **Key Shot Notes:**
> - **Shot 6 (Tarzan Swing):** Use highest dynamism setting for wild swing motion.
> - **Shot 7 (Pip's 1.5s Freeze):** Generate normally — the actual freeze is applied in CapCut.
> - **Shot 9 (Sincerity):** Use lowest motion/subtlest setting. Let the beat breathe.
> - **Shot 10 (TV Remote):** Slow creeping tension. The pupil dilation and finger twitch are the key.

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io/)**.
* **Voice Profiles:**
  * **Barnaby:** High-pitched, shifts from relaxed to panicked to horrified whisper.
  * **Milo:** Fast chirpy monkey chatter, short excited bursts.
  * **Pip:** Fast raspy energetic squeak.
  * **Bao:** Deep warm devastated bass (one line only).

Generate these dialogue lines:
* **Line 1 (Barnaby - Shot 1):** *"Easy hai, aaj."* ──► `assets/sfx/VOICE_Barnaby_SH02_EP003_L01.mp3`
* **Line 2 (Milo - Shot 1):** *"Ooh! Button!"* ──► `assets/sfx/VOICE_Milo_SH02_EP003_L02.mp3`
* **Line 3 (Barnaby - Shot 2):** *"Red buttons mat dabao!"* ──► `assets/sfx/VOICE_Barnaby_SH02_EP003_L03.mp3`
* **Line 4 (Milo - Shot 2):** *"Promise!"* ──► `assets/sfx/VOICE_Milo_SH02_EP003_L04.mp3`
* **Line 5 (Bao - Shot 3):** *"Mera blender!"* ──► `assets/sfx/VOICE_Bao_SH02_EP003_L05.mp3`
* **Line 6 (Barnaby - Shot 4):** *"PIP! Sab band karo!"* ──► `assets/sfx/VOICE_Barnaby_SH02_EP003_L06.mp3`
* **Line 7 (Pip - Shot 5):** *"Ye banda rukta hi nahi!"* ──► `assets/sfx/VOICE_Pip_SH02_EP003_L07.mp3`
* **Line 8 (Barnaby - Shot 10):** *"Milo... nahin..."* (Horrified whisper) ──► `assets/sfx/VOICE_Barnaby_SH02_EP003_L08.mp3`

---

## STEP 4: COMBINE & EXPORT IN CAPCUT (Takes 3 Minutes)

1. **Create Project:** Open **CapCut** ──► Click **New Project** ──► Set **Ratio: `9:16` (Vertical)**.
2. **Timeline Layout:**
   * Drag all 10 clips (`SH02_EP003_Shot01_Clip.mp4` to `Shot10`) onto the video track.
   * Trim clips so the total runtime hits exactly **60 seconds**.
   * Drag the 8 voice audio tracks underneath their respective scenes and align with mouth movements.
3. **The 7-Button SFX Rhythm (Shot 1):**
   * Add 7 unique escalating cartoon SFX (BEEP → BOOP → BONK → DING → HONK → SQUEAK → FOGHORN) over 3 seconds.
4. **Pip's 1.5-Second Comedy Freeze (Shot 7):**
   * Go to Shot 7 (Pip frozen, staring at camera).
   * Freeze the frame for **1.5 seconds** at the peak of his deadpan stare.
   * **IMPORTANT:** Kill ALL music and sound during this 1.5s. Total silence. This is the series' first running-gag subversion — let it land.
5. **The TV Remote Cliffhanger (Shot 10):**
   * After the final frame, hold a BLACK SCREEN for 2 seconds.
   * Add exactly **one single TV remote CLICK** SFX in the darkness.
   * End.
6. **Music & SFX Track:**
   * Upbeat gym/jazz music at `-18dB` throughout Shots 1–6.
   * Kill music completely for Pip's freeze (Shot 7).
   * Warm music for sincerity beat (Shot 9).
   * Low tension drone for TV remote shot (Shot 10).
   * Key SFX: 7 button sounds (Shot 1), rubber band SNAP (Shot 3), blender splatter (Shot 3), sparking crackle (Shot 4), Tarzan *ooh-ooh* (Shot 6), emergency lever CLUNK (Shot 8), single TV CLICK (Shot 10).
7. **Auto-Captions:**
   * Click **Text** ──► **Auto-Captions** ──► Select yellow cartoon font with black stroke.
8. **Export Master Short:**
   * Resolution: `1080p` | Frame Rate: `24fps`.
   * **Save Output to:** `output/SH-02_EP003_60s_Button_Maniac.mp4`

---

## 🚀 READY TO UPLOAD TO YOUTUBE SHORTS

* **Title:** When the monkey presses EVERY button in your resort 🐒💥 #Shorts #Animation
* **Description:** Milo has zero impulse control and Barnaby's gym is full of shiny buttons. What could go wrong? Everything. Everything goes wrong. Watch till the end for the TV remote twist 😂
* **Hashtags:** `#Animation #3DAnimation #PixarStyle #CuteAnimals #Cartoons #SlapstickComedy #Hinglish #ButtonManiac`
* **Pinned Comment:** *"Milo is the reason the resort needs insurance 💀🐒 Who else would press the red button?"*
