# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
# --------------------------
# 3 <= list1.length <= 10 ** 4
# 1 <= a <= b < list1.length - 1
# 1 <= list2.length <= 10 ** 4


class ListNode:
    """
    Create a single Node for a linked list.
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
    Create a linked list.

    :param to_link: Values to put into linked list Nodes.
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
    :param list1: First linked list to test.
    :param list2: Second linked list to test.
    :return:
    """
    if not list1 or not list2:
        assert list1 == list2
    while list1 and list2:
        assert list1.val == list2.val
        list1 = list1.next
        list2 = list2.next
    assert list1 == list2


def merge_in_between(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    # working_sol (85.82%, 31.60%) -> (184ms, 21.15mb)  time: O(n + m) | space: O(1)
    out: ListNode = list1
    # The First Node we need to connect to `list2`
    first_1: ListNode | None = None
    # The Last Node we need to connect with the end of `list2`.
    last_1: ListNode | None = None
    # Number of Nodes we need to delete.
    to_delete: int = b + 1 - a
    # The First and Last Nodes we need to place in `list1`.
    first_2: ListNode = list2
    while list2.next:
        list2 = list2.next
    last_2: ListNode = list2
    while list1:
        a -= 1
        if 0 == a:
            first_1 = list1
            break
        list1 = list1.next
    while to_delete:
        list1 = list1.next
        to_delete -= 1
    last_1 = list1.next
    first_1.next = first_2
    last_2.next = last_1
    return out


# Time complexity: O(n + m) <- n - Number of Nodes in `list1`, m - Number of Nodes in `list2`.
# In the worst case, we will traverse whole `list1` and we're always traversing whole `list2` to get last Node.
# --------------------------
# Auxiliary space: O(1)
# Nothing extra which depends on input, we're only operating with Links of the input LinkedLists `list1` and `list2`.
# Only 1 extra INT `to_delete`.


test_1: ListNode = create_linked([10, 1, 13, 6, 9, 5])
test_a: int = 3
test_b: int = 4
test_2: ListNode = create_linked([1000000, 1000001, 1000002])
test_out: ListNode = create_linked([10, 1, 13, 1000000, 1000001, 1000002, 5])
t_linked(test_out, merge_in_between(test_1, test_a, test_b, test_2))

test_1 = create_linked([0, 1, 2, 3, 4, 5, 6])
test_a = 2
test_b = 5
test_2 = create_linked([1000000, 1000001, 1000002, 1000003, 1000004])
test_out = create_linked([0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6])
t_linked(test_out, merge_in_between(test_1, test_a, test_b, test_2))
