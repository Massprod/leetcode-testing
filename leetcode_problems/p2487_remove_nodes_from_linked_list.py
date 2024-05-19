# You are given the head of a linked list.
# Remove every node which has a node with a greater value anywhere to the right side of it.
# Return the head of the modified linked list.
# --------------------------
# The number of the nodes in the given list is in the range [1, 10 ** 5].
# 1 <= Node.val <= 10 ** 5
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


def remove_nodes(head: ListNode) -> ListNode:
    # working_sol (57.89%, 90.29%) -> (420ms, 51.06mb)  time: O(n) | space: O(n)
    stack: list[ListNode] = []
    while head:
        while stack and stack[-1].val < head.val:
            node: ListNode = stack.pop()
            node.next = None
            if stack:
                stack[-1].next = head
        stack.append(head)
        head = head.next
    return stack[0]


# Time complexity: O(n) <- n - number of Nodes in input LinkedList `head`.
# The worst case, there's only the last Node with the Highest value.
# So, we will traverse (n - 1) Nodes and store them in `stack`, after that we're going to
#  traverse the whole `stack` to delete everything and leave the last node => O(2n).
# --------------------------
# Auxiliary space: O(n)
# The worst case, there's only descending Nodes.
# We will allocate space for each of them in `stack` => O(n).


test: ListNode = create_linked([5, 2, 13, 3, 8])
test_out: ListNode = create_linked([13, 8])
t_linked(remove_nodes(test), test_out)

test = create_linked([1, 1, 1, 1])
test_out = create_linked([1, 1, 1, 1])
t_linked(remove_nodes(test), test_out)

test_leet: list[int] = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
print(test_leet)
