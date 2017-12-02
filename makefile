TRAIN=0
TEST=0
install:
	python html_parser.py
	python corpus_generator.py
	python bayes.py $(TRAIN) $(TEST)
clean:
	rm tweets1;rm tweets2;rm classifier.pickle
	cd Source; rm -r *;mkdir 1;mkdir 2


