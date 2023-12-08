# Given the root of a binary tree, construct a string consisting of parenthesis
#  and integers from a binary tree with the preorder traversal way, and return it.
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship
#  between the string and the original binary tree.
# ------------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -1000 <= Node.val <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_string(root: TreeNode) -> str:
    # working_sol (89.13%, 87.81%) -> (46ms, 18.67mb)  time: O(n) | space: O(n)
    if not root:
        return ''
    out: str = ''

    def preorder(node: TreeNode) -> None:
        # Essentially all we care: 'node(left_child(w.e inside))(right_child(w.e inside))'
        # With extra rules:
        #  - No childs => no openers just value.
        #  - No left child but right child => one-to-one mapping with placeholder, '()' instead of left_child.
        #  - No right child => opener and insides for only left_child.
        nonlocal out
        if not node.left and not node.right:
            out += f'{node.val}'
            return
        out += f'{node.val}'
        if node.left:
            out += '('
            preorder(node.left)
            out += ')'
        if not node.left and node.right:
            out += '()'
        if node.right:
            out += '('
            preorder(node.right)
            out += ')'

    preorder(root)
    return out


# Time complexity: O(n) <- n - number of Nodes inside BinaryTree.
# We're always traversing all Nodes of the BT.
# ------------------------
# Auxiliary space: O(n)
# We're saving every Node value we have into a string + extra symbols for brackets, but it's constant.
# Because for every Node we're saving pairs like: (node.val).
# Even if we don't have left_child but still have right_child we will store '()' instead.
# So, in the worst case if we have all Nodes without left_child, we're going to have (2 * n) pairs in string.
