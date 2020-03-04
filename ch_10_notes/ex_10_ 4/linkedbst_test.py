import unittest
import io
from contextlib import redirect_stdout
from linkedbst import LinkedBST

class UnitTests(unittest.TestCase):
    def test_successor_test1(self):
        t1 = LinkedBST()
        t1.add("G")
        t1.add("C")
        t1.add("A")
        t1.add("B")
        t1.add("E")
        t1.add("D")
        t1.add("F")
        t1.add("K")
        t1.add("I")
        t1.add("H")
        t1.add("J")
        t1.add("M")
        t1.add("L")
        t1.add("N")
        output = io.StringIO()
        with redirect_stdout(output):
            for node in t1:
                 print(t1.successor(node), end = " ")
        t1out = output.getvalue()
        s1 = "H D B C F E G L J I K N M None "
        self.assertEqual(t1out, s1)

    def test_successor_test2(self):
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
        output = io.StringIO()
        with redirect_stdout(output):
            for node in t1:
                 print(t1.successor(node), end = " ")
        t1out = output.getvalue()
        s1 = "B C D E F G H I J K L M N None "
        self.assertEqual(t1out, s1)

    def test_successor_test3(self):
        t1 = LinkedBST()
        t1.add("G")
        t1.add("C")
        t1.add("A")
        t1.add("B")
        t1.add("E")
        t1.add("D")
        t1.add("F")
        t1.add("K")
        t1.add("I")
        t1.add("H")
        t1.add("J")
        t1.add("M")
        t1.add("L")
        t1.add("N")
        output = io.StringIO()
        with redirect_stdout(output):
            for node in t1:
                 print(t1.predecessor(node), end = " ")
        t1out = output.getvalue()
        s1 = "F B None A D C E J H G I L K M "
        self.assertEqual(t1out, s1)

    def test_successor_test4(self):
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
        output = io.StringIO()
        with redirect_stdout(output):
            for node in t1:
                 print(t1.predecessor(node), end = " ")
        t1out = output.getvalue()
        print(t1out)
        s1 = "None A B C D E F G H I J K L M "
        self.assertEqual(t1out, s1)
