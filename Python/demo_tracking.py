# import the necessary packages
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)

servoPINX = 23
servoPINY= 24

GPIO.setup(servoPINX, GPIO.OUT)
GPIO.setup(servoPINY, GPIO.OUT)

pX= GPIO.PWM(servoPINX, 50)
# GPIO 18 als PWM mit 50Hz 
pY= GPIO.PWM(servoPINY, 50) 
# initial position
pX.start(4) 
# initial position
pY.start(4) 
time.sleep(1)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

pX_val = 5.6
pY_val = 3.8

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array

        blur = cv2.blur(image, (1,1))

        #hsv to complicate things, or stick with BGR
        #hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
        #thresh = cv2.inRange(hsv,np.array((100, 31, 4)), np.array((140, 90, 70)))

        lower = np.array([100, 31, 4],dtype="uint8")
        #upper = np.array([225,88,50], dtype="uint8")
        upper = np.array([140, 90, 70], dtype="uint8")

        thresh = cv2.inRange(blur, lower, upper)
        thresh2 = thresh.copy()

        # find contours in the threshold image
        image, contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        # finding contour with maximum area and store it as best_cnt
        max_area = 0
        best_cnt = 1
        for cnt in contours:

                area = cv2.contourArea(cnt)
                if area > max_area:
                        max_area = area
                        best_cnt = cnt
        # finding centroids of best_cnt and draw a circle there
        M = cv2.moments(best_cnt)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])

        print('x =', cx,  ' y = ', cy)

        if cx < 320 and pX_val < 8.5:
                
                pX_val -= 0.2
                time.sleep(0.1)

                if pX_val < 2.5:
                      pX_val += 0.2  
                

        elif cx > 320 and pX_val > 2.5:

                pX_val += 0.2
                time.sleep(0.001)

                if pX_val > 8.5:
                      pX_val -= 0.2        

                
        if cy > 240 and pY_val < 7.5:
                
                pY_val -= 0.2
                time.sleep(0.1)

                if pY_val < 3:
                      pY_val += 0.2  

        elif cy < 240 and pY_val > 3:

                pY_val += 0.2
                time.sleep(0.1)

                if pY_val > 7.5:
                      pY_val -= 0.2  

       
        pX.ChangeDutyCycle(pX_val)
        pY.ChangeDutyCycle(pY_val)
        
        #if best_cnt>1:
        cv2.circle(blur,(cx,cy),10,(0,0,255),-1)
        # show the frame
        cv2.imshow("Frame", blur)
        #cv2.imshow('thresh',thresh2)
        key = cv2.waitKey(1) & 0xFF
 
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
 
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break
