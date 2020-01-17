import unittest
from ex_3_9 import insertionSort
from ex_3_9 import quicksort
from ex_3_9 import quicksortHelper
from ex_3_9 import partition
from ex_3_9 import swap

class UnitTests(unittest.TestCase):
    def test_unit_test(self):
        lyst = [6, 4, 8, 2]
        insertionSort(lyst, 0, 3)
        result = [2, 4, 6, 8]
        self.assertEqual(lyst, result)