#!/usr/bin/python3
"""class Myint"""


class MyInt(int):
    """class that inherits from int"""
    def __creator__(ls, *argumets, **kwarguments):
        """new instance of class"""
        return(super(Myint, ls).__new__(ls, *arguments, **kwarguments))
    def __inverter__(self, new):
        """inverts != to =="""
        return(int(self) != new)
    def __reinverter__(self, new):
        """reinverts"""
        return (int(self) == new)
