import RPi.GPIO as GPIO 
import time 
import serial
import os
import threading
import pygame

pygame.mixer.init()

GPIO.setmode(GPIO.BCM)
servoPIN16 = 23
servoPIN18 = 24

ser = serial.Serial('/dev/ttyACM0',9600)


GPIO.setup(servoPIN16, GPIO.OUT)
GPIO.setup(servoPIN18, GPIO.OUT)

p16 = GPIO.PWM(servoPIN16, 50)
# GPIO 18 als PWM mit 50Hz 
p18 = GPIO.PWM(servoPIN18, 50) 
# initial position
p16.start(4) 
# initial position
p18.start(4) 
time.sleep(1)

middle_y = 3.8
middle_x = 5.6

p16.ChangeDutyCycle(5.6)
p18.ChangeDutyCycle(3.8)

start = False

def neutral():
    
    
    p16.ChangeDutyCycle(5.6)
    p18.ChangeDutyCycle(3.8)
    time.sleep(2.5)

def happy():
    
    p18.ChangeDutyCycle(5)
    time.sleep(0.1)
    p18.ChangeDutyCycle(3)
    time.sleep(0.1)
    p18.ChangeDutyCycle(5)
    time.sleep(0.1)
    p18.ChangeDutyCycle(3)
    time.sleep(0.1)
    p18.ChangeDutyCycle(5)
    time.sleep(0.1)
    p18.ChangeDutyCycle(3)
    time.sleep(0.1)
    p18.ChangeDutyCycle(3.8)
    time.sleep(2.5)



def meh():

    
    
    p18.ChangeDutyCycle(5)
    time.sleep(1)
    p18.ChangeDutyCycle(3)
    time.sleep(1)
    p18.ChangeDutyCycle(3.8)
    time.sleep(2.5)



def surprised():

    
    
    p18.ChangeDutyCycle(6)
    time.sleep(0.1)
    p18.ChangeDutyCycle(2)
    time.sleep(0.2)
    p18.ChangeDutyCycle(3.8)
    time.sleep(0.1)
    p16.ChangeDutyCycle(3)
    time.sleep(0.1)
    p16.ChangeDutyCycle(8)
    time.sleep(0.2)
    p16.ChangeDutyCycle(5.6)
    time.sleep(2.5)

    




def love():

    p16.ChangeDutyCycle(3)
    p18.ChangeDutyCycle(3.8)
    time.sleep(0.1)
    p16.ChangeDutyCycle(4)
    p18.ChangeDutyCycle(5)
    time.sleep(0.1)
    p16.ChangeDutyCycle(5)
    p18.ChangeDutyCycle(6)
    time.sleep(0.1)
    p16.ChangeDutyCycle(6)
    p18.ChangeDutyCycle(5)
    time.sleep(0.1)
    p16.ChangeDutyCycle(7)
    p18.ChangeDutyCycle(3.8)
    time.sleep(0.1)
    p16.ChangeDutyCycle(6)
    p18.ChangeDutyCycle(2.5)
    time.sleep(0.1)
    p16.ChangeDutyCycle(5)
    p18.ChangeDutyCycle(2)
    time.sleep(0.1)
    p16.ChangeDutyCycle(4)
    p18.ChangeDutyCycle(2.5)
    time.sleep(0.1)
    p16.ChangeDutyCycle(3)
    p18.ChangeDutyCycle(5)
    time.sleep(0.1)
    p16.ChangeDutyCycle(5.6)
    p18.ChangeDutyCycle(3.8)
    time.sleep(2.5)

    
def sad():
    
    p16.ChangeDutyCycle(5.6)
    p18.ChangeDutyCycle(3)
    time.sleep(0.2)
    p18.ChangeDutyCycle(2.5)
    time.sleep(0.2)
    p18.ChangeDutyCycle(2)
    time.sleep(1)
    p18.ChangeDutyCycle(3.8)
    time.sleep(2.5)

def Audio(text):

    if text == 1:
        pygame.mixer.music.load("/home/pi/Voice_reply/surprise.mp3")
        pygame.mixer.music.play()
        

    elif text == 2:
        pygame.mixer.music.load("/home/pi/Voice_reply/meh.mp3")
        pygame.mixer.music.play()

    elif text == 3:
        pygame.mixer.music.load("/home/pi/Voice_reply/happy.mp3")
        pygame.mixer.music.play()

    elif text == 4:
        pygame.mixer.music.load("/home/pi/Voice_reply/love.mp3")
        pygame.mixer.music.play()

    elif text == 5:
        pygame.mixer.music.load("/home/pi/Voice_reply/sad.mp3")
        pygame.mixer.music.play()

    


def check():

    read_line = ser.readline().split("\n")
    read_serial = read_line[0]

    read = False

    while not read:
        
        if read_serial == "1":

            t1_1 = threading.Thread(target=Audio(1))
            t1_1.setDaemon(True)
	    t1_1.start()
            t1_2 = threading.Thread(target=surprised())
            t1_2.start()

            read_serial = "0"
            read = True
    
	
        elif read_serial == "2":
            
            t1_1 = threading.Thread(target=Audio(2))
            t1_1.setDaemon(True)
	    t1_1.start()
            t1_2 = threading.Thread(target=meh())
            t1_2.start()
		
            read_serial = "0"
            read = True 

        elif read_serial == "3":
            
            t1_1 = threading.Thread(target=Audio(3))
            t1_1.setDaemon(True)
	    t1_1.start()
            t1_2 = threading.Thread(target=happy())
            t1_2.start()
			
            read_serial = "0"
            read = True
            
        elif read_serial == "4":
            
            t1_1 = threading.Thread(target=Audio(4))
            t1_1.setDaemon(True)
	    t1_1.start()
            t1_2 = threading.Thread(target=love())
            t1_2.start()
           
            read_serial = "0"
            read = True

        elif read_serial == "5":
           
            t1_1 = threading.Thread(target=Audio(5))
            t1_1.setDaemon(True)
	    t1_1.start()
            t1_2 = threading.Thread(target=sad())
            t1_2.start()
            
            read_serial = "0"
            read = True
	
	elif read_serial == "q":

	    read = True
            p16.stop()
            p18.stop()
            GPIO.cleanup()
  
            exit()
	    

    if read_serial == "0":
        read_line = ser.readline().split("\n")
        read_serial = read_line[0]
	
        read = False
        
        

while not start:
    check()  
    



 

