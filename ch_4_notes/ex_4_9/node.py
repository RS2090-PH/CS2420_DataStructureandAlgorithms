"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.

This project asks you to define some functions for manipulating linked structures. 
You should use the Node and TwoWayNode classes, as defined in this chapter. testnode.py 
contains a main() and has been provided to you.

Define a function named insert that inserts an item into a singly linked structure at a 
given position. The function expects three arguments: the item, the position, and the linked 
structure. (The latter may be empty.) The function returns the modified linked structure. 
If the position is greater than or equal to the structure’s length, the function inserts the 
item at its end. An example call of the function, where head is a variable that either is an 
empty link or refers to the first node of a structure, is head = insert(1, data, head).
"""

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

class TwoWayNode(Node):

    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous

# Just an empty link
node1 = None

# A node containing data and an empty link
node2 = Node("A", None)

# A node containing data and a link to node2
node3 = Node("B", node2)
