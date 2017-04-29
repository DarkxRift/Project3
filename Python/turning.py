import RPi.GPIO as GPIO
import time
from sys import argv

GPIO.setmode(GPIO.BCM)
servoPIN16 = 23
servoPIN18 = 24

GPIO.setup(servoPIN16, GPIO.OUT)
GPIO.setup(servoPIN18, GPIO.OUT)

p16 = GPIO.PWM(servoPIN16, 50)
# GPIO 18 als PWM mit 50Hz 
p18 = GPIO.PWM(servoPIN18, 50)  

start = False

while not start:
	
	if argv[1] == "left":
		p16.ChangeDutyCycle(2.5)
		time.sleep(1)
		start = True
	elif argv[1] == "right":
		p16.ChangeDutyCycle(8.5)
		time.sleep(1)
		start = True
	elif argv[1] == "up":
		p18.ChangeDutyCycle(2.5)
		time.sleep(1)
		start = True
	elif argv[1] == "down":
		p18.ChangeDutyCycle(8.5)
		time.sleep(1)
		start = True

p16.stop()
p18.stop()
GPIO.cleanup()
