# You are given an array routes representing bus routes where routes[i]
#  is a bus route that the ith bus repeats forever.
# For example, if routes[0] = [1, 5, 7],
#  this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially),
#  and you want to go to the bus stop target.
# You can travel between bus stops by buses only.
# Return the least number of buses you must take to travel from source to target.
# Return -1 if it is not possible.
# -----------------
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10 ** 5
# All the values of routes[i] are unique.
# sum(routes[i].length) <= 10 ** 5
# 0 <= routes[i][j] < 10 ** 6
# 0 <= source, target < 10 ** 6
from collections import defaultdict, deque


def num_buses_to_destination(routes: list[list[int]], source: int, target: int) -> int:
    # working_sol (89.85%, 26.10%) -> (457ms, 52.5mb)  time: O(n * k) | space: O(n * k)
    if target == source:
        return 0
    # (bus_stop: [routes we can take from this bus_stop])
    graph: dict[int, set[int]] = defaultdict(set)
    for x in range(len(routes)):
        for bus_stop in routes[x]:
            graph[bus_stop].add(x)
    # (bus_stop, buses taken)
    que: deque[tuple[int, int]] = deque([(source, 0)])
    visited: set[int] = {source}
    while que:
        stop_data: tuple[int, int] = que.popleft()
        cur_stop: int = stop_data[0]
        buses: int = stop_data[1]
        if cur_stop == target:
            return buses
        # Route switch == new route == new bus taken.
        for route in graph[cur_stop]:
            for bus_stop in routes[route]:
                if bus_stop not in visited:
                    que.append((bus_stop, buses + 1))
                    visited.add(bus_stop)
            # If we return to this `route` later, it's longer path == we don't care.
            # If we have another `bus_stop` leading to this route with the same path length == we don't care.
            # Because we already added this route `bus_stop`'s into a que with the same bus count.
            # So, we can annul every `route` we processed. Or extra storage for visited routes.
            routes[route] = []
    return -1


# Time complexity: O(n * k) <- ! k - len of current 'route' we process , n - len of input array 'routes' !
#  worst case == every route has unique bus_stops -> create graph with 'n' * 'k' Nodes(stops) => O(n * k).
#  worst case for BFS == [[1, 2], [2, 3], ... etc. [..., target] -> we will use every bus_stop we're given => O(n * k).
#                         ^^Source == 1.
# Auxiliary space: O(n * k)
# worst case == every route has unique bus_stops -> graph will have all bus_stops stored and because they're all unique
#  they only lead to 1 route, but Nodes are equal to ('n' * 'k') => O(n * k).
# worst case for BFS == [[1, 2], [2, 3], ... etc. [..., target] -> allocating space for every tuple(Node + bus_count)
#  in the que, and extra set(visited) with the same size => O(3 * (n * k))
# -----------------
# Ok. Top % are actually doing hybrid version.
# Which I was thinking at first. But failed because tried to use only bus_stops as Nodes and edges.
# In this case we can't count buses taken, but can find what bus_stops we need to visit.
# In hybrid version we can count buses, because when we change route it's always +1 bus.
# Node == bus_stop + Edges == routes we can travel from them.
# And it's a lot faster because we're not forced to build graph with [route: all routes connected].
# Rebuild with this approach cuz 5700ms O(n ** n * k) is too slow.
# n - len of 'routes' , k - current len of 'route' we process.
# -----------------
# Tag is BFS hmm.
# We can use all bus_stops as Nodes and try to move on them, but how to count buses?
# Like: bus_stop '7' can have edges: '8', '9'. And target == '11'
# And all of them are from different routes.
# Something like: [['7', '8', '9', '10', '11'], ['9', '11']]
# If we use BFS on every bus_stop as Node then we will find: '7' -> '8' -> '9' -> '11', buses == 2
# When we could have used: '7' -> '8' -> '9' -> '10' -> '11', with only 1 bus.
# So, we can't use bus_stops as Nodes. Then what?
# Essentially we only care about used buses, right?
# What if we use whole routes as Nodes?
# Like we know that if we have corresponding bus_stops in both routes, then we can travel between them,
#  and it will cost as +1 bus used.
# So, our graph should use whole routes as Nodes and connect them only if they have same bus_stops.
# Should be correct, but slow.


test: list[list[int]] = [[1, 2, 7], [3, 6, 7]]
test_source: int = 1
test_target: int = 6
test_out: int = 2
assert test_out == num_buses_to_destination(test, test_source, test_target)

test = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
test_source = 15
test_target = 12
test_out = -1
assert test_out == num_buses_to_destination(test, test_source, test_target)

test = [[1, 2, 7], [3, 6, 7], [6, 5, 11]]
test_source = 1
test_target = 11
test_out = 3
assert test_out == num_buses_to_destination(test, test_source, test_target)

test = [
    [0, 1, 6, 16, 22, 23], [14, 15, 24, 32], [4, 10, 12, 20, 24, 28, 33],
    [1, 10, 11, 19, 27, 33], [11, 23, 25, 28], [15, 20, 21, 23, 29], [29]
]
test_source = 4
test_target = 21
test_out = 2
assert test_out == num_buses_to_destination(test, test_source, test_target)
