# This program help employees knowing the number of boxes they 
# need to pack items into boxes for shippping

# Import math module
import math

# Ask employees for information about number of items to be packed
items = int(input('Enter the number of items: '))

# Ask employees for information about how many items can be packed into each box
item_per_box = int(input('Enter the number of items per box: '))

# Compute number of boxes needed
boxes = math.ceil(items / item_per_box)

# Print a brief exxplanation for the employees
print()
print(f'For {items} items, packing {item_per_box} items in each box, you will need {boxes} boxes.')