# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way
#  to travel between two different cities (this network form a tree).
# Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
# Your task consists of reorienting some roads such that each city can visit the city 0.
# Return the minimum number of edges changed.
# It's guaranteed that each city can reach city 0 after reorder.
# --------------------
# 2 <= n <= 5 * 10 ** 4
# connections.length == n - 1
# connections[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi


def min_reorder(n: int, connections: list[list[int]]) -> int:
    # working_sol (61.90%, 51.99%) -> (1098ms, 70.54mb)  time: O(n) | space: O(n)
    adj_cities: list[list[list[int]]] = [[] for _ in range(n)]
    for connection in connections:
        # Original connection for a pair of cities.
        # We need to change, sign == 1.
        adj_cities[connection[0]].append([connection[1], 1])
        # Artificial, we need to build. So it's sign == 0.
        adj_cities[connection[1]].append([connection[0], 0])
    count: list[int] = [0]

    def dfs(node: int, parent: int) -> None:
        # Moving from Parent to Child.
        for child, sign in adj_cities[node]:
            # We don't need to use nodes from which we came.
            if child != parent:
                # If we come by original path, we need to reverse it.
                # And we marked it by sign == 1.
                count[0] += sign
                dfs(child, node)

    dfs(0, -1)
    return count[0]


# Time complexity: O(n) -> creating adjacent list for every city => O(n) ->
# n - input value^^| -> populate with every city_pair from connections => O(n) ->
#                    -> using dfs on every node at max 2 times => O(n).
# Auxiliary space: O(n) -> stack will not exceed using all elements from adj_list => O(n) ->
#                       -> and adj_list itself is size of n => O(n).
# --------------------
# Actually had no idea about this method with directions.
# Like every edge of Nodes(cities) pair will have 2 directions:
#  original -> standard connection direction, marked with sign == 1.
#  artificial -> direction we added as reverse, and marked with sign == 0.
# Using DFS on every city to count all original connections, moving from PARENT to CHILD.
# --------------------
# Ok. My solution is working for 74/76 test_cases. 75 missing some nodes, why?
# Like we're checking every path which leads to a correctly set(leading to 0) and not counting them,
#  and only counting +1 for every return from empty path -> leading to not set cities.
# Can't even debug it correctly, 5 * 10 ** 4 connections.
# Don't see how it's check() fault, cuz it's simple check of 2 various paths.
# There's nothing to fail, maybe Graph? Not much experienced with Graphs, guess it can be build
#  incorrectly. It's not even a Graph but adjacent dictionary. Still we're given every connection,
#  between cities, so we can't miss something if we go One by One.
# W.e taking Hints, I just don't know enough about Graphs|Theory.


test: list[list[int]] = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
test_n: int = 6
test_out: int = 3
assert test_out == min_reorder(test_n, test)

test = [[1, 0], [1, 2], [3, 2], [3, 4]]
test_n = 5
test_out = 2
assert test_out == min_reorder(test_n, test)

test = [[1, 0], [2, 0]]
test_n = 3
test_out = 0
assert test_out == min_reorder(test_n, test)

test = [[1, 4], [2, 3], [3, 1], [4, 0], [5, 4]]
test_n = 6
test_out = 0
assert test_out == min_reorder(test_n, test)
