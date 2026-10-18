# Four creative workflows you can run with your agent

Use the bundled fictional assets to learn the workflow, or replace them with your own authorized inputs. You do not need to generate a new portrait, recording or source performance just to try a downstream edit.

**Status:** request fields checked against the exposed creation MCP on October 17, 2026. These are current request recipes, not new generation results. The [September output case](README.md) records the actual outputs, all charged credits and failed criteria. Model changes mean these requests will not reproduce those files exactly. Captions below remain an unvalidated finishing recipe.

## Start once

Ask your connected agent:

> Use one recipe below. Inspect its source media and current tool schema. Reuse my existing connection and spending limit, or ask for a limit before generating. Handle every supported step through a downloaded, reviewed file. Save each project ID before continuing; do not regenerate a job to recover a timeout or failed download. Show the result and any unmet requirement.

Tool names may have a client prefix. These JSON bodies are arguments to the named MCP tool, not messages to send as plain chat. The fixed public URLs return the original demo assets at one repository commit; a GitHub `blob` page is not a media URL. For your own local files, call `video_assets_generate_presigned_url` with the actual media type and extension, PUT raw bytes to its returned `upload_url` without the API token, then substitute its `file_path`. A presigned URL allocation alone does not upload the bytes.

Read `account_retrieve` and the live tool's eligibility guidance before spending. The explicit image-edit and video settings below are supported Free-compatible starting settings as checked on the date above; they are not permission to downgrade a requested quality target or a claim that all downstream operations are free. Include every chosen operation, captions and any authorized retry in the total budget. No prices or completion-time guarantees are implied.

For every creation: retain `id`, call the matching `wait_for_image_project` or `wait_for_video_project`, and continue only after `complete`. Save the exact returned download URL and durable local file. If a wait times out, resume that same ID. If a signed URL expires, retrieve the existing project for a fresh one. Keep API credentials off storage upload/download requests.

## 1. Portrait → impossible world → motion

**Ask:** “Put me in a midnight station with floating golden fish. Keep me recognizable. Make the fish pass behind me, hold the ending, and deliver a short vertical video.”

**Why two steps:** fix identity and composition in a still before paying for motion. Skip the edit when the supplied still already satisfies the brief.

Call `ai_image_editor_create_image`:

```json
{
  "assets": {
    "image_file_paths": [
      "https://raw.githubusercontent.com/magichourhq/skills/08b68fb070130364c75100f22d14481655a6e79b/examples/midnight-remix/portrait.png"
    ]
  },
  "model": "flux-2-klein",
  "resolution": "640px",
  "image_count": 1,
  "aspect_ratio": "9:16",
  "style": {
    "prompt": "Keep the same woman, face, blunt bob and amber raincoat. Place her on a midnight train platform with golden fish floating behind her in the air. One person only, medium shot, face unobstructed, teal station lights, no writing. Leave space around the head and shoulders for a vertical video."
  }
}
```

Wait for the image, download it and inspect the face, outfit, fish and crop. When creative review is delegated, accept it yourself if it meets the brief. Respect a requested user review point. Correct the still before motion if it fails.

Call `image_to_video_create_video` with that accepted image. **Replace `assets.image_file_path` below with the accepted edit's fresh raw download URL or its uploaded file path.** The included URL is the existing demonstrated keyframe, so you can also skip the image-edit call and animate that input directly:

```json
{
  "assets": {
    "image_file_path": "https://raw.githubusercontent.com/magichourhq/skills/08b68fb070130364c75100f22d14481655a6e79b/examples/midnight-remix/keyframe.png"
  },
  "model": "ltx-2.5",
  "resolution": "480p",
  "end_seconds": 5,
  "audio": false,
  "style": {
    "prompt": "A golden fish glides slowly behind the woman's shoulder. She notices it with a small smile and a slight eye movement. Locked camera, one continuous shot. Keep her face and outfit unchanged. Let the fish remain visible and hold the final composition; no fade or cut."
  }
}
```

Wait for the video. Watch the whole clip for identity drift, extra turns, surprise cuts and the ending. Probe the file's actual dimensions; do not assume the requested ratio was honored. Deliver the clean clip and accepted still.

**Second edit:** change only the crop or trim an unwanted ending locally from accepted footage when that satisfies the brief. Do not buy another generation for a new filename or export size. If the motion itself fails, explain the miss and revise only within the remaining authorized budget.

**Existing evidence:** [keyframe](keyframe.png), [performance](performance.mp4) and [vertical export](remix.mp4). The historical take turns farther than requested; it is not an exact motion-control pass.

## 2. Accepted performance → a different face

**Ask:** “Use this other face in the accepted scene. Keep the performance, clothes and setting.”

Reuse the bundled performance and alternate fictional face. Call `face_swap_create_video`:

