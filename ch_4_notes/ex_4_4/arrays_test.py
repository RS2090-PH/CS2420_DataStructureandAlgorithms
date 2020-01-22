import unittest
from arrays import Array

class UnitTests(unittest.TestCase):
    def test_insert_test1(self):
        a = Array(5)
        for item in range(4):
          a.insert(0, item)
        a.insert(1, 10)
        self.assertEqual(a[1], 10)

    def test_insert_test2(self):
        a = Array(5)
        for item in range(2):
          a.insert(0, item)
        a.insert(4, 5)
        self.assertEqual(a[2], 5)

    def test_pop_test1(self):
        a = Array(5)
        for item in range(4):
          a.insert(0, item)
        self.assertEqual(a.pop(2), 1)
        self.assertEqual(a[2], 0)