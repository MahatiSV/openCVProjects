import cv2
import numpy as np
img=cv2.imread("radhekrishna.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original img",img)
res,thresh=cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print("No of contours:"+str(len(contours)))
cv2.drawContours(img,contours,-1,(0,255,0),2)
cv2.imshow("Gray img",gray)
cv2.imshow("Bin_img",thresh)
cv2.imshow("Draw_Contours",img)
#contour detection----day7
"""contour defined as a curve joining all continous pts having same color or intensity
contours are useful tool for
shape analysis
obj detection
recognition
Application:
motion detection
unattended obj detection
bg/fg segmentation      -1===all contours 1 1st contour
////
find and draw contour:
cv2.findContours(),cv2.drawContours()
algorithms for contour detection
cv2.CHAIN_APPROX_SIMPLE
cv2.CHAIN_APPROX_NONE--time taking
STEPS:
read img and convert RGB into GRAY img
why gray?needed for thresholding,also can perform perfect contour algorithms
apply bin thresholding
cv2.THRESH_BINARY
find contour(img,mode,method),draw contour(img,contours,contourIDx,color,thickness)

"""
