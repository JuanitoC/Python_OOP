from multipledispatch import dispatch

"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


def add(a: int, b: int = 14):
    """Return the sum of a and b."""
    return print(a + b)


def add(a: str, b: str = "nabo"):
    """Concat the sum of a and b."""
    return print(a + b)


add(7,7)
