#!/bin/bash

dt=$(date '+%d/%m/%Y %H:%M:%S');
echo "Listening... $dt" >> /srv/voice/scripts/listening.log

python3 /srv/voice/scripts/servo.py -d 180
python3 /srv/voice/scripts/servo.py -d 100

