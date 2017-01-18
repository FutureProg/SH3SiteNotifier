init:	
	pip install -r requirements.txt

install:
	pip install -r requirements.txt

test:
	py.test tests

run:
	python3 app

.PHONY: init test