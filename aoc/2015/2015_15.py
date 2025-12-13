import re

# ew i hate my solution. Still i solved it in ok time (30 min). Couldn't find
# any others' solutions that i liked.

samp = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


def solve2(input: str):
    ing = {}
    for line in input.splitlines():
        if not line.strip():
            continue
        m = re.match(
            r"(.+): capacity (-*\d+), durability (-*\d+), flavor (-*\d+), texture (-*\d+), calories (-*\d+)",
            line,
        )
        if not m:
            raise NameError(line)
        n, a, b, c, d, cal = m.groups()
        ing[n] = [int(x) for x in (a, b, c, d, cal)]
    assert len(ing) == 4
    best = 0
    for i in range(101):
        for j in range(101):
            for k in range(101):
                if i + j + k > 100:
                    continue
                ll = 100 - i - j - k
                cals = [x[4] for x in ing.values()]
                calsum = sum(x * y for x, y in zip([i, j, k, ll], cals))
                if calsum != 500:
                    continue
                myings = [x[:4] for x in ing.values()]
                scores = [
                    max(0, i * x + j * y + k * z + ll * zz)
                    for (x, y, z, zz) in zip(*myings)
                ]
                score = 1
                for x in scores:
                    score = score * x
                if score > best:
                    best = score
    return best


# if __name__ == "__main__":
#     year, day = 2015, 12
#     real = get_data(year=year, day=day)

#     if "print" in sys.argv:
#         print(solve2(samp))
#     elif "submit" in sys.argv:
#         submit(solve2(real), year=year, day=day)
#     else:
#         solve2(samp)
