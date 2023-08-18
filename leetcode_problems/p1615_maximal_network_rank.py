# There is an infrastructure of n cities with some number of roads connecting these cities.
# Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.
# The network rank of two different cities is defined as the total number of directly connected roads to either city.
# If a road is directly connected to both cities, it is only counted once.
# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
# -----------------------
# 2 <= n <= 100
# 0 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 2
# 0 <= ai, bi <= n-1
# ai != bi
# Each pair of cities has at most one road connecting them.


def maximal_network_rank(n: int, roads: list[list[int]]) -> int:
    # working_sol (87.10%, 32.46%) -> (304ms, 18.5mb)  time: O(m + n ** 2) | space: O(m)
    city_roads: dict[int, set[int]] = {}
    max_rank: int = 0
    # Cities are zero_indexed, why?
    # Like it's not intuitive to have City == 0,
    #  and last city == 3 when -> number of cities == n = 4.
    for _ in range(n):
        city_roads[_] = set()
    for pair in roads:
        # ! bidirectional road between cities !
        city_roads[pair[0]].add(pair[1])
        city_roads[pair[1]].add(pair[0])
    # Graph1edges + Graph2edges if GraphsConnected -1.
    # For every pair of cities.
    for x in range(n):
        for y in range(x + 1, n):
            cur_rank: int = len(city_roads[x]) + len(city_roads[y])
            # Every road is bidirectional, so it's either x in y or y in x, w.e.
            if x in city_roads[y]:
                cur_rank -= 1
            max_rank = max(cur_rank, max_rank)
    return max_rank


# Time complexity: O(m + n ** 2) -> populating dictionary with zero_indexed range of cities => O(n) ->
# m - len of input roads^^|  -> record every pair of roads going from one city to another => O(m) ->
# n - input num of cities^^| -> calculating max_rank for every possible pair of cities => O(n ** 2).
# Auxiliary space: O(m) -> in the worse case there's no duplicates in roads, then we will store every possible
#                          pair of roads into a dictionary by their starting cities => O(m).
# -----------------------
# ! The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities. !
# So we need to check all pairs of cities and combine number of ROADS leading to this city or leading from it?
# Cuz all ROADS == ! bidirectional road between cities !, we need to get all incoming|outgoing roads and
# take -1 from it, cuz 1 of these roads connect cities?
# What about not connected cities? ! directly connected roads to either city ! <- guess we don't care,
# and just need to take all pairs and summarize their ROADS and if there's connection between, take -1.
# Something like: Graph1edges + Graph2edges if GraphsConnected -1. Should be correct.


test: list[list[int]] = [[0, 1], [0, 3], [1, 2], [1, 3]]
test_n: int = 4
test_out: int = 4
assert test_out == maximal_network_rank(test_n, test)

test = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
test_n = 5
test_out = 5
assert test_out == maximal_network_rank(test_n, test)

test = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
test_n = 8
test_out = 5
assert test_out == maximal_network_rank(test_n, test)
