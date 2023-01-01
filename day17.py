import cv2
import numpy as np
img=cv2.imread("radhekrishna.jpg")
img=cv2.resize(img,(600,400))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
_,threshold=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
i=0
for c in contours:
    if i==0:
        i=1
        continue
    approx=cv2.approxPolyDP(c,0.04*cv2.arcLength(c,True),True)
    cv2.drawContours(img,[c],-1,(0,0,0),4)
    #find center of shape
    M=cv2.moments(c)
    if M['m00']!=0.0:
        x=int(M['m10']/M['m00'])
        y=int(M['m01']/M['m00'])
    #shape
        if len(approx)==3:
            cv2.putText(img,'triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),2)
        elif len(approx)==4:
            cv2.putText(img,'Quadrilateral',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),2)
        elif len(approx)==5:
            cv2.putText(img,'Pentagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),2)

        elif len(approx)==6:
            cv2.putText(img,'Hexagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),2)
        else:
            cv2.putText(img,'Circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),2)
    cv2.imshow('shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

        



"""
import module
import img
convert the gray scale
apply thresholding
find the contours
run a loop in range of contours and iterate through it
in this loop draw a outline of shapes and find out center point
classify detected shape on basis of no.of contour pts it has
cv2.findContours()
ip img
contour retrieval
cv2.RETR_EXTERNAL--retrieves only extreme outer contours
cv2.RETR_LIST--retrievs all contours without establishing any hierarchial rss
cv2.RETR_TREE-- ""      ""     ""    and establishing hierarchial rss
contour approximations
cv2.CHAIN_APPROX_NONE ---stores all boundary pts
cv2.CHAIN_APPROX_SIMPLE --performs very well
cv2.approxPolyOP(ip curve,epsilon,closed)
epsilon--max dist between approx and original

"""
