import heapq


def path(prev, last):
    return [] if last is None else path(prev, prev[last]) + [last]


def astar_search(start, h_func, moves_func):
    """Find the shortest sequence of states from start to a goal state
    (a state s with h_func(s) == 0).

    stolen from https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2016.ipynb

    Params:
    start: initial state. States must be hashable
    h_func: function that takes a state and returns an estimate of the number
            of moves to the goal state. Must never be higher than the actual
            number of moves, else you may  not get the shortest path.
    moves_func: function that takes a state and returns all valid
            subsequent states

    Returns: [shortest path], {stats}
    """
    # A priority queue, ordered by path length, f = g + h
    frontier = [(h_func(start), start)]

    # start state has no previous state; other states will
    previous = {start: None}

    # The cost of the best path to a state.
    path_cost = {start: 0}

    num_explored = 0

    while frontier:
        (f, s) = heapq.heappop(frontier)
        num_explored += 1
        if h_func(s) == 0:
            return path(previous, s), {
                "num_explored": num_explored,
                "len(frontier)": len(frontier),
            }
        for ns in moves_func(s):
            new_cost = path_cost[s] + 1
            if ns not in path_cost or new_cost < path_cost[ns]:
                # this is what i missed in my search: don't search nodes
                # whose cost is known to be more than optimal
                heapq.heappush(frontier, (new_cost + h_func(ns), ns))
                path_cost[ns] = new_cost
                previous[ns] = s
    return None, {"num_explored": num_explored, "len(frontier)": len(frontier)}
