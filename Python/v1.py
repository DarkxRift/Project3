import pyaudio
from subprocess import call
import speech_recognition as sr
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera

r = sr.Recognizer()
r.energy_threshold=4000 #the sound limit 

wav = 'test.wav'   #playing human voice
message = ' ' 
next = False         #while loop boolean variable

def name_check():   #function for checking  alpha name

	try:
		with sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
			call(["pico2wave", "-w", wav, 'listening'])  #running ommand line codein python
			call(["mplayer", wav])                           #pico 2 wave is a text to speech service play it using mplayer
			audio = r.listen(source)                          #store the recording voice into a variable call audio
			call(["pico2wave", "-w", wav, 'processing'])
			call(["mplayer", wav])
			
		message = (r.recognize_google(audio, language = 'en-us', show_all=False)) # snd the audio to google speech API and store the names in message  
		word =["Alpha","alpha","elfa","alfa","Elfa","Alfa","Elva","elva","ASDA","elver","author","Elsa","Arthur","elsa","Alva"]
		
		
			
		for i in word:      #check the range of words similar to the word alpha
			if i in message.split(" "):
				call(["pico2wave", "-w", wav, "Yes master?"])
				call(['mplayer', wav])

				print("")
				print("")
				print("")
				print(message)
				print("")
				print("")
				print("")

				voice()
				

		else:
			call(["pico2wave", "-w", wav, "Please repeat again"])
			call(['mplayer', wav])
                        

			print("")
			print("")
			print("")
			print(message)
			print("")
			print("")
			print("")
		
	except KeyboardInterrupt:
		exit()
		
	except sr.UnknownValueError:
		call(["pico2wave", "-w", wav, "Could not understand you"])
		call(['mplayer', wav])
		
	except KeyError:
		call(["pico2wave", "-w", wav, "Could not understand you"])
		call(['mplayer', wav])

		
def voice():
	
	try:
		with sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
			call(["pico2wave", "-w", wav, 'listening'])
                        call(["mplayer", wav])
			audio = r.listen(source)
			call(["pico2wave", "-w", wav, 'processing'])
                        call(["mplayer", wav])
			
		message = (r.recognize_google(audio, language = 'en-us', show_all=False))
		
		print("")
		print("")
		print("")
		print(message)
		print("")
		print("")
		print("")
		
		ball(message)
		stop(message)
		streaming(message)
		time(message)
		left(message)
		right(message)
		up(message)
		down(message)
		me(message)
		face(message)
                
                
			
	except KeyboardInterrupt:
		exit()
		
	except sr.UnknownValueError:
		call(["pico2wave", "-w", wav, "Could not understand you"])
		call(['mplayer', wav])
		
		
	
def ball(message): # ball tracking function
	word = ["tracking","racking", "vote-rigging", "Reading", "reading", "talking", "boardtracker","checking", "fitting","Volkswagen","trekking","Trekking", "record", "voortrekker"]
	
	for i in word:
		if i in message.split(" "):
			call(["pico2wave", "-w", wav, "Executing ball tracking sequence"])
			call(['mplayer', wav])
			call(['python' ,'/home/pi/Python/demo_tracking.py'])
			
def stop(message):
	word = ["terminate", "terminix", "Termini", "terminates"]
	
	for i in word:
		if i in message.split(" "):
			call(["pico2wave", "-w", wav, "Goodbye"])
			call(['mplayer', wav])
			exit()
			
		
def streaming(message):
	word = ["camera", "timer"]
	
	for i in word:
		if i in message.split(" "):
			call(["pico2wave", "-w", wav, "Starting live streaming"])
			call(['mplayer', wav])

			call(["python","stream.py"])

                        call(["pico2wave", "-w", wav, "live stream terminated"])
			call(['mplayer', wav])			

def time(message):
	
	word = ["time", "now"]
	
	for i in word:
		if i in message.split(" "):
			call(["pico2wave", "-w", wav, "Checking current time"])
			call(["mplayer", wav])
			
			call(["python","/home/pi/Python/time.py"])
			
			
def left(message):
	word = ["left","unless","timeless","princess","less","penis","Kenya","laugh", "toddler","homeless"]
	
	for i in word:
		if i in message.split(" "):
			call(["python", "/home/pi/Python/turnLeft.py"])
			
def right(message):
	word = ["right", "sunrise"]
	
	for i in word:
		if i in message.split(" "):
			call(["python", "/home/pi/Python/turnRight.py"])

def up(message):
	word = ["up", "lookup","hook-up","co-op"]
	
	for i in word:
		if i in message.split(" "):
			call(["python", "/home/pi/Python/goUp.py"])
			
def down(message):
	word = ["down","lockdown","lookdown","milltown"]
	
	for i in word:
		if i in message.split(" "):
			call(["python", "/home/pi/Python/goDown.py"])
			
def me(message):
	word = ["me","Alchemy", "Hermes"]
	
	for i in word:
		if i in message.split(" "):
			call(["python", "/home/pi/Python/Mid.py"])

def face(message):
	word = ["face", "motion", "bass", "faith","Saif", "Space", "Faye", "Motion","Facebook"]
	
	for i in word:
		if i in message	.split(" "):
			call(["pico2wave", "-w", wav, "Executing emotion sequence"])
			call(["mplayer", wav])
		
			call(["python", "/home/pi/Python/servo-emo.py"])
			

	
		

def greet():
	call(["pico2wave", "-w", wav, 'Hi my name is alpha, nice to meet you'])
	call(["mplayer", wav])

greet()
	
while True:

	name_check()
		
	
	
	
	


