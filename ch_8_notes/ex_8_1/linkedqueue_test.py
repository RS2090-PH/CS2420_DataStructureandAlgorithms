import unittest
from linkedqueue import LinkedQueue

q = LinkedQueue()
for i in range(7):
        q.add(i + 1)

class UnitTests(unittest.TestCase):
    def test_unit_test(self):
        self.assertEqual(len(q), 7)
        q.clear()
        self.assertEqual(len(q), 0)