# this one's much better: https://github.com/r-sreeram/adventofcode/blob/main/2015/2015-6.py

import sys
from aocd import get_data, submit
import numpy as np

year, day = 2015, 6

raw = get_data(year=year, day=day)


def coords(line: str):
    spl = line.split(",")
    c1 = int(spl[0].split()[-1]), int(spl[1].split()[0])
    c2 = int(spl[1].split()[-1]), int(spl[2])
    return c1, c2


def solve1(input: str, size=((1000, 1000))):
    ll = np.zeros(size, dtype=bool)
    for line in input.splitlines():
        if len(line.split(",")) == 3:
            c1, c2 = coords(line)
            if line.startswith("turn on"):
                ll[c1[0] : c2[0] + 1, c1[1] : c2[1] + 1] = True
            elif line.startswith("turn off"):
                ll[c1[0] : c2[0] + 1, c1[1] : c2[1] + 1] = False
            elif line.startswith("toggle"):
                ll[c1[0] : c2[0] + 1, c1[1] : c2[1] + 1] = ~ll[
                    c1[0] : c2[0] + 1, c1[1] : c2[1] + 1
                ]
    # return ll
    return ll.sum(where=True)


def solve2(input: str, size=((1000, 1000))):
    ll = np.zeros(size, dtype=int)
    for line in input.splitlines():
        if len(line.split(",")) == 3:
            c1, c2 = coords(line)
            if line.startswith("turn on"):
                ll[c1[0] : c2[0] + 1, c1[1] : c2[1] + 1] += 1
            elif line.startswith("turn off"):
                ll[c1[0] : c2[0] + 1, c1[1] : c2[1] + 1] -= 1
                ll = ll.clip(0, 99999999999999999)
            elif line.startswith("toggle"):
                ll[c1[0] : c2[0] + 1, c1[1] : c2[1] + 1] += 2
    # return ll
    return ll.sum()


if "print" in sys.argv:
    print(solve2(raw, (5, 5)))

elif "submit" in sys.argv:
    submit(solve2(raw), year=year, day=day)

else:
    solve2(raw)
    # breakpoint here to run/debug interactively
    # This is better in vscode than IDLE or python -i
    print("yo")
