PYTHONPATH ?= $(pwd)

.PHONY: run build lint

run:
	@python -m app.cli.main

build:
	@nuitka --standalone \
		--onefile \
		--lto=yes \
		--clang \
		--include-data-dir=images=images \
		--include-data-dir=out=out \
		--include-package=builders \
		--include-package=models \
		--include-package=models.draw \
		--include-package=models.filters \
		--include-package=models.operations \
		--output-dir=dist \
		app/cli/main.py

lint:
	@pylint --ignore=.venv .
