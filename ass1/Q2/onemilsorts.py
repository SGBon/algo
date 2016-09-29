#sorts 1,000,000 strings using mergesort, quicksort, and radix sort

# mergesort functions
def merge(list1, list2):
    i, j = 0, 0
    list3 = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    if i < len(list1):
        list3.extend(list1[i:])
    if j < len(list2):
        list3.extend(list2[j:])

    return list3

def mergesort(list):
    sortedness = 1

    while sortedness < len(list):
        for i in range(0, len(list), 2*sortedness):
            list1 = list[i:i+sortedness]
            list2 = list[i+sortedness:i+2*sortedness]
            list3 = merge(list1, list2)
            list[i:i+len(list3)] = list3
        sortedness = 2 * sortedness

    return list

# quicksort functions

def partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return i+1

def quicksort(L,p,r):
    if p < r:
        k = partition(L,p,r)
        quicksort(L,p,k-1)
        quicksort(L,k+1,r)

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
    x = radix2(num)
    if i >= len(x):
        return 0
    else:
        d = x[-(i+1)]
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

def RADIX_SORT(A):
    n = max(len(radix2(x)) for x in A)
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
    for i in range(10000):
        unsorted.append(genstring(100))
    print "sorting"

    mergetimes = []
    for i in range(100):
        extra = list(unsorted) # need whole new list so we don't lose original
        elapsed = time.clock()
        mergesort(extra)
        mergetimes.append(time.clock() - elapsed)

    quicktimes = []
    for i in range(100):
        extra = list(unsorted)
        elapsed = time.clock()
        quicksort(extra,0,len(extra)-1)
        quicktimes.append(time.clock() - elapsed)

    radxtimes = []
    for i in range(100):
        extra = list(unsorted)
        elapsed = time.clock()
        radixsort(extra)
        radixtimes.append(time.clock() - elapsed)

    import matplotlib.pyplot as plt
    plt.plot(mergetimes,label="Mergesort")
    plt.plot(quicktimes,label="Quicksort")
    plot.plot(radixtimes,label="Radixsort")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), mode="expand", borderaxespad=0.)
    plt.ylabel("Elapsed Time in Seconds")
    plt.xlabel("Run")
    plt.show()
