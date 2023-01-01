import cv2
import numpy as np
img=cv2.imread("radhekrishna.jpg") #load
cv2.imwrite("radhekrishna.jpg",img)#save img
cv2.imshow("RadhaKrishn",img)#show img
cv2.waitKey(0)
