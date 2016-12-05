import graph
import networkx as nx

def read_graph(filename):
    with open(filename,"r") as graph_file:
        g = nx.Graph()
        for line in graph_file:
            split = line.split("|")
            g.add_edge(split[0],split[1])
        return g

def old_read(filename):
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
            g.add_edge(v1,v2,data=d)
            g.add_edge(v2,v1,data=d)
    return g
