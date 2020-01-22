"""
Author: Ken Lambert
"""

from arrays import Array

class Grid(object):
    """ Represents a twodimensional array. """
    def __init__(self, rows, columns, fillValue = None):
        self.data = Array(rows)
        for  row in range(rows):
            self.data[row] = Array(columns, fillValue)

    def getHeight(self):
        """ Returns the number of rows. """
        return len(self.data)

    def getWidth(self):
        """ Returns the number of columns. """
        return len(self.data[0])

    def __getitem__(self, index):
        """ Supports two-dimensional indexing
        with [row][column]. """
        return self.data[index]

    def __str__(self):
        """ Returns a string representation of the grid. """
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                results += str(self.data[row][col]) + " "
            results += "\n"
        return result
