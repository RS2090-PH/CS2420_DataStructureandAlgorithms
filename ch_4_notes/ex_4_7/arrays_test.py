import unittest
import io
import re
from contextlib import redirect_stdout
from arrays import Array
from grid import Grid
from matrix import Matrix

class UnitTests(unittest.TestCase):
    def test_add_test1(self):
        a = Matrix(3, 3, 3)
        b = Matrix(3, 3, 6)
        print(b)
        c = a + a
        output = io.StringIO()    
        with redirect_stdout(output):
            print(a+a)
        m1 = output.getvalue()
        self.assertTrue(re.match("^(6\s6\s6(\s)*\n)+$", m1))

    def test_mul_test1(self):
        a = Matrix(3, 3, 3)
        b = Matrix(3, 3, 6)
        output = io.StringIO()   
        with redirect_stdout(output):
            print(a * b)
        m1 = output.getvalue()
        self.assertTrue(re.match("^((54\s){3}\n){3}$", m1))

    def test_mul_test2(self):
        a = Matrix(2, 2, 3)
        b = Matrix(2, 3, 6)
        c = a * b
        flag = True
        for i in range(c.getHeight()):
            for j in range(c.getWidth()):
                if c[i][j] != 36:
                    flag = False
        self.assertTrue(flag)

    def test_sub_test1(self):
        a = Matrix(4, 4, 4)
        b = Matrix(4, 4, 2)
        output = io.StringIO()    
        with redirect_stdout(output):
            print(a - b)
        m1 = output.getvalue()
        self.assertTrue(re.match("^(2\s2\s2\s2(\s)*\n)+$", m1))

    def test_sub_test2(self):
        a = Matrix(4, 4, 4)
        b = Matrix(4, 4, 2)
        c = a - b
        flag = True
        print(c)
        for i in range(c.getHeight()):
            for j in range(c.getWidth()):
                if c[i][j] != 2:
                    flag = False
        self.assertTrue(flag)

    def test_mul_exceptiontest1(self):
        a = Matrix(3, 3, 3)
        b = Matrix(2, 2, 6)
        with self.assertRaises(Exception):
            c = a * b
        