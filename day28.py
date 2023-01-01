import cv2
import easygui
import numpy as np
import imageio
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from PIL import ImageTk,Image
top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label=tk.Label(top,background='#CDCDCD', font=('calibri',20,'bold'))

def upload():
    ImagePath=easygui.fileopenbox()
    cartoonify(ImagePath)

def cartoonify(ImagePath):
    #read img
    originalImg=cv2.imread(ImagePath)
    originalImg=cv2.cvtColor(originalImg,cv2.COLOR_BGR2RGB)

    if originalImg is None:
        print("Cannot find any img,choose appropriate file")
        sys.exit()
    ReSized1=cv2.resize(originalImg,(960,540))
    #plt.imshow(ReSized1,cmap='gray')

    #converting an img to gray scale
    grayScaleImg=cv2.cvtColor(originalImg,cv2.COLOR_BGR2GRAY)
    ReSized2=cv2.resize(grayScaleImg,(960,540))
    #plt.imshow(ReSized2,cmap='gray')

    #applying median blur ro smoothen an img
    smoothGrayScale=cv2.medianBlur(grayScaleImg,5)
    ReSized3=cv2.resize(smoothGrayScale,(960,540))
    #plt.imshow(ReSized3,cmap='gray')

    #retrieving edges for cartoon effect by using thresholding technique
    getEdge=cv2.adaptiveThreshold(smoothGrayScale,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9) #because it works irrespective of high or low light img
    ReSized4=cv2.resize(getEdge,(960,540))
    #plt.imshow(ReSized4,cmap='gray')

    #applying bilateral filter to remove noise and keep edge sharpp as required
    colorImg=cv2.bilateralFilter(originalImg,9,300,300) #returns img as waterpaint like thing
    ReSized5=cv2.resize(colorImg,(960,540))
    #plt.imshow(ReSized5,cmap='gray')

    #masking edged img with our "BEAUTIFY" img
    cartoonImg=cv2.bitwiseFilter(originalImg,colorImg,mask=getEdge)

    ReSized6=cv2.resize(cartoonImg,(960,540))
    #plt.imshow(ReSized6,cmap='gray')
    #plotting the whole transition
    images=(ReSized1,ReSized2,ReSized3,ReSized4,ReSized5,ReSized6)
    fig,axes=plt.subplots(3,2,figsize=(8,8),subplot_kw={'xticks':[],'yticks':[]},gridspec_kw=dict(hspace=0.1,wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    save1=tk.Button(top,text="Save cartoon image",command=lambda: save(ImagePath, ReSized6),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
    save1.pack(side="top",pady=50)
    plt.show()

def save(ReSized6, ImagePath):
    #saving an image using imwrite()
    newName="cartoonified_Image"
    path1 = os.path.dirname(ImagePath)
    extension=os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name " + newName +" at "+ path
    tk.messagebox.showinfo(title=None, message=I)

upload=Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=50)

top.mainloop()
"""
---Cartoonifying an Image---
Steps:
import libraries
build the file box to choose a particular file
img stored
transforming an img to gray
smoothening a gray img
retreiving edges
preparing masks
giving cartoon effect
LIBRARIES
cv2
easygui--imported to open a file box.Allows us to select any file from our sys
numpy--imgs stored and processed as numbers.These are taken as arrays
imageio--used to read file which is chosen by file box using a path
matplotlib--used for visualization and plotting,it's imported to form the plot of imgs
os--for os interaction
"""
