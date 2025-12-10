from aocd import get_data, submit

year, day = 2015, 2

sample = "(())"

raw = get_data(year=year, day=day)


def solve1(str: str):
    a = 0
    for line in str.splitlines():
        ll, w, h = [int(x) for x in line.split("x")]
        a += 2 * ll * w + 2 * w * h + 2 * h * ll
        a += min(ll * w, w * h, h * ll)
    return a


def solve2(str: str):
    ribbon = 0
    for line in str.splitlines():
        dims = [int(x) for x in line.split("x")]
        dims.sort()
        a, b = dims[:2]
        ribbon += 2 * a + 2 * b
        ribbon += dims[0] * dims[1] * dims[2]
    return ribbon


# submit works out what part to submit
# submit(solve1(raw), year=year, day=day)
submit(solve2(raw), year=year, day=day)
