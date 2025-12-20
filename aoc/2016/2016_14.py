import re
from functools import lru_cache

import utils.hash as hash


@lru_cache(maxsize=1010)
def myhash(s: str, repeat: int = 1):
    for _ in range(repeat):
        s = hash.md5(s)
    return s


def findkeys2(salt: str, hasher):
    for i in range(9999999999999999):
        m = re.search(r"(.)\1\1", hasher(salt + str(i)))
        if m:
            c = m.group(1) * 5
            if any(c in hasher(salt + str(x)) for x in range(i + 1, i + 1000)):
                yield i


def solve(input: str, nth: int, hasher):
    count = 0
    for i in findkeys2(input, hasher):
        count += 1
        if count == nth:
            return i


def stretch(s: str):
    for _ in range(2017):
        s = hash.md5(s)
    return s


assert solve("abc", 64, lambda s: myhash(s, 1)) == 22728
assert solve("jlmsuwbz", 64, lambda s: myhash(s, 1)) == 35186
assert solve("abc", 1, lambda s: myhash(s, 2017)) == 10

# solve("jlmsuwbz", 64, stretch)
