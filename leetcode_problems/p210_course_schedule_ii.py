# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi]
#   indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses.
# If there are many valid answers, return any of them.
# If it is impossible to finish all courses, return an empty array.
# -----------------------
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.


def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # working_sol (90.69%, 47.59%) -> (92ms, 19.24mb)  time: O(n + k) | space: O(n + k)
    graph: list[list[int]] = [[] for _ in range(numCourses)]
    for _ in prerequisites:
        graph[_[0]].append(_[1])
    doable: list[bool] = [True for _ in range(numCourses)]
    checked: list[bool] = [False for _ in range(numCourses)]
    all_paths: list[int] = []

    def check_node(node_index: int) -> bool:
        # Cycle.
        if not doable[node_index]:
            return False
        # Already visited.
        if checked[node_index]:
            return True
        # Mark to get cycle.
        doable[node_index] = False
        # Mark as visited.
        checked[node_index] = True
        for edge in graph[node_index]:
            if not check_node(edge):
                return False
        doable[node_index] = True
        # Backtracking to get all DFS paths in reverse.
        # We start from course and traverse through all prerequisite courses.
        all_paths.append(node_index)
        return True

    for course in range(numCourses):
        if not check_node(course):
            return []
    return all_paths


# Time complexity: O(n + k) -> creating array 'graph' with 'n' lists => O(n) -> traversing 'prerequisites' to get
# n - input value 'numCourses'^^| all edge connections => O(n + k) -> DFS to check for cycles and get all paths,
# k - len of input array 'prerequisites' == # of edges^^| which essentially check of all Nodes == 'n' => O(2n + k)
# Auxiliary space: O(n + k) -> 'graph' array with 'n' courses as lists + all edges inside => O(n + k) ->
#                           -> 2 extra arrays with courses marking of size 'n' => O(n + k + 2n) ->
#                           -> recursion stack with max size of 'n' => O(4n + k) ->
#                           -> extra array with all courses in correct order 'all_paths', always size 'n' => O(5n + k).
# -----------------------
# Mistakes before rebuild:
#  I was using DFS to check cycles, and after this used DFS again to check paths.
#  Which we don't need because, we're already using DFS on every path possible and never revisit Nodes again.
#  Because marking them in 'checked', so it could be done with backtracking inside of standard DFS to check cycles.


test: int = 2
test_pre: list[list[int]] = [[1, 0]]
test_out: list[int] = [0, 1]
assert test_out == find_order(test, test_pre)

test = 4
test_pre = [[1, 0], [2, 0], [3, 1], [3, 2]]
test_out = [0, 1, 2, 3]
assert test_out == find_order(test, test_pre)

test = 1
test_pre = []
test_out = [0]
assert test_out == find_order(test, test_pre)

test = 7
test_pre = [[1, 0], [5, 2], [2, 1], [3, 0], [3, 4], [4, 5],  [4, 1]]
test_out = [0, 1, 2, 5, 4, 3, 6]
assert test_out == find_order(test, test_pre)

test = 2
test_pre = [[0, 1]]
test_out = [1, 0]
assert test_out == find_order(test, test_pre)
