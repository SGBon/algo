import sys
import hashtable

# defaults
N = 1000
m = 10
func = "f3"
filename = "plot.png"
if len(sys.argv) == 5:
    N = int(sys.argv[1])
    m = int(sys.argv[2])
    func = sys.argv[3]
    filename = sys.argv[4]

# get our hashfunc
if func == "f1":
    h = hashtable.h_mod(m)
elif func == "f2":
    h = hashtable.h_mul(0.2,m)
elif func == "f3":
    h = hashtable.h_mul(0.618034,m)
else:
    h = hashtable.h_mul(0.8,m)

htable = hashtable.HashTable(m,h)

import random
for i in range(N):
    x = hashtable.htentry(random.randint(0,sys.maxint))
    htable.insert(x)

largest = 0;
lengths = []
for i in range(m):
    length = len(htable.T[i])
    lengths.append(length)
    largest = length if length > largest else largest
    print "slot %d had %d collisions" % (i,length)
print "Largest collision was %d" % largest

import matplotlib.pyplot as plt
from pylab import savefig
plt.bar(range(m),lengths)
plt.title("Collisions per slot using %s N=%d m=%d" % (func,N,m))
plt.ylabel("Collisions")
plt.xlabel("Slot")
savefig(filename, bbox_inches='tight')
