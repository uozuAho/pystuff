.PHONY: format lint test precommit bench run

format:
	uv run ruff format

lint:
	uv run ruff check

test:
	uv run pytest --benchmark-skip

precommit: format lint test

bench:
	uv run pytest --benchmark-only --benchmark-sort Name

run:
	uv run main.py

clean:
	rm -rf .benchmarks .pytest_cache .ruff_cache .venv
