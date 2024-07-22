# Given two binary trees original and cloned
#  and given a reference to a node target in the original tree.
# The cloned tree is a copy of the original tree.
# Return a reference to the same node in the cloned tree.
# Note that you are not allowed to change any of the two trees
#  or the target node and the answer must be a reference to a node in the cloned tree.
# ----------------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# The values of the nodes of the tree are unique.
# target node is a node from the original tree and is not null.
# ----------------------------
# Follow up: Could you solve the problem if repeated values on the tree are allowed?


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_target_copy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    # working_sol (86.01%, 16.49%) -> (297ms, 24.66mb)  time: O(n) | space: O(1)
    out: TreeNode | None = None

    def traverse(node: TreeNode) -> bool:
        nonlocal out
        if node.val == target.val:
            out = node
            return True
        if node.left and traverse(node.left):
            return True
        if node.right and traverse(node.right):
            return True

    traverse(cloned)
    return out


# Time complexity: O(n) <- n - number of Nodes inside input BT `cloned`.
# In the worst case, our `target` going to be the most right leaf, so we will traverse every Node of `cloned` => O(n).
# ----------------------------
# Auxiliary space: O(n).
# Stack of the recursion is going to store references to every Node from `cloned` => O(n).
