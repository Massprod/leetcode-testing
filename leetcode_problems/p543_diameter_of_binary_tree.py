# Given the root of a binary tree,
#   return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between
#   any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
# ---------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -100 <= Node.val <= 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_bt(root: TreeNode) -> int:
    # working_sol (80.31%, 96.56%) -> (56ms, 18.6mb)  time: O(n) | space: O(n)
    # we can't travel one node more than once,
    # there's no mentioning on that but test cases
    # are correct only with that assumption
    max_path: list[int] = [0]

    def inorder(node: TreeNode) -> int | None:
        if not node:
            return
        left_path: int = 0
        right_path: int = 0
        if node.left:
            # left -> the longest path in left subtree.
            left_path += 1 + inorder(node.left)
        if node.right:
            # right -> the longest path in right subtree.
            right_path += 1 + inorder(node.right)
        # max path we can travel through this node, and it's both subtrees
        node_max: int = left_path + right_path
        # best option to turn on this node, subtree with the longest path
        best_turn: int = max(left_path, right_path)
        # check of a max_path on cur_node and whole tree
        max_path[0] = max(node_max, max_path[0])
        # returning best option to turn
        return best_turn

    inorder(root)
    return max_path[0]


# Time complexity: O(n) -> traversing whole BT, once => O(n).
# n - nodes of input_BT^^|
# Auxiliary space: O(n) -> in the worst case, BT will be a linked_list with only left_children ->
#                          -> so recursion stack will be a size of n => O(n).
# ---------------------
# It's fun how it recommends literal mirror of the task, but with Easy difficulty.
# Just a copy of p687 without considering values of a nodes.
# Once again they didn't mention that we can't travel over one node more than once,
# guess this is a standard for these tasks.
