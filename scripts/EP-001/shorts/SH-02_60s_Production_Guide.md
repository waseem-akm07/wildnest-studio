# SH-02 Step-by-Step Production Guide (60s)

> **Project:** Critter Haven Resort — SH-02 "The Grand Opening Chaos" (60s Cut)  
> **Source Script:** [SH-02_60s_Grand_Opening_Cut.md](SH-02_60s_Grand_Opening_Cut.md)  
> **Format:** YouTube Short (9:16 Vertical)  
> **Duration:** Exactly 60 Seconds (10 Fast-Paced Clips)  
> **Target Output:** `output/SH-02_60s_Grand_Opening.mp4`

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

Copy and generate each prompt from [SH-02_Grand_Opening_Cut.md](SH-02_Grand_Opening_Cut.md):

1. **Shot 1 (Opening Sign):** `3D Pixar animation style, vertical 9:16, cute chubby golden Syrian hamster in red twist-tie bowtie standing behind miniature tea-saucer desk inside luxury plastic cage, flipping tiny sign to 'RESORT OPEN', warm morning sunlight --ar 9:16` ──► Save as `assets/characters/SH02_Shot01_Keyframe.png`
2. **Shot 2 (Water Drip):** `3D Pixar animation style, vertical 9:16, inside clear plastic tube, golden hamster in red bowtie blinking in surprise as single water drop hits his nose, wide curious eyes, sharp reflections --ar 9:16` ──► Save as `assets/characters/SH02_Shot02_Keyframe.png`
3. **Shot 3 (Pipe Burst):** `3D Pixar animation style, vertical 9:16, high-pressure water stream exploding from pipe joint, blasting directly into face of shocked golden hamster with flying water droplets --ar 9:16` ──► Save as `assets/characters/SH02_Shot03_Keyframe.png`
4. **Shot 4 (Cheek Stuffing):** `3D Pixar animation style, vertical 9:16, hilarious comedy shot of golden hamster with gigantic 3x puffed cheek pouches holding mini sponge, drenched spiky fur, water rising around paws --ar 9:16` ──► Save as `assets/characters/SH02_Shot04_Keyframe.png`
5. **Shot 5 (Helicopter Bowtie):** `3D Pixar animation style, vertical 9:16, golden hamster flying backwards through spiral clear plastic tube, red twist-tie bowtie spinning into circular propeller blur, dynamic motion blur --ar 9:16` ──► Save as `assets/characters/SH02_Shot05_Keyframe.png`
6. **Shot 6 (1.5s Freeze Hold):** `3D Pixar animation style, vertical 9:16, drenched golden hamster with spiky fur and pin-prick pupils staring deadpan directly into camera lens, large spherical water bubble floating over head --ar 9:16` ──► Save as `assets/characters/SH02_Shot06_Keyframe.png`
7. **Shot 7 (Pip Skateboard Arrival):** `3D Pixar animation style, vertical 9:16, low-angle action shot of tiny Roborovski dwarf hamster Pip zooming in on mini tech finger skateboard, confident wink, tool belt, golden sunset light --ar 9:16` ──► Save as `assets/characters/SH02_Shot07_Keyframe.png`
8. **Shot 8 (Button Slingshot Fix):** `3D Pixar animation style, vertical 9:16, colorful shirt button tightly plugged into leaking plastic tube joint, water spray stopped, warm lighting --ar 9:16` ──► Save as `assets/characters/SH02_Shot08_Keyframe.png`
9. **Shot 9 (4:55 PM Speed Mop):** `3D Pixar animation style, vertical 9:16, two hamsters frantically mopping glistening wet cage floor with cotton balls, clock showing 4:55 PM, fast motion blur, spotless clean floor --ar 9:16` ──► Save as `assets/characters/SH02_Shot09_Keyframe.png`
10. **Shot 10 (Pretend-Sleep Loop):** `3D Pixar animation style, vertical 9:16, golden hamster curled up in wooden sleeping hut with cartoon snoring bubble from nose, one sly eye open winking at camera, neat red bowtie, cozy evening light --ar 9:16` ──► Save as `assets/characters/SH02_Shot10_Keyframe.png`

