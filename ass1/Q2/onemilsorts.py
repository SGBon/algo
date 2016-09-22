#sorts 1,000,000 strings using mergesort, quicksort, and radix sort

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


from random import choice
from string import letters

def genstring(length):
    return "".join(choice(letters) for i in range(length))

import time

if __name__ == "__main__":
    unsorted = []
    for i in range(1000000):
        unsorted.append(genstring(100))
    print "sorting"
    mergetimes = []
    for i in range(100):
        elapsed = time.clock()
        mergesort(unsorted)
        elapsed = time.clock() - elapsed
        print elapsed
        mergetimes.append(elapsed)
    print mergetimes
