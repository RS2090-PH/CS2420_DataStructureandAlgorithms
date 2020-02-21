import unittest
from lisplist import buildRange, equals, rest

class UnitTests(unittest.TestCase):
  def equals1_test(self):
    L1 = buildRange(1, 5)
    L2 = buildRange(1, 5)

    # FEEDBACK
    print("Value of L1: ", L1)
    print("Value of L2: ", L2)
    print("Expect True: ", equals(L1, L2))

    self.assertTrue(equals(L1, L2))

  def equals2_test(self):
    L = buildRange(1, 2)
    L1 = rest(rest(L))
    L2 = rest(rest(L))

    # FEEDBACK
    print("Value of L1: ", L1)
    print("Value of L2: ", L2)
    print("Expect True: ", equals(L1, L2))

    self.assertTrue(equals(L1, L2))

  def equals3_test(self):
    L1 = buildRange(1, 5)
    L2 = buildRange(5, 9)

    # FEEDBACK 
    print("Value of L1: ", L1)
    print("Value of L2: ", L2)
    print("Expect False: ", equals(L1, L2))

    self.assertFalse(equals(L1, L2))
