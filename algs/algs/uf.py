# https://algs4.cs.princeton.edu/15uf/QuickUnionUF.java.html
class QuickUnionUF:
    def __init__(self, n: int) -> None:
        if n < 0:
            raise ValueError(f"n must be non-negative, got {n}")

        self._parent = list(range(n))
        self._count = n

    @property
    def count(self) -> int:
        return self._count

    def find(self, p: int) -> int:
        self._validate(p)

        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def _validate(self, p: int) -> None:
        n = len(self._parent)
        if not 0 <= p < n:
            raise IndexError(f"index {p} is not between 0 and {n-1}")

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int) -> None:
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return

        self._parent[root_p] = root_q
        self._count -= 1
