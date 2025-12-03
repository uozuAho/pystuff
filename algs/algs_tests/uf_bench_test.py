import pytest
from algs.union_find import QuickFindUF, QuickUnionUF


# todo: best, worst, random case
@pytest.mark.parametrize("n", [10, 100, 1000])
def test_QuickFindUF_union(benchmark, n):
    a = QuickFindUF(n)
    benchmark(a.union, 0, 0)

@pytest.mark.parametrize("n", [10, 100, 1000])
def test_QuickUnionUF_union(benchmark, n):
    a = QuickUnionUF(n)
    benchmark(a.union, 0, 0)
