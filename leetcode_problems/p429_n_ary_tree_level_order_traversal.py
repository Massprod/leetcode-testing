# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal,
#  each group of children is separated by the null value (See examples).
# ------------------------
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10 ** 4]
from collections import deque
    

class Node:
    def __init__(
            self,
            val: int | None = None,
            children: list['Node' | None] = None
        ):
        self.val = val
        self.children = children


def level_order(root: Node) -> list[list[int]]:
    # working_sol (81.46%, 75.62%) -> (45ms, 19.18mb)  time: O(n) | space: O(n)
    if not root:
        return []
    out: list[list[int]] = [[root.val]]
    que: deque[Node | None] = deque([root, None])
    cur_level: list[int] = []
    while que:
        node: Node | None = que.popleft()
        if node is None:
            if cur_level:
                out.append(cur_level)
            cur_level = []
            if que:
                que.append(None)
            continue
        for children in node.children:
            que.append(children)
            cur_level.append(children.val)
    
    return out


# Time complexity: O(n) <- n - number of nodes in input BT `root`.
# Always traversing every node of the `root`, once => O(n).
# ------------------------
# Auxiliary space: O(n)
# `out` <- allocates space for value from each Node of the `root` => O(n).
# `que` <- allocates space for each node of `root` => O(2 * n).
# `cur_level` <- if there's only 1 level == `out` => O(3 * n).
