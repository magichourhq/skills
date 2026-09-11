# Midnight remixes: animate, recast and restyle one scene

An original portrait becomes a train platform full of floating koi, then a moving scene. Reuse that performance to change the face, replace the whole character, or turn the footage into an illustration. A separate text-only example opens an elevator onto the moon.

**Run date:** September 11, 2026 UTC. **Method:** authenticated Magic Hour creation MCP. **12 jobs, 1,750 credits charged in total**, including all source images, speech and outputs below. No paid retries or discarded generations. Charges were checked after completion; Face Swap settled at 120 credits after an initial 150-credit estimate. This is a demonstration of the routes, not a controlled comparison against generic MCP use or another service.

## Watch and try it

[![Three generated clips: original performance on the left, changed face in the middle, fox conductor on the right](preview.gif)](remix.mp4)

Left: [animated scene](remix.mp4). Center: [new face](face-swap.mp4). Right: [new character](character-replace.mp4). The preview shows the first five seconds at reduced size and frame rate; inspect the original MP4s below for quality. It does not imply identical gesture timing.

Attach your portrait to a connected agent with the [Image-to-Video skill](../../skills/magic-hour-image-to-video) and ask:

> Put me in a midnight train station with golden fish swimming through the air. Keep my face and clothes. Fix the still with AI Image Editor if needed, inspect it, then animate my reaction and the fish. Choose the shot, work within my budget and deliver a finished vertical video.

Then attach another face or character: “Use this face in the accepted clip,” or “Make this character perform that action.” Reuse the performance rather than buying a new scene. [Install and connect →](../../docs/quickstart.md)

## Inputs and all generation outputs

| Step                                     | Files                                          | Model or mode                                        | Final credits |
| ---------------------------------------- | ---------------------------------------------- | ---------------------------------------------------- | ------------: |
| Original fictional portrait              | [portrait.png](portrait.png)                   | nano-banana-2-lite, 1k, 9:16                         |            50 |
| Change the setting, preserve the person  | [keyframe.png](keyframe.png)                   | nano-banana-2-lite, 1k, 9:16                         |            50 |
| Original alternate identity              | [alternate-face.png](alternate-face.png)       | nano-banana-2-lite, 1k, square                       |            50 |
| Elevator opens onto the moon             | [moon-elevator.mp4](moon-elevator.mp4)         | ltx-2.3, 720p, 5 seconds, silent                     |           240 |
| Animate the accepted koi frame           | [performance.mp4](performance.mp4)             | ltx-2.3, 720p, 5 seconds, silent                     |           240 |
| Original station announcement            | [speech.wav](speech.wav)                       | Voice Generator, GLaDOS preset                       |             5 |
| Replace the face in the performance      | [face-swap.mp4](face-swap.mp4)                 | Face Swap v2, all-faces, 0–5 seconds                 |           120 |
| Animate the portrait to speech           | [talking-photo.mp4](talking-photo.mp4)         | Talking Photo realistic, full audio interval         |           190 |
| Original fox conductor reference         | [character.png](character.png)                 | nano-banana-2-lite, 1k, 9:16                         |            50 |
| Replace the whole performer              | [character-replace.mp4](character-replace.mp4) | Character Replace, replace/auto, 720p, 0–5 seconds   |           480 |
| Restyle the original performance         | [video-edit.mp4](video-edit.mp4)               | Video Editor ltx-2.3, 720p, 0–5 seconds              |           180 |
| Replace speech on the moving performance | [lip-sync.mp4](lip-sync.mp4)                   | Lip Sync standard, 24 fps limit, full audio interval |            95 |

[Exact prompts, input dependencies, settings and project IDs →](requests.json). Each reference is included so reproducing a downstream operation does not require regenerating it. The portrait is fictional; it is not a real customer's likeness. The speech is the original line “Welcome aboard. The next stop is the moon.” using the named synthetic character preset; no endorsement or affiliation is implied.

## What worked, what missed, and what remains unverified

The four images were visually inspected. All original MP4s and the WAV were probed and decoded. The Image-to-Video clip was inspected as an all-frame contact sheet; other operations were reviewed through sampled frames across the clip, with additional boundary checks. These checks are narrower than full-speed playback and listening. No independent preference study or general quality win rate is claimed.

