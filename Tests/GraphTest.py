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

    def test_add(self):
        test = Graph()
        self.assertEqual(0, test.vertex_size())
        self.assertEqual(0, test.edge_size())
        self.add_vertices(test)
        self.assertEqual(self.N, test.vertex_size())

    def test_Undirected(self):
        test = UndirectedGraph()
        self.add_vertices(test)
        self.make_complete(test)
        self.assertEqual((self.N * (self.N - 1))/2 + self.N, test.edge_size())



if __name__ == '__main__':
    unittest.main()
