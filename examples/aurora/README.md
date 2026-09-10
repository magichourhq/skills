# AURORA product example

Original synthetic product outputs generated September 10, 2026, using Magic Hour's signed-in web interface. These files are unchanged exports, not retouched demonstrations. They illustrate the workflows in skills version 1.0.0; an agent loading the installed skill through MCP was not tested in this comparison.

| Output | Settings | Credits | Original project ID |
| --- | --- | --- | --- |
| [Generic image](generic-image.png) | Z-Image Turbo, 640 × 360, one image | 5 | `cmtvyb02800u1l101ipb9mgpa` |
| [Guided image](guided-image.png) | Z-Image Turbo, 640 × 360, one image | 5 | `cmtvy7tir00sol101laiyl38p` |
| [Generic video](generic-video.mp4) | LTX-2.5, 480p, 16:9, requested 1 second, audio off | 24 | `cmtvy79ue00vsi601so42e4tm` |
| [Guided video](guided-video.mp4) | LTX-2.5, 480p, 16:9, requested 1 second, audio off | 24 + 5 for the start frame | `cmtvy8uwz00tejf01elz89v31` |

Both MP4s contain H.264 video at 854 × 480 with an encoded duration of 1.041667 seconds. Credit amounts are historical charges for these runs, not current price quotes.

## Image prompts

Generic:

> A cobalt-blue glass perfume bottle labeled AURORA on wet black stone at night.

Guided:

> Premium cinematic 16:9 product hero still. One cobalt-blue glass perfume bottle labeled exactly “AURORA” stands centered on wet black stone at night. Front three-quarter view, bottle and cap geometrically straight, label crisp and legible. Soft violet rim light from right, cool cyan fill from left, realistic droplets and controlled reflection, deep charcoal background. Leave clean negative space on the left third. No people, no extra objects, no extra words, no distorted glass, no watermark.

The original guided prompt contains a tension between “centered” and left-side negative space. The starter prompt in the main README instead explicitly places the product on the right.

## Video prompts

Generic text-to-video:

> Create a cinematic product video of a cobalt-blue perfume bottle labeled AURORA on wet black stone at night, with a slow dolly in and soft rim lighting.

Guided image-to-video, using `guided-image.png` as the start frame:

> Slow, smooth dolly in. The bottle remains fixed and unchanged; preserve the exact AURORA label, rectangular glass geometry, cap, and colors. Soft rim light glides across the glass and droplets; the reflection shifts subtly. No cuts, no new objects, no text changes, no camera roll.

## What this demonstrates

The guided still has a clearer single AURORA label and more usable space on the left. The generic video produces duplicate label text; the guided clip retains the approved image's single label and composition through the last frame. Inspect the files and judge whether those differences matter for your placement.

This pair does not isolate the causal effect of installing a skill: prompts differ, the guided path adds a start-frame generation, seeds were not controlled, and there is one sample per condition. The generic prompts did not request negative space. It does not establish a win rate, longer-video reliability, or customer revenue impact.

For your own comparison, give both workflows the same desired deliverable, count all credits and retries, and inspect label accuracy, product stability, motion, placement, and the downloaded file. Use an authorized reference and AI Image Editor when a real product's identity must remain exact; this synthetic example starts with AI Image Generator because it has no source photo.
