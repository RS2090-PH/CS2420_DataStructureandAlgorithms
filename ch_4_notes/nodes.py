class Node(object):
    """ Represents a singly linked node. """

    def __init__(self, data, next = None):
        self.data = data
        self.next = next 
        
class TwoWayNode(Node):

    def __init__(self, data, previous = None, next = None):
        """ Instantiates a TwoWayNode. """
        Node.__init__(self, data, next)
        self.preious = previous