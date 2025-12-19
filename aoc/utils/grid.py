"""2d grid of anything."""

import typing as t

type Grid = list[list]
type PosXy = tuple[int, int]
type Dir = complex

UP = NORTH = 0 + 1j
RIGHT = EAST = 1 + 0j
DOWN = SOUTH = 0 - 1j
LEFT = WEST = -1 + 0j
ORIGIN = (0, 0)


def parsegrid(input: str, to_row: t.Callable[[str], list], invert_y=False):
    """
    :param input: the whole input
    :param to_row: convert one line to a row
    :param invert_y: if True, y = 0 is the bottom row, else it's the top
    """
    grid = []
    for line in input.splitlines():
        if not line.strip():
            continue
        grid.append(to_row(line))
    if invert_y:
        return list(reversed(grid))
    return grid


def copy(grid: Grid):
    return [row[:] for row in grid]


def tostr(grid: Grid):
    return "\n".join("".join(row) for row in grid)


def render(grid: Grid):
    return tostr(grid)


def chargrid(input: str):
    return parsegrid(input, lambda line: [c for c in line.strip()])


def parse_intgrid(input: str):
    return parsegrid(input, lambda line: [int(c) for c in line.split()])


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


def adjxy(pos: PosXy, diag=False):
    if diag:
        raise NotImplementedError()
    x, y = pos
    return (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)


def adj(grid: Grid, pos: PosXy):
    """Adjacent cell values, in row-major order. No wrap."""
    x, y = pos
    h, w = sizeHw(grid)
    for yy in range(max(0, y - 1), min(h, y + 2)):
        for xx in range(max(0, x - 1), min(w, x + 2)):
            if (x, y) == (xx, yy):
                continue
            yield grid[yy][xx]


def turnleft(facing: Dir):
    return facing * 1j


def turnright(facing: Dir):
    return facing * -1j


def add(pos: PosXy, dir: Dir, num: int) -> PosXy:
    x = pos[0] + int(dir.real) * num
    y = pos[1] + int(dir.imag) * num
    return (x, y)


def manhattan_dist(p1: PosXy, p2: PosXy = ORIGIN):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
