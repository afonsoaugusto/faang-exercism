MAKEFLAGS  	+= --silent
SHELL      	 = /bin/bash


elixir:
	@echo "Run tests in ELIXIR..."
	cd exercism/0/elixir && \
	mix test

go:
	@echo "Run tests in GO..."
	cd exercism/0/go && \
	go test -v ./...

python:
	@echo "Run tests in PYTHON..."
	python3.9 -m venv venv && \
	source venv/bin/activate && \
	pip install --upgrade pip && \
	pip install coverage && \
	coverage run -m unittest discover -s ./exercism/0/python -p 'test_*.py'  && \
	coverage report

commit:
	@echo "Run commit"
	git add .
	git commit -m "add files"
	git push