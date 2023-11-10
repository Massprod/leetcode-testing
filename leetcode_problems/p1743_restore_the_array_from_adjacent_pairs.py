# There is an integer array nums that consists of n unique elements,
#  but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi]
#  indicates that the elements ui and vi are adjacent in nums.
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1]
#  will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]].
# The pairs can appear in any order.
# Return the original array nums.
# If there are multiple solutions, return any of them.
# -------------------------------
# nums.length == n
# adjacentPairs.length == n - 1
# adjacentPairs[i].length == 2
# 2 <= n <= 10 ** 5
# -10 ** 5 <= nums[i], ui, vi <= 10 ** 5
# There exists some nums that has adjacentPairs as its pairs.
from collections import defaultdict


def restore_array(adjacentPairs: list[list[int]]) -> list[int]:
    # working_sol (97.78%, 87.10%) -> (852ms, 65mb)  time: O(n) | space: O(n)
    # We're given 2 options:
    # [nums[i], nums[i+1]] or [nums[i+1], nums[i]]
    # And we can't distinguish them == undirected graph.
    # (node: [neighbours])
    graph: dict[int, list[int]] = defaultdict(list)
    for start, end in adjacentPairs:
        graph[start].append(end)
        graph[end].append(start)
    # We can have correct array with 2 ways:
    # start -> end | end -> start
    out_arr: list[int] = []
    for _node in graph:
        # And start|end of correct array is always used Once in 'adjacentPairs'.
        # Because they have only 1 neighbour.
        if len(graph[_node]) == 1:
            out_arr = [_node, graph[_node][0]]
            break
    # We're given that size of correct_array is 'n' and size of 'adjacentPairs' is 'n - 1'.
    # So, we need array with +1 element higher.
    # Iterative DFS.
    while len(out_arr) <= len(adjacentPairs):
        # Nodes in graph have 2 neighbours (except start and end Nodes).
        neighbour1: int = graph[out_arr[-1]][0]
        neighbour2: int = graph[out_arr[-1]][1]
        previous: int = out_arr[-2]
        # Instead of visited, we can just ignore one of the current Node neighbours.
        # Because we came into this Node from one of them.
        if neighbour1 == previous:
            out_arr.append(neighbour2)
        else:
            out_arr.append(neighbour1)
    return out_arr


# Time complexity: O(n) -> creating undirected graph with all Nodes from 'adjacentPairs' => O(n) ->
# n - len of input array 'adjacentPairs'^^| -> worst case == start|end Nodes are in the end of graph ->
#                                           -> we will traverse whole dictionary to get it => O(n) ->
#                                           -> iterative DFS on all of them Nodes => O(n).
# Auxiliary space: O(n) -> undirected graph 'graph' with all unique values from 'adjacentPairs' as Nodes,
#                          and every Node have 2 neighbours except start and end ->
#                          -> so, number of Nodes will depend on input 'adjacentPairs', but neighbours dont => O(n) ->
#                          -> extra 'out_arr' with all unique_values(Nodes) from 'adjacentPairs' => O(n + (n + 1)).
# -------------------------------
# Well it's 100% undirected graph with DFS.
# Only question is when to start dfs?
# Like we either can start from anything and find path with 'n' elements.
# Or we need to find correct start or end, can we?
# Yeah, we can't use test case like [[1, 2], [2, 1]].
# So start or end will always be used only once.
# Count every Node occurrence and start dfs from node with 1 encounter.
# Should be correct.
# All correct, but slow. Top solutions doing it iteratively, which is not actually better but less memory consuming.
# Rebuild with iterative.


test: list[list[int]] = [[2, 1], [3, 4], [3, 2]]
test_out: list[int] = [1, 2, 3, 4]
assert test_out == restore_array(test)

test = [[4, -2], [1, 4], [-3, 1]]
test_out = [-2, 4, 1, -3]
assert test_out == restore_array(test)

test = [[100000, -100000]]
test_out = [100000, -100000]
assert test_out == restore_array(test)
