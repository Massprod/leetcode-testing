# There are a total of numCourses courses you have to take,
#  labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
#  that you must take course ai first if you want to take course bi.
# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b,
#  and course b is a prerequisite of course c, then course a is a prerequisite of course c.
# You are also given an array queries where queries[j] = [uj, vj].
# For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
# Return a boolean array answer, where answer[j] is the answer to the jth query.
# --------------------------
# 2 <= numCourses <= 100
# 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
# prerequisites[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# All the pairs [ai, bi] are unique.
# The prerequisites graph has no cycles.
# 1 <= queries.length <= 10 ** 4
# 0 <= ui, vi <= n - 1
# ui != vi
from collections import defaultdict, deque


def check_if_prerequisite(numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    # working_sol (74.22%, 94.15%) -> (599ms, 20.09mb)  time: O(n + m + numCourses * numCourses)
    #                                                    space: O(n + m + numCourses * numCourses)
    # {Node: edges}
    graph: dict[int, list[int]] = defaultdict(list)
    for start, end in prerequisites:
        graph[start].append(end)
    # row = course number, column = course who needs this (row=course) to be completed before it.
    reachable: list[list[bool]] = [[False for _ in range(numCourses)] for _ in range(numCourses)]
    # Standard BFS, to get all connections.
    for course in range(numCourses):
        que: deque[int] = deque([course])
        visited: set[int] = {course}
        while que:
            cur_node: int = que.popleft()
            if cur_node in graph:
                for edge in graph[cur_node]:
                    if edge not in visited:
                        reachable[course][edge] = True
                        que.append(edge)
                        visited.add(edge)
    out: list[bool] = []
    for prerequisite, course in queries:
        out.append(reachable[prerequisite][course])
    return out


# Time complexity: O(n + m + numCourses * numCourses) <- m - length of input array `prerequisites`,
#                                                        n - length of input array `queries`.
# Creating graph with all presented connections => O(m).
# Creating matrix with all courses as rows and their connections as columns => O(numCourses * numCourses).
# Worst case: if all Nodes connected like 0 -> 1 -> 2 -> 3 -> 4 ... numCourses - 1.
# So, we will start BFS from 0 and check all Nodes, then 1 and check (all - 1) etc. => O(numCourses * numCourses).
# Extra traversing whole `queries` => O(n).
# O(n + m + 2 * numCourses * numCourses)
# --------------------------
# Auxiliary space: O(n + m + numCourses * numCourses).
# If all pair of `prerequisites` are unique, then we can (m == pairs) like: (uniqueNode: edge) => O(m) for `graph`.
# Creating matrix `reachable` always with same size == numCourses * numCourses => O(numCourses * numCourses).
# Same worst case, then we need to allocate `numCourses` for `visited` => O(numCourses).
# Extra list `out` always with size == n => O(n).


test: int = 2
test_prerequisites: list[list[int]] = [[1, 0]]
test_queries: list[list[int]] = [[0, 1], [1, 0]]
test_out: list[bool] = [False, True]
assert test_out == check_if_prerequisite(test, test_prerequisites, test_queries)

test = 2
test_prerequisites = []
test_queries = [[1, 0], [0, 1]]
test_out = [False, False]
assert test_out == check_if_prerequisite(test, test_prerequisites, test_queries)

test = 3
test_prerequisites = [[1, 2], [1, 0], [2, 0]]
test_queries = [[1, 0], [1, 2]]
test_out = [True, True]
assert test_out == check_if_prerequisite(test, test_prerequisites, test_queries)
