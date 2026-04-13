# You are given a 2D integer array matrix of size n x n representing
#  the adjacency matrix of an undirected graph with n vertices labeled from 0 to n - 1.
#  - matrix[i][j] = 1 indicates that there is an edge between vertices i and j.
#  - matrix[i][j] = 0 indicates that there is no edge between vertices i and j.
# The degree of a vertex is the number of edges connected to it.
# Return an integer array ans of size n where ans[i] represents the degree of vertex i.
# --- --- --- ---
# 1 <= n == matrix.length == matrix[i].length <= 100​​​​​​​
# ​​​​​​​matrix[i][i] == 0
# matrix[i][j] is either 0 or 1
# matrix[i][j] == matrix[j][i]


def find_degrees(matrix: list[list[int]]) -> list[int]:
    # working_solution: (100%, 100%) -> (39ms, 20.48mb)  Time: O(n) Space: O(n)
    # { node: edges }
    graph: dict[int, set[int]] = {
        node: set() for node in range(len(matrix))
    }
    for node in range(len(matrix)):
        for edge in range(len(matrix[node])):
            if 0 == matrix[node][edge]:
                continue
            graph[node].add(edge)
            graph[edge].add(node)

    out: list[int] = [
        len(graph[node]) for node in graph
    ]
    return out


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(n)


test: list[list[int]] = [[0,1 , 1], [1, 0, 1], [1, 1, 0]]
test_out: list[int] = [2, 2, 2]
assert test_out == find_degrees(test)

test = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
test_out = [1, 1, 0]
assert test_out == find_degrees(test)
