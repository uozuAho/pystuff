from pipe import Pipe


def notempty(thing):
    """Usage: where(notempty)"""
    return bool(thing)


@Pipe
def ignore(iterable):
    """Force iteration and drop the result. Good for interactive dev with `tee`
    without having to wrap the pipeline in list
    """
    things = []
    for x in iterable:
        things.append(x)
    return None


@Pipe
def add(iterable):
    return sum(iterable)
