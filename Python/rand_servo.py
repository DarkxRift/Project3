# Autor:	Ingmar Stapel
# Date:		20160811
# Version:	1.0
# Homepage:	www.custom-build-robots.com

import RPi.GPIO as GPIO
import time
from random import randint

GPIO.setmode(GPIO.BCM)

# define the servo pins. 
# Here you could conhange the code and add your pins for example
servoPIN16 = 23
servoPIN18 = 24

move1 = 0
move2 = 0

GPIO.setup(servoPIN16, GPIO.OUT)
GPIO.setup(servoPIN18, GPIO.OUT)

# GPIO 12 als PWM mit 50Hz
p16 = GPIO.PWM(servoPIN16, 50)
# GPIO 18 als PWM mit 50Hz 
p18 = GPIO.PWM(servoPIN18, 50) 
# initial position
p16.start(4) 
# initial position
p18.start(4) 
time.sleep(1)

# This loop will not end until you kill the program
try:
        while True:
                move1 = randint(4, 6)
                move2 = randint(2, 8)

                p16.ChangeDutyCycle(move1)
                p18.ChangeDutyCycle(move2)
                time.sleep(2.5)

except KeyboardInterrupt:
    pass
p16.stop()
p18.stop()
GPIO.cleanup()
