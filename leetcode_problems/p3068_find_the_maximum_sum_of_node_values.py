# There exists an undirected tree with n nodes numbered 0 to n - 1.
# You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi]
#  indicates that there is an edge between nodes ui and vi in the tree.
# You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n,
#  where nums[i] represents the value of the node numbered i.
# Alice wants the sum of values of tree nodes to be maximum,
#  for which Alice can perform the following operation any number of times (including zero) on the tree:
#  - Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
#  - nums[u] = nums[u] XOR k
#  - nums[v] = nums[v] XOR k
# Return the maximum possible sum of the values Alice can achieve
#  by performing the operation any number of times.
# -------------------------
# 2 <= n == nums.length <= 2 * 10 ** 4
# 1 <= k <= 10 ** 9
# 0 <= nums[i] <= 10 ** 9
# edges.length == n - 1
# edges[i].length == 2
# 0 <= edges[i][0], edges[i][1] <= n - 1
# The input is generated such that edges represent a valid tree.
from functools import cache


def maximum_value_sum(nums: list[int], k: int, edges: list[list[int]]) -> int:
    # working_sol (13.64%, 5.11%) -> (1148ms, 45.5mb)  time: O(n) | space: O(n)

    @cache
    def check(node: int, even_odd: int) -> int | float:
        # 0 - odd, 1 - even
        if node >= len(nums):
            if 0 == even_odd:
                return float('-inf')
            return 0
        # Only 2 options we can have.
        we_xor: int = nums[node] ^ k
        we_dont: int = nums[node]
        best_option: int = max(
            we_xor + check(node + 1, even_odd ^ 1),
            we_dont + check(node + 1, even_odd)
        )
        return best_option
    # start with 0 XOR operations == even.
    return check(0, 1)


# Time complexity: O(n) <- n - length of an input array `nums`.
# We're always traversing whole `nums` twice, with both options => O(2n).
# -------------------------
# Auxiliary space: O(n)
# We're using `cache` to store all the call results, and there's `2n` calls => O(2n).
# Also, stack of the recursion is at max == `n` => O(3n).
# -------------------------
# The Main thing to use here is that, if we do (num1 XOR k XOR k) <- we will always restore the original value.
# 0 0 1 ^ 1 1 1 == 1 1 0 ^ 1 1 1 == 0 0 1 <- because we will annul `1` and restore it after the second XOR.
# So, w.e the path we will choose, we're always needed to consider only 2 connected Nodes.
# And we're given `edges` which represent all the connected Nodes in pairs.
# We can take smth like:
#        Node2 -> Node4
#      /
# Node1
#      \
#        Node3 -> Node5
# If we XOR `edge(Node1, Node2)`, and then XOR `edge(Node2, Node4)` Node2 will be restored.
# So, we can just take any Node and use (XOR k) on it or not, and choose maximum from both.
# But we should only consider cases when we used EVEN number of XOR operations, because we're given pairs.
# So, if we see it from using `edges,` we're always going to use EVEN number of values.


test: list[int] = [1, 2, 1]
test_k: int = 3
test_edges: list[list[int]] = [[0, 1], [0, 2]]
test_out: int = 6
assert test_out == maximum_value_sum(test, test_k, test_edges)

test = [2, 3]
test_k = 7
test_edges = [[0, 1]]
test_out = 9
assert test_out == maximum_value_sum(test, test_k, test_edges)

test = [7, 7, 7, 7, 7, 7]
test_k = 3
test_edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
test_out = 42
assert test_out == maximum_value_sum(test, test_k, test_edges)
