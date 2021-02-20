#!/bin/sh

export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1
python3 liveInteraction.py
chromium-browser https://www.youtube.com/embed/dcpQYafcvCg?autoplay=1 &

