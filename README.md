# WildNest Studio

> **AI-generated animated videos for YouTube.**

WildNest Studio creates original animated content using AI tools. Our flagship series is **Critter Haven Resort** — a secret 5-star luxury pet resort hidden inside a plastic hamster cage, where tiny pets live like royalty when their humans leave home.

---

## How to Make a Video

The workflow is simple:

```
1. WRITE THE SCRIPT  →  2. GENERATE THE VIDEO  →  3. UPLOAD TO YOUTUBE
```

### Step-by-Step

1. **Come up with an episode idea** — Use the story engine: `[New Guest] + [Problem] + [5PM Deadline] = Episode`
2. **Write the concept** — Copy `scripts/_template/` folder, select characters from the pre-loaded cast table in `concept.md`
3. **Write the script** — Fill in `script.md` using Hinglish dialogue rules (max 8 words/line) & physical comedy beats
4. **Create the shot list** — Break the script into individual shots with AI prompts and audio stems in `shot-list.md`
5. **Generate images** — Use prompts from `prompts/image-prompts.md` to create character & scene images
6. **Generate video clips** — Use prompts from `prompts/video-prompts.md` to animate scenes (including 1.5s reaction freezes)
7. **Generate voice & audio** — Use prompts from `prompts/voice-prompts.md` for Hinglish TTS & non-verbal squeak banks
8. **Edit everything together** — Assemble clips, audio, and music in DaVinci Resolve (free) or CapCut
9. **Create thumbnail** — Use `prompts/thumbnail-prompts.md` (3-Element CTR Rule)
10. **Upload to YouTube** — Add 3 subtitle tracks (Hinglish, Hindi, English)

---

## AI Tools We Use

| What | Free Option | Paid Option |
|:---|:---|:---|
| **Script Writing** | DeepSeek V3 / Ollama | Claude / GPT-4o |
| **Image Generation** | ComfyUI + Flux/SDXL / Leonardo Free | Midjourney / Flux Pro |
| **Video Generation** | Hailuo AI / Kling Free / AnimateDiff | Google Veo / Runway Gen-3 |
| **Voice Generation** | Microsoft Edge-TTS / Coqui TTS | ElevenLabs |
| **Video Editing** | DaVinci Resolve Free / CapCut | DaVinci Resolve Studio |
| **Thumbnails** | Photopea / GIMP / Canva Free | Photoshop |
| **Subtitles** | Whisper AI (local) | Descript |

---

## Folder Structure

```
wildnest-studio/
│
├── README.md                 ← You are here
│
├── bible/                    ← Series creative foundation (read first!)
│   ├── world.md              ← Universe rules, locations, story engine
│   ├── characters.md         ← All character profiles & AI prompts
│   ├── style-guide.md        ← Art style, colors, lighting, camera rules
│   └── story-framework.md    ← 6-Beat structure, comedy rules, formats
│
├── scripts/                  ← Episode scripts (your main work folder)
│   ├── _template/            ← Copy this for each new episode (pre-loaded with cast & Hinglish rules)
│   │   ├── concept.md
│   │   ├── script.md
│   │   └── shot-list.md
│   └── EP-001/               ← First episode: "The Grand Opening Chaos"
│       ├── concept.md
│       ├── script.md
│       └── shot-list.md
│
├── prompts/                  ← AI prompts (copy-paste ready)
│   ├── image-prompts.md
│   ├── video-prompts.md
│   ├── voice-prompts.md
│   └── thumbnail-prompts.md
│
├── assets/                   ← Generated images, music, sound effects
│   ├── characters/
│   ├── backgrounds/
│   ├── music/
│   └── sfx/
│
├── output/                   ← Final rendered videos ready for upload
│
└── _archive/                 ← Old files (kept for reference, safe to ignore)
```

---

## The Series — Critter Haven Resort

A secret pet resort operates inside a plastic hamster cage. The human leaves at 8 AM, the resort opens. At 5 PM the human returns, everything must be back to normal.

**The cast (pre-loaded in templates):**

| Character | Species | Role | Personality |
|:---|:---|:---|:---|
| **Barnaby** | Golden Syrian Hamster | General Manager | Anxious perfectionist with a red twist-tie bowtie |
| **Pip** | Roborovski Dwarf Hamster | Lead Mechanic | Chaotic speed-demon who "fixes" everything too fast |
| **Leo** | African Lion Cub | VIP Guest | Dramatic king in a gold-foil candy wrapper crown |
| **Milo** | Squirrel Monkey | Acrobat | Can't stop pressing buttons and pulling levers |
| **Ollie** | Great Horned Owl Cub | Night-Shift Manager | Sleepy genius with a thimble monocle |
| **Bao** | Giant Panda Cub | Head Chef | Solves everything with snacks and bear hugs |
| **Rocco** | White Rhinoceros Calf | Luggage Handler | Gentle giant who thinks he's a delicate ballerina |

**Read the full details:** [bible/characters.md](file:///e:/Animation/wildnest-studio/bible/characters.md)

---

## Quick Links

- 🌍 [World Bible](file:///e:/Animation/wildnest-studio/bible/world.md) — Universe rules & locations
- 🎭 [Characters](file:///e:/Animation/wildnest-studio/bible/characters.md) — All character profiles & AI prompts
- 🎨 [Style Guide](file:///e:/Animation/wildnest-studio/bible/style-guide.md) — Colors, lighting, camera rules
- 📖 [Story Framework](file:///e:/Animation/wildnest-studio/bible/story-framework.md) — How to structure episodes
- 🎬 [EP-001 Concept](file:///e:/Animation/wildnest-studio/scripts/EP-001/concept.md) — First episode outline
