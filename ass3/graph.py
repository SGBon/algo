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
        return self.edges[v]

    def neighbours(self, v):
        return self.adjacency[v]

    def keys(self):
        return self.adjacency.keys()
