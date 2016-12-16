class Graph(object):
    """
    Initializes the graph object with a list of vertices
    and edge adjacency list that consists of out going edges
    at index 0 and in going edges at index 1.
    """
    def __init__(self):
        self.vertices = set()
        self.edge_adj = []
        self.out_edges = {}
        self.in_edges = {}
        self.edge_adj.append(self.out_edges)
        self.edge_adj.append(self.in_edges)

    def get_out_edges(self):
        """ Returns the out edges of the graph. """
        return self.edge_adj[0]

    def get_in_edges(self):
        """ Returns the in edges of the graph. """
        return self.edge_adj[1]

    def get_vertices(self):
        """ Returns the vertices in the graph. """
        return self.vertices

    def get_successor(self, v):
        """ Returns the successors of the specified vertex v. """
        return self.get_out_edges()[v]

    def get_predecessor(self, v):
        """ Returns the predecessors of the specified vertex v. """
        return self.get_in_edges()[v]

    def add(self, vertex):
        """ Adds the vertex to the graph and properly initializes
        the vertex in the out_edges and in_edges list for adding edges.
        """
        self.vertices.add(vertex)
        self.get_in_edges()[vertex] = []
        self.get_out_edges()[vertex] = []

    def addEdge(self, u, v):
        """ Adds the edge from edge u to v. Meant to be overriden
        by the Graph subclasses mainly undirected and directed graphs.
        """

    def remove(self, vertex):
        """ Removes the vertex from the graph and all of its adjacent
        edges whether it be in or out edges.
        """

class UndirectedGraph(Graph):
    """Empty class"""

class DirectedGraph(Graph):
