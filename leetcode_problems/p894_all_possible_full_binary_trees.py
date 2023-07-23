# Given an integer n, return a list of all possible full binary trees with n nodes.
# Each node of each tree in the answer must have Node.val == 0.
# Each element of the answer is the root node of one possible tree.
# You may return the final list of trees in any order.
# A full binary tree is a binary tree where each node has exactly 0 or 2 children.
# -------------------
# 1 <= n <= 20


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_possible_fbt(n: int) -> list[TreeNode]:
    # working_sol (19.84%, 20.7%) -> (232ms, 26.1mb)  time: O(2 ** n) | space: O(k * 2 ** n)
    all_bts: list[TreeNode] = []
    # If all given nodes are EVEN, we can't
    # build COMPLETE BT, there's always going to be leftover.
    # And we need to use EVERY given node.
    if n % 2 == 0:
        return all_bts
    # First node used as ROOT.
    root: TreeNode = TreeNode(val=0)
    all_available: int = n - 1
    # If there's no node available after creating of the ROOT,
    # we can't build anything else.
    if all_available == 0:
        all_bts.append(root)
        return all_bts

    def build_sub(nodes: int) -> list[TreeNode]:
        if nodes in alr_build:
            return alr_build[nodes]
        # Actual copy of everything, I will need to rebuild it
        # if it's working correctly.
        all_subs: list[TreeNode] = []
        if nodes % 2 == 0:
            return all_subs
        sub_root: TreeNode = TreeNode(val=0)
        if nodes == 1:
            all_subs.append(sub_root)
            return all_subs
        # -1 node for the root^^
        nodes -= 1
        left_nodes: int = nodes - 1
        right_nodes: int = 1
        left_subs: list[TreeNode] = []
        right_subs: list[TreeNode] = []
        while left_nodes >= 1:
            for _ in build_sub(left_nodes):
                left_subs.append(_)
            for _ in build_sub(right_nodes):
                right_subs.append(_)
            left_nodes -= 2
            right_nodes += 2
            for left_sub in left_subs:
                for right_sub in right_subs:
                    new_root: TreeNode = TreeNode(val=0, left=left_sub, right=right_sub)
                    all_subs.append(new_root)
            left_subs.clear()
            right_subs.clear()
        alr_build[nodes] = all_subs
        return all_subs

    # Right/Left subtrees can be a copies of each other with some node values.
    # Like -> left_nodes == 5, right_nodes == 3
    # after some iterations => left_nodes == 3, right_nodes == 5
    # We're building from NEW_ROOT, so it's always the same SUBTREE
    # just placed on Left/Right sides. We can just reuse it.
    alr_build: dict[int, list[TreeNode]] = {}
    # ROOT + LEFTsub + RIGHTchild <- default tree
    left_sub_nodes: int = all_available - 1
    right_sub_nodes: int = 1
    # Constructed LEFT subtree with set left/right nodes.
    left_sub_trees: list[TreeNode] = []
    # Constructed RIGHT subtree with set left/right nodes.
    right_sub_trees: list[TreeNode] = []
    while left_sub_nodes >= 1:
        # Building of left/right subtrees
        for _ in build_sub(left_sub_nodes):
            left_sub_trees.append(_)
        for _ in build_sub(right_sub_nodes):
            right_sub_trees.append(_)
        # Always need to take 2 nodes from left or right,
        # we're switching nodes from left to right.
        left_sub_nodes -= 2
        right_sub_nodes += 2
        # Permutations of all constructed SUBTREES between themselves,
        # set as childs of a new_root.
        for left_tree in left_sub_trees:
            for right_tree in right_sub_trees:
                new_root_: TreeNode = TreeNode(val=0, left=left_tree, right=right_tree)
                all_bts.append(new_root_)
        # Clearing subtrees, cuz we're getting new
        # node values for every build_call.
        left_sub_trees.clear()
        right_sub_trees.clear()
    return all_bts


# Time complexity: O(2 ** n) -> we need all permutations of n given nodes => O(2 ** n).
# n - input nodes_value^^|
# Auxiliary space: O(k * 2 ** k) -> extra space to store every possible permutations of created subs with k nodes,
# k - nodes used to build subtree^^| in alr_build (all of them are correct % 2 != 0) => O(k * 2 ** k) ->
#                                -> recursion stack, should be something like O(2 ** (k - 1)) => because we're using
#                                every of given k nodes to build, except one to keep balance between left/right
#                                and recalling for every combination and permuting them.
# ^^My view, but I doubt it's correct, because this Recursion/DP problems is still pretty HARD for me
#   and I need to learn more about it.
# -------------------
# If we're given some n nodes to construct BT from it, it's easy to construct SUBTREES from them,
# but how we can get all permutations?
# Like for just some SUBTREE ->
# -> n <- all available nodes, and we should place them as 2 or 0 childs.
# -> First it's always should be 2 to use as childs and 1 as root. n >= 3 to build correct subtree.
# -> n == 3, root = 1 + l_child = 1 + r_child = 1 -> correct full populated subtree.
# But we need 2 subtrees for a root or any other node we're going to build from,
# and still how we can combine them between?
# Like default permutation is take everything from 1 list(or w.e) and combine it
# with everything in 2 list. But if we're creating subtrees from root we will just get 2 subtrees.
# Build subtrees for every node as root and permutate them between themselves immediately?
# Ok. So we need to use some part of the all given nodes for left_sub and (all - left_sub) nodes for right,
# to get all options we need to use all nodes on left side and all nodes on right side + everything between.
# Like -> all == 9, root == 1, left_used == 8, right_used == 0 <- unbalanced from the root,
# so every step should take 3 nodes -> left_used == 5 , right_used == 3 <- now it's correct
# and there's 2 options left_used == 3 and right_used == 5 for permutations.
# So we need to use every node combinations possible for left and right subtrees and permute them between.
# Should be correct.
# Extra we can't build COMPLETE tree from EVEN number, so it's insta return. Because it's always ROOT+LEFT+RIGHT == 3.
