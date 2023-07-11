# Given the root of a binary tree and an integer targetSum,
#   return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
# Each path should be returned as a list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending at any leaf node.
# A leaf is a node with no children.
# ----------------
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, targetSum: int) -> list[list[int]]:
    # working_sol (34.1%, 33.16%) -> (65ms, 21.6mb) time: O(n) | space: O(K * log n)
    if not root:
        return []
    all_paths: list[list[int]] = []

    def inorder(node: TreeNode, path: int, r_path: list[int]) -> None:
        # in_order with record of a path, and path sum
        if node.left is None and node.right is None:
            if path == targetSum:
                r_path.append(node.val)
                all_paths.append(r_path)
            return
        if node.left:
            inorder(node.left, path + node.left.val, r_path + [node.val])
        if node.right:
            inorder(node.right, path + node.right.val, r_path + [node.val])

    inorder(root, root.val, [])
    return all_paths


# Time complexity: O(n) -> traversing whole input_BT, once => O(n).
# n - nodes in input_BT^^|
# Auxiliary space: O(K * log n) -> standard recursion stack for BT => O(log n) -> and we extra storing all paths from
#                          root to leafs, in the worst case every leaf is having correct path,
#                          so we need to include every node in it, and they can be used multiple times
#                          like 1 2 3 4 == 10 and another leaf path is 1 2 3 4 as well, then 1 2 3 added 2 times,
#                          no idea how to calc it correctly, but should be something like =>
#                          => K <- number of correct paths, S - number of nodes in correct path =>
#                          => O(K * S) <- for every correct path we're storing all it's node.values.
#                             ^^But how to connect it with input_BT? (log n) * K?
# ----------------
# Ok. Failed commit -> I was thinking we shouldn't include duplicates, because there's no reasons for it.
# If we were saving correct PATH with node than it should be considered and path will have same VALUES but
# different NODES, in this task it's just VALUES in list, and if there's 2 or more copies of them
# it gives us nothing useful. Well guess we need knowledge about multiple same VALUES path even without saving nodes.
