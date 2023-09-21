"""
Many companies wish to understand the needs
and wants of their customers more deeply so
the company can create products that fill those
needs and wants. One way to understand customers
more deeply is to record the values entered by customers
while they are using a program and then to analyze those values.
One common way to record values is for a program to store them in a file.
"""

# Import the Math funtions
import math

# Print a brief description of the program to the user
print('This program is build to computes')
print('and ouputs the Tires Volume')
print()

# Get values of the tire from the user
width = float(input('Enter the width of the tire in mm (ex 205): '))
ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))



# Compute the Tire Volume using formula
tire_volume = (math.pi * (width**2) * ratio * (width * ratio + 2540 * diameter)) / 10000000000
tire_volume = round(tire_volume, 2)

# Print the result from the calculation.
print()
print(f'The approximate volume is {tire_volume} liters')
