import itertools

samp = """20
15
10
5
5"""


# 10m
def solve(input: str):
    nums = [int(x) for x in input.splitlines()]
    combos = []
    ccount = 0
    minlen = 99999
    for i in range(1, len(nums) + 1):
        for c in itertools.combinations(nums, i):
            if sum(c) == 150:
                combos.append(c)
                ccount += 1
                if len(c) > 0 and len(c) < minlen:
                    minlen = len(c)
    return sum(1 if len(x) == minlen else 0 for x in combos)


# if __name__ == "__main__":
#     year, day = 2015, 17
#     real = get_data(year=year, day=day)

#     if "print" in sys.argv:
#         print(solve(samp))
#     elif "submit" in sys.argv:
#         submit(solve(real), year=year, day=day)
#     else:
#         solve(samp)
