# You are given an integer n and a 2D integer array queries.
# There are n cities numbered from 0 to n - 1.
# Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.
# queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi.
# After each query, you need to find the length of the shortest path from city 0 to city n - 1.
# Return an array answer where for each i in the range [0, queries.length - 1],
#  answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.
# -------------------------
# 3 <= n <= 500
# 1 <= queries.length <= 500
# queries[i].length == 2
# 0 <= queries[i][0] < queries[i][1] < n
# 1 < queries[i][1] - queries[i][0]
# There are no repeated roads among the queries.
import heapq


def shortest_distance_after_queries(n: int, queries: list[list[int]]) -> list[int]:
    # working_sol (50.38%, 8.31%) -> (908ms, 17.64mb)  time: O(m * n * log n) | space: O(m + n)
    # { Node: [ edges ] }
    graph: dict[int, list[int]] = {
        val: [val + 1] for val in range(n - 1)
    }

    def bfs_dij(start: int) -> int:
        node: int
        dist: int
        # [ ( used distance, node ) ]
        que: list[tuple[int, int]] = [(0, start)]
        visited: set[int] = {start}
        heapq.heapify(que)
        while que:
            dist, node = heapq.heappop(que)
            if node == n - 1:
                return dist
            for edge in graph[node]:
                if edge in visited:
                    continue
                visited.add(edge)
                heapq.heappush(
                    que, (dist + 1, edge)
                )
        return -1

    out: list[int] = []
    for _start, _end in queries:
        graph[_start].append(_end)
        out.append(bfs_dij(0))
    return out


# Time complexity: O(m * n * log n) <- m - length of the input array `queries`.
# Always using every `query` from `queries`, and for every `query` we're using Dijkstra's algo => O(m * n * log n).
# -------------------------
# Auxiliary space: O(m + n).
# `out` <- allocates space for each `query` result => O(m).
# `que` <- allocates space for each node => O(m + n).
# `visited` <- allocates space for each node => O(m + 2 * n).


test_n: int = 5
test_queries: list[list[int]] = [[2, 4], [0, 2], [0, 4]]
test_out: list[int] = [3, 2, 1]
assert test_out == shortest_distance_after_queries(test_n, test_queries)

test_n = 4
test_queries = [[0, 3], [0, 2]]
test_out = [1, 1]
assert test_out == shortest_distance_after_queries(test_n, test_queries)
