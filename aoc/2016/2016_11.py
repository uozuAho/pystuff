# took a bunch of ideas from norvig for this one:
# https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2016.ipynb
import itertools
import math
import time
from itertools import combinations, chain
from pprint import pprint

import algs.astar as astar

from utils.input import lines

docs = """
E = elevator. capacity = 2
    - cannot move when empty
    - stops on every floor. contents affect that floor
HG = hydrogen generator
HM = hydrogen microchip
LG = lithium generator
LM = lithium microchip

M chips can't be left with incompatible G without their compatible G
"""

test_pic = """
F4 .  .  .  .  .
F3 .  .  .  LG .
F2 .  HG .  .  .
F1 E  .  HM .  LM
"""

real_pic = """
F1 E POLG THUG THUM PROG RUTG RUTM COBG COBM
F2   POLM PROM
F3
F4
"""

goal = "min steps to bring all items to 4th floor"

VALID_LEVELS = frozenset(range(4))


type State = tuple[frozenset[str]]


def pic_to_state(input: str) -> State:
    floors = sorted(lines(input))
    return tuple(
        frozenset(
            x for x in floor.split() if not x.startswith("F") and x != " " and x != "."
        )
        for floor in floors
    )


def state_to_pic(state: State) -> str:
    floors = []
    for i, floor in enumerate(state):
        floors.append(f"F{i + 1} " + " ".join(sorted(floor)))
    return "\n".join(floors)


def is_valid_floor(floor: frozenset[str]) -> bool:
    if len(floor) <= 1:
        return True
    for m in floor:
        if m.endswith("M"):
            hasowngen = False
            hasothergen = False
            for g in floor:
                if g.endswith("G") and g.startswith(m[:-1]):
                    hasowngen = True
                if g.endswith("G") and not g.startswith(m[:-1]):
                    hasothergen = True
            if hasothergen and not hasowngen:
                return False
    return True


assert is_valid_floor([])
assert is_valid_floor(["E"])
assert is_valid_floor(["HM"])
assert is_valid_floor(["E", "ROCM"])
assert is_valid_floor(["E", "ROCG"])
assert is_valid_floor(["E", "ROCM", "ROCG"])
assert is_valid_floor(['HG', 'E', 'HM'])
assert not is_valid_floor(['LM', 'HG', 'E', 'HM'])
assert not is_valid_floor(['LM', 'HG', 'E'])
assert not is_valid_floor(["ROCM", "ASDG"])
assert not is_valid_floor(["E", "ROCM", "ASDG"])
assert not is_valid_floor({"POLM", "THUM", "POLG"})


def move(state: State, fromlevel: int, tolevel: int, items) -> State | None:
    assert abs(fromlevel - tolevel) == 1
    assert fromlevel in VALID_LEVELS
    assert tolevel in VALID_LEVELS
    assert "E" in state[fromlevel]
    itemset = {*items}
    assert itemset <= state[fromlevel]
    assert len(items) > 0
    newfrom: frozenset[str] = frozenset(state[fromlevel] - {"E"} - itemset)
    if not is_valid_floor(newfrom):
        return None
    newto: frozenset[str] = frozenset(state[tolevel] | {"E"} | itemset)
    if not is_valid_floor(newto):
        return None

    return (
        newfrom if fromlevel == 0 else newto if tolevel == 0 else state[0],
        newfrom if fromlevel == 1 else newto if tolevel == 1 else state[1],
        newfrom if fromlevel == 2 else newto if tolevel == 2 else state[2],
        newfrom if fromlevel == 3 else newto if tolevel == 3 else state[3],
    )


def gen_states(state: State):
    elevel, efloor = [(i, f) for i, f in enumerate(state) if "E" in f][0]
    adj_levels = {elevel + 1, elevel - 1} & VALID_LEVELS
    things = efloor - {"E"}
    for adj in adj_levels:
        for carry in chain(combinations(things, 1), combinations(things, 2)):
            newstate = move(state, elevel, adj, carry)
            if newstate:
                yield newstate


assert (
    len(list(gen_states([{"E", "POLG", "POLM", "THUG", "THUM"}, set(), set(), set()])))
    == 6
)


def est_moves(state: State):
    total = 0
    for i, f in enumerate(state):
        for _ in f:
            total += 3 - i
    return math.ceil(total / 2)


def render(state: State):
    floors = []
    for i, floor in enumerate(state):
        floors.append(f"F{i + 1} " + " ".join(sorted(floor)))
    return "\n".join(reversed(floors))


def solve(input: str):
    init = pic_to_state(input)
    path, stats = astar.astar_search(init, est_moves, gen_states)
    return len(path) - 1, stats

def test_solve():
    pathlen, _ = solve(test_pic)
    assert pathlen == 11


# solve(test_pic)
# solve(real_pic)   # 12 sec-ish

p2_pic = """
F1 E POLG THUG THUM PROG RUTG RUTM COBG COBM ELEG ELEM DILG DILM
F2   POLM PROM
F3
F4
"""

# takes ~15 min
# norvig mentions symmetry breaking to speed things up
# AOC says all probs have a solution that completes in ~15s on old hardware
# solve(p2_pic)


def pairs(floor: frozenset[str]):
    for k, g in itertools.groupby(sorted(floor), key=lambda f: f[:3]):
        gg = tuple(g)
        if len(gg) > 1:
            yield gg


assert list(pairs(["polg", "thum"])) == []
assert list(pairs(["polg", "polm"])) == [("polg", "polm")]
assert list(pairs({"POLM", "THUG", "THUM", "POLG"})) == [
    ("POLG", "POLM"),
    ("THUG", "THUM"),
]


def gen_states_sym(state: State):
    """Same as gen_states, but try to exclude symmetries"""
    elevel, efloor = [(i, f) for i, f in enumerate(state) if "E" in f][0]
    adj_levels = {elevel + 1, elevel - 1} & VALID_LEVELS
    things = efloor - {"E"}

    # if there's more than one pair of chip+gen on a floor, carry any
    # pair is equivalent, so only try one
    p = list(pairs(things))
    ignore_pairs = frozenset(frozenset(x) for x in p[1:])

    # carrying any 1 chip to an empty floor is equivalent
    efloorchips = [x for x in efloor if x.endswith("M")]
    ignore_chips = frozenset(efloorchips[1:])

    for adj in adj_levels:
        destfloor = state[adj]
        for carry in chain(combinations(things, 1), combinations(things, 2)):
            if frozenset(carry) in ignore_pairs:
                continue

            if len(destfloor) == 0 and ignore_chips:
                if len(carry) == 1 and carry[0] in ignore_chips:
                    continue

            newstate = move(state, elevel, adj, carry)
            if newstate:
                yield newstate


assert (
    len(list(gen_states([{"E", "POLG", "POLM", "THUG", "THUM"}, set(), set(), set()])))
    == 6
)
assert (
    len(
        list(
            gen_states_sym([{"E", "POLG", "POLM", "THUG", "THUM"}, set(), set(), set()])
        )
    )
    == 4
)


def solve_fast(input: str):
    init = pic_to_state(input)
    path, n, f = astar.astar_search(init, est_moves, gen_states_sym)
    print("pathlen: ", len(path), "num explored: ", n, "frontier: ", f)
    return len(path) - 1


def timeit(func):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    print("time: ", end - start)


# timeit(lambda: solve_fast(test_pic))
# timeit(lambda: solve(real_pic)) # 7.5sec
# timeit(lambda: solve_fast(real_pic)) # 8sec, doh!

# meh, exercise for later: make it fast. There's threads on reddit about this one.
