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

    test.remove(21)
    test.remove(9)
    test.remove(4)
    test.remove(18)
    test.remove(15)
    test.remove(7)
    print(test)

if __name__ == "__main__":
    main()
