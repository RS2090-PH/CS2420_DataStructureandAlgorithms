import unittest
from linkedbst import LinkedBST

class UnitTests(unittest.TestCase):
    def test_9NodeTree_test(self):
        t1 = LinkedBST()
        t1.add("F")
        t1.add("B")
        t1.add("A")
        t1.add("D")
        t1.add("C")
        t1.add("E")
        t1.add("G")
        t1.add("I")
        t1.add("H")
        expectedHeight = 3
        self.assertEqual(t1.height(), expectedHeight)

    def test_14NodeTree_test(self):
        t1 = LinkedBST()
        t1.add("F")
        t1.add("B")
        t1.add("A")
        t1.add("D")
        t1.add("C")
        t1.add("E")
        t1.add("G")
        t1.add("I")
        t1.add("H")
        t1.add("K")
        t1.add("J")
        t1.add("M")
        t1.add("L")
        t1.add("N")
        expectedHeight = 5
        self.assertEqual(t1.height(), expectedHeight)

    def test_isBalanced_false(self):
        t1 = LinkedBST()
        t1.add("A")
        t1.add("B")
        t1.add("C")
        t1.add("D")
        t1.add("E")
        t1.add("F")
        t1.add("G")
        t1.add("H")
        t1.add("I")
        t1.add("J")
        t1.add("K")
        t1.add("L")
        t1.add("M")
        t1.add("N")
        t1.add("O")
        t1.add("P")
        t1.add("Q")
        t1.add("R")
        t1.add("S")
        self.assertFalse(t1.isBalanced(), msg="isBalanced() returned `True` for an  unbalanced LinkedBST object")

    def test_isBalanced_true(self):
        t1 = LinkedBST()
        t1.add("F")
        t1.add("B")
        t1.add("A")
        t1.add("D")
        t1.add("C")
        t1.add("E")
        t1.add("G")
        t1.add("I")
        t1.add("H")
        t1.add("K")
        t1.add("J")
        t1.add("M")
        t1.add("L")
        t1.add("N")
        self.assertTrue(t1.isBalanced(), msg="isBalanced() returned `False` for a balanced LinkedBST object")