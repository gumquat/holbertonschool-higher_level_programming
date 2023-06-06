#!/usr/bin/python3
""" Base Test Cases"""
import unittest
from models.base import Base
from unittest.mock import patch
from io import StringIO

class TestBase(unittest.TestCase):
    """TEST: BASE CLASS TESTS"""
    def test_Auto_ID(self):
            """TEST: IDs are auto-assigned and different"""
            b1 = Base()
            b2 = Base()
            b3 = Base(11)
            self.assertIsNotNone(b1.id)
            self.assertIsNotNone(b2.id)
            self.assertNotEqual(b1.id, b2.id)
            self.assertEqual(b1.id, 1)
            self.assertEqual(b2.id, 2)
            self.assertEqual(b3.id, 11)
    def Auto_ID_Incrementing(self):
            """TEST: IDs are incrementing upon new instance creation"""
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
    def ID_Type(self):
        """TEST: IDs asigned are ints"""
        base = Base(11)
        self.assertIsInstance(base.id, int)
    def to_json_empty(self):
        """TEST: is json empty upon init"""
        with self.assertRaises(TypeError):
            b = Base()
            json_dictionary = Base.to_json_string()

"""NEEDS this to be run"""
if __name__ == '__main__':
    unittest.main()
