# Given the root of a binary tree, flatten the tree into a "linked list":
#   The "linked list" should use the same TreeNode class
#     where the right child pointer points to the next node in the list
#     and the left child pointer is always null.
#   The "linked list" should be in the same order as a pre-order traversal of the binary tree.
# --------------------------
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# --------------------------
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode) -> None:
    # working_sol (92.41%, 45.65%) -> (45ms, 45.65%)  time: O(n) | space: O(n)
    if not root:
        return
    pre_order: list[TreeNode] = []

    def pre_order_read(node: TreeNode) -> None:
        pre_order.append(node)
        if node.left:
            pre_order_read(node.left)
        if node.right:
            pre_order_read(node.right)

    pre_order_read(root)
    for x in range(1, len(pre_order)):
        pre_order[x - 1].right, pre_order[x - 1].left = pre_order[x], None


# Time complexity: O(n) -> pre-order traversal of whole input_BT => O(n) ->
# n - nodes in input_BT^^| -> extra loop for every saved node => O(n) -> O(n) + O(n) => O(n).
# Auxiliary space: O(n) -> for recursion stack in the worst case, if tree is unbalanced and all nodes  will be
#                       positioned as linked list => O(n) -> and extra list to store all nodes of input_BT => O(n).
# --------------------------
# For constant space we can use Morris Traversal -> https://www.geeksforgeeks.org/morris-traversal-for-preorder/
# Not copying it, failed follow up on my own.
# --------------------------
# No idea about how to do this in constant space, but without it -> just read in pre-order and reassign.
