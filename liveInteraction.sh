#!/bin/sh

export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1

python3 liveInteraction.py -v=$1
#chromium-browser https://www.youtube.com/embed/CKnipnFsuFo?autoplay=1 &

