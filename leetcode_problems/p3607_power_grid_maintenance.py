# You are given an integer c representing c power stations,
#  each with a unique identifier id from 1 to c (1‑based indexing).
# These stations are interconnected via n bidirectional cables,
#  represented by a 2D array connections,
#  where each element connections[i] = [ui, vi] indicates a
#  connection between station ui and station vi.
# Stations that are directly or indirectly connected form a power grid.
# Initially, all stations are online (operational).
# You are also given a 2D array queries,
#  where each query is one of the following two types:
#  - [1, x]: A maintenance check is requested for station x.
#  If station x is online, it resolves the check by itself.
#  If station x is offline, the check is resolved by the operational station
#   with the smallest id in the same power grid as x.
#  If no operational station exists in that grid, return -1.
#  - [2, x]: Station x goes offline (i.e., it becomes non-operational).
# Return an array of integers representing the results of each query of type [1, x]
#  in the order they appear.
# Note: The power grid preserves its structure; an offline (non‑operational)
#  node remains part of its grid and taking it offline does not alter connectivity.
# --- --- --- ---
# 1 <= c <= 10 ** 5
# 0 <= n == connections.length <= min(10 ** 5, c * (c - 1) / 2)
# connections[i].length == 2
# 1 <= ui, vi <= c
# ui != vi
# 1 <= queries.length <= 2 * 10 ** 5
# queries[i].length == 2
# queries[i][0] is either 1 or 2.
# 1 <= queries[i][1] <= c
import heapq

from collections import defaultdict, deque


def process_queries(
    c: int,
    connections: list[list[int]],
    queries: list[list[int]],
) -> list[int]:
    # working_solution: (36.27%, 34.31%) -> (451ms, 112.67mb)  Time: O(c * log c + m * log c) Space: O(c)
    # { node_id: edges }
    graph: dict[int, list[int]] = defaultdict(list)
    # We can have empty `connections`, but there's still `1 -> c` nodes present.
    for node_id in range(1, c + 1):
        graph[node_id] = []
    for start, end in connections:
        graph[start].append(end)
        graph[end].append(start)
    # { node_id: heapq links of the power grid }
    grid_links: dict[int, list[int]] = {}
    power_grids: list[list[int]] = []
    # BFS
    visited: set[int] = set()
    for node_id in graph.keys():
        if node_id in visited:
            continue
        que: deque[int] = deque([node_id])
        visited.add(node_id)
        
        grid: list[int] = [node_id]
        heapq.heapify(grid)
        power_grids.append(grid)
        while que:
            cur_node: int = que.popleft()
            grid_links[cur_node] = grid
            for edge in graph[cur_node]:
                if edge in visited:
                    continue
                heapq.heappush(grid, edge)
                visited.add(edge)
                que.append(edge)
    
    out: list[int] = []

    e_maint: int = 1
    e_off: int = 2

    offline: set[int] = set()
    for query in queries:
        event: int
        target: int
        event, target = query
        if e_maint == event:
            if target not in offline:
                out.append(target)
                continue
            target_grid = grid_links[target]
            min_node: int = -1
            if not target_grid:
                out.append(min_node)
                continue
            min_node: int = target_grid[0]
            while target_grid and min_node in offline:
                heapq.heappop(target_grid)
                if not target_grid:
                    break
                min_node = target_grid[0]
            if not target_grid:
                min_node = -1
            out.append(min_node)
        elif e_off == event:
            offline.add(target)

    return out


# Time complexity: O(c * log c + m * log c)
#   n - length of the input array `connections`,
#   m - length of the input array `queries`.
# ---
# `1 -> c` - loop to get all of the `graph` nodes => O(c).
# Traversing whole input array `connections` => O(c + n).
# BFS on the whole graph to get the connections.
# In the worst case there's only `1` grid, so we will push every node in it. =>
# => O(c + n + c * log c).
# In the worst case, every node will be first put to `offline`,
#  and only after used to get the `1` event. Heap will be used on each query.
# Check every `query` from the `queries` => O(c + n + c * log c + (m // 2) *  log c).
# --- --- --- ---
# Space complexity: O(c)
# `graph` <- allocates space for each node `1 -> c` => O(c).
# `grid_links` <- allocates space for each node `1 ->c ` => O(2 * c).
# In the worst case, there's only `1` power grid and every node in it.
# Even if not, there's only `c` nodes in the grid lists anyway.
# `power_grids` <- allocates space for each node `1 -> c` => O(3 * c).
# `visited` <- allocates space for each node `1 -> c` => O(4 * c).
# `que` <- allocates space for each node `1 -> c` => O(5 * c).
# `out` <- allocates space for each node `1 -> c` => O(6 * c).
# `offline` <- allocates space for each node `1 -> c` => O(7 * c)


test_c: int = 5
test_connections: list[list[int]] = [[1, 2], [2, 3], [3, 4], [4, 5]]
test_queries: list[list[int]] = [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]
test_out: list[int] = [3, 2, 3]
assert test_out == process_queries(test_c, test_connections, test_queries)

test_c = 3
test_connections = []
test_queries = [[1, 1], [2, 1], [1, 1]]
test_out = [1, -1]
assert test_out == process_queries(test_c, test_connections, test_queries)
