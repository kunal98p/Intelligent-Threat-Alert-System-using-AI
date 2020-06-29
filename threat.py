

import numpy as np
import cv2
import imutils
import datetime
import os
import subprocess
from threading import Thread



gun_cascade = cv2.CascadeClassifier('cascade.xml')

camera = cv2.VideoCapture(0)

# initialize the first frame in the video stream
firstFrame = None

# loop over the frames of the video

gun_exist = False
count = 0
while True:
    (grabbed, frame) = camera.read()

    # resize the frame, convert it to grayscale, and blur it
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    if len(gun) > 0:
        gun_exist = True

    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        count = count+1
    # if the first frame is None, initialize it
    if firstFrame is None:
        firstFrame = gray
        continue

    # show the frame and record if the user presses a key
    cv2.imshow("Cam 1", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if(count > 50):
        print("Suspicious Threat Object Detected\nOther security modules activated...")
        break

if(count > 50):
    camera.release()
    cv2.destroyAllWindows()
    
    os.system("python emotions.py")
    
    
   
else:
    print("guns NOT detected")

camera.release()
cv2.destroyAllWindows()
