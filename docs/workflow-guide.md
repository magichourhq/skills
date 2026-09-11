# AI media workflow decisions

The skill adds production decisions around Magic Hour's tools: which source to reuse, what to fix before motion, when a generation is unnecessary, how to judge an output, and how to continue without losing accepted work. The MCP executes jobs; a successful tool call alone does not answer those questions.

## How do I keep a product or character consistent in AI video?

Start with an authorized reference. Use AI Image Editor to change setting or composition while preserving identity. Inspect the still, then feed that exact approved image into image-to-video. For additional shots, return to the same identity anchor and review each still. Describe motion separately from appearance. See [image to video](../skills/magic-hour-image-to-video) and [character consistency](../skills/magic-hour-character-consistency).

## Should I use text-to-video or image-to-video?

Use image-to-video when the starting appearance matters: a real product, recurring character, precise composition or approved style. Text-to-video is useful for an exploratory scene without a locked visual reference. Neither route guarantees identity or motion quality. Our [AURORA comparison](../examples/aurora) illustrates the benefit of an approved still in one case; its different prompts and extra still-generation cost prevent a causal win-rate claim.

## How do I put exact text or a logo in generated media?

Use the original logo and editable text in a compositor. Generate the visual without relying on the model to spell the headline or place it at exact coordinates. Verify the exported file, including motion crossing the copy region. The [finished-ad recipe](../examples/aurora-finished) demonstrates a fixed layout without another paid generation.

## What should I do when an image model ignores the aspect ratio?

Read the downloaded dimensions. Crop only if the complete subject and required copy area survive. Otherwise choose a currently supported reframing route or a contained layout that meets the brief. Do not stretch. In our [five editing attempts](../examples/aurora-edits), changing the model corrected the square ratio, while two vertical prompts still missed a strict placement boundary. These are observations from one synthetic product, not a universal model ranking.

## How do I make a talking video without cutting off the speech?

Finish the script and audio first. Listen to pronunciation and the final word, measure duration, then choose the supported talking-photo or lip-sync interval. Add captions after the final picture cut. Keep the clean master and approved audio. See [talking video](../skills/magic-hour-talking-video); its published output-quality validation is still pending.

## When should I avoid another AI generation?

Use a compositor for exact cropping, trimming, copy, logo placement and soundtrack assembly. Reuse accepted source media when the brief only changes a headline or placement. For a genuine visual change to existing footage, use [video editing](../skills/magic-hour-video-editing) and compare the result against the original. A new job is not a recovery mechanism for an expired download URL or a polling timeout.

## Which Magic Hour model is best?

Choose from the [live schema](https://docs.magichour.ai/api-reference/openapi.json) for the required operation, references, duration, resolution, audio, tier and budget. Treat provider model descriptions as selection guidance, not measured quality. Inspect the first output before expanding a batch. Our [dated observations](../skills/magic-hour-campaign-kit/references/model-observations.md) document both accepted outputs and failures; no static winner is justified across every job.

## What evidence is published?

| Workflow                                                          | Current evidence                                                                                                                                   | Still missing                                                         |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Product image and image-to-video                                  | Original files, exact prompts, settings, project IDs and historical costs                                                                          | Controlled installed-agent comparison; broader subjects and durations |
| Product editing and campaign reframing                            | All five attempts, including wrong ratios, drift and failed placement                                                                              | Broader real-product and portrait coverage                            |
| Final ad composition                                              | Executed FFmpeg recipe, editable copy, deterministic export                                                                                        | Destination-platform acceptance and audience response                 |
| Character continuity                                              | [Five authenticated MCP outputs](../examples/nori-character), two paired prompt comparisons, exact prompts, IDs and charged credits; mixed results | More characters, repeated runs, blind review and animation            |
| Thumbnails, talking video, generative video editing and subtitles | Live creation-tool discovery and request-schema review                                                                                             | Authenticated output runs and visual/audio quality comparisons        |

To compare a skill with your usual MCP workflow, use the same brief, source, allowed tools, model settings and spending ceiling. Count failed attempts and total cost, hide workflow labels during quality review where practical, and judge task completion, fidelity, timing and export usability. Repeat across different subjects before reporting a general advantage. Downloading or installing a skill is not evidence of retained use, customer revenue or search citations.
