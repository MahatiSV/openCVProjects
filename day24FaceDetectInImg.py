import cv2
import numpy as np

face_detector1=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_detector1=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

img=cv2.imread("radhekrishna.jpg")
img=cv2.resize(img,(700,500))
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_detector1.detectMultiScale(grayImg)
print(type(faces))   #returns matrix

if(len(faces)==0):
    print("No faces found!!")
else:
    print(faces)
    print(faces.shape)
    print("Number of faces detected: "+str(faces.shape[0]))

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.rectangle(img,((0,img.shape[0]-25)),(270,img.shape[0]),(255,255,0),-1)
    cv2.putText(img,"Number of faces detected: "+str(faces.shape[0]),(0,img.shape[0]-10),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0),1)

    cv2.imshow('Image with faces',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
