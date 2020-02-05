"""
File: arrayqueue.py
"""

from arrays import Array
from abstractcollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Initalize self._front and self._rear here
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self._front = 0
        self._rear = 0
        self._count = 0
        AbstractCollection.__init__(self, sourceCollection)
        

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        pass
    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        return self.items[self._front]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self._front = 0
        self._rear = 0
        self.count = 0
        self.size = 0
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        if self._rear + 1 == len(self.items):
            temp = Array(len(self.items) * 2)
            for rep in range(0, len(self.items)):
                temp[rep] = self.items[rep]
            self.items = temp

            self.items[self._rear] = item
            self._count += 1
            self._rear += 1
            self.size += 1
        else:
            self.items[self._rear] = item
            self._count += 1
            self._rear += 1
            self.size += 1

        #if self._rear + 1 == self.DEFAULT_CAPACITY - 1:
        #    self.items[self._rear] = item
        #    self._count += 1
        #    self._rear += 1
        #    self.size += 1
        #else:
        #    self.items[self._rear] = item
        #    self._count += 1
        #    self._rear += 1
        #    self.size += 1
    
    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self._count == 0:
            raise KeyError()
        if self._front == self.DEFAULT_CAPACITY - 1:
            temp = self.items[self._front]
            self.items[self._front] = None
            self._front = 0
            self._count -= 1
            return temp
        else:
            temp = self.items[self._front]
            self.items[self._front] = None
            self._front += 1
            self._count -= 1
            return temp
            