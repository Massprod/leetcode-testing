# Given the head of a linked list, return the list after sorting it in ascending order.
# --------------------
# The number of nodes in the list is in the range [0, 5 * 10 ** 4].
# -10 ** 5 <= Node.val <= 10 ** 5
# --------------------
# Follow up: Can you sort the linked list in O(n log n) time and O(1) memory (i.e. constant space)?
from random import randint


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


def t_one_linked(to_test: ListNode, testout: list[int]) -> None:
    tempo: ListNode = to_test
    count: int = 0
    for _ in range(len(testout)):
        assert testout[_] == tempo.val
        tempo = tempo.next
        count += 1
    assert count == len(testout)


def sort_list(head: ListNode) -> ListNode:
    # working_sol (74.17%, 37.60%) -> (450ms, 38.8mb)  time: O(n * log n) | space: O(1)
    if not head:
        return head

    def merge_sort(root: ListNode) -> ListNode:
        # We can't divide LinkedList with only 1 Node. And don't need to.
        if not root.next:
            return root
        middle: ListNode = root
        # Node before 'middle' to divide 'root' in 2 parts.
        pre_middle: ListNode = root
        # Standard turtle-hare to find 'middle'.
        fast: ListNode = root
        while fast and fast.next:
            fast = fast.next.next
            pre_middle = middle
            middle = middle.next
        pre_middle.next = None
        # Standard MergeSort.
        left: ListNode = merge_sort(root)
        right: ListNode = merge_sort(middle)
        new_root: ListNode = ListNode(0)
        cursor: ListNode = new_root
        while left and right:
            if left.val < right.val:
                cursor.next = left
                left = left.next
                cursor = cursor.next
            else:
                cursor.next = right
                right = right.next
                cursor = cursor.next
        if left:
            cursor.next = left
        if right:
            cursor.next = right
        return new_root.next

    return merge_sort(head)


# Time complexity: O(n * log n) <- # n - number of Nodes of input LinkedList 'head'.
# Standard MergeSort algorithm takes O(n * log n), and it's copy of it but with search of the current LL middle.
# Auxiliary space: O(1).
# If we ignore recursion stack, and we allowed to do this. Then we're always using already created Nodes of
#  input LL and just reassign them between themselves.
# Only dummy 'new_root' and 'cursor' created, but they don't depend on input.


test: ListNode = create_linked([4, 2, 1, 3])
test_out: list[int] = [1, 2, 3, 4]
t_one_linked(sort_list(test), test_out)

test = create_linked([-1, 5, 3, 4, 0])
test_out = [-1, 0, 3, 4, 5]
t_one_linked(sort_list(test), test_out)

test = create_linked([2, 3, 5, 4])
test_out = [2, 3, 4, 5]
t_one_linked(sort_list(test), test_out)

test_pri: list[int] = [randint(-10 ** 5, 10 ** 5) for _ in range(5 * 10 ** 4)]
# print(test_pri)
test = create_linked(test_pri)
test_pri.sort()
t_one_linked(sort_list(test), test_pri)
