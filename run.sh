#!/bin/bash
script/run --debug  \
  --name 'sat1' \
  --uri 'tcp://0.0.0.0:10700' \
  --mic-command 'arecord -D plughw:CARD=Mic,DEV=0 -r 16000 -c 1 -f S16_LE -t raw' \
  --snd-command 'aplay -r 22050 -c 1 -f S16_LE -t raw' \
  --detection-command '/srv/voice/scripts/listening.sh' \
  --tts-stop-command '/srv/voice/scripts/speaking.sh'
  #--wake-uri 'tcp://192.168.178.20:10400' \
  #--wake-word-name 'alexa'
