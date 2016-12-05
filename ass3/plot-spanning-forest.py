import graphreader
import sys

if len(sys.argv) == 3:
    filename = sys.argv[1]
    outfile = sys.argv[2]
else:
    print "Usage: %s [input file] [output file]" % sys.argv[0]
    sys.exit(0)

g = graphreader.read_graph(filename)

import networkx as nx
from matplotlib import pyplot as plt

plt.figure()
    nx.draw(g,node_size=10,edge_color="gray",width=0.5)
plt.show()
