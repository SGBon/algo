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
    return i

def quicksort(L,p,r):
    if p < r:
        k = partition(L,p,r)
        quicksort(L,p,k-1)
        quicksort(L,k+1,r)

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
        extra = list(unsorted)
        elapsed = time.clock()
        mergesort(extra)
        mergetimes.append(time.clock() - elapsed)

    quicktimes = []
    for i in range(100):
        extra = list(unsorted) # need whole new list so we don't lose original
        elapsed = time.clock()
        quicksort(extra,0,len(extra)-1)
        quicktimes.append(time.clock() - elapsed)

    import matplotlib.pyplot as plt
    plt.plot(mergetimes,label="Mergesort")
    plt.plot(quicktimes,label="Quicksort")
    plt.plot(quicktimes,label="Quicksort")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), mode="expand", borderaxespad=0.)
    plt.ylabel("Elapsed Time in Seconds")
    plt.xlabel("Run")
    plt.show()
