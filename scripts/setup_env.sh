#!/usr/bin/env bash
# Make a fresh container able to produce clips.
#
# Why this exists: the session container is ephemeral and ships without ffmpeg
# or yt-dlp, so scripts/cut_clip.py and the whole production path are dead on
# arrival in a new session. That is a five-minute rediscovery every time, and
# it tends to happen halfway through real work rather than at the start.
#
# Idempotent and deliberately non-fatal: a setup script that blocks the session
# when a mirror is down is worse than one that reports what is missing.
# Note apt indexes in these images are often stale -- installing without an
# update first fails on 404s for packages that have since been superseded.

set -u
missing=()
command -v ffmpeg  >/dev/null 2>&1 || missing+=(ffmpeg)
command -v yt-dlp  >/dev/null 2>&1 || missing+=(yt-dlp)

if [ ${#missing[@]} -eq 0 ]; then
    echo "clip toolchain present: $(ffmpeg -version 2>/dev/null | head -1 | cut -d' ' -f1-3), yt-dlp $(yt-dlp --version 2>/dev/null)"
    exit 0
fi

echo "installing missing clip toolchain: ${missing[*]}"

for tool in "${missing[@]}"; do
    case "$tool" in
        yt-dlp)
            pip3 install --quiet --disable-pip-version-check yt-dlp 2>/dev/null \
                || echo "  WARN: yt-dlp install failed -- source downloads unavailable"
            ;;
        ffmpeg)
            apt-get update -qq >/dev/null 2>&1
            apt-get install -y -qq --no-install-recommends ffmpeg >/dev/null 2>&1 \
                || echo "  WARN: ffmpeg install failed -- cut_clip.py cannot run"
            ;;
    esac
done

command -v ffmpeg >/dev/null 2>&1 && command -v yt-dlp >/dev/null 2>&1 \
    && echo "clip toolchain ready" \
    || echo "clip toolchain INCOMPLETE -- production is blocked until resolved"
exit 0
