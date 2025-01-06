# You are given the root of a binary tree with unique values.
# In one operation, you can choose any two nodes at the same level
#  and swap their values.
# Return the minimum number of operations needed to make the values at each level
#  sorted in a strictly increasing order.
# The level of a node is the number of edges along the path between it
#  and the root node.
# ---------------------
# The number of nodes in the tree is in the range [1, 10 ** 5].
# 1 <= Node.val <= 10 ** 5
# All the values of the tree are unique.
from collections import deque
from utils.binary_tree import TreeNode


def minimum_operations(root: TreeNode) -> int:
    # working_sol (99.35%, 18.95%) -> (123ms, 50.31mb)  time: O(n * log n) | space: O(n)
    out: int = 0
    que: deque[TreeNode | None] = deque([root, None])
    cur_lvl: list[int] = []
    # BFS with delimiter.
    while que:
        cur_node: TreeNode | None = que.popleft()
        # region LevelEnd
        if cur_node is None:
            if not que and not cur_lvl:
                break
            # Check every value we need to place.
            # If it has incorrect position == we need to switch it.
            # And we need to update position of switched values.
            # Otherwise, we will overcount switches.
            target_lvl: list[int] = sorted(cur_lvl)
            # { value: index_position }
            positions: dict[int, int] = {
                val: index for index, val in enumerate(cur_lvl)
            }
            for index in range(len(cur_lvl)):
                if cur_lvl[index] != target_lvl[index]:
                    out += 1
                    # Correct position for the value.
                    cur_target_position: int = positions[target_lvl[index]]
                    # Set current value position to the correct one.
                    positions[cur_lvl[index]] = cur_target_position
                    # Switch current value into correct position.
                    cur_lvl[cur_target_position] = cur_lvl[index]
            if que:
                que.append(None)
            cur_lvl = []
            continue
        # endregion LevelEnd
        cur_lvl.append(cur_node.val)
        if cur_node.left:
            que.append(cur_node.left)
        if cur_node.right:
            que.append(cur_node.right)
    return out


# Time complexity: O(n * log n) <- n - number of Nodes in the input BT.
# Standard BFS with delimiter takes O(n) => O(n).
# For each level we're sorting it and traversing.
# In complete BT, maximum size of the tree level is equal to (n // 2).
# O(2 * n + (n // 2) * log n) => O(n * log n).
# ---------------------
# Auxiliary space: O(n)
# `cur_lvl` <- at max `n // 2`.
# `target_lvl` <- at max `n // 2`.
# `positions` <- at max `n // 2` keys.
# `que` <- allocates space for each node => O(n).
