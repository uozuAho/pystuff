import hashlib

year, day = 2015, 4

sample = ""

# raw = get_data(year=year, day=day)


def solve(input: str):
    for i in range(9999999999999):
        b = (input + str(i)).encode("utf-8")
        r = hashlib.md5(b)
        if str(r.hexdigest()).startswith("00000"):
            return i


def solve2(input: str):
    for i in range(9999999999999):
        b = (input + str(i)).encode("utf-8")
        r = hashlib.md5(b)
        if str(r.hexdigest()).startswith("000000"):
            return i


# submit(solve(raw), year=year, day=day)
