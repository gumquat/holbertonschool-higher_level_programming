#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from models.base import Base
# from models.rectangle import Rectangle as Rectangle
# from models.square import Square as Square


class TestBase(unittest.TestCase):
    """makes some bass class ez ref for testing"""
    b = Base()
    r = # Rectangle()
    s = # Square()

    """BASE CLASS TESTING"""
    def test_Auto_ID(self):
        """TEST: IDs are auto-assigned and different"""
        b1 = Base()
        b2 = Base()
        self.assertIsNotNone(b1.id)
        self.assertIsNotNone(b2.id)
        self.assertNotEqual(b1.id, b2.id)
    def Auto_ID_Incrementing(self):
        """TEST: IDs are incrementing upon new base creation"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
    def Base_89(self):
        """TEST: saving the ID passed exists"""
        b1 = Base(89)
        self.assertEqual(b1.id, 89)
