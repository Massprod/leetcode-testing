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
    # working_sol (73.81%, 97.60%) -> (64ms, 20.29mb)  time: O(2log n) | space: O(n)
    que: deque[TreeNode] = deque()
    que.append(root)
    # using heap with inverted values
    heap: heapq = []
    heapq.heapify(heap)
    min_value: int | None = None
    while que:
        current: TreeNode = que.popleft()
        if len(heap) != k:
            # inverting all values, so we can pop the highest value
            # -5 < -3 reverse back 5 > 3 <- actually pop() highest
            # * -1 for better visibility
            heapq.heappush(heap, current.val * -1)
            if min_value is None:
                min_value = current.val * -1
            min_value = max(min_value, current.val * -1)
            # ignore left/right subtrees if their values higher than min_value and heap is already K
            # or add left/right subtrees if their values lower than highest(heap[0]) met before ->
            # -> otherwise we can miss cases like 3 - 1 - 2,  after 1 we won't take turn to 2.
            # Added it as extra check here, cuz we don't need to pop() element lastly added into a heap,
            # but we already need to decide if we're taking turns or not. Because heap is full.
            if len(heap) == k:
                if current.left and (current.left.val * -1 > min_value or current.left.val * - 1 > heap[0]):
                    que.append(current.left)
                if current.right and (current.right.val * -1 > min_value or current.right.val * -1 > heap[0]):
                    que.append(current.right)
                continue
        if len(heap) == k:
            if (current.val * -1) > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, current.val * -1)
                min_value = max(min_value, current.val * -1)
            if current.left and (current.left.val * -1 > min_value or current.left.val * - 1 > heap[0]):
                que.append(current.left)
            if current.right and (current.right.val * -1 > min_value or current.right.val * -1 > heap[0]):
                que.append(current.right)
        else:
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
    # there's K elements in a heap, and they sorted from MAX to MIN if inverted back,
    # so we can just take [0](MAX) -> which is smallest in a heap,
    # but we need K element of smallest counted from left to right.
    # So [0] it's actually HIGHEST of SMALLEST, and we have it already sorted.
    return heapq.heappop(heap) * -1


# Time complexity: O(2log n) -> in the worst case, k == n, for every node of input_BT we will add its value,
# n - nodes in input_BT^^| now with extra checks part of the nodes with right_subtree values higher than node on
#                          which we decide to take turn will be ignored, so it's =>
#                          => O(log n) + heap operations == O(log n) => O(log n)
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
# -------------------
# After failing to create random values BT, I see that we have given CORRECT BT.
# So every right subtree of a node is going to have only higher values than node, and
# left is smaller. So we can actually optimize it, to not check every node in a BT.
# Added extra check on where to turn -> [100,75,150,73,88, 140, 175, 65, 74, 87, 95,135, 144, 174, 180, 60], k = 3 ->
# -> don't building trees myself, but for this test_case on Leetcode.
# With this turn addition now it's should PARTLY IGNORE right_subtree of the ROOT.
# Guess it's need to be done with IN-ORDER because, we're extra checking nodes on each level when we know
# that left subtree is always lower, and we can just ignore right_subtree until we're done with left.
# Rebuild then.
