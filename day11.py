import cv2
import numpy as np
#img=np.zeros((400,400,3),np.uint8)#doubt
"""cv2.circle(img,(180,170),80,(255,255,255),4)
cv2.imshow("dark",img)
cv2.rectangle(img,(40,30),(200,300),(0,232,255),4)
cv2.imshow("Dark",img)
cv2.line(img,(100,230),(320,450),(231,7,0),5)
cv2.imshow("Dark",img)"""
img=cv2.imread("radhekrishna.jpg")
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"RadhaKrishna",(15,105),font,1,(200,25,25),6)
cv2.imshow("Dark",img)

"""draw circle
cv2.circle(img,center,radius,color,thickness)
draw rectangle
cv2.rectangle(img,pt1,pt2,color,thickness)
pt1--vertex of rectangle
pt2--vertex of rect opp to pt1
draw line
cv2.line(img,pt1,pt2,color,thickness)
write text on img
cv2.putText(img,text,org,font,color)
org--text start pt coords
font--font size
color--color of texts
"""