---

## STEP 2: ANIMATE THE 10 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com/)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip (Kling automatically matches 9:16).

For each shot:
1. Upload the corresponding keyframe image (`SH02_Shot01_Keyframe.png` to `Shot10`).
2. Copy the **AI Video Prompt** from [SH-02_Grand_Opening_Cut.md](SH-02_Grand_Opening_Cut.md).
3. Click **Generate** ──► Download video clip as `assets/SH02_Shot01_Clip.mp4` through `Shot10`.

---

## STEP 3: GENERATE CHARACTER VOICES (TTS)

* **Where to go:** Open **[ElevenLabs](https://elevenlabs.io/)**.
* **Voice Profiles:**
  * **Barnaby:** Expressive, slightly high-pitched, formal pompous tenor.
  * **Pip:** Fast, raspy, energetic hyperactive squeak.

Generate these dialogue lines:
* **Line 1 (Barnaby - Shot 1):** *"Human gaya! Resort open karo!"* ──► `assets/sfx/VOICE_Barnaby_SH02_L01.mp3`
* **Line 2 (Barnaby - Shot 2):** *"Ek boond? Main sambhal loonga!"* ──► `assets/sfx/VOICE_Barnaby_SH02_L02.mp3`
* **Line 3 (Barnaby - Shot 4):** *(Muffled)* *"Mmmph! Pip kahan hai?!"* ──► `assets/sfx/VOICE_Barnaby_SH02_L03.mp3`
* **Line 4 (Pip - Shot 7):** *"Don't worry boss! Main hoon na!"* ──► `assets/sfx/VOICE_Pip_SH02_L04.mp3`
* **Line 5 (Human Voice - Shot 10):** *"Aww, he's sleeping!"* ──► `assets/sfx/VOICE_Human_SH02_L05.mp3`

---

## STEP 4: COMBINE & EXPORT IN CAPCUT (Takes 3 Minutes)

1. **Create Project:** Open **CapCut** ──► Click **New Project** ──► Set **Ratio: `9:16` (Vertical)**.
2. **Timeline Layout:**
   * Drag all 10 clips (`SH02_Shot01_Clip.mp4` to `Shot10`) onto the video track.
   * Trim clips slightly so the total runtime hits exactly **60 seconds**.
   * Drag the 5 voice audio tracks underneath their respective scenes and line them up with the character's mouth.
3. **The 1.5-Second Comedy Freeze (Shot 6):**
   * Go to Shot 6 (drenched Barnaby staring deadpan at the camera).
   * Freeze the frame for **1.5 seconds** right before the giant bubble bursts!
4. **Music & SFX Track:**
   * Add playful jazz hotel music at `-18dB`.
   * Add cartoon SFX: Water hiss (Shot 3), bubble pop (Shot 6), slingshot twang (Shot 8), loud cartoon snores (Shot 10).
5. **Auto-Captions:**
   * Click **Text** ──► **Auto-Captions** ──► Select yellow cartoon font with black stroke.
6. **Export Master Short:**
   * Resolution: `1080p` | Frame Rate: `24fps`.
   * **Save Output to:** `output/SH-02_Grand_Opening_60s.mp4`.

---

## 🚀 READY TO UPLOAD TO YOUTUBE SHORTS

* **Title:** When your luxury pet resort floods before 5 PM! 🚨🐹 #Shorts
* **Description:** Barnaby opens the secret 5-star pet resort, but a broken pipe creates complete chaos before the human gets home! Can Pip save the day?
* **Hashtags:** `#Animation #3DAnimation #PixarStyle #CuteAnimals #Cartoons #SlapstickComedy #Hinglish`
* **Pinned Comment:** "Which character are you: Overthinking Barnaby or Chaotic Mechanic Pip? 👇"
