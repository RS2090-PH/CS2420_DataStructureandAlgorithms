"""
File: expressiontree.py
Project 10.7  Completes the node classes for expression trees.

Defines nodes for expression trees.
"""

from tokens import Token

class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data):
        self.data = data

    def postfix(self):
        return str(self.data)

    def prefix(self):
        return str(self.data)

    def infix(self):
        return str(self.data)

    def value(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

class InteriorNode(object):
    """Represents an operator and its two operands."""

    def __init__(self, op, leftOper, rightOper):
        self.operator = op
        self.leftOperand = leftOper
        self.rightOperand = rightOper

    def postfix(self):
        return self.leftOperand.postfix() + " " + \
            self.rightOperand.postfix() + " " + \
                str(self.operator)

    def prefix(self):
        return str(self.operator) + " " + \
            self.leftOperand.prefix() + " " + \
                self.rightOperand.prefix()

    def infix(self):
        return "(" + self.leftOperand.infix() + " " + \
            str(self.operator) + " " + \
                self.rightOperand.infix() + ")"

    def value(self):
        return eval("(" + self.leftOperand.infix() + " " + \
            str(self.operator) + " " + \
                self.rightOperand.infix() + ")")

def main():
    a = LeafNode(4)
    b = InteriorNode(Token('+'), LeafNode(2), LeafNode(3))
    c = InteriorNode(Token('*'), a, b)
    c = InteriorNode(Token('-'), c, b) 
    print("Expect ((4 * (2 + 3) - (2 + 3)):", c.infix())
    print("Expect - * 4 + 2 3 + 2 3       :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + -       :", c.postfix())
    print("Expect 15                      :", c.value())

if __name__ == "__main__":
    main()
