# generate 100,000,000 strings and write to file strings.txt

from random import choice
from string import uppercase

def genstring(length):
    return "".join(choice(uppercase) for i in range(length))

if __name__ == "__main__":
    f = open("unsorted.txt","w")
    for i in range(100000000):
        f.write(genstring(100))
        f.write("\n")
    f.close()
