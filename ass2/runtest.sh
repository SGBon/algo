#!/bin/sh
FUNCS=("f1" "f2" "f3" "f4")
NS=(100000 1000000)
MS=(100 1000)
for f in ${FUNCS[@]};
do
  for n in ${NS[@]};
  do
    for m in ${MS[@]};
    do
      echo $n $m $f
      python test-has.py $n $m $f $f$n$m.png
    done
  done
done
