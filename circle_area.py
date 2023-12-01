import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry, FloatEntry
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window.
    frm_main = Frame(root)
    frm_main.master.title("Area of a Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, to add
    # labels, text entry boxes, and buttons.
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
    # Create label for the number entry and the result.
    lbl_radius = Label(frm_main, text="Radius of the Circle:")
    lbl_area = Label(frm_main, text="Area of the Circle:")

    # Create the number entry.
    ent_radius = FloatEntry(frm_main, width=5)

    # Create a label to display the result.
    txt_area = Label(frm_main, width=5, anchor="e")

    # # Create labels to display the units.
    lbl_area_units = Label(frm_main, text="cm2")
    lbl_radius_units = Label(frm_main, text="Centimeters")
    # # Ratios don't have units
    # lbl_diam_units = Label(frm_main, text="inches")
    # lbl_vol_units = Label(frm_main, text="liters")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, number entries, and buttons in a grid.
    lbl_radius.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
    ent_radius.grid(      row=0, column=1, padx=3, pady=2, sticky="w")
    lbl_area_units.grid(row=1, column=2, padx=0, pady=2, sticky="w")
    lbl_radius_units.grid(row=0, column=2, padx=0, pady=2, sticky="w")

    # lbl_ratio.grid(     row=1, column=0, padx=3, pady=2, sticky="e")
    # ent_ratio.grid(     row=1, column=1, padx=3, pady=2, sticky="w")
    # Ratios don't have units.

    # lbl_diam.grid(      row=2, column=0, padx=3, pady=2, sticky="e")
    # ent_diam.grid(      row=2, column=1, padx=3, pady=2, sticky="w")
    # lbl_diam_units.grid(row=2, column=2, padx=0, pady=2, sticky="w")

    lbl_area.grid(   row=1, column=0, padx=3, pady=2, sticky="e")
    txt_area.grid(   row=1, column=1, padx=3, pady=2, sticky="w")
    # lbl_vol_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
    btn_clear.grid(    row=4, column=2, padx=3, pady=2, sticky="n")


    # This function is called each time the user releases a key.
    def calculate(event):
        """Compute the approximate volume of a tire in liters."""
        try:
            # Get the user input.
            r = ent_radius.get()
            # a = ent_ratio.get()
            # d = ent_diam.get()

            # Compute the tire volume in liters.
            a = (math.pi * r ** 2)

            # Display the volume rounded to one digit
            # after the decimal for the user to see.
            txt_area.config(text=f"{a:.2f}")

        except ValueError:
            # When the user deletes all the digits in one
            # of the number entries, clear the result.
            txt_area.config(text="")


    # This function is called each time
    # the user clicks the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        # ent_ratio.clear()
        # ent_diam.clear()
        txt_area.config(text="")
        ent_radius.focus()


    # Bind the calculate function to the three number
    # entries so that the calculate function will be called
    # when the user changes the text in the number entries.
    ent_radius.bind("<KeyRelease>", calculate)
    # ent_ratio.bind("<KeyRelease>", calculate)
    # ent_diam.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the width text field.
    ent_radius.focus()


# If this file is executed like this:
# > python teach_solution.py
if __name__ == "__main__":
    main()