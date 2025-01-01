PYTHONPATH ?= $(pwd)

.PHONY: run lint

run:
	@python -m app.cli.main

lint:
	@pylint --ignore=.venv .
