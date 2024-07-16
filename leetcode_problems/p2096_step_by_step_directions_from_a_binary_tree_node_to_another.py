# You are given the root of a binary tree with n nodes.
# Each node is uniquely assigned a value from 1 to n.
# You are also given an integer startValue representing the value of the start node s,
#  and a different integer destValue representing the value of the destination node t.
# Find the shortest path starting from node s and ending at node t.
# Generate step-by-step directions of such path as a string consisting
#  of only the uppercase letters 'L', 'R', and 'U'.
# Each letter indicates a specific direction:
#  - 'L' means to go from a node to its left child node.
#  - 'R' means to go from a node to its right child node.
#  - 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.
# --------------------------
# The number of nodes in the tree is n.
# 2 <= n <= 10 ** 5
# 1 <= Node.val <= n
# All the values in the tree are unique.
# 1 <= startValue, destValue <= n
# startValue != destValue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_directions(root: TreeNode, start_value: int, dest_value: int) -> str:
    # working_sol (95.81%, 49.66%) -> (234ms, 52.28mb)  time: O(n) | space: O(n)
    start_path: list[str] = []
    dest_path: list[str] = []
    cur_path: list[str] = []

    def traverse(node: TreeNode) -> None:
        nonlocal start_path
        nonlocal dest_path
        nonlocal cur_path
        # Already found both paths, no reasons to continue.
        if start_path and dest_path:
            return
        if start_value == node.val:
            start_path = cur_path[:]
        elif dest_value == node.val:
            dest_path = cur_path[:]
        if node.left:
            cur_path.append('L')
            traverse(node.left)
            cur_path.pop()
        if node.right:
            cur_path.append('R')
            traverse(node.right)
            cur_path.pop()

    traverse(root)
    index: int = 0
    # We only care about the first Node when they're paths start to differ.
    # And because we start from `root`, we can delete everything before this Node.
    while index < min(len(start_path), len(dest_path)) and start_path[index] == dest_path[index]:
        index += 1
    # Also we need to change every turn from `start_value` -> `dest_value` to 'U'.
    # Because, it's turns from not common Nodes and their higher than `start_value` => parents.
    # And we need to traverse through them to get into `dest_value`.
    start_path = ['U' for _ in start_path[index:]]
    dest_path = dest_path[index:]
    return ''.join(start_path + dest_path)


# Time complexity: O(n) <- n - number of Nodes inside the input BT `root`.
# We're always traversing whole BT, once => O(n).
# In the worst case, every Node will be used with `cur_path`, like first_leaf -> last_leaf,
#  and we have only left_childs in the left subtree of the `root` and right childs in the right subtree.
# Then we're going to have `(n - 2) // 2` stored in `cur_path` and traversed for copying in `start_path`,
#  same goes for the `dest_path` => O(n + (n - 2)).
# Extra slicing and changing all values in `start_path` + `dest_path`,
#  both of them joined will have a size of `n - 2` => O(n + (n - 2) * 2).
# Extra traversing both of them concat + `join` => O(n + (n - 2) * 3).
# --------------------------
# Auxiliary space: O(n)
# With the same case, we're going to have `dest_path` + `start_path` + `cur_path` of sizes `(n - 2) // 2`
# Slices are full sized in this case, and extra space to `join` them => O(n - 2).
