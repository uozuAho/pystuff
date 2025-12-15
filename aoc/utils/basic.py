import typing as t

type Pred = t.Callable[[t.Any], bool]


def count(seq: t.Iterable, pred: Pred):
    return sum(1 if pred(x) else 0 for x in seq)


def get_or_add(d: dict, key, value=None):
    if key in d:
        return d[key]
    else:
        d[key] = value
    return value
