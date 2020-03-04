from node import Node

class LinkedList:

    ''' manipulates a linked-list of Nodes '''

    def __init__(self):
        self.head = None

    def InsertAtFront(self, data):

        ''' adds a new Node at the front if the linked-list '''
        self.head = Node(data, self.head) #Exam question, to complete

    def __str__(self):

        ''' returns a string representation of the linked-list '''
        probe = self.head #Exam question, to complete
        temp = ""
        front = 1
        
        while probe != None:
            if front == 1:
                temp = temp + str(probe.data)
                probe = probe.next
                front -= 1
            else:
                temp = temp + ", " + str(probe.data)
                probe = probe.next

        return temp

    def InsertAtTail(self, data):

        ''' adds a new Node at the tail (or end) of the linked-list '''
        probe = self.head #Exam question, to complete
        tail = None
        while probe.next != None:
            tail = probe
            probe = probe.next
        tail = probe
        probe = Node(data, probe.next)
        tail.next = probe
        

    def RemoveFromFront(self):
        
        ''' Removes the first node of the linked-list.'''
        temp = self.head.data #Exam question, to complete
        self.head = self.head.next

        return temp

    def __contains__(self, target):

        ''' returns True if target is in the linked-list '''

        pass


def main():
    test = LinkedList() #Added post-test, to check my work. Total
    print(test)         #fail but that's what happens without an 
                        #IDE to test code.

    test.InsertAtFront("Tail")
    test.InsertAtFront(3)
    test.InsertAtFront(2)
    test.InsertAtFront(1)
    test.InsertAtFront("Front")
    print(test)

    test2 = test
    test2.RemoveFromFront()
    test2.RemoveFromFront()
    print(test2)

    test3 = test
    test3.InsertAtTail("NewTail")
    print(test3)


if __name__ == "__main__":
    main()
