from math import pi, pow

"""
This program creates the blueprint for building circle objects.
It is equipped with methods to set the center of the circle, to set the radius of the circle, to set the diameter of the
circle, to estimate the area of the circle, estimate the circumference of the circle, and to describe the circle.
"""


# function to estimate the area of a circle
def area(*, radius, diameter):
    if radius is not None:
        return pi * pow(radius, 2)
    else:
        return (pi / 4) * pow(diameter, 2)


# function to estimate the circumference of the circle
def circumference(*, radius, diameter):
    if radius is not None:
        return 2 * pi * radius
    else:
        return pi * diameter


class Circle:

    # The init function for crating instances of the circle class
    def __init__(self, center_x, center_y, radius=None, diameter=None):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.diameter = diameter

    # function to set radius of the circle
    def set_radius(self, radius):
        self.radius = radius

    # function to  set the diameter of the circle
    def set_diameter(self, diameter):
        self.diameter = diameter

    # function to estimate the area of a circle
    def area(self):
        return area(radius=self.radius, diameter=self.diameter)

    # function to estimate the circumference of a circle
    def circumference(self):
        return circumference(radius=self.radius, diameter=self.diameter)

    # function to give a description of the class
    def __str__(self):
        if self.radius is not None:
            print("This is a circle with radius", str(self.radius) + " units", "and area ",
                  f"{area(radius=self.radius, diameter=None):.2f} square units", "and circumference",
                  f"{circumference(radius=self.radius, diameter=None):.2f} units")
        else:
            print("This is a circle with diameter", str(self.diameter) + " units ", "and area ",
                  f"{area(radius=None, diameter=self.diameter):.2f} square units", "and circumference",
                  f"{circumference(radius=None, diameter=self.diameter):.2f} units")




