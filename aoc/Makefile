# print answer to console
p:
	uv run python tmp.py print

# as above, use pypy
pp:
	uv run --python pypy-3.11 tmp.py print

# submit
s:
	uv run python tmp.py submit

# interactive. Not as good as debugger, but faster to start
i:
	uv run python -i tmp.py

# unit tests
t:
	uv run pytest --benchmark-skip

test: t

# benchmarks
b:
	uv run pytest --benchmark-only

# benchmarks, use pypy
bb:
	uv run --python pypy-3.11 pytest --benchmark-only

format:
	uv run ruff format

lint:
	uv run ruff check

lintfix:
	uv run ruff check --fix

precommit: format lint test

clean:
	rm -rf __pycache__ .benchmarks .pytest_cache .ruff_cache .venv
