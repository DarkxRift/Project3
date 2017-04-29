from subprocess import call
import time

wav = "test.wav"

c_time = time.strftime("%H:%M")
		
call(["pico2wave", "-w", wav,"Current Time is " + c_time])
call(["mplayer", wav])
