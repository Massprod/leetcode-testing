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
