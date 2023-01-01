import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Users\12243\AppData\Local\Programs\Tesseract\tesseract-ocr-w64-setup-v5.2.0.20220712.exe'
img=cv2.imread("text1.jpg")
text=pytesseract.image_to_string(img)
print(text)
cv2.imshow("original_image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Optical Char Recognition---machine read text
Application:
-Passport recog in Airports
-Automation of Data Entry
-Licenses plates recognition
-Converting handwritten doc into electronic img
-create audio files(text or audio)
Tesseract OCR---can be used directly or using an API to extract printed
text from imgs
----------------------
Converting img to str
need pytesseract
set the pytesseract path in code
convert an img to str
----------------------
create audio file
gTTS is a py lib with Google Translates Text-Speech API
install:pip install gtts
import necessary libs
set tesseract path
img reading
grab text from img using tesseract
set lang
convert text 2 audio
save audio
play audio file
"""
