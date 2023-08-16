# Given the root of a binary tree and an integer targetSum,
#   return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards
#   (i.e., traveling only from parent nodes to child nodes).
# ---------------
# The number of nodes in the tree is in the range [0, 1000].
# -10 ** 9 <= Node.val <= 10 ** 9
# -1000 <= targetSum <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, targetSum: int) -> int:
    # working_sol (96.14%, 69.45) -> (49ms, 17.7mb)  time: O(n) | space: O(n)
    # Empty BT, no path possible.
    if not root:
        return 0
    # (0: 1) <- pair to get first node,
    # cuz we're checking node.val + all_before
    # with First node all_before == 0, and we need this
    # option to be considered and give us +1 correct path.
    # Same goes not only for the first node, but any node
    # with all_before + node.val == targetSum.
    # In other word FULL_PATH == targetSum.
    path_sums: dict[int, int] = {0: 1}

    def inorder(node: TreeNode, path: int = 0, correct: int = 0) -> int:
        # Full SUM path from ROOT to this node included.
        cur_path: int = node.val + path
        # SUM of nodes, in our case oneway is always:
        # node1 + node2 ... node?? <- we memorize all options,
        # so if we take FULL path so far and take target from it
        # that will give us SUM we could use to check correct path.
        # And because we store every SUM on this oneway.
        # We can check if there's something equal stored,
        # and if there's correct value. Then somewhere before this Node,
        # exist some sequence of nodes with their SUM == OPTION,
        # and if we remove them we would get correct_path.
        option: int = cur_path - targetSum
        # Always check before storing cur_path,
        # otherwise with pathSum == 0, we will count
        # every possible node as correct_path.
        if option in path_sums:
            correct += path_sums[option]
        # Store|Increment -> current_path we made so far,
        # from ROOT to the call Node.
        if cur_path in path_sums:
            path_sums[cur_path] += 1
        else:
            path_sums[cur_path] = 1
        if node.left:
            correct += inorder(node.left, cur_path)
        if node.right:
            correct += inorder(node.right, cur_path)
        # On the way backwards, we need to decrease count for
        # current_path, because it's not available anymore.
        # We're going into another subtree or ending.
        # And we allowed only count ways from TOP -> Bottom,
        # with only 1 turn left|right.
        path_sums[cur_path] -= 1
        return correct

    return inorder(root)


# Time complexity: O(n) -> using every node only once, worst case BT with only 1 subtree => O(n).
# n - node in input_BT^^|
# Auxiliary space: O(n) -> for case with BT, with only 1 subtree -> like linked_list, every node will have cur_path
#                          stored and recursion stack will be the same size of 'n' => O(2n).
# ---------------
# Every sum of nodes is node1 + node2 + w.e nodes, so we can just store every sum,
# and find SUM - target, and if there's something hit we can assume there's some nodes
# which can be deleted from a path and their sum is equal to this diff.
# Check every node and count this hits.
