# EP-003 Step-by-Step Production Guide

> **Project:** Critter Haven Resort — EP-003 "The Button Maniac"
> **Source Script:** [script.md](script.md) | **Shot List:** [shot-list.md](shot-list.md)
> **Format:** Standard YouTube Episode (16:9 Cinematic Widescreen)
> **Duration:** ~2 minutes 30 seconds (12 Core Shots)
> **Target Master Output:** `output/EP-003_MASTER.mp4`

Follow these 4 exact steps to generate and assemble this master episode manually:

---

## 🛠️ RECOMMENDED FREE TOOLS TO OPEN

1. **AI Image Tool:** [Leonardo.ai](https://leonardo.ai/) (150 free daily credits) OR [Tensor.art / Flux](https://tensor.art/)
2. **AI Video Tool:** [Kling AI](https://klingai.com/) (Daily free credits) OR [Hailuo AI / Minimax](https://hailuoai.video/)
3. **AI Voice Tool:** [ElevenLabs](https://elevenlabs.io/) (Free tier) OR Microsoft Edge-TTS
4. **Video Editor:** [CapCut](https://www.capcut.com/) (Free desktop / mobile app) OR DaVinci Resolve (Free)

---

## STEP 1: GENERATE THE 12 KEYFRAME IMAGES (Text-to-Image)

* **Where to go:** Open **Leonardo.ai** ──► Click **Image Generation**.
* **Canvas Setting:** Look at the left sidebar ──► Set **Aspect Ratio** to **`16:9` (Landscape)**.
* **Model:** Select **Leonardo Phoenix** or **3D Animation style**.

Copy the prompts from [shot-list.md](shot-list.md) for each shot:

* **Shot 1 (Easy Reservation):** `3D Pixar animation style, cinematic 16:9, cute chubby golden Syrian hamster in red twist-tie bowtie at miniature tea saucer desk, casually shrugging with relaxed grin while reading tiny postage stamp clipboard, warm 8AM morning sunlight, 8k --ar 16:9` ──► Save as `assets/characters/EP003_Shot01_Keyframe.png`
* **Shot 2 (7-Button Spam):** `3D Pixar animation style, cinematic 16:9, small energetic squirrel monkey pressing large shiny button on plastic tube hatch with both hands, grinning with massive excited eyes, chubby hamster flinching in background, bright lobby lighting --ar 16:9` ──► Save as `assets/characters/EP003_Shot02_Keyframe.png`
* **Shot 3 (Fitness Center Reveal):** `3D Pixar animation style, cinematic 16:9, wide establishing shot of miniature gym inside hamster cage, three large colorful hamster wheels, rubber-band belts, fruit blender, wall panel of shiny red green yellow buttons, squirrel monkey staring with saucer-sized pupils --ar 16:9` ──► Save as `assets/characters/EP003_Shot03_Keyframe.png`
* **Shot 4 (Red Button Warning + Secret Tail):** `3D Pixar animation style, cinematic 16:9, comedy two-shot, hamster pointing at red buttons, monkey nodding innocently while his prehensile tail secretly wraps around a red lever behind his back --ar 16:9` ──► Save as `assets/characters/EP003_Shot04_Keyframe.png`
* **Shot 5 (Belt Snap + Blender Explosion):** `3D Pixar animation style, cinematic 16:9, hamster wheel spinning at extreme speed, rubber-band belt snapping, blender spraying fruit pulp, panda chef in doorway splattered with mango, chaotic lighting --ar 16:9` ──► Save as `assets/characters/EP003_Shot05_Keyframe.png`
* **Shot 6 (All 3 Wheels at Max):** `3D Pixar animation style, cinematic 16:9, high angle, three hamster wheels at dangerous maximum speed, smoking rubber bands sparking, monkey pressing buttons, hamster sprinting in panic, emergency orange lighting --ar 16:9` ──► Save as `assets/characters/EP003_Shot06_Keyframe.png`
* **Shot 7 (Pip vs Milo Speed Race):** `3D Pixar animation style, cinematic 16:9, fast-paced action, tiny dwarf hamster snipping rubber band while squirrel monkey presses restart button, hamster wheel between them, speed lines, emergency lighting --ar 16:9` ──► Save as `assets/characters/EP003_Shot07_Keyframe.png`
* **Shot 8 (Tarzan Swing):** `3D Pixar animation style, cinematic 16:9, dynamic sweeping shot, squirrel monkey swinging from rubber band across gym ceiling Tarzan-style pressing ceiling buttons mid-swing, tiny hamster on skateboard below looking up helplessly --ar 16:9` ──► Save as `assets/characters/EP003_Shot08_Keyframe.png`
* **Shot 9 (Pip's 1.5s Freeze):** `3D Pixar animation style, cinematic 16:9, deadpan close-up of tiny dwarf hamster mechanic with pin-prick pupils staring at camera in frozen shock, paperclip visor slid over one eye, monkey swinging past in soft-focus background, warm orange lighting --ar 16:9` ──► Save as `assets/characters/EP003_Shot09_Keyframe.png`
* **Shot 10 (Rubber Band Lure):** `3D Pixar animation style, cinematic 16:9, hamster holding up shiny yellow rubber band gleaming in golden light, mesmerized monkey reaching toward it with massive dilated pupils, tiny hamster sprinting toward emergency lever in background --ar 16:9` ──► Save as `assets/characters/EP003_Shot10_Keyframe.png`
* **Shot 11 (Sincerity Beat — Tying Rubber Band):** `3D Pixar animation style, cinematic 16:9, warm floor-level two-shot, hamster kneeling to tie yellow rubber band around sad monkey's wrist, broken machinery in background, golden afternoon light, heartfelt moment --ar 16:9` ──► Save as `assets/characters/EP003_Shot11_Keyframe.png`
* **Shot 12 (TV Remote Cliffhanger):** `3D Pixar animation style, cinematic 16:9, squirrel monkey staring at TV remote on bedside table with enormous dilated pupils and mischievous grin, hamster peeking from wooden hut with one horrified eye in background, warm evening glow --ar 16:9` ──► Save as `assets/characters/EP003_Shot12_Keyframe.png`

---

## STEP 2: ANIMATE THE 12 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com/)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip (Kling automatically matches 16:9).

For each shot:
1. Upload the corresponding keyframe image (`EP003_Shot01_Keyframe.png` to `Shot12`).
2. Copy the **AI Video Prompt** from [shot-list.md](shot-list.md).
3. Click **Generate** ──► Download video clip as `assets/EP003_Shot01_Clip.mp4` through `Shot12`.

> **Key Shots to Pay Attention To:**
> - **Shot 2 (7-Button Spam):** Fast rhythm — each press should feel snappier than the last. Consider generating 2 versions and picking the punchiest.
> - **Shot 8 (Tarzan Swing):** Use Kling's highest motion/dynamism setting. The swing needs to feel fluid and wild.
> - **Shot 9 (Pip's 1.5s Freeze):** Generate as normal — the actual 1.5s freeze frame is applied manually in CapCut (Step 4).
> - **Shot 11 (Sincerity Beat):** Use lowest motion setting. Minimal movement. Let the emotion breathe.
> - **Shot 12 (TV Remote):** Slow, creeping tension. The pupil dilation is the key.

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io/)**.
* **Voice Profiles:**
  * **Barnaby:** Anxious, slightly high-pitched, formal pompous tenor.
  * **Milo:** Fast, chirpy, high-energy monkey chatter — short excited bursts.
  * **Pip:** Fast, raspy, energetic hyperactive squeak.
  * **Bao:** Deep, warm, gentle, devastated bass.

Generate these dialogue lines:
* **Line 1 (Barnaby - Shot 1):** *"Milo — Gym pass. Easy hai, aaj."* ──► `assets/sfx/VOICE_Barnaby_EP003_L01.mp3`
* **Line 2 (Milo - Shot 2):** *"Ooh! Button! Ek aur! Ek aur!"* ──► `assets/sfx/VOICE_Milo_EP003_L02.mp3`
* **Line 3 (Barnaby - Shot 4):** *"Red buttons mat dabao. Bilkul mat."* ──► `assets/sfx/VOICE_Barnaby_EP003_L03.mp3`
* **Line 4 (Milo - Shot 4):** *"Haan haan! No red! Promise!"* ──► `assets/sfx/VOICE_Milo_EP003_L04.mp3`
* **Line 5 (Bao - Shot 5):** *"Mera blender! Smoothie barbaad ho gaya!"* ──► `assets/sfx/VOICE_Bao_EP003_L05.mp3`
* **Line 6 (Barnaby - Shot 6):** *"Ruko! Sab kuch band karo! PIP!"* ──► `assets/sfx/VOICE_Barnaby_EP003_L06.mp3`
* **Line 7 (Pip - Shot 7):** *"Ye banda rukta hi nahi! Boss, help!"* ──► `assets/sfx/VOICE_Pip_EP003_L07.mp3`
* **Line 8 (Pip - Shot 11):** *"Sab band. Finally."* (Exhausted whisper) ──► `assets/sfx/VOICE_Pip_EP003_L08.mp3`
* **Line 9 (Barnaby - Shot 12):** *"Milo... nahin..."* (Horrified whisper) ──► `assets/sfx/VOICE_Barnaby_EP003_L09.mp3`

---

## STEP 4: COMBINE & EXPORT IN CAPCUT / DAVINCI

1. **Create Project:** Open **CapCut** ──► Click **New Project** ──► Set **Ratio: `16:9` (Widescreen)**.
2. **Timeline Layout:**
   * Drag all 12 clips (`EP003_Shot01_Clip.mp4` to `Shot12`) onto the video track in order.
   * Drag the 9 voice audio tracks underneath their respective scenes and align with character mouth movements.
3. **The 7-Button Spam Rhythm (Shot 2):**
   * Add 7 unique cartoon button SFX, each louder and weirder: BEEP → BOOP → BONK → DING → HONK → SQUEAK → FOGHORN.
   * Space them evenly across 3 seconds for maximum comedic rhythm.
4. **Pip's 1.5-Second Comedy Freeze (Shot 9):**
   * Go to Shot 9 (Pip frozen, staring at camera).
   * Freeze the frame for **1.5 seconds** at the peak of his deadpan stare.
   * Important: This is the FIRST TIME Pip freezes (subverting the running gag). Let the silence land fully.
5. **The Sincerity Beat (Shot 11):**
   * Slow Shot 11 down slightly (0.8x speed) to let the rubber-band-tying moment breathe for a full 10 seconds.
6. **The TV Remote Cliffhanger (Shot 12):**
   * After the blackout frame, add exactly **one single TV remote CLICK** SFX in total darkness.
   * Hold the black screen for 2 full seconds after the click before the video ends.
7. **Music & SFX Track:**
   * Add playful upbeat gym/jazz music at `-18dB` throughout Shots 1–8.
   * **Kill the music completely** during Pip's 1.5s freeze (Shot 9) — total silence.
   * Add warm ambient music during the sincerity beat (Shot 11).
   * Add tension music (low drone) during the TV remote moment (Shot 12).
   * Key SFX: 7-button sounds (Shot 2), lever clank (Shot 5), rubber band SNAP (Shot 5), blender splatter (Shot 5), sparking crackle (Shot 6–8), rubber band Tarzan twang (Shot 8), emergency lever CLUNK (Shot 10), single TV click (Shot 12).
8. **Auto-Captions:**
   * Click **Text** ──► **Auto-Captions** ──► Select yellow cartoon font with black stroke.
9. **Export Master Episode:**
   * Resolution: `1080p` or `4K` | Frame Rate: `24fps`.
   * **Save Output to:** `output/EP-003_MASTER.mp4`
