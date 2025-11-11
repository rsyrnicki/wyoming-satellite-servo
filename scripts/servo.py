#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time

import argparse

RANGE_DEG = 180

#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > RANGE_DEG or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/RANGE_DEG #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--degrees", help="Servo degrees.", type=int)
args = parser.parse_args()


GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 12 for PWM signal
pwm_gpio = 12
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

#Init at 0°
pwm.start(angle_to_percent(args.degrees))
time.sleep(0.1)

#Go at 90°
#pwm.ChangeDutyCycle(angle_to_percent(90))
#time.sleep(1)

#pwm.ChangeDutyCycle(angle_to_percent(RANGE_DEG))
#time.sleep(1)

#Init at 0°
#pwm.start(angle_to_percent(0))
#time.sleep(1)

#Close GPIO & cleanup
pwm.stop()
#GPIO.cleanup()
