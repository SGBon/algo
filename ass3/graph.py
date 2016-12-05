import networkx as nx

class Graph:
    def __init__(self):
        self.adjacency = dict()
        self.nodes = dict()
        self.edges = dict()

    def add_node(self, v, data=None):
        self.adjacency[v] = []
        self.nodes[v] = data

    def add_edge(self, v1, v2, data=None):
        self.adjacency[v1].append(v2)
        self.edges[(v1,v2)] = data

    def node(self, v):
        return self.nodes.get(v)

    def edge(self, v1, v2):
        return self.edges.get(v1,v2)

    def neighbours(self, v):
        return self.adjacency[v]

    def keys(self):
        return self.adjacency.keys()

    def to_nx(self):
        g = nx.Graph()
        g.add_nodes_from(self.nodes.keys())
        g.add_edges_from(self.edges.keys())
        return g
