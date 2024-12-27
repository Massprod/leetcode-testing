# Given the root of a binary tree, construct a 0-indexed m x n string matrix res
#  that represents a formatted layout of the tree.
# The formatted layout matrix should be constructed using the following rules:
#  - The height of the tree is height and the number of rows m
#    should be equal to height + 1.
#  - The number of columns n should be equal to 2height+1 - 1.
#  - Place the root node in the middle of the top row
#    (more formally, at location res[0][(n-1)/2]).
#  - For each node that has been placed in the matrix at position res[r][c],
#    place its left child at res[r+1][c-2height-r-1]
#     and its right child at res[r+1][c+2height-r-1].
#  - Continue this process until all the nodes in the tree have been placed.
#  - Any empty cells should contain the empty string "".
# Return the constructed matrix res.
# ----------------------
# The number of nodes in the tree is in the range [1, 2 ** 10].
# -99 <= Node.val <= 99
# The depth of the tree will be in the range [1, 10].
from utils.binary_tree import TreeNode


def print_tree(root: TreeNode) -> list[list[str]]:
    # working_sol (100.00%, 5.86%) -> (0ms, 18.04mb)  time: O(n + h) | space: O(n + h)
    #region Height
    def dfs(node: TreeNode, depth: int) -> int:
        max_depth: int = depth
        if node.left:
            max_depth = max(
                max_depth, dfs(node.left, depth + 1)
            )
        if node.right:
            max_depth = max(
                max_depth, dfs(node.right, depth + 1)
            )
        
        return max_depth
        
    height: int = dfs(root, 0)
    #endregion Height
    out: list[list[str]] = [
        ['' for _ in range(2 ** (height + 1) - 1)] for _ in range(height + 1)
    ]

    def dfs_place(node: TreeNode, row: int, col: int) -> None:
        nonlocal out, height

        next_row: int = row + 1
        col_shift: int = 2 ** (height - row - 1)
        if node.left:
            left_col: int = col - col_shift
            out[next_row][left_col] = str(node.left.val)
            dfs_place(node.left, next_row, left_col)
        if node.right:
            right_col: int = col + col_shift
            out[next_row][right_col] = str(node.right.val)
            dfs_place(node.right, next_row, right_col)
    
    root_row: int = 0
    root_col: int = (len(out[0]) - 1) // 2
    out[root_row][root_col] = str(root.val)
    dfs_place(root, root_row, root_col)

    return out


# Time complexity: O(n + h) <- n - number of Nodes in the input BT `root`,
#                              h - height of the input BT `root`.
# Traversing whole input BT `root` to get height => O(n).
# Creating a matrix of sizes: `(h + 1) * (2 ** (h + 1) - 1)` =
# => O(n + (h + 1) * (2 ** (h + 1) -1)).
# Extra traversing whole input BT to place Node values in their places =
# => O(n + (h + 1) * (2 ** (h + 1) -1) + n).
# ----------------------
# Auxiliary space: O(n + h).
# `out` <- allocates space for (h + 1) * (2 ** (h + 1) - 1) strings => O(h).
# DFS stacks allocates space for each Node of BT => O(2 * n + h).
