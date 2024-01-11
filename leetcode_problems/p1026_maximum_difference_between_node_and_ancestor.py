# Given the root of a binary tree, find the maximum value v for which there exist different
#  nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
# -----------------------
# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 10 ** 5
from collections import deque
from random import randint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bt_from_level_order(nodes: list[int]) -> TreeNode:
    root: TreeNode = TreeNode(nodes[0])
    que: deque[TreeNode] = deque([root])
    index: int = 1
    while que:
        cur_node: TreeNode = que.popleft()
        if index < len(nodes):
            if nodes[index] is not None:
                cur_node.left = TreeNode(nodes[index])
                que.append(cur_node.left)
            else:
                cur_node.left = None
        index += 1
        if index < len(nodes):
            if nodes[index] is not None:
                cur_node.right = TreeNode(nodes[index])
                que.append(cur_node.right)
            else:
                cur_node.right = None
        index += 1
    return root


def read_level_order(root: TreeNode) -> list[int]:
    nodes: list[int | None] = []
    que: deque[TreeNode] = deque([root])
    while que:
        cur_node: TreeNode = que.popleft()
        if cur_node is None:
            nodes.append(None)
            continue
        nodes.append(cur_node.val)
        que.append(cur_node.left)
        que.append(cur_node.right)
    while nodes[-1] is None:
        nodes.pop()
    return nodes


def max_ancestor_diff(root: TreeNode) -> int:
    # working_sol (85.36%, 74.81%) -> (38ms, 19.01mb)  time: O(n) | space: O(n)
    # First, every Node in left or right subtree from current Node,
    #  can be considered as descendant. And every Node above is ancestor.
    # To get maximised difference, we need to find minimum and maximum of current Node subtrees.
    # Because we can have Node.val == 5, and in subtrees min == 0 and max == 100.
    # So, we will get maximum difference with abs(5 - 100).
    # Or, if we think about it more and don't rush as I did, we can just take:
    #  ! maximum of subtree - minimum of subtree == maximum difference !
    # But w.e., not so slow and working.

    def dfs(node: TreeNode) -> tuple[int, int, int]:
        # If no childs.
        # `node.val` is maximum and minimum values we can have in this subtree.
        min_value: int = node.val
        max_value: int = node.val
        # Minimum diff we can have == 0.
        cur_max_diff: int = 0
        max_diff: int = 0
        if node.left:
            min_val_in_left, max_val_in_left, max_so_far = dfs(node.left)
            cur_max_diff = max(
                abs(node.val - min_val_in_left),
                abs(node.val - max_val_in_left),
            )
            min_value = min(min_val_in_left, min_value)
            max_value = max(max_val_in_left, max_value)
            max_diff = max(max_so_far, cur_max_diff)
        if node.right:
            min_val_in_right, max_val_in_right, max_so_far = dfs(node.right)
            cur_max_diff = max(
                abs(node.val - min_val_in_right),
                abs(node.val - max_val_in_right),
                cur_max_diff,
            )
            min_value = min(min_val_in_right, min_value)
            max_value = max(max_val_in_right, max_value)
            max_diff = max(max_so_far, cur_max_diff, max_diff)
        # (minimum value in current subtree, maximum value in current subtree, max_difference we found so far)
        return min_value, max_value, max_diff

    return dfs(root)[2]


# Time complexity: O(n) <- n - number of Nodes in input BT `root`.
# We will traverse whole input BT `root`, and for each Node which have childs we will choose min, max, and calc diff.
# Which is constant operations, and if Node doesn't have a childs it's just an insta return of min, max values => O(n).
# -----------------------
# Auxiliary space: O(n).
# Worst case: BT with Nodes placed in style of LinkedList, so recursion stack will be of size `n` => O(n).
# Every constant INTs we use, doesn't depend on input.


test: list[int] = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
test_tree: TreeNode = bt_from_level_order(test)
assert test == read_level_order(test_tree)
test_out: int = 7
assert test_out == max_ancestor_diff(test_tree)

test = [1, None, 2, None, 0, 3]
test_tree = bt_from_level_order(test)
assert test == read_level_order(test_tree)
test_out = 3
assert test_out == max_ancestor_diff(test_tree)

test = [1, 2, 10, 0, 6, None, 14, None, None, 4, 100, 13, None, None, None, 200]
test_tree = bt_from_level_order(test)
assert test == read_level_order(test_tree)
test_out = 199
assert test_out == max_ancestor_diff(test_tree)

test = [1, 2]
test_tree = bt_from_level_order(test)
assert test == read_level_order(test_tree)
test_out = 1
assert test_out == max_ancestor_diff(test_tree)

test = [randint(0, 10 ** 5) for _ in range(5000)]
print(test)
