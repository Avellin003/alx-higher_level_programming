#!/usr/bin/python3

"""creation of class with inheritance"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class"""
    def __init__(self, width, height):
        """init rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """string represantaion"""
        ans = f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
        return me
 
    def area(self):
        """area method"""
        return self.__width * self.__height

    def __str__(self):
        """string method"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__heigh))

    class Square(Rectangle):
        """class squre"""
        def __init__(self, size):
            """init"""
            self.integer_validator("size", size)
            self.__size = size
            super().__init__(size, size)

        def area(self):
            """area"""
            return self.__size ** 2

        def __str__(self):
            """stringer"""
            return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
