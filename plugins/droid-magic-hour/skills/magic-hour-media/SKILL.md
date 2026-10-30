---
name: magic-hour-media
description: Create or edit images and video, generate music, or recover an existing Magic Hour media project when the user requests media work.
---

# Magic Hour media

Discover the connected Magic Hour tools and their current schemas. Use `workflow_guide_retrieve` for task-specific inputs and workflow guidance. If authentication is needed, use Droid's `/mcp` browser authorization flow; never ask for an API key or OAuth token in chat.

Use `account_retrieve` to verify account access and available credits before a paid request. Tool discovery alone does not prove authorization. Match the user's requested media, model, duration, resolution and source assets to the current schema and account eligibility. Use a matching estimate when available; otherwise explain that a quote is unavailable and obtain an explicit credit budget before generation. Estimates do not authorize spending.

Use only source media the user owns or is authorized to use. Upload local bytes through a supported upload mechanism before passing its returned file path. If the environment cannot transfer a file, report that limitation and request a supported source input.

Submit an authorized creation once and retain the accepted project ID. Wait or retrieve that same ID until the actual terminal status is known. After a timeout or uncertain acceptance, recover the existing job before considering another paid request. Do not regenerate automatically.

Return the actual completed output or exact download URL, preserving its signed query parameters. Report failures and content mismatches accurately. Reusing an existing project does not authorize creating, deleting or changing it.
