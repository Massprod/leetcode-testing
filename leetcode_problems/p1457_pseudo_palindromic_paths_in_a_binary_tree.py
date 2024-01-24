# Given a binary tree where node values are digits from 1 to 9.
# A path in the binary tree is said to be pseudo-palindromic if at least one permutation
#  of the node values in the path is a palindrome.
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
# --------------------------
# The number of nodes in the tree is in the range [1, 10 ** 5].
# 1 <= Node.val <= 9
from random import randint
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_from_level_order(values: list[int]) -> TreeNode:
    # Bad building, but working.
    root: TreeNode = TreeNode(values[0])
    node_index: int = 0
    que: deque[TreeNode | None] = deque([root])
    while (2 * node_index + 1) < len(values):
        cur_node: TreeNode | None = que.popleft()
        # Every level Node index is (*2) for every previous level Nodes,
        #  and +1, +2 for childs.
        val_index: int = 2 * node_index + 1
        if values[val_index] is None:
            cur_node.left = None
        else:
            cur_node.left = TreeNode(values[val_index])
            que.append(cur_node.left)
        val_index = 2 * node_index + 2
        if values[val_index] is None:
            cur_node.right = None
        else:
            cur_node.right = TreeNode(values[val_index])
            que.append(cur_node.right)
        node_index += 1
    return root


def level_order_read(root: TreeNode) -> list[int]:
    out: list[int | None] = []
    que: deque[TreeNode] = deque([root])
    while que:
        node: TreeNode = que.popleft()
        if not node:
            out.append(None)
            continue
        out.append(node.val)
        que.append(node.left)
        que.append(node.right)
    while out[-1] is None:
        out.pop()
    return out


def pseudo_palindromic_paths(root: TreeNode) -> int:
    # working_sol (94.67%, 97.33%) -> (373ms, 43.6mb)  time: O(n) | space: O(n)
    # {digit: # of occurrences in the current path}
    path: dict[int, int] = defaultdict(int)

    def dfs(node: TreeNode) -> int:
        # Record path, we travel.
        path[node.val] += 1
        # Leaf -> check path, for palindrome build possibility.
        if not node.left and not node.right:
            middle_used: bool = False
            for digit, occurrences in path.items():
                # Even can be used, in any case.
                # Odd can be used once, to place 1 in the middle.
                if occurrences % 2:
                    if not middle_used:
                        middle_used = True
                    # If we have more than 1 odd, then we can't build palindrome.
                    else:
                        path[node.val] -= 1
                        return 0
            path[node.val] -= 1
            return 1
        pals: int = 0
        if node.left:
            pals += dfs(node.left)
        if node.right:
            pals += dfs(node.right)
        path[node.val] -= 1
        return pals

    return dfs(root)


# Time complexity: O(n) <- n - number of Nodes inside input BT `root`.
# W.e the case, we're always traversing whole BT, once => O(n).
# But, extra to this we're always extra traversing all values of Nodes we visited.
# And w.e the # of occurrences we're always having 1-9 values as keys in dict `path`, so we can call it constant.
# --------------------------
# Auxiliary space: O(n).
# If out BT in style of LinkedList, then we will have recursion stack of size `n`.
# And our dict `path` is always at max having 1-9 digits stored as keys, so we can call it constant.
# It depends on input `root` and values in it, but it's still linear => O(n).


test_vals: list[int] = [2, 1, 1, 1, 3, None, None, None, None, None, 1]
test: TreeNode = build_from_level_order(test_vals)
assert level_order_read(test) == test_vals
test_out: int = 1
assert test_out == pseudo_palindromic_paths(test)

test_vals = [2, 3, 1, 3, 1, None, 1]
test = build_from_level_order(test_vals)
assert level_order_read(test) == test_vals
test_out = 2
assert test_out == pseudo_palindromic_paths(test)

test_vals = [9]
test = build_from_level_order(test_vals)
assert level_order_read(test) == test_vals
test_out = 1
assert test_out == pseudo_palindromic_paths(test)

test_vals = [randint(1, 9) for _ in range(10 ** 5)]
print(test_vals)
