from collections import deque
# You are given a perfect binary tree where all leaves are on the same level,
#   and every parent has two children.
# The binary tree has the following definition:


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# --------------------
# The number of nodes in the tree is in the range [0, (2 ** 12) - 1].
# -1000 <= Node.val <= 1000
# --------------------
# Follow-up:
# You may only use constant extra space.
# The recursive approach is fine.
# You may assume implicit stack space does not count as extra space for this problem.


def connect(root: Node) -> Node:
    # working_sol (94.39%, 63.42%) -> (67ms, 18.1mb)  time: O(n) | space: O(1)
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
# --------------------
# Ok. It's working, only question is -> can we count using deque() as constant space?
# !
# You may assume implicit stack space does not count as extra space for this problem. ! ->
# -> Like, recursion stack is same the as deque(), because we're not creating anything new and operating only with
# node links. But no idea if it's allowed or not => My opinion it's the same.
# Anyway I have no idea how to maintain recursion with function_calls() in this case.
# Maybe extra search later, im satisfied with mine anyway.
# --------------------
# Most basic way is to just order-level traverse with level record and assign indexes
# Like -> [x].next = [x + 1] if x != len(level). But it's extra space and too easy.
# Other way I know is to use delimiter with deque() reading, I was using recursion and deque() before.
# But in recursion I don't know how to maintain levels and when 2+ levels node split is it even possible?
# Like we call left or right and inside this recursion calls, how we will get left and right subtrees together?
# With que it's easy, cuz we can just use some delimiter and maintain level by level, and every other node from que
# until we hit delimiter is right node.
