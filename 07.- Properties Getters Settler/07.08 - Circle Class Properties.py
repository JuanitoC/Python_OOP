"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    VALID_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Please enter a valid radius.")

    radius = property(get_radius, set_radius)


my_circle = Circle(69, 'Blue')

# Radius
print("radius con property inicial: "+str(my_circle.radius))
print("_radius  inicial: "+str(my_circle._radius))

my_circle.radius = 1

print("radius con property: "+str(my_circle.radius))
print("_radius : "+str(my_circle._radius))

