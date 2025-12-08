""" 2d grid of characters """

type Grid = list[list[str]]
type PosXy = tuple[int, int]
type Dir = complex

UP = NORTH = 0 + 1j
RIGHT = EAST = 1 + 0j
DOWN = SOUTH = 0 - 1j
LEFT = WEST = -1 + 0j
ORIGIN = (0, 0)

def togrid(input: str) -> Grid:
    grid = []
    for line in input.splitlines():
        if not line.strip(): continue
        grid.append([c for c in line.strip()])
    return grid

def height(grid: Grid):
    return len(grid)

def width(grid: Grid):
    return len(grid[0])

def sizeHw(grid: Grid) -> tuple[int, int]:
    return height(grid), width(grid)

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
