#!/usr/bin/python3
"""testing"""


import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """testing of the class"""
    def setting(self):
        """checks if the b1 is successfully set Base() at base.py"""
        self.b1 = base.Base()
        self.b2 = base.Base()
        self.b3 = base.Base()
        self.b4 = base.Base()
        self.b5 = base.Base()
if __name__ == "__main__":
    unittest.main()
