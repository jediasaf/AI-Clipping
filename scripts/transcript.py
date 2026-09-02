#!/usr/bin/env python3
"""
Parse a YouTube VTT/SRT caption file into clean, timestamped transcript lines
for the clip-miner to analyse.

Why this exists: YouTube auto-captions are messy in two specific ways that
break naive parsers, and both matter to us.

1. Inline word-level timing tags: "so the thing<00:00:02.480><c> about</c>"
2. Rolling duplication: each line is emitted twice, once as a partial and once
   complete, so a raw parse yields ~2x the text.

(1) produces garbage quotes. (2) roughly doubles the transcript we feed to the
model, for zero added information. We strip both.

Design note: this prints a BOUNDED preview to stdout and writes the full
transcript to JSON on disk. Never dump a whole transcript to stdout — on a long
video that floods the agent's context and crowds out the actual reasoning.

Provenance: independently implemented. The caption-cleaning approach was
informed by github.com/op7418/Youtube-clipper-skill (MIT), which handles
inline VTT timing tags well; the rolling-caption de-duplication and the
frame-accurate cut are ours, and fix defects in that project.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# <00:00:02.480> timing tags and <c>/<c.colorE5E5E5> span tags
INLINE_TAG = re.compile(r"<\d{2}:\d{2}:\d{2}[.,]\d{3}>|</?c[^>]*>")
# WebVTT cue settings trailing the timestamp line
CUE_SETTINGS = re.compile(r"\s+(align|position|size|line|region|vertical):\S+")
TIMESTAMP = re.compile(
    r"(\d{2}:\d{2}:\d{2}[.,]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[.,]\d{3})"
)


def to_seconds(ts: str) -> float:
    h, m, rest = ts.split(":")
    s, ms = re.split(r"[.,]", rest)
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def fmt(seconds: float) -> str:
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def parse(path: Path) -> list[dict]:
    """Return [{start, end, text}] with inline tags stripped and rolling
    duplicates collapsed."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    cues: list[dict] = []

    for block in re.split(r"\n\s*\n", raw):
        lines = [ln for ln in block.splitlines() if ln.strip()]
        if not lines:
            continue
        match = None
        idx = 0
        for i, ln in enumerate(lines):
            match = TIMESTAMP.search(CUE_SETTINGS.sub("", ln))
            if match:
                idx = i
                break
        if not match:
            continue

        text = " ".join(lines[idx + 1:])
        text = INLINE_TAG.sub("", text)
        text = re.sub(r"<[^>]+>", "", text)          # any residual markup
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue

        cues.append(
            {"start": to_seconds(match.group(1)),
             "end": to_seconds(match.group(2)),
             "text": text}
        )

    return dedupe(cues)


def _tail_head_overlap(prev_words: list[str], cur_words: list[str]) -> int:
    """Longest k where the last k words of prev are the first k words of cur."""
    for k in range(min(len(prev_words), len(cur_words)), 0, -1):
        if prev_words[-k:] == cur_words[:k]:
            return k
    return 0


def dedupe(cues: list[dict]) -> list[dict]:
    """Collapse YouTube's rolling captions.

    Rolling captions scroll: the tail of one cue reappears as the head of the
    next.  "the thing nobody tells you about starting out"
           "about starting out is that it compounds"
    So the relationship is an overlap, not a prefix. Merging on prefix alone
    leaves "about starting out" in the transcript twice, which inflates word
    counts and hands the Clip Miner a timestamp pointing at a repeat.

    We merge on the longest tail/head overlap and append only the remainder.
    A strict prefix is just the case where the overlap is the whole of prev.

    Overlaps of a single word are left alone. Real speech repeats short words
    across a cue boundary often enough that merging on k=1 would delete words
    the speaker actually said, and a lost word costs more than a duplicated one.
    """
    out: list[dict] = []
    for cue in cues:
        if out:
            prev = out[-1]
            if cue["text"] == prev["text"]:
                prev["end"] = max(prev["end"], cue["end"])
                continue
            prev_words = prev["text"].split()
            cur_words = cue["text"].split()
            k = _tail_head_overlap(prev_words, cur_words)
            if k and (k >= 2 or k == len(prev_words)):
                if k < len(cur_words):
                    prev["text"] = " ".join(prev_words + cur_words[k:])
                prev["end"] = max(prev["end"], cue["end"])
                continue
        out.append(dict(cue))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("caption_file", type=Path)
    ap.add_argument("-o", "--out", type=Path, help="JSON output (default: <input>.json)")
    ap.add_argument("--preview", type=int, default=25, help="lines to print (default 25)")
    args = ap.parse_args()

    if not args.caption_file.is_file():
        print(f"error: no such file: {args.caption_file}", file=sys.stderr)
        return 1

    cues = parse(args.caption_file)
    if not cues:
        print("error: no cues parsed — is this a VTT/SRT file?", file=sys.stderr)
        return 1

    out = args.out or args.caption_file.with_suffix(".transcript.json")
    duration = cues[-1]["end"]
    lines = [f"[{fmt(c['start'])}] {c['text']}" for c in cues]

    out.write_text(
        json.dumps(
            {"source": str(args.caption_file), "duration_seconds": duration,
             "cue_count": len(cues), "lines": lines, "cues": cues},
            indent=2, ensure_ascii=False),
        encoding="utf-8")

    words = sum(len(c["text"].split()) for c in cues)
    print(f"parsed   {len(cues)} cues, {words} words, duration {fmt(duration)}")
    print(f"written  {out}")
    print(f"\npreview (first {min(args.preview, len(lines))} of {len(lines)} lines):")
    print("\n".join(lines[:args.preview]))
    if len(lines) > args.preview:
        print(f"... {len(lines) - args.preview} more lines in {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
