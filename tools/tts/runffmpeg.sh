#!/usr/bin/bash

for i in *.wav
do 
    ffmpeg -i "$i" "${i%.*}.mp3"
done

rm wavfiles/*.wav

mv wavfiles/*.mp3 ../../resource/vocabx