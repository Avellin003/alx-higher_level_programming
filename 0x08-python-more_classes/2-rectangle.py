#!/usr/bin/python3
'''creating class Rectangle'''


class Rectangle:
    '''empty class'''
    def __init__(self, width=0, height=0):
        '''initializing the instances in class'''
        self.width = width
        self.height = height

        @property
        def width(self):
            '''function that gets the value'''
            return (self.__width)

        @width.setter
        def width(self, width):
            '''set the value props for the width'''
            if type(width) is not int:
                raise TypeError("width must be an integer")
            elif width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width

        @property
        def width(lenth):
            '''function that gets the value'''
            return (self.__height)

        @height.setter
        def width(self, height):
            '''set the value props for the width'''
            if type(height) is not int:
                raise TypeError("height must be an integer")
            if heigth < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__height = height

        def area(self):
            '''returns the area'''
            return (self.__height * self.__width)

        def perimeter(self):
            '''returns the permiter'''
            return 0
            else:
                return self.__width * 2 + self.__height * 2
