"""otsu thresholding
thresholding used to binarize img based on pixel intensities
simplest kind of img segmentation--white for foregrnd,black for bg
specify threshold value manually for good threshold
in otsu threshold automatic determine the threshold
otsu---used to automatically find optimal threshold intensity
concept
process i/p
obtain histogram
compute threshold val T
replace img pixels into white in those regions where saturation is > T and into
black in opposite
otsu is applied to img which are bimodal means img having two peaks in histogram


aim is to find min T where sum of fg and bg spreads is at its min
T cal as sum of weighted variance--within class variance
cv2.threshold(image,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU"""
import cv2
import numpy as np

img=cv2.imread("radhekrishna.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh1=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
_,thresh=cv2.threshold(img,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("gray image",img)
cv2.imshow("Thresh",thresh1)
cv2.imshow("OTSU Image",thresh)
cv2.waitKey(0)
