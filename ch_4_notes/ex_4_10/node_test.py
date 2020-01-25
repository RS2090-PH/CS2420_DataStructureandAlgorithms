import unittest
import io
import re
from node import Node
from nodetest import printStructure, insert, pop
from contextlib import redirect_stdout

class UnitTests(unittest.TestCase):
    def test_pop_test1(self):
        head = None
        head = insert(0, "0", head)
        head = insert(1, "1", head)
        head = insert(2, "2", head)
        (head, item) = pop(1, head)
        output = io.StringIO()
        with redirect_stdout(output):
            printStructure(head)
        outVal = output.getvalue()
        self.assertTrue(re.match("0\s2\s", outVal))

    def test_pop_test2(self):
        head = None
        head = insert(0, "0", head)
        head = insert(1, "1", head)
        head = insert(2, "2", head)
        (head, item) = pop(2, head)
        output = io.StringIO()
        with redirect_stdout(output):
            printStructure(head)
        outVal = output.getvalue()
        print(outVal)
        self.assertTrue(re.match("0\s1\s", outVal))