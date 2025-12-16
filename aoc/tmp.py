import itertools
from collections import deque

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

real = """
The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
The third floor contains nothing relevant.
The fourth floor contains nothing relevant.
"""

# my translation of real to picture format
real_pic = """
F1 E POLG THUG THUM PROG RUTG RUTM COBG COBM
F2   POLM PROM
F3
F4
"""

goal = "min steps to bring all items to 4th floor"
# idea: parallel BFS all possible moves

def pic_to_state(input: str):
    floors = sorted(lines(input))
    return [[x for x in floor.split()
            if not x.startswith("F") and x != ' ' and x != '.']
            for floor in floors]

# pic_to_state(test_pic)
# pic_to_state(real_pic)

# up to here, 22min

# list of floors in increasing order, each floor lists contents
type State = list[list[str]]


def gen_all_states(state: State):
    elevel, econtents = [(i, f[1:]) for i, f in enumerate(state) if "E" in f][0]
    nextlevels = list(filter(lambda x: 0 <= x <= 3, [elevel - 1, elevel + 1]))
    for nextlevel in nextlevels:
        for c in econtents:
            nextstate = [s[:] for s in state]
            nextstate[elevel].pop(0) # elevator
            nextstate[elevel].remove(c)
            nextstate[nextlevel].insert(0, "E")
            nextstate[nextlevel].append(c)
            yield nextstate
        for cc in itertools.combinations(econtents, 2):
            nextstate = [s[:] for s in state]
            nextstate[elevel].pop(0)  # elevator
            nextstate[elevel].remove(cc[0])
            nextstate[elevel].remove(cc[1])
            nextstate[nextlevel].insert(0, "E")
            nextstate[nextlevel].append(cc[0])
            nextstate[nextlevel].append(cc[1])
            yield nextstate


def is_valid_f(floor: list[str]) -> bool:
    chips = [x[:-1] for x in floor if x.endswith('M')]
    gens = [x[:-1] for x in floor if x.endswith('G')]
    for chip in chips:
        if gens and chip not in gens:
            return False
    return True


def is_valid(state: State):
    return all(is_valid_f(f) for f in state)


assert is_valid(pic_to_state(test_pic))
assert is_valid([['E', 'HM', 'LM'], ['HG'], ['LG'], []])
assert is_valid([['LM'], ['E', 'HG', 'HM'], ['LG'], []])


def next_valid_states(state: State):
    return [x for x in gen_all_states(state) if is_valid(x)]

# still going, 43m total

def is_goal(state: State):
    return not any(state[:-1])


assert not is_goal([['E', 'HM', 'LM'], ['HG'], ['LG'], []])
assert is_goal([[], [], [], ['E', "blah"]])


def solve(state: State):
    q = deque([(state, 0)])
    while True:
        s, depth = q.popleft()
        # print(s, depth)
        if is_goal(s):
            return depth
        q.extend((x, depth + 1) for x in next_valid_states(s))


# print(solve(pic_to_state(test_pic)))
print(solve(pic_to_state(real_pic)))
