# EP-001 Step-by-Step Production Guide

> **Project:** Critter Haven Resort — EP-001 "The Grand Opening Chaos"  
> **Source Script:** [script.md](script.md) | **Shot List:** [shot-list.md](shot-list.md)  
> **Format:** Standard YouTube Episode (16:9 Cinematic Widescreen)  
> **Duration:** ~2 minutes 30 seconds (12 Core Shots)  
> **Target Master Output:** `output/EP-001_MASTER.mp4`

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

* **Shot 1 (8AM Opening):** `3D Pixar animation style, cinematic 16:9, cute chubby golden Syrian hamster named Barnaby popping out of fluffy cedar wood shavings inside luxury modern cage, red twist-tie bowtie, warm morning sunlight, volumetric light, 8k --ar 16:9` ──► Save as `assets/characters/EP001_Shot01_Keyframe.png`.
* **Shot 2 (Sign Flip):** `3D Pixar animation style, low angle, golden hamster in red bowtie behind tea-saucer reception desk, tiny cardboard sign 'RESORT OPEN', soft morning lighting --ar 16:9` ──► Save as `assets/characters/EP001_Shot02_Keyframe.png`.
* **Shot 3 (Water Drip):** `3D Pixar animation style, inside clear plastic tube, golden hamster looking at falling water droplet on his nose, wide curious eyes, sharp reflections --ar 16:9` ──► Save as `assets/characters/EP001_Shot03_Keyframe.png`.
* **Shot 4 (Gasket Push):** `3D Pixar animation style, close up, golden hamster on tiptoes pressing tiny paw against bulging black rubber gasket on clear pipe, high tension reflections --ar 16:9` ──► Save as `assets/characters/EP001_Shot04_Keyframe.png`.
* **Shot 5 (Gasket Burst):** `3D Pixar animation style, dynamic jet of water exploding from pipe joint, spraying directly into face of surprised hamster, splashing droplets, cinematic water physics --ar 16:9` ──► Save as `assets/characters/EP001_Shot05_Keyframe.png`.
* **Shot 6 (Cheek Stuffing):** `3D Pixar animation style, hilarious comedy shot of golden hamster with gigantic 3x puffed cheek pouches holding mini sponge, drenched spiky fur, water rising --ar 16:9` ──► Save as `assets/characters/EP001_Shot06_Keyframe.png`.
* **Shot 7 (Helicopter Bowtie):** `3D Pixar animation style, motion blur shot of hamster flying backward through spiral tube carried by water wave, red bowtie spinning into circular propeller blur --ar 16:9` ──► Save as `assets/characters/EP001_Shot07_Keyframe.png`.
* **Shot 8 (1.5s Freeze Hold):** `3D Pixar animation style, deadpan close-up of drenched hamster with spiky wet fur and pin-prick pupils staring directly at camera, giant spherical water bubble hovering above head --ar 16:9` ──► Save as `assets/characters/EP001_Shot08_Keyframe.png`.
* **Shot 9 (Pip Skateboard Arrival):** `3D Pixar animation style, low angle action shot of Pip the tiny dwarf hamster powersliding in on a toy skateboard, wearing mini tool belt, golden hour 4:30PM light --ar 16:9` ──► Save as `assets/characters/EP001_Shot09_Keyframe.png`.
* **Shot 10 (Slingshot Button Fix):** `3D Pixar animation style, cozy sincere moment, soggy golden hamster in bowtie looks down gratefully at tiny dwarf mechanic with slingshot, shirt button plugged into pipe leak --ar 16:9` ──► Save as `assets/characters/EP001_Shot10_Keyframe.png`.
* **Shot 11 (4:55 PM Speed Mop):** `3D Pixar animation style, high angle wide shot, two hamsters frantically mopping glistening wet floor with cotton balls, clock showing 4:55 PM, motion blur of frantic cleaning --ar 16:9` ──► Save as `assets/characters/EP001_Shot11_Keyframe.png`.
* **Shot 12 (Pretend-Sleep Loop):** `3D Pixar animation style, golden hamster curled up inside wooden hut with cartoon snoring bubble from nose, one sly eye open winking at camera, neat red bowtie, cozy evening glow --ar 16:9` ──► Save as `assets/characters/EP001_Shot12_Keyframe.png`.

---

## STEP 2: ANIMATE THE 12 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com/)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip (Kling automatically matches 16:9).

For each shot:
1. Upload the corresponding keyframe image (`EP001_Shot01_Keyframe.png` to `Shot12`).
2. Copy the **AI Video Prompt** from [shot-list.md](shot-list.md).
3. Click **Generate** ──► Download video clip as `assets/EP001_Shot01_Clip.mp4` through `Shot12`.

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io/)**.
* **Voice Profiles:**
  * **Barnaby:** Anxious, slightly high-pitched, formal pompous tenor.
  * **Pip:** Fast, raspy, energetic hyperactive squeak.

Generate these dialogue lines:
* **Line 1 (Barnaby - Shot 1):** *"Human gaya! Resort open karo, chalo!"* ──► `assets/sfx/VOICE_Barnaby_L01.mp3`
* **Line 2 (Barnaby - Shot 3):** *"Ek boond? No problem, main sambhal loonga."* ──► `assets/sfx/VOICE_Barnaby_L02.mp3`
* **Line 3 (Barnaby - Shot 6):** *(Muffled through cheeks)* *"Mmmph! Pip kahan hai?! Tube phat gaya!"* ──► `assets/sfx/VOICE_Barnaby_L03.mp3`
* **Line 4 (Pip - Shot 10):** *"Five minutes bache hain! Jaldi saaf karo!"* ──► `assets/sfx/VOICE_Pip_L04.mp3`
* **Line 5 (Human Voice - Shot 12):** *"Aww, look how peaceful! He's been sleeping all day."* ──► `assets/sfx/VOICE_Human_L05.mp3`

---

## STEP 4: COMBINE & EXPORT IN CAPCUT / DAVINCI

1. **Create Project:** Open **CapCut** ──► Click **New Project** ──► Set **Ratio: `16:9` (Widescreen)**.
2. **Timeline Layout:**
   * Drag all 12 clips (`EP001_Shot01_Clip.mp4` to `Shot12`) onto the video track.
   * Drag the 5 voice audio tracks underneath their respective scenes and line them up with the character's mouth.
3. **The 1.5-Second Comedy Freeze (Shot 8):**
   * Go to Shot 8 (drenched Barnaby staring deadpan at the camera).
   * Freeze the frame for **1.5 seconds** right before the giant bubble bursts!
4. **Music & SFX Track:**
   * Add playful jazz hotel music at `-18dB`.
   * Add SFX: Door click (Shot 1), water drip (Shot 3), high pressure spray hiss (Shot 5), bubble pop (Shot 8), slingshot twang (Shot 10), loud cartoon snores (Shot 12).
5. **Auto-Captions:**
   * Click **Text** ──► **Auto-Captions** ──► Select yellow cartoon font with black stroke.
6. **Export Master Episode:**
   * Resolution: `1080p` or `4K` | Frame Rate: `24fps`.
   * **Save Output to:** `output/EP-001_MASTER.mp4`.
