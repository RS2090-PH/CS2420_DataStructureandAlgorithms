"""
Author: Robby Stohel
File: stack.py

This file contains the Stack class and constructor/push/pop/top/size/clear
    methods used for creating and modifying a stack.
"""

class Stack(): # < Pylint said object wasn't necessary for cleanliness in python3...
    """
    The ADT Stack Class.

    Allows the user to:
        -create stack
        -push to stack
        -pop from stack
        -see top item in stack
        -see stack size
        -clear the stack
    """
    def __init__(self):
        """
        QuickDescription.
        Process:
             initializes a new abstract stack objects by using a list
             object and item count.
        Args:
            self: self
        Returns:
            ReturnValue(Type): ReturnDescription
        """
        self.stack = list()
        self.count = 0

    def __str__(self):
        """
        Allows user to print the stack as a string.
        Process:
            -creates a temp string and concatenates each value on
              the stack to the temp string, returning the temp
              string in the end
        Args:
            self: self
        Returns:
            temp(str): String created from stack items
        """
        temp = ""
        for item in self.stack:
            temp += (" " + item)

        return temp

    def push(self, item):
        """
        Pushes received item to the end of the stack.
        Process:
            -Increments stack item count
            -Receives item to be pushed onto stack and appends to stack
        Args:
            self: self
            item(int/float/str): Item to be pushed onto stack
        Returns:
            None
        """
        self.count += 1
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns top item on the stack.
        Process:
            -Decriments stack item count
            -Pops last item from stack
        Args:
            self: self
        Returns:
            Returns item removed from stack
        """
        if self.count <= 0:
            raise IndexError("Cannot pop from an empty stack.")
        self.count -= 1
        return self.stack.pop()

    def peek(self):
        """
        Returns the item at the top of the stack.
        Process:
            -checks the stack size and returns an IndexError if stack
              is empty
            -returns item at the end of stack
        Args:
            self: self
        Returns:
            last item in stack
        """
        if self.count <= 0:
            raise IndexError("No items currently in stack.")
        return self.stack[self.count  - 1]

    def size(self):
        """
        Returns the size of the stack.
        Process:
            -returns the current count for stack size
        Args:
            self: self
        Returns:
            self.count(int): The item count in the stack
        """
        return self.count

    def clear(self):
        """
        Removes every item in the stack.
        Process:
            -pops the items from the stack while the stack size
              is greater than 0.
        Args:
            self: self
        Returns:
            None
        """
        while self.count > 0:
            self.pop()
