# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#   k is a positive integer and is less than or equal to the length of the linked list.
#   If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# -------------------------------
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# -------------------------------
# Follow-up: Can you solve the problem in O(1) extra memory space?


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


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    # working_sol (83.33%, 62.9%) -> (47ms, 17.5mb)  time: O(n) | space: O(k)
    if not head:
        return head
    if k == 1:
        return head
    step: int = 1
    # First Node in new k-th group.
    first_in_new: ListNode = head
    path: list[ListNode] = [first_in_new]
    new_head: ListNode | None = None
    # Last Node in previous k-th group we need to link with new group.
    # Initially we don't have previous group == None.
    last_in_prev: ListNode | None = None
    while first_in_new and first_in_new.next:
        if step < k:
            step += 1
            first_in_new = first_in_new.next
            path.append(first_in_new)
        if step == k:
            first_in_new: ListNode = first_in_new.next
            # First reversed node of all == new_head.
            if not new_head:
                new_head = path[-1]
            for x in range(len(path) - 1, 0, -1):
                path[x].next = path[x - 1]
            if last_in_prev:
                last_in_prev.next = path[-1]
            last_in_prev = path[0]
            last_in_prev.next = first_in_new
            path.clear()
            step = 1
            path.append(first_in_new)
    return new_head


# Time complexity: O(n) -> essentially we're using every Node twice: first to add into a path, and second
# n - Node of input linked list^^|  to reassign them between => O(2n).
# Auxiliary space: O(1) -> path size is always equal to 'k' => O(k).
# k - input value 'k'^^|  Don't know if we can call it constant, because we're storing them in a list.
#                         But even LeetCode different tasks never consider recursion stacks
#                          as extra space for linked lists. List is similar, so might be O(1).
# -------------------------------
# Rebuilding with the same approach, but less cluster_###k.
# Read 'k' nodes -> reverse them between -> reassign last in previous group to a first in new group ->
#  -> reassign last in new group to a next possible group <- Repeat.


test: ListNode = create_linked([1, 2, 3, 4, 5])
test_k: int = 2
test_out: ListNode = create_linked([2, 1, 4, 3, 5])
t_linked(test_out, reverse_k_group(test, test_k))

test = create_linked([1, 2, 3, 4, 5])
test_k = 3
test_out = create_linked([3, 2, 1, 4, 5])
t_linked(test_out, reverse_k_group(test, test_k))

test = create_linked([1, 2])
test_k = 2
test_out = create_linked([2, 1])
t_linked(test_out, reverse_k_group(test, test_k))
