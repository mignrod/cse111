# This program computes and prints the storage efficiency
# for each of the following 12 steel can sizes.

# Import math modules for this program
# So math.pi function could be used
import math

# Defining the Main function
def main():
    can_names = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z Short', '#10', '#211', '#300', '#303']
    can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    can_cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

    best_storage_efficiency = None
    best_cost_efficiency = None
    best_storage_number = -1
    best_cost_number = -1

    # For each can in the list extract value and
    # assign into the variables
    for i in range(len(can_names)):
        name = can_names[i]
        radius = can_radius[i]
        height = can_height[i]
        cost = can_cost[i]
    
        # Call cost and storage efficiency functions
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)

        # Print can sizes and values
        print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.0f}')

        # If the storage efficiency of the current can size is
        # greater than the maximum storage efficiency, save then
        # the current can size name and its storage efficiency.
        if storage_efficiency > best_storage_number:
            best_storage_number = storage_efficiency
            best_storage_can = name

        # If the cost efficiency of the current can size is
        # greater than the maximum cost efficiency, then save
        # the current can size name and its cost efficiency.
        if cost_efficiency > best_cost_number:
            best_cost_number = cost_efficiency
            best_cost_can = name

    # Print best storage and cost efficiencies
    print()
    print('Best can size in storage efficiency:', best_storage_can)
    print('Best can size in cost efficiency:', best_cost_can)

# Defining compute volume function
# In this function we could compute the volume for cylinder forms
def compute_volume(radius, height):
    volume = (math.pi * radius**2) * height
    return volume

# Defining compute surface area function
# In this function we could compute surface area for cylinder forms
def compute_surface_area (radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


# Defining compute storage efficiency function
def compute_storage_efficiency(radius, height):
    storage_efficiency = compute_volume(radius, height) / compute_surface_area(radius, height)
    return storage_efficiency

# Defining compute cost efficiency fnction
# Compuute and return cost efficiency
def compute_cost_efficiency(radius, height, cost):
    cost_efficiency = compute_volume(radius, height) / cost
    return cost_efficiency

# Calling main function and
# Start this program
main()