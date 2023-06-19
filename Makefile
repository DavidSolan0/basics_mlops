install_dependencies:
	pip install --upgrade pip && \
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint src

test_pipeline:
	python -m pytest -vv test_workflow.py

all: install_dependencies lint test_pipeline
