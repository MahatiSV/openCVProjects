#day-4 Edge Detection
#usually changes happen b/w boundaries of objs in imgs
#steps in edge detection i/p img -> imgs smoothening -> edge pt detection -> edge localization -> o/p
#edges are detected through identifying sudden changes in intensity
#edge localization-->locate edges appropriately,linking
#Types:Sobel edge detector Canny edge detector
#sobel:finding edges in x,y directions then finding gradient at every pixel so related to gradient type
#steps: converting img into grayscale
#convolving gray img with sobel-x filter; convolving gray img with sobel-y filter
#calc gradient magnitude and dir
import cv2
import numpy as np
img=cv2.imread("radhekrishna.jpg") 
#cv2.imshow("Original_img",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray_img",gray) #64F--for depth
sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
#cv2.imshow("Sobel_Edgesx",sobelx)
sobely=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
#cv2.imshow("Sobel_Edgesy",sobely)
laplacian=cv2.Laplacian(gray,cv2.CV_64F)
#cv2.imshow("Laplacian",laplacian)

blur=cv2.GaussianBlur(img,(5,5),0)
canny=cv2.Canny(blur,100,200)
cv2.imshow("Canny edges",canny) #clean output when compared to sobel

