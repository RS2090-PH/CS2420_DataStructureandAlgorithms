import unittest
from tokens import Token
from expressiontree import LeafNode, InteriorNode


class UnitTests(unittest.TestCase):
    def test_InteriorNode_valueTest1(self):
        leaf1 = LeafNode(5)
        leaf2 = LeafNode(10)
        node = InteriorNode(Token('+'), leaf1, leaf2)
        self.assertEqual(node.value(), 15)

    def test_InteriorNode_valueTest2(self):
        leaf1 = LeafNode(5)
        leaf2 = LeafNode(10)
        node1 = InteriorNode(Token('+'), leaf1, leaf2)
        node2 = InteriorNode(Token('*'), leaf1, node1)
        self.assertEqual(node2.value(), 75)

    def test_InteriorNode_valueTest3(self):
        leaf1 = LeafNode(5)
        leaf2 = LeafNode(10)
        node1 = InteriorNode(Token('+'), leaf1, leaf2)
        node2 = InteriorNode(Token('*'), leaf1, node1)
        node3 = InteriorNode(Token('-'), node2, leaf2)
        self.assertEqual(node3.value(), 65)

    def test_InteriorNode_infixTest1(self):
        leaf1 = LeafNode(5)
        leaf2 = LeafNode(10)
        node1 = InteriorNode(Token('+'), leaf1, leaf2)
        node2 = InteriorNode(Token('*'), leaf1, node1)
        node3 = InteriorNode(Token('-'), node2, leaf2)
        s = "((5 * (5 + 10)) - 10)"
        self.assertEqual(node3.infix(), s)

    def test_InteriorNode_infixTest2(self):
        leaf1 = LeafNode(72)
        leaf2 = LeafNode(14)
        node1 = InteriorNode(Token('+'), leaf1, leaf2)
        node2 = InteriorNode(Token('*'), leaf1, node1)
        node3 = InteriorNode(Token('/'), node2, leaf2)
        s = "((72 * (72 + 14)) / 14)"
        print(node3.infix())
        self.assertEqual(node3.infix(), s)

    def test_InteriorNode_prefixTest1(self):
        leaf1 = LeafNode(5)
        leaf2 = LeafNode(10)
        node1 = InteriorNode(Token('+'), leaf1, leaf2)
        node2 = InteriorNode(Token('*'), leaf1, node1)
        node3 = InteriorNode(Token('-'), node2, leaf2)
        s = "- * 5 + 5 10 10"
        print(node3.prefix())
        self.assertEqual(node3.prefix(), s)

    def test_InteriorNode_prefixTest2(self):
        leaf1 = LeafNode(72)
        leaf2 = LeafNode(14)
        node1 = InteriorNode(Token('+'), leaf1, leaf2)
        node2 = InteriorNode(Token('*'), leaf1, node1)
        node3 = InteriorNode(Token('/'), node2, leaf2)
        s = "/ * 72 + 72 14 14"
        self.assertEqual(node3.prefix(), s)

    def test_InteriorNode_postfixTest1(self):
        leaf1 = LeafNode(5)
        leaf2 = LeafNode(10)
        node1 = InteriorNode(Token('+'), leaf1, leaf2)
        node2 = InteriorNode(Token('*'), leaf1, node1)
        node3 = InteriorNode(Token('-'), node2, leaf2)
        s = "5 5 10 + * 10 -"
        print(node3.postfix())
        self.assertEqual(node3.postfix(), s)

    def test_InteriorNode_postfixTest2(self):
        leaf1 = LeafNode(72)
        leaf2 = LeafNode(14)
        node1 = InteriorNode(Token('+'), leaf1, leaf2)
        node2 = InteriorNode(Token('*'), leaf1, node1)
        node3 = InteriorNode(Token('/'), node2, leaf2)
        s = "72 72 14 + * 14 /"
        self.assertEqual(node3.postfix(), s)
