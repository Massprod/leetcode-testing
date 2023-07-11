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


def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int] | set[int]:
    # working_sol (5%, 59.10%) -> (132ms, 16.8mb)  time: O(n + K * S) | space: O(log n)
    if k == 0:
        return [target.val]
    k_values: set[int] = set()
    visited: set[int] = set()

    def target_sub(node: TreeNode) -> str | bool:
        # find in which subtree target is
        if node.val == target.val:
            return True
        if node.left:
            if target_sub(node.left):
                return "left"
        if node.right:
            if target_sub(node.right):
                return "right"

    def inorder_beneath(node: TreeNode, found: bool = False, distance: int = 0,
                        left_s: bool = False, right_s: bool = False) -> bool | tuple[int, bool]:
        # there's 2 options when distance is correct in this solution:
        # for left_s, target in a left_subtree of the ROOT
        # first -> if we found target in a left_subtree of inner_node, than we're going to
        #   check every right_subtree of a backtrack_nodes and distance will
        #   be correct from target -> current_node.
        # second -> if we found target in a right_subtree of inner_node, then we need to
        #   recheck whole left_subtree of this node, because we're doing in_order traversal,
        #   and because of that every other node on backtrack will be rechecked as well.
        #   But distance from them will be counted in the same way as from target,
        #   which is why we need to save visited from left_subtree.
        # For the right_s it's the same, but all mirrored.
        if distance == k and node.val not in visited:
            k_values.add(node.val)
            return True
        if node.val == target.val:
            found = True
        # if target in left subtree
        if left_s:
            # reading in order whole BT to find target
            # if we find target, and it's left_leaf then we can just backtrace
            # and check every right_subtree on the nodes on the way -> from target to root
            if node.left:
                if found:
                    inorder_beneath(node.left, found, distance + 1, left_s, right_s)
                else:
                    distance, found = inorder_beneath(node.left, left_s=left_s)
                    if distance >= 0 and found:
                        distance += 1
                    if distance == k:
                        k_values.add(node.val)
            if node.right:
                if found:
                    inorder_beneath(node.right, found, distance + 1, left_s, right_s)
                else:
                    distance, found = inorder_beneath(node.right, left_s=left_s)
                    if distance >= 0 and found:
                        distance += 1
                    if distance == k:
                        k_values.add(node.val)
            # Slow part, I don't know how to avoid it,
            # but in the case if we find target in right_subtree of a backtrack node
            # in this case we're already checked it left_subtree, and we need to redo this.
            # This is why, we're recalling check on every left_subtree of a backtrack nodes.
            # The problem this solution raises -> after we end with node in which right_subtree
            # we found a target, this check will be raised for every other node afterward ->
            # because of that it's taking extra time, and checks distance AGAIN.
            # Solution I came up with, is to save everything we added from left_subtree
            # we already checked, and even if we redo this check afterward, distance will be correct
            # but values ignored.
            if node.left and found:
                inorder_beneath(node.left, found, distance + 1, left_s, right_s)
            if found:
                visited.add(node.val)
                return distance, True
            return distance, False
        # if target in right subtree
        if right_s:
            # reading in mirrored in_order BT to find target
            # again, if we find target we're backtracking to find every node
            # on the way back and their left_subtrees -> from target to root.
            if node.right:
                if found:
                    inorder_beneath(node.right, found, distance + 1, left_s, right_s)
                else:
                    distance, found = inorder_beneath(node.right, right_s=right_s)
                    if distance >= 0 and found:
                        distance += 1
                    if distance == k:
                        k_values.add(node.val)
            if node.left:
                if found:
                    inorder_beneath(node.left, found, distance + 1, left_s, right_s)
                else:
                    distance, found = inorder_beneath(node.left, right_s=right_s)
                    if distance >= 0 and found:
                        distance += 1
                    if distance == k:
                        k_values.add(node.val)
            # Same problem, but now -> if we found target inside left_subtree of a node
            # then we need to extra check his right_subtree, because we're already done it before
            # and fixed this with same approach of saving all values in visited.
            # Then, when we will check left_subtree of a ROOT and backtrack nodes, we will ignore all this values,
            # even if they have correct distance from node we're searching from.
            if node.right and found:
                inorder_beneath(node.right, found, distance + 1, left_s, right_s)
            if found:
                visited.add(node.val)
                return distance, True
            return distance, False

    target_subtree: str = target_sub(root)
    if target_subtree == "left":
        inorder_beneath(root, left_s=True)
    else:
        inorder_beneath(root, right_s=True)
    return k_values


# Time complexity: O(n + K * S) -> suppose in the worst case target is the most left leaf in right subtree of a root ->
# n - nodes in input_BT^^| -> then, first we're checking whole BT to find in which subtree it's positioned => O(n) ->
# K - nodes in back_path^^|-> after that we're traversing BT again to find the target and start backtracking from it,
# S - nodes in subtree  ^^|   to find it will cost O(n) and backtrack in this case will be the same O(n),
#      of back_path     ^^|   because we're extra checking every node from target to root and other subtree of the root
#                             and because I didn't succeed in doing this without extra search in right subtrees
#                             of the backtrack_nodes (in case of target on the left side it's left subtrees),
#                             we need to check every right subtree AGAIN, and this one costly O(log n * (n - log n)) ->
#                          -> better to use K <- num of backtrack nodes, S <- num of nodes in its right/left subtree
#                             then for every node on the backtrack_path we're checking it's right/left subtree ->
#                          -> O(K * S), S = (n - log n) where (log n) is K and equal to backtrack_nodes.
#                             ^^Should somewhat correct, hard to calculate more correctly.
#                          => O(n + K * S).
# Auxiliary space: O(log n) -> only values of nodes with correct distance will be stored in 2 extra lists => O(log n).
#                              If we don't ignore recursion_stack -> O(log n) to find target_subtree,
#                              and O(log n) to made search with inorder_beneath() from root => O(3 * log n).
# ---------------------
# Ok. Made it work, but totally need to learn more about BTs. Just to have some extra knowledge.
# It's good experience to make this task on my own, but it's not really needed.
