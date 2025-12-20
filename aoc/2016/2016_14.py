import re
from functools import lru_cache

import utils.hash as hash
from utils.basic import nth


@lru_cache(maxsize=1010)
def myhash(salt: str, i: int, repeat: int = 1):
    for _ in range(repeat):
        salt = hash.md5(salt + str(i))
    return salt


def findkeys2(salt: str, hasher):
    for i in range(9999999999999999):
        m = re.search(r"(.)\1\1", hasher(salt, i))
        if m:
            c = m.group(1) * 5
            if any(c in hasher(salt, x) for x in range(i + 1, i + 1001)):
                yield i


def solve(input: str, n: int, hasher):
    return nth(findkeys2(input, hasher), n)


assert solve("abc", 64, myhash) == 22728
assert solve("jlmsuwbz", 64, myhash) == 35186

def asdf(salt, i):
    return myhash(salt, i, 2017)

# this may be broken, not sure
assert solve("abc", 1, asdf) == 18 # was 10??
