#importing required packages
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

#initialize mediapipe
mpHands=mp.solutions.hands
hands=mpHands.Hands(max_num_hands=1,min_detection_confidence=0.7)
myDraw=mp.solutions.drawing_utils

#load the gesture recognition model
model=load_model('mp_hand_gesture')

#load class names
f=open('gesture.names','r')
classNames=f.read().split('\n')
f.close()
print(classNames)

#Initialize webcam
cap=cv2.VideoCapture(0)

while True:
    #read each frame from webcam
    _,frame=cap.read()
    x ,y, c=frame.shape

    #flip frame vertically
    frame=cv2.flip(frame,1)
    framergb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    #get hand landmark prediction
    result=hands.process(framergb)
    #print(result)
    className=''

    #post process the result
    if result.multi_hand_landmarks:
        landmarks=[]
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx=int(lm.x*x)
                lmy=int(lm.y*y)

                landmarks.append([lmx,lmy])
            #drawing landmarks on frames
            myDraw.draw_landmarks(frame,handslms,mpHands.HAND_CONNECTIONS)

            #predict gestures
            prediction=model.predict([landmarks])
            #print(prediction)                      
            classID=np.argmax(prediction)
            className=classNames[classID]
    #show prediction of frame
    cv2.putText(frame,className,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    #show final o/p
    cv2.imshow("Output",frame)
    if cv2.waitKey(1)==ord('q'):
        break
#release webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
            
"""Hand Gesture recognition using media pipe framework,tensorflow in open cv and python
MEDIA PIPE is a customizable ML solutions framework
open src and cross-platform framework and light-weight
comes with some pre-trained ML solutions like
--face detection
--pose estimation
--hand recognition
--object detection
Tensor FLow is an open src lib for ML and DL
It can be used across a range of tasks but has a particular focus on deep neural n/w

have opencv  pip install opencv-python
pip install mediapipe
pip install tensorflow

STEPS:
import packages
initialize models
read frames from webcam
detect hand keypoints
Used file
Model
 -gand detection
  Mp.solutions.hands
-prediction for gestures
  mp_hand_gesture
Gesture Name
 gestures_names
"""
