#!/usr/bin/env bash
# ==============================================================================
# Development Environment Setup Script
# Opens Firefox with the DSA YouTube Playlist and launches the working Antigravity IDE
# ==============================================================================

PROJECT_DIR="/home/hammad/project/dsa"
PLAYLIST_URL="https://www.youtube.com/playlist?list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU"

echo "=== Initializing DSA Study & Dev Environment ==="

# 1. Open Firefox with the DSA Playlist
echo "[1/2] Opening Firefox with the YouTube playlist..."
if command -v firefox >/dev/null 2>&1; then
    nohup firefox "$PLAYLIST_URL" >/dev/null 2>&1 &
else
    echo "Firefox command not found in PATH, trying xdg-open..."
    nohup xdg-open "$PLAYLIST_URL" >/dev/null 2>&1 &
fi

sleep 1

# 2. Open Working Antigravity IDE (Snap version)
echo "[2/2] Opening Antigravity IDE application..."
SNAP_ANTIGRAVITY="/snap/bin/antigravity-ide-snap.antigravity-ide"

if [ -x "$SNAP_ANTIGRAVITY" ]; then
    env -u ELECTRON_RUN_AS_NODE nohup "$SNAP_ANTIGRAVITY" "$PROJECT_DIR" >/dev/null 2>&1 &
elif command -v antigravity-ide >/dev/null 2>&1; then
    env -u ELECTRON_RUN_AS_NODE nohup antigravity-ide "$PROJECT_DIR" >/dev/null 2>&1 &
else
    echo "Error: Could not locate Antigravity IDE executable." >&2
fi

echo "Environment setup triggered successfully! Happy coding!"
