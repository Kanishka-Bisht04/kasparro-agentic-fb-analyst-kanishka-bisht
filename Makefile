run:
	python src/run.py "Analyze ROAS drop"

test:
	pytest tests/

lint:
	flake8 src