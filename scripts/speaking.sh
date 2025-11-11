#!/bin/bash

dt=$(date '+%d/%m/%Y %H:%M:%S');
echo "Speaking... $dt" >> /srv/voice/scripts/speaking.log

#sleep 5s

python3 /srv/voice/scripts/servo.py -d 100
python3 /srv/voice/scripts/servo.py -d 180
python3 /srv/voice/scripts/servo.py -d 100
python3 /srv/voice/scripts/servo.py -d 180
python3 /srv/voice/scripts/servo.py -d 100
python3 /srv/voice/scripts/servo.py -d 180
python3 /srv/voice/scripts/servo.py -d 100
python3 /srv/voice/scripts/servo.py -d 180
python3 /srv/voice/scripts/servo.py -d 100
