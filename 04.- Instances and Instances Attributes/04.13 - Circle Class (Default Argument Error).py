"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    def __init__(self, color, radius=5): # This throws an error
        self.radius = radius
        self.color = color


my_circle = Circle('Green')
print(my_circle.radius)
print(my_circle.color)
