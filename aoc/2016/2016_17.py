from utils.hash import md5
from algs.astar import astar_search
import utils.grid as grid


def isopen(path: str, passcode: str):
    return tuple(x in "bcdef" for x in md5(passcode + path)[:4])


def nexts(pos, path: str, passcode: str, gridsize=4):
    u, d, left, r = isopen(path, passcode)
    n = []
    if pos[1] > 0 and u:
        n.append((grid.up(pos), path + "U"))
    if pos[1] < (gridsize - 1) and d:
        n.append((grid.down(pos), path + "D"))
    if pos[0] > 0 and left:
        n.append((grid.left(pos), path + "L"))
    if pos[0] < (gridsize - 1) and r:
        n.append((grid.right(pos), path + "R"))
    return n


assert nexts((0, 0), "", "hijkl") == [((0, 1), "D")]
assert nexts((0, 1), "D", "hijkl") == [((0, 0), "DU"), ((1, 1), "DR")]
assert nexts((1, 1), "DR", "hijkl") == []
assert nexts((0, 0), "DU", "hijkl") == [((1, 0), "DUR")]
assert nexts((1, 0), "DUR", "hijkl") == []


def solve(passcode: str, gridsize=4):
    start = ((0, 0), "")

    def h(state):
        pos, path = state
        return grid.manhattan_dist(pos, (3, 3))

    def g(state):
        pos, path = state
        return nexts(pos, path, passcode, gridsize)

    return astar_search(start, h, g)


p, stats = solve("yjjvjgan")
assert p[-1][1] == "RLDRUDRDDR"


def solve2(passcode: str, gridsize=4):
    front = [((0, 0), "")]
    longest = 0

    while front:
        pos, path = front.pop()
        if pos == (3, 3):
            longest = max(longest, len(path))
        else:
            front.extend(nexts(pos, path, passcode, gridsize))

    return longest


assert solve2("ihgpwlah") == 370
