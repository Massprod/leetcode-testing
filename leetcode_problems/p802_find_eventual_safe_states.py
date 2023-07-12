# There is a directed graph of n nodes with each node labeled from 0 to n - 1.
# The graph is represented by a 0-indexed 2D integer array graph where graph[i]
#   is an integer array of nodes adjacent to node i,
#   meaning there is an edge from node i to each node in graph[i].
# A node is a terminal node if there are no outgoing edges.
# A node is a safe node if every possible path starting from that node
#   leads to a terminal node (or another safe node).
# Return an array containing all the safe nodes of the graph.
# The answer should be sorted in ascending order.
# --------------------
# n == graph.length  ,  1 <= n <= 10 ** 4
# 0 <= graph[i].length <= n  ,  0 <= graph[i][j] <= n - 1
# graph[i] is sorted in a strictly increasing order.
# The graph may contain self-loops.
# The number of edges in the graph will be in the range [1, 4 * 10 ** 4].


def eventual_safe_nodes(graph: list[list[int]]) -> list[int] | set[int]:
    # working_sol (92.41%, 84.44%) -> (643ms, 23.7mb)  time: O(n + k) | space: O(n)
    length: int = len(graph)
    # visited nodes, because we're using recursion to cull some calls
    # we're marking them as checked and ignore afterward
    checked: list[bool] = [False for _ in range(length)]
    # nodes on a cycle path
    unsafe: list[bool] = [False for _ in range(length)]

    def check_node(graph_index: int) -> bool:
        # if already checked and found unsafe, ignore
        if unsafe[graph_index]:
            return True
        # if already visited and didn't find it unsafe, ignore
        if checked[graph_index]:
            return False
        # mark as unsafe until found otherwise
        checked[graph_index] = True
        unsafe[graph_index] = True
        # check every edge of the node
        for edge in graph[graph_index]:
            # if node have edges, then we need to check them
            if check_node(edge):
                return True
        # otherwise its TERMINAL node, and we can mark it as SAFE
        unsafe[graph_index] = False
        return False

    for x in range(length):
        check_node(x)
    safe: list[int] = [_ for _ in range(length) if unsafe[_] is False]
    return safe


# Time complexity: O(n + k) -> creating checked and unsafe, both => O(n) + O(n) ->
# n - len of input_graph^^|| -> looping through whole input_graph(array) => O(n) -> recursion will be called for
# k - num of graph_edges^^|| every node only once and edges as well, afterwards insta return  => O(n + k) ->
#                            -> creating new array safe to store all safe nodes => O(n) ->
#                            -> O(n) + O(n) + O(n + k) + O(n) => O(4n + k) => O(n + k).
# Auxiliary space: O(n) -> creating 3 extra arrays of the same size as input_graph => O(3n) ->
#                          -> and making recursion calls for every node, in the worst case every node is connected
#                          like from 0 to n, then recursion stack will be the size of n => O(n).
# --------------------
# Topological sorting problem.
# We can use DFS -> and use checked as a stack to make sure we're not going into cycle and recheck any nodes.
#   In recursion, we're marking every node as checked and unsafe, and after that checking every edge of this node.
#   If there's NO edges, then its Terminal node, and we can mark is as safe. Otherwise, mark of the node stays as
#   unsafe, and every node on backtrack path will be left as unsafe as well.
#   Allows us to mark every node on the way and ignore them afterwards.
# --------------------
# Beat TLE with my solution, by adding backwards track adding into safe nodes from first_path,
#   but it's needs to be sorted afterwards which is not going to work with this TimeLimit.
# Ok. Extra search, there's some part I just don't know how to use faster.
# --------------------
# 93/112 and TLE. Well it's working, but what can we cull?
# Add extra check if X is already in unsafe_nodes which is ignoring recursion call for that,
# and added whole path with a loop into unsafe_nodes, not enough.
# I could extra remember correct path, but then I would need to delete unsafe nodes from it, after we found them.
# It's going to be even slower, or use set for this, but then we need to sort it after...
# --------------------
# !
# The graph may contain self-loops. ! if loops than it's insta_False, cuz it can't have all path leading to terminals.
# Recursion with checking every node in graphs to check every path of this node leading to terminal,
# or having a loop? But what is PATH here?
# Like in first test 0 -> 1 -> 2 -> 5 correct path, but there's another path from 1 which doesn't lead
# to the terminal 1 -> 3 -> 0 it's a loop, and it's incorrect in example.
# So every path STARTING from 0 should be correct even if it SPLITS?
# Because 0 -> 1 is correct path if we consider his continuation as 2 -> 5 but, if we split it
# than it should have both path correct. Only way why it can be False in example.
# So we need to have all SPLITS a.k.a node being safe or terminal.
# Guess loop should be insta False for every node included in it,
# cuz it's one of their ways(splits) leading to a loop.
# No idea about TLE, but if we have 10 ** 4 nodes it's need to be sorted along the way for ->
# -> ! The answer should be sorted in ascending order. ! -> otherwise it's extra slow.


test1 = [[1, 2], [2, 3], [5], [0], [5], [], []]
test1_out = [2, 4, 5, 6]
print(eventual_safe_nodes(test1))
assert test1_out == eventual_safe_nodes(test1)

test2 = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
test2_out = [4]
print(eventual_safe_nodes(test2))
assert test2_out == eventual_safe_nodes(test2)

test3 = [[]]
test3_out = 0
print(eventual_safe_nodes(test3))
assert test3_out == eventual_safe_nodes(test3)
