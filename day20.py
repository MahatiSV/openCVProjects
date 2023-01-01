import cv2
import numpy as np
cap=cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()
while(1): #reading frame
    res,img=cap.read()
    fgmask=fgbg.apply(img)
    cv2.imshow("original",img)
    cv2.imshow("fgmask",fgmask)
    k=cv2.waitKey(30)& 0xff
    if k==27:
       break
cv2.release()
cv2.destroyAllWindows()
"""
bg substraction (BS)
extracting moving fg from static bg
used for obj seg,security enhancement,cnting no.of visitors,no.of vehicle in traffic
It is open to learn and identify fg mask
How BS works?
BS calc fg mask performing a - b/w cur frame &bg model
BG model
2-step: bg initialization,bg update
read data from vdeo--cv2.VideoCapture()
create and update bg model--cv2.BackgroundSubtractor()
get and show fg mask by cv2.imshow()
3 algorithms
--BackgroundSubtractorMOG -->gaussian mixture based segmen algo
--BackgroundSubtractorMOG2 -->also as above but it provides better adaptability to varying scenes due to illumination changes
--BackgroundSubtractorCMG -->
/////Steps:
create an obj to signify algo we are using bg subtraction
apply BackgroundSubtractor.apply() fun on img

"""
