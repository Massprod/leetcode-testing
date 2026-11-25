# You are given an integer n and a directed graph with n nodes labeled from 0 to n - 1.
# The graph is represented by a 2D array edges, where edges[i] = [ui, vi, delayi]
#  indicates an edge from node ui to vi along which a signal takes delayi units of time to arrive.
# Node u is an incoming neighbor of node v if there is an edge from u to v.
# Node 0 is active at time 0, and all other nodes are initially inactive.
# When a node becomes active at time t, it immediately sends one signal
#  along each of its outgoing edges.
# Once active, a node remains active and does not send its signals again.
# A signal sent along an edge with delay d arrives at time t + d.
# You are also given an integer array requiredSignals of length n,
#  where requiredSignals[i] is the number of distinct incoming neighbors of node i
#  from which a signal must arrive before node i can activate.
# An inactive node i becomes active at the earliest time t at which signals
#  have arrived from at least requiredSignals[i] distinct incoming neighbors.
# Return an array ans of length n where ans[i] is the earliest time node i becomes active.
# If node i never becomes active, ans[i] should be -1.
# Note: The value of requiredSignals[0] is irrelevant, since node 0 is active at time 0
#  and sends its outgoing signals at that time.
# --- --- --- ---
# 2 <= n == requiredSignals.length <= 10 ** 5
# 0 <= edges.length <= 10 ** 5
# edges[i] = [ui, vi, delayi]
# 0 <= ui, vi <= n - 1
# ui != vi
# 1 <= delayi <= 10 ** 9
# There is at most one directed edge from any node ui to any node vi.
# 1 <= requiredSignals[i] <= n - 1
import heapq
from collections import defaultdict


def earliest_activation_times(
    n: int,
    edges: list[list[int]],
    requiredSignals: list[int],
) -> list[int]:
    # working_solution: (80.69%, 92.99%) -> (482ms, 74.21mb)  Time: O(n + e * log e) Space: O(n + e)
    # { node: [(edge, delay)]}
    graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for node, edge, delay in edges:
        graph[node].append(
            (edge, delay)
        )
    out: list[int] = [-1 for _ in range(n)]
    arrivals: list[int] = [0 for _ in range(n)]
    # Because we ignore [0] we need to start with it's edges
    out[0] = 0
    # [(time, node)]
    que: list[tuple[int, int]] = [
        (delay, edge)
        for edge, delay in graph[0]
    ]
    heapq.heapify(que)
    while que:
        time, node = heapq.heappop(que)
        if -1 != out[node]:
            continue
        arrivals[node] += 1
        # Not activated yet
        if arrivals[node] < requiredSignals[node]:
            continue
        # Activates
        out[node] = time
        for edge, delay in graph[node]:
            # Already activated == earlier time
            if -1 != out[edge]:
                continue
            heapq.heappush(
                que, (time + delay, edge)
            )
    
    return out


# Time complexity: O(n + e * log e)
# n - number of nodes
# e - number of edges
# --- --- --- ---
# Space complexity: O(n + e)


test_n: int = 3
test_edges: list[list[int]] = [
    [0, 1, 1], [0, 2, 1]
]
test_required_signals: list[int] = [1, 1, 2]
test_out: list[int] = [0, 1, -1]
assert test_out == earliest_activation_times(test_n, test_edges, test_required_signals)

test_n = 4
test_edges = [
    [0, 1, 1], [0, 2, 1], [1, 3, 2], [2, 3, 2]
]
test_required_signals = [3, 1, 1, 2]
test_out = [0, 1, 1, 3]
assert test_out == earliest_activation_times(test_n, test_edges, test_required_signals)

test_n = 4
test_edges = [
    [0, 1, 2], [1, 2, 3], [0, 2, 5], [2, 3, 1]
]
test_required_signals = [3, 1, 2, 1]
test_out = [0, 2, 5, 6]
assert test_out == earliest_activation_times(test_n, test_edges, test_required_signals)

test_n = 4
test_edges = [
    [0, 1, 2], [1, 0, 1], [1, 2, 1], [2, 3, 1], [3, 2, 1]
]
test_required_signals = [3, 1, 2, 1]
test_out = [0, 2, -1, -1]
assert test_out == earliest_activation_times(test_n, test_edges, test_required_signals)
