# Copyright 2023, program coded by Miguelangel Rodriguez.

# This program let users select an edition tool for their images
# and save new images into theirs devices.

import cv2
import os
import tkinter as tk
import numpy as np
from tkinter.filedialog import *
from tkinter import *

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title('Image Editor')
    frm_main.pack(padx=50, pady=50, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Creat a brief information for users. 
    lbl_welcome = Label(frm_main, text='Select an edition tool for your Image', font='Helvetica 20')

    # Make and add the principal buttons letting user 
    # choose an edition options.
    btn_rb_img = Button(frm_main, text='Remove Background', bg='aquamarine', font='Helvetica 16')
    btn_pencil_img = Button(frm_main, text='Sketch Pencil Effect', bg='aquamarine', font='Helvetica 16')
    btn_rz_img = Button(frm_main, text='Resize/Rescale Image', bg='aquamarine', font='Helvetica 16')
    btn_bw_img = Button(frm_main, text='Black & White Image', bg='aquamarine', font='Helvetica 16')

    # Layout buttons and label in a grid.
    lbl_welcome.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
    btn_rb_img.grid(row=1, column=0, padx=15, pady=12)
    btn_pencil_img.grid(row=1, column=1, padx=15, pady=12)
    btn_rz_img.grid(row=2, column=0, padx=15, pady=12)
    btn_bw_img.grid(row=2, column=1, padx=15, pady=12)

    btn_pencil_img.config(command=sketch_image())

def sketch_image():
    """
    Convert  simple image into new image with a sketch pencil style.

    Parameter: a simple image
    Return: nothing
    """
    # Give a brief explanation to user
    print('Hola')
    # image_path = askopenfilename()

    # image = cv2.imread(image_path)

    # os.chdir(r'C:/Users/User/Desktop/convertimages/sketch')
    # directory = os.getcwd()
    # print("Before saving image:")   
    # print(os.listdir(directory)) 

    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # inverted = 250-gray_image
    # blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    # invertedblur = 255-blurred

    # pencilsketch = cv2.divide(gray_image, invertedblur, scale = 256.0)

    # filename = input('Enter the file name: ')
    # # Saving the file
    # cv2.imwrite(filename, pencilsketch)

    # print("After saving image:")    
    # print()  
    # print('Successfully saved') 

# If this file is executed like this:
# > python image_editor.py
# then call the main function.
if __name__ == "__main__":
    main()