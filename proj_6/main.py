"""
Author: Robby Stohel
File: Main.py

This file provides a main driver to test the binary search and node classes.
"""

from binarysearchtree import BinarySearchTree

def main():
    """ Main driver function to test binary search. """
    test = BinarySearchTree()
    test.add(21)
    test.add(26)
    test.add(30)
    test.add(9)
    test.add(4)
    test.add(14)
    test.add(28)
    test.add(18)
    test.add(15)
    test.add(10)
    test.add(2)
    test.add(3)
    test.add(7)

    preorder = test.preorder()
    for item in preorder:
        print(str(item) + ", ", end=" ")
    print("")
    print(test)
    print("Lonsg string so I can see the test height: ", test.height())

    test.remove(21)
    test.remove(9)
    test.remove(4)
    test.remove(18)
    test.remove(15)
    test.remove(7)
    print(test)

    bst = BinarySearchTree()
    print("Produced: ", bst.height())
    print("Expects: ", -1)
    for i in range(511):
        bst.add(i)

    print("Produced: ", bst.height())
    print("Expects: ", 510)
    bst.rebalance_tree()
    print("Produced: ", bst.height())
    print("Expects: ", 8)

    newtest = BinarySearchTree()
    for i in range(7):
        newtest.add(i)
    newtest.rebalance_tree()
    print(newtest)

    lasttest = BinarySearchTree()
    lasttest.add(1)
    print("Added")
    lasttest.add(1)

if __name__ == "__main__":
    main()
