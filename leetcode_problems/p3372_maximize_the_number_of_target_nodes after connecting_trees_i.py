# There exist two undirected trees with n and m nodes,
#  with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1,
#  respectively, where edges1[i] = [ai, bi] indicates that there is an edge between
#  nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates
#  that there is an edge between nodes ui and vi in the second tree.
# You are also given an integer k.
# Node u is target to node v if the number of edges on the path from u to v
#  is less than or equal to k. Note that a node is always target to itself.
# Return an array of n integers answer, where answer[i]
#  is the maximum possible number of nodes target to node i of the first tree
#  if you have to connect one node from the first tree to another node in the second tree.
# Note that queries are independent from each other.
# That is, for every query you will remove the added edge
#  before proceeding to the next query.
# ------------------------------
# 2 <= n, m <= 1000
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.
# 0 <= k <= 1000
from collections import deque, defaultdict


def max_target_nodes(
        edges1: list[list[int]], edges2: list[list[int]], k: int,
) -> list[int]:
    # working_sol (77.95%, 71.65%) -> (1537ms, 18.62mb)  time: O(m ** 2 + n ** 2) | space: O(n + m)
    # Essentially we need to count all the nodes we can reach starting
    #  from every node in the first tree `edges1`.
    # Because we can connect second tree on any position,
    #  we can just find the longest path from every node of the second tree.
    # And combine these paths together later == maximum number of nodes we can reach.
    # So, BFS from each node in the first/second tree and distance limit == k.
    # Summ the longest path in the second tree with paths of the nodes in the first tree.
    
    def bfs_count(start: int, graph: dict[int, list[int]], limit: int) -> int:
        '''
        Counts maximum number of nodes we can reach in the provided `graph`,
        starting from the `start` node.
        With `limit` number of edges to visit on the path to each node we trying to visit.
        '''
        # We can only use one node to connect.
        if 0 == limit:
            return 1
        level: int = 0
        # We need distance == count how many steps we made.
        # None == new level == new step.
        que: deque[int | None] = deque([start, None])
        # No need for extra counter, every `node` we visit == target.
        # Because we can reach it, and it's in the same graph.
        visited: set[int] = {start}
        while que:
            node: int | None = que.popleft()
            if node is None:
                level += 1
                # Over the limit == we don't need more.
                if level >= limit:
                    break
                # Still have something to check.
                if que:
                    que.append(None)
                    continue
                # Nothing to check.
                break
            # Check every edge and count it.
            for edge in graph[node]:
                if edge in visited:
                    continue
                que.append(edge)
                visited.add(edge)

        return len(visited)
    
    tree1_graph: dict[int, list[int]] = defaultdict(list)
    for start, end in edges1:
        tree1_graph[start].append(end)
        tree1_graph[end].append(start)
    # We need particular order, failed 1st submit on this :)
    # ! where answer[i] is the maximum possible number of nodes target to node i !
    out: list[int] = [1 for _ in tree1_graph]
    # We can't connect it with anything.
    # Only node itself is going to be a target.
    if 0 == k:
        return out
    
    tree2_graph: dict[int, list[int]] = defaultdict(list)
    for start, end in edges2:
        tree2_graph[start].append(end)
        tree2_graph[end].append(start)
    max_tree2_path: int = 0
    # If we can visit every node of the graph, there's no reason to check.
    # And if limit is higher => we can visit everything.
    if (k - 1) > len(tree2_graph):
        max_tree2_path = len(tree2_graph)
    else:
        for node in tree2_graph:
            # `k - 1` <- because we need to connect this `node`
            #  with the starting node of the first tree.
            max_tree2_path = max(
                max_tree2_path, bfs_count(node, tree2_graph, k - 1)
            )
    # Difference with the first tree, that we don't need to remove connection node.
    if k >= len(tree1_graph):
        for node in tree1_graph:
            out[node] = max_tree2_path + len(tree1_graph)
    else:
        # After we get maximum possible path we can have in the second tree.
        # All we need is to connect this with every path we start
        #  from each node of the first tree.
        for node in tree1_graph:
            out[node] = max_tree2_path + bfs_count(node, tree1_graph, k)

    return out


# Time complexity: O(m ** 2 + n ** 2) <- m - number of the nodes in the first tree,
#                                        n - number of the nodes in the second tree.
# In the worst case `k` is going to be equal than a second tree size.
# We're going to traverse full second tree for each node of it => O(n * n).
# In the worst case `k` is going to be lower than a first tree size.
# We're going to traverse it as well => O(m ** 2 + n ** 2).
# ------------------------------
# Auxiliary space: O(m + n).
# `tree1_graph` <- allocates space for each node of the first tree => O(m).
# `tree2_graph` <- allocates space for each node of the second tree => O(n + m).
# Every call of the `bfs_count`, allocates space for:
# `visited` <- allocates space for each node of the provided graph => O(n + m + max(n, m)).
# `que` <- allocates space for each node of the provided graph => O(n + m + 2 * max(n, m)).


test_edges1: list[list[int]] = [[0, 1], [0, 2], [2, 3], [2, 4]]
test_edges2: list[list[int]] = [[0, 1], [0, 2], [0, 3], [2,7], [1, 4], [4, 5], [4, 6]]
test_k: int = 2
test_out: list[int] = [9, 7, 9, 8, 8]
assert test_out == max_target_nodes(test_edges1, test_edges2, test_k)

test_edges1 = [[0, 1], [0, 2], [0, 3], [0, 4]]
test_edges2 = [[0, 1], [1, 2], [2, 3]]
test_k = 1
test_out = [6, 3, 3, 3, 3]
assert test_out == max_target_nodes(test_edges1, test_edges2, test_k)
