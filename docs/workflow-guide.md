# AI media workflow decisions

The skill adds production decisions around Magic Hour's tools: which source to reuse, what to fix before motion, when a generation is unnecessary, how to judge an output, and how to continue without losing accepted work. The MCP executes jobs; a successful tool call alone does not answer those questions.

## How do I put myself into a video or make my character perform?

Use [Face Swap](../skills/magic-hour-face-swap) to change a face while preserving the existing performance and body. Use [Character Replace](../skills/magic-hour-character-replace) when the body/costume/character should change, or when a reference character should perform source motion. For a newly imagined scene, edit the supplied portrait into the intended start frame and animate it. The [remix guide](../skills/magic-hour-media/references/remix.md) explains how to choose without learning API fields.

## Can I make music videos or a singing character?

Start with the selected audio phrase. A visible performance uses Talking Photo or Lip Sync; new audio-guided visuals use Audio-to-Video; precisely timed sequences require an available compositor. These tools have different guarantees. See [music and performance](../skills/magic-hour-media/references/music.md) for timing, source reuse and the checks still needed before claiming synchronized output.

## How do I keep a product or character consistent in AI video?

Start with an authorized reference. Use AI Image Editor to change setting or composition while preserving identity. Inspect the still, then feed that exact approved image into image-to-video. For additional shots, return to the same identity anchor and review each still. Describe motion separately from appearance. See [image to video](../skills/magic-hour-image-to-video) and [character consistency](../skills/magic-hour-character-consistency).

## Should I use text-to-video or image-to-video?

Use image-to-video when the starting appearance matters: a real product, recurring character, precise composition or approved style. Text-to-video is useful for an exploratory scene without a locked visual reference. Neither route guarantees identity or motion quality. Our [AURORA comparison](../examples/aurora) illustrates the benefit of an approved still in one case; its different prompts and extra still-generation cost prevent a causal win-rate claim.

## How do I put exact text or a logo in generated media?

Use the original logo and editable text in a compositor. Generate the visual without relying on the model to spell the headline or place it at exact coordinates. Verify the exported file, including motion crossing the copy region. The [finished-ad recipe](../examples/aurora-finished) demonstrates a fixed layout without another paid generation.

## What should I do when an image model ignores the aspect ratio?

Read the downloaded dimensions. Crop only if the complete subject and required copy area survive. Otherwise choose a currently supported reframing route or a contained layout that meets the brief. Do not stretch. In our [five editing attempts](../examples/aurora-edits), changing the model corrected the square ratio, while two vertical prompts still missed a strict placement boundary. These are observations from one synthetic product, not a universal model ranking.

## How do I make a talking video without cutting off the speech?

Finish the script and audio first. Listen to pronunciation and the final word, measure duration, then choose the supported talking-photo or lip-sync interval. Add captions after the final picture cut. Keep the clean master and approved audio. Our [Talking Photo and Lip Sync outputs](../examples/midnight-remix) include full-duration audio streams, but metadata cannot prove pronunciation or synchronization; their listening review remains outstanding. See [talking video](../skills/magic-hour-talking-video).

## When should I avoid another AI generation?

Use a compositor for exact cropping, trimming, copy, logo placement and soundtrack assembly. Reuse accepted source media when the brief only changes a headline or placement. For a genuine visual change to existing footage, use [video editing](../skills/magic-hour-video-editing) and compare the result against the original. A new job is not a recovery mechanism for an expired download URL or a polling timeout.

## Which Magic Hour model is best?

Choose from the [live schema](https://docs.magichour.ai/api-reference/openapi.json) for the required operation, references, duration, resolution, audio, tier and budget. Treat provider model descriptions as selection guidance, not measured quality. Inspect the first output before expanding a batch. Our [dated observations](../skills/magic-hour-campaign-kit/references/model-observations.md) document both accepted outputs and failures; no static winner is justified across every job.

## What evidence is published?

The [evidence index](evidence.md) links every published case, exact prompts, output files, observed failures and remaining validation gaps. It also explains how to reproduce comparisons and cite a fixed version. A completed tool call does not prove quality, and these cases do not establish general superiority or business lift.

## How do I direct advanced work without learning API parameters?

Describe the finished result, attach accepted sources and state the budget or reuse an existing one. The skills choose the technical route and perform delegated creative checks. For task-specific decisions, use the [advanced recipes](../README.md#go-further): reference photoshoots, faithful edits, multi-shot films, recurring casts, thumbnails, language versions and repurposed footage. Each reference ships inside its corresponding skill.
