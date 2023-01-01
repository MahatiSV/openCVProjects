import cv2
import numpy as np
img=cv2.imread("radhekrishna.jpg")
kernal=np.ones((5,5),np.uint8)
dilation=cv2.dilate(img,kernal)
erosion=cv2.erode(img,kernal)
morphology=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)
morphologyClose=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)
morphologyGradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernal)

cv2.imshow("Morphology",morphology)
cv2.imshow("Morphology_Close",morphologyClose)
cv2.imshow("Morphology_Gradient",morphologyGradient)
cv2.imshow("Original",img)
cv2.imshow("Dilation",dilation)
cv2.imshow("Erosion_img",erosion)
"""Morphological techniques
---used to extract img components that r helpful for desc and repre of shape of region
---require i/p img,struct component
Basic morphological operations--
erosion--shorten img,
reduce no.of pixel of boundaries of img
dilation--expand img
add no.of pixel of boundaries of img
Morphology transform--
open--used for removing internal noise of img
      erosion followed by dilation
close-dilation followed by erosion
"""
