# Given the head of a linked list, we repeatedly delete consecutive sequences
#  of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.
# You may return any such answer.
# ----------------------------
# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.


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


def remove_zero_sum(head: ListNode) -> ListNode:
    # working_sol (76.49%, 89.64%) -> (40ms, 16.79mb)  time: O(n) | space: O(n)
    prefixes: dict[int, ListNode] = {}
    prefix: int = 0
    first: ListNode = ListNode(0, head)
    last: ListNode = first
    while last:
        prefix += last.val
        if prefix in prefixes:
            delete: ListNode = prefixes[prefix]
            last = delete.next
            pre: int = prefix + last.val
            while pre != prefix:
                del prefixes[pre]
                last = last.next
                pre += last.val
            delete.next = last.next
        else:
            prefixes[prefix] = last
        last = last.next
    return first.next


# Time complexity: O(n) <- n - number of Nodes inside the input LinkedList `head`.
# Worst case: we will delete everything.
# So, we will visit every Node twice.
# ----------------------------
# Auxiliary space: O(n)
# Worst case: we will store every Node prefix inside `prefixes`.


test: ListNode = create_linked([1, 2, -3, 3, 1])
test_out: ListNode = create_linked([3, 1])
t_linked(remove_zero_sum(test), test_out)

test = create_linked([1, 2, 3, -3, 4])
test_out = create_linked([1, 2, 4])
t_linked(remove_zero_sum(test), test_out)

test = create_linked([1, 2, 3, -3, -2])
test_out = create_linked([1])
t_linked(remove_zero_sum(test), test_out)
