# Automation — Production Pipeline Scripts

> **Purpose:** Python scripts and automation tools that accelerate the production pipeline.

## Planned Automation

| Script | Purpose | Pipeline Stage |
| :--- | :--- | :--- |
| `batch_render.py` | Batch AI image generation with locked prompts | Stage 5: Asset Generation |
| `color_audit.py` | Automated hex color validation against locked palettes | Stage 10: QA Audit |
| `rename_assets.py` | Bulk rename outputs to studio naming convention | Stage 5–6 |
| `subtitle_gen.py` | Auto-generate 3 SRT tracks from script | Stage 12: Upload |
| `analytics_pull.py` | Pull YouTube Studio metrics for retrospective | Stage 13: Analytics |
| `prompt_regression.py` | Test 10 master prompts against new AI model versions | QA / Pipeline Maintenance |

## Standards

- All scripts follow `standards/Coding_Standard.md`
- Scripts must include docstrings and usage examples
- Use Python 3.10+ with type hints
