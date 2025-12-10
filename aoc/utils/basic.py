import typing as t

type Pred = t.Callable[[t.Any], bool]

def count(seq, pred: Pred):
    return sum(1 if pred(x) else 0 for x in seq)
