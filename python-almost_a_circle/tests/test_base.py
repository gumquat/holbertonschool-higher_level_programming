#!/usr/bin/python3
""" Base Class Test Cases"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests base class"""
    def test_max_int(self):
        """Auto Assigned ID test - exists y/n"""
        b = Base()
        self.assertEqual(b.id, 1)