```json
{
  "assets": {
    "video_source": "file",
    "video_file_path": "https://raw.githubusercontent.com/magichourhq/skills/08b68fb070130364c75100f22d14481655a6e79b/examples/midnight-remix/performance.mp4",
    "face_swap_mode": "all-faces",
    "image_file_path": "https://raw.githubusercontent.com/magichourhq/skills/08b68fb070130364c75100f22d14481655a6e79b/examples/midnight-remix/alternate-face.png"
  },
  "start_seconds": 0,
  "end_seconds": 5,
  "style": {
    "version": "default"
  }
}
```

This example has one subject. **Do not use `all-faces` on a group scene when only one person should change.** For that request, detect the actual faces, inspect the detection result and use `individual-faces` with the intended `face_mappings`; never invent an original-face path.

Wait, download and review the face through head turns, the opening and ending, hairline blending and unintended changes elsewhere. Face Swap changes the face; use Character Replace when the whole character or costume must change.

**Second edit:** swap a different authorized face into the same original performance, not into the previous swapped result. Reuse the action and setting. Preserve the clean original and each accepted identity version separately.

**Existing evidence:** [face-swapped clip](face-swap.mp4). The actual output shrank in dimensions; profile likeness and temporal blending still need full-speed review. No multi-person video tracking result is claimed.

## 3. Portrait + accepted recording → talking character

**Ask:** “Make this portrait deliver my announcement. Keep the full sentence, then add captions if they fit my budget.”

Call `ai_talking_photo_create_talking_photo` using the original demo recording “Welcome aboard. The next stop is the moon.”:

```json
{
  "assets": {
    "image_file_path": "https://raw.githubusercontent.com/magichourhq/skills/08b68fb070130364c75100f22d14481655a6e79b/examples/midnight-remix/keyframe.png",
    "audio_file_path": "https://raw.githubusercontent.com/magichourhq/skills/08b68fb070130364c75100f22d14481655a6e79b/examples/midnight-remix/speech.wav"
  },
  "start_seconds": 0,
  "end_seconds": 3.920042,
  "style": {
    "generation_mode": "realistic"
  }
}
```

The interval is the measured demo audio duration, not a generic announcement length. Measure your replacement recording and select the full spoken interval within the current mode limit. **Text alone is not an input to Talking Photo.** If no approved recording exists and no authorized speech-generation route is available, request that one missing input; do not invent a voice tool or silently change the voice.

Wait, download, watch and listen through the final word. Check pronunciation, mouth timing after pauses, face stability and audio continuity. If listening is unavailable, deliver with that review explicitly unverified.

**Second edit:** keep the accepted recording when changing the portrait. Keep the clean talking clip when changing captions. A new recording changes the performance and requires the appropriate new video job; a caption change does not require recreating the talking head.

**Existing evidence:** [talking clip](talking-photo.mp4) and [recording](speech.wav). Historical stream/frame checks do not establish audible pronunciation or synchronization.

## 4. Existing footage + replacement recording → dialogue remix

**Ask:** “Use this recording as the dialogue in my existing clip. Keep the scene and action.”

Call `lip_sync_create_video`:

```json
{
  "assets": {
    "video_source": "file",
    "video_file_path": "https://raw.githubusercontent.com/magichourhq/skills/08b68fb070130364c75100f22d14481655a6e79b/examples/midnight-remix/performance.mp4",
    "audio_file_path": "https://raw.githubusercontent.com/magichourhq/skills/08b68fb070130364c75100f22d14481655a6e79b/examples/midnight-remix/speech.wav"
  },
  "start_seconds": 0,
  "end_seconds": 3.920042,
  "max_fps_limit": 24,
  "style": {
    "generation_mode": "lite"
  }
}
```

Use `lite` here because the source performance is not a speaking take. The live schema requires visible mouth movement in the opening seconds for `standard` and `pro`; do not select them blindly as “higher quality.” For a still portrait—even one saved as a static video—use Talking Photo instead.

Your replacement audio and source clip must cover the chosen interval. Do not loop a face or cut the last word to hide insufficient footage. Wait, download, and watch with sound for alignment, pauses, teeth/jaw artifacts and the last word.

**Second edit:** reuse the original source performance and the newly approved recording. Avoid repeatedly lip-syncing an already modified output when the original remains available. Save the full clean master before captions.

**Existing evidence:** [historical Lip Sync output](lip-sync.mp4) used `standard`, not this recipe's `lite`. Its video stream was slightly shorter than the audio, and listening review remains outstanding. This request corrects mode selection; no new output-quality result is claimed.

## Add captions to an accepted spoken clip

Use `auto_subtitle_generator_create_video` only when requested and budgeted. Keep the clean master. Supply the accepted talking/Lip Sync clip's fresh exact raw download URL or uploaded `file_path` as `assets.video_file_path`, `start_seconds: 0`, the measured complete spoken interval as `end_seconds`, and `style: {"template": "minimalist"}`. A template or valid custom configuration is required; an empty `style` is not enough.

Wait and save the captioned file separately. Check every name/number against the recording, readable placement and the final word. Do not promise an editable transcript or SRT unless the tool actually returns one. This caption step has no published output validation in the original case.

[Install and connect](../../docs/quickstart.md) · [All historical requests and costs](requests.json) · [Review before delivery](../../skills/ai-media-quality-review)
