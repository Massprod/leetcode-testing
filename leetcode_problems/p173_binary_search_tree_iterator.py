# Implement the BSTIterator class that represents an iterator over
#   the in-order traversal of a binary search tree (BST):
#    1) BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
#        The root of the BST is given as part of the constructor.
#        The pointer should be initialized to a non-existent number smaller than any element in the BST.
#    2) boolean hasNext() Returns true if there exists a number in the traversal
#        to the right of the pointer, otherwise returns false.
#    3) int next() Moves the pointer to the right, then returns the number at the pointer.
#
# Notice that by initializing the pointer to a non-existent smallest number,
#   the first call to next() will return the smallest element in the BST.
# You may assume that next() calls will always be valid.
# That is, there will be at least a next number in the in-order traversal when next() is called.
# -------------------
# The number of nodes in the tree is in the range [1, 10 ** 5].
# 0 <= Node.val <= 10 ** 6
# At most 10 ** 5 calls will be made to hasNext, and next.
# -------------------
# Follow up:
# Could you implement next() and hasNext() to run in average O(1) time
#   and use O(h) memory, where h is the height of the tree?
from typing import Iterator
from itertools import tee


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    # working_sol (70.1%, 70.23%) -> (84ms, 22.6mb)

    def __init__(self, root: TreeNode):

        def inorder(node: TreeNode) -> Iterator[int]:
            # standard inorder, but with yield
            if not node.left and not node.right:
                yield node.val
                return
            if node.left:
                yield from inorder(node.left)
            yield node.val
            if node.right:
                yield from inorder(node.right)

        gen: Iterator[int] = inorder(root)
        self.gen_peek, self.gen_copy = tee(gen, 2)
        # count for hasNext
        self.checked_nodes: int = 1
        # count for next
        self.called_nodes: int = 0

    def next(self):
        # checked_nodes maintain (last possible node + 1)
        if self.called_nodes < self.checked_nodes:
            try:
                next(self.gen_peek)
                self.checked_nodes += 1
            except StopIteration:
                pass
            self.called_nodes += 1
        return next(self.gen_copy)

    def hasNext(self):
        try:
            next(self.gen_peek)
            self.checked_nodes += 1
            return True
        except StopIteration:
            # we can call hasNext more than next and ever first,
            # than it's going to raise and to escape it
            # comparing with actually called_nodes(next)
            if self.called_nodes < self.checked_nodes - 1:
                return True
            return False


# Time complexity:
#      Initiation: O(1) -> didn't found is tee() actually O(1) or it's deepcopy with linear time,
#                          but if we assume we do 2 copies in constant time then there's nothing else => O(1).
#      next: O(log n) -> every call to a Generator continues in-order traverse,
#                        and we proceed only part of the BT => O(log n) -> in our case we're calling 2 times ->
#                     -> because we need to maintain info about BT having nodes unvisited => O(log n) -> O(2 * log n).
#      hasNext: O(log n) -> same approach as next, but now we're calling Generator once => O(log n).
# Auxiliary space:
#      Initiation: O(1) -> creating 2 extra INTs, and 2 copies of Generator, none of this depends on input => O(1).
#      next: O(n) -> in the worst case with unbalanced tree, every node on the path will be equal to all BT nodes,
#                    so recursion stack will be a size of n => O(n).
#                    ^^Should I include this into init? Need to learn more about where Generator is stored,
#                      because function will operate with links from input BT, and we're not copying it.
#                      But Generator itself, and it's recursion how we calculate it?
#                      This all should be stored in object, and we just call next() on it.
#      hasNext: O(n) -> same logic with recursion => O(n).
#                       ^^Doubt it's correctness, revisit after learn more.
# -------------------
# Follow up is actually should be the same if we assume that, Generator calls will be the same as number of Node.
# Because in this case we're just delaying execution, and we can in-order traverse BT on initiation.
# Then store every node in a que or list and return them one by one.
# But if we're not calling next() same time as number of Nodes in BT, then it's going to be a waste.
# W.e it's too easy to rebuild, leaving it like this.
# My goal was to successfully make Generator with correct returns.
# -------------------
# Well, extra checked Generator, and I was correct it's just continues execution.
# So first call for a next() will lead recursion for a first left_most leaf,
# and stops, every call just continues it -> standard recursion is O(n) cuz we're just traversing
# through all nodes of BT. Can we call Generator constant in this case?
# I guess it's not and there's no extra on it for now.
# Because if other leaf is 3-4 nodes away, it's not constant it's logarithmic.
# -------------------
# Super easy task if we just in-order traverse on initiation and return either from deque,
# or simple list with saving index. But it can't be a task like this.
# Guess it's actually task to create Generator for in-order traverse, but in this case how
# we can do follow_up? Because everytime we will call next() it's just going to continue execution,
# and return next node in correct in-order way.
# I will make Generator first, and try to just read and return from saved data after.
# Because we're not blocked from saving whole in-order path, in BSTIterator object.
# Then initiation will be a costly, but next() and hasNext() constant.


# Debugger purposes:
def build_tree(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    # working_sol (22.55%, 9.94%) -> (216ms, 91.6mb)  time: O(n ** 2) | space: O(n)
    if not inorder and not postorder:
        return None
    # postorder root is last index
    root: TreeNode = TreeNode(val=postorder[-1])
    # find root position
    in_order_index: int = inorder.index(root.val)
    # divide left/right subtrees by ROOT in inorder
    left_subtree: list[int] = inorder[: in_order_index]
    right_subtree: list[int] = inorder[in_order_index + 1:]
    # divide left/right subtrees by ROOT in postorder
    postorder_left_subtree: list[int] = postorder[:len(left_subtree)]
    postorder_right_subtree: list[int] = postorder[len(left_subtree):-1]
    # go deeper, and build with backtrack path
    root.left = build_tree(left_subtree, postorder_left_subtree)
    root.right = build_tree(right_subtree, postorder_right_subtree)
    return root


test1_in = [9, 3, 15, 20, 7]
test1_post = [9, 15, 7, 20, 3]
test1_out = [3, 9, 20, None, None, 15, 7]
test = build_tree(test1_in, test1_post)

print("Test:")
itest = BSTIterator(test)
print(itest.next(), itest.next(), itest.hasNext(), itest.hasNext())
