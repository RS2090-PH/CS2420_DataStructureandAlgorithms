import unittest
from graph import LinkedEdge, LinkedDirectedGraph, LinkedVertex

class UnitTests(unittest.TestCase):
    def test_addEdge(self): # Tests error alert when adding duplicate edge
        g = LinkedDirectedGraph()
        g.addVertex("A")
        g.addVertex("B")
        g.addVertex("C")
        g.addEdge("A", "B", 2.5)
        with self.assertRaises(AttributeError):
            g.addEdge("A", "B", 2.5)

    def test_addVertex(self): # Tests error alert when adding duplicate vertex
        g = LinkedDirectedGraph()
        g.addVertex("A")
        g.addVertex("B")
        g.addVertex("C")
        g.addEdge("A", "B", 2.5)
        with self.assertRaises(AttributeError):
            g.addVertex("A")

    def test_getVertex(self): # Tests error alert when getting non-existent vertex
        g = LinkedDirectedGraph()
        g.addVertex("A")
        g.addVertex("B")
        g.addVertex("C")
        g.addEdge("A", "B", 2.5)
        with self.assertRaises(AttributeError):
            g.getVertex("F")

    def test_getEdge(self): # Tests error alert when getting non-existent edge
        g = LinkedDirectedGraph()
        g.addVertex("A")
        g.addVertex("B")
        g.addVertex("C")
        g.addEdge("A", "B", 2.5)
        with self.assertRaises(AttributeError):
            g.getEdge("Q", "P")