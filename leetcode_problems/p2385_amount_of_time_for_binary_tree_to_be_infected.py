# You are given the root of a binary tree with unique values, and an integer start.
# At minute 0, an infection starts from the node with value start.
# Each minute, a node becomes infected if:
#   - The node is currently uninfected.
#   - The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.
# -----------------------
# The number of nodes in the tree is in the range [1, 10 ** 5].
# 1 <= Node.val <= 10 ** 5
# Each node has a unique value.
# A node with a value of start exists in the tree.
from collections import deque
from collections import defaultdict


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
        if not cur_node:
            continue
        if index < len(nodes):
            if nodes[index]:
                cur_node.left = TreeNode(nodes[index])
                que.append(cur_node.left)
            else:
                cur_node.left = None
        index += 1
        if index < len(nodes):
            if nodes[index]:
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
        if not cur_node:
            nodes.append(None)
            continue
        nodes.append(cur_node.val)
        que.append(cur_node.left)
        que.append(cur_node.right)
    while nodes[-1] is None:
        nodes.pop()
    return nodes


def amount_of_time(root: TreeNode, start: int) -> int:
    # working_sol (93.30%, 77.28%) -> (375ms, 63.18mb)  time: O(n) | space: O(n)
    # {Node: edges}, max 3 edges (parent, left child, right child), so we might use tuple() but w.e.
    und_graph: dict[int, list[int]] = defaultdict(list)

    def dfs(node: TreeNode) -> None:
        # Build undirected Graph from BT.
        # Every parent points to every child, every child points to every parent.
        if node.left:
            und_graph[node.val].append(node.left.val)
            und_graph[node.left.val].append(node.val)
            dfs(node.left)
        if node.right:
            und_graph[node.val].append(node.right.val)
            und_graph[node.right.val].append(node.val)
            dfs(node.right)

    dfs(root)
    # Standard BFS with delimiter to get maximum distance we can travel from infected Node.
    out: int = -1
    que: deque[int | None] = deque([start, None])
    visited: set[int] = {start}
    while que:
        cur_node: int = que.popleft()
        if cur_node is None:
            out += 1
            if que:
                que.append(None)
            continue
        for edge in und_graph[cur_node]:
            if edge not in visited:
                que.append(edge)
                visited.add(edge)
    return out


# Time complexity: O(n) <- n - number of Nodes in input BT.
# First we traverse whole BT to build undirected graph `und_graph` => O(n).
# Second, we traverse `und_graph` with BFS, to get maximum distance we can travel.
# To get this distance, we always traverse whole graph `und_graph`,
#  and # of Nodes in him is equal to number of Nodes in BT => O(n).
# -----------------------
# Auxiliary space: O(n).
# First we use dfs() to build `und_graph` and in the worst case this BT will be like a linked list.
# So, recursion stack == `n` => O(n).
# Dictionary for undirected graph `und_graph` will always hold every Node and edges to it.
# Because we can have only 3 edges (parent, left child, right child), we can say it constant.
# So, dictionary will have `n` keys => O(n).
# We use BFS with deque `que` to traverse whole `und_graph`, and we will allocate space for every
#  Node we add into the `que` => O(n).
# Extra to this set `visited` will hold every Node we visit, and we always visit all Nodes => O(n).
# -----------------------
# See how it can be done with Graph, but why bother and double traverse.
# If we can just find how many levels beneath infected Node and above it?
# We can just know subtrees of ROOT and on which level infected positioned.
# And decide on that, let's test.
# Seems working but need more test_cases, let's fail.
# -----------------------
# Incorrect, because we can have cases when we need to cover not just levels, but neighbour Nodes.
# And they will be missed if we just consider levels. So, it's better to use Graph and just BFS to get
#  maximum distance we need to cover.


test: list[int] = [1, 5, 3, None, 4, 10, 6, 9, 2]
test_tree: TreeNode = bt_from_level_order(test)
assert read_level_order(test_tree) == test
test_start: int = 3
test_out: int = 4
assert test_out == amount_of_time(test_tree, test_start)

test = [1]
test_tree = bt_from_level_order(test)
assert read_level_order(test_tree) == test
test_start = 1
test_out = 0
assert test_out == amount_of_time(test_tree, test_start)

test = [
    1, 5, 3, None, 4, 10, 6, 9, 2, 11, 33, 44, 55, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 27, 111, 1111, 123, 1234
]
test_tree = bt_from_level_order(test)
assert read_level_order(test_tree) == test
test_start = 1111
test_out = 9
assert test_out == amount_of_time(test_tree, test_start)

test = [1, None, 2, 3, 4, None, 5]
test_tree = bt_from_level_order(test)
assert read_level_order(test_tree) == test
test_start = 4
test_out = 3
assert test_out == amount_of_time(test_tree, test_start)
