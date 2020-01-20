"""
File: arrays.py
An Array is like a list, but the client can use
only [], len, and str.

To instantiate, use
<variable> = Array(<capacity>, <optional fill value>)

The fill value is non by default.
"""

class Array(object):
    """ Representing an array. """

    def __init__(self, capacity, fillValue = None):
        """ Capacity is the static size of teh array.
        fillValue is place at each position. """

        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)
        
        def __len__(self):
            """ -> The capacity of the array. """
            return len(self.items)

        def __str__(self):
            """ -> The string representation of the array. """
            return str(self.items)

        def __iter__(self):
            """ Supports traversal with a for loop. """
            return iter(self.items)

        def __getitem__(self, index):
            """ Subscript operator for access at index. """
            return self.items[index]

        def __setitem__(self, index, newItem):
            """ Subscript operator for replacement at index. """
            self.items[index] = newItem