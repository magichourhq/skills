---
name: magic-hour-talking-media
description: Create and quality-check Magic Hour talking-photo or lip-sync video from authorized portrait, video, and audio inputs. Use when the user explicitly asks Magic Hour to animate a portrait speaking or replace the speech performance in an existing video. Generic avatar requests do not activate this skill.
license: MIT
metadata:
  author: magichourhq
  version: "1.0.0"
---

# Magic Hour talking media

Create a stable speaking performance with intelligible audio and believable mouth timing. A created project is incomplete until it finishes, its media is retrievable, and the result has been inspected.

Generation consumes Magic Hour credits. Use a connected Magic Hour creation MCP at `https://mcp.magichour.ai/` when available. Otherwise read `references/setup.md`. Inspect the live tool schemas before choosing a mode, duration, resolution, or cost.

## Choose the workflow

- Use `ai_talking_photo_create_talking_photo` when the input is a still portrait plus speech audio.
- Use `lip_sync_create_video` when the input is an existing video whose mouth movement should match replacement audio.
- If the user has a script but no audio, create or obtain the approved voice track first. Do not infer permission to clone a real person's voice.

Do not turn a still into a generic image-to-video clip when the goal is speech synchronization. Do not use Talking Photo when the user needs to preserve motion from an existing performance.

## Prepare inputs

Use face and voice media the user is entitled to use. A public URL alone does not establish consent or ownership.

For a portrait, prefer one visible, front-facing face with open eyes, a neutral closed mouth, even lighting, and enough space around the head and shoulders. Avoid occluded mouths, extreme profile angles, tiny faces, heavy motion blur, or text crossing the face.

For lip sync, prefer a stable face track with the mouth visible. Trim long dead sections before generation when the user authorizes it. The audio should contain the final performance: remove leading silence, check speech is intelligible, and avoid clipping or music that overwhelms the voice.

Set `start_seconds` and `end_seconds` to the intended audio or video segment, with end greater than start and within the current mode limits. For Talking Photo, use the live schema's reliable likeness-preserving mode unless the user explicitly wants prompt-guided motion. For Lip Sync, use the live default for a general request and choose a higher-fidelity mode only when the current schema, plan, and authorized budget support it.

Local files must be uploaded before tool use. Follow `references/setup.md`; never pass a local filesystem path as a Magic Hour hosted path.

## Create and wait

Submit one creation request and immediately retain the returned project ID. Do not enable automatic retries on the creation call. If it times out before returning an ID, reconcile through available project history instead of blindly spending credits again.

Call `wait_for_video_project` with that ID. A polling timeout means the existing job may still be running. Continue retrieval of the same project; never start a replacement job merely to recover polling.

When the project reports `complete`, use its exact signed download URL with every query parameter intact. Retrieve the same project again if the link expired.

## Inspect and deliver

Preview the whole clip with audio. Check:

- words begin and end at the intended timestamps
- mouth shapes align with consonants and closures rather than merely moving continuously
- identity, eyes, teeth, jawline, hair, and background remain stable
- head motion and expression feel intentional and do not jitter
- audio is intelligible, continuous, correctly paced, and free of clipping
- the video does not freeze, warp, or collapse at the final frames

If the result fails, isolate the cause. Improve or trim audio for timing and silence problems; choose a clearer portrait or video segment for occlusion and tracking problems; change the generation mode only when it addresses the observed failure. Change one useful variable per retry and stay inside the authorized credit budget.

Return the finished video or usable link, its saved location when applicable, the project ID, the mode and time range used, and any material limitation.
