from collections import defaultdict
import itertools

year, day = 2015, 9

# real = get_data(year=year, day=day)

# samp = real
samp = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""


def solve(input: str):
    v = set([])
    e = defaultdict(dict)
    for line in input.splitlines():
        if not line.strip():
            continue
        x, _, y, _, d = line.split()
        v.add(x)
        v.add(y)
        e[x][y] = int(d)
        e[y][x] = int(d)
    maxdist = 0
    for path in itertools.permutations(v):
        dist = 0
        for i in range(1, len(path)):
            x0 = path[i - 1]
            x1 = path[i]
            dist += e[x0][x1]
        if dist > maxdist:
            maxdist = dist
    return maxdist


# if "print" in sys.argv:
#     print(solve(samp))

# elif "submit" in sys.argv:
#     submit(solve(real), year=year, day=day)

# else:
#     solve(samp)
#     # breakpoint here to run/debug interactively
#     # This is better in vscode than IDLE or python -i
#     print("yo")
