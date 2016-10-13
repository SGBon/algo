#sorting algorithm to sort on disk
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


CHUNK_SIZE = 100
TOTAL_SIZE = 1000
CHUNKS = TOTAL_SIZE/CHUNK_SIZE
if __name__ == "__main__":
    # create CHUNKS sorted chunks of CHUNK_SIZE length
    # by reading CHUNK_SIZE strings at a time
    # overwrite unsorted file so that it's presorted
    with open("unsorted.txt","r+") as f:
        for i in range(CHUNKS):
            curr_chunk = [] # list to hold current chunk of strings
            lastbyte = f.tell()
            for j in range(CHUNK_SIZE):
                curr_chunk.append(f.readline())
            curr_chunk = mergesort(curr_chunk) # mergesort seperate chunks
            # overwrite chunk region in unsorted file
            currbyte = f.tell()
            f.seek(lastbyte)
            for j in curr_chunk:
                f.write(j)
            f.seek(currbyte)
        # return to beginning of file, perform CHUNKS-way merge
        # merge step appends smallest value at start of presorted chunks
        # to end of sorted file
        import btree
        bst = BST()
        with open("sorted.txt","w"):
            print "hello
