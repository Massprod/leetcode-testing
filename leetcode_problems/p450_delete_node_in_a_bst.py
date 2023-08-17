# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
#   - Search for a node to remove.
#   - If the node is found, delete the node.
# --------------------
# The number of nodes in the tree is in the range [0, 10 ** 4].
# -10 ** 5 <= Node.val <= 10 ** 5
# Each node has a unique value.
# root is a valid binary search tree.
# -10 ** 5 <= key <= 10 ** 5


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root: TreeNode, key: int) -> TreeNode:
    # working_sol (94.69%, 51.14%) -> (64ms, 20.8mb)  time: O(n) | space: O(n)
    if not root:
        return root

    def delete(node: TreeNode) -> None | bool:
        # No childs node need to be reassigned differently.
        if not node.left and not node.right:
            return True
        # If node have only right child ->
        elif not node.left:
            # -> we can just switch values with this child and reset pointers:
            # DeletedNode is not actually deleted, but its value changed.
            # And now it should point correctly to childs of its node.right child.
            node.val, node.right, node.left = node.right.val, node.right.right, node.right.left
        # Same goes for left child.
        elif not node.right:
            node.val, node.left, node.right = node.left.val, node.left.left, node.left.right
        # Check if we can replace DeleteNode with just his childs, without
        # searching for Min|Max in them.
        elif node.left and not node.left.right:
            node.val = node.left.val
            node.left = node.left.left
        elif node.right and not node.right.left:
            node.val = node.right.val
            node.right = node.right.right
        # If there's 2 childs. Then we need to find maximum in his LeftSubtree(child),
        # or minimum in his RightSubtree(child). Either of them will work for replacement.
        elif node.left and node.left.right:
            # If there's right child we need to find maximum in it.
            cur_node: TreeNode | None = node.left
            # Same problem, we can't just find some last node == maximum.
            # We need to find node which points on this node
            #  and reassign last_node childs to it.
            while cur_node.right.right:
                cur_node = cur_node.right
            if cur_node.right.left:
                node.val, cur_node.right = cur_node.right.val, cur_node.right.left
            # Or don't if he doesn't have any. Then its just points to None.
            else:
                node.val, cur_node.right = cur_node.right.val, None

    def search(node: TreeNode) -> None | bool:
        if not node:
            return
        if node.val == key:
            # We can't just make node == None,
            # nodes which pointing on it will still have connection.
            # So we need to reassign them. If there's no childs
            # for deletion node we need to reassign it for previous node.
            if delete(node):
                return True
        if key > node.val:
            # Reassign pointer.
            # Pointer == Node pointing on target node.
            if search(node.right):
                node.right = None
                return
        if key < node.val:
            if search(node.left):
                node.left = None
                return
    # BST with only 1 node.
    if not root.left and not root.right:
        if root.val == key:
            root = None
        return root
    search(root)
    return root


# Time complexity: O(n) -> search for a correct Node is standard BST => O(log n) ->
# n - nodes of input_BST^^| -> and search for minimum|maximum in left|right subtrees is also only a part => O(log n) ->
#                           -> but in the worst case I need to rebuild, or it's still full search and then O(n) ->
#                           -> like, case with deleting a node with Left + Right child and Left child is having
#                           right child as well, and this RightSubtree will have only 1 line with w.e number of nodes,
#                           we will traverse all of these nodes to get Minimum => O(n).
#                           Ok. Changed, now we will check if there's way to replace it with Right|Left child,
#                           without searching in them. Now it should be faster in some cases, but still should be O(n).
#                           Because some cases with just 3 nodes and we need to delete some leaf, which is actually a
#                           node == 3. So everything will be used once anyway. On median Θ(log n).
# Auxiliary space: O(n) -> if we traverse everything, then we're store everything in a stack => O(n).
# --------------------
# Ok. Done. Not good-looking, but working solution. Pretty sure there's better standard way of doing it.
# But if I'm capable of doing this on my own it's better to delay googling.
# Basic rule is that, I don't know or there no way to delete node just by node == None,
# we need to reassign nodes which pointing it to new ones.
# And every node we're deleting if it's having any Left child with Right child in it,
# we need to find maximum value in this child, otherwise it will conflict with BST standard.
# Every parent having Less values in left_subtree and higher in right_subtree.
# Same goes for right_child of delete Node, but now we need minimum value in this subtree.
# And if there's no childs we can just delete this node, reassign it as None for pointer.
