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
    # working_sol (96.78%, 5.10%) -> (104ms, 20.21mb)  time: O(n + k) | space: O(n + k)
    graph: list[list[int]] = [[] for _ in range(numCourses)]
    for _ in prerequisites:
        graph[_[0]].append(_[1])
    doable: list[bool] = [True for _ in range(numCourses)]
    checked: list[bool] = [False for _ in range(numCourses)]
    all_paths: dict[int, list[int]] = {}
    for _ in range(numCourses):
        all_paths[_] = []

    def check_node(node_index: int) -> bool:
        # if already checked and marked
        if not doable[node_index]:
            return False
        # if visited, ignore
        if checked[node_index]:
            return True
        # marks, until proven otherwise
        doable[node_index] = False
        checked[node_index] = True
        # if edges, check them
        for edge in graph[node_index]:
            # append every edge we meet until hitting terminal
            # and assign them to their start_node(course they needed_first)
            # like 1 <- 3 <- 0, 1 <- 4 <- 0 =>
            #   => 1: (3, 4) | 4: (0) | 3: (0)
            all_paths[node_index].append(edge)
            if not check_node(edge):
                return False
        # if no edges, doable
        doable[node_index] = True
        return True

    for _ in range(numCourses):
        if not check_node(_):
            return []
    # courses already put in order
    already_done: set[int] = set()
    # correct order to take all courses
    order: list[int] = []

    def backtrack(start: int) -> None:
        # walk through all nodes stored in dict,
        # and record path from them to their Terminal node, backwards
        for _ in all_paths[start]:
            if _ not in already_done:
                backtrack(_)
        if start not in already_done:
            order.append(start)
            already_done.add(start)

    # check every path for a nodes, except Terminals
    for _ in range(numCourses):
        # and append them only once
        if len(all_paths[_]) == 0 and _ not in already_done:
            order.append(_)
            already_done.add(_)
        if _ not in already_done:
            backtrack(_)
    return order


# Time complexity: O(n + k) -> creating 3 arrays with size of n, and populating one with same indexes used => O(4n) ->
# k - len(prerequisites)^^|-> for each index in graph or just plain numCourses their equal, calling recursion
# n - num of courses^^|    which is going to be recalled for every edge in the graph nodes, number of which is
#                          equal to k == len(prerequisites) => O(n + k) ->
#                          -> after that for every node in a graph checking their path to be completed,
#                          because we already recorded every node path from its node to the Terminal we can,
#                          just walk this path backwards and record every node in this order ->
#                          -> this walk will use every node, and it's edges once again => O(n + k).
# Auxiliary space: O(n + k) -> 2 extra arrays of size n => 2O(n) -> extra array of size n with lists inside, each list
#                          having a size of edges to its node, if summarized they will be equal to k => O(n + k) ->
#                          -> extra dictionary to store all nodes and their edges as values => O(n + k) ->
#                          -> extra set of size n, storing every possible node => O(n) ->
#                          -> extra list of size n, we're storing all unique nodes in correct order in it => O(n) ->
#                          -> in the worst case, we're having courses like 0 -> 1 -> 2 -> 3 -> 4 -> 5 etc.
#                          like every node is linked, then our recursion stack for DFS(check_node) will be O(n),
#                          every node is stored => O(n) -> same goes to a backtrack() we just do 1 walk with
#                          every node included => O(n) -> O(n + k).
# -----------------------
# Made it a x5 faster, by culling extra backtrack_calls.
# First commit was just a testing of work, I was lucky to not get TLE otherwise I would be focused on it and
# might miss that there's 3 places where backtrack() was extra called.
# Now it's good speed with 60%+ performance, but memory is meh.
# For the first time encounter with Topological_sort it's still fine.
# -----------------------
# So we're just using DFS to get data about cycles and if there's one, insta return with empty_array.
# But if there's correct paths we're recording every possible path from checked_nodes.
# In a path I included every course(node) we need to complete BEFORE we can do checked_course.
# After that, using Backtrack to walk for a path of all required courses for current_course we want to append,
# and after tracking down the node with NO requirement(terminal) we can add this whole path backwards into order array.
# For the cases with terminal nodes, we're just appending them Once and forgetting.
# ^^Because their placement is irrelevant.
# -----------------------
# Doing this by intuition first, and learn about Topological_sorting in a more bookish style after.
#    Hints marking this problem as a Topological_sort^^|


test1 = 2
test1_pre = [[1, 0]]
test1_out = [0, 1]
print(find_order(test1, test1_pre), "\n")
assert test1_out == find_order(test1, test1_pre)

test2 = 4
test2_pre = [[1, 0], [2, 0], [3, 1], [3, 2]]
test2_out = [0, 1, 2, 3]
print(find_order(test2, test2_pre), "\n")
assert test2_out == find_order(test2, test2_pre)

test3 = 1
test3_pre = []
test3_out = [0]
print(find_order(test3, test3_pre), "\n")
assert test3_out == find_order(test3, test3_pre)

test4 = 7
test4_pre = [[1, 0], [5, 2], [2, 1], [3, 0], [3, 4], [4, 5],  [4, 1]]
test4_out = [0, 1, 2, 5, 4, 3, 6]
print(find_order(test4, test4_pre), "\n")
assert test4_out == find_order(test4, test4_pre)

# test5 -> failed -> forgot to extra check if we already completed course taken from keys with len == 0.
#                    Because this is courses we can add no matter the time, they don't require anything.
#                    And they were repeated, without this check.
test5 = 2
test5_pre = [[0, 1]]
test5_out = [1, 0]
print(find_order(test5, test5_pre))
assert test5_out == find_order(test5, test5_pre)
