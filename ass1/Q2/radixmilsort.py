#sorts 1,000,000 strings using radix sort
# radixsort functions
# convert data to bit string
def radix2(data):
    if type(data) is int: # convert integer to bit string
        return "{0:b}".format(data)
    elif type(data) is str: # convert a character string to bit string
        ret = ''.join('{0:08b}'.format(ord(x), 'b') for x in data) # need full bytes
        return ret

# Get the i-th digit of binary string x
def digit(num,i):
    if i >= len(num):
        return 0
    else:
        d = num[-(i+1)]
        return 0 if d == '0' else 1

def empty_array(size, init=None):
    return [init for i in range(size)]

# sort A using binary digit i
def COUNTING_SORT(A,i):
    n = len(A)
    k = 2
    B = empty_array(size=n)
    C = empty_array(size=k,init=0)

    for a in A:
        d = digit(a,i)
        C[d] = C[d] + 1

    for j in range(1,k):
        C[j] = C[j] + C[j-1]

    for a in reversed(A):
        d = digit(a,i)
        B[C[d]-1] = a
        C[d] = C[d] - 1

    return B

def RADIX_SORT(A,n):
    for i in range(n):
        A = COUNTING_SORT(A,i)
    return A

from random import choice
from string import uppercase

def genstring(length):
    return "".join(choice(uppercase) for i in range(length))

import time

if __name__ == "__main__":
    unsorted = []
    for i in range(1000000):
        unsorted.append(genstring(100))

    # convert unsorted strings to binary once
    unsortedbins = []
    for i in unsorted:
        unsortedbins.append(radix2(i))

    # compute largest binary string for radix sort once
    n = max(len(radix2(x)) for x in unsorted)
    print "sorting"
    extra = list(unsortedbins)
    elapsed = time.clock()
    RADIX_SORT(extra,n)
    print "Time to sort one million strings with radix sort ",time.clock() - elapsed
