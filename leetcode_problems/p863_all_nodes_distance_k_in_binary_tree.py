# Given the root of a binary tree, the value of a target node target, and an integer k,
#   return an array of the values of all nodes that have a distance k from the target node.
# You can return the answer in any order.
# ---------------------
# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    if k == 0:
        return [target.val]
    k_values: list[int] = []

    def root_distance(node: TreeNode) -> str | bool:
        # find in which subtree target is
        if node.val == target.val:
            return True
        if node.left:
            if root_distance(node.left):
                return "left"
        if node.right:
            if root_distance(node.right):
                return "right"

    def inorder_beneath(node: TreeNode, found: bool = False, distance: int = 0,
                        left_s: bool = False, right_s: bool = False) -> bool | [int, bool]:
        if distance == k:
            k_values.append(node.val)
            return distance, True
        if node.val == target.val:
            found = True
        # if target in left subtree
        if left_s:
            if node.left:
                if found:
                    inorder_beneath(node.left, found, distance + 1, left_s, right_s)
                else:
                    distance, found = inorder_beneath(node.left, left_s=left_s)
                    if distance >= 0 and found:
                        distance += 1
                    if distance == k:
                        k_values.append(node.val)
            if node.right:
                if found:
                    inorder_beneath(node.right, found, distance + 1, left_s, right_s)
                else:
                    distance, found = inorder_beneath(node.right, left_s=left_s)
                    if distance >= 0 and found:
                        distance += 1
                    if distance == k:
                        k_values.append(node.val)
            if found:
                return distance, True
            return distance, False
        # if target in right subtree
        if right_s:
            if node.right:
                if found:
                    inorder_beneath(node.right, found, distance + 1, left_s, right_s)
                else:
                    distance, found = inorder_beneath(node.right, right_s=right_s)
                    if distance >= 0 and found:
                        distance += 1
                    if distance == k:
                        k_values.append(node.val)
            if node.left:
                if found:
                    inorder_beneath(node.left, found, distance + 1, left_s, right_s)
                else:
                    distance, found = inorder_beneath(node.left, right_s=right_s)
                    if distance >= 0 and found:
                        distance += 1
                    if distance == k:
                        k_values.append(node.val)
            if found:
                return distance, True
            return distance, False

    target_subtree: str = root_distance(root)
    if target_subtree == "left":
        inorder_beneath(root, left_s=True)
    else:
        inorder_beneath(root, right_s=True)
    return k_values
