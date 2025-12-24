import operator
import math
from functools import reduce


def product(itr):
    return reduce(operator.mul, itr, 1)

def divisors(n):
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            if n // i != i:
                yield n // i


def proper_divisors(n):
    """ all divisors < n """
    return (x for x in divisors(n) if x < n)
