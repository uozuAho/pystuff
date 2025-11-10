from mylib.stuff import hello_msg


def test_hello_msg():
    assert hello_msg("bert") == "hi bert!"


def test_hello_msg_b(benchmark):
    benchmark(hello_msg, "aaaaaaaa")
