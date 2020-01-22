import unittest
from ex_4_3 import Array

class UnitTests(unittest.TestCase):
    def test_grow_test1(self):
        a = Array(5)
        a.grow()
        a.grow()
        self.assertEqual(len(a), 20)

    def test_shrink_test1(self):
        a = Array(10)
        a.grow()
        a.grow()
        a.grow()
        a.shrink()
        a.shrink()
        self.assertEqual(len(a), 20)

    def test_shrink_test2(self):
        a = Array(10)
        a.grow()
        a.grow()
        a.shrink()
        a.shrink()
        a.shrink()
        a.shrink()
        self.assertEqual(len(a), 10)