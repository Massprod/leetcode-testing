# One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node,
#  we record the node's value. If it is a null node, we record using a sentinel value such as '#'.
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#",
#  where '#' represents a null node.
# Given a string of comma-separated values preorder,
#  return true if it is a correct preorder traversal serialization of a binary tree.
# It is guaranteed that each comma-separated value in the string must be either an integer
#  or a character '#' representing null pointer.
# You may assume that the input format is always valid.
#  - For example, it could never contain two consecutive commas, such as "1,,3".
# Note: You are not allowed to reconstruct the tree.
# -----------------------
# 1 <= preorder.length <= 10 ** 4
# preorder consist of integers in the range [0, 100] and '#' separated by commas ','.


def is_valid_serialization(preorder: str) -> bool:
    # working_sol (89.63%, 7.04%) -> (31ms, 16.80mb)  time: O(n) | space: O(n)
    # preorder == Node -> left child (becomes Node) -> right child (becomes Node)
    preorder_values: list[str] = preorder.split(',')
    limit: int = len(preorder_values) - 1
    if 0 == limit:
        # We allow EMPTY tree == ['#']
        if '#' == preorder_values[0]:
            return True
        # But we don't allow the single Node tree.
        return False

    def check(node_ind: int) -> int:
        nonlocal limit
        nonlocal preorder_values
        # Out of bounds.
        # Subtree doesn't end with left and right childs == #.
        if limit < node_ind:
            return 0
        if '#' == preorder_values[node_ind]:
            return node_ind
        # Check the whole left subtree.
        # Last node == return index == right subtree starts from it.
        left_child_end: int = check(node_ind + 1)
        if not left_child_end:
            return 0
        # Check whole right subtree.
        right_child_end: int = check(left_child_end + 1)
        if not right_child_end:
            return 0
        return right_child_end

    out = check(0)
    # True == we used every Node from a tree.
    # False == we don't use every Node from a tree.
    return True if out == limit else False


# Time complexity: O(n) <- n - length of the input string `preorder`.
# Always traversing whole input string `preorder`, once => O(n).
# -----------------------
# Auxiliary space: O(n)
# In the worst case there's only left child of `root`.
# Recursion stack will be of size `n` => O(n).


test: str = "9,3,4,#,#,1,#,#,2,#,6,#,#"
test_out: bool = True
assert test_out == is_valid_serialization(test)

test = "1,#"
test_out = False
assert test_out == is_valid_serialization(test)

test = "9,#,#,1"
test_out = False
assert test_out == is_valid_serialization(test)
