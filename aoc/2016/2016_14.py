import re
from collections import deque

import utils.hash as hash


def findkeys(salt: str, hasher):
    cands = deque()
    counter = 0
    while True:
        while len(cands) < 1002:
            cands.append((counter, hasher(salt + str(counter))))
            counter += 1
        n, h = cands.popleft()
        m = re.search(r"(.)\1\1", h)
        if m:
            c = m.group(1)
            cc = c * 5
            for i in range(1, 1001):
                nn, hh = cands[i]
                if cc in hh:
                    yield n, h
                    break


def solve(input: str, nth: int, hasher):
    count = 0
    for k in findkeys(input, hasher):
        count += 1
        print(count, k)
        if count == nth:
            return k


def stretch(s: str):
    for _ in range(2017):
        s = hash.md5(s)
    return s


# solve("abc", 64, hash.md5)
# solve("jlmsuwbz", 64, hash.md5)

# solve("abc", 64, stretch)
# solve("jlmsuwbz", 64, stretch)
