#sorts 1,000,000 strings using mergesort, quicksort, and radix sort

def mergesort(list):


from random import choice
from string import letters

def genstring(length):
    return "".join(choice(letters) for i in range(length))

if __name__ == "__main__":
    unsorted = []
    for i in range(1000000):
        unsorted.append(genstring(100))
    mergesort(unsorted)
