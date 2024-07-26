# There are n cities numbered from 0 to n-1.
# Given the array edges where edges[i] = [fromi, toi, weighti]
#  represents a bidirectional and weighted edge between cities fromi and toi,
#  and given the integer distanceThreshold.
# Return the city with the smallest number of cities that are reachable through some path
#  and whose distance is at most distanceThreshold,
#  If there are multiple such cities, return the city with the greatest number.
# Notice that the distance of a path connecting cities i and j
#  is equal to the sum of the edges' weights along that path.
# ----------------------
# 2 <= n <= 100
# 1 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti, distanceThreshold <= 10^4
# All pairs (fromi, toi) are distinct.


def find_the_city(n: int, edges: list[list[int]], distance_threshold: int) -> int:
    # working_sol (44.04%, 80.04%) -> (455ms, 17.60mb)  time: O(n ** 3) | space: O(n * n)

    # Floyd-Warshall
    def floyd(nodes: int, graph_dist: list[list[int | float]]) -> None:
        for con in range(nodes):
            for node1 in range(nodes):
                for node2 in range(nodes):
                    graph_dist[node1][node2] = min(
                        graph_dist[node1][node2],
                        graph_dist[node1][con] + graph_dist[con][node2],
                    )

    # row = Node, col = edge, value = distance between them.
    graph_distances: list[list[int | float]] = [[float('inf') for _ in range(n)] for _ in range(n)]
    # Distance to itself == 0
    for _ in range(n):
        graph_distances[_][_] = 0
    # Distances we know.
    for start, end, distance in edges:
        graph_distances[start][end] = distance
        graph_distances[end][start] = distance
    floyd(n, graph_distances)
    out: int = -1
    cities_count = n
    for node in range(n):
        cur_cities_count: int = 0
        for edge in range(n):
            if node != edge and graph_distances[node][edge] <= distance_threshold:
                cur_cities_count += 1
            if cur_cities_count > cities_count:
                break
        if cities_count >= cur_cities_count:
            cities_count = cur_cities_count
            out = node
    return out


# Time complexity: O(n ** 3) <- n - input value == # of Nodes in graph, k - length of input array `edges`
# Always creating `graph_distances` with size == `n * n` => O(n * n).
# Always populating distance for Nodes themselves => O(n + n * n).
# Always populating distances between Nodes we know => O(n + n * n + k).
# Floyd-Warshall <- 3 nested loops to get distances between Nodes through some Connector Node => O(n ** 3) =>
# => O(n ** 3 + n + k + n * n).
# Extra traversing every Node to get cities we can reach => O(2 * (n * n) + n + k + n ** 3).
# ----------------------
# Auxiliary space; O(n * n)
# `graph_distances` <- always of size `n * n`) => O(n * n).


test: int = 4
test_edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
test_distance: int = 4
test_out: int = 3
assert test_out == find_the_city(test, test_edges, test_distance)

test = 5
test_edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
test_distance = 2
test_out = 0
assert test_out == find_the_city(test, test_edges, test_distance)
