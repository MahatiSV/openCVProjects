import cv2
import numpy as np
"""rectangle=np.zeros((300,300),dtype='uint8')
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("rectangle",rectangle)

circle=np.zeros((300,300),dtype='uint8')
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("circle",circle)

bitwise_and=cv2.bitwise_and(rectangle,circle)
bitwise_or=cv2.bitwise_or(rectangle,circle)
bitwise_xor=cv2.bitwise_xor(rectangle,circle)

cv2.imshow("AND",bitwise_and)
cv2.imshow("OR",bitwise_or)
cv2.imshow("XOR",bitwise_xor)"""
#process of masking
#3 steps
#create black canvas with same dimension as an image
#changing values of mask by drawing any fig in img and providing it with a white color
#performing bitwise ADD oper on img with mask

img=cv2.imread("radhekrishna.jpg")
img=cv2.resize(img,(500,500))
cv2.imshow("Original",img)

mask=np.zeros(img.shape[:2],dtype='uint8') #doubt?????? ones--white bg
#cv2.rectangle(mask,(100,100),(400,400),255,-1)
cv2.circle(mask,(290,180),120,255,-1)

masked_img=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("MaskedImage",masked_img)

