""" 2d grid of characters """

type Grid = list[list[str]]
type PosXy = tuple[int, int]

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
