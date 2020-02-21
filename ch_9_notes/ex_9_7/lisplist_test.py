import unittest
from lisplist import buildRange, insert

class UnitTests(unittest.TestCase):
  def test(self):
    lyst = buildRange(1, 9)
    lyst = insert(5, 99, lyst)
    expected = "(1 2 3 4 5 99 6 7 8 9)"
    print("Expected: ", expected)
    print("Actual:   ", lyst)
    self.assertEqual(str(lyst), str(expected))