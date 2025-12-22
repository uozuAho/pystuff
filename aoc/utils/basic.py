import operator
import typing as t
from functools import reduce

type Pred = t.Callable[[t.Any], bool]


def count(seq: t.Iterable, pred: Pred):
    return sum(1 if pred(x) else 0 for x in seq)


def get_or_add(d: dict, key, value=None):
    if key in d:
        return d[key]
    else:
        d[key] = value
    return value


def first(itr):
    for x in itr:
        return x
    return None


def nth(iterable, n):
    if n < 1:
        raise ValueError("n < 1. This function is 1 indexed")
    c = 0
    for i in iterable:
        c += 1
        if c == n:
            return i
    return None


def product(itr):
    return reduce(operator.mul, itr, 1)
