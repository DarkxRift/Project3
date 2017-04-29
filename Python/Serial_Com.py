import serial

ser = serial.Serial('/dev/ttyACM0',9600)

while True:
	read_line =ser.readline().split("\n")
	print (read_line[0])
