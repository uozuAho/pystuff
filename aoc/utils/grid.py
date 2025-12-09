""" 2d grid of anything.
    Maybe this should replace chargrid?

    Origin = (0, 0), bottom left.
    +y is up
"""

type Grid = list[list]
type PosXy = tuple[int, int]
type Dir = complex

UP = NORTH = 0 + 1j
RIGHT = EAST = 1 + 0j
DOWN = SOUTH = 0 - 1j
LEFT = WEST = -1 + 0j
ORIGIN = (0, 0)


def el(grid: Grid, pos: PosXy):
    return grid[pos[1]][pos[0]]

def height(grid: Grid):
    return len(grid)

def width(grid: Grid):
    return len(grid[0])

def sizeHw(grid: Grid) -> tuple[int, int]:
    return height(grid), width(grid)

def transpose(grid: Grid) -> Grid:
    return list(list(x) for x in zip(*grid))

def cols(grid: Grid) -> Grid:
    return transpose(grid)

def adj(grid: Grid, pos: PosXy):
    """ Adjacent cell values, in row-major order. No wrap. """
    x, y = pos
    h, w = sizeHw(grid)
    for yy in range(max(0, y - 1), min(h, y + 2)):
        for xx in range(max(0, x - 1), min(w, x + 2)):
            if (x, y) == (xx, yy): continue
            yield grid[yy][xx]

def turnleft(facing: Dir): return facing * 1j

def turnright(facing: Dir): return facing * -1j

def add(pos: PosXy, dir: Dir, num: int) -> PosXy:
    x = pos[0] + int(dir.real) * num
    y = pos[1] + int(dir.imag) * num
    return (x, y)

def manhattan_dist(p1: PosXy, p2: PosXy = ORIGIN):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
