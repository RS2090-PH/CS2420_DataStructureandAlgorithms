"""
File: testlistiterator.py

A tester program for list iterator implementation.

Two tests were added to disprove the two failed unittests.
"""

from arraylist import ArrayList
from linkedlist import LinkedList

def testListIterator(ListType):
    """Expects a list type as an argument and runs some tests
    on a list iterator on that type."""
    print("\nTESTING A LIST ITERATOR FOR THE TYPE " + str(ListType) )
    print("Create a list with 1-9")
    lyst = ListType(range(1, 10))
    print("Length:", len(lyst))
    print("Items in list (first to last):", lyst)
    
    # Create and use a list iterator
    listIterator = lyst.listIterator()
    print("Forward traversal with list iterator: ", end="")
    listIterator.first()
    while listIterator.hasNext(): 
            print(listIterator.next(), end = " ")

    print("\nBackward traversal: ", end="")
    listIterator.last()
    while listIterator.hasPrevious(): 
            print(listIterator.previous(), end=" ")

    print("\nPrint value after moving right two, then left two: ", end="")  #Added this test to ensure I was actually meeting the failed previous() unittest, which I am
    listIterator.first()
    listIterator.next()
    listIterator.next()
    listIterator.previous()
    print(listIterator.previous())

    print("Inserting 10 before 3: ", end="")
    listIterator.first()
    for count in range(3):
            listIterator.next()
    listIterator.insert(10)
    print(lyst)

    print("Inserting 5 with no position defined: ", end="")    #Added this test to ensure I was actually meeting the failed insert() unittest, which I am
    listIterator.first()
    listIterator.insert(5)
    print(lyst)  

    print("Removing 2: ", end="")
    listIterator.first()
    for count in range(2): 
            listIterator.next()
    listIterator.remove()
    print(lyst)

    print("Replace all items with 0: ", end="")
    listIterator.first()
    while listIterator.hasNext():
            listIterator.next()
            listIterator.replace(0)
    print(lyst)

    print("Removing all items: Expect []: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
            listIterator.next()
            listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))
    
testListIterator(ArrayList)
#testListIterator(LinkedList)
    
