"""
File: abstractstack.py
Author: Ken Lambert
"""

from abstractcollection import AbstractCollection

class AbstractStack(AbstractCollection):
    """An abstract stack implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.sourceCollection = sourceCollection
        self.ab_collection = AbstractCollection(self.sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        self.push(item)

    def push(self, item):
        """Inserts item at top of the stack."""
        self.ab_collection[len(self)] = item 
        self.size += 1
    