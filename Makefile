VIRTUALENV := python3 -m venv

## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## venv - Install the virtual environment
venv:
	$(VIRTUALENV) ~/.venv/python_project/
	ln -snf ~/.venv/python_project/ venv
	venv/bin/pip install -e ."[dev]"

## install - Install the project locally
install: | venv

## clean - Remove the virtual environment and clear out .pyc files
clean:
	rm -rf ~/.venv/python_project/ venv
	find . -name '*.pyc' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

## lint - Lint the project
lint:
	venv/bin/flake8 python_project/*.py
	venv/bin/flake8 test/unit/*.py

## test - Test the project
test:
	venv/bin/pytest

## coverage - Test the project and generate an HTML coverage report
coverage:
	venv/bin/pytest --cov=python_project --cov-branch --cov-report=html --cov-report=term-missing

.PHONY: help install clean lint test coverage
