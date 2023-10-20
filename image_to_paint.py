# This program could convert a simple image
# to a sketch image to paint on it. This process
# needs apply 3 filters after the final result.

import cv2
import os
import numpy as np
from tkinter.filedialog import *
from tkinter import *

image_path = askopenfilename()

image = cv2.imread(image_path)

os.chdir(r'C:/Users/User/Desktop/convertimages/sketch')
directory = os.getcwd()
print("Before saving image:")   
print(os.listdir(directory)) 

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255-gray_image
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
invertedblur = 255-blurred

pencilsketch = cv2.divide(gray_image, invertedblur, scale = 256.0)

filename = input('Enter the file name: ')
# Saving the file
cv2.imwrite(filename, pencilsketch)

print("After saving image:")    
print()  
print('Successfully saved') 