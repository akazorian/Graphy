from random import randint
import sys
sys.path.append("/Users/Alex_Kazorian/Documents/Projects/Graphy/Package")

import unittest
from Graph import *

class TestGraphPackage(unittest.TestCase):

    N = 1000

    def add_vertices(self, graph):
        for v in range(self.N):
            graph.add(v)

    def make_complete(self, graph):
        for u in range(self.N):
            for v in range(self.N):
                graph.add_edge(u, v)

    def u_remove(self, test):
        self.add_vertices(test)
        self.make_complete(test)
        self.assertEqual((self.N * (self.N - 1))/2 + self.N, test.edge_size())
        for i in range(self.N):
            test.remove(i)
            self.assertFalse(test.contains(i))
            for n in range(i, self.N):
                self.assertFalse(test.contains_edge(i, n))
                self.assertFalse(test.contains_edge(n, i))

    def u_edge_remove(self, test):
        self.add_vertices(test)
        self.make_complete(test)
        for u in test.get_vertices():
            v = randint(0, self.N)
            test.removeEdge(u, v)
            self.assertFalse(test.contains_edge(u, v))
            self.assertFalse(test.contains_edge(v, u))

    def d_remove(self, test):
        self.add_vertices(test)
        self.make_complete(test)
        self.assertEqual(self.N * self.N, test.edge_size())
        for i in range(self.N):
            test.remove(i)
            self.assertFalse(test.contains(i))
            for n in range(i, self.N):
                self.assertFalse(test.contains_edge(i, n))

    def d_edge_remove(self, test):
        self.add_vertices(test)
        self.make_complete(test)
        for u in test.get_vertices():
            v = randint(0, self.N)
            test.removeEdge(u, v)
            self.assertFalse(test.contains_edge(u, v))

    def test_add(self):
        test = Graph()
        self.assertEqual(0, test.vertex_size())
        self.assertEqual(0, test.edge_size())
        self.add_vertices(test)
        self.assertEqual(self.N, test.vertex_size())

    def test_Undirected(self):
        test = UndirectedGraph()
        self.u_remove(test)
        self.u_edge_remove(test)

    def test_Directed(self):
        test = DirectedGraph()
        self.d_remove(test)
        self.d_edge_remove(test)

if __name__ == '__main__':
    unittest.main()
