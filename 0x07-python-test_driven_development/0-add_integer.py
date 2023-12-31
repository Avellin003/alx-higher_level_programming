#!/usr/bin/python3
"""add_integer function that adds up two integers"""


def add_integer(a, b=98):
    '''returns sum of two numbers'''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return (a + b)
