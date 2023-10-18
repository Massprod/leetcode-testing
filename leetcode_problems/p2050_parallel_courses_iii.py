# You are given an integer n, which indicates that there are n courses labeled from 1 to n.
# You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej]
#  denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship).
# Furthermore, you are given a 0-indexed integer array time where time[i] denotes
#  how many months it takes to complete the (i+1)th course.
# You must find the minimum number of months needed to complete all the courses following these rules:
#  - You may start taking a course at any time if the prerequisites are met.
#  - Any number of courses can be taken at the same time.
# Return the minimum number of months needed to complete all the courses.
# Note: The test cases are generated such that it is possible to complete every course
# (i.e., the graph is a directed acyclic graph).
# ----------------------
# 1 <= n <= 5 * 10 ** 4
# 0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10 ** 4)
# relations[j].length == 2
# 1 <= prevCoursej, nextCoursej <= n
# prevCoursej != nextCoursej
# All the pairs [prevCoursej, nextCoursej] are unique.
# time.length == n
# 1 <= time[i] <= 10 ** 4
# The given graph is a directed acyclic graph.


def minimum_time(n: int, relations: list[list[int]], time: list[int]) -> int:
    # working_sol (83.53%, 21.77%) -> (1403ms, 80mb)  time: O(n) | space: O(n)
    # Essentially we need LONGEST(by time) path in the graph.
    # Because we can travel all of them simultaneously:
    #  ! Any number of courses can be taken at the same time !
    # We can have multiple Nodes point to the same, no reasons to recalculate DFS.
    dfs_cache: dict[int, int] = {}
    acyc_graph: dict[int, list[int]] = {}
    for start, end in relations:
        if start in acyc_graph:
            acyc_graph[start].append(end)
        else:
            acyc_graph[start] = [end]

    def dfs(cur_node: int) -> int:
        if cur_node in dfs_cache:
            return dfs_cache[cur_node]
        # Node leads to nothing => last Node we need to visit.
        if cur_node not in acyc_graph:
            # ! time[i] denotes how many months
            #   it takes to complete the (i+1)th course !
            # It's 0-indexed, and Nodes are 1-indexed.
            return time[cur_node - 1]
        cur_path: int = 0
        for edge in acyc_graph[cur_node]:
            cur_path = max(cur_path, dfs(edge))
        # Time we need to complete Node(course) itself.
        cur_path += time[cur_node - 1]
        dfs_cache[cur_node] = cur_path
        return cur_path

    path_time: int = 0
    # ! n courses labeled from 1 to n !
    for node in range(1, n + 1):
        path_time = max(path_time, dfs(node))
    return path_time


# Time complexity: O(n) -> ! 1 <= n <= 5 * 10 ** 4 and 'relations' max_len == 5 * 10 ** 4 ! == O(n-1) to build graph ->
# n - number of Nodes^^| -> and after we build graph, we're always using DFS on ALL the Nodes ->
#                        -> because cache is used, we will always check every Node and paths only once => O(2n).
# Auxiliary space: O(n) -> worst case == everything is connected in a line except last node ->
#                        -> we will store (n - 1) Nodes as starts in 'acyc_graph' dict => O(n - 1) ->
#                        -> because last node is always insta return we're not caching it ->
#                        -> extra dict 'dfs_cache' with same (n - 1) Nodes stored => O(n - 1) ->
#                        -> extra recursion stack with max_size == n, because we can graph like linked_list => O(3n).
# ----------------------
# Tags: DP, Graph, Topological Sort.
# Hmm, can't we just DFS it?
# Because what we essentially want is the LONGEST(by time not # of Nodes) path in a graph.
# We need ALL courses to be complete, and we can make them simultaneously.
# So if we start some path we can complete only in its own time, but every other path can be done without it.
# And because we need ALL, it's always LONGEST path we can travel with DFS.
# Extra we're given -> ! The given graph is a directed acyclic graph ! <- there's no cycles.
# No cycles, we need longest, and we have all starting points == 1 -> n.
# Should be correct to just DFS from every node like find Maximum sum_path in BT before.
# Let's try DFS and check topological sort later.


test_n: int = 3
test_rel: list[list[int]] = [[1, 3], [2, 3]]
test_time: list[int] = [3, 2, 5]
test_out: int = 8
assert test_out == minimum_time(test_n, test_rel, test_time)

test_n = 5
test_rel = [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]]
test_time = [1, 2, 3, 4, 5]
test_out = 12
assert test_out == minimum_time(test_n, test_rel, test_time)
