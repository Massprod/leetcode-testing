# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
#   that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
# -----------------------
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # working_sol (96.42%, 65.33%) -> (103ms, 19mb)  time: O(n + k) | space: O(n)
    graph: list[list[int]] = [[] for _ in range(numCourses)]
    for _ in prerequisites:
        graph[_[0]].append(_[1])
    doable: list[bool] = [True for _ in range(numCourses)]
    checked: list[bool] = [False for _ in range(numCourses)]

    def dfs(node_index: int) -> bool:
        # Ends with a cycle.
        if not doable[node_index]:
            return False
        # Visited.
        if checked[node_index]:
            return True
        # Mark as False, to get cycle.
        doable[node_index] = False
        checked[node_index] = True
        for edge in graph[node_index]:
            if not dfs(edge):
                return False
        # Mark as True, doesn't lead to a cycle.
        doable[node_index] = True
        return True

    for _ in range(numCourses):
        if not dfs(_):
            return False
    return True


# Time complexity: O(n + k) -> creating 3 lists of size n => O(3n) -> looping once through whole graph, once ->
# n == numCourses ^^|  -> and for each index calling recursion which is going to be recalled for every edge
#                         in the graph nodes, number of edges is equal to len(prerequisites) as k ->
#                      -> because every pair in prerequisites always have 1 node, and 1 edge => O(n + k).
# Auxiliary space: O(n) -> 3 extra arrays of size n => O(n).
# -----------------------
# No it's incorrect, we need to actually check if we can do ALL COURSES, and we have always given
# the numCourses which is equal to number of ALL COURSES provided.
# So I can delete extra check and make it little bit faster.
# -----------------------
# Only question is -> what courses we need to ! Return true if you can finish all courses ! finish,
# like is it ALL courses in prerequisites, or we can be given 100+ courses in it,
# but only need to complete 1. Should be correct -> we need to complete only given numCourses.
# -----------------------
# DFS -> because if there's cycle we can't complete course. Repeating of p802.
# Only now we need to create our graph by ourselves, everything else is the same.


test: int = 2
test_pre: list[list[int]] = [[1, 0]]
test_out: bool = True
assert test_out == can_finish(test, test_pre)

test = 2
test_pre = [[1, 0], [0, 1]]
test_out = False
assert test_out == can_finish(test, test_pre)

# test3 -> failed -> Forgot to make check_node() return True in case of a course being doable.
test = 2
test_pre = [[0, 1]]
test_out = True
assert test_out == can_finish(test, test_pre)
