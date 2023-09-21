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
