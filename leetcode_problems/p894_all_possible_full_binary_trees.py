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
    # working_sol (96.69%, 70.58%) -> (168ms, 20.06mb)  time: O(2 ** n) | space: O(k * 2 ** k)
    # Right/Left subtrees can be a copies of each other with some node values.
    # Like -> left_nodes == 5, right_nodes == 3
    # after some iterations => left_nodes == 3, right_nodes == 5
    # We're building from NEW_ROOT, so it's always the same SUBTREE
    # just placed on Left/Right sides. We can just reuse it.
    alr_build: dict[int, list[TreeNode]] = {}

    def build_sub(nodes: int) -> list[TreeNode]:
        if nodes in alr_build:
            return alr_build[nodes]
        all_subs: list[TreeNode] = []
        if nodes % 2 == 0:
            return all_subs
        if nodes == 1:
            return [TreeNode(val=0)]
        # ROOT + LEFTsub + RIGHTchild <- default tree
        # Always should be odd to even start building,
        # root is taking -1 first,
        # so it's always even after it.
        # We can always take extra -1 to get correct
        # left subtree available nodes:
        left_avail_nodes: int = nodes - 2
        # Right is by default at least == 1.
        right_avail_nodes: int = 1
        while left_avail_nodes >= 1:
            # Constructed LEFT subtree with set left/right node values.
            left_subs: list[TreeNode] = build_sub(left_avail_nodes)
            # Constructed RIGHT subtree with set left/right node values.
            right_subs: list[TreeNode] = build_sub(right_avail_nodes)
            # To keep BT complete we need to switch 2 nodes from left or right subtrees.
            # We're using LEFT -> RIGHT switch:
            left_avail_nodes -= 2
            right_avail_nodes += 2
            # Building ROOT + LEFT + RIGHT subtrees, with all possible permutations
            # of LEFT + RIGHT subs, with duplicates, because they can be MIRRORED.
            for left_sub in left_subs:
                for right_sub in right_subs:
                    new_root: TreeNode = TreeNode(val=0, left=left_sub, right=right_sub)
                    all_subs.append(new_root)
        # Store permutations for used node_value.
        alr_build[nodes] = all_subs
        return all_subs

    return build_sub(n)


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
