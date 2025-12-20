from pipe import where
from utils.pipe import notempty, ignore, add


def test_notempty_ints():
    assert list([0, 1, 2] | where(notempty)) == [1, 2]


def test_notempty():
    assert list([[], None, {}, "", 1] | where(notempty)) == [1]


def test_ignore():
    assert [1, 2, 3] | ignore is None


def test_add():
    assert [1, 2, 3] | add == 6
