#!/usr/bin/python3

"""
creator of module square
"""


class Square:

    """
    object __init__ raises Errors
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            """
            object area returns the exponential of 2
            of the value given size
            """

            return self.__size ** 2
