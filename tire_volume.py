"""
Many companies wish to understand the needs
and wants of their customers more deeply so
the company can create products that fill those
needs and wants. One way to understand customers
more deeply is to record the values entered by customers
while they are using a program and then to analyze those values.
One common way to record values is for a program to store them in a file.
"""

# Import the Math funtions and datetime from library
import math
from datetime import datetime

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

# Get day from the Computer system
today = datetime.now()


# Open a text file named volumes.txt in append mode
with open('volumes.txt', 'at') as volumes_file:

    # Print on file
    print(f'Current date: {today:%d-%m-%Y}', file=volumes_file)
    print(f'Width of tire: {width:.0f}', file=volumes_file)
    print(f'Aspect ratio of the tire: {ratio:.0f}', file=volumes_file)
    print(f'Diameter of the wheel: {diameter:.0f}', file=volumes_file)
    print(f'Volume of the tire: {tire_volume}', file=volumes_file)

    # Print blank space for future append.
    print('', file=volumes_file)