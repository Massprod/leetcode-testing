# Given a binary tree root and an integer target,
#  delete all the leaf nodes with value target.
# Note that once you delete a leaf node with value target
#  , if its parent node becomes a leaf node and has the value target,
#  it should also be deleted (you need to continue doing that until you cannot).
# --------------------------
# The number of nodes in the tree is in the range [1, 3000].
# 1 <= Node.val, target <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def remove_leaf_nodes(root: TreeNode, target: int) -> TreeNode | None:
    # working_sol (82.84%, 98.37%) -> (41ms, 16.96mb)  time: O(n) | space: O(n)
    def dfs(node: TreeNode) -> bool:
        if node.val == target and not node.left and not node.right:
            return True
        delete_left: bool = False
        delete_right: bool = False
        if node.left:
            delete_left = dfs(node.left)
        if node.right:
            delete_right = dfs(node.right)
        if delete_left:
            node.left = None
        if delete_right:
            node.right = None
        if node.val == target and not node.left and not node.right:
            return True
        return False

    result = dfs(root)
    if result:
        return None
    return root


# Time complexity: O(n) <- n - number of Nodes inside input BT `root`.
# Always traversing whole input BT `root` once => O(n).
# --------------------------
# Auxiliary space: O(n)
# In the worst case our BT `root` will be in the style of a linkedList.
# So, we will traverse it to the last leaf and the stack will be of `n` size, storing all of the Nodes => O(n).
# --------------------------
# Not doing tests, it's another medium, and I need to do extra class for creating and testing BT. Maybe later.
