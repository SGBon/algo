# implementation of a hashtable
class htentry:
    def __init__(self,key):
        self.key = key

class HashTable:
    # m is slots in hashtable
    # h is function to hash with
    def __init__(self,m,h):
        self.h = h
        self.T = [[] for i in range(m)]

    #
    def insert(self,x):
        index = self.h(x.key)
        self.T[index].append(x)

    def search(self,key):
        index = self.h(key)
        for x in self.T[index]:
            if x.key == key:
                return x
        return None

    def delete(self,key):
        index = self.h(key)
        for x in self.T[index]:
            if x.key == key:
             self.T[index].remove(x)


# we use currying because function pointers make this all the much simpler
# multiplication based function for hashing
import math
def h_mul(A,m):
    def c_mul(key):
        prod = key*A
        frac = prod - math.floor(prod)
        #if frac > 0.0:
            #print frac
        return int(math.floor(m*frac))
    return c_mul

# modulo based function for hashing
def h_mod(m):
    def c_mod(key):
        return (key*key) % m
    return c_mod
