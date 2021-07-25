import numpy as np
import cv2
import time
import winsound
import serial

#0 is for default webcam which is the enternal webcam. Use other nos. for external webcam if '0' doesn't work
cap = cv2.VideoCapture(0)

last_elapsed_time=0
start_time=int(time.time())
subject_eyes_open=0
subject_eyes_close=0

eyes = cv2.CascadeClassifier('haarcascade_eye.xml')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        eyes_open=False
        
        #downsample
        #frameD = cv2.pyrDown(cv2.pyrDown(frame))
        #frameDBW = cv2.cvtColor(frameD,cv2.COLOR_RGB2GRAY)
    
        #detect face
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        detected = eyes.detectMultiScale(frame, 1.3, 5)
    
        #eyes = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        #detected2 = eyes.detectMultiScale(frameDBW, 1.3, 5)

        for (x,y,w,h) in detected:
            eyes_open=True
            cv2.rectangle(frame, (x,y), ((x+w),(y+h)), (0,0,255),1) 
            cv2.line(frame, (x,y), ((x+w,y+h)), (0,0,255),1)
            cv2.line(frame, (x+w,y), ((x,y+h)), (0,0,255),1)

        if eyes_open==True:
            subject_eyes_open+=1
        else:
            subject_eyes_close+=1

            
        cv2.imshow('frame', frame)


        elapsed_time=int(time.time())-start_time
        if last_elapsed_time<elapsed_time:
            print(elapsed_time)
        

        if elapsed_time==5:
            print('Duration of 5 seconds has been reached')
            print("No. of times subject's eyes found open: " + str(subject_eyes_open))
            print("No. of times subject's eyes found closed: " + str(subject_eyes_close))
            if subject_eyes_close  -  subject_eyes_open > (subject_eyes_open/2):
                print('Result: eyes closed')
                latest=time.time()
                #refers to loction in my computer, needs to be changed or can simply be written as winsound.PlaySound("Siren_Noise-KevanGC-1337458893", winsound.SND_ALIAS)
                winsound.PlaySound("C:\Users\Ansh Arora\Downloads\Siren_Noise-KevanGC-1337458893", winsound.SND_ALIAS)

            else:
                print('Result: eyes opened')
                latest=time.time()
                
            subject_eyes_open=0
            subject_eyes_close=0
            start_time=int(time.time())

        last_elapsed_time=elapsed_time
            
            

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
#Property Rights Owner - Ansh Arora (Pvt. Ltd.)
