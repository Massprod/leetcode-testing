# Given the head of a singly linked list where elements are sorted in ascending order,
#   convert it to a height-balanced binary search tree.
# -----------------
# The number of nodes in head is in the range [0, 2 * 10 ** 4].
# -10 ** 5 <= Node.val <= 10 ** 5
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked(to_link: list[int]) -> ListNode:
    tempo = link = ListNode()
    for index in range(len(to_link)):
        tempo.val = to_link[index]
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            tempo = tempo.next
    return link


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def show_tree_level_order(root: TreeNode) -> list[int | None]:
    if not root:
        return []
    show_tree: list[int | None] = []
    que: deque = deque()
    que.appendleft(root)
    # if there's only None left, then it's last level, and we have nothing to check
    # any() <- checks everything in iterable and if there's no elements we break.
    # any() used to eliminate extra level with nulls, when que is empty,
    #       and still store Nulls for other levels.
    while any(que):
        current_node: TreeNode = que.popleft()
        if current_node is None:
            show_tree.append(None)
            continue
        show_tree.append(current_node.val)
        que.append(current_node.left)
        que.append(current_node.right)

    return show_tree


def sorted_linked_list_to_bst(head: ListNode) -> TreeNode | None:
    # working_sol (93.45%, 90.96%) -> (127ms, 20.1mb)  time: O(n * log n) | space: O(log n)
    if not head:
        return None
    # if only 1 node left, it's only option to assign as leaf
    if not head.next:
        return TreeNode(val=head.val)
    # standard Floyd
    slow: ListNode | None = head
    fast: ListNode = head
    # we need to break linked list on the middle node
    rem_mid: ListNode | None = None
    while fast and fast.next:
        rem_mid = slow
        slow = slow.next
        fast = fast.next.next
    # break linked
    rem_mid.next = None
    root: TreeNode = TreeNode(val=slow.val)
    root.left = sorted_linked_list_to_bst(head)
    root.right = sorted_linked_list_to_bst(slow.next)
    return root


# Time complexity: O(n * log n) -> always taking middle, so it's always height-balanced tree ->
# n - nodes in input_list^^| -> for every recursion call we will extra traverse halves of input_linked_list,
#                            so O(n) calls and inside recursion we extra traverse changing linked_list of median
#                            sizes (log n) => O(n * log n).
# Auxiliary space: O(log n) -> we're not creating linked_lists and operating only with their links,
#                              stack of recursion for height-balance BT will be O(log n).
# -----------------
# Same task as p108, but now I just need to traverse linked list and find it's middle.
# Or we can just rebuild linked_list into a list, don't think it's a good idea and better to read it.
# As always hare + turtle(Floyd).


test1 = create_linked([-10, -3, 0, 5, 9])
test1_out = [0, -3, 9, -10, None, 5]
test = sorted_linked_list_to_bst(test1)
print(show_tree_level_order(test))
assert test1_out == show_tree_level_order(test)
del test

test2 = []
test2_out = []
test = sorted_linked_list_to_bst(test2)
print(show_tree_level_order(test))
assert test2_out == show_tree_level_order(test)
del test
