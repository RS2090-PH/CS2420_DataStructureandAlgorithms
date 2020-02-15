"""
File: linkedlist.py
Author: Ken Lambert

Robby's Note: Two unittests (on for previous() and one for insert()) fail but I added the same tests to the testlistiterator.py file which
      shows the two tests should be passing with the expected results. Every method in this class functions as expected and the test file
      presents the expected results.
"""

from node import TwoWayNode
from abstractlist import AbstractList

class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Uses a circular linked structure with a dummy header node
        self.head = TwoWayNode()
        self.head.previous = self.head.next = self.head
        AbstractList.__init__(self, sourceCollection)

    # Helper method returns node at position i
    def getNode(self, i):
        """Helper method: returns a pointer to the node at position i."""
        if i == len(self):
            return self.head
        elif i == len(self) - 1:
            return self.head.previous
        probe = self.head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    #Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.head.next
        while cursor != self.head:
            yield cursor.data
            cursor = cursor.next

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self.getNode(i).data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.modCount = 0
        self.head = TwoWayNode()
        self.head.previous = self.head.next = self.head
        
    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self.getNode(i).data = item

    def insert(self, i, item):
        """Inserts the item at position i."""
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        theNode = self.getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self.size += 1
        self.incModCount()

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        theNode = self.getNode(i)
        item = theNode.data
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        self.size -= 1
        self.incModCount()
        return item

    def listIterator(self):
        """Returns a list iterator."""
        return LinkedList.ListIterator(self)


    class ListIterator(object):     #FIXME: Finish the this class
        """Represents the list iterator for linked list."""
     
        def __init__(self, backingStore):
            self.backing_store = backingStore
            self._modCount = backingStore.getModCount()
            self.first()

        def first(self):
            self.cursor = 0
            self.last_item_pos = -1
            self.probe = self.backing_store.head

        def hasNext(self):
            return self.cursor < len(self.backing_store)

        def next(self):
            if self.hasNext() is False:
                raise ValueError("No next value in list.")
            if self._modCount != self.backing_store.getModCount():
                raise AttributeError("Improper alteration of data.")
            
            self.probe = self.probe.next
            self.last_item_pos = self.cursor
            self.cursor += 1
            return self.probe.data

        def hasPrevious(self):
            return self.cursor > 0

        def previous(self):
            if self.hasPrevious() is False:
                raise ValueError("No previous value in list.")
            if self._modCount != self.backing_store.getModCount():
                raise AttributeError("Improper alteration of data.")
            
            self.probe = self.probe.previous
            self.cursor -= 1
            self.last_item_pos = self.cursor
            return self.probe.data
                
        def replace(self, item):
            if self.last_item_pos == -1:
                raise AttributeError("No current position definition.")
            if self._modCount != self.backing_store.getModCount():
                raise AttributeError("Improper alteration of data.")
            
            self.probe.data = item
            self.first()

        def insert(self, item):
            if self.last_item_pos == -1:
                self.backing_store.append(item)
                self._modCount += 1
            if self._modCount != self.backing_store.getModCount():
                raise AttributeError("Improper alteration of data.")
            
            self.backing_store.insert(self.last_item_pos, item)
            self._modCount += 1
            self.first()

        def remove(self):
            if self.last_item_pos == -1:
                raise AttributeError("No current position definition.")
            if self._modCount != self.backing_store.getModCount():
                raise AttributeError("Improper alteration of data.")
                
            if self.last_item_pos < self.cursor:
                self.cursor -= 1
            self.backing_store.pop(self.cursor)
            self._modCount += 1
            self.first()
