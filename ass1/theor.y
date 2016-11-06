1.1
The functionality of the function 'f' is to determine and return true if any element in list 'x' is 0; false otherwise or if 'x' has no elements.

1.2
T(n) = O(1) when n <= 1
T(n) = 3T(n/3) otherwise

1.3
assume T(n) = 3T(n/3), need to show T(n) = O(n)
there exist some a,b such that T(n) < an + b, for all large n
suppose T(k) <= ak + b for all k < n, we show T(n) <= an + b

T(n) = 3T(n/3)
  <= 3(a(n/3) + b)
  <= an + b
a >= b

we showed T(n) = 3T(n/3) which implies some a,b exist such that T(n) <= an + b
therefore -> T(n) = O(n) Q.E.D.

1.4
function f(x: List[Integer]){
  var anyzero: Boolean = false
  var n: Integer = Length(x)
  for(var i = 0; i < n; ++i){
    if(x[i] == 0){
      anyzero = true
      break
    }
  }
  return anyzero
}

1.5
Both the recursive and iteration approach have the same runtime complexity of O(n)

2.1
1 byte/char * 100 chars/string * 1,000,000 strings = 100,000,000 bytes ~ 95.367 megabytes

2.3
The chart showing comparison between merge sort and quick sort is shown below. Radix sort took a very long time to perform just one run (16.6 minutes) so I did not bother running it 100 times (as that would take 27 hours) and it is clear that it performs much worse than the other two sorts.

3.1
1 byte/char * 100 chars/string * 100,000,000 strings = 10,000,000,000 bytes ~ 9.313 gigabytes

3.3
DISK-BASED-SORT(n):
  n = total number of strings
  k = number of strings in a chunk
  c = n/k // number of chunks
  starts = array[0..c] // position in file where chunks begin
  // sort c chunks of strings of length k separately using merge sort and overwrite chunks in file
  open unsorted file for reading
  for i = 0 to c
    current-chunk = array[0..k]
    starts[i] = position in file
    for j = 0 to k
      current-chunk(j) = next-string-in-file
    mergesort(current)
    seek in file to position at starts[i]
    for j = 0 to k
      write to file current-chunk(j)

  // perform an c-way merge
  set position in unsorted file to beginning
  chunk-position = array[0..c] // current position in unsorted file for each chunk
  open file for sorted list
  bst = a binary search tree
  // populate a binary search tree with front value of each chunk
  for i = 0 to c
    nextstring = string in unsorted file at chunk-position(i)
    chunk-position(i) = new file position
    add nextstring with chunk number to bst

  while bst has > 0 elements
    smallest-string = remove smallest value in bst
    chunk = chunk smallest-string originates from
    append smallest-string to end of file
    if chunk-position(chunk) < k
      nextstring = string in unsorted file at chunk-position(chunk)
      chunk-position(chunk) = current position in file
      add nextstring with chunk to bst

3.4
with n = total number of strings, k = number of strings in a chunk, and c = n/k
first we sort c chunks using merge sort. Merge sort has a complexity of u*log(u) for some u being the length of of an input array, and
each chunk is k strings long, so the complexity of sorting each of these chunks is:
c*(k*log(k))

The second half of the algorithm is merging c chunks. to do so, we have to read the front of all the seperatly sorted chunks and choose the smallest.
In order to find the smallest front-value easily, we employ a binary search tree which has log(m) insertion, removal, and smallest value look up time where m is the height of the tree, so we write the smallest values into this tree.
that means we insert into the tree n times and remove n times, which comes out to 2n*log(m)
Therefore, the disk based sorting algorithm has a runtime complexity of c*(k*log(k)) + 2n*log(m)
