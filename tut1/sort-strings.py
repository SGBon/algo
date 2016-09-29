import sys
import time

if len(sys.argv) < 2:
    print "Usage: f"
    sys.exit(0)

filename = sys.argv[1]

def timed_sort(array):
    start = time.time()
    array.sort()
    return time.time() - start

with open(filename,"r") as f:
    lines = f.readlines()
    t = timed_sort(lines)
    print "Sorted %d strings from %s in %.6f seconds" % (len(lines),filename,t)
