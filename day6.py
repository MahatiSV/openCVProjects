import cv2
import numpy as np
img=cv2.imread("radhekrishna.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

res,thresh=cv2.threshold(img,125,255,cv2.THRESH_BINARY)
res,thresh2=cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)
res,thresh3=cv2.threshold(img,125,255,cv2.THRESH_TRUNC)
res,thresh4=cv2.threshold(img,125,255,cv2.THRESH_TOZERO)
res,thresh5=cv2.threshold(img,125,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("Thresh_Binary",thresh)
cv2.imshow("Thresh_Binary_Inv",thresh2)
cv2.imshow("Thresh_Trunc",thresh3)
cv2.imshow("Thresh_Trunc2Zero",thresh4)
cv2.imshow("Thresh_Trunc2Zero_Inv",thresh5)
"""Threshold techniques--img segmentation--extract fg from bg
-done using img pixel value
Process of thresholding
comparing each pixel value of img to spec threshold
this divides all pixels of i/p img into grps

pixel intensity<thresh---black(0)
>--white(1)
Basic thresholding is binary
------------cv2.THRESH_BINARY-----------
if pixl val>thresh set val to 255 else 0
cv2.threshold(img,120,255,cv2.THRESH_BINARY)
------------cv2.THRESH_BINARY_INV-------
------------cv2.THRESH_TRUNC------------
if intensity>thresh val--truncated to threshold
------------cv2.THRESH_TOZERO-----------

set to src(x,y) if(src(x,y)>thresh 0 otherwise
------------cv2.THRESH_TOZERO_INV-------
"""

