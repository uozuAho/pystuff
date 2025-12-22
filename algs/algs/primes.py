from dataclasses import dataclass
import functools
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def primes(nmax: int):
    """primes up to but not including nmax,
    using https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""
    _p = [True] * nmax
    for i in range(2, math.ceil(math.sqrt(nmax)) + 1):
        if _p[i]:
            for j in range(i * i, nmax, i):
                _p[j] = False
    for i in range(2, nmax):
        if _p[i]:
            yield i


@dataclass
class _Node:
    val: int
    left: "_Node | None" = None
    right: "_Node | None" = None


def prime_factors(n: int) -> list[int]:
    """Find all prime factors of n. Uses the factor tree method. Not as
    efficient as the sieve, but easy to implement."""

    @functools.cache
    def facs2(_n):
        """first 2 factors (if they exist)"""
        for i in range(2, _n // 2 + 1):
            if _n % i == 0:
                return [i, _n // i]
        return None

    def factree(node: _Node):
        facs = facs2(node.val)
        if facs:
            node.left = factree(_Node(facs[0]))
            node.right = factree(_Node(facs[1]))
        return node

    def leaf_vals(tree: _Node, vals=None):
        if vals is None:
            vals = []
        if tree.left and tree.right:
            leaf_vals(tree.left, vals)
            leaf_vals(tree.right, vals)
        else:
            vals.append(tree.val)
        return vals

    return leaf_vals(factree(_Node(n)))
