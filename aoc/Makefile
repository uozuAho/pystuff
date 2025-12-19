# print answer to console
p:
	uv run python tmp.py print

# as above, use pypy. Note you'll need to change
# python version in project.toml and only use python
# features supporte by pypy
pp:
	uv run --python pypy-3.11 tmp.py

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

pc: precommit

clean:
	rm -rf __pycache__ .benchmarks .pytest_cache .ruff_cache .venv

prof:
	uv run python -m profiling.sampling tmp.py

proflame:
	uv run python -m profiling.sampling --flamegraph tmp.py
