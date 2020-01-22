import unittest
from arrays import Array

class UnitTests(unittest.TestCase):
    def test_eq_test1(self):
        a = Array(10)
        b = Array(10)
        self.assertEqual(a, b)

    def test_eq_test2(self):
        a = Array(10)
        b = Array(5)
        self.assertEqual(a, b)

    def test_eq_test3(self):
        a = Array(10)
        b = []
        self.assertNotEqual(a, b)

    def test_eq_test4(self):
        a = Array(10)
        b = Array(10)
        b.insert(15, 15)
        self.assertNotEqual(a, b)