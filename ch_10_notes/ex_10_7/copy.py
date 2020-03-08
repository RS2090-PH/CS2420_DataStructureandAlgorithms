"""
File: expressiontree.py
Project 10.7  Completes the node classes for expression trees.

Defines nodes for expression trees.
"""

from tokens import Token

class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data=None):
        self.data = Token(data)

    def __str__(self):
        return str(self.data._value)

class InteriorNode(object):
    """Represents an operator and its two operands."""

    def __init__(self, oper=None, data1=None, data2=None):
        self.opper = oper
        self.first_leaf = data1
        self.second_leaf = data2

    def __str__(self):
        temp = "(%s %s %s)" % (self.first_leaf, self.opper, self.second_leaf)

        return temp

    def infix(self):
        #return None
        return "(%s %s %s)" % (self.first_leaf, self.opper, self.second_leaf)

    def prefix(self):
        def recurse(node):
            if type(node) is LeafNode:
                yield node._value
            else:
                yield node.opper._value
                recurse(node.first_leaf)
                recurse(node.second_leaf)
        recurse(self)

    def postfix(self):
        return None

    def value(self):
        return None


def main():
    a = LeafNode(4)
    b = InteriorNode(Token('+'), LeafNode(2), LeafNode(3))
    c = InteriorNode(Token('*'), a, b)
    c = InteriorNode(Token('-'), c, b) 
    if type(a) is LeafNode:
        print("yes")
    else:
        print("no")
    if type(b) is InteriorNode:
        print("yes")
    else:
        print("no")
    print("Expect ((4 * (2 + 3) - (2 + 3)):", c.infix())
    print("Expect - * 4 + 2 3 + 2 3       :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + -       :", c.postfix())
    print("Expect 15                      :", c.value())

if __name__ == "__main__":
    main()




