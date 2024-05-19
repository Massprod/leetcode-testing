# You are given the root of a full binary tree with the following properties:
#  - Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
#  - Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR
#     and 3 represents the boolean AND.
# The evaluation of a node is as follows:
#  - If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
#  - Otherwise, evaluate the node's two children and apply the boolean operation of its value
#     with the children's evaluations.
# Return the boolean result of evaluating the root node.
# A full binary tree is a binary tree where each node has either 0 or 2 children.
# A leaf node is a node that has zero children.
# ------------------------
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 3
# Every node has either 0 or 2 children.
# Leaf nodes have a value of 0 or 1.
# Non-leaf nodes have a value of 2 or 3.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluate_tree(root: TreeNode) -> bool:
    # working_sol (81.84%, 92.02%) -> (43ms, 16.78mb)  time: O(n) | space: O(log n)
    # 0 - False
    # 1 - True
    # 2 - OR
    # 3 - AND

    def dfs(node: TreeNode) -> bool:
        # ! Every node has either 0 or 2 children. !
        if not node.left:
            return True if node.val else False
        left_child: bool = dfs(node.left)
        right_child: bool = dfs(node.right)
        if 2 == node.val:
            return left_child | right_child
        return left_child & right_child

    return dfs(root)


# Time complexity: O(n) <- n - number of Nodes in the input BT `root`.
# Always traversing whole BT to use every `node.val` => O(n).
# ------------------------
# Auxiliary space: O(log n)
# With this constraints we're not going to have BT like a LinkedList.
# So, we're only going to have a stack with part of the Nodes => O(log n).
