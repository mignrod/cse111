# Copyright 2023, program coded by Miguelangel Rodriguez.

# This program let users select an edition tool for their images
# and save new images into theirs devices.

import cv2
import os
import tkinter as tk
import numpy as np
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import sys
from PIL import Image, ImageTk
import imutils


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create a fixed size for window
    # and a minimum size in resized mode.
    root.geometry('850x630+30+30')
    root.minsize(width=400, height=300)

    # Create the main window. In tkinter,
    # a window is also called a frame.
    global frm_main
    frm_main = Frame(root)
    frm_main.master.title('Image Editor')
    frm_main.pack(padx=5, pady=5)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

# Create label to show input image
def select_image():
    """
    Let select image for edition. We can see the selected image before the edition
    toll selection. 
    Parameter:
    Return: nothing
    """
    image_path = filedialog.askopenfilename(filetypes=[
        ('image', '.jpg'),
        ('image', '.jpeg'),
        ('image', '.png')])

    if len(image_path) > 0: 
        global image

        # Read input image
        image = cv2.imread(image_path)
        image = imutils.resize(image, height=330)

        # Show input image in the GUI
        image_to_show = imutils.resize(image, width=200)
        image_to_show = cv2.cvtColor(image_to_show, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(image_to_show)
        img = ImageTk.PhotoImage(image=im)

        lbl_input_image.configure(image=img)
        lbl_input_image.image = img
    
def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """    
    # image = None
    # Creat a brief information for users. 
    lbl_welcome = Label(frm_main, text='Select an Image to Edit', font='Helvetica 16', bg='red')

    # Create labels in which images are shows
    lbl_info_input_img = Label(frm_main, text='Input Image', width=40, font='Helvetica 10', bd=2)
    global lbl_input_image
    lbl_input_image = Label(frm_main, width=40)
    lbl_info_ouput_img = Label(frm_main, text='Output Image', width=40, font='Helvetica 10', bd=2)
    global lbl_output_image
    lbl_output_image = Label(frm_main, width=80, bg='beige')

    # Make and add the principal buttons letting user 
    # choose an edition options.
    btn_select_img = Button(frm_main, text='Select Image', font='Helvetica 12', width=30, command=select_image)
    btn_rb_img = Button(frm_main, text='Remove Background', bg='aquamarine', font='Helvetica 10')
    btn_pencil_img = Button(frm_main, text='Sketch Pencil Effect', bg='aquamarine', font='Helvetica 10', command=sketch_image)
    btn_rz_img = Button(frm_main, text='Resize/Rescale Image', bg='aquamarine', font='Helvetica 10')
    btn_bw_img = Button(frm_main, text='Black & White Image', bg='aquamarine', font='Helvetica 10')
    btn_clear = Button(frm_main, text='Clear', bg='black', fg='white', font='Helvetica 10')
    btn_exit = Button(frm_main, text='Exit', bg='red', fg='white', font='Helvetica 10')

    #Create a status bar
    global lbl_status
    lbl_status = Label(frm_main, text='', padx=5, pady=5)

    # Layout buttons and label in a grid.
    lbl_welcome.grid(row=0, column=0, columnspan=3, padx=10, pady=6, sticky='nsew')
    btn_select_img.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    lbl_info_input_img.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')
    lbl_input_image.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')
    btn_rb_img.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')
    btn_pencil_img.grid(row=4, column=1, padx=5, pady=5, sticky='nsew')
    btn_rz_img.grid(row=5, column=0, padx=5, pady=5, sticky='nsew')
    btn_bw_img.grid(row=5, column=1, padx=5, pady=5, sticky='nsew')
    lbl_status.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')
    btn_clear.grid(row=7, column=0, padx=5, pady=5, sticky='nsew')
    btn_exit.grid(row=7, column=1, padx=5, pady=5, sticky='nsew')
    lbl_info_ouput_img.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')
    lbl_output_image.grid(row=2, column=3, rowspan=5, padx=5, pady=5, sticky='nsew')

    # Give commands for every tool
    # btn_pencil_img.config(command=sketch_image)

    def clear():
        """
        Clear the message and let user select another tool.
        """
        btn_clear.focus()
        lbl_status.config(text='')
        lbl_input_image.config(image='')
        lbl_output_image.config(image='')

    # Configure clear and exit buttons
    btn_clear.config(command=clear)
    btn_exit.config(command=sys.exit)

def sketch_image():
    """
    Convert  simple image into new image with a sketch pencil style.

    Parameter: a simple image
    Return: nothing
    """
    # Get the image selected
    image

    # Edit image and convert
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 250-gray_image
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    invertedblur = 255-blurred

    # Save image in a variable called pencilsketch
    pencilsketch = cv2.divide(gray_image, invertedblur, scale = 256.0)

    # Ask user folder and name to save the image
    filename = filedialog.asksaveasfilename()

    # Saving the file
    cv2.imwrite(filename, pencilsketch)

    # Show a message for complete operation
    msg = 'Image Saved Successfully!'
    lbl_status.config(text=msg, font='Helvetica 14', fg='green')

    # Show Image
    show_images(pencilsketch)
    
    
def show_images(image):
    """
    Show edited images
    """ 
    # Catch Output Image
    image = imutils.resize(image, height=100, width=100)
    image_to_show = image
    im = Image.fromarray(image_to_show)
    img = ImageTk.PhotoImage(image=im)

    lbl_output_image.configure(image=img)
    lbl_output_image.image = img

# If this file is executed like this:
# > python image_editor.py
# then call the main function.
if __name__ == "__main__":
    main()