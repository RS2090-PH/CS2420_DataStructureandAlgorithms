import unittest
from node import Node
from testnode import length

class UnitTests(unittest.TestCase):
    def test_length_test(self):
        head = None
        self.assertEqual(length(head), 0)

    def test_length_test2(self):
        head = None
        for count in range(1, 10):
            head = Node(count, head)
        self.assertEqual(length(head), 9)

    def test_length_test3(self):
        head = None
        for count in range(20, 23):
            head = Node(count, head)
        self.assertEqual(length(head), 3)