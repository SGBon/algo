import graph
import networkx as nx

def read_graph(filename):
    with open(filename,"r") as graph_file:
        g = graph.Graph()
        for line in graph_file:
            line = line.rstrip() # don't want those newline characters
            split = line.split("|")
            v1 = split[0]
            v2 = split[1]
            d = {"weight":split[2]}
            if g.node(v1) == None:
                g.add_node(v1,data=dict())
            if g.node(v2) == None:
                g.add_node(v2,data=dict())
            if g.edge(v1,v2) == None:
                g.add_edge(v1,v2,data=d)
        return g
