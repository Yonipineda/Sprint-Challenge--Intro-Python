# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class



# assignment down below 

class Vehicle:
    '''Base class, or Parent class.'''
    pass 

class GroundVehicle(Vehicle): # inherit from vehicle 
    pass 

class Car(GroundVehicle):  # car inherits from ground vehicle 
    pass

class Motorcycle(GroundVehicle):  # motorcycle inherits from groundvehicle 
    pass 

class FlightVehicle(Vehicle):  # flightvehicles inherit from vehicle 
    pass 

class Airplane(FlightVehicle): # airplane from flight vehicle 
    pass 

class Starship(FlightVehicle):   # GO SPACEX!!
    pass