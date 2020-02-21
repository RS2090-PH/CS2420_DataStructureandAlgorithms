import unittest
from lisplist import cons, removeAll, equals, THE_EMPTY_LIST

class UnitTests(unittest.TestCase):
  def removeall1_test(self):
    L1 = cons(2, cons(1, cons(2, cons(3, THE_EMPTY_LIST))))
    L2 = removeAll(2, L1)
    expected = cons(1, cons(3, THE_EMPTY_LIST))

    # FEEDBACK
    print("Starting list: ", L1)
    print("Expect (1 3): ", L2)    

    self.assertTrue(equals(L2, expected))

  def removeall2_test(self):
    L1 = cons(2, cons(1, cons(2, cons(3, THE_EMPTY_LIST))))
    L2 = removeAll(3, L1)
    expected = cons(2, cons(1, cons(2, THE_EMPTY_LIST)))

    # FEEDBACK
    print("Starting list: ", L1)
    print("Expect (2 1 2): ", L2)

    self.assertTrue(equals(L2, expected))