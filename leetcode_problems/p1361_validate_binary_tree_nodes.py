# You have n binary tree nodes numbered from 0 to n - 1
#  where node i has two children leftChild[i] and rightChild[i],
#  return true if and only if all the given nodes form exactly one valid binary tree.
# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
# Note that the nodes have no values and that we only use the node numbers in this problem.
# ---------------------
# n == leftChild.length == rightChild.length
# 1 <= n <= 10 ** 4
# -1 <= leftChild[i], rightChild[i] <= n - 1
from collections import deque


def validate_bt_nodes(n: int, leftChild: list[int], rightChild: list[int]) -> bool:
    # working_sol (75.75%, 43.11%) -> (265ms, 19.6mb)  time: O(n) | space: O(n)
    que: deque[int] = deque()
    left_childs: set[int] = set(leftChild)
    right_childs: set[int] = set(rightChild)
    # DFS|BFS we still need to find Root first.
    for node in range(n):
        # Root can't be a child.
        if (node in left_childs) or (node in right_childs):
            continue
        # And correct BT can't have more than 1.
        if que:
            return False
        que.append(node)
    # Standard BFS.
    visited: set[int] = set()
    while que:
        cur_node: int = que.popleft()
        # Cycle or two pointers.
        if cur_node in visited:
            return False
        if leftChild[cur_node] >= 0:
            que.append(leftChild[cur_node])
        if rightChild[cur_node] >= 0:
            que.append(rightChild[cur_node])
        visited.add(cur_node)
    # ! n == leftChild.length == rightChild.length !
    # Every Node used == correct BT.
    return len(visited) == len(leftChild)


# Time complexity: O(n) -> ! n == leftChild.length == rightChild.length ! traverse of both input arrays => O(2n) ->
# n - input value 'n'^^|  -> standard BFS to check all Nodes we have == 'n' => O(n).
# Auxiliary space: O(n) -> worst case == correct BT with all Nodes used -> tree sets with length == 'n' => O(3n) ->
#                          -> extra list 'que' with all nodes used as well => O(4n).
# ---------------------
# It's not validate Binary SEARCH Tree, so it is just check of 3 conditions:
#  1) No more than 1 root == Nodes without parent.
#  2) No more than 1 parent for every Node.
#  3) No Nodes which points to its parent == cycle.
# DFS|BFS should be enough for this. But we need to find ROOT's first.
# Only way I see is just check all 'n' Nodes if something isn't presented in childs == ROOT.
# Let's try.


test_n: int = 4
test_left: list[int] = [1, -1, 3, -1]
test_right: list[int] = [2, -1, -1, -1]
test_out: bool = True
assert test_out == validate_bt_nodes(test_n, test_left, test_right)

test_n = 4
test_left = [1, -1, 3, -1]
test_right = [2, 3, -1, -1]
test_out = False
assert test_out == validate_bt_nodes(test_n, test_left, test_right)

test_n = 2
test_left = [1, 0]
test_right = [-1, -1]
test_out = False
assert test_out == validate_bt_nodes(test_n, test_left, test_right)
