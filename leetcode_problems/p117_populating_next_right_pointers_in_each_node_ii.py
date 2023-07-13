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
    # working_sol (78.37%, 62.91%) -> (61ms, 17.7mb)  time: O(n) | space: O(1)
    if not root:
        return root
    que: deque[Node | None] = deque()
    que.append(root)
    # delimiter to break node.next assignments
    que.append(None)

    while any(que):
        # if we have anything on [0] except delimiter
        while que[0]:
            current = que.popleft()
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
            current.next = que[0]
        # add delimiter for traversed level
        que.append(None)
        # remove delimiter for previous level
        que.popleft()

    return root


# Time complexity: O(n) -> standard order-level traverse, with simple delimiter to break node.next() assignments ->
# n - nodes in input_BT^^| -> every node will be used only once => O(n).
# Auxiliary space: O(1) -> nothing extra, except deque() but we should be allowed to ignore that ->
#                          -> first of all, almost all tasks is actually ignoring recursion_stack() and deque() in this
#                          case is equal to that, and we're using only links without creating anything extra => O(1).
# ----------------------
# Actual repetition of p117, but now we don't have PERFECT tree, which is doesn't matter in my solution.
# Because we're just adding nodes in que if they exist, if they don't ignore.
# But level structure in que in the same, node -> node -> delimiter.
# And if there's missing nodes, we will just hit delimiter as always and move to the next level.
