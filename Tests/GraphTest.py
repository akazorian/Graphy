import sys
sys.path.append("/Users/Alex_Kazorian/Documents/Projects/Graphy/Package")

import unittest
from Graph import *

class TestGraphPackage(unittest.TestCase):

    N = 1000

    def add_vertices(self, graph, number):
        for v in range(number):
            graph.add(v)

    def test_add(self):
        test = Graph()
        self.assertEqual(0, test.vertex_size())
        self.assertEqual(0, test.edge_size())
        self.add_vertices(test, self.N)
        self.assertEqual(1000, test.vertex_size())

if __name__ == '__main__':
    unittest.main()
