from dataclasses import dataclass
from aocd import get_data, submit

year, day = 2015, 5

real = get_data(year=year, day=day)

# samp = real
samp = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

@dataclass
class Map:
    h: int
    w: int
    obs: set[tuple[int, int]]

    def is_in_bounds(self, x , y):
        return 0 <= x < self.w and 0 <= y < self.h

    def is_obs(self, x, y):
        return (x, y) in self.obs

@dataclass
class Guard:
    x: int
    y: int
    c: str

    def copy(self):
        return Guard(self.x, self.y, self.c)

    def go_next(self, map: Map):
        x, y = infront(self)
        if map.is_obs(x, y):
            self.c = turn_right(self.c)
        else:
            self.x = x
            self.y = y

def parse(input: str) -> tuple[Map, Guard]:
    w = 0
    obs = set([])
    row = 0
    guard = None
    for line in input.splitlines():
        if not line.strip():
            continue
        w = len(line)
        for i, c in enumerate(line):
            if c == '#':
                obs.add((i, row))
            if c == '^':
                guard = Guard(i, row, c)
        row +=1
    m = Map(row, w, obs)
    if not guard:
        raise KeyError("no guard")
    return m, guard

def infront(guard: Guard) -> tuple[int, int]:
    match guard.c:
        case '^': return guard.x, guard.y - 1
        case '>': return guard.x + 1, guard.y
        case 'v': return guard.x, guard.y + 1
        case '<': return guard.x - 1, guard.y
        case _: raise KeyError("bad guard char")

def turn_right(c: str) -> str:
    match c:
        case '^': return '>'
        case '>': return 'v'
        case 'v': return '<'
        case '<': return '^'
        case _: raise KeyError("bad guard char")

def solve1(input: str):
    map, guard = parse(input)
    visited = set([])
    while map.is_in_bounds(guard.x, guard.y):
        visited.add((guard.x, guard.y))
        guard.go_next(map)
    return len(visited)

def has_loop(map, guard: Guard):
    visited = set([])
    tmp_guard = guard.copy()
    while map.is_in_bounds(tmp_guard.x, tmp_guard.y):
        gstate = (tmp_guard.x, tmp_guard.y, tmp_guard.c)
        if gstate in visited:
            return True
        visited.add(gstate)
        tmp_guard.go_next(map)
    return False

def solve2(input: str):
    map, guard = parse(input)
    loopers = 0
    for y in range(map.h):
        for x in range(map.w):
            if not map.is_obs(x, y):
                map.obs.add((x, y))
                if has_loop(map, guard):
                    loopers += 1
                map.obs.remove((x, y))
    return loopers
