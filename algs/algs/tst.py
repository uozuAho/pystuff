from dataclasses import dataclass
from typing import Generic, TypeVar

V = TypeVar("V")


@dataclass
class _Node(Generic[V]):
    char: str
    left: "_Node[V] | None" = None
    mid: "_Node[V] | None" = None
    right: "_Node[V] | None" = None
    val: "V | None" = None


class Tst(Generic[V]):
    """Symbol table with string keys implemented using a ternary search trie.
    Ported from https://algs4.cs.princeton.edu/52trie/TST.java.html
    """

    def __init__(self):
        self._size: int = 0
        self._root: _Node[V] | None = None

    def size(self) -> int:
        return self._size

    def contains(self, key: str) -> bool:
        if key is None:
            raise ValueError("argument to contains() is null")
        return self.get(key) is not None

    def get(self, key: str) -> "V | None":
        if key is None:
            raise ValueError("calls get() with null argument")
        if len(key) == 0:
            raise ValueError("key must have length >= 1")
        x = self._get(self._root, key, 0)
        if x is None:
            return None
        return x.val

    def _get(self, x: "_Node[V] | None", key: str, d: int) -> "_Node[V] | None":
        if x is None:
            return None
        char = key[d]
        if char < x.char:
            return self._get(x.left, key, d)
        elif char > x.char:
            return self._get(x.right, key, d)
        elif d < len(key) - 1:
            return self._get(x.mid, key, d + 1)
        else:
            return x

    def put(self, key: str, val: "V | None") -> None:
        if key is None:
            raise ValueError("calls put() with null key")
        if not self.contains(key):
            self._size += 1
        elif val is None:
            self._size -= 1
        self._root = self._put(self._root, key, val, 0)

    def _put(
        self, x: "_Node[V] | None", key: str, val: "V | None", d: int
    ) -> "_Node[V]":
        c = key[d]
        if x is None:
            x = _Node(char=c)
        if c < x.char:
            x.left = self._put(x.left, key, val, d)
        elif c > x.char:
            x.right = self._put(x.right, key, val, d)
        elif d < len(key) - 1:
            x.mid = self._put(x.mid, key, val, d + 1)
        else:
            x.val = val
        return x

    def longest_prefix_of(self, query: str) -> "str | None":
        if query is None:
            raise ValueError("calls longest_prefix_of() with null argument")
        if len(query) == 0:
            return None
        length = 0
        x = self._root
        i = 0
        while x is not None and i < len(query):
            c = query[i]
            if c < x.char:
                x = x.left
            elif c > x.char:
                x = x.right
            else:
                i += 1
                if x.val is not None:
                    length = i
                x = x.mid
        return query[:length] if length > 0 else None

    def keys(self) -> list[str]:
        queue: list[str] = []
        self._collect(self._root, [], queue)
        return queue

    def keys_with_prefix(self, prefix: str) -> list[str]:
        if prefix is None:
            raise ValueError("calls keys_with_prefix() with null argument")
        queue: list[str] = []
        x = self._get(self._root, prefix, 0)
        if x is None:
            return queue
        if x.val is not None:
            queue.append(prefix)
        self._collect(x.mid, list(prefix), queue)
        return queue

    def keys_that_match(self, pattern: str) -> list[str]:
        queue: list[str] = []
        self._collect_pattern(self._root, [], 0, pattern, queue)
        return queue

    def _collect(
        self, x: "_Node[V] | None", prefix: list[str], queue: list[str]
    ) -> None:
        if x is None:
            return
        self._collect(x.left, prefix, queue)
        if x.val is not None:
            queue.append("".join(prefix) + x.char)
        self._collect(x.mid, prefix + [x.char], queue)
        self._collect(x.right, prefix, queue)

    def _collect_pattern(
        self,
        x: "_Node[V] | None",
        prefix: list[str],
        i: int,
        pattern: str,
        queue: list[str],
    ) -> None:
        if x is None:
            return
        c = pattern[i]
        if c == "." or c < x.char:
            self._collect_pattern(x.left, prefix, i, pattern, queue)
        if c == "." or c == x.char:
            if i == len(pattern) - 1 and x.val is not None:
                queue.append("".join(prefix) + x.char)
            if i < len(pattern) - 1:
                self._collect_pattern(x.mid, prefix + [x.char], i + 1, pattern, queue)
        if c == "." or c > x.char:
            self._collect_pattern(x.right, prefix, i, pattern, queue)
