# You are given the root of a binary tree and a positive integer k.
# The level sum in the tree is the sum of the values of the nodes that are on the same level.
# Return the kth largest level sum in the tree (not necessarily distinct).
# If there are fewer than k levels in the tree, return -1.
# Note that two nodes are on the same level if they have the same distance from the root.
# --------------------------
# The number of nodes in the tree is n.
# 2 <= n <= 10 ** 5
# 1 <= Node.val <= 10 ** 6
# 1 <= k <= n
import heapq
from collections import deque
from utils.binary_tree import TreeNode


def kth_largest_level_sum(root: TreeNode, k: int) -> int:
    # working_sol (100%, 17.40%) -> (40ms, 52.88mb)  time: O(n + (m * log m) + (k * log m)) | space: O(n + m)
    out: int = -1
    cur_level: int = 0
    heap: list[int] = []
    heapq.heapify(heap)
    que: deque[TreeNode | None] = deque([root, None])
    # Standard BFS with delimiter.
    while que:
        cur_node: TreeNode | None = que.popleft()
        if cur_node is None:
            heapq.heappush(
                heap, cur_level * -1
            )
            cur_level = 0
            if que:
                que.append(None)
            continue
        cur_level += cur_node.val
        if cur_node.left:
            que.append(cur_node.left)
        if cur_node.right:
            que.append(cur_node.right)
    if k > len(heap):
        return -1
    for _ in range(k):
        out = heapq.heappop(heap) * -1
    return out


# Time complexity: O(n + m * log m + k * log m) <- n - number of Nodes inside the input BT `root`,
#                                                  m - number of levels of BT.
# Always traversing whole input BT to get all the level sums => O(n).
# Every level we traverse we're pushing into `heap` => O(n + m * log m).
# Extra we're always `pop` `k` elements from this `heap` => O(n + (m * log m) + (k * log m)).
# --------------------------
# Auxiliary space: O(n + m).
# `heap` <- allocates space for each level of the input BT => O(m).
# `que` <- allocates space for each node of the input BT => O(n + m).
