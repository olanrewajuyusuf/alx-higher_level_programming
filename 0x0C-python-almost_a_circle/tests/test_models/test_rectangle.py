"""Unittest for Rectangle model"""
from models.rectangle import Rectangle

import unittest

class TestBase(unittest.TestCase):

    """Testing rectangle id"""
    def test_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    """Testing rectangle width and height"""
    def test_width_height(self):
        r4 = Rectangle(9, 3, 5, 5, 12)

        self.assertEqual(r4.width, 9)
        self.assertEqual(r4.height, 3)

        r4.width = 5
        r4.height = 9

        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 9)

    """Testing rectangle x and y"""
    def test_x_y(self):
        r5 = Rectangle(9, 3, 2, 3, 12)

        self.assertEqual(r5.x, 2)
        self.assertEqual(r5.y, 3)

        r5.x = 3
        r5.y = 8

        self.assertEqual(r5.x, 3)
        self.assertEqual(r5.y, 8)


if __name__ == "__main__":
    unittest.main()
