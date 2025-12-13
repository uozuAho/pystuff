year, day = 2015, 3

sample = ""

# raw = get_data(year=year, day=day)


def solve1(str: str):
    x, y = 0, 0
    vs = set([(x, y)])
    for c in str:
        if c == "^":
            y += 1
        elif c == ">":
            x += 1
        elif c == "v":
            y -= 1
        elif c == "<":
            x -= 1
        vs.add((x, y))
    return len(vs)


def solve2(str: str):
    x, y = 0, 0
    xr, yr = 0, 0
    who = 0
    vs = set([(x, y)])
    for c in str:
        if who == 0:
            if c == "^":
                y += 1
            elif c == ">":
                x += 1
            elif c == "v":
                y -= 1
            elif c == "<":
                x -= 1
            vs.add((x, y))
        else:
            if c == "^":
                yr += 1
            elif c == ">":
                xr += 1
            elif c == "v":
                yr -= 1
            elif c == "<":
                xr -= 1
            vs.add((xr, yr))
        who = 1 - who
    return len(vs)


# submit works out what part to submit
# submit(solve2(raw), year=year, day=day)
