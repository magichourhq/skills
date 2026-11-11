# Two LTX-2.5 video examples

Both examples use the Magic Hour API or creation MCP. The credits are the charges for the recorded jobs. Check the current [pricing](https://docs.magichour.ai/billing/overview) and supported settings before running either example.

## Animate a product photo

Use the [original serum-bottle photo](https://github.com/magichourhq/ai-video-model-benchmark/blob/main/assets/inputs/skincare-orbit.png) as the starting frame for Image-to-Video. See the [exact prompt and source](https://github.com/magichourhq/ai-video-model-benchmark/blob/main/benchmark.json) under `skincare-orbit`.

The [displayed attempt](https://github.com/magichourhq/ai-video-model-benchmark/blob/main/assets/outputs/skincare-orbit/ltx-2.5/attempt-01.mp4) requested LTX-2.5, eight seconds, 720p and audio off. It returned a 1278 × 722 silent clip at 24 fps and charged 384 credits. The bottle stays in view, but the cap is cropped near the end. The [benchmark gallery](https://github.com/magichourhq/ai-video-model-benchmark/blob/main/GALLERY.md#paid-social-product-hero) includes the other attempts.

## Open an elevator onto a lunar landscape

One Text-to-Video job completed on November 10, 2026 Pacific through the creation MCP. It used LTX-2.5, 480p, 9:16, five seconds and audio off. The [MP4](moon-elevator.mp4) is 480 × 854, 24 fps and 5.04 seconds. The job charged 120 credits. No paid retry was made.

> One locked five-second vertical shot from inside a brushed-steel elevator facing its closed doors. During the first two seconds the doors slide apart, revealing a quiet lunar landscape with a distant ridge and blue Earth above it. Hold on the reveal until the end. Natural light, straight door frames, no people, no signage, no captions, no camera movement.

The doors open onto a barren landscape but keep moving through most of the clip. There is little hold on the reveal, and the requested blue Earth is not clear.

The [Midnight Remixes case](../midnight-remix) records the earlier LTX-2.3 runs. Magic Hour has since [replaced LTX 2.3](https://magichour.ai/models/ltx-2-3).
