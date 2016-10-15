PY=python
UFILE=unsorted.txt
SFILE=sorted.txt
GENNER=genhunmil.py
SORTER=disksort.py
GENERATED=$(UFILE) $(SFILE)

run: prepare $(SFILE)

$(SFILE): $(SORTER) $(UFILE)
	time -p $(PY) $(SORTER)

prepare: $(UFILE)

$(UFILE): $(GENNER)
	$(PY) $(GENNER)

clean:
	rm $(GENERATED)
