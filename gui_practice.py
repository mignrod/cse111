from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import tkinter as tk
import cv2
import imutils
import numpy as np

def detect_color():
    global image
    if selected.get() == 1:
        # Red was selected
        rng_down1 = np.array([0, 140, 90], np.uint8)
        rng_high1  = np.array([8, 255, 255], np.uint8)
        rng_down2 = np.array([160, 140, 90], np.uint8)
        rng_high2 = np.array([180, 255, 255], np.uint8)
    
    if selected.get() == 2:
         # Yellow was selected
        rng_down = np.array([10, 98, 0], np.uint8)
        rng_high  = np.array([25, 255, 255], np.uint8)

    if selected.get() == 3:
         # Blue was selected
        rng_down = np.array([88, 104, 121], np.uint8)
        rng_high  = np.array([99, 255, 243], np.uint8)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    


def select_image():
    path_image = filedialog.askopenfilename(filetypes=[
        ('image', '.jpg')
        ('image', '.jpeg')
        ('image', '.png')
    ])

    if len(path_image) > 0:
        global image

        image = cv2.imread(path_image)
        image = imutils.resize(image, height=380)

        image_to_show = imutils.resize(image, width=180)
        image_to_show = cv2.cvtColor(image_to_show, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(image_to_show)
        img = ImageTk.PhotoImage(image=im)

        lbl_input_image.configure(image=img)
        lbl_input_image.image = img

        lbl_info1 = Label(root, text='Input Image')
        lbl_info1.grid(column=0, row=1, padx=5, pady=5)

image = None

root = tk.Tk()

lbl_input_image = Label(root)
lbl_input_image.grid(column=0, row=2)

lbl_output_image = Label(root)
lbl_output_image.grid(column=1, row=1)

lbl_info2 = Label(root, text='What color would you like to highlight?')
lbl_info2.grid(column=0, row=3, padx=5, pady=5)

selected = IntVar()
rad1 = Radiobutton(root, text='Red', width=25, value=1, variable=selected, command=detect_color)
rad2 = Radiobutton(root, text='Yellow', width=25, value=2, variable=selected, command=detect_color)
rad3 = Radiobutton(root, text='Blue', width=25, value=3, variable=selected, command=detect_color)
rad1.grid(column=0, row=4)
rad2.grid(column=0, row=5)
rad3.grid(column=0, row=6)

btn_select_img = Button(root, text='Select Image', width=25, command=select_image)
btn_select_img.grid(column=0, row=0, padx=5, pady=5)

root.mainloop()