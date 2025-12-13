samp = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""

type Lights = list[list[bool]]
type Pos = tuple[int, int]


def parse(input: str) -> Lights:
    lights = []
    for line in input.splitlines():
        if not line.strip():
            continue
        row = [True if c == "#" else False for c in line]
        lights.append(row)
    return lights


def height(lights: Lights):
    return len(lights)


def width(lights: Lights):
    return len(lights[0])


def adj(lights: Lights, pos: Pos):
    x, y = pos
    for yy in range(max(0, y - 1), min(height(lights), y + 2)):
        for xx in range(max(0, x - 1), min(width(lights), x + 2)):
            if (x, y) == (xx, yy):
                continue
            yield lights[yy][xx]


def next(lights: Lights):
    h = height(lights)
    w = width(lights)
    nl = [[False] * w for _ in range(h)]

    for y in range(0, h):
        for x in range(0, w):
            num_on = sum(1 if c else 0 for c in adj(lights, (x, y)))
            if num_on == 3:
                nl[y][x] = True
            elif num_on == 2 and lights[y][x]:
                nl[y][x] = True

    return nl


def next2(lights: Lights):
    nl = next(lights)
    h = height(lights)
    w = width(lights)
    nl[0][0] = True
    nl[0][w - 1] = True
    nl[h - 1][0] = True
    nl[h - 1][w - 1] = True
    return nl


def render(lights: Lights):
    out = ""
    for row in lights:
        out += "".join("#" if c else "." for c in row) + "\n"
    return out


def solve(input: str):
    lights = parse(input)
    for _ in range(100):
        lights = next(lights)  # part 1
        # lights = next2(lights)  # part 2
    return sum(1 if c else 0 for row in lights for c in row)


# if __name__ == "__main__":
#     year, day = 2015, 12
#     real = get_data(year=year, day=day)

#     if "print" in sys.argv:
#         print(solve(samp))
#     elif "submit" in sys.argv:
#         submit(solve(real), year=year, day=day)
#     else:
#         solve(samp)
