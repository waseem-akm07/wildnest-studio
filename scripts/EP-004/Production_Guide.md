# EP-004 Step-by-Step Production Guide

> **Project:** Critter Haven Resort — EP-004 "The Great Bao Blockage"
> **Source Script:** [script.md](script.md) | **Shot List:** [shot-list.md](shot-list.md)
> **Format:** Standard YouTube Episode (16:9 Cinematic Widescreen)
> **Duration:** ~2 minutes 30 seconds (12 Core Shots)
> **Target Master Output:** `output/EP-004_MASTER.mp4`

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
* **Canvas Setting:** Set **Aspect Ratio** to **`16:9` (Landscape)**.
* **Model:** Select **Leonardo Phoenix** or **3D Animation style**.

Copy the prompts from [shot-list.md](shot-list.md) for each shot:

* **Shot 1 (Lunch Rush Announcement):** `3D Pixar animation style, cinematic 16:9, cute chubby golden Syrian hamster named Barnaby in red twist-tie bowtie at miniature desk, flipping tiny chalkboard sign "LUNCH RUSH", warm 8AM morning sunlight, detailed fur, cheerful expression, 8k --ar 16:9` ──► Save as `assets/characters/EP004_Shot01_Keyframe.png`
* **Shot 2 (Five-Star Knife Skills & Prep):** `3D Pixar animation style, cinematic 16:9, lovable fluffy giant panda cub named Bao wearing red-and-white checkered neckerchief behind wooden block counter, tiny bowls of sunflower seeds, popsicle-stick boards, miniature blender, confident masterchef grin --ar 16:9` ──► Save as `assets/characters/EP004_Shot02_Keyframe.png`
* **Shot 3 (Sneaky Snacking Escalation):** `3D Pixar animation style, cinematic 16:9, comedy close-up of chubby panda cub chef sneaking bright dried berry into mouth with guilty side-glancing eyes, round belly bulging over counter, stretching neckerchief, bright kitchen --ar 16:9` ──► Save as `assets/characters/EP004_Shot03_Keyframe.png`
* **Shot 4 (Barnaby's Check-In & Big Gulp):** `3D Pixar animation style, cinematic 16:9, cartoon moment where panda cub's tummy has ballooned into enormous round sphere like fuzzy basketball after swallowing snack whole, tiny hamster in doorway walking away, popped neckerchief, shocked cute face --ar 16:9` ──► Save as `assets/characters/EP004_Shot04_Keyframe.png`
* **Shot 5 (Hydraulic Tube Wedging):** `3D Pixar animation style, cinematic 16:9, side view of round fluffy panda cub hopelessly wedged inside clear curved plastic hamster tunnel, enormous chubby belly pressed flat against circular tube walls like airtight cork, paddling paws helplessly, balancing trays --ar 16:9` ──► Save as `assets/characters/EP004_Shot05_Keyframe.png`
* **Shot 6 (King Leo's Impatient Wait):** `3D Pixar animation style, cinematic 16:9, dramatic low-angle shot of haughty lion cub named Leo wearing shiny gold-foil candy crown and napkin tucked into neck, sitting at miniature dining table with silver fork and knife held upright, glaring with royal impatience --ar 16:9` ──► Save as `assets/characters/EP004_Shot06_Keyframe.png`
* **Shot 7 (Push & Pull Struggle):** `3D Pixar animation style, cinematic 16:9, wide comedy shot of clear plastic tube, huge panda cub wedged tightly, tiny dwarf hamster mechanic in visor pushing rear with all his might, baby rhino calf pulling front paw, straining comedic action --ar 16:9` ──► Save as `assets/characters/EP004_Shot07_Keyframe.png`
* **Shot 8 (1.5s GROUP Reaction Freeze):** `3D Pixar animation style, cinematic 16:9, deadpan comedy freeze-frame: golden hamster in red bowtie, tiny dwarf hamster in paperclip visor, baby rhino calf with tape on horn all standing in a row, completely frozen with shocked pin-prick pupils staring at camera --ar 16:9` ──► Save as `assets/characters/EP004_Shot08_Keyframe.png`
* **Shot 9 (Cheek-Stuffing Mountain Climb):** `3D Pixar animation style, cinematic 16:9, hilarious action shot: golden hamster with enormous puffed cheek pouches swollen three times head size crawling over gigantic soft furry belly of stuck panda cub inside plastic tube, carrying tiny strawberry slice, wobbling balance --ar 16:9` ──► Save as `assets/characters/EP004_Shot09_Keyframe.png`
* **Shot 10 (Cotton Slingshot & Cork-Pop):** `3D Pixar animation style, cinematic 16:9, high-energy cartoon pop: oversized panda cub shooting out of circular plastic tunnel opening like champagne cork amid speed lines and popping dust motes, roaring with laughter, eyes squeezed shut in glee --ar 16:9` ──► Save as `assets/characters/EP004_Shot10_Keyframe.png`
* **Shot 11 (Ruined Feast & Sincerity Cookie):** `3D Pixar animation style, cinematic 16:9, heartfelt emotional two-shot: sad giant panda cub sitting on floor surrounded by dropped trays, offering single golden paw-print cookie with both large furry paws to kind golden hamster, golden 4PM sunset light, deep emotional warmth --ar 16:9` ──► Save as `assets/characters/EP004_Shot11_Keyframe.png`
* **Shot 12 (4:59 PM Bedtime Squeeze & Human Pat):** `3D Pixar animation style, cinematic 16:9, comedy ending: fluffy panda cub stuck head-first in circular door of wooden crate, only fluffy rear end and tail sticking out, giant human hand gently patting back, hamster facepalming in overturned teacup in background --ar 16:9` ──► Save as `assets/characters/EP004_Shot12_Keyframe.png`

---

## STEP 2: ANIMATE THE 12 VIDEO CLIPS (Image-to-Video)

* **Where to go:** Open **[Kling AI](https://klingai.com/)** (or **Hailuo AI**).
* **Mode Selection:** Click **AI Video** ──► Choose **Image to Video (I2V)**.
* **Duration:** Set to **5 seconds** for each clip (16:9 Landscape).

For each shot:
1. Upload the corresponding keyframe image (`EP004_Shot01_Keyframe.png` to `Shot12`).
2. Copy the **AI Video Prompt** from [shot-list.md](shot-list.md).
3. Click **Generate** ──► Download video clip as `assets/EP004_Shot01_Clip.mp4` through `Shot12`.

> **Key Shots to Pay Attention To:**
> - **Shot 4 (The Big Gulp):** The belly expansion must feel snappy and cartoonish — like inflating a balloon in 1 second.
> - **Shot 8 (Group Freeze):** Generate the clip normally with subtle ambient motion, then apply a complete **1.5-second Freeze Frame** inside CapCut (Step 4) for comedic perfection.
> - **Shot 9 (Cheek-Stuffing Climb):** Barnaby's cheeks must look soft and gelatinous while he balances and fixes his bowtie.
> - **Shot 10 (Cork-Pop):** Use Kling's high motion setting so Bao shoots forward with punchy cartoon velocity.
> - **Shot 11 (Sincerity Beat):** Use lowest motion setting. Gentle, tender expressions; let the heartfelt moment breathe.

---

## STEP 3: GENERATE HINGLISH VOICE LINES & SFX

### Dialogue Lines (ElevenLabs / Edge-TTS)

Use ElevenLabs with the character voice profiles established in `voice-prompts.md`:

| Character | Voice Profile | Line to Generate | Output Filename |
|:---|:---|:---|:---|
| **Barnaby** | High-pitched, articulate, nervous manager | *"Aaj resort ka pehla big feast hai!"* | `assets/sfx/EP004_Barnaby_01.mp3` |
| **Bao** | Deep, gentle, warm, rumbling panda cub | *"Menu... bilkul five-star hoga, Boss!"* | `assets/sfx/EP004_Bao_01.mp3` |
| **Bao** | Chewing sounds & satisfied mumbling | *"Nom-nom-nom!"* | `assets/sfx/EP004_Bao_02.mp3` |
| **Barnaby** | Crisp, brisk check-in | *"Bao! Starters ready hai na?"* | `assets/sfx/EP004_Barnaby_02.mp3` |
| **Bao** | Muffled, guilty, high innocent pitch | *"Haan boss! Sab on track hai!"* | `assets/sfx/EP004_Bao_03.mp3` |
| **Bao** | Straining, cute squeak | *"Uh oh. Tube thoda chhota ho gaya?"* | `assets/sfx/EP004_Bao_04.mp3` |
| **Leo** | Haughty, dramatic royal lion cub | *"Mera royal lunch kahan hai?!"* | `assets/sfx/EP004_Leo_01.mp3` |
| **Pip** | Hyperactive, high-speed squeak | *"Zor lagao, Rocco!"* | `assets/sfx/EP004_Pip_01.mp3` |
| **Barnaby** | Fast, urgent problem-solving | *"Leo wait nahi karega! Idea chahiye!"* | `assets/sfx/EP004_Barnaby_03.mp3` |
| **Barnaby** | Muffled, full cheeks, formal | *"Aapka lunch, Your Majesty!"* | `assets/sfx/EP004_Barnaby_04.mp3` |
| **Leo** | Disappointed royal scoff | *"Yeh? Sirf ek bite?!"* | `assets/sfx/EP004_Leo_02.mp3` |
| **Bao** | Uncontrollable booming belly laughs | *"Hahaha! HO HO HO!"* | `assets/sfx/EP004_Bao_05.mp3` |
| **Bao** | Soft, heartbroken, trembling whimper | *"Sorry, Barnaby... maine sab kharab kiya."* | `assets/sfx/EP004_Bao_06.mp3` |
| **Barnaby** | Gentle, comforting, heartfelt | *"Best cookie ever, Bao. Sab theek hai."* | `assets/sfx/EP004_Barnaby_05.mp3` |
| **Human** | Warm, fond pet owner | *"Aww, Bao, did you eat too many treats again? You chubby boy!"* | `assets/sfx/EP004_Human_01.mp3` |

### Crucial Sound Effects (Freesound.org / Pixabay)
* `SFX_Knife_Chop.mp3` — Fast rhythmic vegetable chopping
* `SFX_Blender_Whir.mp3` — Miniature electric blender whirring
* `SFX_Belly_Balloon.mp3` — Rubber balloon inflating sound
* `SFX_Tube_Wedged_Thump.mp3` — Rubbery hydraulic vacuum seal *THWUMP*
* `SFX_Fork_Tapping.mp3` — Impatient metallic fork on porcelain *TINK-TINK-TINK*
* `SFX_Rubber_Stretch.mp3` — Boingy rubber band stretching sound
* `SFX_Clock_Tick_Tock.mp3` — Deadpan clock ticks during the 1.5s group freeze
* `SFX_Bowtie_Snap.mp3` — Crisp snap when Barnaby adjusts bowtie mid-climb
* `SFX_Slingshot_Twang.mp3` — High-tension rubber band release
* `SFX_Champagne_Pop.mp3` — Loud cartoon cork pop for Bao shooting free
* `SFX_Gentle_Acoustic_Theme.mp3` — Warm, cozy acoustic guitar track for sincerity beat
* `SFX_Belly_Pats.mp3` — Affectionate soft thuds on fur

---

## STEP 4: ASSEMBLE IN CAPCUT / DAVINCI RESOLVE

* **Project Settings:** Resolution: **1920 x 1080 (16:9 Widescreen)** | Frame Rate: **24 fps**.

### Timeline Track Layout:
```
[V1] Video Clips: Shot 01 ──► Shot 02 ──► ... ──► Shot 12
[A1] Voice Dialogue: Barnaby, Bao, Leo, Pip, Human
[A2] Sound Effects: Chops, Gulp, Tube Thwump, Clock, Cork Pop, Pat-Pat
[A3] Background Music: Upbeat Pizzicato Strings (Scenes 1-4) ──► Sudden Mute (Group Freeze) ──► Warm Acoustic Guitar (Scene 5) ──► Cozy Piano Outro (Scene 6)
```

### Critical Editing Rules for EP-004:
1. **The 1.5-Second GROUP Freeze (Shot 8):**
   - At timestamp 1:35, split clip 8 at the exact moment Barnaby, Pip, and Rocco look forward.
   - Insert a **Freeze Frame of exactly 1.5 seconds (36 frames at 24fps)**.
   - **MUTE ALL MUSIC AND AMBIENCE.**
   - Add ONLY three isolated, deadpan clock ticks: *TICK... TOCK... TICK.*
   - Immediately resume rapid panic music when the freeze breaks.
2. **The Cheek-Stuffing Climb (Shot 9):**
   - Keep the comedic rhythm rolling as Barnaby scales Bao's belly.
   - Add a subtle comedic squeak on every step.
   - Insert a crisp, audible *SNAP!* right when Barnaby adjusts his bowtie mid-air.
3. **The Champagne Cork Pop (Shot 10):**
   - Cut sharply from the belly laughing vibrations to the sudden high-velocity shot of Bao popping out.
   - Pair with the loudest, punchiest *CORK-POP* sound effect.
4. **The Sincerity Beat (Shot 11):**
   - Let silence linger for 2 seconds after the cookie is offered.
   - Fade in soft, fingerpicked acoustic guitar when Barnaby smiles.

### Final Export:
* File Name: `output/EP-004_MASTER.mp4`
* Format: MP4 (H.264), 1080p, 24fps, Audio AAC 320kbps.
