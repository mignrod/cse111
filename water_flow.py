# This program compute many aspect of water flow, to implement a elevated water tank
# distribution system, to ensure water flow for all city.  

def water_column_height(tower_height, tank_height):
    """
    This function calculates and returns the height of a column of water from a tower height and a tank wall height.
    Parameter: tower_height and tank_height.
    returns: float number with the water column height value.
    """
    water_column_height = tower_height + (3 * tank_height) / 4
    return water_column_height

def pressure_gain_from_water_height(height):
    """
    This function calculates and returns the pressure caused by Earths gravity pulling on the water stored in an elevated tank.
    Parameter: The elevation height of the tank.
    returns: float number with the pressure gained value.
    """
    pressure = (998.2 * 9.80665 * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    This function calculates and returns the water pressure lost because of the friction between
    the water and the walls of a pipe that it flows through. 
    Parameter: pipe_diameter, pipe_length, friction_factor, fluid_velocity.
    returns: float number with the pressure lost value.
    """
    pressure_loss_from_pipe = (-friction_factor * pipe_length * 998.2 * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss_from_pipe