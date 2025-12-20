import re

from utils.basic import first
from utils.input import lines

test = """
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
"""


def parseline(line: str):
    n, pos = re.findall(r"(\d+) positions.*position (\d+)", line)[0]
    return int(n), int(pos)


def discpos(discs, tstart=0):
    for i, disc in enumerate(discs):
        yield (disc[1] + i + tstart + 1) % disc[0]


def solve(input):
    discs = list(map(parseline, lines(input)))
    return first(i for i in range(8888888888) if all(x == 0 for x in discpos(discs, i)))


assert solve(test) == 5
