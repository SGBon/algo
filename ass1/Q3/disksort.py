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

#utility functions
def zeros(n):
    return [0] * n

def string_at_pos(pos,file):
    file.seek(pos)
    return file.readline(),file.tell()


if __name__ == "__main__":
    # create CHUNKS sorted chunks of CHUNK_SIZE length
    # by reading CHUNK_SIZE strings at a time
    # overwrite unsorted file so that it's presorted
    CHUNK_SIZE = 100
    TOTAL_SIZE = 1000
    CHUNKS = TOTAL_SIZE/CHUNK_SIZE
    chunk_starts = zeros(CHUNKS) # beginning of chunks within file as byte offsets
    with open("unsorted.txt","r+") as unfile:
        for i in range(CHUNKS):
            curr_chunk = [] # list to hold current chunk of strings
            lastbyte = unfile.tell()
            chunk_starts[i] = lastbyte
            for j in range(CHUNK_SIZE):
                curr_chunk.append(unfile.readline())
            curr_chunk = mergesort(curr_chunk) # mergesort seperate chunks
            # overwrite chunk region in unsorted file
            currbyte = unfile.tell()
            unfile.seek(lastbyte)
            for j in curr_chunk:
                unfile.write(j)
            unfile.seek(currbyte)

        # return to beginning of file, perform CHUNKS-way merge
        # merge step appends smallest value at start of presorted chunks
        # to end of sorted file
        unfile.seek(0)
        from btree import BST
        bst = BST() # binary tree to search smallest value quickly during merge step
        fpos = zeros(CHUNKS) # position offsets in unsorted file
        STRING_LENGTH = 20
        with open("sorted.txt","w") as sofile:
            print chunk_starts
            print fpos
            print string_at_pos(chunk_starts[1] + fpos[1],unfile)
