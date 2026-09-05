# EP-002 Step-by-Step Production Guide

> **Project:** Critter Haven Resort — EP-002 "The King's Arrival"
> **Source Script:** [script.md](script.md) | **Shot List:** [shot-list.md](shot-list.md)
> **Format:** Standard YouTube Episode (16:9 Cinematic Widescreen)
> **Duration:** ~2 minutes 30 seconds (12 Core Shots)
> **Target Master Output:** `output/EP-002_MASTER.mp4`

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

* **Shot 1 (Royal Reservation):** `3D Pixar animation style, cinematic 16:9, cute chubby golden Syrian hamster in red twist-tie bowtie at miniature tea-saucer desk, holding postage-stamp clipboard with wide terrified eyes, warm 8AM morning sunbeams, ultra-detailed hamster fur, 8k --ar 16:9` ──► Save as `assets/characters/EP002_Shot01_Keyframe.png`
* **Shot 2 (Leo Tube Arrival):** `3D Pixar animation style, low angle, fluffy dramatic African lion cub flying out of colorful plastic tube hatch in shower of golden glitter, gold-foil candy wrapper crown tilted, one paw extended, vibrant lobby background --ar 16:9` ──► Save as `assets/characters/EP002_Shot02_Keyframe.png`
* **Shot 3 (Cotton Ball Inspection):** `3D Pixar animation style, medium two-shot, large fluffy lion cub holding single tiny cotton ball between two claws staring with theatrical disbelief at nervous golden hamster in red bowtie inside shoebox suite, thimble lamp glowing --ar 16:9` ──► Save as `assets/characters/EP002_Shot03_Keyframe.png`
* **Shot 4 (Bed Collapse):** `3D Pixar animation style, hilarious side-view of dramatic lion cub with gold-foil crown sitting flat on completely collapsed cardboard shoebox floor, paw raised to forehead in theatrical despair, Barnaby watching open-mouthed --ar 16:9` ──► Save as `assets/characters/EP002_Shot04_Keyframe.png`
* **Shot 5 (Barnaby Panic Sprint):** `3D Pixar animation style, low angle fast-motion tracking shot of chubby golden hamster in red bowtie sprinting in full panic-blur through colorful translucent plastic tube corridor, motion-blur on legs, ears pinned back, mouth open --ar 16:9` ──► Save as `assets/characters/EP002_Shot05_Keyframe.png`
* **Shot 6 (Rocco Cotton Tower):** `3D Pixar animation style, wide shot, massive white rhinoceros calf balancing enormous wobbling tower of 50 fluffy cotton balls on his golden horn, eyes crossed in deep concentration, tongue slightly out, yellow construction tape on horn, two hamsters watching nervously --ar 16:9` ──► Save as `assets/characters/EP002_Shot06_Keyframe.png`
* **Shot 7 (Cotton Blizzard Launch):** `3D Pixar animation style, dynamic wide action shot, rhino calf mid-trip launching 50 white cotton balls in explosive slow-motion blizzard filling entire hamster cage lobby, two tiny hamsters frozen in shock, cinematic particle physics --ar 16:9` ──► Save as `assets/characters/EP002_Shot07_Keyframe.png`
* **Shot 8 (1.5s Freeze + Crown Landing):** `3D Pixar animation style, close-up of cotton-coated golden hamster with pin-prick pupils staring directly at camera in deadpan shock, in background lion cub with one eye open patting a cotton ball that just landed on his tilted crown --ar 16:9` ──► Save as `assets/characters/EP002_Shot08_Keyframe.png`
* **Shot 9 (Speed Build Montage):** `3D Pixar animation style, high-angle wide shot, two hamsters and rhino calf frantically speed-building magnificent towering cotton-ball royal bed inside shoebox room, clock showing 4:30PM, motion blur on paws, golden-hour orange glow --ar 16:9` ──► Save as `assets/characters/EP002_Shot09_Keyframe.png`
* **Shot 10 (Leo Sinks In + Sincerity Beat):** `3D Pixar animation style, warm sincere medium two-shot, large fluffy lion cub sunk into magnificent cotton mountain royal bed, one eye open looking gently at small golden hamster with quiet proud smile, golden afternoon light --ar 16:9` ──► Save as `assets/characters/EP002_Shot10_Keyframe.png`
* **Shot 11 (Royal Refuses to Hide):** `3D Pixar animation style, wide comedic shot, golden hamster in red bowtie frantically gesturing at lion cub on cotton mountain who is completely unbothered with one regal eye open, dwarf hamster hiding behind thimble, warm evening lighting --ar 16:9` ──► Save as `assets/characters/EP002_Shot11_Keyframe.png`
* **Shot 12 (Human Pats Leo / Barnaby Smirk):** `3D Pixar animation style, close-up of fluffy lion cub in gold-foil crown sitting smugly in cotton nest, large human hand gently patting his head, warm cozy evening glow --ar 16:9` ──► Save as `assets/characters/EP002_Shot12_Keyframe.png`

