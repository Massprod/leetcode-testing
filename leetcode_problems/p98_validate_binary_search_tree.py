# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#  1) The left subtree of a node contains only nodes with keys less than the node's key.
#  2) The right subtree of a node contains only nodes with keys greater than the node's key.
#  3) Both the left and right subtrees must also be binary search trees.
# ---------------------
# The number of nodes in the tree is in the range [1, 10 ** 4].
# -2 ** 31 <= Node.val <= 2 ** 31 - 1


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:
    # working_sol (37.55%, 95.32%) -> (64ms, 18.7mb)  time: O(n) | space: O(log n)

    def inorder(node: TreeNode, l_limit: list[int], r_limit: list[int]) -> bool:
        # checking correct TYPE for rule #3
        if node.left or node.right:
            if type(node.left) is not TreeNode and type(node.right) is not TreeNode:
                return False
        # left_turn
        # l_limit -> holds every node value which is higher than our current_node
        #             and current_node is in it LEFT SUBTREE
        if node.left:
            if node.left.val < node.val:
                l_limit.append(node.val)
                for _ in l_limit:
                    if not node.left.val < _:
                        return False
                for _ in r_limit:
                    if not node.left.val > _:
                        return False
                if not inorder(node.left, l_limit, r_limit):
                    return False
                l_limit.pop()
            else:
                return False
        # right_turn
        # r_limit -> holds every node value which is lower than out current_node
        #             and current_node is in it RIGHT SUBTREE
        if node.right:
            if node.right.val > node.val:
                r_limit.append(node.val)
                for _ in l_limit:
                    if not node.right.val < _:
                        return False
                for _ in r_limit:
                    if not node.right.val > _:
                        return False
                if not inorder(node.right, l_limit, r_limit):
                    return False
                r_limit.pop()
            else:
                return False
        return True

    return inorder(root, [], [])


# Time complexity: O(n) -> somewhat in_order traversal of whole input_BT, once => O(n).
# n - nodes in input_BT^^|
# Auxiliary space: O(log n) -> nothing extra used, only operating with links to original nodes, but recursion stack
#                          is still taking some space, to store every node_link, and limits => O(n + log n) ->
#                          -> if we consider links to be constant and ignored, than only limits should be
#                          considered, and it's O(log n), because only part of original nodes from input_BT
#                          will be added => O(log n).
# ---------------------
# Flow:
#   Most hard part was to understand how we can limit subtree_values, using l_limit and r_limit for that.
#   l_limit -> holds every node value which is higher than our current_node and current_node is in it LEFT SUBTREE.
#   r_limit -> holds every node value which is lower than out current_node and current_node is in it RIGHT SUBTREE.
#   first we check every possible left_turn from root (because I'm stuck with in_order traversal) ->
#   ( don't know how to call it more correctly, like we go deeper not side_ways, but w.e)
#   -> on this first_step we can only filter on what is in l_limit, and node_values only appended in l_limit
#      if we can make this left_turn from the node. In better words nodes from which we can make a left_turn. ->
#   -> after checking every left_turn from root, we're returning from it with the same path, but if on the way back
#      we can make RIGHT_TURN than we're making it, and value of every node from which we can make this turn
#      is going to be added into r_limit -> now we can filter on both options, we need to have every value in
#      RIGHT SUBTREE to be lower than any value in l_limit and higher than any value in r_limit ->
#   -> this all allows us to check only LEFT SIDE of the root ->
#   second we check everything on the RIGHT SIDE of root -> same approach as before, but now we're just
#      made only ONE big turn from root, it's the same approach for every node on the back_path ->
#   -> but now it's RIGHT TURN from root.
#   So in the end, we're checking every possible node until we can make LEFT_TURN, and after that checking
#   every possible RIGHT_TURN on the way back, including root itself. After that place of the starting_node,
#   is changed and we're just repeating.
#   !
#   Totally need to learn more methods to read BTs, because I'm only familiar with in_order, and maybe there's
#   better/simplier way to do tasks like this. !
# ---------------------
# Well, guess Medium with BT is standard Hard :)
# Rebuild first build -> because there was a problem with considering PATH,
#   we should always consider values we meet before, and I wasn't.
# After testing on this: [26,24,30,14,25,27,32,13,18,null,null,null,null,null,null,null,null, 16, 20, 15, 17]
# First build is failed, and actually whole new solution is build on that test_case.
# Using Leetcode to build test_cases and test them, because there's no reason to make function to populate BT.
# Maybe later, or there should be a task for that.
# ---------------------
# !
# Both the left and right subtrees must also be binary search trees. !
# ^^Made extra check for type of what stored in node.left, node.right.
# ---------------------
# If understood correctly, all we need is just check EVERY node for 1, 2 cases.
# Every node should be like that ->  node.left.val < node.val < node.right.val
# Shouldn't matter in which way we're reading, just break when this rule isn't correct.
# Incorrect ! THE LEFT SUBTREE ! so every node in left and right subtree should be compared to root?
# Or NODE is changing every time we change it?
