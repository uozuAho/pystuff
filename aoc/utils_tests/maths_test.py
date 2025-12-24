import pytest

from utils.maths import product, divisors, proper_divisors


def test_product():
    assert product([1, 2, 3]) == 6
    assert product([1, 2, 3, 4]) == 24
    # assert product([]) == 0  # what is the product of an empty set?

@pytest.mark.parametrize(
    "n, expected",
    [
        (3, (1, 3)), (4, (1, 2, 4)), (15, (1, 3, 5, 15))
    ]
)
def test_divisors(n, expected):
    assert tuple(sorted(divisors(n))) == expected
