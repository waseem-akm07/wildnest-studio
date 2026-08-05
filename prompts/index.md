# Prompts — Master Prompt Library

> **Purpose:** Centralized library of reusable AI prompt templates organized by generation type and AI platform.

Prompts are treated as **production code** — versioned, tested, and archived. A well-crafted prompt template is a permanent production asset.

## Subdirectories

| Folder | What Goes Here |
| :--- | :--- |
| `Image/` | Image generation prompts (character renders, environments, props) |
| `Video/` | Video generation prompts (animation clips, motion sequences) |
| `Voice/` | Voice synthesis prompts (character dialogue, non-verbal sounds) |
| `Thumbnail/` | Thumbnail generation prompts (YouTube cover art) |
| `ChatGPT/` | ChatGPT-optimized prompts (scripting, brainstorming) |
| `Claude/` | Claude-optimized prompts (long-form writing, analysis) |
| `Gemini/` | Gemini-optimized prompts (multimodal, research) |

## Active Production Prompts

Active sprint prompts live in `production/current/[PROD-ID]/prompts/` during the sprint, then graduate to this library once approved.

**Currently active:** `production/current/CHR-001/prompts/` — Barnaby turnaround prompt package.

## Prompt Naming Convention

```
[PROD_ID]_PROMPT_[MODEL]_V[VER].txt
Example: CHR-001_PROMPT_FLUX_V01.txt
Example: EP-001_PROMPT_VEO_V01.txt
```
