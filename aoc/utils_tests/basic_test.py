from utils.basic import nth, product


def test_nth():
    assert nth([0, 1, 2], 1) == 0


def test_product():
    assert product([1, 2, 3]) == 6
    assert product([1, 2, 3, 4]) == 24
    # assert product([]) == 0  # what is the product of an empty set?
