# You are given the root of a binary tree.
# A ZigZag path for a binary tree is defined as follows:
#   Choose any node in the binary tree and a direction (right or left).
#   If the current direction is right, move to the right child of the current node;
#     otherwise, move to the left child.
#   Change the direction from right to left or from left to right.
#   Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
# Return the longest ZigZag path contained in that tree.
# ------------------------
# The number of nodes in the tree is in the range [1, 5 * 10 ** 4].
# 1 <= Node.val <= 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_zz(root: TreeNode) -> int:
    # working_sol (72.28%, 13.86%) -> (356ms, 64.6mb)  time: O(n) | space: O(n)
    # Bad solution, rebuild later.
    # But I don't see how to count in recursion correctly, for now.
    max_zig: list[int] = [0]

    def move(node: TreeNode, left: bool, right: bool, path: int) -> None:
        # All path from any node we started includes
        # every node we met, and we don't need 1 of them ->
        # ->! Zigzag length is defined as the number of nodes visited - 1. !
        if not node:
            path -= 1
            max_zig[0] = max(max_zig[0], path)
            return
        # Previously made Left turn, we can either
        # start a new route with LEFT tur, or continue with same
        # path and turn RIGHT.
        if left:
            move(node.right, False, True, path + 1)
            move(node.left, True, False, 0 + 1)
        # Mirror of above.
        if right:
            move(node.left, True, False, path + 1)
            move(node.right, False, True, 0 + 1)

    move(root, True, True, 0)
    return max_zig[0]


# Time complexity: O(n) -> from every node we either move Right|Left and count all paths ->
# n - nodes of input_BT^^| -> so every Node will be used only once => O(n).
# Auxiliary space: O(n) -> linked_list style BT with all nodes stored in recursion stack => O(n).
# ------------------------
# Start new counter from every node and increment by 1 for every backward,
# extra -1 for ! Zigzag length is defined as the number of nodes visited - 1. !.
