from collections import Counter
from utils import grid as g
from utils.basic import count
from utils.input import lines

# norvig's is so much cleaner: https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2016.ipynb


test = """
.......
.......
.......
"""


def rect(grid: g.Grid, x, y):
    new = g.copy(grid)
    for r in range(0, y):
        for c in range(0, x):
            new[r][c] = "#"
    return new


assert (
    g.tostr(rect(g.chargrid(test), 3, 2))
    == """###....
###....
......."""
)

def rot(seq: list[str], num: int):
    w = len(seq)
    return [seq[(i - num + w) % w] for i in range(w)]
    # much better: return seq[-num:] + seq[:-num]


assert rot(['#','.','.'], 0) == ['#','.','.']
assert rot(['#','.','.'], 1) == ['.','#','.']
assert rot(['#','.','.'], 2) == ['.','.','#']
assert rot(['#','.','.'], 3) == ['#','.','.']
assert rot(['#','.','.'], 4) == ['.','#','.']


def rotr(grid: g.Grid, y, b):
    return grid[:y] + [rot(grid[y], b)] + grid[y + 1:]


temp = rect(g.chargrid(test), 2, 2)
assert g.tostr(rotr(temp, 0, 1)) == """.##....
##.....
......."""


def rotc(grid: g.Grid, x, b):
    cols = g.cols(grid)
    newcols = cols[:x] + [rot(cols[x], b)] + cols[x + 1:]
    return g.transpose(newcols)

assert g.tostr(rotc(temp, 0, 1)) == """.#.....
##.....
#......"""


def parsecmd(cmd: str):
    if cmd.startswith('rect'):
        x, y = [int(x) for x in cmd.split()[1].split('x')]
        return lambda grid: rect(grid, x, y)
    if 'x=' in cmd:
        x, num = [int(x) for x in cmd.split('=')[1].split('by')]
        return lambda grid: rotc(grid, x, num)
    if 'y=' in cmd:
        y, num = [int(x) for x in cmd.split('=')[1].split('by')]
        return lambda grid: rotr(grid, y, num)
    raise KeyError("ohno: " + cmd)


def test_cmds():
    screen = g.chargrid("""
    .......
    .......
    .......
    """)
    screen = parsecmd("rect 1x1")(screen)
    screen = parsecmd("rotate row y=0 by 1")(screen)
    screen = parsecmd("rotate column x=1 by 1")(screen)
    assert g.tostr(screen) == """.......
.#.....
......."""


def solve(input):
    screen = [['.'] * 50 for _ in range(6)]
    for line in lines(input):
        cmd = parsecmd(line)
        screen = cmd(screen)
    c = Counter(c for row in screen for c in row)
    print(g.tostr(screen).replace('.', ' '))
    return c['#']
