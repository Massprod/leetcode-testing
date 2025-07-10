# A maximum tree is a tree where every node has a value greater
#  than any other value in its subtree.
# You are given the root of a maximum binary tree and an integer val.
# Just as in the previous problem, the given tree was constructed from a list
#  a (root = Construct(a)) recursively with the following Construct(a) routine:
#  - If a is empty, return null.
#  - Otherwise, let a[i] be the largest element of a. Create a root node with the value a[i].
#  - The left child of root will be Construct([a[0], a[1], ..., a[i - 1]]).
#  - The right child of root will be Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]]).
#  - Return root.
# Note that we were not given a directly, only a root node root = Construct(a).
# Suppose b is a copy of a with the value val appended to it.
# It is guaranteed that b has unique values.
# Return Construct(b).
# ---------------------
# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 100
# All the values of the tree are unique.
# 1 <= val <= 100
from utils.binary_tree import TreeNode


def insert_into_max_tree(root: TreeNode, val: int) -> TreeNode:
    # working_sol (100.00%, 17.27%) -> (0ms, 17.96mb)  time: O(n) | space: O(1)

    def dfs(node: TreeNode | None, target: int) -> TreeNode:
        # Always turn right for the highest.
        if node and target < node.val:
            # Reassign if we don't find anything smaller than a `target`.
            node.right = dfs(node.right, target)
            return node
        # Otherwise, create and place subtree on the left side.
        new_node = TreeNode(val=target)
        new_node.left = node
        return new_node
        
    if root.val < val:
        return TreeNode(
            val=val, left=root,
        )
    
    dfs(root, val)
    return root


# Time complexity: O(n) <- n - number of nodes in the input BT `root`.
# Always traversing input BT `root`, once => O(n).
# ---------------------
# Auxiliary space: O(1)
