#!/usr/bin/python3

"""class Myint"""


class MyInt(int):
    """class that inherits from int"""

    def __eq__(self, new):
        """inverts != to =="""
        return(int(self) != new)

    def __ne__(self, new):
        """reinverts"""
        return (int(self) == new)
