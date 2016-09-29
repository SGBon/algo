BF=big.txt
SF=small.txt
WF=wide.txt
MS=make-strings.py
SS=sort-strings.py
OUTS=$(BF) $(SF) $(WF)
BIGFLAGS=100000 100 $(BF)
SMALLFLAGS=100 10 $(SF)
WIDEFLAGS=1000 10000 $(WF)

.PHONY: big wide clean

all: big wide small

big: $(BF) $(SS)
	python $(SS) $(BF)

small: $(SF) $(SS)
	python $(SS) $(SF)

wide: $(WF) $(SS)
	python $(SS) $(WF)

$(BF): $(MS)
	python $(MS) $(BIGFLAGS)

$(WF): $(MS)
	python $(MS) $(WIDEFLAGS)

$(SF): $(MS)
	python $(MS) $(SMALLFLAGS)

clean:
	rm -f $(OUTS)
