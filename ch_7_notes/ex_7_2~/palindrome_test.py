import unittest
from palindrome import isPalindrome

class UnitTests(unittest.TestCase):
    def test_true(self):
        self.assertEqual(isPalindrome('noon'), True)
    
    def test_false(self):
        self.assertEqual(isPalindrome('cat'), False)