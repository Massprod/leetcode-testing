# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1,
#  and an array edges where edges[i] = [ui, vi, wi] represents a directed edge
#  from node ui to node vi with cost wi.
# Each node ui has a switch that can be used at most once: when you arrive at ui
#  and have not yet used its switch, you may activate it on one
#  of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.
# The reversal is only valid for that single move,
#  and using a reversed edge costs 2 * wi.
# Return the minimum total cost to travel from node 0 to node n - 1.
# If it is not possible, return -1.
# --- --- --- ---
# 2 <= n <= 5 * 10 ** 4
# 1 <= edges.length <= 10 ** 5
# edges[i] = [ui, vi, wi]
# 0 <= ui, vi <= n - 1
# 1 <= wi <= 1000
import heapq
from collections import defaultdict


def min_cost(n: int, edges: list[list[int]]) -> int:
    # working_solution: 76.27%, 37.82%) -> (420ms, 71.05mb)  Time: O(n * log n) Space: O(n)
    cost: int
    node: int
    # { node: [ (edge, cost) ] }
    graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for start, end, cost in edges:
        graph[start].append((end, cost))
        graph[end].append((start, 2 * cost))
    # Standard Djikstra
    target: int = n - 1
    visited: set[int] = set()
    # [ (cost, node) ]
    que: list[tuple[int, int]] = [(0, 0)]
    heapq.heapify(que)
    max_cost: int = n * 100000
    costs: list[int] = [max_cost for _ in range(n)]
    # 0 - the start
    costs[0] = 0
    
    while que:
        cost, node = heapq.heappop(que)
        if target == node:
            return cost
        if node in visited:
            continue
        visited.add(node)

        for edge, cost_move in graph[node]:
            new_cost: int = cost + cost_move
            if new_cost > costs[edge]:
                continue
            costs[edge] = new_cost
            heapq.heappush(que, (new_cost, edge))

    return -1


# Time complexity: O(n * log n)
# --- --- --- ---
# Space complexity: O(n)


test: int = 4
test_edges: list[list[int]]= [
    [0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]
]
test_out: int = 5
assert test_out == min_cost(test, test_edges)

test = 4
test_edges = [
    [0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 3]
]
test_out = 3
assert test_out == min_cost(test, test_edges)
