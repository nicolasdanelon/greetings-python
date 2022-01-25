tests:
	export PYTHONPATH=src/ && python3 -m pytest

venv:
	python3 -m venv .

install:
	pip install -r requirements.txt

