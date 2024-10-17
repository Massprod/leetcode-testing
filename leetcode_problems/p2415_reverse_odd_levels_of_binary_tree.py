# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
#  - For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18],
#     then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
# The level of a node is the number of edges along the path between it and the root node.
# -----------------------
# The number of nodes in the tree is in the range [1, 2 ** 14].
# 0 <= Node.val <= 10 ** 5
# root is a perfect binary tree.
from collections import deque
from utils.binary_tree import TreeNode


def reverse_odd_levels(root: TreeNode) -> TreeNode:
    # working_sol (99.42%, 50.76%) -> (615ms, 21.28mb)  time: O(n) | space: O(n)
    def switch_nodes(nodes: list[TreeNode]) -> list:
        left: int = 0
        right: int = len(nodes) - 1
        while left < right:
            nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val
            left += 1
            right -= 1
        return []
    # Standard BFS
    cur_level: int = 0
    odd_nodes: list[TreeNode] = []
    que: deque[TreeNode | None] = deque([root, None])
    while que:
        cur_node: TreeNode | None = que.popleft()
        if cur_node is None:
            cur_level += 1
            if cur_level % 2:
                odd_nodes = switch_nodes(odd_nodes)
            if que:
                que.append(None)
            continue
        # We're given `perfect binary tree` <- last level == we don't care
        if not cur_node.left and not cur_node.right:
            continue
        if not cur_level % 2:
            odd_nodes.append(cur_node.left)
            odd_nodes.append(cur_node.right)
        que.append(cur_node.left)
        que.append(cur_node.right)
    return root


# Time complexity: O(n) <- n - number of Nodes inside the input BT `root`.
# Always traversing whole input BT `root`, once => O(n).
# -----------------------
# Auxiliary space: O(n)
# In the worst case - there's only 2 levels, `odd_nodes` allocates space for (n - 1) => O(n).
# -----------------------
# Actually we store our last level, and we traverse every ODD level.
# But I don't see how we can calc it :)
# Like, perfect BT == prev_level * 2 = nodes of the next level.
# Only => Nodes = 2 ** level + 1  - 1 == 2 ** 0 + 2 ** 1 + 2 ** 2 + ... + 2 ** level
