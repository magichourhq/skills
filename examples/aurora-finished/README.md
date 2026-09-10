# AURORA: exact layout after generation

![Square AURORA ad layout](poster.png)

[Play the six-second export](finished-ad.mp4).

This fictional creative uses the existing [guided Magic Hour video](../aurora/guided-video.mp4), project `cmtvy8uwz00tejf01elz89v31`. The source was generated through the web interface; finishing used local FFmpeg on September 10, 2026. No additional generation credits were spent. Headline and CTA are example copy, not claims about a real product.

The finished file is 1080×1080 H.264, 24 fps, six seconds, silent. The source remains at its native 854×480 inside the canvas: it is not stretched or upscaled. Its 25 source frames provide approximately 1.04 seconds of generated motion, followed by a deliberate final-frame hold. This is **not** a six-second generated-video demonstration. The source watermark remains visible, so this is a finishing example rather than a watermark-free production ad. The larger canvas does not add source detail.

## Reproduce or adapt

Run from this directory with FFmpeg built with `drawtext` and `libx264`. Supply a licensed bold font at `font.ttf`; the published example used macOS Arial Bold. Font files are not distributed. Keep the three UTF-8 text files editable. `expansion=none` renders copy literally instead of interpreting percent expressions.

```sh
# Example on macOS; use your own licensed font on other systems.
cp '/System/Library/Fonts/Supplemental/Arial Bold.ttf' font.ttf

ffmpeg -nostdin -hide_banner -loglevel error -threads 1 \
  -i ../aurora/guided-video.mp4 \
  -vf "tpad=stop_mode=clone:stop_duration=5,\
pad=1080:1080:113:350:color=0x0b1016,\
drawbox=x=113:y=148:w=64:h=4:color=0x83d6ed:t=fill,\
drawtext=fontfile=font.ttf:textfile=brand.txt:expansion=none:fontcolor=0x83d6ed:fontsize=24:x=113:y=97,\
drawtext=fontfile=font.ttf:textfile=headline.txt:expansion=none:fontcolor=0xf4f3f0:fontsize=92:x=107:y=204,\
drawbox=x=113:y=896:w=854:h=1:color=0x3c4b5c:t=fill,\
drawtext=fontfile=font.ttf:textfile=cta.txt:expansion=none:fontcolor=0xf4f3f0:fontsize=26:x=113:y=939" \
  -t 6 -an -r 24 -c:v libx264 -threads 1 -crf 18 \
  -pix_fmt yuv420p -movflags +faststart finished-ad.mp4

ffmpeg -nostdin -hide_banner -loglevel error -i finished-ad.mp4 \
  -frames:v 1 poster.png
```

FFmpeg refuses to overwrite existing output files with this command; choose new output names for another version. `-nostdin` also prevents FFmpeg from consuming commands when an agent runs the recipe through standard input. The coordinates fit this source and this copy only. For different source dimensions, calculate its panel fit first; for longer copy, render and adjust line breaks/font size. Do not assume these margins satisfy a particular ad platform's overlays. `-an` intentionally removes audio; change that decision for an audio brief. Do not commit the local font file.

## What to inspect

The headline and CTA occupy separate fixed regions and never depend on the image model spelling them correctly. The complete source frame, product and watermark remain visible. Inspect the motion-to-hold transition as well as the first and final frame; the hold is intentional, not a stalled generation. Verify duration and streams with `ffprobe` and decode the full file before accepting an export.

This validates the provided finishing recipe for one source. It does not validate authenticated MCP execution, platform ad acceptance, visual superiority, click-through rate, or revenue lift. The [editing attempts](../aurora-edits) explain why exact layout deserves a separate composition step instead of repeated paid prompt repairs.
