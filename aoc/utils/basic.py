import typing as t

type Pred = t.Callable[[t.Any], bool]

def count(seq, pred: Pred):
    return sum(1 if pred(x) else 0 for x in seq)


def pipe(init, *funcs):
    """ pipe functions together, like F#'s |>
        Eg. instead of d(c(b(a()))):
        pipe(a, b, c, d)

        Works with generators, dunno how!
    """
    current = init
    for f in funcs:
        current = f(current)
    return current
