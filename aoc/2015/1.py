from aocd import get_data, submit

year, day = 2015, 1

sample = "(())"

raw = get_data(year=year, day=day)


def solve1(str):
    f = 0
    for x in str:
        if x == "(":
            f += 1
        elif x == ")":
            f -= 1
    return f


def solve2(str):
    f = 0
    pos = -1
    for i, x in enumerate(str):
        if x == "(":
            f += 1
        elif x == ")":
            f -= 1
        if pos == -1 and f == -1:
            pos = i + 1
    return pos


print(solve1(raw))
# submit works out what part to submit
# submit(solve1(raw), year=year, day=day)
# submit(solve2(raw), year=year, day=day)
