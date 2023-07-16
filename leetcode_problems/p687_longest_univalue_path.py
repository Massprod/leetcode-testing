# Given the root of a binary tree, return the length of the longest path,
#   where each node in the path has the same value. This path may or may not pass through the root.
# The length of the path between two nodes is represented by the number of edges between them.
# ---------------------
# The number of nodes in the tree is in the range [0, 10 ** 4].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_univalue(root: TreeNode) -> int:
    # working_sol (75.86%, 90.17%) -> (340ms, 20.18mb)  time: O(n) | space: O(n)
    if not root:
        return 0
    # we can't travel one node more than once,
    # there's no mentioning on that but test cases
    # are correct only with that assumption
    max_path: list[int] = [0]

    def inorder(node: TreeNode) -> tuple[int, int] | None:
        if not node:
            return
        left_path: int = 0
        right_path: int = 0
        if node.left:
            # left -> the longest path in left subtree.
            # same -> value of a next node.
            left, same = inorder(node.left)
            # going backwards and checking value of
            # cur_node and prev node
            if node.val == same:
                left_path += 1 + left
        if node.right:
            # right -> the longest path in right subtree.
            right, same = inorder(node.right)
            if node.val == same:
                right_path += 1 + right
        # max path we can travel through this node, and it's both subtrees
        node_max: int = left_path + right_path
        # best option to turn on this node, subtree with the longest path
        best_turn: int = max(left_path, right_path)
        # check of a max_path on cur_node and whole tree
        max_path[0] = max(node_max, max_path[0])
        # returning best option to turn and value of the node
        # to compare with other nodes in a backwards path
        return best_turn, node.val

    inorder(root)
    return max_path[0]


# Time complexity: O(n) -> traversing whole BT, once => O(n).
# n - nodes of input_BT^^|
# Auxiliary space: O(n) -> in the worst case, BT will be a linked_list with only left_children ->
#                          -> so recursion stack will be a size of n => O(n).
# ---------------------
# Ok. Tested with:
# [5,5,5,5,5,5,5,5,5,5,null,null,null,null,null,5,null,null,null,5,null,5,5,5,5,5,5,5,5,5,null,null,null,null,null,null]
# If we could travel more than once through the one node, then it will be path of 13 and correct leetcode
# answer is 10, it's only possible when we pass ONCE. So I will assume that we can use one node ONCE.
# ---------------------
# Same problem as p124, but we need to count only nodes with same values on a path, not whole path.
# Only problem with that I see is that there's no info about can we use nodes more than once?
# Like if we can travel 2-3 times through one node is going to be hard to count, and I need to test it.
