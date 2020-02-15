"""
File: filemodel.py
Project 9.4

Data model for a file viewer.  Supports navigation
through the lines of a file.
"""

from linkedlist import LinkedList

class FileModel(object):

    def __init__(self, filename):
        file = open(filename, "r")
        self.lyst = LinkedList()
        self.lyst_iter = LinkedList.ListIterator(self.lyst)
        for line in file:
            self.lyst_iter.insert(line)
        file.close

    def first(self):
        self.lyst_iter.first()
        return self.lyst_iter.next()

    def last(self):
        self.lyst_iter.last()
        return self.lyst_iter.previous()

    def next(self):
        return self.lyst_iter.next()

    def previous(self):
        return self.lyst_iter.previous()
        