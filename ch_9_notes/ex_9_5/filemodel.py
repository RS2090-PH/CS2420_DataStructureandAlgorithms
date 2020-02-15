"""
File: filemodel.py
Project 16.6

Data model for a file viewer.  Supports navigation
through the lines of a file. Also suppports insertions,
removals, and replacements of a line at the current position,
and saving the changes to the file.
"""

from linkedlist import LinkedList

class FileModel(object):

    def __init__(self, filename):
        # New instance variable _canModify permits or
        # disallows removals and replacements
        # New instance variable _filename needed to save
        # modifications to the file
        file = open(filename, 'r')
        self._list = LinkedList().listIterator()
        for line in file:
            self._list.insert(line)
        file.close()
        self._canModify = False
        self._filename = filename

    def first(self):
        self._list.first()
        self._canModify = True
        return self._list.next()

    def last(self):
        self._list.last()
        return self.previous()

    def next(self):
        if self._list.hasNext():
            self._canModify = True
            return self._list.next()
        else:
            return None

    def previous(self):
        if self._list.hasPrevious():
            self._canModify = True
            return self._list.previous()
        else:
            return None

    def canModify(self):
        """Returns True if a line can be removed or replaced
        or False otherwise."""
        if self._canModify == True:
            return True
        else:
            return False

    def insert(self, line):
        """Inserts line at the current position or at the
        end of the list if the position is undefined."""
        self._list.insert(line)

    def remove(self):
        """Precondition: canModify() returns True"""
        return self._list.remove()

    def replace(self, line):
        """Precondition: canModify() returns True"""
        if self.canModify() == True:
            return self._list.replace(line)

    def save(self):
        """Saves the list of lines to a file."""
        file = open(self._filename, "w")
        self._list.first()
        #file.write(str(self._list.first() + "\n"))

        while self._list.hasNext() is not False:
            file.write(str(self._list.next()))

        file.close()
