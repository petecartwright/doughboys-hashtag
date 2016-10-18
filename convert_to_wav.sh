#!/bin/bash

# convert every mp3 in this directory to 16-bit WAV files
for f in *.mp3; do 
    ffmpeg -i "$f" -acodec pcm_s16le -ac 1 -ar 16000 "${f%.mp3}.wav"; 
done

# move all of these wav files to the wav/ directory
for i in $( ls *.wav ); do
    mv $i wav/
done