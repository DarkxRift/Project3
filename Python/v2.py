import pyaudio
from subprocess import call
import speech_recognition as sr
import RPi.GPIO as GPIO
import time

r = sr.Recognizer()
r.energy_threshold=4000


wav = 'test.wav'
message = ' ' 
next = False

def voice():
	
	try:
		with sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
			call(["pico2wave", "-w", wav, 'listening'])
                        call(["mplayer", wav])
			audio = r.listen(source)
			call(["pico2wave", "-w", wav, 'processing'])
                        call(["mplayer", wav])
		
		message = (r.recognize_google(audio, language = 'en-us', show_all=False))
		call(["pico2wave", "-w", wav, message])
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

while True:

	voice()
		
	
	
	
	


