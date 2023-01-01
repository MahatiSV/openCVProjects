import cv2
import numpy as np
img=cv2.imread("radhekrishna.jpg")
img =cv2.resize(img,(600,400))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#applying SIFT detector
sift=cv2.SIFT_create()
keypt,description=sift.detectAndCompute(img,None)
#marking the keypt on img using circles
#img=cv2.drawKeypoints(gray,keypt,img) or
img=cv2.drawKeypoints(gray,keypt,img,(120,120,0),cv2.DRAW_MATCHES_FLAGS_DEFAULT)
#cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS can be cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,cv2.DRAW_MATCHES_FLAGS_DEFAULT
cv2.imshow("KeyPoint_Image",img)
"""
SIFT------Scalar Invariant Feature Transform--is a feature detection in cv
help locate local features in an img keypts in an img
these keypts are scale,rotation invariant used in various cv like
obj detection
img matching
scene detection
major advantage of sift is over edge features
not affected by size or orientation of img
------Steps for extracting  interest pt:
scale space peek selection(constructing a scale space)--make sure sccale-independent---Gaussian blur to reduce noise
keypt localization--find local maxima and minima,remove low contrast keypts(unwanted)
orientation assignment
keypt descriptor
----Different of Gaussian(DOG)--creates another set of imgs
cv2.drawKeypoints()--grayimg,key_pts,o.p img,color,
flag
 -cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
 -cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
 -cv2.DRAW_MATCHES_FLAGS_DEFAULT
cv2.xfeatures2d.SIFT_create() or cv2.SIFT_create()
"""
