# Given the root of a binary tree, replace the value of each node
#  in the tree with the sum of all its cousins' values.
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
# Return the root of the modified tree.
# Note that the depth of a node is the number of edges
#  in the path from the root node to it.
# ----------------------------
# The number of nodes in the tree is in the range [1, 10 ** 5].
# 1 <= Node.val <= 10 ** 4
from collections import deque
from utils.binary_tree import TreeNode


def replace_value_in_tree(root: TreeNode) -> TreeNode:
    # working_sol (95.80%, 42.31%) -> (172ms, 67.68mb)  time: O(n) | space: O(n + k)
    # { level: sum_of_nodes }
    level_sums: dict[int, int] = {
        0: 0,
        1: 0,
    }

    def bfs_check(node: TreeNode, change_nodes: bool = False) -> None:
        nonlocal level_sums
        que: deque[TreeNode | None] = deque([node, None])
        cur_level: int = 0
        cur_level_sum: int = 0
        while que:
            cur_node: TreeNode | None = que.popleft()
            if not cur_node:
                if not change_nodes:
                    if not change_nodes and 2 <= cur_level:
                        level_sums[cur_level] = cur_level_sum
                    cur_level_sum = 0
                cur_level += 1
                if que:
                    que.append(None)
                continue
            if not change_nodes:
                cur_level_sum += cur_node.val
            left_val: int = 0
            right_val: int = 0
            if cur_node.left:
                left_val = cur_node.left.val
                que.append(cur_node.left)
            if cur_node.right:
                right_val = cur_node.right.val
                que.append(cur_node.right)
            # All we care about is to change the value of Nodes on 2+ levels to a (cousins - (node +  brother))
            if change_nodes and 1 <= cur_level:
                change_val: int = level_sums.get(cur_level + 1, 0) - left_val - right_val
                if cur_node.left:
                    cur_node.left.val = change_val
                if cur_node.right:
                    cur_node.right.val = change_val

    root.val = 0
    if root.left:
        root.left.val = 0
    if root.right:
        root.right.val = 0
    bfs_check(root, False)
    bfs_check(root, True)
    return root


# Time complexity: O(n) <- n - number of Nodes in the input BT `root`.
# Always traversing whole input BT `root`, twice => O(2 * n).
# ----------------------------
# Auxiliary space: O(n + k) <- k - number of levels of the input BT `root`.
# `level_sum` <- allocates space for each level of the `root` => O(k).
# `que` <- standard BFS que, allocates space for each Node in BT `root` => O(n + k).
