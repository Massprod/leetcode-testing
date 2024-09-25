from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        node_string: str = f'Node: {self.val}\n'
        if self.left:
            node_string += f'    Left: {self.left.val}\n'
        else:
            node_string += f'    Left: None\n'
        if self.right:
            node_string += f'    Right: {self.right.val}\n'
        else:
            node_string += f'    Right: None\n'
        node_string += '-' * 20
        return node_string


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


def bst_from_preorder(
        preorder: list[int],
        index: list[int],
        min_val: int | float = float('-inf'),
        max_val: int | float = float('inf')
) -> TreeNode | None:

    if len(preorder) <= index[0]:
        return None
    cur_val: int = preorder[index[0]]
    if not (min_val < cur_val < max_val):
        return None
    node: TreeNode = TreeNode(cur_val)
    index[0] += 1
    if index[0] < len(preorder):
        node.left = bst_from_preorder(preorder, index, min_val, cur_val)
        node.right = bst_from_preorder(preorder, index, cur_val, max_val)
    return node
