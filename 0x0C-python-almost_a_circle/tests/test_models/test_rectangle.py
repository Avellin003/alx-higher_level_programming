#!/usr/bin/python3
"""the tester for the rectangle.py"""



import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """unittest testing starts"""
    def test_rectangle_inherits_base(self):
        self.assertIsInstance(Rectangle(4, 2), Base)

    def test_without_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_with_one_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_with_two_arguments(self):
        value1 = Rectangle(1, 2)
        value2 = Rectangle(2, 1)
        self.assertEqual(value1.id, value2.id - 1)

    def test_with_three_argumets(self):
        value1 = Rectangle(1, 2, 3)
        value2 = Rectangle(3, 2 ,1)
        self.assertEqual(value1.id, value2.id -1)

    def test_with_four_arguments(self):
        value1 = Rectangle(1, 2, 3, 4)
        value2 = Rectangle(4, 3, 2 ,1)
        self.assertEqual(value1.id, value2.id -1)

    def test_five_arguments(self):
        self.assertEqual(ZZ)
if __name__ == "__main__":
    unittest.main()
