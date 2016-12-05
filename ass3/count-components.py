# based off of bfs
def count_components(G):
    for v in G.keys():
        G.node(v)["color"] = "white"

    count = 0
    for s in G.keys():
        if G.node(s)["color"] == "white":
            queue = [s]
            G.node(s)["color"] = "gray"

            while len(queue) > 0:
                u = queue.pop(0)
                for v in G.neighbours(u):
                    if G.node(v)["color"] == "white":
                        queue.append(v)
                        G.node(v)["color"] = "gray"
                G.node(u)["color"] = "black"
            count = count + 1
    return count

import graphreader
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print "Usage: %s [filename]" % sys.argv[0]
    sys.exit(0)

g = graphreader.old_read(filename)
print count_components(g)
