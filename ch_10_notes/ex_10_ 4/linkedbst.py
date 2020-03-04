"""
File: linkedbst.py
Project 10.3

Adds a method to rebalance the tree.
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from math import log
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue

class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.root = None
        AbstractCollection.__init__(self, sourceCollection)
        
    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self.root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self.root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                lyst.append(node.data)
                recurse(node.left)
                recurse(node.right)
        recurse(self.root)
        return iter(lyst)

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self.root)
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self.root)
        return iter(lyst)

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        lyst = list()
        queue = LinkedQueue()
        if not self.isEmpty():
            queue.add(self.root)
        while not queue.isEmpty():
            node = queue.pop()
            lyst.append(node.data)
            if node.left != None:
                queue.add(node.left)
            if node.right != None:
                queue.add(node.right)
        return iter(lyst)

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        def recurse(node):
            if node is None:
                return None
            elif node.data == item:
                return node.data
            elif node.data > item:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self.root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.root = None
        self.size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position 
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal, 
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self.root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self.root)
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty(): return None
        
        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self.root
        parent = preRoot
        direction = 'L'
        currentNode = self.root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right
                
        # Return None if the item is absent
        if itemRemoved == None: return None
        
        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentNode.left == None \
           and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:
            
        # Case 2: The node has no left child
            if currentNode.left == None:
                newChild = currentNode.right
                
        # Case 3: The node has no right child
            else:
                newChild = currentNode.left
                
        # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild
            
        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self.size -= 1
        if self.isEmpty():
            self.root = None
        else:
            self.root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        probe = self.root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        """Returns the height of the tree (the length of the longest path
        from the root to a leaf node).
        When len(t) < 2, t.height() == 0."""
        def recurse(node):
            if node == None:
                return 0
            else:
                return 1 + max(recurse(node.left), recurse(node.right))
        h = recurse(self.root)
        if not self.isEmpty():
            h -= 1
        return h

    def isBalanced(self):
        """Returns True if the tree is balaned or False otherwise.
        t is balanced iff t.height() < 2 * log2(len(t) + 1) - 1."""
        return self.height() < 2 *log(len(self) + 1, 2) - 1

    def rebalance(self):
        """Rebalances the tree."""
        def rebuild(data, first, last):
            if first <= last:
                mid = (first + last) // 2
                self.add(data[mid])
                rebuild(data, first, mid - 1)
                rebuild(data, mid + 1, last)
        data = list(self.inorder())
        self.clear()
        rebuild(data, 0, len(data) - 1)

    def predecessor(self, item):
        pred = LinkedStack()

        def recurse(node, item):
            if node != None:
                if item <= node.data:
                    recurse(node.left, item)
                elif item > node.data:
                    pred.push(node.data)
                    recurse(node.right, item)

        if self.isEmpty():
            return None
        else:
            recurse(self.root, item)

        result = None
        if not pred.isEmpty():
            result = pred.pop()

        return result

    def successor(self, item): #FIXME: Incomplete
        succ = LinkedStack()

        def recurse(node, item):
            if node != None:
                if item >= node.data:
                    recurse(node.right, item)
                elif item < node.data:
                    succ.push(node.data)
                    recurse(node.left, item)

        if self.isEmpty():
            return None
        else:
            recurse(self.root, item)

        result = None
        if not succ.isEmpty():
            result = succ.pop()

        return result


def main():
    t1 = LinkedBST()
    t1.add("G")
    t1.add("C")
    t1.add("B")
    t1.add("E")
    t1.add("D")
    t1.add("F")
    t1.add("K")
    t1.add("I")
    t1.add("H")
    t1.add("J")
    t1.add("M")
    t1.add("L")
    t1.add("N")

    print(t1.successor("B"))
    print(t1.successor("D"))
    print(t1.successor("F"))
    print(t1.successor("H"))
    print(t1.successor("O"))

    t2 = LinkedBST()
    print(t2.predecessor("A"))

if __name__ == "__main__":
    main()
