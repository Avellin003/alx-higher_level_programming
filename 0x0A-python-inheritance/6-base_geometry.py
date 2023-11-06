#!/usr/bin/python3
"""
write class BaseGeometry with method area
that raises an exception
"""

class BaseGeometry:
    """a class with a public instance area"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
