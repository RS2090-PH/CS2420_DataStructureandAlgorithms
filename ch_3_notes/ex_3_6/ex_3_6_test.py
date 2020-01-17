from ex_3_6 import fib
import unittest

class UnitTests(unittest.TestCase):
    def test_unit_test(self):
        temp = [0,0,0,0,0]
        problemSize = 3
        for count in range(5):
              temp[count] = fib(problemSize, {})
              problemSize*=2
        result = [2,8,144,46368,4807526976]
        self.assertEqual(temp, result)