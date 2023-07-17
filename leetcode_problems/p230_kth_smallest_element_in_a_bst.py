# Given the root of a binary search tree,
#   and an integer k, return the kth smallest value (1-indexed)
#   of all the values of the nodes in the tree.
# -------------------
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10 ** 4
# 0 <= Node.val <= 10 ** 4
from collections import deque
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode, k: int) -> int:
    # working_sol (59.77%, 97.60%) -> (67ms, 20.29mb)  time: O(n * log n) | space: O(n)
    que: deque[TreeNode] = deque()
    que.append(root)
    # using heap with inverted values
    heap: heapq = []
    heapq.heapify(heap)
    while que:
        current: TreeNode = que.popleft()
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
        if len(heap) != k:
            # inverting all values, so we can pop the highest value
            # -5 < -3 reverse back 5 > 3 <- actually pop() highest
            # * -1 for better visibility
            heapq.heappush(heap, current.val * -1)
            continue
        if (current.val * -1) > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, current.val * -1)
    # there's K elements in a heap, and they sorted from MAX to MIN if inverted back,
    # so we can just take [0](MAX) -> which is smallest in a heap,
    # but we need K element of smallest counted from left to right.
    # So [0] it's actually HIGHEST of SMALLEST, and we have it already sorted.
    return heapq.heappop(heap) * -1


# Time complexity: O(n * log n) -> in the worst case, k == n, for every node of input_BT we will add its value
# n - nodes in input_BT^^| into a heap, heapq.heappop() and heappush() are O(log n), so for every node heappush() =>
#                          => O(n * log n).
# Auxiliary space: O(n) -> in the same worst case, heap will be a size of n, storing every node.val() in it =>
#                          => O(n) -> extra to this que with median size of O(log n).
# -------------------
# Standard reversed heapq with len of K, store everything higher than min_value
# and ignore everything lower than min_value, after we append K elements into a heap.
# -------------------
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
#   and you need to find the kth smallest frequently, how would you optimize?
# -------------------
# Hmm. Are we allowed to store BT? Like if we store K nodes into a heapq with inverted values
# and check if the newly added/updated values are higher than min_value or lower than min_value in it.
# If it's higher than we delete lowest and append new, if it's lower we just ignore it.
# Otherwise, I don't see how we can optimize it, because we need an info about what's in a tree.
# Before we can do something about it.
