from collections import Counter
import utils.grid as g
from pipe import map
from utils.input import lines, transpose

test = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""


# same but way more elegant: https://github.com/iKevinY/advent/blob/main/2016/day06.py


def solve(input: str):
    grid = g.parse_chargrid(input)
    c = [Counter(col) for col in g.cols(grid)]
    letters = [x.most_common(1) for x in c]
    return "".join(x[0][0] for x in letters)


def solve2(input: str):
    grid = g.parse_chargrid(input)
    c = [Counter(col) for col in g.cols(grid)]
    letters = [x.most_common()[-1] for x in c]
    return "".join(x[0][0] for x in letters)


def pipesolve1(input):
    # fmt: off
    return "".join(
        transpose(lines(input))
        | map(Counter)
        | map(lambda x: x.most_common()[0][0])
    )
    # fmt: on


def pipesolve2(input):
    # fmt: off
    return "".join(
        transpose(lines(input))
        | map(Counter)
        | map(lambda x: x.most_common()[-1][0])
    )
    # fmt: on


def test_sols():
    assert solve(test) == "easter"
    assert solve2(test) == "advent"
    assert pipesolve1(test) == "easter"
    assert pipesolve2(test) == "advent"
