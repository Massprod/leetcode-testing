# You are given an integer n. There is an undirected graph with n vertices,
#  numbered from 0 to n - 1.
# You are given a 2D integer array edges where edges[i] = [ai, bi] denotes
#  that there exists an undirected edge connecting vertices ai and bi.
# Return the number of complete connected components of the graph.
# A connected component is a subgraph of a graph in which there exists a path
#  between any two vertices, and no vertex of the subgraph shares
#  an edge with a vertex outside of the subgraph.
# A connected component is said to be complete if there exists
#  an edge between every pair of its vertices.
# ------------------------
# 1 <= n <= 50
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated edges.
from collections import deque


def count_complete_components(n: int, edges: list[list[int]]) -> int:
    # working_sol (27.34%, 16.83%) -> (72ms, 18.52mb)  time: O(n + k) | space: O(n + k)
    # All we actually care it's how many DFS | BFS we can complete.
    # Because, we need a fully connected components.
    # So, just start BFS | DFS from all we can, and if start node is not yet visited
    #  count it's edges and visited nodes for a full connection:
    # n * (n - 1) // 2
    # --- ---
    # DFS should be faster, because we wouldn't need `visited_edges`.
    # Every DFS step == new edge. But, I started with BFS => make it work first.
    out: int = 0
    # { node: [edges] }
    graph: dict[int, list[int]] = {
        node: [] for node in range(n)
    }
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    def bfs_check(
        node: int,
        visited_nodes: set[int],
        visited_edges: set[tuple[int, int]],
    ) -> int:
        if node in visited_nodes:
            return 0
        que: deque[int] = deque([node])
        visited_nodes.add(node)
        component_nodes: int = 1
        used_edges: int = 0
        while que:
            cur_node: int = que.popleft()
            for edge in graph[cur_node]:
                # Standard pair.
                edge_pair: tuple[int, int] = (cur_node, edge)
                # Reversed pair.
                r_edge_pair: tuple[int, int] = (edge, cur_node)
                if (edge_pair not in visited_edges
                    and r_edge_pair not in visited_edges):
                    used_edges += 1
                    visited_edges.add(edge_pair)
                    visited_edges.add(r_edge_pair)
                if edge in visited_nodes:
                    continue
                component_nodes += 1
                que.append(edge)
                visited_nodes.add(edge)
        
        # Component are fully connected if =>  n *(n - 1) // 2 <- n - # of nodes
        fully_connected: int = component_nodes * (component_nodes - 1) // 2
        return fully_connected == used_edges
        
    visited: set[int] = set()
    for start_node in graph:
        out += bfs_check(start_node, visited, set())
    
    return out


# Time complexity: O(n + k) <- n - input value `n`.
#                              k - length of the input array `edges`.
# Building graph with `n` keys, and traversing `edges` to assign them => O(n + k).
# BFS -> starting from each unique node and check every edges of the graph => O(2 * (n + k)).
# ------------------------
# Auxiliary space: O(n + k)
# `graph` <- allocates space for each `edge` from `edges` and `n` nodes => O(n + k).
# `visited` <- allocates space for each `node` we check => O(2 * n + k).
# In the worst case, we only get 1 component and it's fully connected.
# `visited_edges` <- allocates space for each `edge` => O(2 * n + 2 * k).


test: int = 6
test_edges: list[list[int]] = [[0, 1], [0, 2], [1, 2], [3, 4]]
test_out: int = 3
assert test_out == count_complete_components(test, test_edges)

test = 6
test_edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
test_out = 1
assert test_out == count_complete_components(test, test_edges)
