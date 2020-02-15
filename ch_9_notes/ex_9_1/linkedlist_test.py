import unittest
from arraylistiterator import ArrayListIterator
from linkedlist import LinkedList

class UnitTests(unittest.TestCase):
    def hasnext1_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        output = listIterator.hasNext()
        self.assertEqual(output, True)

    def hasnext2_test(self):
        lyst = LinkedList(range(0))
        listIterator = lyst.listIterator()
        listIterator.first()
        output = listIterator.hasNext()
        self.assertEqual(output, False)

    def next1_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        listIterator.next()
        output = listIterator.next()
        self.assertEqual(output, 2)

    def next2_test(self):
        lyst = LinkedList(range(1, 3))
        listIterator = lyst.listIterator()
        listIterator.first()
        listIterator.next()
        listIterator.next()
        self.assertRaises(ValueError, listIterator.next)

    def hasprevious1_test_hasNext(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        listIterator.next()
        output = listIterator.hasPrevious()
        self.assertEqual(output, True)

    def hasprevious2_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        output = listIterator.hasPrevious()
        self.assertEqual(output, False)

    def previous1_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        listIterator.next()
        listIterator.next()
        listIterator.previous()
        output = listIterator.previous()
        print (output)
        self.assertEqual(output, 1)

    def previous2_test(self):
        lyst = LinkedList(range(1, 3))
        listIterator = lyst.listIterator()
        listIterator.first()
        self.assertRaises(ValueError, listIterator.previous)

    def replace1_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        for count in range(6):
            listIterator.next()
        listIterator.replace(0)
        self.assertEqual(lyst, LinkedList([1, 2, 3, 4, 5, 0, 7, 8, 9]))

    def replace2_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        with self.assertRaises(AttributeError):
            listIterator.replace(5)

    def insert1_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        for count in range(4):
            listIterator.next()
        listIterator.insert(0)
        self.assertEqual(lyst, LinkedList([1, 2, 3, 0, 4, 5, 6, 7, 8, 9]))

    def insert2_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        listIterator.insert(0)
        self.assertEqual(lyst,  LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def remove1_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        for count in range(8):
            listIterator.next()
        listIterator.remove()
        self.assertEqual(lyst,  LinkedList([1, 2, 3, 4, 5, 6, 7, 9]))

    def remove2_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        listIterator.first()
        for count in range(7):
            listIterator.next()
        listIterator.previous()
        listIterator.remove()
        self.assertEqual(lyst, LinkedList([1, 2, 3, 4, 5, 6, 8, 9]))

    def remove3_test(self):
        lyst = LinkedList(range(1, 10))
        listIterator = lyst.listIterator()
        self.assertRaises(AttributeError, listIterator.remove)
