import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():

    pic_num = 1
    
        
    for i in "/home/pi/negatives_images":
        try:
            print(i)
            img = cv2.imread("/home/pi/negatives_images/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("/home/pi/negatives_images/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
            
        except Exception as e:
            print(str(e))
            
            
def find_uglies():
    match = False
    for file_type in ['/home/pi/negatives_images/']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('/home/pi/uglies/'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('/home/pi/uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

store_raw_images()
