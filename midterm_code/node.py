class Node:

    ''' holds data in a singly linked list '''

    def __init__(self, data = 0, next=None):

        ''' initializes this Node '''

        self.next = next

        self.data = data