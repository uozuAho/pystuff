from collections import deque

import algs.astar as astar
import utils.grid as grid


type Xy = tuple[int, int]


def is_open(pos: Xy, fav=1350):
    x, y = pos
    if x < 0 or y < 0:
        return False
    val = x * x + 3 * x + 2 * x * y + y + y * y
    val += fav
    return val.bit_count() % 2 == 0


assert is_open((0, 0), 10)
assert not is_open((1, 0), 10)


def solve(start: Xy, goal: Xy, fav: int):
    return astar.astar_search(
        start,
        lambda pos: grid.manhattan_dist(pos, goal),
        lambda pos: [xy for xy in grid.adjxy(pos) if is_open(xy, fav)],
    )


def numlocs(start: Xy, fav=1350, maxdepth=50):
    visited = {start}
    frontier = deque()
    frontier.appendleft((0, start))
    while frontier:
        d, current = frontier.popleft()
        if d > maxdepth:
            break
        visited.add(current)
        frontier.extend(
            (d + 1, adj)
            for adj in grid.adjxy(current)
            if not is_open(adj, fav) and adj not in visited
        )
    return len(visited)
