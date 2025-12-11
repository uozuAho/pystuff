import itertools


def pipe(init, *funcs):
    """pipe functions together, like F#'s |>
    Eg. instead of d(c(b(a()))):
    pipe(a, b, c, d)
    """
    current = init
    for f in funcs:
        current = f(current)
    return current


def pprint(x):
    if hasattr(x, "__next__"):
        x = list(x)
    if len(x) == 1:
        print(x)
    else:
        print('[')
        for y in x:
            print('  ', y)
        print(']')
    return x


def flatten(x):
    return itertools.chain.from_iterable(x)
