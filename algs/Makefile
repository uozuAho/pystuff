.PHONY: format lint test precommit bench run

format:
	uv run ruff format

lint:
	uv run ruff check

test:
	uv run pytest --benchmark-skip

precommit: format lint test

pc: precommit

bench:
	uv run pytest --benchmark-only --benchmark-sort Name

run:
	uv run main.py
