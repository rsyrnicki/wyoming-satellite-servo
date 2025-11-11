from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
from gpiozero import Servo
from time import sleep

#factory = PiGPIOFactory()

#servo_0 = AngularServo(12, min_angle=-90, max_angle=90)
#servo_0.angle = 0
#sleep(1)
#servo_0.angle=90

servo = Servo("GPIO18")
sleep(2)
servo.min()
sleep(2)
servo.max()
