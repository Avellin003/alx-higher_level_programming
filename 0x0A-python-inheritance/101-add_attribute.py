#!/usr/bin/python3
"""adds attributes to objects"""


def add_attribute(ob, at, val):
    """adds new attributes to an object"""
    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, at, val)
