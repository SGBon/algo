import graphreader
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print "Usage: %s [filename]" % sys.argv[0]
    sys.exit(0)

g = graphreader.read_graph(filename)
print "Nodes: %d Edges: %d" % (len(g.nodes),len(g.edges))
