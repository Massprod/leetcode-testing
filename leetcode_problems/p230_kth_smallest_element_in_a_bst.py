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
    # working_sol (98.93%, 82.14%) -> (51ms, 20.34mb)  time: O(log n) | space: O(n)
    que: deque[TreeNode] = deque()
    que.append(root)
    # using heap with inverted values
    heap: heapq = []
    heapq.heapify(heap)

    def inorder(node: TreeNode) -> None:
        # Because I'm trying to ignore turns, it's better to do this with in-order than order-level.
        # Still going to take 1 step in most of the right_subtrees but at least not all of them.
        # We have given CORRECT BT, so it's always => node.left.val < node.val < node.right.val
        # If we're not populated heap, we can ADD w.e nodes we met.
        if len(heap) != k:
            heapq.heappush(heap, node.val * -1)
            # Easier to check last added value like this than try to extra_check it below(after).
            if len(heap) == k:
                # Ignore left turn if it's values going to be higher than already met MAX_VALUE(heap[0]).
                # Mostly need to ignore nodes in right subtree of a root.
                if node.left and node.left.val * -1 > heap[0]:
                    inorder(node.left)
                # Ignore right turn with same approach.
                if node.right and node.right.val * -1 > heap[0]:
                    inorder(node.right)
                return
            # If heap isn't populated, we check everything.
            if node.left:
                inorder(node.left)
            if node.right:
                inorder(node.right)
            return
        if len(heap) == k:
            # Only add values lower than MAX_VALUE,
            # all values inverted, so it's HIGHER than LOWEST in a heap
            if (node.val * -1) > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, node.val * -1)
            else:
                return
            # Same approach to make a turn left or right.
            if node.left and node.left.val * -1 > heap[0]:
                inorder(node.left)
            if node.right and node.right.val * -1 > heap[0]:
                inorder(node.right)

    inorder(root)
    # there's K elements in a heap, and they sorted from MAX to MIN if inverted back,
    # so we can just take [0](MAX) -> which is smallest in a heap,
    # but we need K element of smallest counted from left to right.
    # So [0] it's actually HIGHEST of SMALLEST, and we have it already sorted.
    return heapq.heappop(heap) * -1


# Time complexity: O(log n) -> in the worst case, k == n, for every node of input_BT we will add its value,
# n - nodes in input_BT^^| now with extra turn checks part of the nodes with left/right subtree values higher
#                          than MAX_VALUE we already met will be ignored, so it's should be correct =>
#                          => O(log n) + heap operations == O(log n) => O(log n)
# Auxiliary space: O(n) -> in the same worst case, heap will be a size of n, storing every node.val() in it =>
#                          => O(n) -> extra to this, recursion with median size of O(log n).
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
# Ok. Version with in-order is essentially the same, and we're still stepping into a right_subtree.
# But breaking instantly, dunno how to make it ignore first node of a right_subtree while going backwards.
# W.e I'm still focused too much on this, but I made the solution with 98.93%. So it's good practice.
# There's mistake, I don't need min_value because it's duplicate and didn't add anything for (node.val * -1> heap[0]).
