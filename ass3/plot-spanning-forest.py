import graphreader
import sys

def maximal_cut(G,X):
    w_max = None
    e_max = None
    for e in G.edges.keys():
        if e[0] in X and e[1] not in X:
            w = G.edges[e]["weight"]
            if  w_max == None or w > w_max:
                e_max = e
                w_max = w
    return e_max

def prim(G,r):
    n = len(G.keys())
    X = set([r])
    T = set([])
    for i in range(n-1):
        u = maximal_cut(G,X)
        if not u:
            return T
        g.node(u[1])["color"] = "black"
        X.add(u[1])
        T.add(u)
    return T

if len(sys.argv) == 3:
    filename = sys.argv[1]
    outfile = sys.argv[2]
else:
    print "Usage: %s [input file] [output file]" % sys.argv[0]
    sys.exit(0)

g = graphreader.read_graph(filename)

# initialize nodes for spanning forest finding
for r in g.keys():
    g.node(r)["color"] = "white"

# go through every node, if node is already checked
# don't calculate the mst, checked status
# is done just like bst
forest = []
for r in g.keys():
    if g.node(r)["color"] == "white":
        mst = prim(g,r)
        forest.append(mst)
        g.node(r)["color"] = "black"

print len(forest)

import networkx as nx
from matplotlib import pyplot as plt

todraw = g.to_nx()
plt.figure()
nx.draw(todraw,node_size=10,edge_color="gray",width=0.5)
plt.show()
