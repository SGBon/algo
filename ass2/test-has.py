import sys
import hashtable

# defaults
N = 100000
m = 10
func = "f3"
filename = "plot.png"
if len(sys.argv) == 5:
    N = int(sys.argv[1])
    m = int(sys.argv[2])
    func = argv[3]
    filename = argv[4]

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

for i in range(m):
    print "Length of slot %d %d" % (i,len(htable.T[i]))
