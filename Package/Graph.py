""" In this module, you will find a generic Graph super class
that is to be extended to implement undirected and directed graphs.
"""

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
        self.edge_count = 0
        self.vertex_count = 0

    def vertex_size(self):
        """ Returns the number of vertices in the graph. """
        return self.vertex_count

    def edge_size(self):
        """ Returns the number of edges in the graph. """
        return self.edge_count

    def get_out_edges(self):
        """ Returns the out edges of the graph. """
        return self.edge_adj[0]

    def get_in_edges(self):
        """ Returns the in edges of the graph. """
        return self.edge_adj[1]

    def get_vertices(self):
        """ Returns the vertices in the graph. """
        return self.vertices

    def get_successor(self, vertex):
        """ Returns the successors of the specified vertex v. """
        return self.get_out_edges()[vertex]

    def get_predecessor(self, vertex):
        """ Returns the predecessors of the specified vertex v. """
        return self.get_in_edges()[vertex]

    def contains(self, vertex):
        """ Returns true iff I contain the vertex. """
        return vertex in self.get_vertices()

    def contains_edge(self, u, v):
        """ Returns true iff I contain the edges
        from u to v. """
        return self.contains(u) and self.contains(v) and u in self.get_out_edges() and v in self.get_successor(u)

    def add(self, vertex):
        """ Adds the vertex to the graph and properly initializes
        the vertex in the out_edges and in_edges list for adding edges.
        """
        self.vertices.add(vertex)
        self.get_in_edges()[vertex] = []
        self.get_out_edges()[vertex] = []
        self.vertex_count += 1

    def add_edge(self, u, v):
        """ Adds the edge from edge u to v. Meant to be overriden
        by the Graph subclasses mainly undirected and directed graphs.
        """

    def remove(self, vertex):
        """ Removes the vertex from the graph and all of its adjacent
        edges whether it be in or out edges.
        """

    def removeEdge(self, u, v):
        """ Removes the edge (u, v) from the graph as specified by the
        graph type. If the graph is of the type UndirectedGraph, then the edge
        (u, v) and (v, u) should be removed from out_edges and in_edges. If the
        graph is of the type DirectedGraph, then only the edge (u, v) should be
        removed.
        """

class UndirectedGraph(Graph):
    """ Representation of an undirected graph. """

    def add_edge(self, u, v):
        if not self.contains_edge(u, v):
            self.get_predecessor(u).append(v)
            self.get_successor(u).append(v)
            self.get_predecessor(v).append(u)
            self.get_successor(v).append(u)
            self.edge_count += 1

    def remove(self, vertex):
        if self.contains(vertex):
            successor = self.get_successor(vertex)
            self.vertices.remove(vertex)
            self.out_edges.pop(vertex, None)
            self.in_edges.pop(vertex, None)
            for v in successor:
                if v != vertex:
                    self.get_successor(v).remove(vertex)
                    self.get_predecessor(v).remove(vertex)

    def removeEdge(self, u, v):
        if self.contains_edge(u, v):
            self.get_successor(u).remove(v)
            self.get_predecessor(u).remove(v)
            self.get_successor(v).remove(u)
            self.get_predecessor(v).remove(u)

class DirectedGraph(Graph):
    """ Representation of a directed graph. """

    def add_edge(self, u, v):
        if not self.contains_edge(u, v):
            self.get_successor(u).append(v)
            self.get_predecessor(v).append(u)
            self.edge_count += 1

    def remove(self, vertex):
        if self.contains(vertex):
            successor = self.get_successor(vertex)
            predecessor = self.get_predecessor(vertex)
            self.vertices.remove(vertex)
            self.out_edges.pop(vertex, None)
            self.in_edges.pop(vertex, None)
            for v in successor:
                if v != vertex:
                    self.get_predecessor(v).remove(vertex)
            for v in predecessor:
                if v != vertex:
                    self.get_successor(v).remove(vertex)

    def removeEdge(self, u, v):
        if self.contains_edge(u, v):
            self.get_successor(u).remove(v)
            self.get_predecessor(v).remove(u)

class WeightedGraph(object):
    """
    Initializes a weighted graph. In effect, all edges
    have a weight. If not specified, it will default to 0.
    This class can work with either directed graphs or undirected
    graphs depending on the graph given to the constructor.
    """
    def __init__(self, graph):
        self.graph = graph
        self.weights = {}

    def add_edge(self, u, v, weight=0):
        """
        Adds the edge 'u:v' to the graph with the specified
        weight. If a weight is not given, then the default value
        is 0.
        """

    def remove(self, vertex):
        """
        Removes the vertex and all edges connected to the vertex
        from the graph, along with all their edge weights.
        """

    def removeEdge(self, u, v):
        """
        Removes the edge 'u:v' from the graph. Removes the edge weight from
        self as well.
        """

    def set_weight(self, u, v, weight):
        """
        Sets the weight of the edge 'u:v' in graph to the specified weight.
        """
        if self.graph.contains_edge(u, v):
            self.weights["{}:{}".format(u, v)] = weight

    def get_weight(self, u, v):
        """ Returns the weight for the edge u:v """
        if self.graph.contains_edge(u, v):
            return self.weights["{}:{}".format(u, v)]
