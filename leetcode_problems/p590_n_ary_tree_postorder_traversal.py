# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
# ------------------
# The number of nodes in the tree is in the range [0, 10 ** 4].
# 0 <= Node.val <= 10 ** 4
# The height of the n-ary tree is less than or equal to 1000.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def postorder(root: Node) -> list[int]:
    # working_sol (97.39%, 69.61%) -> (35ms, 18.19mb)  time: O(n) | space: O(n)
    post_order: list[int] = []

    def post_order_traverse(node: Node) -> None:
        if not node:
            return
        for child in node.children:
            post_order_traverse(child)
        post_order.append(node.val)

    post_order_traverse(root)
    return post_order


# Time complexity: O(n) <- n - number of Nodes in the input N-ary tree `root`.
# We're always traversing whole tree, once => O(n).
# ------------------
# Auxiliary space: O(n)
# If N-ary tree is in style of linked list, we're going to have stack of size `n` => O(n).
# And `post_order` array with result of a traversal is always of size `n` => O(2n).
