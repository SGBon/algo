PY=python
UFILE=unsorted.txt
SFILE=sorted.txt
GENERATED=$(UFILE) $(SFILE)

run: prepare $(SFILE)

$(SFILE):
	$(PY) disksort.py

prepare: $(UFILE)

$(UFILE):
	$(PY) genhunmil.py

clean:
	rm $(GENERATED)
