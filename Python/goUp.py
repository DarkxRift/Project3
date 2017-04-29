import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servoPIN16 = 23
servoPIN18 = 24

GPIO.setup(servoPIN16, GPIO.OUT)
GPIO.setup(servoPIN18, GPIO.OUT)

p16 = GPIO.PWM(servoPIN16, 50)
# GPIO 18 als PWM mit 50Hz 
p18 = GPIO.PWM(servoPIN18, 50) 
# initial position
p18.start(6.5) 
 
time.sleep(1)
p16.stop()
p18.stop()
GPIO.cleanup()
