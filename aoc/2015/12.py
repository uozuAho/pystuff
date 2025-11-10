from collections.abc import Iterable
import sys
from aocd import get_data, submit
import json

def getnums(itr, ignore=None):
    if isinstance(itr, int):
        # print(itr)
        yield itr
    elif isinstance(itr, dict):
        # print(itr)
        if ignore is None or ignore not in itr.values():
            for x in itr.values():
                yield from getnums(x, ignore)
    elif isinstance(itr, Iterable) and not isinstance(itr, str):
        for x in itr:
            yield from getnums(x, ignore)

# pattern matching example
def getnums_p(itr, ignore=None):
    match itr:
        case int():
            yield itr
        case dict():
            if ignore is None or ignore not in itr.values():
                for x in itr.values():
                    yield from getnums(x, ignore)
        case Iterable() if not isinstance(itr, str):
            for x in itr:
                yield from getnums(x, ignore)
        case _:
            raise TypeError("oh no")

def solve(input: str):
    j = json.loads(input)
    nums = list(getnums(j))
    # print(nums)
    return sum(nums)

def solve2(input: str):
    j = json.loads(input)
    nums = list(getnums(j, ignore="red"))
    # print(nums)
    return sum(nums)

if __name__ == "__main__":
    assert solve("[1,2,3]") == 6
    assert solve("""{"a":2,"b":4}""") == 6
    assert solve("[[[3]]]") == 3
    assert solve("""{"a":{"b":4},"c":-1}""") == 3

    assert solve("""{"a":[-1,1]}""") == 0
    assert solve("""[-1,{"a":1}]""") == 0
    assert solve("[]") == 0
    assert solve("{}") == 0

    assert solve2("[1,2,3]") == 6
    assert solve2("""[1,{"c":"red","b":2},3]""") == 4

    year, day = 2015, 12
    real = get_data(year=year, day=day)
    samp = real

    if 'print' in sys.argv:
        print(solve(samp))
    elif 'submit' in sys.argv:
        submit(solve2(real), year=year, day=day)
    else:
        solve(samp)
