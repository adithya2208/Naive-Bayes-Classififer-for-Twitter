TRAIN=0
TEST=0
init_dirs:
	mkdir Source
	cd Source;mkdir 1;mkdir 2
install:
	python html_parser.py
	python corpus_generator.py
	python bayes.py $(TRAIN) $(TEST)
clean:
	rm Source -r
	rm tweets1
	rm tweets2
	rm classifier.pickle
	


