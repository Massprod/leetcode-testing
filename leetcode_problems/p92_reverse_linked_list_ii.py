# Given the head of a singly linked list and two integers left and right where left <= right,
#  reverse the nodes of the list from position left to position right, and return the reversed list.
# --------------------
# The number of nodes in the list is n.
# 1 <= n <= 500  ,  -500 <= Node.val <= 500  ,  1 <= left <= right <= n
# --------------------
# Follow up: Could you do it in one pass?


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


def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    # working_sol (89.45%, 99.49%) -> (36ms, 16.3mb)  time: O(n) | space: O(1)
    if (right - left) == 0:
        return head
    all_nodes: list[ListNode] = []
    steps: int = 0
    # Save everything we need to reverse.
    while steps != right:
        all_nodes.append(head)
        head = head.next
        steps += 1
    # Reverse needed slice.
    for x in range(right - 1, left - 2, -1):
        # First node, doesn't have neighbour to reverse.
        if x == 0:
            all_nodes[x].next = None
            continue
        all_nodes[x].next = all_nodes[x - 1]
    # Last node in reverse.
    all_nodes[left - 1].next = head
    # If something present before last node,
    #  then we're changing part of the original list.
    if left - 2 >= 0:
        all_nodes[left - 2].next = all_nodes[right - 1]
        return all_nodes[0]
    # Otherwise it was full list reverse.
    return all_nodes[-1]


# Time complexity: O(n) -> worst case we're having full reverse constraints, so we will traverse whole linked list
# n - nodes of input_list^^| to store nodes, and second time to reassign them => O(2n)
# Auxiliary space: O(1) -> because we're using only links of original linked_list we can call it constant => O(1).
#                          ^^At least this is how Leetcode treated recursions when dealing with links.
# --------------------
# Ok. Made this with recreating of Nodes when we actually need to ->
# -> ! reverse the nodes of the list from position left to position right, and return the reversed list. !
# So it's correct and accepted, but if we follow description more accurate, then we can't rebuild Nodes.
# We need to reverse existed Nodes. Change to use Nodes only.
# Failed with recursion, dunno it's really hard to maintain start, end Nodes at some cases.


test: ListNode = create_linked([1, 2, 3, 4, 5])
test_left: int = 2
test_right: int = 4
test_out: ListNode = create_linked([1, 4, 3, 2, 5])
t_linked(reverse_between(test, test_left, test_right), test_out)

test = create_linked([5])
test_left = 1
test_right = 1
test_out = create_linked([5])
t_linked(reverse_between(test, test_left, test_right), test_out)

test = create_linked([1, 4, 5, 2, 1, 1, 1, 2, 2])
test_left = 4
test_right = 5
test_out = create_linked([1, 4, 5, 1, 2, 1, 1, 2, 2])
t_linked(reverse_between(test, test_left, test_right), test_out)

test = create_linked([3, 5])
test_left = 1
test_right = 2
test_out = create_linked([5, 3])
t_linked(reverse_between(test, test_left, test_right), test_out)

test = create_linked([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test_left = 9
test_right = 10
test_out = create_linked([1, 2, 3, 4, 5, 6, 7, 8, 10, 9])
t_linked(reverse_between(test, test_left, test_right), test_out)

test = create_linked([1, 2, 3])
test_left = 1
test_right = 2
test_out = create_linked([2, 1, 3])
t_linked(reverse_between(test, test_left, test_right), test_out)
