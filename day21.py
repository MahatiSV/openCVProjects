import cv2
import numpy as np
img=cv2.imread("radhekrishna.jpg")
template=cv2.imread("radhekrishnaLogo.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
tmpGray=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

res=cv2.matchTemplate(imgGray,tmpGray,cv2.TM_CCOEFF_NORMED)
(minVal,maxVal,minLoc,maxLoc)=cv2.minMaxLoc(res)
startX,startY=maxLoc
endX=startX+template.shape[1]
endY=startY+template.shape[0]
cv2.rectangle(img,(startX,startY),(endX,endY),(255,0,0),3)
cv2.imshow("output",img)
cv2.waitKey(0)
"""
Method of TM
Template Matching is a technique for proces of moving template over entire img and calc similarity
b/w template and larger img
the idea here is to find identical regions of an img that match a template we provide
we can see func-----cv2.matchTemplate(),cv2.minMaxLoc()
.........Process.........
done by comparing each of pixel values of src img one at a time to template img
o.p would be an array of similarity values when compared to the template img
....How does TM works
template img (TI) simply slide over i.p img
template and patch of i.p img under TI are compared
result obtained is compared with threshold
if res>threshold the portion will be marked detected
.....
cv2.matchTemplate(img_gray,temp_gray,cv2.TM_CCOEFF_NORMED)
main img,TI,method for matching
//
The res matrix will have a larger value (closer 2 1)where there's likely to tmp match
viceversa cond also
to find looca with largest val and therfore most likely match,we call cv2.minMaxLoc passing re matrix

"""
