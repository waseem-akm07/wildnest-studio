# Voice Prompts — AI Voice Synthesis Templates

> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** [Studio README](file:///e:/Animation/wildnest-studio/README.md) ──► [Voice/](file:///e:/Animation/wildnest-studio/prompts/Voice/index.md) ──► `index.md`  
> 🎯 **Canonical Source:** [WPOS-001 AI Production Pipeline OS](file:///e:/Animation/wildnest-studio/docs/09_Production/01_AI_Production_Pipeline.md)  
> 📜 **Governing Standard:** [STD-PROMPT-001 Prompt Standard](file:///e:/Animation/wildnest-studio/standards/Prompt_Standard.md)  

---


> **Purpose:** Reusable prompt templates for generating character dialogue and non-verbal vocalizations.

## Primary Tool

| Tool | Use Case |
| :--- | :--- |
| ElevenLabs Professional | Primary character voice synthesis |
| Bark (Open Source) | Fallback for cost optimization |
| Local Chatterbox TTS | Offline fallback |

## Voice Profile Requirements (from BRAND-001)

- **Barnaby:** Crisp, formal, overly polite Hinglish; fast-paced, squeaks when panicked
- **Pip:** Hyperactive, raspy, breathless 3-word Hinglish bursts
- **Non-verbal sounds:** Each character needs 8 locked sounds (squeak, gasp, groan, chirp, hum, grunt, sigh, giggle)
- Non-verbal sounds remain **identical across all global dubs**

## Language Rules

- Natural Hinglish (75% Hindi grammar + 25% English loanwords)
- **8-word maximum** per spoken line
- Conversational warmth — never formal "kid-vid" announcer voice