"""
File: testlist.py

A tester program for list implementations.
"""

from arraylist import ArrayList
from linkedlist import LinkedList

def main():
        # Create a list
        lyst = ArrayList()
        lyst.append("a")
        lyst.append("b")
        print("List contains: ", lyst)

        # Create a list iterator:
        listIterator = lyst.listIterator()
        
        print("Current cursor location: ", listIterator.cursor)
        print("hasNext(): ", listIterator.hasNext())
        listIterator.first()
        print("Current cursor location: ", listIterator.cursor)
        listIterator.next()
        print("Cursor location after next():" , listIterator.cursor)
        listIterator.replace("c")
        print("After replace: ", lyst)
        print(listIterator.next())
        print(listIterator.next())

        

if __name__ == "__main__":
        main()

