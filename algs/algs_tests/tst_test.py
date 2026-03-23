import pytest
from algs.tst import Tst


def make_seashells_st() -> Tst[int]:
    st: Tst[int] = Tst()
    for i, word in enumerate(
        ["she", "sells", "sea", "shells", "by", "the", "sea", "shore"]
    ):
        st.put(word, i)
    return st


def test_keys():
    st = make_seashells_st()
    assert st.keys() == ["by", "sea", "sells", "she", "shells", "shore", "the"]


def test_size():
    st = make_seashells_st()
    assert st.size() == 7


def test_get():
    st = make_seashells_st()
    assert st.get("she") == 0
    assert st.get("sells") == 1
    assert st.get("shells") == 3
    assert st.get("by") == 4
    assert st.get("the") == 5
    assert st.get("sea") == 6
    assert st.get("shore") == 7


def test_get_missing():
    st = make_seashells_st()
    assert st.get("shell") is None
    assert st.get("sh") is None
    assert st.get("xyz") is None


def test_contains():
    st = make_seashells_st()
    assert st.contains("she")
    assert st.contains("sea")
    assert not st.contains("shell")
    assert not st.contains("xyz")


def test_longest_prefix_of_shellsort():
    st = make_seashells_st()
    assert st.longest_prefix_of("shellsort") == "shells"


def test_longest_prefix_of_shell():
    st = make_seashells_st()
    assert st.longest_prefix_of("shell") == "she"


def test_longest_prefix_of_no_match():
    st = make_seashells_st()
    assert st.longest_prefix_of("xyz") is None


def test_keys_with_prefix():
    st = make_seashells_st()
    assert st.keys_with_prefix("shor") == ["shore"]


def test_keys_with_prefix_multiple():
    st = make_seashells_st()
    assert st.keys_with_prefix("se") == ["sea", "sells"]


def test_keys_with_prefix_exact_match():
    st = make_seashells_st()
    result = st.keys_with_prefix("she")
    assert "she" in result
    assert "shells" in result


def test_keys_with_prefix_no_match():
    st = make_seashells_st()
    assert st.keys_with_prefix("xyz") == []


def test_keys_that_match():
    st = make_seashells_st()
    assert st.keys_that_match(".he.l.") == ["shells"]


def test_keys_that_match_wildcard():
    st = make_seashells_st()
    assert st.keys_that_match("...") == ["sea", "she", "the"]


def test_keys_that_match_no_match():
    st = make_seashells_st()
    assert st.keys_that_match("zzz") == []


def test_put_overwrite():
    st: Tst[int] = Tst()
    st.put("hello", 1)
    st.put("hello", 2)
    assert st.get("hello") == 2
    assert st.size() == 1


def test_put_delete_with_none():
    st: Tst[int] = Tst()
    st.put("hello", 1)
    st.put("world", 2)
    assert st.size() == 2
    st.put("hello", None)
    assert st.size() == 1
    assert st.get("hello") is None
    assert st.contains("hello") is False


def test_empty_tst():
    st: Tst[int] = Tst()
    assert st.size() == 0
    assert st.keys() == []
    assert st.get("anything") is None
    assert st.contains("anything") is False


def test_invalid_key_get():
    st: Tst[int] = Tst()
    with pytest.raises(ValueError):
        st.get(None)
    with pytest.raises(ValueError):
        st.get("")


def test_invalid_key_put():
    st: Tst[int] = Tst()
    with pytest.raises(ValueError):
        st.put(None, 1)


def test_invalid_key_contains():
    st: Tst[int] = Tst()
    with pytest.raises(ValueError):
        st.contains(None)
