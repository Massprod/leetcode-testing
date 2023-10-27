from collections import deque
# Given a binary tree:


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.


def connect(root: Node) -> Node:
    # working_sol (82.90%, 68.50%) -> (47ms, 17.7mb)  time: O(n) | space: O(n)
    if not root:
        return root
    # Standard BFS with delimiter.
    que: deque[Node | None] = deque([root, None])

    while que:
        current = que.popleft()
        if not current:
            if que:
                que.append(None)
            continue
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
        if que[0]:
            current.next = que[0]

    return root


# Time complexity: O(n) -> traversing all Nodes of input BT once => O(n).
# n - Nodes of input BT^^|
# Auxiliary space: O(n) -> extra space for every Node => O(n).
#                       Leetcode ignores recursion stack and deque in some cases, but it's not really correct.
# ----------------------
# Actual repetition of p117, but now we don't have PERFECT tree, which is doesn't matter in my solution.
# Because we're just adding nodes in que if they exist, if they don't ignore.
# But level structure in que in the same, node -> node -> delimiter.
# And if there's some missing Nodes, we will just hit delimiter as always and move to the next level.