---

## STEP 2: ANIMATE THE 12 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com/)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip (Kling automatically matches 16:9).

For each shot:
1. Upload the corresponding keyframe image (`EP002_Shot01_Keyframe.png` to `Shot12`).
2. Copy the **AI Video Prompt** from [shot-list.md](shot-list.md).
3. Click **Generate** ──► Download video clip as `assets/EP002_Shot01_Clip.mp4` through `Shot12`.

> **Key Shots to Pay Attention To:**
> - **Shot 7 (Cotton Blizzard):** Enable slow-motion mode in Kling if available. The blizzard is the episode's signature viral moment.
> - **Shot 8 (1.5s Freeze):** Generate as normal — the freeze will be applied manually in the editor in Step 4.
> - **Shot 10 (Sincerity Beat):** Aim for the gentlest, warmest motion output. Minimal movement.

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io/)**.
* **Voice Profiles:**
  * **Barnaby:** Anxious, slightly high-pitched, formal pompous tenor.
  * **Leo:** Deep, booming theatrical bass — followed by squeaky cub voice on emotional lines.
  * **Pip:** Fast, raspy, energetic hyperactive squeak.
  * **Rocco:** Deep, gentle, polite rumble.

Generate these dialogue lines:
* **Line 1 (Barnaby - Shot 1):** *"Leo — Royal Suite — 100 feather bed chahiye."* ──► `assets/sfx/VOICE_Barnaby_EP002_L01.mp3`
* **Line 2 (Barnaby - Shot 2):** *"Welcome, welcome! Suite ready hai, Your Magnificence!"* ──► `assets/sfx/VOICE_Barnaby_EP002_L02.mp3`
* **Line 3 (Leo - Shot 2):** *"Hmph. Show me my royal chambers."* ──► `assets/sfx/VOICE_Leo_EP002_L03.mp3`
* **Line 4 (Leo - Shot 3):** *"Ek... cotton ball?"* (Horrified whisper) ──► `assets/sfx/VOICE_Leo_EP002_L04.mp3`
* **Line 5 (Leo - Shot 4):** *"Main... main toot gaya. Emotionally."* ──► `assets/sfx/VOICE_Leo_EP002_L05.mp3`
* **Line 6 (Barnaby - Shot 4):** *"Pip! Rocco! Emergency hai! Jaldi aao!"* ──► `assets/sfx/VOICE_Barnaby_EP002_L06.mp3`
* **Line 7 (Rocco - Shot 6):** *"Nahin nahin nahin nahin—"* (Gentle horrified gasp) ──► `assets/sfx/VOICE_Rocco_EP002_L07.mp3`
* **Line 8 (Leo - Shot 10):** *"...Theek hai. Acceptable."* then *"Ab pillow fluff karo. Dono side se."* ──► `assets/sfx/VOICE_Leo_EP002_L08.mp3`
* **Line 9 (Pip - Shot 9):** *"Five minutes bache hain, boss!"* ──► `assets/sfx/VOICE_Pip_EP002_L09.mp3`
* **Line 10 (Human Voice - Shot 12):** *"Aww — look at that cozy little nest!"* ──► `assets/sfx/VOICE_Human_EP002_L10.mp3`

---

## STEP 4: COMBINE & EXPORT IN CAPCUT / DAVINCI

1. **Create Project:** Open **CapCut** ──► Click **New Project** ──► Set **Ratio: `16:9` (Widescreen)**.
2. **Timeline Layout:**
   * Drag all 12 clips (`EP002_Shot01_Clip.mp4` to `Shot12`) onto the video track in order.
   * Drag the 10 voice audio tracks underneath their respective scenes and align with character mouth movements.
3. **The 1.5-Second Comedy Freeze (Shot 8):**
   * Go to Shot 8 (cotton-coated Barnaby staring deadpan at the camera).
   * Freeze the frame for **1.5 seconds** at the peak of his deadpan stare, right before the cotton ball drifts down.
4. **The Sincerity Beat (Shot 10):**
   * Slow Shot 10 down slightly (0.8x speed) to let the quiet gratitude moment breathe for a full 10 seconds.
5. **Music & SFX Track:**
   * Add playful brass hotel jazz music at `-18dB` throughout.
   * Add SFX: Door click (Shot 1), glitter shimmer + royal fanfare (Shot 2), slow bass sting (Shot 3), cardboard crunch *CRACK!* (Shot 4), rubber-band snap + cotton launch *WHOOOMP* (Shot 7), soft cotton *poof* (Shot 8), clock chime (Shot 9), bowtie adjustment *PING* (Shot 12).
6. **Auto-Captions:**
   * Click **Text** ──► **Auto-Captions** ──► Select yellow cartoon font with black stroke.
7. **Export Master Episode:**
   * Resolution: `1080p` or `4K` | Frame Rate: `24fps`.
   * **Save Output to:** `output/EP-002_MASTER.mp4`
