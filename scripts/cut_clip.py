#!/usr/bin/env python3
"""
Cut a frame-accurate vertical clip from a source video.

Why not just stream-copy: the common recipe is `-ss <t> -i in.mp4 -c copy`,
which is fast but snaps the cut to the nearest keyframe. On a YouTube download
that GOP is often 2-10 seconds, so the clip opens seconds early or late. For a
3-minute chapter nobody notices. For a clip whose entire value is its first
frame, it either amputates the hook or opens on dead air — which is exactly the
thing we are trying to engineer.

So we re-encode. It costs seconds of CPU and buys an exact in-point.

Output defaults to 1080x1920 (9:16) via a centre crop, per the house format.
Pass --keep-aspect when a campaign's rules require the original framing.

Provenance: independently implemented. The caption-cleaning approach was
informed by github.com/op7418/Youtube-clipper-skill (MIT), which handles
inline VTT timing tags well; the rolling-caption de-duplication and the
frame-accurate cut are ours, and fix defects in that project.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def to_seconds(value: str) -> float:
    """Accept 12.5, 1:05, 1:05.25, or 01:02:03.5."""
    if re.fullmatch(r"\d+(\.\d+)?", value):
        return float(value)
    parts = value.split(":")
    if not 2 <= len(parts) <= 3:
        raise argparse.ArgumentTypeError(f"bad timestamp: {value}")
    parts = [float(p) for p in parts]
    while len(parts) < 3:
        parts.insert(0, 0.0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def build_command(ffmpeg: str, src: Path, start: float, duration: float,
                  dest: Path, vertical: bool, crf: int) -> list[str]:
    cmd = [ffmpeg, "-hide_banner", "-loglevel", "error",
           "-ss", f"{start:.3f}", "-i", str(src), "-t", f"{duration:.3f}"]

    if vertical:
        # min() guards sources already narrower than 9:16 so the crop never
        # exceeds the frame.
        cmd += ["-vf", "crop='min(iw,ih*9/16)':'min(ih,iw*16/9)',"
                       "scale=1080:1920:flags=lanczos,setsar=1"]

    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", str(crf),
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart", "-y", str(dest)]
    return cmd


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path)
    ap.add_argument("start", type=to_seconds, help="e.g. 4:12 or 252.5")
    ap.add_argument("end", type=to_seconds, help="e.g. 4:38 or 278")
    ap.add_argument("output", type=Path)
    ap.add_argument("--keep-aspect", action="store_true",
                    help="skip the 9:16 crop (campaign rules override the default)")
    ap.add_argument("--crf", type=int, default=18, help="quality, lower is better (default 18)")
    ap.add_argument("--dry-run", action="store_true", help="print the command, do not run")
    args = ap.parse_args()

    duration = args.end - args.start
    if duration <= 0:
        print(f"error: end ({args.end}s) must be after start ({args.start}s)", file=sys.stderr)
        return 1
    if not args.dry_run and not args.source.is_file():
        print(f"error: no such file: {args.source}", file=sys.stderr)
        return 1

    ffmpeg = shutil.which("ffmpeg") or "ffmpeg"
    if not args.dry_run and not shutil.which("ffmpeg"):
        print("error: ffmpeg not found on PATH.\n"
              "  macOS:  brew install ffmpeg\n"
              "  Debian: sudo apt install ffmpeg", file=sys.stderr)
        return 1

    cmd = build_command(ffmpeg, args.source, args.start, duration, args.output,
                        not args.keep_aspect, args.crf)

    if args.dry_run:
        print(" ".join(cmd))
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    print(f"cutting {duration:.2f}s from {args.start:.2f}s "
          f"({'9:16 1080x1920' if not args.keep_aspect else 'original aspect'})")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffmpeg failed:\n{result.stderr.strip()}", file=sys.stderr)
        return result.returncode

    size = args.output.stat().st_size / 1_048_576
    print(f"wrote {args.output} ({size:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
