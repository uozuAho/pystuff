import re
from pipe import tee, map, where
from utils.input import lines
from utils.pipe import ignore
import itertools

test1 = """
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
"""

real = """
"""


def extract2(line: str):
    bits = [x for x in re.split(r"\[|\]", line) if x]
    return bits[0::2], bits[1::2]


assert extract2("asdf") == (["asdf"], [])
assert extract2("asdf[fii]") == (["asdf"], ["fii"])


def has_abba(str: str):
    for i in range(len(str) - 3):
        a, b, c, d = str[i : i + 4]
        if a == d and b != a and b == c:
            return True
    return False


assert has_abba("abba")
assert not has_abba("abbc")


def supports_tls(nons, hypers):
    return any(has_abba(x) for x in nons) and not any(has_abba(x) for x in hypers)


# ptt1
# len(list(
#     lines(test1)
#     | map(extract2)
#     # | map(lambda x: (x, supports_tls(x[0], x[1])))
#     | where(lambda x: supports_tls(x[0], x[1]))
#     | tee
# ))  # type: ignore


def get_abas(str: str):
    for i in range(len(str) - 2):
        if str[i] == str[i + 2] and str[i + 1] != str[i]:
            yield str[i : i + 3]


assert list(get_abas("ab")) == []
assert list(get_abas("aba")) == ["aba"]
assert list(get_abas("abab")) == ["aba", "bab"]


test2 = """
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
"""


def get_many_abas(x):
    for a in x:
        yield from get_abas(a)


def supports_ssl(nons, hypers):
    abas = get_many_abas(nons)
    for a in abas:
        babb = a[1] + a[0] + a[1]
        if any(babb in x for x in hypers):
            return True
    return False


# pt2
# len(list(
#     lines(pyperclip.paste())
#     | map(extract2)
#     # | map(lambda x: list(get_many_abas(x[0])))
#     | where(lambda x: supports_ssl(x[0], x[1]))
#     | tee
# ))  # type: ignore
