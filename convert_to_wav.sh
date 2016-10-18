#!/bin/bash

# convert every mp3 in this directory to 16-bit WAV files
for f in $( ls downloads/*.mp3 ); do 
    echo transcoding $f
    ffmpeg -i "$f" -acodec pcm_s16le -ac 1 -ar 16000 "downloads/${f%.mp3}.wav"; 
done

# move all of these wav files to the wav/ directory
for i in $( ls downloads/*.mp3  ); do
    mv $i downloads/wav/
done