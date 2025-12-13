import pytest
import utils.grid as g


def go(input: str, start=None) -> g.PosXy:
    if start is None:
        start = (0, 0)
    num = 0
    pos = start
    facing = g.NORTH
    visited = set([pos])
    for x in input.split(","):
        if "L" in x:
            num = int(x.replace("L", ""))
            facing = g.turnleft(facing)
        elif "R" in x:
            num = int(x.replace("R", ""))
            facing = g.turnright(facing)
        else:
            raise KeyError("asdfasdf")
        revisited = False
        for _ in range(num):
            pos = g.add(pos, facing, 1)
            if pos in visited:
                revisited = True
                break
            else:
                visited.add(pos)
        if revisited:
            break
    return pos


# fmt: off
@pytest.mark.parametrize(
    "directions, dist", [
        ("R2, L3", 5),
        ("R2, R2, R2", 2),
        ("R5, L5, R5, R3", 12)
    ]
)
# fmt: on
def test_go(directions: str, dist: int):
    assert dist == g.manhattan_dist(go(directions))
