---
name: magic-hour-campaign-kit
description: Create a coordinated Magic Hour image set from one approved reference for multiple placements, such as a website hero, square product card, and vertical social creative. Use when the user explicitly requests Magic Hour campaign variants or a matching asset set. Not for one isolated image or an unrelated collection.
license: MIT
metadata:
  author: magichourhq
  version: "1.0.0"
---

# Magic Hour campaign kit

Produce a consistent set that fits its placements. Multiple attractive images do not make a usable kit if the product changes between them or the site's copy covers it.

## Define the set before spending

Use the requested placements, not a default batch. For each, record aspect ratio, subject position and scale, copy area, background, and file dimensions. Read the user's actual layout or template when available; do not invent universal social safe-area dimensions.

| Example placement | Composition | Must stay clear |
| --- | --- | --- |
| Wide website hero | Complete product on the right | Left third for heading and CTA |
| Square catalog card | Complete product centered, clean background | Breathing room at every edge |
| Vertical social creative | Product below the upper copy area | Requested headline and platform-overlay regions |

Lock common identity: source image, shape, proportions, materials, colors, cap, logo, and exact label. Distinguish that from deliberate setting and layout changes. Different backgrounds must not accidentally create different products.

## Approve one reference, then branch from it

Inspect the reference. If none exists, generate one with `ai_image_generator_create_image`; use `ai_image_editor_create_image` for changes to an existing source. Solve identity and text before expanding the set. When the user delegates creative decisions, perform the quality check yourself; require their approval only if requested.

Create each placement directly from the same approved reference. Do not make the vertical image from the square image and then the hero from the vertical image: each edit can inherit unnoticed drift. Reuse an accepted variant only for minor repair after identity review. A seed, if exposed, is not an identity lock.

Crop locally when that preserves the full subject and copy area; otherwise edit/reframe with the reference. Do not stretch a wide image into a vertical file. Keep exact headline and CTA copy in a layout layer when a suitable tool is available. Never invent offers, claims, or endorsements.

For each prompt, state the placement-specific change first, then common identity constraints:

> Reframe this reference as a 9:16 vertical product creative. Keep the whole bottle in the lower half, with the upper third dark and uncluttered for copy. Preserve the reference camera angle, blue glass, cap dimensions, silhouette, and one exact “AURORA” label. Retain the wet-stone setting and violet/cyan lighting. No new objects or text.

## Generate the minimum set

Use the existing creation MCP at `https://mcp.magichour.ai/`; [connection guide](https://github.com/magichourhq/magic-hour-mcp/blob/main/user.md). The docs MCP only searches documentation. For API fallback, keep credentials outside chat/source code and read the [live OpenAPI](https://docs.magichour.ai/api-reference/openapi.json).

Check model, aspect ratio, resolution, reference limits, and per-output costs. Confirm the total set fits the authorized budget before the first variant, including source-generation or repair allowance. Do not buy credits or upgrade. Do not generate a collage when separate deliverables were requested. Different placement prompts normally require separate jobs; `image_count` does not assign a different prompt to each image.

For local inputs, obtain a presigned URL with `video_assets_generate_presigned_url`, PUT raw bytes without the API bearer token, verify success, and pass its `file_path`. Create one intended generator/editor job at a time. Save each ID alongside its placement; use `wait_for_image_project`. On the API, use `POST /v1/ai-image-generator` or `/v1/ai-image-editor`, then `GET /v1/image-projects/{id}`. Recover the same job after a wait timeout; never repeat an ambiguous creation request automatically.

Inspect the first variant before continuing so a broken prompt pattern does not consume the budget. If it passes, create remaining requested placements within the existing authorization. Choose resolution for the actual use: a small preview is not a finished high-resolution campaign asset.

## Review together and hand off

Compare every variant with the original and each other. Verify downloaded dimensions, not just the requested ratio. If a model ignores it, crop only when the complete subject and copy area survive; otherwise choose a supported reframing/model route within budget. Check readable label text; cap, proportions, material, and color; full-subject crop; copy area; and intentional lighting differences. A consistent misspelling is still a failure. Repair only failed placements, starting from the original when identity changed.

For a requested animated variant, use its approved still as the image-to-video input and prompt mainly for motion. Keep the copy area clear throughout. Do not animate every placement unless requested and budgeted. If the image-to-video skill is installed, use it; otherwise consult the live schema, submit once, wait for that video ID, and inspect the full clip before delivery.

Deliver individual files with placement names and a concise mapping of placement, dimensions, project ID, and defects. Preserve exact signed URLs; retrieve the same project if its link expires. Save durable files for application use. Show the set together when possible. Report rejected variants separately rather than counting every completed job as an accepted asset.
