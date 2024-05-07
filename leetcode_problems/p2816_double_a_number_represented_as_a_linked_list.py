# You are given the head of a non-empty linked list representing
#  a non-negative integer without leading zeroes.
# Return the head of the linked list after doubling it.
# ------------------------
# The number of nodes in the list is in the range [1, 10 ** 4]
# 0 <= Node.val <= 9
# The input is generated such that the list represents
#  a number that does not have leading zeros, except the number 0 itself.
from random import randint


class ListNode:
    """
    Create single Node for a linked list.
    """

    def __init__(self, x: int = 0, next: 'ListNode' = None):
        """
        :param x: value of the Node.
        :param next: Node to which it points.
        """
        self.val = x
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked(to_link: list[int]) -> ListNode | None:
    """
    Create linked list.

    :param to_link: values to put into linked list Nodes.
    """
    if not to_link:
        return None
    tempo = link = ListNode()
    for index in range(len(to_link)):
        tempo.val = to_link[index]
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            tempo = tempo.next
    return link


def t_linked(list1: ListNode | None, list2: ListNode | None) -> None:
    """
    Test two linked lists to have same values.
    :param list1: first linked list to test.
    :param list2: second linked list to test.
    :return:
    """
    if not list1 or not list2:
        assert list1 == list2
    while list1 and list2:
        assert list1.val == list2.val
        list1 = list1.next
        list2 = list2.next
    assert list1 == list2


def double_it(head: ListNode) -> ListNode:
    # working_sol (72.46%, 86.07%) -> (230ms, 19.28mb)  time: O(n) | space: O(n)
    all_nodes: list[ListNode] = []
    while head:
        all_nodes.append(head)
        head = head.next
    carry_over: int = 0
    for index in range(len(all_nodes) - 1, -1, -1):
        cur_val: int = (all_nodes[index].val * 2) + carry_over
        # ! 0 <= Node.val <= 9 ! <- so maximum value is `18`
        if 10 <= cur_val:
            carry_over = 1
            all_nodes[index].val = cur_val % 10
        else:
            carry_over = 0
            all_nodes[index].val = cur_val
    if carry_over:
        new_head: ListNode = ListNode(carry_over)
        new_head.next = all_nodes[0]
        return new_head
    return all_nodes[0]


# Time complexity: O(n) <- n - number of Nodes in given `head`.
# We're always store every Node of `head` in `all_nodes` and extra traversing it, once => O(n).
# ------------------------
# Auxiliary space: O(n)
# `all_nodes` always stores all the `head` Nodes => O(n).
# One extra Node and 1 extra INT used => O(n + 1).


test: ListNode = create_linked([1, 8, 9])
test_out: ListNode = create_linked([3, 7, 8])
t_linked(double_it(test), test_out)

test = create_linked([9, 9, 9])
test_out = create_linked([1, 9, 9, 8])
t_linked(double_it(test), test_out)

test_leet: list[int] = [randint(0, 9) for _ in range(10 ** 4)]
print(test_leet)
