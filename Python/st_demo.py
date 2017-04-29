from subprocess import call

call(["python", "stream.py", "&"])

text = input("type here:")
if text == 'q':
	call(["sh", "/home/pi/kill.sh"])
	
        call(["pico2wave", "-w", wav, "live streaming is terminated"])
        call(['mplayer', wav])
