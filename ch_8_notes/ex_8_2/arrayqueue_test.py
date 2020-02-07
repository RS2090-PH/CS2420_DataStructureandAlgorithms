import unittest
from arrayqueue import ArrayQueue

p = ArrayQueue()
for i in range(7):
    p.add(i + 1)

q = ArrayQueue()
for i in range(12):
    q.add(i + 1)

r = ArrayQueue()
for i in range(7):
        r.add(i + 1)

s = ArrayQueue()
for i in range(3):
    s.add(i + 1)

t = ArrayQueue()
for i in range(1):
    t.add(i + 1)

class UnitTests(unittest.TestCase):
    def add1_unit_test(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(str(expected), str(p))
        
    def add2_unit_test(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12]
        self.assertEqual(str(expected), str(q))

    def clear_unit_test(self):
        rLength = len(r)
        self.assertEqual(rLength, 7)
        r.clear()
        rLength = len(r)
        self.assertEqual(rLength, 0)

    def pop2_unit_test(self):
        s.pop()
        expected = [2, 3]
        self.assertEqual(str(expected), str(s))

    def pop1_unit_test(self):
        t.pop()
        with self.assertRaises(KeyError):
              t.pop()