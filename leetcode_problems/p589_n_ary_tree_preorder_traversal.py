# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)
# --------------------------
# The number of nodes in the tree is in the range [0, 10 ** 4].
# 0 <= Node.val <= 10 ** 4
# The height of the n-ary tree is less than or equal to 1000.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root: Node) -> list[int]:
    # working_sol (96.91%, 82.90%) -> (36ms, 18.15mb)  time: O(n) | space: O(n)
    # Preorder == Node itself + w.e child in left -> right order.
    if not root:
        return []
    out: list[int] = [root.val]
    for child in root.children:
        out += preorder(child)
    return out


# Time complexity: O(n) <- n - number of Nodes inside of given `root`.
# Always using every Node of the `root`, once => O(n).
# --------------------------
# Auxiliary space: O(n)
# We're always creating arrays which in their summarized sizes equal to `n` => O(n).
# If tree will be in the style of LinkedList, we're going to have a stack with all Nodes in it => O(2n).
