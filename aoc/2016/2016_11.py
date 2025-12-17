# took a bunch of ideas from norvig for this one:
# https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2016.ipynb

import math
from itertools import combinations, chain
import utils.astar as astar

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


def move(state: State, fromlevel: int, tolevel: int, items) -> State:
    assert abs(fromlevel - tolevel) == 1
    assert fromlevel in VALID_LEVELS
    assert tolevel in VALID_LEVELS
    assert "E" in state[fromlevel]
    itemset = {*items}
    assert itemset <= state[fromlevel]
    assert len(items) > 0
    newfrom: frozenset[str] = frozenset(state[fromlevel] - {"E"} - itemset)
    newto: frozenset[str] = frozenset(state[tolevel] | {"E"} | itemset)
    return tuple(
        newfrom if i == fromlevel else newto if i == tolevel else floor
        for i, floor in enumerate(state)
    )


def is_valid_floor(floor: set[str]) -> bool:
    chips = [x[:-1] for x in floor if x != "E" and x.endswith("M")]
    gens = [x[:-1] for x in floor if x != "E" and x.endswith("G")]
    for chip in chips:
        if gens and chip not in gens:
            return False
    return True


def is_valid_state(state: State) -> bool:
    return all(is_valid_floor(f) for f in state)


def gen_states(state: State):
    elevel, efloor = [(i, f) for i, f in enumerate(state) if "E" in f][0]
    adj_levels = {elevel + 1, elevel - 1} & VALID_LEVELS
    things = efloor - {"E"}
    for adj in adj_levels:
        for carry in chain(combinations(things, 1), combinations(things, 2)):
            newstate = move(state, elevel, adj, carry)
            if is_valid_state(newstate):
                yield newstate


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
    path = astar.astar_search(init, est_moves, gen_states)
    # for x in path:
    #     print('------')
    #     print(render(x))
    return len(path) - 1


# solve(test_pic)
# solve(real_pic)

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
