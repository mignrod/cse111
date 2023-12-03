# Copyright 2023, program coded by Miguelangel Rodriguez.

# This program let users select an edition tool for their images
# and save new images into theirs devices.

import cv2
import os
import tkinter as tk
import numpy as np
from tkinter.filedialog import *
from tkinter import *
import sys
from PIL import Image, ImageTk
import imutils


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    global frm_main
    frm_main = Frame(root)
    frm_main.master.title('Image Editor')
    frm_main.pack(padx=50, pady=50)

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
    btn_clear = Button(frm_main, text='Clear', bg='black', fg='white', font='Helvetica 16')
    btn_exit = Button(frm_main, text='Exit', bg='red', fg='white', font='Helvetica 16')

    #Create a status bar
    global lbl_status
    lbl_status = Label(frm_main, text='', padx=50, pady=20)

    # Layout buttons and label in a grid.
    lbl_welcome.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
    btn_rb_img.grid(row=1, column=0, padx=15, pady=12)
    btn_pencil_img.grid(row=1, column=1, padx=15, pady=12)
    btn_rz_img.grid(row=2, column=0, padx=15, pady=12)
    btn_bw_img.grid(row=2, column=1, padx=15, pady=12)
    lbl_status.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    btn_clear.grid(row=4, column=0, padx=10, pady=12)
    btn_exit.grid(row=4, column=1, padx=10, pady=12)

    # Give commands for every tool
    btn_pencil_img.config(command=sketch_image)

    def clear():
        """
        Clear the message and let user select another tool.
        """
        btn_clear.focus()
        lbl_status.config(text='')

    # Configure clear and exit buttons
    btn_clear.config(command=clear)
    btn_exit.config(command=sys.exit)

def sketch_image():
    """
    Convert  simple image into new image with a sketch pencil style.

    Parameter: a simple image
    Return: nothing
    """
    msg = lbl_status['text']
    msg = 'Select Image'
    lbl_status.config(text=msg, font='Helvetica 16')

    # Select file from device
    image_path = askopenfilename()
    image = cv2.imread(image_path)

    # Show a message in the status label
    msg = 'Processing Image'
    lbl_status.config(text=msg, font='Helvetica 16')

    # Edit image and convert
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 250-gray_image
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    invertedblur = 255-blurred

    # Save image in a variable called pencilsketch
    pencilsketch = cv2.divide(gray_image, invertedblur, scale = 256.0)

    # Ask user folder and name to save the image
    filename = asksaveasfilename()

    # Saving the file
    cv2.imwrite(filename, pencilsketch)

    # Show a message for complete operation
    msg = 'Image Saved Successfully!'
    lbl_status.config(text=msg, font='Helvetica 16', fg='green')

    # Show Image
    show_images(pencilsketch)
    
    
def show_images(image):
    """
    Show edited images
    """ 
    root = Toplevel(frm_main)
    root.geometry('400x400')
    root.title('Output Image')

    # Catch Output Image
    image = imutils.resize(image, height=100, width=100)
    image_to_show = image
    im = Image.fromarray(image_to_show)
    img = ImageTk.PhotoImage(image=im)
    

    img = Label(root, image=img)    
    root.mainloop()




# If this file is executed like this:
# > python image_editor.py
# then call the main function.
if __name__ == "__main__":
    main()