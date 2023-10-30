# Given the root of a binary search tree,
#   and an integer k, return the kth smallest value (1-indexed)
#   of all the values of the nodes in the tree.
# -------------------
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10 ** 4
# 0 <= Node.val <= 10 ** 4
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode, k: int) -> int:
    # working_sol (88.1%, 82.14%) -> (47ms, 20.34mb)  time: O(n * log k) | space: O(n)
    # Using MAX heapq.
    heap: heapq = []
    heapq.heapify(heap)

    def search(node: TreeNode) -> None:
        # We have given CORRECT BT, so it's always => node.left.val < node.val < node.right.val
        # If we're not populated heap, we can ADD w.e nodes we met.
        if len(heap) != k:
            heapq.heappush(heap, node.val * -1)
            # Easier to check last added value like this than try to extra check it after.
            if len(heap) == k:
                # Ignore left turn if it's values going to be higher than MAX_VALUE(heap[0]).
                if node.left and node.left.val * -1 > heap[0]:
                    search(node.left)
                # Ignore right turn with same approach.
                if node.right and node.right.val * -1 > heap[0]:
                    search(node.right)
                return
            # If heap isn't populated, we check everything.
            if node.left:
                search(node.left)
            if node.right:
                search(node.right)
            return
        if len(heap) == k:
            # Only add values lower than MAX_VALUE,
            #  all values are inverted, so it's HIGHER than LOWEST in a heap
            if (node.val * -1) > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, node.val * -1)
            # If we come from right_turn => everything in this subtree,
            #  will be higher than pre_turn Node values == insta break.
            else:
                return
            # Otherwise, we can check both subtrees.
            if node.left and (node.left.val * -1) > heap[0]:
                search(node.left)
            if node.right and (node.right.val * -1) > heap[0]:
                search(node.right)

    search(root)
    # There's K elements in a heap, and they're sorted from MAX to MIN if inverted back.
    # We need K element of smallest counted from left to right.
    # So [0] it's actually HIGHEST of 'k' SMALLEST.
    return heapq.heappop(heap) * -1


# Time complexity: O(n * log k) -> worst case == BT with only descending Nodes -> we're traversing whole input BT
# n - Nodes of input BT^^|  and pushing every new Node value into a heapq => O(n * log k).
# Auxiliary space: O(n) -> worst case == (n == k) -> heapq will store 'n' values of every Node => O(n) ->
#                          -> extra to this, BT with only descending Nodes in linked list style ->
#                          -> recursion stack will be a size of 'n' as well => O(2n).
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
# -------------------
# Forgot that if we count NODE itself first, it's pre-order not inorder.
# They're going the same path, but recording is different.
