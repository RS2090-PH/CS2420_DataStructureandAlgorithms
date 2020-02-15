"""
Author: Robby Stohel
File: stack.py

This file contains the Stack class and constructor/push/pop/top/size/clear
    methods used for creating and modifying a stack.
"""

class Stack(): # < Pylint said object wasn't necessary for cleanliness in pythong3...
    """
    QuickDescription.
    """
    def __init__(self):
        """
        QuickDescription.
        Process:
            FullProcessDescription.
        Args:
            Argument(Type): ArgDescription
        Returns:
            ReturnValue(Type): ReturnDescription
        """
        self.stack = list()
        self.count = 0

    def push(self, item):
        """
        QuickDescription.
        Process:
            FullProcessDescription.
        Args:
            Argument(Type): ArgDescription
        Returns:
            ReturnValue(Type): ReturnDescription
        """
        self.count += 1
        self.stack.append(item)

    def pop(self):
        """
        QuickDescription.
        Process:
            FullProcessDescription.
        Args:
            Argument(Type): ArgDescription
        Returns:
            ReturnValue(Type): ReturnDescription
        """
        if self.count <= 0:
            raise IndexError("Cannot pop from an empty stack.")
        self.count -= 1
        return self.stack.pop()

    def top(self):
        """
        QuickDescription.
        Process:
            FullProcessDescription.
        Args:
            Argument(Type): ArgDescription
        Returns:
            ReturnValue(Type): ReturnDescription
        """
        if self.count <= 0:
            raise IndexError("No items currently in stack.")
        return self.stack[self.count  - 1]

    def size(self):
        """
        QuickDescription.
        Process:
            FullProcessDescription.
        Args:
            Argument(Type): ArgDescription
        Returns:
            ReturnValue(Type): ReturnDescription
        """
        return self.count

    def clear(self):
        """
        QuickDescription.
        Process:
            FullProcessDescription.
        Args:
            Argument(Type): ArgDescription
        Returns:
            ReturnValue(Type): ReturnDescription
        """
        while self.count > 0:
            self.pop()