| Operation                   | Observed result                                                                                                                | Failed criterion or remaining check                                                                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image edit → Image-to-Video | The edited woman retains the bob and raincoat in a new environment. The animated subject stays recognizable and the fish move. | She turns farther than requested and looks both ways; the final pose misses the requested calm gaze at the fish. Temporal smoothness is not established by the contact sheet.                       |
| Face Swap                   | The alternate facial features and facial hair appear while the source bob, coat and scene remain.                              | This tests one person and one reference, not multi-person mapping, cuts or difficult hand occlusion. Profile likeness and temporal blending still need full-speed review. Output dimensions shrink. |
| Text-to-Video               | The closed elevator reveals the moon and Earth, with time to read the reveal.                                                  | The model adds unwanted numerals/signage and camera movement despite the prompt. This take is not an exact-constraint pass.                                                                         |
| Talking Photo               | The portrait develops mouth and facial movement; the output includes an audio track spanning the supplied speech interval.     | Pronunciation, audible final word and audio/mouth alignment have not been listened to. File frame rate differs from project metadata.                                                               |
| Character Replace           | The fox's recognizable face, fur and costume replace the woman; the platform, fish and broad head-turn sequence remain.        | The 0–5-second request returns 5.375 seconds. Gesture timing is not frame-exact; fast actions, multiple people and object contact are untested.                                                     |
| Video Editor                | The footage becomes a drawn illustration while retaining the scene's main colors and subject cues.                             | The head is already turned in the opening where the source faces forward. The requested timing and facial likeness are not fully preserved; it is not a faithful-action pass.                       |
| Lip Sync                    | The existing moving scene receives mouth changes and a full-duration audio stream.                                             | Pronunciation and synchronization remain unreviewed by ear. The video stream is slightly shorter than the audio stream. No singing or multilingual result was tested.                               |

The shared scene makes route differences inspectable. It is deliberately not evidence of every audience's taste or of social virality. Music-video generation, body swap, multi-person face mapping, Character Replace animate mode and caption quality are not exercised in this case.

## Verify the file rather than trusting the settings

These values come from the downloaded files, not the requested resolution or project estimate.

| Original file         | Dimensions | Video fps | Video duration | Audio duration |
| --------------------- | ---------- | --------: | -------------: | -------------: |
| performance.mp4       | 720 × 1296 |        24 |     5.041667 s |           none |
| moon-elevator.mp4     | 720 × 1296 |        24 |     5.041667 s |           none |
| face-swap.mp4         | 568 × 1024 |        24 |     5.000000 s |           none |
| talking-photo.mp4     | 448 × 832  |        25 |     3.960000 s |     3.920000 s |
| character-replace.mp4 | 704 × 1280 |        24 |     5.375000 s |           none |
| video-edit.mp4        | 704 × 1280 |        24 |     5.000000 s |           none |
| lip-sync.mp4          | 570 × 1024 |        24 |     3.875000 s |     3.920000 s |

The source WAV is 3.920042 seconds. Both speech-video requests use that measured interval. The Talking Photo project reported 24 fps while the file is 25 fps, and the returned height exceeds its requested `max_resolution: 720`. Do not silently certify a requested frame size, duration or frame rate from the API response. Full speech duration in metadata does not prove the words sound correct.

## Reproduce or finish a variation

Use the live tool schemas before spending: model availability and prices can change. Upload the bundled input files with `video_assets_generate_presigned_url`, PUT raw bytes to the returned upload URL without the API bearer token, and substitute each returned `file_path` for the corresponding `<uploaded:filename>` placeholder in [requests.json](requests.json). These placeholders are explanatory, not valid paths. Cosmetic job names and expiring URLs are omitted. No seed was supplied; regeneration will vary.

Submit the chosen operation once, save its ID and use the matching wait/retrieve tool. A wait timeout does not require another paid creation. Every created job in this case is included above. To try only recasting, upload the included performance and chosen identity; the other generation steps are unnecessary.

The [vertical export](remix.mp4) uses all 121 generated frames, at original speed, with eight pixels cropped from the top and bottom to make an exact 720 × 1280 canvas. Subject and fish stay within this crop in the reviewed frames. It contains no soundtrack, caption, held-frame extension or extra generation. Run from this folder with FFmpeg installed:

```sh
ffmpeg -i performance.mp4 -vf 'crop=720:1280:0:8,setsar=1' -c:v libx264 -crf 18 -preset fast -pix_fmt yuv420p -an -movflags +faststart remix.mp4
```

Keep the originals when adding captions, sound or another export size. Check the actual streams and final word before combining speech and picture. If a brief requires exact action timing, return to the original performance rather than chaining the restyled take. [Routing and recovery decisions →](../../skills/magic-hour-media/references/remix.md)
