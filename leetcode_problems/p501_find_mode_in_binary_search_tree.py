# Given the root of a binary search tree (BST) with duplicates,
#  return all the mode(s) (i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.
# Assume a BST is defined as follows:
#  The left subtree of a node contains only nodes with keys less than or equal to the node's key.
#  The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
#  Both the left and right subtrees must also be binary search trees.
# ------------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -10 ** 5 <= Node.val <= 10 ** 5


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_mode(root: TreeNode) -> list[int]:
    # working_sol (96.53%, 36.54%) -> (45ms, 20.83mb)  time: O(n) | space: O(n)
    nodes: dict[int, int] = {}

    def inorder(node: TreeNode) -> None:
        if node.left:
            inorder(node.left)
        if node.val in nodes:
            nodes[node.val] += 1
        else:
            nodes[node.val] = 1
        if node.right:
            inorder(node.right)

    inorder(root)
    out: list[int] = []
    cur_max: int = 0
    for key, value in nodes.items():
        if value > cur_max:
            cur_max = value
            out = [key]
        elif value == cur_max:
            out.append(key)
    return out


# Time complexity: O(n) -> traversing all Nodes to get their occurrences => O(n) ->
# n - Node of input BST^^| -> worst case == every Node value is unique -> traversing all Node again to get mode => O(n).
# Auxiliary space: O(n) -> same worst case -> dictionary 'nodes' will store every Node value => O(n).
