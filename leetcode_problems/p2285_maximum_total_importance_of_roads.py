# You are given an integer n denoting the number of cities in a country.
# The cities are numbered from 0 to n - 1.
# You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there
#  exists a bidirectional road connecting cities ai and bi.
# You need to assign each city with an integer value from 1 to n,
#  where each value can only be used once.
# The importance of a road is then defined as the sum of the values of the two cities it connects.
# Return the maximum total importance of all roads possible after assigning the values optimally.
# ---------------------------------
# 2 <= n <= 5 * 10 ** 4
# 1 <= roads.length <= 5 * 10 ** 4
# roads[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no duplicate roads.
from collections import defaultdict, deque


def maximum_importance(n: int, roads: list[list[int]]) -> int:
    # working_sol (58.61%, 10.66%) -> (1244ms, 45.23mb)  time: O(n + n * log n) | space: O(n)
    # {Node: [edges]} == {City: [roads]}
    graph: dict[int, list[int]] = defaultdict(list)
    for city1, city2 in roads:
        graph[city1].append(city2)
        graph[city2].append(city1)
    # [cities sorted by their importance == number of edges(roads) they have] <- descending order
    sorted_cities: list[int] = [index for index in range(n)]
    sorted_cities.sort(reverse=True, key=lambda x: len(graph[x]))
    importance: int = n
    out: int = 0
    for city in sorted_cities:
        # W.e the path we choose and method we use BFS|DFS.
        # We're still going to use roads(edges) of the particular Node(City) only Once.
        # And every single one of them is a sum of this city and adjusted city.
        # So, we can just ignore adjusted cities and count all the roads of a city.
        out += importance * len(graph[city])
        importance -= 1
    return out


# Time complexity: O(n + n * log n) <- n - input value `n`.
# `len(roads)` == `n` -> We're always traversing whole `roads` to build the graph => O(n).
# Building and sorting array with the same size `n` => O(n + n * log n).
# And extra traversing this sorted array `sorted_cities` once again => O(n) => O(3n + n * log n).
# ---------------------------------
# Auxiliary space: O(n).
# `graph` is always of the size `n` and values inside at max is going to be of size `n - 1`,
#  when Node is connected to every1.
# `sorted_cities` is also of size `n` and `sort()` is taking extra `n` => O(3n).


test_n: int = 5
test: list[list[int]] = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
test_out: int = 43
assert test_out == maximum_importance(test_n, test)

test_n = 5
test = [[0, 3], [2, 4], [1, 3]]
test_out = 20
assert test_out == maximum_importance(test_n, test)

test_n = 10
test = [[7, 8], [8, 5], [5, 1], [0, 4], [4, 2], [2, 3], [9, 2], [2, 6], [6, 4], [4, 7], [7, 9], [9, 5], [4, 8], [8, 3],
        [8, 9], [9, 3], [3, 1], [1, 4]]
test_out = 238
assert test_out == maximum_importance(test_n, test)
