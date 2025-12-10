import tmp


def testasdf():
    assert True is True


def test_my_function(benchmark):
    benchmark(tmp.solve, "aaaaaaaa")
