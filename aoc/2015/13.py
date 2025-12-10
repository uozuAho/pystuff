from collections import defaultdict
import itertools
import re
import sys
from aocd import get_data, submit

# much nicer: https://github.com/r-sreeram/adventofcode/blob/main/2015/2015-13.py

samp = """
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""


def solve1(input: str):
    ppl = defaultdict(dict)
    for line in input.splitlines():
        if not line.strip():
            continue
        m = re.match(
            r"(.+) would (.+) (\d+) happiness units by sitting next to (.+)\.", line
        )
        assert m
        x, gl, num, y = m.groups()
        # print(x, gl, num, y)
        sign = -1 if gl == "lose" else +1
        ppl[x][y] = sign * int(num)
    # print(ppl.keys())
    max_total = -99999999999999
    max_p = None
    for p in itertools.permutations(ppl.keys()):
        total = 0
        p_ext = [p[-1]] + list(p) + [p[0]]
        for i in range(1, len(p_ext) - 1):
            total += ppl[p_ext[i]][p_ext[i - 1]]
            total += ppl[p_ext[i]][p_ext[i + 1]]
        if total > max_total:
            max_total = total
            max_p = p
    return max_total


def solve2(input: str):
    ppl = defaultdict(dict)
    for line in input.splitlines():
        if not line.strip():
            continue
        m = re.match(
            r"(.+) would (.+) (\d+) happiness units by sitting next to (.+)\.", line
        )
        assert m
        x, gl, num, y = m.groups()
        # print(x, gl, num, y)
        sign = -1 if gl == "lose" else +1
        ppl[x][y] = sign * int(num)
    for k in ppl.keys():
        ppl[k]["wozza"] = 0
    ppl["wozza"] = {x: 0 for x in ppl.keys()}
    # print(ppl.keys())
    max_total = -99999999999999
    max_p = None
    for p in itertools.permutations(ppl.keys()):
        total = 0
        p_ext = [p[-1]] + list(p) + [p[0]]
        for i in range(1, len(p_ext) - 1):
            total += ppl[p_ext[i]][p_ext[i - 1]]
            total += ppl[p_ext[i]][p_ext[i + 1]]
        if total > max_total:
            max_total = total
            max_p = p
    return max_total


if __name__ == "__main__":
    year, day = 2015, 13
    real = get_data(year=year, day=day)

    if "print" in sys.argv:
        print(solve2(samp))
    elif "submit" in sys.argv:
        submit(solve2(real), year=year, day=day)
    else:
        solve2(samp)
