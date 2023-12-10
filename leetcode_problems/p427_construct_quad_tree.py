# Given an n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
# Return the root of the Quad-Tree representing grid.
# ------------------------
# A Quad-Tree is a tree data structure in which each internal node has exactly four children.
# Besides, each node has two attributes:
#   - val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
#     Notice that you can assign the val to True or False when isLeaf is False,
#      and both are accepted in the answer.
#   - isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
#   class Node {
#       public boolean val;
#       public boolean isLeaf;
#       public Node topLeft;
#       public Node topRight;
#       public Node bottomLeft;
#       public Node bottomRight;
#   }
# We can construct a Quad-Tree from a two-dimensional area using the following steps:
#  1) If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True
#     and set val to the value of the grid and set the four children to Null and stop.
#  2) If the current grid has different values, set isLeaf to False and set val to any value
#     and divide the current grid into four sub-grids as shown in the photo.
#  3) Recurse for each of the children with the proper sub-grid.
# ------------------------
# n == grid.length == grid[i].length
# n == 2x where 0 <= x <= 6
from collections import deque


class Node:

    def __init__(self, val: bool, isLeaf: bool, topLeft: None or 'Node',
                 topRight: None or 'Node', bottomLeft: None or 'Node', bottomRight: None or 'Node'):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def t_bfs_read(node: Node) -> list[list[int]]:
    que: deque[Node | None] = deque([node])
    # [isLeaf, val]
    out: list[list[int] | None] = []
    while que:
        cur_node: Node = que.popleft()
        if not cur_node:
            out.append(None)
            continue
        out.append([1 if cur_node.isLeaf else 0, 1 if cur_node.val else 0])
        que.append(cur_node.topLeft)
        que.append(cur_node.topRight)
        que.append(cur_node.bottomLeft)
        que.append(cur_node.bottomRight)
    # Last empty childs, ignored on Leetcode reading.
    while out[-1] is None:
        out.pop()
    return out


def construct(grid: list[list[int]]) -> Node:
    # working_sol (89.49%, 86.32%) -> (98ms, 17.1mb)  time: O(n) | space: O(n)
    base_val: int = grid[0][0]
    leaf: bool = True
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != base_val:
                leaf = False
                break
        if not leaf:
            break
    if leaf:
        return Node(
            val=True if base_val == 1 else False,
            isLeaf=True,
            topLeft=None,
            bottomLeft=None,
            topRight=None,
            bottomRight=None,
        )
    height_half: int = len(grid) // 2
    length_half: int = len(grid[0]) // 2
    top_left: list[list[int]] = [row[:length_half] for row in grid[:height_half]]
    bot_left: list[list[int]] = [row[:length_half] for row in grid[height_half:]]
    top_right: list[list[int]] = [row[length_half:] for row in grid[:height_half]]
    bot_right: list[list[int]] = [row[length_half:] for row in grid[height_half:]]
    return Node(
        # Notice that you can assign the val to True or False when isLeaf is False,
        #  and both are accepted in the answer.
        val=True if base_val == 1 else False,
        isLeaf=False,
        topLeft=construct(top_left),
        bottomLeft=construct(bot_left),
        topRight=construct(top_right),
        bottomRight=construct(bot_right),
    )


# Time complexity:
#  O((d + 1) * k) <- d - depths of QuadTree, k - points stored.
#  OR
#  O(n) <- n - input matrix `grid` cells.
# No idea which one is correct, but first option is from https://www.jordansavant.com/book/algorithms/quadtree.md
# And another from CSE554 presentation for some picture analysis, and they compare QuadTree(2D) vs Octrees (3D).
# Essentially if we have every cells like [1, 0] [0, 1].
# So we will have Leafs only with 1 cell in the end, and traverse all cells for the First Node => O(n).
# Then we will traverse same # of cells, but in 4 sub-grids => O(2n).
# And we repeat this until we get Leafs with only 1 cell inside.
# So, it's should be Linear O(n) but with some constant, which we ignore I guess.
# ------------------------
# Auxiliary space: O(n).
# If we apply same logic, then First Node will hold all 'n' cells => O(n).
# Next will have (n // 4) parts for each sub-grid, but in the it's still O(2n).
# And repeating until all Leafs == single cell, so it should be correct to say Linear O(n).


test: list[list[int]] = [[0, 1], [1, 0]]
test_out: list[list[int] | None] = [[0, 0], [1, 0], [1, 1], [1, 1], [1, 0]]
assert test_out == t_bfs_read(construct(test))

test = [
    [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]
]
test_out = [[0, 1], [1, 1], [0, 0], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]
assert test_out == t_bfs_read(construct(test))
