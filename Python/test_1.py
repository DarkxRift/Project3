import cv2
import serial
import numpy as np
import RPi.GPIO as gpio
def empty(z):
    pass
height=120
width=160
cross=width/2
centre=height/2
segment=height/5
minArea=800
maxArea=5000
ser=serial.Serial('/dev/ttyACM0',9600,timeout=100)
cam = cv2.VideoCapture(0)
if cam.isOpened():
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,120)
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,160)
while (True):
    ret,frame = cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    image_mask=cv2.inRange(hsv,np.array([0,81,66]),np.array([92,222,189]))    
    erode=cv2.erode(image_mask,None,iterations=3)
    moments=cv2.moments(erode,True)
    area=moments['m00']
    if moments['m00'] >=minArea:
        x=moments['m10']/moments['m00']
        y=moments['m01']/moments['m00']
        cv2.circle(frame,(int(x),int(y)),5,(0,255,0),-1)
        if (y>centre):
                ser.write('2')       
        elif (y<centre):
                ser.write('1')
        print area
    if (area<minArea ):
        ser.write('3')
    
    if area>maxArea:
        ser.write('4')
    
    if area==0:
        ser.write('5')
    cv2.imshow('eroded',erode)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==27:
        break
       

cv2.destroyAllWindow()
cam.release()
