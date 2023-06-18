.PHONY: setup install_dependencies test_pipeline

setup:
    python -m venv .venv
    . .venv/bin/activate
    pip install --upgrade pip

install_dependencies:
    . .venv/bin/activate
    pip install -r requirements.txt

format:
	black *.py

test_pipeline:
    . .venv/bin/activate
    python pytest -m test_workflow.py


