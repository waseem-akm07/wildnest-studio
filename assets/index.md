# Assets — Reusable Studio Asset Library

> **Purpose:** Centralized storage for all reusable production assets that compound across episodes.

Assets stored here are **production-locked and approved.** Do not place raw AI outputs or work-in-progress files here — those belong in `production/current/`.

## Subdirectories

| Folder | Contents | Naming Format |
| :--- | :--- | :--- |
| `Characters/` | Locked turnarounds, LoRA models, expression sheets | `CHR-XXX_[VIEW]_V[VER].png` |
| `Backgrounds/` | Approved environment renders, camera presets | `ENV-[NAME]_[ANGLE]_V[VER].png` |
| `Logos/` | WildNest brand logos, watermarks, end cards | `LOGO_[VARIANT]_V[VER].png` |
| `Fonts/` | Licensed typography files | `[FontName]_[Weight].ttf` |
| `Music/` | Approved music stems, ambient tracks | `MUSIC_[MOOD]_[BPM]BPM_V[VER].wav` |
| `SFX/` | Sound effects, foley, non-verbal vocal banks | `SFX_[CATEGORY]_[NAME].wav` |
| `References/` | Visual reference boards, mood boards, style targets | `REF_[TOPIC]_[DATE].png` |

## Rules

- Only **CEO-approved, QA-passed** assets belong here.
- All files must follow the studio naming convention (`standards/Naming_Convention.md`).
- Asset reuse target: **>75%** of environments reused per new episode.
