# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path
#  from the root node down to the farthest leaf node.
# Nary-Tree input serialization is represented in their level order traversal,
#  each group of children is separated by the null value (See examples).
# -----------------------------
# The total number of nodes is in the range [0, 10 ** 4].
# The depth of the n-ary tree is less than or equal to 1000.
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def max_depth(root: Node) -> int:
    # working_sol (87.48%, 57.41%) -> (38ms, 18.06mb)  time: O(n) | space: O(n)
    out: int = 0
    if not root:
        return out
    # Standard BFS with delimiter.
    que: deque[Node | None] = deque([root, None])
    while que:
        cur_node: Node = que.popleft()
        if cur_node is None:
            out += 1
            if que:
                que.append(None)
            continue
        for child in cur_node.children:
            que.append(child)
    return out


# Time complexity: O(n) <- n - number of Nodes inside an input Tree `root`.
# Standard BFS approach, so we're going to use every Node once => O(n).
# -----------------------------
# Auxiliary space: O(n)
# `que` will allocate space for every Node => O(n).
