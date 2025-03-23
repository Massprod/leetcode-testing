# You are in a city that consists of n intersections numbered from 0 to n - 1
#  with bi-directional roads between some intersections.
# The inputs are generated such that you can reach any intersection
#  from any other intersection and that there is at most one road between
#  any two intersections.
# You are given an integer n and a 2D integer array roads where
#  roads[i] = [ui, vi, timei] means that there is a road
#  between intersections ui and vi that takes timei minutes to travel.
# You want to know in how many ways you can travel from intersection 0
#  to intersection n - 1 in the shortest amount of time.
# Return the number of ways you can arrive at your destination
#  in the shortest amount of time.
# Since the answer may be large, return it modulo 10 ** 9 + 7.
# --------------------------
# 1 <= n <= 200
# n - 1 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 3
# 0 <= ui, vi <= n - 1
# 1 <= timei <= 10 ** 9
# ui != vi
# There is at most one road connecting any two intersections.
# You can reach any intersection from any other intersection.
import heapq


def count_paths(n: int, roads: list[list[int]]) -> int:
    # working_sol (94.48%, 68.75%) -> (12ms, 25.05mb)  time: O((n + m) * log(n))
    #                                                  space: O(n + m)
    # { node: [(edge, time to travel)] }
    graph: dict[int, list[tuple[int, int]]] = {
        inter: [] for inter in range(n)
    }

    for start, end, time in roads:
        graph[start].append(
            (end, time)
        )
        graph[end].append(
            (start, time)
        )

    target_node: int = n - 1
    time_limit: int = 200 * 10 ** 9
    min_times: list[int] = [time_limit for _ in range(n)]
    # We start from `0` == we can reach it with 1 path.
    node_paths: list[int] = [1] + [0 for _ in range(n - 1)]
    #  [ (travel_time, node) ]
    que: list[tuple[int, int]] = [(0, 0)]
    heapq.heapify(que)
    while que:
        acc_time: int
        cur_node: int
        acc_time, cur_node = heapq.heappop(que)
        # We already have a path, which takes less time to travel.
        # Than the one we try to explore => skip + ignore.
        if acc_time > min_times[cur_node]:
            continue
        for edge, time in graph[cur_node]:
            edge_time: int = time + acc_time
            # We found a less consuming path.
            if edge_time < min_times[edge]:
                min_times[edge] = edge_time
                # Paths leading to this Node are equal to paths
                #  ending on the Node we come from.
                # For the same amount of time we checked.
                node_paths[edge] = node_paths[cur_node]
                heapq.heappush(que, (edge_time, edge))
            # We found the same time consuming path.
            # But it's coming from a different Node => extra new path.
            elif edge_time == min_times[edge]:
                node_paths[edge] += node_paths[cur_node]

    return node_paths[target_node] % (10 ** 9 + 7)


# Time complexity: O((n + m) * log(n)) <- n - number of nodes
#                                         m - number of edges in the graph.
# Creating graph with all Nodes and their edges traversal => O(n + m).
# Traversing whole graph, with Djikstra's algo and using every Node + edges, once =>
# => O(n + m + (n + m) * log (n)).
# heap.pop()||push() always log(N) <- N - number of current records.
# --------------------------
# Auxiliary space: O(n + m)
# `graph` <- allocates space for each Node as a key, and values are edges => O(n + m).
# `min_times` <- allocates space for each Node == `n` => O(2 * n + m).
# `node_paths` <- allocates space for each Node == `n` => O(3 * n + m).
# `que` <- allocates space for each Node we visit => O(4 * n + m).


test_n: int = 7
test_roads: list[list[int]] = [
    [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3],
    [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2],
]
test_out: int = 4
assert test_out == count_paths(test_n, test_roads)

test_n = 2
test_roads = [[1, 0, 10]]
test_out = 1
assert test_out == count_paths(test_n, test_roads)
