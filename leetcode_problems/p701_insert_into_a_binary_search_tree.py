# You are given the root node of a binary search tree (BST) and a value to insert into the tree.
# Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion,
#  as long as the tree remains a BST after insertion.
# You can return any of them.
# -------------------
# The number of nodes in the tree will be in the range [0, 10 ** 4].
# -10 ** 8 <= Node.val <= 10 ** 8
# All the values Node.val are unique.
# -10 ** 8 <= val <= 10 ** 8
# It's guaranteed that val does not exist in the original BST.


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    # working_sol (82.28%, 91.22%) -> (108ms, 19mb)  time: O(n) | space: O(n)
    if not root:
        return TreeNode(val)

    # ! It's guaranteed that val does not exist
    #   in the original BST. !
    # We're given correct BST.
    # And we need to return correct BST.
    # So, there's 100% will be a placement option.
    # And we can either shift some child_node and insert
    #  between him and his parent, or just place as some leaf.
    def check(node: TreeNode) -> None:
        if node.val > val:
            if node.left:
                check(node.left)
            else:
                node.left = TreeNode(val)
        if node.val < val:
            if node.right:
                check(node.right)
            else:
                node.right = TreeNode(val)

    check(root)
    return root


# Time complexity: O(n) -> worst case == BST with style of linked list, and we're given LOWER than the lowest value ->
# n - number of nodes in BST^^| -> so we will traverse whole BST and insert left_leaf => O(n).
# Auxiliary space: O(n) -> same worst case, our recursion stack will be of n size => O(n).
# -------------------
# Classic failed commit with BT problem. ! ALWAYS CHECK FOR 0 Nodes CONSTRAINT !
# -------------------
# We're given correct BST, and we need to return correct BST.
# So there's 100% chance that we will have a placement for our value.
# And it's either shifting nodes and placing a new one between them, which is too much bother.
# Or we can just always place new Node as a Leaf.
# At least I don't see any case when we couldn't.
# Should be correct to just traverse until empty leaf_spot of some node with lower|higher value than our input_value.
