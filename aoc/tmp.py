from pipe import tee
from utils.input import lines
from utils.pipe import ignore

test = """
abc
def
"""

real = """
"""

list(
lines(test)
| tee
) # type: ignore


def solve(input: str):
    return ""


def test_sols():
    assert solve(test) == ""
