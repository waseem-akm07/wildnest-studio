# Production — Active Production Workspace

> **Purpose:** All active sprint work happens here. This is the operational workspace for current production.

## Structure

```
production/
├── Workflow.md              ◄── WSPW-001: Daily Operational Playbook (14-stage chain)
└── current/                 ◄── Active sprint folders
    └── CHR-001/             ◄── Barnaby character production sprint (Phase 1)
        ├── 00_Brief.md      ◄── Production brief (PROD-CHR-001)
        └── prompts/         ◄── Master prompt manifests
```

## How It Works

1. Each active sprint gets a folder under `current/` named by production ID.
2. When a sprint is completed, approved assets move to `assets/` and the sprint folder is archived.
3. Follow the standard sprint folder structure:

```
production/current/[PROD-ID]/
├── 00_Brief.md       ◄── Production brief (goals, specs, exit criteria)
├── prompts/          ◄── AI prompt manifests
├── outputs/          ◄── Raw AI generations (unedited)
├── review/           ◄── Selected candidates + QA feedback
└── final/            ◄── Approved, locked assets ONLY
```

## References

- Daily operational playbook: `production/Workflow.md` (WSPW-001)
- Pipeline architecture: `docs/09_Production/01_AI_Production_Pipeline.md` (WPOS-001)
- MVP execution roadmap: `docs/09_Production/WildNest_MVP_Roadmap.md` (WPOS-MVP-001)
