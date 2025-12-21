import algs.astar as astar


def test_astar():
    def h(state: int):
        return 10 - state

    def gennext(state: int):
        return state - 1, state + 1

    path, _ = astar.astar_search(0, h, gennext)

    assert path == list(range(11))
