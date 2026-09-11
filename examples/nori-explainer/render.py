"""Compose an original reference-first explainer from accepted media, without API calls."""

from pathlib import Path
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = Path(os.environ.get("NORI_FONT_DIR", "/System/Library/Fonts/Supplemental"))
SOURCES = ROOT.parent / "nori-character"
BEATS = (
    ("anchor.png", "Choose one", "reference.", "Check the details you want to keep.", 7.347),
    ("greenhouse-baseline.png", "Change the scene.", "Keep the character.", "Inspect the still before adding motion.", 5.123),
    ("garden-guided.png", "Reuse what", "already works.", "Save accepted files for the next episode.", 6.840),
)


def label(draw, xy, value, size, color, bold=False):
    font = ImageFont.truetype(str(FONTS / ("Arial Bold.ttf" if bold else "Arial.ttf")), size)
    draw.text(xy, value, font=font, fill=color)


for i, (source, heading, second, body, duration) in enumerate(BEATS, 1):
    frame = Image.new("RGB", (1280, 720), "#101D38")
    frame.paste(Image.open(SOURCES / source).convert("RGB").resize((620, 620)), (636, 50))
    d = ImageDraw.Draw(frame)
    label(d, (48, 54), "MAGIC HOUR / FIELD NOTES", 19, "#A8CDF5", True)
    label(d, (48, 184), f"0{i}", 25, "#80BFFF", True)
    label(d, (48, 248), heading, 46, "white", True)
    label(d, (48, 306), second, 46, "white", True)
    label(d, (48, 420), body, 22, "#C9DDF1")
    label(d, (48, 650), "Original Nori artwork / synthetic voice demonstration", 16, "#A8CDF5")
    frame.save(ROOT / f"scene-{i}.png")

timeline = ROOT / "timeline.ffconcat"
timeline.write_text("ffconcat version 1.0\n" + "".join(
    f"file scene-{i}.png\nduration {beat[4]:.3f}\n" for i, beat in enumerate(BEATS, 1)
) + "file scene-3.png\n")
subprocess.run([
    "ffmpeg", "-nostdin", "-v", "error", "-y", "-threads", "1",
    "-f", "concat", "-safe", "0", "-i", str(timeline), "-i", str(ROOT / "narration.wav"),
    "-i", str(ROOT / "greenhouse-motion.mp4"), "-filter_complex_threads", "1",
    "-filter_complex", "[0:v]fps=24[base];[2:v]scale=620:620,setsar=1,"
    "tpad=stop_mode=clone:stop_duration=0.082,setpts=PTS-STARTPTS+7.347/TB[motion];"
    "[base][motion]overlay=636:50:enable='gte(t,7.347)*lt(t,12.470)':eof_action=pass[video]",
    "-map", "[video]", "-map", "1:a:0", "-af", "apad=pad_dur=0.6", "-t", "19.31",
    "-r", "24", "-c:v", "libx264", "-threads", "1", "-preset", "medium", "-crf", "20",
    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
    str(ROOT / "explainer.mp4"),
], check=True)
