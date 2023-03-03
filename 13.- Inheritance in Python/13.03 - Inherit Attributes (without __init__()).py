"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Polygon:

    CONSTANT_VALUE = ['CONSTANT']
    def __init__(self, num_sides, color):
        self._num_sides = num_sides
        self._color = color

    def get_color(self):
        return self._color

    def get_num_sides(self):
        return self._num_sides


class Triangle(Polygon):
    pass


my_triangle = Triangle(3, "Blue")

print(my_triangle.get_color())
print(my_triangle.get_num_sides())
print(my_triangle.CONSTANT_VALUE)
