---
name: magic-hour-video-editing
description: Edit or repurpose existing footage with Magic Hour, choosing between generative visual edits, subtitles, and precise local trim, crop or composition. Use for a source video that needs changes or social versions, not a new video from scratch.
license: MIT
metadata:
  author: magichourhq
  version: "1.0.0"
---

# Magic Hour video editing

Keep the footage the user already likes. Choose the operation that changes the requested property without unnecessarily regenerating motion, identity or speech.

## Inspect before choosing

Read the source's actual duration, dimensions, frame rate and audio streams. Watch the relevant interval. Record the requested change and what must survive: subject identity, actions, timing, dialogue, original sound, frame shape or a specific object. A short clip with several cuts may need separate edits; do not assume the model maintains continuity through every cut.

| Requested change | Operation |
| --- | --- |
| Change scene appearance, materials or visual style | `ai_video_editor_create_video` using the original footage |
| Add speech captions | `auto_subtitle_generator_create_video` after picture edits |
| Trim, resize, reframe, add exact copy/logo, or assemble | Available compositor such as FFmpeg or an existing video editor |
| Change a visible speaker's speech | Lip-sync route, not a generic visual-edit prompt |

Do not use a generative edit to perform a lossless requirement. It can redraw unrequested regions and does not guarantee pixel-preserved backgrounds, logos or faces. Do not claim tracking, masks or object-isolated controls unless the chosen tool exposes them.

## Apply one purposeful edit

Select an interval within the current model's minimum and maximum length. Describe the visual change, then protected action and camera behavior:

> Change only the room's appearance to a warm, sunlit illustration. Preserve the person's action of placing the cup on the table, the camera position, shot timing, cup count and framing. No cuts, new characters or added text.

That prompt is a requested constraint, not a guarantee. Inspect cup contact, hands, occlusion, faces and cuts in the output. If the model changes required action or identity, return to the original source and narrow the change or choose a live-supported alternative within budget. Do not chain unreviewed edited clips.

For a vertical version, check the entire motion path before cropping. If a tracked subject or important context will leave the crop, use a designed contained layout when the brief permits, or use an editor that actually supports the required tracking. Do not stretch, invent missing edge content, or assume one crop works across camera cuts.

## Preserve audio and caption last

Verify whether the edited output retains the desired audio; do not infer it from a successful video job. Keep the source master, choose the intended soundtrack explicitly, and align any replacement to the exact edited interval. Never use `-shortest` blindly when it could cut off speech. Check the first and last audible words.

Apply subtitles to the final cut so timing and coordinates refer to the delivered picture. Check the live style template/custom fields. Inspect names, numbers, language support, line breaks and platform overlays. If editable caption text is required but the API only returns a rendered video, use a suitable local caption workflow or report the missing deliverable.

## Execute and hand off

Use the creation MCP at `https://mcp.magichour.ai/`; [setup](https://github.com/magichourhq/magic-hour-mcp/blob/main/user.md). For API use, consult the [OpenAPI](https://docs.magichour.ai/api-reference/openapi.json): `/v1/ai-video-editor`, `/v1/auto-subtitle-generator`, and `GET /v1/video-projects/{id}`. Respect current models, intervals, resolution, tier and the total authorized cost.

For local footage, obtain `video_assets_generate_presigned_url`, PUT raw bytes to `upload_url` without the API bearer token, then use `file_path`. Submit once, retain the ID and `wait_for_video_project`. Resume the same job after a wait timeout; do not repeat an ambiguous creation. Preserve signed URLs exactly and download durable files.

Decode the final export, verify its actual dimensions/duration/audio, and inspect full playback including transitions. Compare against the original, not just the last intermediate. Deliver the clean master, requested derivatives, edit decisions and unresolved defects. Reuse accepted edits for future crops/copy changes; regenerate only when the visual brief changes. Generative edits and caption quality are schema-reviewed but not yet validated in a published authenticated run.
