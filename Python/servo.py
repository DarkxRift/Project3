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
p16.start(5.6) 
# initial position
p18.start(3.8) 
time.sleep(1)

middle_y = 3.8
middle_x = 5.6


start = False

while not start:

    txt = float(input('number range 1 to 10: '))

    p16.ChangeDutyCycle(txt)

    if txt == 11:
        start = True
        

p16.stop()
p18.stop()
GPIO.cleanup()
