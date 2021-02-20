#!/bin/sh

export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1
python3 liveInteraction.py -l="model/x_labels.txt" -m="model/x_model.h5"
chromium-browser https://www.youtube.com/embed/dcpQYafcvCg?autoplay=1 &

