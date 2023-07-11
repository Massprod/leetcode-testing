# You are given the root of a binary search tree (BST),
#   where the values of exactly two nodes of the tree were swapped by mistake.
# Recover the tree without changing its structure.
# ------------------
# The number of nodes in the tree is in the range [2, 1000].
# -2 ** 31 <= Node.val <= 2 ** 31 - 1


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverTree(root: TreeNode) -> None:
    # working_sol (69.2%, 82.8%) -> (83ms, 16.6mb)  time: O(n * log n) | space: O(n)
    if not root:
        return
    nodes: list[TreeNode] = []

    def inorder(node: TreeNode) -> None:
        # in_order -> gives sorted list of values from correct BT
        if node.left:
            inorder(node.left)
        nodes.append(node)
        if node.right:
            inorder(node.right)

    inorder(root)
    values: list[int] = []
    for _ in nodes:
        values.append(_.val)
    values.sort()
    for x in range(len(nodes)):
        nodes[x].val = values[x]


# Time complexity: O(n * log n) -> in_order traversal of whole input_BT, once => O(n) ->
# n - nodes in input_BT^^| -> sorting result of traversal => O(n * log n) ->
#                          -> replacing every node value in input_BT for correct one => O(n) ->
#                          -> O(n) + O(n * log n) + O(n) => O(n * log n).
# Auxiliary space: O(n) -> store links to all nodes in input_BT => O(n) -> store every value of them => O(n) ->
#                          -> O(n) + O(n) => O(2n) => O(n). If we don't ignore recursion than extra O(log n) for stack.
# ------------------
# in_order -> gives sorted list of values from correct BT. All we need for O(n) space, with O(1) no idea.
# Maybe reuse task when we needed to find node with incorrect value and then,
# replace every other node value with it and extra check again on every switch?
# But it will be a recursion, and it's not O(1). Only if we ignore stack, w.e. It's again some extra_hard follow up.
