# Video Prompts — AI Video Generation Templates

> **Purpose:** Reusable prompt templates for generating animated video clips from static renders.

## Primary Tools

| Tool | Use Case |
| :--- | :--- |
| Google Veo | Primary video generation (character animation from reference frames) |
| Runway Gen-3 | Secondary video generation with ControlNet motion guidance |
| Luma Dream Machine | Backup for smooth camera motion sequences |

## Key Requirements

- **24fps** progressive output
- **ControlNet pose keyframing** to maintain character consistency
- **1.5-second reaction holds** must be achievable (36 frozen frames)
- Zero AI melting/warping artifacts in final output
- Character must match LoRA-locked geometry from turnaround sheets
