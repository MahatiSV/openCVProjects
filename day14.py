import cv2
import numpy as np
img=cv2.imread("radhekrishna.jpg") #give img input here
img=cv2.resize(img,(600,400))

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

clahe=cv2.createCLAHE(clipLimit=5)
fin_img=clahe.apply(img)
cv2.imshow("Gray img",img)
cv2.imshow("Final Img After AHE",fin_img)
"""for HE
#after resize
equ=cv2.equalizeHist(img)
image=np.hstack((img,equ)) #hstack for merging img,equ
#cv2.imshow("Original",img) 
cv2.imshow("Equalized",image)
--------------------------------
darker intensity-0(Black)
else white 1
histogram equalization--method in img processing of contrast adjustment using img histogram
The method is useful in imgs with bgs and fgs that are both bright or both dark
cv2.equalizeHist(img)
Parameters:
Gray level(rK)
no of pixel(nK)
Prob Distr Fun(PDF=nk/n)
Cumulative distr Fun
---------------------
Adaptive Histogram Equalization (AHE)
cv2.createCLAHE(clipLimit)
clipLimit--default 40
titleGridSize--default 8X8
CLAHE--clip limiting AHE
"""

