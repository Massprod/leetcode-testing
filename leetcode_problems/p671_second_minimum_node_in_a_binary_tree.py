# Given a non-empty special binary tree consisting of nodes with the non-negative value,
#  where each node in this tree has exactly two or zero sub-node.
# If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
# More formally, the property root.val = min(root.left.val, root.right.val) always holds.
# Given such a binary tree, you need to output the second minimum value
#  in the set made of all the nodes' value in the whole tree.
# If no such second minimum value exists, output -1 instead.
# --------------------
# The number of nodes in the tree is in the range [1, 25].
# 1 <= Node.val <= 2 ** 31 - 1
# root.val == min(root.left.val, root.right.val) for each internal node of the tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_second_min_value(root: TreeNode) -> int:
    # working_sol (96.50%, 98.01%) -> (25ms, 16.23mb)  time: O(n) | space: O(n)
    # Don't see how all of these gibberish:
    # ! root.val = min(root.left.val, root.right.val) !
    # Can help us, because we still have no idea what's behind every child.
    # And we can have child with this `min` value and behind it something bigger.
    # And if everything else is equal, we can't ignore it. So, wtf this rules?
    first_min: int | float = float('inf')
    second_min: int | float = float('inf')

    def dfs(node: TreeNode) -> None:
        nonlocal first_min, second_min
        if node.val < first_min:
            first_min, second_min = node.val, first_min
        elif node.val != first_min and node.val < second_min:
            second_min = node.val
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)

    dfs(root)
    return second_min if second_min != float('inf') else -1


# Time complexity: O(n) <- n - number of Nodes inside the input BT `root`
# Always traversing whole BT `root`, once => O(n).
# --------------------
# Auxiliary space: O(n).
# If BT is structures like LinkedList, our recursion stack is going to be of size `n` => O(n).
