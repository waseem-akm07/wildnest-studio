# WildNest Studio Naming Conventions Standard

> **Document ID:** STD-NAMING-001  
> **Version:** 1.0  
> **Status:** Mandatory Studio Standard  
> **Owner:** Studio Technical Director & Pipeline Architect  

---

## 1. Overview

This document specifies the mandatory naming conventions across all digital assets, production files, canonical documentation, prompts, code scripts, and rendered media inside **WildNest Studio**. Strict adherence to these conventions prevents asset drift, ensures automated pipeline compatibility, and enables seamless asset discovery.

---

## 2. General Rules

- **Use UPPERCASE for Document & Asset Type Prefixes** (e.g., `PRD-`, `UNI-`, `CHR-`, `EP-`, `WPOS-`).
- **Use Snake_Case or PascalCase for Script & File Names** as specified per domain below.
- **Never use spaces, special characters, or accented letters** in file names. Use underscores (`_`) or hyphens (`-`).
- **Always include versioning tags** (`_V01`, `_V02`) on generated media assets and prompt packages.

---

## 3. Asset & File Naming Formats

### 3.1 Character & Environment Assets (`assets/`)

```
ASSET TYPE              SYNTAX FORMAT                                  EXAMPLE
──────────────────────  ────────────────────────────────────────────── ─────────────────────────────────
Character Turnaround    [CHR_ID]_[VIEW]_[VERSION].[ext]                CHR-001_FRONT_V01.png
Character Expression    [CHR_ID]_EXP_[EMOTION]_[VERSION].[ext]         CHR-001_EXP_PANIC_V01.png
Environment Set         ENV-[NAME]_[ANGLE]_[VERSION].[ext]             ENV-LOBBY_ANGLE01_V01.png
Environment Lighting    ENV-[NAME]_[LIGHTING]_[VERSION].[ext]          ENV-LOBBY_GOLDENHOUR_V01.png
Prop Asset              PROP-[NAME]_[VARIANT]_[VERSION].[ext]          PROP-THIMBLE_CUP_V01.png
```

### 3.2 Media & Audio Stems (`assets/Music/`, `assets/SFX/`)

```
ASSET TYPE              SYNTAX FORMAT                                  EXAMPLE
──────────────────────  ────────────────────────────────────────────── ─────────────────────────────────
Voice Stem              VOICE_[CHAR]_[LINE_ID]_[LANG].[ext]            VOICE_BARNABY_L01_HINGLISH.wav
Non-Verbal Soundbank    SFX_VOCAL_[CHAR]_[SOUND_TYPE]_[VER].[ext]       SFX_VOCAL_BARNABY_SQUEAK_V01.wav
Foley Sound Effect      SFX_FOLEY_[CATEGORY]_[NAME]_[VER].[ext]        SFX_FOLEY_TUBE_THWIP_V01.wav
Music Track             MUSIC_[MOOD]_[BPM]BPM_V[VER].[ext]             MUSIC_TENSION_135BPM_V01.wav
```

### 3.3 Production Sprint & Episode Files (`episodes/`, `production/`)

```
FILE TYPE               SYNTAX FORMAT                                  EXAMPLE
──────────────────────  ────────────────────────────────────────────── ─────────────────────────────────
Episode Folder          episodes/EP-[XXX]/                             episodes/EP-001/
Episode Brief           episodes/EP-[XXX]/00_Episode_Brief.md          episodes/EP-001/00_Episode_Brief.md
Production Sprint Dir   production/current/[PROD-ID]/                  production/current/CHR-001/
Master Script           [PROD_ID]_01_Script_V[VER].md                  EP-001_01_Script_V01.md
Timecoded Shotboard     [PROD_ID]_02_Shot_List_V[VER].md               EP-001_02_Shot_List_V01.md
Final Master Render     [PROD_ID]_MASTER_[RES]_[DATE].[ext]            EP-001_MASTER_4K_20260805.mp4
```

### 3.4 Prompt Packages (`prompts/`)

```
PROMPT TYPE             SYNTAX FORMAT                                  EXAMPLE
──────────────────────  ────────────────────────────────────────────── ─────────────────────────────────
Image Prompt Manifest   [PROD_ID]_PROMPT_[MODEL]_V[VER].txt            CHR-001_PROMPT_FLUX_V01.txt
Video Prompt Manifest   [PROD_ID]_PROMPT_[ENGINE]_V[VER].txt           EP-001_PROMPT_VEO_V01.txt
Negative Prompt Pack    [PROD_ID]_NEGATIVE_V[VER].txt                  CHR-001_NEGATIVE_V01.txt
```

---

## 4. Canonical Document IDs

All studio documentation inside `docs/` must bear a standardized Document ID tag in its header metadata:

| Scope | ID Format | Example |
| :--- | :--- | :--- |
| **Vision & Strategy** | `PRD-[XXX]` | `PRD-001` (Master PRD) |
| **Universe & Lore** | `UNI-[XXX]` | `UNI-001` (Critter Haven Resort Bible) |
| **Character System** | `CHR-BIBLE-[XXX]`, `CHR-[XXX]` | `CHR-BIBLE-001`, `CHR-001` (Barnaby Profile) |
| **Story & Scripts** | `SB-[XXX]`, `EP-TEMPLATE-[XXX]` | `SB-001` (Master Story Bible) |
| **Art & Style** | `ART-[XXX]` | `ART-001` (Visual Style Guide) |
| **Brand & Localization** | `BRAND-[XXX]` | `BRAND-001` (Language Strategy) |
| **Production Operating System** | `WPOS-[XXX]`, `WSPW-[XXX]` | `WPOS-001`, `WSPW-001` (Daily Workflow) |
| **Studio Standards** | `STD-[TOPIC]-[XXX]` | `STD-NAMING-001` |

---

## 5. Compliance & Enforcement

Any asset or file that does not adhere to these naming conventions will fail **Gate 3 (Visual & Asset Consistency)** during the 8-Gate QA audit and must be renamed before being committed to `assets/` or `docs/`.
