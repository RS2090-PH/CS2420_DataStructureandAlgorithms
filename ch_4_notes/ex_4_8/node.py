"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.

This project asks you to define some functions for manipulating linked structures. 
You should use the Node and TwoWayNode classes, as defined in this chapter. Create a 
tester module in testnode.py that contains your function definitions and your code for 
testing them.

Define a function length (not len) that expects a singly linked structure as an argument. 
The function returns the number of items in the structure.
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

    def length(self, head):
        probe = head
        while probe != None:
            length += 1
            probe = probe.next
            
        return length

def main():

    # Just an empty link
    node1 = None

    # A node containing data and an empty link
    node2 = Node("A", None)

    # A node containing data and a link to node2
    node3 = Node("B", node2)

if __name__ == "__main__":
    main()
