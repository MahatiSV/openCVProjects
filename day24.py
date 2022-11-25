import cv2
import numpy as np

face_detector1=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_detector1=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

cap=cv2.VideoCapture(0) #accessing cam
while(1):
    # Capture frame-by-frame
    res,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_detector1.detectMultiScale(gray)

    # Draw a rectangle around the faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    # Display the resulting frame
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) &0xFF==ord('q'):
        break
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

