import unittest
from linkedstack import LinkedStack
from arraystack import ArrayStack

class UnitTests(unittest.TestCase):
        def arpeek_unit_test(self):
        temp = ArrayStack()
        for count in range(5):
              temp.push(count+1)
        self.assertEqual(temp.peek(), 5)

    def arpush_unit_test(self):
        temp = ArrayStack()
        for count in range(20):
              temp.push(count+1)
        self.assertEqual(len(temp),20)
    
    def arclear_unit_test(self):
        temp = ArrayStack()
        for count in range(4):
              temp.push(count+1)
        temp.clear()
        self.assertEqual(temp.isEmpty(), True)
    
    def arpop_unit_test(self):
        temp = ArrayStack()
        for count in range(4):
              temp.push(count+1)
        temp.pop()
        self.assertEqual(temp.peek(), 3)
        temp.pop()
        self.assertEqual(len(temp),2)

    def lipeek_unit_test(self):
        temp = LinkedStack()
        for count in range(5):
              temp.push(count+1)
        self.assertEqual(temp.peek(), 5)

    def lipush_unit_test(self):
        temp = LinkedStack()
        for count in range(20):
              temp.push(count+1)
        self.assertEqual(len(temp),20)

    def liclear_unit_test(self):
        temp = LinkedStack()
        for count in range(4):
              temp.push(count+1)
        temp.clear()
        self.assertEqual(temp.isEmpty(), True)

    def lipop_unit_test(self):
        temp = ArrayStack()
        for count in range(4):
              temp.push(count+1)
        temp.pop()
        self.assertEqual(temp.peek(), 3)
        temp.pop()
        self.assertEqual(len(temp),2)

    def araddstor_unit_test(self):
        temp = ArrayStack()
        for count in range(20):
              temp.push(count+1)
        self.assertEqual(len(temp.items), 20)

    def arremstor_unit_test(self):
        temp = ArrayStack()
        for count in range(20):
              temp.push(count+1)
        for count in range(15):
              temp.pop()
        self.assertEqual(len(temp.items), 10)

    def arexcep_unit_test(self):
        temp = ArrayStack()
        with self.assertRaises(KeyError):
            temp.pop()

    def liexcep_unit_test(self):
        temp = LinkedStack()
        with self.assertRaises(KeyError):
            temp.pop()
        