import unittest
import io
from contextlib import redirect_stdout
from node import Node
from testnode import insert, printStructure

class UnitTests(unittest.TestCase):
    def test_insert_test(self):
        head = None
        head = insert(0, "0", head)
        head = insert(1, "1", head)
        head = insert(2, "2", head)
        output = io.StringIO()
        with redirect_stdout(output):
            printStructure(head)
        outVal = output.getvalue()
        print(outVal)
        self.assertTrue(re.match("0\s1\s2\s", outVal), msg="expected {} to match : `0 1 2 `".format(outVal))

    def test_insert_indexmovetest(self):
        head = None
        head = insert(0, "0", head)
        head = insert(0, "1", head)
        head = insert(0, "2", head)
        output = io.StringIO()
        with redirect_stdout(output):
            printStructure(head)
        outVal = output.getvalue()
        print(outVal)
        self.assertTrue(re.match("2\s1\s0\s", outVal))